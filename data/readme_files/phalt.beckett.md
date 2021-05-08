===========
💫 Beckett
===========

**Hypermedia API Client Framework**

.. image:: https://img.shields.io/pypi/v/beckett.svg
        :target: https://pypi.python.org/pypi/beckett

.. image:: https://circleci.com/gh/phalt/beckett/tree/master.svg?style=svg
        :target: https://circleci.com/gh/phalt/beckett/tree/master

.. image:: https://codecov.io/gh/phalt/beckett/branch/master/graph/badge.svg?token=T9mYPv0Ep2
        :target: http://codecov.io/github/phalt/beckett?branch=master

.. image:: https://landscape.io/github/phalt/beckett/master/landscape.svg?style=flat
        :target: https://landscape.io/github/phalt/beckett/master
        :alt: Code Health

Beckett is a convention-based framework for building Python interfaces around HTTP APIs.


📚 Documentation
-----------------

https://phalt.github.io/beckett


📖 Features
------------

- Define your API client in Python instead of a data serialization language.
- Encourages good HTTP and REST practices without being too strict.
- Resources are transformed into typed instances - no more raw dictionaries!
- Automatic URL routing for RESTful interaction to your resources.
- Hypermedia relationship links are automagically resolved into python methods.
- Supports hypermedia response formats such as JSONAPI and HAL. [IN DEV]
- Works out of the box, but each resource is completely configurable.


🏗 Status
----------

Beckett is **stable** and suitable for projects, but expect occasional updates for bug fixes.


🎥 Credits
-----------

This package was created with Cookiecutter_.

We use `Python Requests`_ for talking HTTP.

Free software: ISC license_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`Python Requests`: https://github.com/audreyr/cookiecutter-pypackage
.. _license: https://github.com/phalt/beckett/blob/master/LICENSE
