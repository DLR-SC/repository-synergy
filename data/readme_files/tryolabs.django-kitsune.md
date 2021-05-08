:Author:
	Raul Garreta - Tryolabs <raul@tryolabs.com>

:Project Website:
	https://github.com/tryolabs/django-kitsune


***********
Description
***********

A Django Admin app to perform host server monitoring. A control panel will be added to the Admin in order to configure hosts, checks and monitor check results.
Notification rules can be defined to notify administrator users by mail.
All host shall have access to a common database in order to get information about scheduled jobs and check jobs to run.


***********
Screenshots
***********

.. image:: http://www.tryolabs.com/static/images/kitsune_jobs.jpg

.. image:: http://www.tryolabs.com/static/images/kitsune_job.jpg


********
Features
********

* Hosts

  * Add hosts to monitor

* Checks

  * Add jobs with checks to be performed
  * Schedule
  * Check to be performed
  * Host to check
  * Select users or groups to be notified
  * Configure notification rules
  * Select how to render results
  * Set amount of log history to keep

* Custom Checks

  * You can implement your own checks by implementing a subclass of `kitsune.base.BaseKitsuneCheck`

* Nagios Checks

  * A builtin check is provided that wrapps any Nagios check.
  * You can use any existing Nagios check within django-kitsune

* Logs

  * Log and list check results

* Result Renderers

  * Can implement renderers by implementing a subclass of `kitsune.renderers.KitsuneJobRenderer`
  * Returns a html with the corresponding result that will be rendered within result listings.

* List Checks

  * Host name, last time performed, last result, next scheduled run.

* Notification Rules

  * Notifications through e-mail.
  * Configure who to notify: Groups or Users.
  * Configure when to trigger a notification.
  * Configure the frequency of notifications to avoid spam emails :)

* All configurations are made through a graphic UI within admin panel.


************
Requirements
************

* Python 2.6 and higher.
* Nagios plugins: ``sudo apt-get install nagios-plugins`` (if you want to use Nagios checks).


************
Installation
************

To install Kitsune:

1. ``easy_install django-kitsune`` or download package and execute ``python setup.py install``
2. Add ``'kitsune'`` to the ``INSTALLED_APPS`` in your project's ``settings.py``
3. Configure ``cron`` in every host to run a kitsune management command by running ``crontab`` command::

	* * * * * /path/to/your/project/manage.py kitsune_cron

Every minute cron will run a management command to check pending jobs.
Note that both, django-kitsune and your project must be installed in each host, and each host must have access to the common database (where kitsune tables shall be stored).


*************
Configuration
*************

Kitsune can be configured via the following parameters, to be defined in your project settings file:

* ``KITSUNE_RENDERERS``: List of modules that contain renderer classes, eg:: ``KITSUNE_RENDERERS = ['myproject.myapp.renderers']``.

Kitsune comes with a default renderer ``kitsune.renderers.KitsuneJobRenderer``.


*****
Usage
*****

Add a new Host
--------------

Add a Nagios check
------------------

For example, to add a check_disk, do the following steps:

1. Within Admin go to Kitsune -> Jobs -> Add job
2. Fill the necessary fields, eg:

   * Name: check_disk
   * Host: select a job from the combobox
   * Command: select nagios wrapper: ``kitsune_nagios_check``
   * Args: you must provide a special parameter `check` with the name of the nagios check eg: check=check_disk.

   Then provide the necessary nagios check arguments, in this case: -u=GB -w=5 -c=2 -p=/
   To sum up, the string of arguments will be: ``check=check_disk -u=GB -w=5 -c=2 -p=/``

3. Select the result Renderer, eg: KitsuneJobRenderer

4. Configure scheduling options, eg: Frequency: Hourly, Params: ``interval:1``.

   Params are semicolon-separated list of `rrule <http://labix.org/python-dateutil>`_ parameters.
   
   This will schedule the check to be run every 1 hour.

5. Configure log options, last logs to keep specifies the last N logs to keep.

6. Configure Notification rules.
   
   Every check returns a status code of ``0=OK, 1=WARNING, 2=CRITICAL ERROR, 3=UNKNOWN ERROR`` with its corresponding status message.
   With notification rules you must set the:

   * ``Threshold`` (the status code to be reached)
   * ``Rule type``: 

     * ``Last time``: triggered when last result reached the threshold.
     * ``N last times``: triggered when last N results reached the threshold.
     * ``M of N last times``: triggered when M of the last N results reached the threshold.
       ``Rule N`` and ``Rule M`` parameters.

7. Notification frequency:

   * ``Interval unit``, ``Interval value`` sets the maximum frequency to receive email notifications. These are useful to avoid filling admin inbox with notification mails.
   * ``User/Group`` specifies the users or group of users to be notified. These must be staff users and shall be created within admin.


Add a custom check
------------------

In order to implement a custom check, you must implement a class that is subclass of ``kitsune.base.BaseKitsuneCheck``.

Within this class, you must implement the method ``check(self, *args, **options)``. For example::

	from kitsune.renderers import STATUS_OK, STATUS_WARNING, STATUS_CRITICAL, STATUS_UNKNOWN
	from kitsune.base import BaseKitsuneCheck
	
	class Command(BaseKitsuneCheck):
	    help = 'A simple test check.'
	    
	    def check(self, *args, **options):
	        self.status_code = STATUS_OK
	        
	        if self.status_code == STATUS_OK:
	            self.status_message = 'OK message'
	        elif self.status_code == STATUS_WARNING:
	            self.status_message = 'WARNING message'
	        elif self.status_code == STATUS_CRITICAL:
	            self.status_message = 'CRITICAL message'
	        else:
	            self.status_message = 'UNKNOWN message'

With ``*args and **options`` you will receive the arguments and options set from the Args string.
Modules that implement checks are Django management commands, and must live within management.commands package of an app within your project.

Add a custom renderer
---------------------

Renderers are in charge to render the results within the admin panel. They will take the status code and status message and return a html.
If you want to implement your own renderer, you must implement a class that is sublcass of ``kitsune.renderers.KitsuneJobRenderer``.
You must implement to methods: ``get_html_status(self, log)`` that receives a log and and returns a html for status code.
``get_html_message(self, log)`` that recevies a log and returns a html for status message.
For example::

	from django.template.loader import render_to_string
	from kitsune.renderers import KitsuneJobRenderer
	from kitsune.base import STATUS_OK, STATUS_WARNING, STATUS_CRITICAL, STATUS_UNKNOWN
	
	class MyJobRenderer(KitsuneJobRenderer):
	    
	    def get_html_status(self, log):
	        return render_to_string('kitsune/status_code.html', dictionary={'status_code':int(log.stderr)})
	        
	    def get_html_message(self, log):
	        return 'All OK!'
        
Then you must specify where to get this renderer with the ``KITSUNE_RENDERERS`` at your project settings (see bellow).

***************
Acknowledgments
***************

Kitsune scheduling system is based on   `django-chronograph <https://bitbucket.org/wnielson/django-chronograph>`_. 


