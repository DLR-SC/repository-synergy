############
ProbeManager
############

.. image:: https://www.ko-fi.com/img/donate_sm.png
   :alt: Donate
   :target: https://ko-fi.com/mtreussart

|Licence| |Version|


.. image:: https://api.codacy.com/project/badge/Grade/afc2ab5226584ac3b594eb09ebcc2ccc?branch=master
   :alt: Codacy Grade
   :target: https://app.codacy.com/app/treussart/ProbeManager?utm_source=github.com&utm_medium=referral&utm_content=treussart/ProbeManager&utm_campaign=badger

.. image:: https://api.codacy.com/project/badge/Coverage/8c16c475964d4db58ce0c7de0d03abbf?branch=master
   :alt: Codacy Coverage
   :target: https://www.codacy.com/app/treussart/ProbeManager?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=treussart/ProbeManager&amp;utm_campaign=Badge_Coverage

+------------------+--------------------+
| Status           | Operating system   |
+==================+====================+
| |Build_Status|   | Linux x86\_64      |
+------------------+--------------------+

.. |Licence| image:: https://img.shields.io/github/license/treussart/ProbeManager.svg
.. |Stars| image:: https://img.shields.io/github/stars/treussart/ProbeManager.svg
.. |Forks| image:: https://img.shields.io/github/forks/treussart/ProbeManager.svg
.. |Downloads| image:: https://img.shields.io/github/downloads/treussart/ProbeManager/total.svg
.. |Version| image:: https://img.shields.io/github/tag/treussart/ProbeManager.svg
.. |Commits| image:: https://img.shields.io/github/commits-since/treussart/ProbeManager/latest.svg
.. |Build_Status| image:: https://travis-ci.org/treussart/ProbeManager.svg?branch=master
   :target: https://travis-ci.org/treussart/ProbeManager

Presentation
============

It is common to see that many IDS (intrusion and detection system), including the software and its rules are not updated regularly. This can be explained by the fact the software and rule management is often complicated, which can be a particular problem for small and medium sized enterprises that normally lack system security expertise and full time operators to supervise their respective IDS. This finding encouraged me to develop an application (ProbeManager) that will better manage network and machine detection probes on a system.

ProbeManager is an application that centralizes the management of intrusion detection systems. The purpose of ProbeManager is to simplify the deployment of detection probes and to put together all of their functionalities in one single place. ProbeManager also allows you to check the status of the probes and to be notified whenever there is a problem or dysfunction. ProbeManager is not a SIEM (security information and event management), therefore, it doesn’t display the probe outputs (alerts, logs, etc…)

ProbeManager is currently compatible with NIDS Suricata and Bro, and it will soon also be compatible with OSSEC.

Features
--------

* Search rules in all probes.
* List installed probes and their status (Running or not, uptime ...).
* Install, update probe.
* Start, stop, reload and restart probe.
* Push, Email notifications (change of status, ...).
* API Restfull.
* See all asynchronous jobs.

Usage
=====

.. image:: https://raw.githubusercontent.com/treussart/ProbeManager/master/docs/data/Deployement_example_of_Probemanager_in_a_network.png
   :alt: Deployement example of Probemanager in a network

.. image:: https://raw.githubusercontent.com/treussart/ProbeManager/master/docs/data/Deployement_example_of_Probemanager_in_a_VPS.png
   :alt: Deployement example of Probemanager in a VPS

Installation
============

Operating System
----------------

+------------+------------+-----------+
|  OS        |    prod    |   test    |
+============+============+===========+
|  OSX 12+   |            |     X     |
+------------+------------+-----------+
|  Debian 9  |     X      |           |
+------------+------------+-----------+
|  Ubuntu 14 |     X      |           |
+------------+------------+-----------+

OSX 12+ (Only for project development), Debian stable and Ubuntu 14.04+ are Supported and tested.

Requirements
------------

-  Python3.5+
-  Pip
-  Rabbitmq-server (installed with install script)
-  Postgresql (installed with install script)

Retrieve the project
--------------------

`Source code on Github <https://github.com/treussart/ProbeManager/>`_

.. code-block:: sh

    git clone --recursive https://github.com/treussart/ProbeManager.git

Install
-------

For developer :
^^^^^^^^^^^^^^^

.. code-block:: sh

    ./install.sh
    ./start.sh

For Production :
^^^^^^^^^^^^^^^^

Default destination path : /usr/local/share

For same destination path : .

Be sure to have the write rights in the destination path.

.. code-block:: sh

    ./install.sh prod [destination path]

With Django server (not recommended) :

.. code-block:: sh

    [destination path]./start.sh prod

With Apache (Only for Debian) :

.. code-block:: sh

     http://localhost

Launch the tests
----------------

(Only for Dev or Travis) :

.. code-block:: sh

    ./test.sh


Open the file with a web browser :

::

    coverage_html/index.html


Add a submodule
===============

.. code-block:: sh

    git submodule add -b master --name suricata https://github.com/treussart/ProbeManager_Suricata.git probemanager/suricata

Modules must respect a few rules:

* A file version.txt (generated by install script)
* A file README.rst
* A folder api with a variable 'urls_to_register' into urls.py (Optional)
* An install script : install.sh (Optional)
* A script for initializing the database : init_db.sh (Optional)


Documentation
=============


Respect standard : reStructuredText (RST).

.. code-block:: sh

    venv/bin/python probemanager/manage.py runscript generate_doc --settings=probemanager.settings.dev


Open the file with a web browser :

::

    docs/_build/html/index.html

Or retrieve the full documentation `here <https://treussart.github.io/ProbeManager/>`_
