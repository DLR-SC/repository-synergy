Simpleflow
==========

<p class=badges>
[![Pypi Status](https://badge.fury.io/py/simpleflow.png)](http://badge.fury.io/py/simpleflow) [![Build Status](https://travis-ci.org/botify-labs/simpleflow.svg?branch=master)](https://travis-ci.org/botify-labs/simpleflow)
</p>

Simpleflow is a Python library that provides abstractions to write programs in
the [distributed dataflow paradigm](https://en.wikipedia.org/wiki/Distributed_data_flow).
It coordinates the execution of distributed tasks with [Amazon SWF](https://aws.amazon.com/swf/).

It relies on *futures* to describe the dependencies between tasks. A `Future` object
models the asynchronous execution of a computation that may end.  It tries to mimic
the interface of the Python [concurrent.futures](http://docs.python.org/3/library/concurrent.futures) library.


Features
--------

- Provides a `Future` abstraction to define dependencies between tasks.
- Define asynchronous tasks from callables.
- Handle workflows with Amazon SWF.
- Implement replay behavior like the Amazon Flow framework.
- Handle retry of tasks that failed.
- Automatically register decorated tasks.
- Encodes/decodes large fields to S3 objects transparently (aka "jumbo fields").
- Handle the completion of a decision with more than 100 tasks.
- Provides a local executor to check a workflow without Amazon SWF (see
  `simpleflow --local` command).
- Provides decider and activity worker process for execution with Amazon SWF.
- Ships with the `simpleflow` command. `simpleflow --help` for more information
  about the commands it supports.

You can read more in the **Features** section of the documentation.


Overview
--------

Please read and even run the `demo` script to have a quick glance of
`simpleflow` commands. To run the `demo`  you will need to start decider
and activity worker processes.

Start a decider with::

    $ simpleflow decider.start --domain TestDomain --task-list test examples.basic.BasicWorkflow

Start an activity worker with::

    $ simpleflow worker.start --domain TestDomain --task-list quickstart

Then execute `./extras/demo`.


More informations
-----------------

Read the main documentation at https://botify-labs.github.io/simpleflow/.
