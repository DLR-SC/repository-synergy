==================
Ganeti Web Manager
==================

Ganeti Web Manager is a Django-based web application that allows administrators
and clients access to their ganeti clusters.

Documentation
=============

Documentation_ for |gwm| is hosted by `Read the Docs <http://readthedocs.org>`_.
You can find up to date documentation for current and previous releases at
http://ganeti-webmgr.readthedocs.org/en/latest.

If your looking to develop or contribute to GWM, please refer to the
development documentation at http://ganeti-webmgr.readthedocs.org/en/develop

Building the Documentation
--------------------------

Our documentation is written in ReStructuredText and built using Sphinx. First
you will need to install the dependencies to a virtualenv or to your system's
python installation::

  pip install -r requirements/docs.txt

Then you will need to run the following commands to build the documentation::

  cd docs/
  make html

The documentation will be located at ``docs/build/html/`` as html files.
If you open ``index.html`` with your web browser, it will take you to the
table of contents.


Installation
============

For installation instructions please refer to our installation_ documentation.


Compatibility
=============

For a list of versions and browsers supported by |gwm| check our compatibility_ documentation.


Dependencies
============

A list of dependencies can be found in our requirements_ documentation.

Links
=====

* `Project page <http://code.osuosl.org/projects/ganeti-webmgr>`_
* Documentation_
* `Mailing List <http://groups.google.com/group/ganeti-webmgr>`_
* `Twitter <http://twitter.com/ganetiwebmgr>`_
* IRC: ``#ganeti-webmgr`` on freenode.net

.. _installation: http://ganeti-webmgr.readthedocs.org/en/latest/getting_started/installing.html
.. _compatibility: http://ganeti-webmgr.readthedocs.org/en/latest/project_info/compatibility.html
.. _requirements: http://ganeti-webmgr.readthedocs.org/en/latest/getting_started/requirements.html
.. _Documentation: http://ganeti-webmgr.readthedocs.org/en/latest

.. |gwm| replace:: Ganeti Web Manager
