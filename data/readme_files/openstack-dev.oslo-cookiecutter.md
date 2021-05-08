===========================
oslo-cookiecutter-openstack
===========================

Cookiecutter template for an Oslo library (part of the OpenStack
project). See https://github.com/audreyr/cookiecutter.

* Free software: Apache license
* pbr_: Set up to use Python Build Reasonableness
* hacking_: Enforces the OpenStack Hacking Guidelines
* testrepository_: Runs tests using testrepository
* OpenStack-Infra_: Ready for OpenStack Continuous Integration testing
* Tox_ testing: Setup to easily test for Python 2.6, 2.7, 3.3, 3.4
* Sphinx_ docs: Documentation ready for generation and publication

Usage
-----

Generate a Python package project::

    cookiecutter https://opendev.org/openstack/oslo-cookiecutter

Oslo libraries require a working git repo for pbr to work, so you need
to init a repo and commit to it before doing anything else::

    cd oslo.$module_name
    git init
    git add .
    git commit -a

Then:

* Add the project to the OpenStack Infrastructure


.. _pbr: http://docs.openstack.org/developer/pbr
.. _OpenStack-Infra: http://docs.openstack.org/infra/system-config
.. _testrepository: https://testrepository.readthedocs.org/
.. _Tox: http://testrun.org/tox/
.. _Sphinx: http://sphinx-doc.org/
.. _hacking: https://opendev.org/openstack/hacking
