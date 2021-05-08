divspl (Dustin Ingram's Very Special Programming Language)
==========================================================

An implementation of a FizzBuzz DSL using `rply <https://github.com/alex/rply>`_.

Description
===========

``divspl`` is an interpreter for the DIVSPL DSL (Dustin Ingram's Very Special
Programming Language Domain Specific Language), which is used for implementing
FizzBuzz-like programs. For more information, see http://promptworks.com/blog/the-fastest-fizzbuzz-in-the-west.

Installation
============

::

    $ pip install divspl

Or for local development::

    $ virtualenv env
    $ source env/bin/activate
    $ python setup.py install

Usage
=====

::

    $ divspl [filename]

Where::

    filename            A *.divspl filename to execute

Example
=======

Use the interpreter to execute valid DIVSPL code::

    $ divspl fizzbuzz.divspl

Or use it as a shebang::

    #!env/bin/divspl
    1...15
    fizz=3
    buzz=5

Then::

    $ ./fizzbuzz.divspl


Compiling with RPython
======================

``divspl`` is compatible with `RPython <https://rpython.readthedocs.io>`__. To
compile::

    $ pip install rply
    $ mkdir -p pypy
    $ wget https://bitbucket.org/pypy/pypy/get/default.tar.bz2
    $ tar -xvvf default.tar.bz2 -C pypy --strip-components=1
    $ mkdir -p bin
    $ python pypy/rpython/bin/rpython --output=bin/divspl divspl/target.py

You now have a compiled ``divspl`` binary in ``./bin``, which you can use as
follows::

    $ bin/divspl fizzbuzz.divspl

Contact
=======

:On PyPI:
    http://pypi.python.org/pypi/divspl/

:Source:
    https://github.com/di/divspl

:Issues:
    https://github.com/di/divspl/issues
