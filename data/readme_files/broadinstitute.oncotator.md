  .. image:: https://travis-ci.org/broadinstitute/oncotator.svg?branch=develop
    :target: https://travis-ci.org/broadinstitute/oncotator
  
  .. image:: https://coveralls.io/repos/broadinstitute/oncotator/badge.png?branch=issue_211_travis
    :target: https://coveralls.io/r/broadinstitute/oncotator?branch=issue_211_travis

======================
Oncotator Is No Longer Supported or Maintained
======================

Funcotator is a new Functional Annotation tool (the spiritual successor to Oncotator).  It is: 
  * Better: many bugs have been fixed and edge cases have been improved.
  * Faster: annotate more variants in less time
  * Easier to use and deploy: a single jar with no tricky installation or dependencies, and a tool for fetching the datasources

Funcotator is available as part of the GATK toolkit and works out of the box with both Mutect2 and HaplotypeCaller for somatic and germline annotation, respectively. 
It also has a Featured Workspace on Terra.

A Funcotator tutorial, as well as a full comparison of Funcotator and Oncotator and other helpful information can be found on the GATK website here:
https://gatk.broadinstitute.org/hc/en-us/articles/360035889931-Funcotator-Information-and-Tutorial

The github repository for GATK and Funcotator can be found here:
https://github.com/broadinstitute/gatk



-----------------------------------



======================
Oncotator
======================

License
-------

Oncotator is free for non-profit users.  Please see the LICENSE file here for more information.

Package Overview
----------------

The name of the directory, oncotator, is also the name of the **distribution**.
This distribution contains the oncotator package.

For more information:
http://www.broadinstitute.org/cancer/cga/oncotator

This distribution is the standalone version of Oncotator.  If you wish to use the web interface:
http://www.broadinstitute.org/oncotator

Please note that the web interface uses an older version of Oncotator and older datasources.

All documentation can be found in the Oncotator forums: http://gatkforums.broadinstitute.org/categories/oncotator

Installation
------------

Currently, Windows is unsupported, though this is due to a dependency, pysam, being unsupported in Windows.

IMPORTANT:  You will need root access to your python interpreter or a python virtual environment.  More information about virtual environments can be found on the following site:
https://pypi.python.org/pypi/virtualenv

As a reminder, virtualenv.py can be run as a standalone script, thereby bypassing superuser requirements.  Please see the above link for more details.

Before installing, we recommend installing pyvcf and numpy manually, before attempting the Oncotator install.  You may need to prepend each of the following commands with sudo::

    $ pip install numpy
    $ pip install pyvcf

This distribution is installable through the standard ``setup.py`` method.  Note that Distribute will be installed as part of the setup process if it isn't already::

    $ python setup.py install

Because the setup.py specifies an entry point as a console script, ``oncotator``  and ``initializeDatasource`` will be installed into your Python's ``bin/`` directory


Unit Test Setup
---------------

NOTE: Unit tests require a minimum of 4GB to run.

Before running the unit tests for the first time, please perform the following steps:

1) Execute the following three lines in the same directory as setup.py::

    $ mkdir -p out
    $ ln -s test/configs configs
    $ ln -s test/testdata testdata

2) Many unit tests rely on having the standard set of hg19 datasources, which are in a separate download.  To point the unit testing framework to your datasources, you must create a personal test config::

    $ cp configs/personal-test.config.template configs/personal-test.config
    In configs/personal-test.config, replace ```dbDir=MY_DB_DIR/``` with ```dbDir=``` the appropriate path to you oncotator datasource directory.


Running the Automated Unit Tests (with Virtual Env Creation)
--------------------
The automated unit tests (``run_ci_tests.sh``) require 6 GB to run.
This can take a fair amount of time (~20 minutes), since a full install into a new virtual environment is performed.

Execute the following line in the same directory as setup.py (provide the appropriate path to the db dir with your datasources)::

    $ bash run_ci_tests.sh <DB_DIR>


Running the Automated Unit Tests (without Virtual Env Creation)
--------------------
You can simply run the unit tests in the currently active python environment, which takes a lot less time (< 6 minutes), but requires
all dependencies to be installed.  However, you must follow the instructions for Unit Test Setup above (Steps 1 and 2), if
not already performed.  Then run (in the same directory as setup.py)::

    $ nosetests --all-modules --exe -w test -v --processes=4 --process-timeout=480  --process-restartworker


Please note that there is a known bug with ``--processes`` and output to XML.  If you alter the above nosetests command to include junit xml (``--with-xunit``), remove the last three options (```--processes=4 --process-timeout=480  --process-restartworker```).  This will cause tests to only run on one core.

Creating a Virtual Environment for Running Oncotator
--------------------
Follow these steps from the same directory as setup.py.  The first command will take several minutes::

    bash scripts/create_oncotator_venv.sh <venv_location>
    source <venv_location>/bin/activate
    python setup.py install

Version Information
-------------------

Once Oncotator is installed, run it with the -V flag to get version information::

    $ Oncotator -V


Git Process Starting with v1.0.0.0 (Developers)
-----------------------------------------------

For an overview on the oncotator process for adding features, bugfixes, and general day-to-day branching, please see::
http://nvie.com/posts/a-successful-git-branching-model/


Help
-------------------

Please post questions, issues, and feature requests in the forum at http://gatkforums.broadinstitute.org/categories/oncotator
