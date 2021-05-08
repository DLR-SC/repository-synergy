Py2neo v4
=========
.. image:: https://img.shields.io/github/license/technige/py2neo.svg
   :target: https://www.apache.org/licenses/LICENSE-2.0
   :alt: License

**Py2neo** is a client library and toolkit for working with `Neo4j <https://neo4j.com/>`_ from within `Python <https://www.python.org/>`_ applications and from the command line.
The library supports both Bolt and HTTP and provides a high level API, an OGM, admin tools, an interactive console, a Cypher lexer for Pygments, and many other bells and whistles.
Unlike previous releases, Py2neo does not require an HTTP-enabled server and can work entirely through Bolt.

When considering whether to use py2neo or the `official Python Driver for Neo4j <https://github.com/neo4j/neo4j-python-driver>`_, there is a trade-off to be made.
Py2neo offers a higher level API and an OGM, but the official driver provides mechanisms to work with clusters, such as automatic retries.
If you are new to Neo4j, need an OGM, do not want to learn Cypher immediately, or require data science integrations, py2neo may be the better choice.
If you are building a high-availability Enterprise application, or are using a cluster, you likely need the official driver.


Installation
------------
.. image:: https://img.shields.io/pypi/v/py2neo.svg
   :target: https://pypi.python.org/pypi/py2neo
   :alt: PyPI version

.. image:: https://img.shields.io/travis/technige/py2neo/v4.svg
   :target: https://travis-ci.org/technige/py2neo
   :alt: Build Status

.. image:: https://img.shields.io/coveralls/github/technige/py2neo/v4.svg
   :target: https://coveralls.io/github/technige/py2neo?branch=v4
   :alt: Coverage Status

To install the latest stable version of py2neo, simply use pip:

.. code-block::

    $ pip install py2neo

Or to install the latest bleeding edge code directly from GitHub, use:

.. code-block::

    $ pip install git+https://github.com/technige/py2neo.git#egg=py2neo


Note that code installed directly from GitHub is likely to be unstable.
Your mileage may vary.


Requirements
------------

.. image:: https://img.shields.io/pypi/pyversions/py2neo.svg
   :target: https://www.python.org/
   :alt: Python versions

.. image:: https://img.shields.io/badge/neo4j-3.2%20%7C%203.3%20%7C%203.4%20%7C%203.5%20%7C%204.0-blue.svg
   :target: https://neo4j.com/
   :alt: Neo4j versions

The following versions of Python and Neo4j are supported:

- Python 2.7 / 3.5 / 3.6 / 3.7 / 3.8
- Neo4j 3.2 / 3.3 / 3.4 / 3.5 / 4.0 (the latest point release of each version is recommended)

While either Neo4j Community or Enterprise edition may be used, py2neo offers no direct support for Enterprise-only features, such as `Causal Clustering <https://neo4j.com/docs/operations-manual/current/clustering/>`_.

Note also that Py2neo is developed and tested under **Linux** using standard CPython distributions.
While other operating systems and Python distributions may work, support for these is not available.


Contact
-------

For more information, read the `handbook <http://py2neo.org/v4>`_.
