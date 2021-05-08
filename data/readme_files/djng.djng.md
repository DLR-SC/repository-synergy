djng
====

[![Join the chat at https://gitter.im/djng/djng](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/djng/djng?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Kick-start your Django and AngularJS based web applications in minutes.
Your project will be deployed on Heroku so you can focus on building apps and not infrastructure.

The project provides a minimal set of useful libraries to get you started as quickly as possible.
Specific topics are covered by [recipes](https://github.com/djng/djng/wiki).

What you get:

 * Django backend providing a [REST API](http://www.django-rest-framework.org/).
 * AngularJS client including [Restangular](https://github.com/mgonto/restangular) and [UI Router](http://angular-ui.github.io/ui-router/site/#/api/ui.router).
 * Architecture following the [the twelve-factor app methodology](http://12factor.net/).
 * Configured Heroku environment including logging and monitoring.
 * Everything is built on Heroku - No need to commit build artifacts to your repository.

Prerequisites
-------------

 * Installed [Python](http://python.org/) and [Virtualenv](http://pypi.python.org/pypi/virtualenv) in a unix-style environment.
   See this [guide](http://install.python-guide.org/) for guidance.
 * An installed version of [Postgres](http://www.postgresql.org/) to test locally.
   Also create a user and database for your project.
 * Installed [Node.js](http://nodejs.org/).
 * Installed [Grunt](http://gruntjs.com/getting-started) and [Bower](http://bower.io/#install-bower).
 * Installed [Compass](http://compass-style.org/install/).
 * Installed [Heroku Toolbelt](https://toolbelt.heroku.com/).
 * A Heroku user account. [Signup is free and instant](https://signup.heroku.com/signup/dc).

Bootstrap your project
----------------------

	mkdir myproject && cd $_
    wget -qO- https://raw.githubusercontent.com/djng/djng-init/master/djng.sh | bash
    
_Make sure you like what's inside [djng.sh](https://raw.githubusercontent.com/djng/djng-init/master/djng.sh)._

Developing
----------
Watch for changes in your client:

    cd client
    grunt watch

Run the django development server:

    source venv/bin/activate
    cd server
    python manage.py runserver_plus

### Developing locally with Foreman

If you want to execute your local development environment in the same manner as the remote environment 
you can use [Foreman](https://github.com/ddollar/foreman) (it’s installed automatically by the Heroku Toolbelt) to run your Procfile-backed app.

Build your client:

    cd client
    grunt build
    
Set `DJANGO_DEBUG=False` in `server/.env` and collect the static files:

    cd server
    ./manage.py collectstatic --noinput

Run foreman:
    
    foreman start -e server/.env


This ensures that incompatibilities and hard to find bugs are caught before deploying to 
production and treats the application as a holistic unit instead of a series of individual
commands working independently.


Deploying
---------
Add files, commit all your changes and push to heroku:
 
    git add .
    git commit -m 'your changes'
    git push heroku master

How it works
------------

This section covers the setup project process as done by djng-init,
the interaction between the client and the server and the Heroku deployment.

### Environment

#### Django server

[Virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) is used to create an isolated Python environment
for the Django server. The requirements are kept in requirements.txt and requirements_dev.txt:
    
    virtualenv venv –no-site-packages
    source venv/bin/activate
    pip install -r requirements.txt
    pip install -r requirements_dev.txt
 
All environment specific configurations for Django are located in server/.env:

    $ cat serve.env
    DJANGO_DEBUG=True
    DJANGO_SECRET=SUPER_SECRET
    DATABASE_URL=postgres://DBUSER:DBPW@localhost/DBNAME
    DJANGO_FROM_MAIL=me@example.com
    DJANGO_ADMINS=<John Doe> john@example.com
    DJANGO_MANAGERS=<John Doe> john@example.com

This configuration is then used in the Django `settings.py`.

This environment is conveniently loaded by `manage.py` for local development. On Heroku this configuration is 
managed by [config vars](https://devcenter.heroku.com/articles/config-vars). This project uses the handy 
[heroku-config](https://github.com/ddollar/heroku-config) plugin to manage the configuration.

##### AngularJs Client

All client dependencies are managed by npm and bower:

    cd client
    npm install
    bower install

### Serving static assets

All static assets are served by [WhiteNoise](http://whitenoise.evans.io/en/latest/) in production to keep things simple. 
During local development the files are served by the [django.contrib.staticfile](https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#module-django.contrib.staticfiles) 
app directly from the client directory.

**Note:** As this is a SPA Django needs to catch all URLs handled by the client and return the index.html.
Therefore this URL pattern has to come last in your `urls.py` as it would otherwise override all other url definitions.

### Heroku Deployment

This project uses [heroku-buildpack-multi](https://github.com/heroku/heroku-buildpack-multi) to run two buildpacks. 
One is [heroku-buildpack-webapp-client](https://github.com/djng/heroku-buildpack-webapp-client) to build the client and 
the other one is [heroku-buildpack-python](https://github.com/heroku/heroku-buildpack-python) to run Django defined in `.buildpacks`:

    $ heroku config:add BUILDPACK_URL=https://github.com/heroku/heroku-buildpack-multi.git
    $ cat .buildpacks
    https://github.com/djng/heroku-buildpack-webapp-client.git
    https://github.com/heroku/heroku-buildpack-python.git
