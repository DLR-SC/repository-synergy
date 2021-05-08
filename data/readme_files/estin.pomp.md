Pomp
====

.. image:: https://img.shields.io/circleci/project/github/estin/pomp/master.svg
    :target: https://circleci.com/gh/estin/pomp/tree/master
    :alt: circleci

.. image:: https://img.shields.io/codecov/c/github/estin/pomp/master.svg
    :target: https://codecov.io/gh/estin/pomp/branch/master
    :alt: codecov

.. image:: https://img.shields.io/pypi/v/pomp.svg
    :target: https://pypi.python.org/pypi/pomp/
    :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/pyversions/pomp.svg
    :target: https://pypi.python.org/pypi/pomp
    :alt: python versions

.. image:: https://img.shields.io/pypi/wheel/pomp.svg
    :target: https://pypi.python.org/pypi/pomp/
    :alt: Have wheel

.. image:: https://img.shields.io/pypi/l/pomp.svg
    :target: https://pypi.python.org/pypi/pomp/
    :alt: License

----------

Pomp is a screen scraping and web crawling framework. Pomp is inspired by and
similar to `Scrapy`_, but has a simpler implementation that lacks the hard
`Twisted`_ dependency.

Features:

* Pure python
* Only one dependency for Python 2.x - `concurrent.futures`_ (backport of
  package for Python 2.x)
* Supports one file applications; Pomps doesn't force a specific project layout
  or other restrictions.
* Pomp is a meta framework like `Paste`_: you may use it to create your own
  scraping framework.
* Extensible networking: you may use any sync or async method.
* No parsing libraries in the core; use you preferred approach.
* Pomp instances may be distributed and are designed to work with an external
  queue.

Pomp makes no attempt to accomodate:

* redirects
* proxies
* caching
* database integration
* cookies
* authentication
* etc.

If you want proxies, redirects, or similar, you may use the excellent
`requests`_ library as the Pomp downloader.

`Pomp examples`_

`Pomp docs`_


Pomp is written and maintained by Evgeniy Tatarkin and is licensed under the
BSD license.

.. _Scrapy: http://scrapy.org/
.. _Twisted: http://twistedmatrix.com/
.. _concurrent.futures: http://pythonhosted.org/futures/
.. _Pomp examples: https://github.com/estin/pomp/tree/master/examples
.. _Pomp docs: http://pomp.readthedocs.org
.. _Paste: http://pythonpaste.org/
.. _requests: http://www.python-requests.org/en/latest/
