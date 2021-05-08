Asynchronous Python HTTP Requests for Humans
============================================

.. image:: https://travis-ci.org/ross/requests-futures.png?branch=master
        :target: https://travis-ci.org/ross/requests-futures

Small add-on for the python requests_ http library. Makes use of python 3.2's
`concurrent.futures`_ or the backport_ for prior versions of python.

The additional API and changes are minimal and strives to avoid surprises.

The following synchronous code:

.. code-block:: python

    from requests import Session

    session = Session()
    # first requests starts and blocks until finished
    response_one = session.get('http://httpbin.org/get')
    # second request starts once first is finished
    response_two = session.get('http://httpbin.org/get?foo=bar')
    # both requests are complete
    print('response one status: {0}'.format(response_one.status_code))
    print(response_one.content)
    print('response two status: {0}'.format(response_two.status_code))
    print(response_two.content)

Can be translated to make use of futures, and thus be asynchronous by creating
a FuturesSession and catching the returned Future in place of Response. The
Response can be retrieved by calling the result method on the Future:

.. code-block:: python

    from requests_futures.sessions import FuturesSession

    session = FuturesSession()
    # first request is started in background
    future_one = session.get('http://httpbin.org/get')
    # second requests is started immediately
    future_two = session.get('http://httpbin.org/get?foo=bar')
    # wait for the first request to complete, if it hasn't already
    response_one = future_one.result()
    print('response one status: {0}'.format(response_one.status_code))
    print(response_one.content)
    # wait for the second request to complete, if it hasn't already
    response_two = future_two.result()
    print('response two status: {0}'.format(response_two.status_code))
    print(response_two.content)

By default a ThreadPoolExecutor is created with 8 workers. If you would like to
adjust that value or share a executor across multiple sessions you can provide
one to the FuturesSession constructor.

.. code-block:: python

    from concurrent.futures import ThreadPoolExecutor
    from requests_futures.sessions import FuturesSession

    session = FuturesSession(executor=ThreadPoolExecutor(max_workers=10))
    # ...

As a shortcut in case of just increasing workers number you can pass
`max_workers` straight to the `FuturesSession` constructor:

.. code-block:: python

    from requests_futures.sessions import FuturesSession
    session = FuturesSession(max_workers=10)

FutureSession will use an existing session object if supplied:

.. code-block:: python

    from requests import session
    from requests_futures.sessions import FuturesSession
    my_session = session()
    future_session = FuturesSession(session=my_session)

That's it. The api of requests.Session is preserved without any modifications
beyond returning a Future rather than Response. As with all futures exceptions
are shifted (thrown) to the future.result() call so try/except blocks should be
moved there.

Canceling queued requests (a.k.a cleaning up after yourself)
============================================================

If you know that you won't be needing any additional responses from futures that
haven't yet resolved, it's a good idea to cancel those requests. You can do this
by using the session as a context manager:

.. code-block:: python

    from requests_futures.sessions import FuturesSession
    with FuturesSession(max_workers=1) as session:
        future = session.get('https://httpbin.org/get')
        future2 = session.get('https://httpbin.org/delay/10')
        future3 = session.get('https://httpbin.org/delay/10')
        response = future.result()

In this example, the second or third request will be skipped, saving time and
resources that would otherwise be wasted.

Iterating over a list of requests responses
===========================================

Without preserving the requests order:

.. code-block:: python

    from concurrent.futures import as_completed
    from requests_futures.sessions import FuturesSession
    with FuturesSession() as session:
        futures = [session.get('https://httpbin.org/delay/{}'.format(i % 3)) for i in range(10)]
        for future in as_completed(futures):
            resp = future.result()
            print(resp.json()['url'])

Working in the Background
=========================

Additional processing can be done in the background using requests's hooks_
functionality. This can be useful for shifting work out of the foreground, for
a simple example take json parsing.

.. code-block:: python

    from pprint import pprint
    from requests_futures.sessions import FuturesSession

    session = FuturesSession()

    def response_hook(resp, *args, **kwargs):
        # parse the json storing the result on the response object
        resp.data = resp.json()

    future = session.get('http://httpbin.org/get', hooks={
        'response': response_hook,
    })
    # do some other stuff, send some more requests while this one works
    response = future.result()
    print('response status {0}'.format(response.status_code))
    # data will have been attached to the response object in the background
    pprint(response.data)

Hooks can also be applied to the session.

.. code-block:: python

    from pprint import pprint
    from requests_futures.sessions import FuturesSession

    def response_hook(resp, *args, **kwargs):
        # parse the json storing the result on the response object
        resp.data = resp.json()

    session = FuturesSession()
    session.hooks['response'] = response_hook

    future = session.get('http://httpbin.org/get')
    # do some other stuff, send some more requests while this one works
    response = future.result()
    print('response status {0}'.format(response.status_code))
    # data will have been attached to the response object in the background
    pprint(response.data)   pprint(response.data)

A more advanced example that adds an `elapsed` property to all requests.

.. code-block:: python

    from pprint import pprint
    from requests_futures.sessions import FuturesSession
    from time import time


    class ElapsedFuturesSession(FuturesSession):

        def request(self, method, url, hooks=None, *args, **kwargs):
            start = time()
            if hooks is None:
                hooks = {}
            
            def timing(r, *args, **kwargs):
                r.elapsed = time() - start

            try:
                if isinstance(hooks['response'], (list, tuple)):
                    # needs to be first so we don't time other hooks execution
                    hooks['response'].insert(0, timing)
                else:
                    hooks['response'] = [timing, hooks['response']]
            except KeyError:
                hooks['response'] = timing

            return super(ElapsedFuturesSession, self) \
                .request(method, url, hooks=hooks, *args, **kwargs)



    session = ElapsedFuturesSession()
    future = session.get('http://httpbin.org/get')
    # do some other stuff, send some more requests while this one works
    response = future.result()
    print('response status {0}'.format(response.status_code))
    print('response elapsed {0}'.format(response.elapsed))

Using ProcessPoolExecutor
=========================

Similarly to `ThreadPoolExecutor`, it is possible to use an instance of
`ProcessPoolExecutor`. As the name suggest, the requests will be executed
concurrently in separate processes rather than threads.

.. code-block:: python

    from concurrent.futures import ProcessPoolExecutor
    from requests_futures.sessions import FuturesSession

    session = FuturesSession(executor=ProcessPoolExecutor(max_workers=10))
    # ... use as before

.. HINT::
    Using the `ProcessPoolExecutor` is useful, in cases where memory
    usage per request is very high (large response) and cycling the interpretor
    is required to release memory back to OS.

A base requirement of using `ProcessPoolExecutor` is that the `Session.request`,
`FutureSession` all be pickle-able.

This means that only Python 3.5 is fully supported, while Python versions
3.4 and above REQUIRE an existing `requests.Session` instance to be passed
when initializing `FutureSession`. Python 2.X and < 3.4 are currently not
supported.

.. code-block:: python

    # Using python 3.4
    from concurrent.futures import ProcessPoolExecutor
    from requests import Session
    from requests_futures.sessions import FuturesSession

    session = FuturesSession(executor=ProcessPoolExecutor(max_workers=10),
                             session=Session())
    # ... use as before

In case pickling fails, an exception is raised pointing to this documentation.

.. code-block:: python

    # Using python 2.7
    from concurrent.futures import ProcessPoolExecutor
    from requests import Session
    from requests_futures.sessions import FuturesSession

    session = FuturesSession(executor=ProcessPoolExecutor(max_workers=10),
                             session=Session())
    Traceback (most recent call last):
    ...
    RuntimeError: Cannot pickle function. Refer to documentation: https://github.com/ross/requests-futures/#using-processpoolexecutor

.. IMPORTANT::
  * Python >= 3.4 required
  * A session instance is required when using Python < 3.5
  * If sub-classing `FuturesSession` it must be importable (module global)

Installation
============

    pip install requests-futures

.. _`requests`: https://github.com/kennethreitz/requests
.. _`concurrent.futures`: http://docs.python.org/dev/library/concurrent.futures.html
.. _backport: https://pypi.python.org/pypi/futures
.. _hooks: http://docs.python-requests.org/en/master/user/advanced/#event-hooks