======================
Turbulenz Python Tools
======================

The Turbulenz Python Tools package provides a set of Python based tools for development of projects using the
`Turbulenz Engine <http://github.com/turbulenz/turbulenz_engine>`_.

The tools are primarily related to asset and code generation and optimization for HTML5 based games.

History
=======

The latest release is 1.0.7 which can be found here `<https://pypi.python.org/pypi/turbulenz_tools/1.0.7>`_

A full history of changes can be found in the
`Changelog <http://github.com/turbulenz/turbulenz_tools/blob/master/CHANGES.rst>`_


Installation/Setup
==================

The recommended path for using the Turbulenz Python Tools is to either install the Turbulenz SDK from the Turbulenz
Hub, or clone the `Open Source Turbulenz Engine repository <http://github.com/turbulenz/turbulenz_engine>`_ and follow
it's setup guide.
Both of these methods will install the Turbulenz Python Tools and their dependencies from
`PyPi <http://pypi.python.org>`_ using VirtualEnv, however you can also install Turbulenz Python Tools globally on your
system or via similar virtual environment packages using Python package managers like SetupTools and pip.

Once installed the individual tools will be available from the command line in your environment, for example
``dae2json --help`` will give details on the available options for the dae2json tool.


Tools
=====

+-----------------------+-------------------------------------------------------------------------------------------+
| Tool Command/Name     | Description                                                                               |
+=======================+===========================================================================================+
| bmfont2json           | Convert `Bitmap Font Generator <http://www.angelcode.com/products/bmfont/>`_ data (.fnt)  |
|                       | files into a Turbulenz JSON asset. Only text .fnt files are supported.                    |
+-----------------------+-------------------------------------------------------------------------------------------+
| dae2json              | Convert Collada (.dae) files into a Turbulenz JSON asset.                                 |
|                       | dae2json is based on the `Collada specification                                           |
|                       | <http://www.khronos.org/files/collada_spec_1_5.pdf>`_.                                    |
+-----------------------+-------------------------------------------------------------------------------------------+
| effect2json           | Convert Effect Yaml (.effect) files into a Turbulenz JSON asset.                          |
+-----------------------+-------------------------------------------------------------------------------------------+
| exportevents          | Export event logs and anonymised user information of a game from the                      |
|                       | `Turbulenz Hub <https://hub.turbulenz.com>`_                                              |
+-----------------------+-------------------------------------------------------------------------------------------+
| json2json             | Merge JSON asset files.                                                                   |
+-----------------------+-------------------------------------------------------------------------------------------+
| json2stats            | Report metrics on JSON asset files.                                                       |
+-----------------------+-------------------------------------------------------------------------------------------+
| json2tar              | Generate a TAR file for binary assets referenced from a JSON asset.                       |
+-----------------------+-------------------------------------------------------------------------------------------+
| json2txt              | Generate plain text or html from a JSON asset.                                            |
+-----------------------+-------------------------------------------------------------------------------------------+
| makehtml              | Converts a .js file and, optionally, some HTML template code into a full HTML page that   |
|                       | can be used to load and run code built with the maketzjs tool.                            |
+-----------------------+-------------------------------------------------------------------------------------------+
| maketzjs              | Converts a JavaScript file into a .tzjs file or .canvas.js file, with optional            |
|                       | compression.                                                                              |
+-----------------------+-------------------------------------------------------------------------------------------+
| material2json         | Convert Material Yaml (.material) files into a Turbulenz JSON asset.                      |
+-----------------------+-------------------------------------------------------------------------------------------+
| obj2json              | Convert Wavefront .obj files into a Turbulenz JSON asset.                                 |
+-----------------------+-------------------------------------------------------------------------------------------+
| xml2json              | Convert XML assets into a structured JSON asset.                                          |
+-----------------------+-------------------------------------------------------------------------------------------+



Documentation
=============

Full documentation for the usage of each tool can be found in the Turbulenz Engine docs at
`<http://docs.turbulenz.com/tools/index.html>`_

This documentation is built from the `Turbulenz Engine repository <http://github.com/turbulenz/turbulenz_engine>`_


Dependencies
============

The only dependencies for using the Turbulenz Python Tools are Python 2.7.x and a number of Python packages. These
additional packages will be automatically installed as dependencies when the Turbulenz Python Tools package is
installed with a Python package manager.


Licensing
=========

The Turbulenz Python Tools are licensed under the
`MIT license <http://github.com/turbulenz/turbulenz_tools/raw/master/LICENSE>`_


Contributing
============

Our contributors are listed `here <http://github.com/turbulenz/turbulenz_tools/blob/master/CONTRIBUTORS.rst>`_

Contributions are always encouraged whether they are small documentation tweaks, bug fixes or suggestions for larger
changes. You can check the `issues <http://github.com/turbulenz/turbulenz_tools/issues>`_ or `discussion forums
<https://groups.google.com/group/turbulenz-engine-users>`_ first to see if anybody else is undertaking similar changes.

If you'd like to contribute any changes simply fork the project on Github and send us a pull request or send a Git
patch to the discussion forums detailing the proposed changes. If accepted we'll add you to the list of contributors.

We include a .pylintrc file in the repository which allows you to check your code conforms to our standards. Our
documentation is built from the Turbulenz Engine open source repository so please consider how your changes may affect
the documentation.

Note: by contributing code to the Turbulenz Python Tools project in any form, including sending a pull request
via Github, a code fragment or patch via private email or public discussion groups, you agree to release your
code under the terms of the MIT license that you can find in the
`LICENSE <http://github.com/turbulenz/turbulenz_tools/raw/master/LICENSE>`_ file included in the source distribution.


Links
=====

| Turbulenz game site - `turbulenz.com <https://turbulenz.com>`_
| Turbulenz developer service and SDK download - `hub.turbulenz.com <https://hub.turbulenz.com>`_
| Documentation for this module and the SDK - `docs.turbulenz.com <http://docs.turbulenz.com>`_
| About Turbulenz - `biz.turbulenz.com <http://biz.turbulenz.com>`_
