Systers Portal [![Build Status](https://travis-ci.org/systers/portal.svg?branch=master)](https://travis-ci.org/systers/portal) [![Coverage Status](https://coveralls.io/repos/github/systers/portal/badge.svg?branch=master)](https://coveralls.io/r/systers/portal?branch=master)
==============

Systers Portal is for Systers communities to post and share information within
and with other communities.

Website: http://portal.systers.org

Project page: http://systers.github.io/portal/


If you are an Outreachy Applicant, start with reading [this](https://github.com/systers/ossprojects/wiki/Systers-Portal) for meetup features, please go through [this](https://github.com/systers/ossprojects/wiki/Meetup-Features).

Setup for developers (Unix)
---------------------------

1. Make sure you have installed Python 3.6, [pip3](https://pip.pypa.io/en/latest/) and [virtualenv](http://www.virtualenv.org/en/latest/).
1. If working behind a proxy, make sure your environment variables are properly set up. If
   you still get an error due to proxy, use "-E" flag along with "sudo" to export all the
   environment variables.
1. Make sure you have python3-dev installed on your operating system. For Debian, you would additionally require libpq-dev.
   Install by using `sudo apt-get install libpq-dev python3-dev`
1. Make sure you have PostgreSQL installed. For a tutorial on installing
   Postgres, [Django Girls'](http://djangogirls.org) ebook,
   [Tutorials Extension](http://djangogirls.org/resources/), is a reference.
   The info is also on [Django Girls GitHub repository](https://github.com/DjangoGirls/tutorial-extensions/blob/master/en/optional_postgresql_installation/README.md).
1. Clone the repo - `git clone git@github.com:systers/portal.git` and cd into
  the `portal` directory. If working behind a proxy, follow the instructions [here](https://cms-sw.github.io/tutorial-proxy.html).
1. Create a virtual environment with Python 3 and install dependencies:

     ```bash
     $ virtualenv venv --python=/path/to/python3
     $ source venv/bin/activate
     $ pip install -r requirements/dev.txt
     $ sudo apt-get install python-gdal
     ```
1. Create `systersdb` database, where `systersdb` might be any suitable name.
    ```
    $ sudo -i -u postgres
    $ createuser <any name e.g. alice> --pwprompt
    $ psql
    $ CREATE DATABASE systersdb;
    $ \c systersdb;
    $ GRANT ALL PRIVILEGES ON DATABASE systersdb to <the name>;
    ```
1. Fill in the database details in `systers_portal/settings/dev.py`.
1. Run `export SECRET_KEY=foobarbaz` in your terminal, ideally the secret key
  should be 40 characters long, unique and unpredictable. Optionally to set the
  shell variable every time you activate the virtualenv, edit `venv/bin/activate`
  and add to the bottom the export statement.
1. Run `python systers_portal/manage.py migrate`.
1. Run `python systers_portal/manage.py cities_light` for downloading and importing data for django-cities-light.
1. Run `python systers_portal/manage.py createsuperuser` to create a superuser for the admin panel.
  Fill in the details asked.
1. Run `python systers_portal/manage.py runserver` to start the development server. When in testing
  or production, feed the respective settings file from the command line, e.g. for
  testing `python systers_portal/manage.py runserver --settings=systers_portal.settings.testing`.
1. Before commiting run `flake8 systers_portal` and fix PEP8 warnings.
1. Run `python systers_portal/manage.py test --settings=systers_portal.settings.testing`
  to run all the tests.


If you face some issues while installing and making Portal up in your local, have a look at issues labelled as [While Setting up Portal](https://github.com/systers/portal/labels/While%20Setting%20up%20Portal).


Setup for developers (Windows)
------------------------------

1. Make sure you have installed Python 3.6, make sure you the right one (32/64 bits). [Source](https://www.python.org/downloads/). During installation please pay attention to the following details :
- Tick/Select Add Python 3.6 to PATH
- Select Customize Installation (this is important)
- **Tick/Select pip (others, leave as default), this is important**
- Tick install for all users
- Tick add Python to environment variables
- Tick create shortcuts for installed applications
- Precomplie standard libary
- Select install location and hit install
1. Run `pip install virtualenv` using windows command line
1. You would have to install PostgreSQL. Download from [official location](https://www.postgresql.org/download/windows/) or alternative location, you could lookup some PostgreSQL tutorials online if you are completely blank on this. 
1. Clone the repo - `git clone git@github.com:systers/portal.git` and cd into the `portal` directory. Use git CMD or git Bash(unix-like terminal) to do so.
1. Create a virtual environment with Python 3 and install dependencies, using CMD :
 
     ```bash
     $ virtualenv venv
     $ ./venv/Scripts/activate
     $ pip install -r requirements/dev.txt 
     ```
1. Create `systersdb` database, where `systersdb` might be any suitable name.
- Open the SQL Shell for postgresql from the windows start menu or wherever accessible

    ```
    $ Server [localhost]:  Just press enter, leave this empty
    $ Database [postgres]: Just press enter, leave this empty
    $ Port [5432]: This is the default port just press enter, leave this empty
    $ Username [postgres]: This is the default username just press enter, leave this empty
    $ Password for user postgres: Input password you created during installation and press enter
    $ CREATE USER <anyname you want e.g systers> WITH PASSWORD 'your password';
    $ CREATE DATABASE systersdb;
    $ \c systersdb;
    $ GRANT ALL PRIVILEGES ON systersdb TO <username created above>;
    ```
1. Fill in the database details in `systers_portal/settings/dev.py`.
1. Run `set SECRET_KEY=foobarbaz` in your terminal, ideally the secret key
  should be 40 characters long, unique and unpredictable. 
1. Run `python systers_portal/manage.py migrate`.
1. Run `python systers_portal/manage.py cities_light` for downloading and importing data for django-cities-light.
1. Run `python systers_portal/manage.py createsuperuser` to create a superuser for the admin panel.
  Fill in the details asked.
1. Run `python systers_portal/manage.py runserver` to start the development server. When in testing
  or production, feed the respective settings file from the command line, e.g. for
  testing `python systers_portal/manage.py runserver --settings=systers_portal.settings.testing`.
1. Before commiting run `flake8 systers_portal` and fix PEP8 warnings.
1. Run `python systers_portal/manage.py test --settings=systers_portal.settings.testing`
  to run all the tests.

Congratulations! you just set up the Systers Portal on you windows dev enviroment. If you face any issues while installing and making Portal up in your local, have a look at issues labelled as [While Setting up Portal](https://github.com/systers/portal/labels/While%20Setting%20up%20Portal).




Run Portal in a Docker container
--------------------------------

If you wish to view a sneak peek of the Systers Portal, you may use Docker to
preview the Portal.
Note: The following Docker configuration is not intended to be run in
production at the moment. It may be configured to do so in the future.

1. Install [Docker](https://docs.docker.com/installation/).
   Follow the installation steps for your specific operating system:
     * Docker runs natively on a Linux-based system.
     * For Windows and Mac OS X, you should follow instructions for installing
       boot2docker which also installs VirtualBox.
1. Install [docker-compose](http://docs.docker.com/compose/install/).
   Note: fig has been deprecated. Docker-compose replaces fig.
1. Create a new directory on your local system.
1. Enter `git clone git@github.com:systers/portal.git` to clone the Systers
   Portal repository. After the clone is done, change directory (cd) to the
   `portal` directory.
1. Run `docker-compose build`. This pulls the Docker images required to run the
   project and installs the necessary dependencies.
1. **This step will require the Django SECRET_KEY.**
   Run `docker run -e SECRET_KEY=foobarbaz portal_web`.
1. Run `docker-compose run web python systers_portal/manage.py migrate`.
1. Run `docker-compose run web python systers_portal/manage.py cities_light` for downloading and importing data for django-cities-light.
1. *Optional:*
   Run `docker-compose run web python systers_portal/manage.py createsuperuser`
   if you wish to create a superuser to access the admin panel.
1. Run `docker-compose up` to start the webserver for the Django Systers Portal
   project.
1. Systers Portal should be running on port 8000.
     * If you are on Linux, enter `http://0.0.0.0:8000` in your browser.
     * If you are using boot2docker on Windows or Mac OS X, enter
       `http://192.168.59.103:8000/` in your browser. If this IP address
       doesn't work, run `boot2docker ip` from the command line and replace
       the previous IP address in the HTTP request with the IP returned by
       boot2docker.


Documentation
-------------

Documentation for Systers Portal is generated using [Sphinx](http://sphinx-doc.org/)
and available online at http://systers-portal.readthedocs.org/

To build the documentation locally run:
```bash
$ cd docs/
$ make html
```

To view the documentation open the generated `index.html` file in browser -
`docs/_build/html/index.html`.

For more information on semantics and builds, please refer to the Sphinx
[official documentation](http://sphinx-doc.org/contents.html).

You can view the requirements document [here](docs/requirements/Systers_GSoC14_Portal_Requirements.pdf).
