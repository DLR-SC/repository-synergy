bok-choy
========

.. image:: https://img.shields.io/pypi/v/bok_choy.svg
    :target: https://pypi.python.org/pypi/bok_choy/
    :alt: PyPI

.. image:: https://travis-ci.org/edx/bok-choy.svg?branch=master
    :target: https://travis-ci.org/edx/bok-choy
    :alt: Travis

.. image:: http://codecov.io/github/edx/bok-choy/coverage.svg?branch=master
    :target: http://codecov.io/github/edx/bok-choy?branch=master
    :alt: Codecov

.. image:: https://readthedocs.org/projects/bok-choy/badge/?version=latest
    :target: http://bok-choy.readthedocs.io/en/latest/
    :alt: Documentation

.. image:: https://img.shields.io/pypi/pyversions/bok_choy.svg
    :target: https://pypi.python.org/pypi/bok_choy/
    :alt: Supported Python versions

.. image:: https://img.shields.io/github/license/edx/bok-choy.svg
    :target: https://github.com/edx/bok-choy/blob/master/LICENSE.txt
    :alt: License

UI-level acceptance test framework.  `Full documentation available on ReadTheDocs`__.

__ http://bok-choy.readthedocs.org/en/latest/


Overview
--------

A Python framework for writing robust Selenium tests.


Installation
------------

As Bok Choy is a Python framework, you first need to install Python.
If you’re running Linux or Mac OS X, you probably already have it installed.
We recommend that you use `pip <http://www.pip-installer.org/>`_ to install your Python
packages:

.. code-block:: bash

   pip install bok_choy

.. Note::

   On Ubuntu Linux 18.04 you might have to install
   *firefox-geckodriver* (for Firefox) and/or *chromium-chomedriver* (for Chromium),
   especially if you hit the following Error when running bok_choy::

     bok_choy.promise.BrokenPromise: Promise not satisfied: Browser is instantiated successfully.


Running Tests
-------------

To run the test suite for bok-choy itself:

* Install Firefox; as of this writing, the current `version 59.0.1 <https://ftp.mozilla.org/pub/firefox/releases/59.0.1/>`_
  works with the latest selenium Python package (3.11.0)
* Install `phantomjs <http://phantomjs.org/download.html>`_
* Create a virtualenv which uses Python 2.7, 3.5, or 3.6
* With that virtualenv activated, run ``pip install -r requirements/tox.txt`` to
  install the `tox <http://tox.testrun.org/>`_ testing tool and its
  dependencies
* Run ``tox -e py27`` (or ``tox -e py35``, etc.).  If you want to run the tests in
  parallel, add the desired number of worker processes like ``tox -e py27 -- -n 5``
  or ``tox -e py35 -- -n auto``.
* To test and build the documentation, run ``tox -e doc``
* To run an individual test, run ``py.test tests/<test file>::<test class>::<test name>``


License
-------

The code in this repository is licensed under the Apache License, Version 2.0,
unless otherwise noted.

Please see ``LICENSE.txt`` for details.


How to Contribute
-----------------

Contributions are very welcome. The easiest way is to fork this repo, and then
make a pull request from your fork. The first time you make a pull request, you
may be asked to sign a Contributor Agreement.


Reporting Security Issues
-------------------------

Please do not report security issues in public. Please email security@edx.org


Mailing List and IRC Channel
----------------------------

You can discuss this code on the `edx-code Google Group <https://groups.google.com/forum/#!forum/edx-code>`_
or in the **testing** channel on the `Open edX Slack <https://openedx.slack.com>`_.
