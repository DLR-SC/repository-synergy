==================
specs-cookiecutter
==================

Cookiecutter template for an OpenStack specs repo projects. See https://github.com/audreyr/cookiecutter.

* Free software: Apache license
* pbr_: Set up to use Python Build Reasonableness
* OpenStack-Infra_: Ready for OpenStack Continuous Integration testing
* Tox_ testing: Setup to easily building sphunx docs
* Sphinx_ docs: Documentation ready for generation and publication

Usage
-----

Generate a Python package project::

    cookiecutter https://git.openstack.org/openstack-dev/specs-cookiecutter.git

OpenStack projects require a working git repo for pbr to work, so you need to
init a repo and commit to it before doing anything else::

    cd $repo_name
    git init
    git add .
    git commit -a

Then:

* Add the project to the OpenStack Infrastructure


.. _pbr: http://docs.openstack.org/developer/pbr
.. _OpenStack-Infra: http://docs.openstack.org/infra/system-config
.. _Tox: http://testrun.org/tox/
.. _Sphinx: http://sphinx-doc.org/
