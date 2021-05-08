CERT Australia CTI Toolkit
==========================

.. image:: https://travis-ci.org/certau/cti-toolkit.svg?branch=master
    :target: https://travis-ci.org/certau/cti-toolkit

.. image:: https://landscape.io/github/certau/cti-toolkit/develop/landscape.svg?style=flat
   :target: https://landscape.io/github/certau/cti-toolkit/develop
   :alt: Code Health

.. image:: https://coveralls.io/repos/github/certau/cti-toolkit/badge.svg?branch=v1.0
    :target: https://coveralls.io/github/certau/cti-toolkit?branch=v1.0

.. image:: https://readthedocs.org/projects/cti-toolkit/badge/?version=latest
    :target: http://cti-toolkit.readthedocs.org/en/latest/?badge=latest

.. image:: https://badge.fury.io/py/cti-toolkit.svg
    :target: https://badge.fury.io/py/cti-toolkit

This package contains cyber threat intelligence (CTI) tools created
by CERT Australia.


Installation
------------

Installation is streamlined using Python's setuptools. The following
installation process has been tested on clean install of Ubuntu 14.04.

#. Install prerequisites required by setuptools and libtaxii::

    $ sudo apt-get install python-pip python-dev libxml2-dev libxslt1-dev libz-dev

#. Install the cti-toolkit::

    $ sudo pip install cti-toolkit

That's it. You should now be able to run utilities, such as
``stixtransclient.py``::

    $ stixtransclient.py -h

Documentation
-------------

Online documentation is available at `<http://cti-toolkit.readthedocs.org/>`_.

To build the documentation you need Sphinx::

    $ sudo pip install Sphinx sphinxcontrib-napoleon sphinx_rtd_theme
    $ cd docs
    $ make html

This will create an HTML version of the documentation in ``docs/_build/html``.

Tests
-----

Requires tox::

    $ sudo pip install tox

Then run the tests from the repository root using::

    $ tox

Acknowledgements
----------------

CERT Australia would like to acknowledge the following contributors:

* `Robert Wallhead <https://github.com/thisismyrobot>`_
