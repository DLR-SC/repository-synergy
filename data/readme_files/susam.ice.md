Ice - WSGI on the rocks
=======================
Ice is a Python module with a WSGI microframework meant for developing
small web applications in Python. It is a single file Python module
inspired by `Bottle`_.

.. image:: https://travis-ci.org/susam/ice.svg?branch=master
   :target: https://travis-ci.org/susam/ice

.. image:: https://coveralls.io/repos/susam/ice/badge.svg?branch=master
   :target: https://coveralls.io/r/susam/ice?branch=master

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://github.com/susam/ice/blob/master/LICENSE.rst

Why Ice?
--------
This microframework was born as a result of experimenting with WSGI
framework. Since what started as a small experiment turned out to be
several hundred lines of code, it made sense to share the source code on
the web, just in case anyone else benefits from it.

This microframework has a very limited set of features currently. It may
be used to develop small web applications. For large web applications,
it may make more sense to use a more wholesome framework such as
`Flask`_ or `Django`_.

It is possible that you may find that this framework is missing a useful
API that another major framework provides. In such a case, you have
direct access to the WSGI internals to do what you want via the
documented `API`_.

If you believe that a missing feature or a bug fix would be useful to
others, you may `report an issue`_, or even better, fork this `project
on GitHub`_, develop the missing feature or the bug fix, and send a
patch or a pull request. In fact, you are very welcome to do so, and
turn this experimental project into a matured one by contributing your
code and expertise.

.. _Bottle: https://bottlepy.org/
.. _Flask: http://flask.pocoo.org/
.. _Django: https://www.djangoproject.com/
.. _API: http://icepy.readthedocs.io/en/latest/ice.html
.. _report an issue: https://github.com/susam/ice/issues
.. _project on GitHub: https://github.com/susam/ice


Requirements
------------
This module should be used with Python 3.3 or any later version of
Python interpreter.

This module depends only on the Python standard library. It does not
depend on any third party libraries.


Installation
------------
You can install this module using pip3 using the following command. ::

    pip3 install ice

You can install this module from source distribution. To do so,
download the latest .tar.gz file from https://pypi.python.org/pypi/ice,
extract it, then open command prompt or shell, and change your current
directory to the directory where you extracted the source distribution,
and then execute the following command. ::

    python3 setup.py install

Note that on a Windows system, you may have to replace ``python3`` with
the path to your Python 3 interpreter.


Resources
---------
Here is a list of useful links about this project.

- `Documentation on Read The Docs <http://icepy.readthedocs.org/>`_
- `Latest release on PyPI <https://pypi.python.org/pypi/ice>`_
- `Source code on GitHub <https://github.com/susam/ice>`_
- `Issue tracker on GitHub <https://github.com/susam/ice/issues>`_
- `Changelog on GitHub
  <https://github.com/susam/ice/blob/master/CHANGES.rst>`_


Support
-------
To report bugs, suggest improvements, or ask questions, please create a
new issue at http://github.com/susam/ice/issues.


License
-------
This is free software. You are permitted to use, copy, modify, merge,
publish, distribute, sublicense, and/or sell copies of it, under the
terms of the MIT License. See `LICENSE.rst`_ for the complete license.

This software is provided WITHOUT ANY WARRANTY; without even the implied
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See
`LICENSE.rst`_ for the complete disclaimer.

.. _LICENSE.rst: https://github.com/susam/ice/blob/master/LICENSE.rst
