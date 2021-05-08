qiBuild
=======

.. image:: http://img.shields.io/pypi/v/qibuild.png
  :target: https://pypi.python.org/pypi/qibuild
.. image:: https://travis-ci.org/aldebaran/qibuild.svg?branch=master
  :target: https://travis-ci.org/aldebaran/qibuild

qiBuild is a collection of command-line tools to help development of multiple
projects.

It contains:

* ``qibuild`` : compilation of C++ projects made easy, using `CMake <http://www.cmake.org/>`_ as a backend
* ``qitoolchain``: managing cross-toolchains and pre-compiled packages
* ``qisrc``: managing several git projects
* ``qidoc``: managing documentation written using `Sphinx <http://sphinx-doc.org/>`_ or
  `Doxygen <http://www.stack.nl/~dimitri/doxygen/>`_
* ``qipy``: managing Python projects depending on C++ projects using
  `virtualenv <https://virtualenv.pypa.io/en/latest/>`_ as a backend

Please refer to the documentation for more information.

qibuild is under a BSD-style license that can be found in the COPYING file.
Any contribution is more than welcome ;)


git repository
--------------

http://github.com/aldebaran/qibuild

Mailing list
-------------

https://groups.google.com/a/aldebaran-robotics.com/group/qibuild-dev/topics

IRC channel
-----------

Join us on ``#qi`` on freenode.

Documentation
-------------

http://doc.aldebaran.com/qibuild/

Installation
------------

Requirements: ``Python`` with ``pip``

Just run::

  pip install qibuild



qiBuild contains work from
---------------------------

* cmake http://www.cmake.org/cmake/project/license.html (BSD)

* gclient http://code.google.com/p/gclient/ (BSD)

* pygments http://pygments.org/ (BSD)
