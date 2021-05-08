.. image:: https://travis-ci.org/agronholm/asyncio_extras.svg?branch=master
  :target: https://travis-ci.org/agronholm/asyncio_extras
  :alt: Build Status
.. image:: https://coveralls.io/repos/agronholm/asyncio_extras/badge.svg?branch=master&service=github
  :target: https://coveralls.io/github/agronholm/asyncio_extras?branch=master
  :alt: Code Coverage
.. image:: https://readthedocs.org/projects/asyncio-extras/badge/?version=latest
  :target: https://asyncio-extras.readthedocs.io/en/latest/?badge=latest
  :alt: Documentation Status

This library provides several conveniences to users of asyncio_:

* decorator for making asynchronous context managers (like ``contextlib.contextmanager``)
* decorator and context manager for running a function or parts of a function in a thread pool
* helpers for calling functions in the event loop from worker threads and vice versa
* helpers for doing non-blocking file i/o

.. _asyncio: https://docs.python.org/3/library/asyncio.html
