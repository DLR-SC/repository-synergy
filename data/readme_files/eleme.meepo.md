=====
Meepo
=====

.. image:: http://img.shields.io/travis/eleme/meepo/master.svg?style=flat
   :target: https://travis-ci.org/eleme/meepo

.. image:: http://img.shields.io/pypi/v/meepo.svg?style=flat
   :target: https://pypi.python.org/pypi/meepo

.. image:: http://img.shields.io/pypi/dm/meepo.svg?style=flat
   :target: https://pypi.python.org/pypi/meepo

Meepo is event sourcing and event broadcasting for databases.

Documentation: https://meepo.readthedocs.org/


Installation
============

.. highlight:: bash

:Requirements: **Python 2.x >= 2.7** or **Python 3.x >= 3.2** or **PyPy**

To install the latest released version of Meepo::

    $ pip install meepo


Features
========

Meepo can be used to do lots of things, including replication, eventsourcing,
cache refresh/invalidate, real-time analytics etc. The limit is all the tasks
should be row-based, since meepo only gives ``table_action`` -> ``pk``
style events.

* Row-based database replication.

* Replicate RDBMS to NoSQL and search engine.

* Event Sourcing.

* Logging and Auditing

* Realtime analytics


Usage
=====

Checkout `documentation`_ and `examples/`_.

.. _`documentation`: https://meepo.readthedocs.org/en/latest/
.. _`examples/`: https://github.com/eleme/meepo/tree/develop/examples
