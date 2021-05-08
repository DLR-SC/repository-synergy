============
Layer Linter
============


.. image:: https://img.shields.io/pypi/status/layer-linter

.. image:: https://img.shields.io/pypi/v/layer_linter.svg
        :target: https://pypi.python.org/pypi/layer_linter

.. image:: https://img.shields.io/pypi/pyversions/layer-linter.svg
    :alt: Python versions
    :target: http://pypi.python.org/pypi/layer-linter/

.. image:: https://api.travis-ci.org/seddonym/layer_linter.svg?branch=master
        :target: https://travis-ci.org/seddonym/layer_linter

.. image:: https://codecov.io/gh/seddonym/layer_linter/branch/master/graph/badge.svg
        :target: https://codecov.io/gh/seddonym/layer_linter

.. image:: https://readthedocs.org/projects/layer-linter/badge/?version=latest
        :target: https://layer-linter.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


**Layer Linter has been deprecated in favour of Import Linter.**

`Import Linter`_ does everything Layer Linter does, but with more features and a slightly different API.
If you're already using Layer Linter, migrating to Import Linter is simple: there is a guide here_.

Outline
-------

Layer Linter checks that your project follows a custom-defined layered architecture, based on
its internal dependencies (i.e. the imports between its modules).

* Free software: BSD license
* Documentation: https://layer-linter.readthedocs.io.

.. _Import Linter: https://github.com/seddonym/import-linter
.. _here: https://layer-linter.readthedocs.io/en/latest/migrating-to-import-linter.html

Overview
--------

Layer Linter is a command line tool to check that you are following a self-imposed
architecture within your Python project. It does this by analysing the internal
imports between all the modules in your code base, and compares this
against a set of simple rules that you provide in a ``layers.yml`` file.

For example, you can use it to check that no modules inside ``myproject.foo``
import from any modules inside ``myproject.bar``, even indirectly.

This is particularly useful if you are working on a complex codebase within a team,
when you want to enforce a particular architectural style. In this case you can add
Layer Linter to your deployment pipeline, so that any code that does not follow
the architecture will fail tests.

Quick start
-----------

Install Layer Linter::

    pip install layer-linter

Decide on the dependency flows you wish to check. In this example, we have
organised our project into three subpackages, ``myproject.high``, ``myproject.medium``
and ``myproject.low``. These subpackages are known as *layers*. Note: layers must
have the same parent package (i.e. all be in the same directory). This parent is known as a *container*.

Create a ``layers.yml`` in the root of your project. For example::

    My Layers Contract:
      containers:
        - myproject
      layers:
        - high
        - medium
        - low

(This contract tells Layer Linter that the order of the layers runs from ``low`` at the bottom
to ``high`` at the top. Layers higher up can import ones lower down, but not the other way around.)

Note that the container is an absolute name of a Python package, while the layers are relative to the container.

Now, from your project root, run::

    layer-lint myproject

If your code violates the contract, you will see an error message something like this::

    ============
    Layer Linter
    ============

    ---------
    Contracts
    ---------

    Analyzed 23 files, 44 dependencies.
    -----------------------------------

    My layer contract BROKEN

    Contracts: 0 kept, 1 broken.

    ----------------
    Broken contracts
    ----------------


    My layer contract
    -----------------


    1. myproject.low.x imports myproject.high.y:

        myproject.low.x <-
        myproject.utils <-
        myproject.high.y

For more details, see `Usage`_.

.. _Usage: https://layer-linter.readthedocs.io/en/latest/usage.html
