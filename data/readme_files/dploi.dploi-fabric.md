==================
Dploi Fabric Tasks
==================

This is a set of reusable fabric tasks. It uses the new-style task system
of fabric >= 1.2

Usage
=====
 * Add ``dploi-fabric`` to your buildout environment (preferably in
   ``development_local.cfg``, the servers have no use for it).
 * Create a ``fabfile.py`` as normal.
 * Pick and choose the modules and import them in the ``fabfile.py``, e.g.::

      from fabric.decorators import task

      from dploi_fabric.db import pg # if project uses mysql, import "mysql" instead
      from dploi_fabric import supervisor, nginx
      from dploi_fabric import git, utils, buildout, south, django_utils, project

      from dploi_fabric.conf import load_settings

      @task
      def dev():
          load_settings('dev')

      @task
      def stage():
          load_settings('stage')

      @task
      def live():
          load_settings('live')

      @task
      def deploy():
          pg.dump.run()
          git.update()
          buildout.run()
          south.migrate.run()
          django_utils.collectstatic()
          supervisor.restart()
          supervisor.status()
          nginx.update_config_file()

 * in the project root, create a file ``deployment.py`` following this template::

      project_name = 'awesome_new_website'
      
      settings = {
          'dev': {
              'hosts': ['yourserver.com'],
              'autostart': True,
              'path': '/home/awesome_new_website-dev/app/',
              'user': 'awesome_new_website-dev',
              'buildout_cfg': 'server_dev.cfg',
              'repo': 'git@github.com:youruser/awesome_new_website.git',
              'branch': 'master',
              'backup_dir': '/home/awesome_new_website-dev/tmp/', # Used for mysql/psql dumps
              'db_name': 'awesome_new_website-dev',
              'db_username': 'awesome_new_website-dev',
              'domains': ['sitename-dev.agency.com', 'www.sitename.com'],
              'domains_redirect': [
                  {'domain': 'sitename.com', 'destination_domain': 'www.sitename.com'},
              ],
              'ssl': True,
              'ssl_key_path': '../config/ssl.key', # This must be uploaded manually, possibly by a task in the future
              'ssl_cert_path': '../config/ssl.crt', # This must be uploaded manually, possibly by a task in the future
              'basic_auth': False,
              'basic_auth_path': '../config/htpasswd', # This must be uploaded manually, possibly by a task in the future
          },
      }

   add settings for stage/live as needed.


 * call ``bin/fab --list`` for a list of commands

.. note:: when using these tasks, all project-specific tasks have to be decorated
   with the ``@task`` decorator from ``fabric.api``.

Configuration file (config.ini)
===============================

Remember to add config.ini, example:

   [static]
   
   /media/ = py_src/project/media/

and/or

   [static]
   
   /static/ = %(static_files)s

Celery
------

The ``[celery]`` section has some special configuration parameters:

 * ``version`` (default: empty): set the celery version. Other the value ``3.1`` is recognized and triggers the
   usage of the ``celery`` command instead of the django-celery based ``manage.py celeryd``.
 * ``app`` (default: ``project``): the module that contains the ``celery.py`` (see the `celery documentation`_)

Other options
-------------

   [checkout]

   tool = buildout (default)

   tool = virtualenv


   [celery] (if the section is present, celery is enabled)


   [django]

   base = .

   base = project/

   base = py_src/project (doesnt work with buildout yet, as it would try to access py_src/project/bin/django)


   append_settings = true

   append_settings = false

   [static]

   (see above)

   /url-path/ = rel-path-filesystem/

    [sendfile]
    /protected/media/ = ../upload/

.. _celery documentation: http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html