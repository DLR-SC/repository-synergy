Crab
====

.. startcrabintro

Crab is a dashboard system for monitoring cron jobs, or other scheduled
tasks.  The Crab server receives messages when tasks start or finish,
and displays the status of all of the tasks via a web interface.  It
can also send notifications by email, for example to warn if a task
fails, is missed or does not complete within its time-out period.

Tasks communicate with the Crab server by JSON messages sent by HTTP
PUT requests.  The finish message includes the status of the job,
and any output from it.  Further messages are used to import and
export the client's crontab, which the server uses to determine the
intended schedule.

.. endcrabintro
.. startcrabinstall

Requirements
------------

Packages
~~~~~~~~

* `crontab`_ (0.15 or newer)
* `CherryPy`_ (`PyPI entry <http://pypi.python.org/pypi/CherryPy>`__)
* `Mako`_ (`PyPI entry <http://pypi.python.org/pypi/Mako/>`__)
* `jQuery`_
* `PyRSS2Gen`_ (optional)
* `Font Awesome`_ (optional)
* `ansi_up`_ (optional)
* `MySQL Connector`_ (needed only if using a MySQL database)

.. _`crontab`: http://pypi.python.org/pypi/crontab/
.. _`CherryPy`: http://www.cherrypy.org/
.. _`Mako`: http://www.makotemplates.org/
.. _`jQuery`: http://jquery.com/
.. _`PyRSS2Gen`: http://pypi.python.org/pypi/PyRSS2Gen/
.. _`Font Awesome`: https://fontawesome.com/
.. _`ansi_up`: https://github.com/drudru/ansi_up
.. _`MySQL Connector`: http://dev.mysql.com/downloads/connector/python/

Python Version
~~~~~~~~~~~~~~

Crab server
  Has been tested on Python 2.6, 2.7 and 3.2.

Client library and utilities
  Works with Python 2.4 in addition to the above versions (but
  may require the ``pytz`` and ``simplejson`` packages also to be
  installed).

Installation
------------

The Crab server, clients and libraries can be installed as follows::

    python setup.py install

If necessary, the ``--install-data`` option can be used to configure
the location in which the templates (``templ``), resources (``res``)
and example files (``doc``) should be installed.

To run Crab without installing it, and if any of the Python dependencies
listed above can not be installed, they can be symlinked into the ``lib``
directory in the following locations::

    lib/PyRSS2Gen.py
    lib/cherrypy
    lib/crontab
    lib/mako

The jQuery JavaScript library should be copied or symlinked into
Crab's ``res`` directory as::

    res/jquery.js

To use Font Awesome icons, copy or symlink its ``webfonts`` directory into
Crab's ``res`` directory, and also place its stylesheet inside
that subdirectory, giving::

    res/webfonts/fontawesome-all.css
    res/webfonts/fa-*.*

Note that Font Awesome is not backward compatible between major
version numbers.  Crab now uses version 5 of Font Awesome.

To use ansi_up to interpret ANSI color commands in cron job output,
copy or symlink the ``ansi_up.js`` file into Crab's ``res`` directory::

    res/ansi_up.js

.. endcrabinstall

The Crab Server
---------------

.. startcrabserver

Database Creation
~~~~~~~~~~~~~~~~~

A SQLite database file can be prepared for Crab using the
schema provided::

    % sqlite3 crab.db < doc/schema.sql

Alternatively if you are going to be using MySQL for your
Crab database, create the database::

    % mysqladmin -u root -p create crab

and create a user account for crab, changing the password
(the "identified by" clause) to something suitable::

    % mysql -u root -p mysql
    > create user 'crab'@'localhost' identified by 'crab';
    > grant all on crab.* to 'crab'@'localhost';
    > flush privileges;

You can prepare a table creation script suitable for MySQL
using the Makefile in the `doc` directory of the source package::

    % make -C doc schema_mysql.sql
    % mysql -u crab -p crab < doc/schema_mysql.sql

Configuration
~~~~~~~~~~~~~

The Crab server is configured by a ``crabd.ini`` file which can
be placed either in ``/etc/crab/`` or ``~/.crab/``.  Note that this
is a CherryPy configuration file, which is read slightly differently to
typical ``.ini`` files which use Python's ConfigParser. ::

    % cp doc/crabd.ini ~/.crab/

The example ``crabd.ini`` file should be edited to uncomment the
``[crab]`` and ``[store]`` sections.  The ``home`` and ``file`` entries
must point to the location of Crab's data files and the database file
just created.  By default the data files are installed in ``share/crab``
relative to the Python system prefix (``sys.prefix``).

There is also an ``[outputstore]`` section in the server configuration
file.  This allows the output from cron jobs and raw crontab files
to be stored separately, and can be used to prevent the main
database from becoming excessively large.

If you would like to have Crab delete the history of job events over
a certain age, you can have it run a cleaning service by enabling the
``[clean]`` section of the server configuration file.  Here you can
select the cleaning schedule and length of history to keep.  A fairly
frequent cleaning schedule is recommended to avoid the accumulation
of a large number of old events so that each cleaning operation does
not take long.  If the file output store is being used, the cleaning
service will remove only the event records and not the output
text.  You can remove old output text separately, for example by running
in your output store directory::

    % find output -type f -mtime +90 -delete
    % find output -type d -empty -delete

Running
~~~~~~~

The Crab server is run as ``crabd``.  When the server
is executed directly, it will stay in the foreground::

    % crabd

It can also be run in the background with the ``crabd-check`` script,
which checks that it is not still running from a previous invocation of
``crabd-check``.  Therefore this is suitable for running from cron
to keep the server running::

    PYTHONPATH=/path/to/crab/lib
    PATH=/path/to/crab/scripts:/bin:/usr/bin
    7-57/10 * * * * CRABIGNORE=yes crabd-check

With the server running, the Crab dashboard should be visible from
a web browser, by default on port 8000.  The Crab clients will use this
same web service to communicate with the server.

Migrating Job Information
~~~~~~~~~~~~~~~~~~~~~~~~~

The Crab server has the ability to export and import cron job information,
including:

* The list of cron jobs.
* The configuration and notifications attached to each job.
* General host/user-based notifications.
* Raw crontabs.

You can write this information to a JSON file using the ``--export``
option::

    % crabd --export job_information.json

Similarly you can read information with the ``--import`` option::

    % crabd --import job_information.json

This merges the information from the file with the server's existing
configuration.  You can also give a file name of ``-`` to export
to standard output or read from standard input.

.. endcrabserver

Monitoring Cron Jobs
--------------------

.. startcrabclient

There are two Crab client commands: the ``crab`` utility, and
the ``crabsh`` wrapper shell.  Cron jobs can either be run under
``crabsh``, or they can be updated to report their own status
to the Crab server.

Configuration
~~~~~~~~~~~~~

The Crab clients are configured by a ``crab.ini`` file which can
be placed either in ``/etc/crab/`` or ``~/.crab/``.  The file
specifies how to contact the Crab server, and the username and
hostname which the client will use to report cron jobs. ::

    % cp doc/crab.ini ~/.crab/

The configuration can be checked with the ``crab info`` command.
This reports the settings, and indicates which configuration
files were read.  It is a useful way to check that everything
is in order before importing a crontab.

The ``crabsh`` Wrapper
~~~~~~~~~~~~~~~~~~~~~~

``crabsh`` is a wrapper script designed to act like a shell.  It can
therefore be invoked by cron via the ``SHELL`` variable, for example::

    PYTHONPATH=/path/to/crab/lib
    SHELL=/path/to/crab/scripts/crabsh
    0 10 * * 1-5 CRABID=test echo "Test cron job"

Where the rules following the ``SHELL`` assignment will be run with the
wrapper.  The ``PYTHONPATH`` will need to be set if Crab is not installed
where the system can find it.  Cron requires the full path when
specifying the ``SHELL``. The ``CRABID`` parameter is used to
give the cron job a convenient and unique name.  This is optional,
unless there are multiple jobs with the same command,
in which case they would otherwise be indistinguishable.
However if it specified, then it must be unique for a given
host and user, as the Crab server will use it in preference
to the command string to identify cron job reports.

``crabsh`` will notify the server when the job starts, and when it finishes,
assuming it succeeded if the exit status was zero.

Crab-aware Cron Jobs
~~~~~~~~~~~~~~~~~~~~

Alternatively a cron job can report its own status to the Crab server.
The most straightforward way to do this is to execute the ``crab``
utility.  So a cron job written as a shell script could include
commands such as::

   % crab start -c "$0"
   % crab finish -c "$0"
   % crab fail -c "$0"

In this way you can also report a warning with ``crab warning`` or an
unknown status with ``crab unknown``.

Python
    If the cron job is written in Python, it could import ``crab.client``
    directly and make use of the ``CrabClient`` class.

Perl
    A Perl module `WWW::Crab::Client`_ is also available.

.. _`WWW::Crab::Client`: http://search.cpan.org/perldoc?WWW::Crab::Client

Other languages
    Other language libraries could be written.  They would need to make
    HTTP PUT requests with an appropriate JSON message.

Managing the Cron Job List
~~~~~~~~~~~~~~~~~~~~~~~~~~

The Crab server needs to be given the schedule for each job so that it
can detect when a job is late or missed.  This is done by "importing"
a user's crontab file::

    % crab import

The database entries can then be checked by "exporting" them,
again using the ``crab`` utility::

    % crab export
    > CRON_TZ=Pacific/Honolulu
    > 0 10 * * 1-5 CRABID=test echo "Test cron job"

The output is a set of crontab-style lines representing the entries
from the database.  The crontab can be retrieved exactly as last imported
(from a separate database table containing the raw crontab) by giving
the ``--raw`` option as follows::

    % crab export --raw

This is useful as a backup in case a crontab is accidentally lost.
However it will not contain any new jobs which have been added automatically
by the Crab server since the last import.

Cron Job Parameters
~~~~~~~~~~~~~~~~~~~

In order to specify the Crab specific parameters of a cron job,
Bourne-style shell variables at the start of a command are used.
The syntax for each cron job is as follows::

    <schedule> [CRABIGNORE=yes] [CRABID=<identifier>] <command string>

A command starting with CRABIGNORE set to a value other than
0/no/off/false will be ignored when importing a crontab,
and ``crabsh`` will not report its status to the Crab server.

A CRABID specification will override any CRABID environment variable
in effect, and is a better way of specifying the identifier as it
can not apply to more than one cron job.  There should not be multiple
jobs with the same identifier for any user and host.

The Crab parameters can be placed in any order before the remainder of the
command string, but they must precede any other variables.

Environment Variables
~~~~~~~~~~~~~~~~~~~~~

CRABCLIENTHOSTNAME
    The host name to be used by Crab clients to identify themselves,
    overriding any value in the configuration files.

CRABECHO
    If present and not set to 0/no/off/false then ``crabsh`` will print out
    the standard output and standard error it receives from the cron job.
    This allows the output to be sent by email via cron's default
    behavior as well as being captured by the Crab system.

CRABHOME
    If present overrides the Crab server home directory, where the
    ``res`` and ``templ`` directories are to be found.

CRABHOST
    Specifies the Crab server to which clients should connect, overriding
    the setting in the configuration file.

CRABID
    Specifies the job identifier which ``crabsh`` will use to file reports
    if there is no ``CRABID=`` variable at the start of the cron command.
    This should be used with caution to avoid specifying the same
    identifier for multiple cron jobs.

CRABIGNORE
    Prevents Crab from acting on specific cron jobs.  Jobs imported
    with this value present and not set to 0/no/off/false will not
    be entered into the database.  Additionally if the ``crabsh``
    wrapper script is used to run such a job, it will not report its
    status to the Crab server.

CRABPIDFILE
    Gives the path to a PID file which ``crabsh`` should use to control
    the execution of a cron job.  When this parameter is set, it will
    use the file to try not to run multiple copies of the job at the
    same time.  Each job should have a separate PID file, so this
    parameter is most conveniently given at the start of a command string.

CRABPORT
    Specifies the port on the Crab server, overriding the setting in the
    configuration file.

CRABSHELL
    The shell which ``crabsh`` will use to invoke the cron job command.
    Defaults to ``/bin/sh`` regardless of the user's shell to replicate
    cron's behavior.

CRABSYSCONFIG
    The directory to be searched for system-level configuration files.
    If not set, then /etc/crab will be used.

CRABUSERCONFIG
    A directory to search for user-level configuration files.  If not
    set then ~/.crab will be used.

CRABUSERNAME
    The user name to be used by Crab clients to identify themselves,
    overriding any value in the configuration files.

CRON_TZ
    Cron reads this variable to know in which timezone to interpret
    the crontab schedule.  When the server receives a crontab,
    it will check for this timezone and use it to override the
    general timezone which the ``crab`` utility will send with
    the crontab (if it is able to determine it).

MAILTO
    Configures the email address to which cron sends email.  This is
    useful when ``CRABECHO`` is on, or if ``crabsh`` needs to report
    a failure to contact the Crab server.

SHELL
    Cron uses this variable to select the shell which will be used
    to execute the cron jobs.  The full path must be specified.
    Crab does not use this variable itself.

TZ
    This can be set to the system timezone, in which case ``crab import``
    will use it as the default timezone for the crontab.


.. endcrabclient
.. startcrabweb

The Web Interface
-----------------

The Crab dashboard allows the status of the jobs to be monitored.
On this page, the job status column will change color to indicate
the status, and it will flash while the job is running.  Clicking
on the status will lead to the most recent output recorded for
the job.

The host and user columns contain links leading to a summary page
of the cron jobs for a given user or host.  From this page,
the links below each table can be used to show deleted jobs,
and to display the raw crontab as last imported.

Clicking on a job ID or command link leads to the job information
page, giving a summary of the job's parameters and a table of the
most recent events.  Clicking the status of any job finish
event leads to the corresponding output.

Job Configuration
~~~~~~~~~~~~~~~~~

Below the summary on the job information page, there is a link
allowing the job's configuration to be edited.
If a job is deleted, then its configuration is considered to be
orphaned.  In this case, when configuring a job for which
no configuration exists, the system will offer a list of
orphaned configurations for re-linking.  This should be used
when the job is actually the continuation of a previous job.
Note that notifications which are attached to specific jobs
are linked via the configuration.  Therefore re-linking the
configuration will re-attach all associated notifications.

However this problem can generally be avoided by giving the jobs
suitable names via the ``CRABID`` parameter.  Crab will then be able
to recognize jobs by name even if the command string changes.

The grace period
specifies how close to the scheduled time the job must start
in order not to be considered missed.  The time-out is the
maximum expected duration of the job.  If it runs for longer
than this, it will be marked as stopped with timed-out (error) status.
Note that the job may actually still be running when this status is
displayed.  If the job is restarted, or reported as already running,
during the time-out period, then the time-out is reset.
If either of these timing parameters are left blank then the default
values of 2 minutes grace period and 5 minutes time-out will be used.

Regular expression patterns used to determine success or failure
and to identify warnings can be given.  These patterns are compared
to the standard output and standard error of the job when it finishes,
but do not override a more severe status.  For example if a job is reported
as finishing with failure, then it will be logged as such even
if the success or warning patterns match.  If none of the patterns
match then the status is logged as it was reported, unless a
success pattern was defined.  If the success pattern does not match
then the status will be failure if the was no failure pattern
or unknown if there was a failure pattern which did not match.

The "Inhibit execution" checkbox can be use to temporarily
request that a job not be run.  This setting is stored in
the Crab server and passed to the client when it reports
that a job is being started.  Note that there is no guarantee
that the job will not be run while this option is selected: the
client could fail to connect to the server before
starting the job, or it could choose to ignore the
inhibit setting.  The ``crabsh`` wrapper shell reads a
configuration parameter ``allow_inhibit`` from the ``crabsh``
section of the ``cran.ini`` file to determine whether
inhibit requests should be honored.  (The default value
is true, i.e. it will not run the job if it receives the
inhibit flag in response to its job starting message.)

The job configuration page also allows jobs to be marked as deleted.
Normally this would be done by importing a new crontab without that
job in it, but having this available on the web interface is useful
in situations such as the host being inaccessible.  Note that
if a start or finish event is received from the job, but the
Crab server is still able to identify it, then the job
should be automatically marked as not deleted.

There is also the option to alter the job identifier.  However
care must be taken to also update it in the job itself, for
example via the ``CRABID`` parameter in the crontab.  If the
identifier is changed via the web server but not in the job,
then the Crab server will identify it as a new job the next time it
receives a start or finish report from it.

Notifications
~~~~~~~~~~~~~

Crab includes a configurable notifications system, which currently
supports sending notification messages by email.  Notifications
can either be attached to a specific job, or configured
by host name and/or by user name.

A link below the summary on the job information page allows
notifications to be attached to that job.  Check-boxes
for each notification can be used to select which
severity of events should be featured, and whether the job
output should be included.  The schedule box should contain
a cron-style schedule specification (e.g. ``0 12 * * *``),
and if left blank, will default to the value given in the
``crabd.ini`` file, allowing all notification schedules to be
managed in one place.  Notifications will only be sent if there
are relevant events, so it is possible to request
almost-immediate error warnings by including a schedule of
``* * * * *`` and selecting errors only.

The add and delete links can be used to
add and remove notifications, but the changes are not saved
until the ``Configure`` button is clicked.

The drop-down menu which appears when the mouse is positioned
over the Crab heading at the top of each page includes a link to
the main notifications page.  This allows notifications to be
configured by host name and/or by user name.  Notifications
will include any jobs where the host and user match the specified
values, but if either is left blank, then it will match all entries.

Additional Job Actions
~~~~~~~~~~~~~~~~~~~~~~

Depending on the state of a job, additional links may appear
below the summary on the job information page.
These are:

* "Clear status": this appears when the job is in a warning or
  error state.
  Selecting this option sets the job state to "Cleared",
  which you can use to acknowledge the problem.
  The job's status will then be shown in green on the dashboard.

* "Resume inhibited job": this appears when the inhibit setting
  has been selected on the job configuration page.
  The link provides a convenient means of removing the
  inhibit setting.

.. endcrabweb

Screenshots
~~~~~~~~~~~

* The dashboard page:

    .. image:: http://grahambell.github.io/crab/img/screenshot-dashboard.png

* View of cron jobs by host:

    .. image:: http://grahambell.github.io/crab/img/screenshot-host.png

* Information page for a cron job:

    .. image:: http://grahambell.github.io/crab/img/screenshot-job.png

Copyright
---------

| Copyright (C) 2012-2014 Science and Technology Facilities Council.
| Copyright (C) 2015-2018 East Asian Observatory.

Crab is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Crab.  If not, see <http://www.gnu.org/licenses/>.

Additional Links
----------------

* `Crab entry on PyPI <https://pypi.python.org/pypi/crab>`_
* `Documentation at Read the Docs <http://crab.readthedocs.io/en/latest/>`_
* `Repository at GitHub <https://github.com/grahambell/crab>`_
* `ADASS article about Crab <http://www.aspbooks.org/a/volumes/article_details/?paper_id=35592>`_
