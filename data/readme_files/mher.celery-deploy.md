Deployment tool for Celery
==========================

`celerydeploy` is a fabric_ script for deploying and managing Celery_
worker processes.

`celerydeploy` creates `virtual environments`_ on remote hosts, deploys
task modules and manages celeryd worker processes with supervisord_.

Usage
-----

Before calling `celerydeploy` provide a deployment path and a list of
target hosts. `celerydeploy` will try to find `CELERY_DEPLOY_PATH` 
variable in Celery configuration file. Target hosts can be provided
with `CELERY_DEPLOY_HOSTS` variable or using --hosts command line option.
Third-party libraries can be installed by listing them in `PIP_PACKAGES`
variable.

Setup Celery on localhost and example.com: ::

    $ celerydeploy --hosts example.com,localhost worker.setup

Start, stop or restart workers: ::

    $ celerydeploy worker.start

    $ celerydeploy worker.stop

    $ celerydeploy worker.restart

Update task modules and restart workers: ::

    $ celerydeploy worker.deploy worker.restart

Get a list of possible commands: ::

    $ celerydeploy --list

celerydeploy is a fabric script and can be embedded into other deployment
scripts.

Installation
------------

To install celerydeploy, simply: ::

    $ pip install celerydeploy

.. _`fabric`: http://fabfile.org/
.. _`celery`: http://celeryproject.org/
.. _`supervisord`: http://supervisord.org/
.. _virtual environments: http://pypi.python.org/pypi/virtualenv


.. image:: https://d2weczhvl823v0.cloudfront.net/mher/celery-deploy/trend.png
   :alt: Bitdeli badge
   :target: https://bitdeli.com/free

