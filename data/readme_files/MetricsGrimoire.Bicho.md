Important notice (2018-09-19)
-----------------------------

This project lacked active development for a long while, and it is very
unlikely that it gets develpment attention in the future. For those
interested in retrieving and processing data from issue tracking repositories
(bug tracking repositories), please consider checking GrimoireLab [1] and
GrimoireLab-Perceval [2] 

[1] https://chaoss.github.io/grimoirelab
[2] https://github.com/chaoss/grimoirelab-perceval


Description
-----------

Bicho is a command line-based tool used to parse bug/issue tracking
systems. It gets all the information associated with issues and stores
them in a relational database. (It is part of the MetricsGrimoire suite,
which produces data for vizGrimoire to analyze and visualize.)

Currently Bicho supports:
- Bugzilla
- Sourceforge.net (abandoned)
- JIRA
- Launchpad
- GitHub
- Maniphest
- Redmine
- Gerrit
- Allura (unstable)
- Google Code (abandoned)
- Trac


 License
---------

Bicho is licensed under GNU General Public License (GPL), version 2 or later.


 Download
----------

Home page:
* http://metricsgrimoire.github.com/Bicho/

Releases:
* https://github.com/MetricsGrimoire/Bicho/downloads

Latest version:
* git://github.com/MetricsGrimoire/Bicho.git


 Requirements
------------

 * Python >= 2.4
 * Python Storm. You'll also need the following Python libraries:
   - mysqldb (default engine should be set to MYISAM)
   - python-launchpadlib (only for for Launchpad backend)
 * Beautiful Soup library: error-tolerant HTML parser for Python
 * python-feedparser
 * dateutil


 Installation
-------------

 You can install Bicho running the setup.py script:

  # python setup.py install

 For the impatients:

  $ bicho --help


 Running Bicho
--------------

This is a quick list of example commands you would run in your terminal to
get bug data from various kinds of bug trackers and capture it in a
database on your local machine. The general format is:

$ bicho --db-user-out=[YOUR DATABASE USERNAME] --db-password-out=[YOUR DATABASE PASSWORD] --db-database-out=[NAME OF DATABASE] -d [DELAY BETWEEN REQUESTS IN NUMBER OF SECONDS] -b [ABBREVIATION FOR BACKEND] -u [BUGTRACKER URL IN QUOTES]

For more guidance, please see doc/UserManual.txt .

It is very important to use a delay. If you run Bicho against big sites
without a delay between bug queries, your IP address could be banned!

E1. Getting information from a project that uses Bugzilla, like Bicho ;)

$ bicho --db-user-out=[DB USER] --db-password-out=[DB PASS] --db-database-out=[DB NAME] -d 15 -b bg -u "https://bugzilla.libresoft.es/buglist.cgi?product=bicho"

E2. Getting information from a project hosted on sourceforge.net

$ bicho --db-user-out=[DB USER] --db-password-out=[DB PASS] --db-database-out=[DB NAME] -d 15 -b sf -u "http://sourceforge.net/tracker/?atid=516295&group_id=66938"

E3. Getting information from a project using JIRA

$ bicho --db-user-out=[DB USER] --db-password-out=[DB PASS] --db-database-out=[DB NAME] -d 15 -b jira -u "http://support.petalslink.com/browse/PETALSMASTER"

E4. Getting information from a project using Launchpad

$ bicho --db-user-out=[DB USER] --db-password-out=[DB PASS] --db-database-out=[DB NAME] -d 15 -b lp -u "https://bugs.launchpad.net/openstack"

E5. Getting information from a project using Allura

$ bicho --db-user-out=[DB USER] --db-password-out=[DB PASS] --db-database-out=[DB NAME] -d 15 -b allura -u "http://sourceforge.net/rest/p/allura/tickets"

E6. Getting information from a project using GitHub

$ bicho --db-user-out=[DB USER] --db-password-out=[DB PASS] --db-database-out=[DB NAME] -b github -u "https://api.github.com/repos/composer/composer/issues" --backend-token=[API TOKEN]

E7. Getting information from a project using Redmine

$ bicho --db-user-out=[DB USER] --db-password-out=[DB PASS] --db-database-out=[DB NAME] --backend-user=[REDMINE USER] --backend-password=[REDMINE PASSWORD] -d 1 -b redmine -u "https://www.bitergia.net/"

E8. Getting information from Maniphest

$ bicho --db-user-out=[DB USER] --db-password-out=[DB PASS] --db-database-out=[DB NAME] --backend-token=[API TOKEN] -b maniphest -u https://phabricator.wikimedia.org [--no-resume]

E9. Getting information from Trac

$ bicho --db-user-out=[DB USER] --db-password-out=[DB PASS] --db-database-out=[DB NAME] -b trac -u https://fedorahosted.org/freeipa/

E10. Getting information from Review Board

$ bicho --db-user-out=[DB USER] --db-password-out=[DB PASS] --db-database-out=[DB NAME] -n 25 -b reviewboard -u https://reviews.apache.org/groups/geode/


Known issues
------------

Newer versions of MySQL server may raise the next error message:
```
Error Code: 1406. Data too long for column
```

To avoid this problem, please update your MySQL configuration removing `STRICT_TRANS_TABLES` value from `sql-mode` parameter.


 Roadmap
---------

0.93:
* The updated list of bugs to be fixed can be found here https://github.com/MetricsGrimoire/Bicho/issues?milestone=1&page=1&state=open
* Incremental support broken by issues updated during the download bug #28
* Incorrect order downloading issues from Bugzilla #20
* Incoherent number of issues after webkit analysis bug bugzilla support #26
* Error in database character sets while comparing dates #8
* Problem cloning repo in case insensitive systems #12
* Incremental feature doesn't support multiple projects in the same database #30

1.0:
* https://github.com/MetricsGrimoire/Bicho/issues?milestone=2&page=1&state=open
* issues_log for bugzilla and launchpad
** Launchad support for issues_log table enhancement launchpad support #24
** More efficient and cleaner code for the table issues_log for bugzilla
* New table with information about executions (date, issues downloaded, etc ..)
* Tests, tests and tests
* Improved debug mode with more useful details
* Network fault tolerance (in order to survive to connection issues)
* New backends:
** FusionForge


 Improving Bicho
----------------

Source code, wiki and ITS available on GitHub:
* https://github.com/MetricsGrimoire/Bicho

Please write to the developers mailing at
* metrics-grimoire _at _ lists.libresoft.es

If you want to receive updates about new versions, and keep in touch
with the development team, consider subscribing to the list. It is a
very low traffic list (< 1 msg a day):

* https://lists.libresoft.es/listinfo/metrics-grimoire


 Credits
--------

Bicho has been originally developed by the GSyC/LibreSoft group at the
Universidad Rey Juan Carlos in Mostoles, near Madrid (Spain). It is
part of a wider research on libre software engineering, aiming to gain
knowledge on how libre software is developed and maintained.


 FAQ
----

F1. Bicho crashed with 'UnicodeEncodeError' exception

UnicodeEncodeError appears when it is not possible to write the data in the
database with the encoding used by this one. To avoid that, set your database
to use UTF-8. For instance:

CREATE DATABASE [DB NAME] CHARACTER SET utf8 COLLATE utf8_unicode_ci;

F2. What is the database schema?

There is a nice PNG schema in the directory /doc/database .

F3. How can I create a new backend?

Tell us through the contact information above that you want to create a new
backend. We'll try to give you as much information as possible.

Whenever possible, we want to use available APIs. However, some old
bugtrackers used to not have APIs, and even today, some APIs don't give us
all of the information that we want. So a new backend needs to be able to
fall back to HTML scraping and parsing via Beautiful Soup in cases where the
bug tracker's API doesn't exist (maybe an old version of Bugzilla/JIRA/etc.)
or doesn't provide stuff we want.

While writing a new backend, please also write tests per tests/README.md .

F4. How can I submit a bug report?

Use the GitHub issue tracker: https://github.com/MetricsGrimoire/Bicho/issues .
