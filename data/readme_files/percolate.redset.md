redset
======

|PyPI version| |build status| |Coverage Status|

You may not need heavyweights like Celery or RQ. Maintaing an AMQP server 
might be overkill. There's a simpler, easier way to distribute work.

Redset provides simple, generic sorted sets backed by Redis that can be used to
coordinate distributed systems and parcel out work. Unlike more common
distribution libraries like Celery or RQ, redset avoids duplicate work for
certain use-cases by maintaining a set of tasks instead of a list or queue.
And it does so with a dead-simple interface that feels natural for Python.

Redset is currently used in the wild to do things like

- maintain a high-throughput work queue of streaming updates to be processed
- power a multi-producer, multi-consumer scraping architecture that won't do
  the same work twice
- maintain a simple, cross-process set of "seen" items that each have a 
  TTL
- schedule non-duplicate, periodic polling of analytics on social services


Features
--------

-  No worker daemons to run, no heavy AMQP service to monitor
-  Safe for multiple producers and consumers
-  Seamless, simple use with Python objects using serializers
-  Zero dependencies: you provide an object that implements the 
   ``redis.client.Redis`` interface, we don't ask any questions.
-  Simple, easy-to-read implementation
-  Mimics Python's native ``set`` interface
-  Battle-tested
-  Python 3 compatible

Simple example
--------------

.. code:: python

    import json
    import redis

    from redset import TimeSortedSet

    r = redis.Redis()
    ss = TimeSortedSet(r, 'important_json_biz', serializer=json)

    ss.add({'foo': 'bar1'})
    ss.add({'foo': 'bar2'})
     
    ss.add({'foo': 'bar3'})
    ss.add({'foo': 'bar3'})

    len(ss)
    # 3


    # ...some other process A

    ss.peek()
    # {'foo': 'bar1'}

    ss.pop()
    # {'foo': 'bar1'}


    # ...meanwhile in process B (at exactly same time as A's pop)

    ss.take(2)
    # [{'foo': 'bar2'}, {'foo': 'bar3'}]

Docs
----

`Here <http://redset.readthedocs.org/en/latest/>`__

About
-----

This software was developed at `Percolate <https://percolate.com>`__,
where we use it for all sorts of things that involve maintaining
synchronized sets of things across process boundaries. A common use-case
is to use redset for coordinating time-sensitive tasks where duplicate
requests may be generated.

Redset is unopinionated about how consumers look or behave. Want to have
a plain 'ol Python consumer managed by supervisor? Fine. Want to be able
to pop off items from within a celery job? Great. Redset has no say in
where or how it is used: mechanism, not policy.

Usage concepts
--------------

``redset.SortedSet`` and its subclasses can be instantiated with a few
paramters that are notable.

Specifying a serializer
~~~~~~~~~~~~~~~~~~~~~~~

Since Redis only stores primitive numbers and strings, handling
serialization and deserialization is a key part of making redset set
usage simple in Python.

A ``serializer`` instance can be passed (which adheres to the
``redset.interfaces.Serializer`` interface, though it need not subclass
it) to automatically handle packing and unpacking items managed with
redset.

Specifying a scorer
~~~~~~~~~~~~~~~~~~~

A callable that specifies how to generate a score for items being added
can also be passed to SortedSet's constructor as ``scorer``. This
callable takes one argument, which is the item *object* (i.e. the item
before serialization) to be "scored."

Related projects
----------------

-  `redis-py <https://github.com/andymccurdy/redis-py>`__
-  `celery <https://github.com/celery/celery>`__
-  `RQ <http://python-rq.org/>`__

.. |PyPI version| image:: https://badge.fury.io/py/redset.png
   :target: http://badge.fury.io/py/redset
.. |build status| image:: https://travis-ci.org/percolate/redset.png?branch=master
   :target: https://travis-ci.org/percolate/redset
.. |Coverage Status| image:: https://coveralls.io/repos/percolate/redset/badge.png?branch=master
   :target: https://coveralls.io/r/percolate/redset?branch=master
