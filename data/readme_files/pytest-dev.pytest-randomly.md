===============
pytest-randomly
===============

.. image:: https://img.shields.io/travis/pytest-dev/pytest-randomly.svg
        :target: https://travis-ci.org/pytest-dev/pytest-randomly

.. image:: https://img.shields.io/pypi/v/pytest-randomly.svg
        :target: https://pypi.python.org/pypi/pytest-randomly

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/python/black

.. figure:: https://raw.githubusercontent.com/pytest-dev/pytest-randomly/master/logo.png
   :scale: 50%
   :alt: Randomness power.

Pytest plugin to randomly order tests and control ``random.seed``. (Also
available `for nose <https://github.com/adamchainz/nose-randomly>`_).

--------
Features
--------

All of these features are on by default but can be disabled with flags.

* Randomly shuffles the order of test items. This is done first at the level of
  modules, then at the level of test classes (if you have them), then at the
  order of functions. This also works with things like doctests.
* Resets ``random.seed()`` at the start of every test case and test to a fixed
  number - this defaults to ``time.time()`` from the start of your test run,
  but you can pass in ``--randomly-seed`` to repeat a randomness-induced
  failure.
* If
  `factory boy <https://factoryboy.readthedocs.io/en/latest/reference.html>`_
  is installed, its random state is reset at the start of every test. This
  allows for repeatable use of its random 'fuzzy' features.
* If `faker <https://pypi.python.org/pypi/faker>`_ is installed, its random
  state is reset at the start of every test. This is also for repeatable fuzzy
  data in tests - factory boy uses faker for lots of data.
* If `numpy <http://www.numpy.org/>`_ is installed, its random state is reset
  at the start of every test.
* If additional random generators are used, they can be registered under the
  ``pytest_randomly.random_seeder``
  `entry point <https://packaging.python.org/specifications/entry-points/>`_ and
  will have their seed reset at the start of every test. Register a function
  that takes the current seed value.

-----
About
-----

Randomness in testing can be quite powerful to discover hidden flaws in the
tests themselves, as well as giving a little more coverage to your system.

By randomly ordering the tests, the risk of surprising inter-test dependencies
is reduced - a technique used in many places, for example Google's C++ test
runner `googletest
<https://code.google.com/p/googletest/wiki/V1_5_AdvancedGuide#Shuffling_the_Tests>`_.

By resetting the random seed to a repeatable number for each test, tests can
create data based on random numbers and yet remain repeatable, for example
factory boy's fuzzy values. This is good for ensuring that tests specify the
data they need and that the tested system is not affected by any data that is
filled in randomly due to not being specified.

This plugin is a Pytest port of my plugin for nose, ``nose-randomly``. I've
written a `blog post on its history <https://adamj.eu/tech/2018/01/08/pytest-randomly-history/>`_.

-----
Usage
-----

Install from pip with:

.. code-block:: bash

    python -m pip install pytest-randomly

Python 3.5 to 3.8 supported.

Pytest will automatically find the plugin and use it when you run ``pytest``.
The output will start with an extra line that tells you the random seed that is
being used:

.. code-block:: bash

    $ pytest
    ...
    platform darwin -- Python 3.7.2, pytest-4.3.1, py-1.8.0, pluggy-0.9.0
    Using --randomly-seed=1553614239
    ...

If the tests fail due to ordering or randomly created data, you can restart
them with that seed using the flag as suggested:

.. code-block:: bash

    pytest --randomly-seed=1234

Or more conveniently, use the special value ``last``:

.. code-block:: bash

    pytest --randomly-seed=last

Since the ordering is by module, then by class, you can debug inter-test
pollution failures by narrowing down which tests are being run to find the bad
interaction by rerunning just the module/class:

.. code-block:: bash

    pytest --randomly-seed=1234 tests/module_that_failed/

You can disable behaviours you don't like with the following flags:

* ``--randomly-dont-reset-seed`` - turn off the reset of ``random.seed()`` at
  the start of every test
* ``--randomly-dont-reorganize`` - turn off the shuffling of the order of tests

The plugin appears to Pytest with the name 'randomly'. To disable it
altogether, you can use the ``-p`` argument, for example:

.. code-block:: sh

    pytest -p no:randomly

-----------
Entry Point
-----------

If you're using a different randomness generator in your third party package,
you can register an entrypoint to be called every time ``pytest-randomly``
reseeds. Implement the entrypoint ``pytest_randomly.random_seeder``, referring
to a function/callable that takes one argument, the new seed (int).

For example in your ``setup.cfg``:

.. code-block:: sh

    [options.entry_points]
    pytest_randomly.random_seeder =
        mypackage = mypackage.reseed

Then implement ``reseed(new_seed)``.
