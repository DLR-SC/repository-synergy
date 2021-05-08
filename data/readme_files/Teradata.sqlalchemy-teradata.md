Dialect for SQLAlchemy
======================

SQLAlchemy is a database toolkit that provides an abstraction over
databases. It allows you to interact with relational databases using an
object relational mapper or through a pythonic sql rendering engine
known as the core.

Read the documentation and more: http://www.sqlalchemy.org/

The Teradata Dialect is an implementation of SQLAlchemy’s Dialect
System. It implements various classes that are specific to interacting
with the teradata dbapi, construction of sql specific to Teradata, and
more. The project is still in an incubation phase. See test/usage\_test
for how the dialect is used for the core expression language api.

Design Principles
=================

::

    * Have a simple setup process and a minimal learning curve
    * Provide a simple core that is modular and extensible
    * Be an easy way to interact with the database out of the box

Quick Start
===========

Install the sqlalchemy-teradata library:

::

    [sudo] pip install sqlalchemy-teradata

Setup the connect url to point to the database. See the `example`_ in
the wiki.

Get Involved
============

::

    * We welcome your contributions in: Documentation, Bug Reporting, Tests, and Code (Features & Bug Fixes)
    * You can contribute to our documentation by going to our github wiki.
    * All code submissions are done through pull requests.

We have a room in `gitter`_. It is still based off of the old repo but it will do.

Tests
=====

The dialect is tested using the pytest plugin. You can run pytest in the sqlalchemy-teradata
directory with the ``py.test``\ command. By default the tests are run against the database
URI specified in ``setup.cfg`` under the ``[db]`` heading.

You can override the dburi you would like the tests to run against:

.. code:: 

    py.test --dburi:teradata://user:pw@host

To view the databases aliased in setup.cfg:

.. code:: 

    py.test --dbs all

To run the tests against an aliased database URI in setup.cfg:

.. code:: 

    py.test --db default
    py.test --db teradata

If the --db flag nor the --dburi flag are specified when running py.test,
the database uri specified as ``default`` in setup.cfg is used.

Typical usage:

.. code:: python

    # test all the things (against default)!
    py.test -s test/*

    # run tests in this file
    py.test -s test/test_suite.py

    # run TestClass in the the file
    py.test -s test/test_suite.py::TestClass

    # just run a specific method in TestClass
    py.test -s test/test_suite.py::TestClass::test_func

see the `pytest docs`_ for more info

See Also
========

-  `PyTd`_: the DB API 2.0 implementation found in the teradata module
-  `sqlalchemy\_aster`_: A SQLAlchemy dialect for aster

.. _gitter: https://gitter.im/sandan/sqlalchemy-teradata
.. _example: https://github.com/Teradata/sqlalchemy-teradata/wiki/Examples#creating-an-engine
.. _pytest docs: http://pytest.org/latest/contents.html#toc
.. _PyTd: https://github.com/Teradata/PyTd
.. _sqlalchemy\_aster: https://github.com/KarolTx/sqlalchemy_aster
