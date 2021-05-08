|pulsar-queue|

:Badges: |license|  |pyversions| |status| |pypiversion|
:CI: |circleci| |coverage| |appveyor|
:Downloads: http://pypi.python.org/pypi/pulsar-queue
:Source: https://github.com/quantmind/pulsar-queue
:Mailing list: `google user group`_
:Design by: `Quantmind`_ and `Luca Sbardella`_
:Platforms: Linux, OSX, Windows. Python 3.5 and above
:Keywords: server, asynchronous, concurrency, actor, process, queue, tasks, redis


.. |pypiversion| image:: https://badge.fury.io/py/pulsar-queue.svg
  :target: https://pypi.python.org/pypi/pulsar-queue
.. |pyversions| image:: https://img.shields.io/pypi/pyversions/pulsar-queue.svg
  :target: https://pypi.python.org/pypi/pulsar-queue
.. |license| image:: https://img.shields.io/pypi/l/pulsar-queue.svg
  :target: https://pypi.python.org/pypi/pulsar-queue
.. |status| image:: https://img.shields.io/pypi/status/pulsar-queue.svg
  :target: https://pypi.python.org/pypi/pulsar-queue
.. |downloads| image:: https://img.shields.io/pypi/dd/pulsar-queue.svg
  :target: https://pypi.python.org/pypi/pulsar-queue
.. |travis| image:: https://img.shields.io/travis/quantmind/pulsar-queue/master.svg
  :target: https://travis-ci.org/quantmind/pulsar-queue
.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/7us462jl0de2w0ly/branch/master?svg=true
    :target: https://ci.appveyor.com/project/lsbardel/pulsar-queue
.. |coverage| image:: https://codecov.io/gh/quantmind/pulsar-queue/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/quantmind/pulsar-queue
.. |circleci| image:: https://circleci.com/gh/quantmind/pulsar-queue.svg?style=svg
    :target: https://circleci.com/gh/quantmind/pulsar-queue

Asynchronous server for consuming asynchronous IO tasks, green IO tasks,
blocking IO tasks and long running CPU bound tasks.

* Fully configurable
* Consumers poll tasks from distributed message brokers (redis broker implemented)
* Publish/subscribe for real-time event and logging (redis pub/sub backend)
* Can schedule tasks when run as a scheduler (``--schedule-periodic`` flag)
* Build on top of pulsar_ and asyncio_


TL;DR
========

Clone the repository::

    git clone git@github.com:quantmind/pulsar-queue.git


Move to the ``tests/example`` directory and run the server::

    python manage.py



.. contents:: **CONTENTS**


Four steps tutorial
========================

1 - Create a script
----------------------

A simple python file which runs your application:

.. code::

    vim manage.py


.. code:: python

    from pq.api import PulsarQueue


    task_paths = ['sampletasks.*', 'pq.jobs']


    def app():
        return PulsarQueue(config=__file__)

    if __name__ == '__main__':
        app().start()


2 - Implement Jobs
---------------------

Create the modules where Jobs_ are implemented.
It can be a directory containing several submodules.

.. code::

    mkdir sampletasks
    cd sampletasks
    vim mytasks.py

.. code:: python

    import asyncio
    import time

    from pq import api


    @api.job()
    def addition(self, a=0, b=0):
        return a + b


    @api.job()
    async def asynchronous(self, lag=1):
        start = time.time()
        await asyncio.sleep(lag)
        return time.time() - start


3 - Run the server
---------------------

Run the server with two task consumers (pulsar actors).

**NOTE**: Make sure you have Redis server up and running before you start the server.

.. code::

    python manage.py -w 2

4 - Queue tasks
---------------------

Launch a python shell and play with the api

.. code:: python

    >>> from manage import app
    >>> api = app().api()
    >>> task = api.tasks.queue('addition', a=4, b=6)
    >>> task
    <TaskFuture pending ID=i26ad5c14c5bb422e87b0f7ccbce5ba06>
    >>> task = task.wait()
    task.addition<i24ab99ddf2744902a375e039790dcbc4><SUCCESS>
    >>> task.result
    10
    >>> task.status_string
    'SUCCESS'

You can also queue tasks with a ``delay``

.. code:: python

    >>> task = api.tasks.queue('addition', a=4, b=6, callback=False, delay=2).wait()
    >>> task.status_string
    'QUEUED'
    >>> task.time_queued    # timestamp
    >>> task = task.done_callback.wait()
    >>> task.status_string
    'SUCCESS'
    >>> task.time_started - task.time_queued
    2.00

**NOTE**: The ``wait`` method in a task future can only be used on the shell
or when the event loop is not running. In all other cases one should ``await``
for the task future in a coroutine.

API
=============

The producer API is obtained from the Task application ``api`` method:

.. code:: python

    from pq.api import PusarQueue

    api = PusarQueue(...).api()


API methods
---------------

*api*.start()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Start listening to events. This method return a coroutine which resolve in the api:

.. code:: python

    api = await api.start()

The start method is used when the api is used by application to queue messages/tasks
and listen for events published by distributed consumers.

*api*.on_events(*message_type*, *event_re*, *callback*)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add a callback invoked every time an event matching the regular expression ``event_re``
occurs on the ``message_type`` channel. The *callback* has the following signature:

.. code:: python

    def event_callback(channel, event, message):
        # event is string, the event matched
        # message is of type message_type

If the event is a task event (see events_) the message is a Task_ object.

This method is useful when creating applications which needs to respond to the
queue server events in real time::

    api.on_events('task', 'queued', callback)
    api.on_events('task', 'started', callback)
    api.on_events('task', 'done', callback)


*api*.remove_event_callback(*message_type*, *event_re*, *callback*)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove a previously added event callback. This method is safe.

*api*.queue(*message*, *callback=True*)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Queue a message in the message queue, equivalent to:

.. code:: python

    api.broker.queue(message, callback)

This method returns a ``MessageFuture``, a subclass of asyncio Future_ which
resolves in a ``message`` object.
If ``callback`` is True (default) the Future is resolved once the message
is delivered (out of the queue), otherwise is is resolved once the message
is queued (entered the queue).

*api*.execute(*message*)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Execute a message without queueing. This is only supported by messages with
a message consumer which execute them (the ``tasks`` consumer for example).
If *message* is a Task_, this method is equivalent to:

.. code:: python

    api.tasks.execute(task)

This method returns a ``MessageFuture``, a subclass of asyncio Future_ which
resolve in a ``message`` object.

*api*.consumers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

List of consumers registered with the api.

Tasks API
-----------------

The tasks producer is obtained vua the ``tasks`` property from the producer API instance

.. code:: python

    tasks = api.tasks

The following methods are available for the tasks producer:


*tasks*.queue(*jobname*, *\*\*kwargs*)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Queue a task and return a **TaskFuture** which is resolved once the task has finished.
It is possible to obtain a task future resolved when the task has been queued, rather than finished, by passing the **callback=False** parameter:

.. code:: python

    task = await tasks.queue(..., callback=False)
    task.status_string  # QUEUED

The ``kwargs`` parameters are used as input parameters for the Job_ callable with the exception of:

* ``callback``: discussed above
* ``delay``: delay execution by a given number of seconds
* ``queue``: overrides the Job_ [default_queue](#job-default-queue)
* [timeout](#job-timeout)
* ``meta_params``: dictionary of parameters used by the Job_ callable to override default values of:
  * [max_retries](#job-max-retries)
  * [retry_delay](#job-retry-delay)
  * [max_concurrency](#job-max-concurrency)

*tasks*.queue_local(*jobname*, *\*\*kwargs*)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Queue a job in the local task queue. The local task queue is processed by the same server instance. It is equivalent to execute:

.. code:: python

    task = await tasks.queue(..., queue=tasks.node_name)
    task.queue  # tasks.node_name


*tasks*.execute(*jobname*, *\*args*, *\*\*kwargs*)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Execute a task immediately, it does not put the task in the task queue.
This method is useful for debugging and testing. It is equivalent to execute:

.. code:: python

    task = await tasks.queue(..., queue=False)
    task.queue          # None
    task.status_string  # SUCCESS


*tasks*.queues()
~~~~~~~~~~~~~~~~~~~~~~~~

Return the list of queue names the backend is subscribed. This list is not empty when the backend is a task consumer.

*tasks*.job_list(*jobname=None*)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Returns a list of ``job_name``, ``job_description`` tuples. The ``job_name`` is a string which must be used as the **jobname** parameter when executing or queing tasks. The ``job_description`` is a dictionary containing metadata and documentation for the job. Example:

.. code:: python

    jobs = dict(tasks.job_lits())
    jobs['execute.python']
    # {
    #   'type': 'regular',
    #   'concurrency': 'asyncio',
    #   'doc_syntax': 'markdown',
    #   'doc': 'Execute arbitrary python code on a subprocess ... '
    # }


The Job class
-----------------

The **Job** class is how task factories are implemented and added to the
tasks backend registry. When writing a new **Job** one can either subclass:

.. code:: python

    import asyncio

    class AsyncSleep(api.Job):

        async def __call__(self, lag=1):
            await asyncio.sleep(lag)


or use the less verbose **job** decorator:

.. code:: python

    @api.job()
    async def asyncsleep(self, lag=1):
        await asyncio.sleep(lag)


In either cases the ``self`` parameter is an instance of a **Job** class and
it has the following useful attributes and methods:

*job*.backend
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The tasks backend that is processing this Task_ run

*job*.default_queue
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The default queue name where tasks for this job are queued. By default it is ``None``
in which case, if a ``queue`` is not given when queueing a task, the first queue
from the `queues <#tasks_queues>`_ list taken.

*job*.http
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Best possible HTTP session handler for the job concurrency mode.

*job*.logger
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Python logging handler for this job. The name of this handler
is ``<app_name>.<job.name>``.

*job*.max_retries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Optional positive integer which specify the maximum number of retries when a
task fails or is revoked. If not available failing tasks are not re-queued.
It can be specified as a class attribute or during initialisation from the task
meta parameters.

*job*.retry_delay
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Optional positive integer which specifies the number of seconds to delay a task
retry.

*job*.name
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The name of this job. Used to queue tasks

*job*.task
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Task_ instance associated with this task run

*job*.queue(*jobname*, *\*args*, *\*\*kwargs*)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Queue a new job form a task run. It is equivalent to:

.. code:: python

    meta_params = {'from_task': self.task.id}
    self.backend.tasks.queue(..., meta_params=meta_params)


*job*.shell(*command*, *\*\*kwargs*)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Execute a shell command and returns a coroutine:

.. code:: python

    await self.shell("...")


The Task
-----------

A task contains the metadata information of a job run and it is exchanged between task producers and task consumers via a distributed task queue.


Task States
-----------------

A Task_ can have one of the following ``task.status``:

* ``QUEUED = 6`` a task queued but not yet executed.
* ``STARTED = 5`` a task where execution has started.
* ``RETRY = 4`` a task is retrying calculation.
* ``REVOKED = 3`` the task execution has been revoked (or timed-out).
* ``FAILURE = 2`` task execution has finished with failure.
* ``SUCCESS = 1`` task execution has finished with success.


**FULL_RUN_STATES**

The set of states for which a Task_ has run: ``FAILURE`` and ``SUCCESS``


**READY_STATES**

The set of states for which a Task_ has finished: ``REVOKED``, ``FAILURE`` and ``SUCCESS``

Events
-------------

The task queue broadcast several events during task execution and internal state:

* ``task_queued``: a new Task_ has been queued, the message is a task instance
* ``task_started``: a Task_ has started to be consumed by a task consumer, it is out of the task queue
* ``task_done``: a Task_ is done, the message is a task in a **READY_STATES**


Configuration
------------------

There are several parameters you can use to twick the way the task queue works.
In this list the name in bold is the entry point in the config file and **cfg**
dictionary, while, the value between brackets shows the command line entry with default
value.

* **concurrent_tasks** (``--concurrent-tasks 5``)

    The maximum number of concurrent tasks for a given worker in a task consumer server.

* **data_store** (``--data-store redis://127.0.0.1:6379/7``)

    Data store used for publishing and subscribing to messages (redis is the
    only backend available at the moment)

* **max_requests** (``--max-requests 0``)

    The maximum number of tasks a worker will process before restarting.
    A 0 value (the default) means no maximum number, workers will process
    all tasks forever.

* **message_broker** (``--message-broker ...``)

    Data store used as distributed task queue. If not provided (default) the
    ``data_store`` is used instead. Redis is the
    only backend available at the moment.

* **message_serializer** (``--message-serializer json``)

    The decoder/encoder for messages and tasks. The default is **JSON** but **Message Pack**
    is also available if msgpack_ is installed.

* **schedule_periodic** (``--schedule-periodic``)

    When ``True``, the task application can schedule periodic Jobs_.
    Usually, only one running server is responsible for
    scheduling tasks.

* **task_pool_timeout** (``--task-pool-timeout 2``)

    Timeout in seconds for asynchronously polling tasks from the queues. No need to change this parameter really.

* **workers** (``--workers 4``)

    Number of workers (processes) consuming tasks.


Tasks Concurrency
======================

A task can run in one of four ``concurrency`` modes.
If not specified by the ``Job``, the concurrency mode is ``ASYNC_IO``.

ASYNC_IO
-----------

The asynchronous IO mode is associated with tasks which return
an asyncio Future or a coroutine. These tasks run concurrently
in the worker event loop.
An example can be a Job to scrape web pages and create new tasks to process the html

.. code:: python

    @api.job()
    async def scrape(self, url=None):
        assert url, "url is required"
        request = await self.http.get(url)
        html = request.text()
        task = self.queue('process.html', html=html, callback=False)
        return task.id


THREAD_IO
-------------

This concurrency mode is best suited for tasks performing
*blocking* IO operations.
A ``THREAD_IO`` job runs its tasks in the event loop executor.
You can use this model for most blocking operation unless

* Long running CPU bound
* The operation does not release the GIL

Example of tasks suitable for thread IO are IO operations on files.
For example the test suite uses this Job for testing ``THREAD_IO``
concurrency (check the ``tests.example.jobs.standard`` module
for the full code):


.. code:: python

    @api.job(concurrency=api.THREAD_IO)
    def extract_docx(self, input=None, output=None):
        """
        Extract text from a docx document
        """
        import docx
        assert input and output, "input and output must be given"
        document = docx.Document(input)
        text = '\n\n'.join(_docx_text(document))
        with open(output, 'w') as fp:
            fp.write(text)
        return {
            'thread': threading.get_ident(),
            'text': len(text)
        }

CPUBOUND
------------

It assumes the task performs blocking CPU bound operations.
Jobs with this consurrency mode run their tasks on sub-processeses
using `asyncio subprocess`_ module.

Extend
=================

It is possible to enhance the task queue application by passing
a custom ``Manager`` during initialisation.
For example:

.. code:: python

    from pq import api

    class Manager(api.Manager):

        async def store_message(self, message):
            """This method is called when a message/task is queued,
            started and finished
            """
            if message.type == 'task':
                # save this task into a db for example

        def queues(self):
            """List of queue names for Task consumers
            By default it returns the node name and the task_queues
            in the config dictionary.
            """
            queues = [self.backend.node_name]
            queues.extend(self.cfg.task_queues)
            return queues


    tq = PulsarQueue(Manager, ...)


The ``Manager`` class is initialised when the backend handler is initialised
(on each consumer and in the scheduler).

Changelog
==============

* `Versions 0.5 <https://github.com/quantmind/pulsar-queue/blob/master/docs/history/0.5.md>`_
* `Versions 0.4 <https://github.com/quantmind/pulsar-queue/blob/master/docs/history/0.4.md>`_
* `Versions 0.3 <https://github.com/quantmind/pulsar-queue/blob/master/docs/history/0.3.md>`_
* `Versions 0.2 <https://github.com/quantmind/pulsar-queue/blob/master/docs/history/0.2.md>`_
* `Versions 0.1 <https://github.com/quantmind/pulsar-queue/blob/master/docs/history/0.1.md>`_

License
=============
This software is licensed under the BSD 3-clause License. See the LICENSE
file in the top distribution directory for the full license text. Logo designed by Ralf Holzemer,
`creative common license`_.


.. _`google user group`: https://groups.google.com/forum/?fromgroups#!forum/python-pulsar
.. _`Luca Sbardella`: http://lucasbardella.com
.. _`Quantmind`: http://quantmind.com
.. _`creative common license`: http://creativecommons.org/licenses/by-nc/3.0/
.. _pulsar: https://github.com/quantmind/pulsar
.. _asyncio: https://docs.python.org/3/library/asyncio.html
.. _greenlet: https://greenlet.readthedocs.io/en/latest/
.. _msgpack: https://pypi.python.org/pypi/msgpack-python
.. _`asyncio subprocess`: https://docs.python.org/3/library/asyncio-subprocess.html
.. _Future: https://docs.python.org/3/library/asyncio-task.html#future
.. _Job: #the-job-class
.. _Jobs: #the-job-class
.. _Task: #the-task
.. _Events: #events
.. _events: #events
.. |pulsar-queue| image:: https://fluidily-public.s3.amazonaws.com/pulsar/queue/pulsar-queue-banner.svg
   :target: https://github.com/quantmind/pulsar-queue
