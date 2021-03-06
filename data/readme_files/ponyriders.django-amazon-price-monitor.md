|Build Status| |codecov.io| |Requirements Status| |Stories in Ready| |Landscape|

.. contents:: Table of Contents

django-amazon-price-monitor
===========================

Monitors prices of Amazon products via Product Advertising API.

**Necessary settings changes for upcoming version 0.8 can be found in the** `history <https://github.com/ponyriders/django-amazon-price-monitor/blob/master/HISTORY.rst>`_ **.**
UPDATE: 0.8 will never come, see the end of life announcement below.

END OF LIFE
-----------

**!!! IMPORTANT !!!**


Since January 23rd 2019 the efficiency guidelines for using the Product Advertising API have changed dramatically.
Requests limits for the API are now calculated based on the revenue generated with the Amazon Associate account the
Product Advertising API is connected with.

You can find the details here: https://docs.aws.amazon.com/AWSECommerceService/latest/DG/TroubleshootingApplications.html#efficiency-guidelines

**For django-amazon-price-monitor this means the END OF LIFE from now on.**

But why?

We started the project to solve the issue of saving money with Amazon while having control over your data by self
hosting this project. To continue maintaining and extending the project we'd need to have enough revenue in our
associate account, which we do not have. The result is that our API account used for developing this project is blocked
and we cannot continue. Also our private little instance of pricemonitor, used by some of our friends and us, will be
shut down, too.

The changes in the guidelines make it pretty hard for small projects that do not primarily focus on generating revenue
with Amazon to continue. As the `django-amazon-price-monitor` did not get that much love in the last months and years
from us as we focused on other things, the only logic consequence for us is to pull the plug.

Thanks to all involved for participating in this journey with us!

Best

Alex + Martin


Basic structure
---------------

This is a reusable Django app that can be plugged into your project. It
consists basically of this parts:

-  Models
-  Frontend components
-  Angular Frontend API
-  Amazon API component

Models
~~~~~~

-  Product

   -  representation of an Amazon product

-  Price

   -  representation of a price of an Amazon product at a specific time

-  Subscription

   -  subscribe to a product at a specific price with an email
      notification

Frontend components
~~~~~~~~~~~~~~~~~~~

The frontend displays all subscribed products with additional
information and some graphs for price history.

The features are the following:

-  list products
-  show product details
-  show product price graphs
-  add subscriptions
-  adjust subscription price value
-  delete subscriptions

Angular Frontend API
~~~~~~~~~~~~~~~~~~~~

Simply the API consumed by AngularJS, based on Django REST Framework.

Amazon API component
~~~~~~~~~~~~~~~~~~~~

Fetches product information from Amazon Product Advertising API through
several tasks powered by Celery and weaves the data into the models.

License
-------

This software is licensed with the MIT license. So feel free to do with
it whatever you like.

Setup
-----

Prerequisites
~~~~~~~~~~~~~

+--------+----------------------+-----------------+------+
| Python | 3.4                  | 3.5             | 3.6  |
+========+======================+=================+======+
| Django | 1.8, 1.9, 1.10, 1.11 | 1.9, 1.10, 1.11 | 1.11 |
+--------+----------------------+-----------------+------+

For additional used packages see `setup.py <https://github.com/ponyriders/django-amazon-price-monitor/blob/master/setup.py#L23>`__.

Included angular libraries
~~~~~~~~~~~~~~~~~~~~~~~~~~

-  angular-django-rest-resource (`commit:
   81d752b363668d674201c09d7a2ce6f418a44f13 <https://github.com/blacklocus/angular-django-rest-resource/tree/81d752b363668d674201c09d7a2ce6f418a44f13>`__)

Basic setup
~~~~~~~~~~~

Add the following apps to *INSTALLED\_APPS*:

::

    INSTALLED_APPS = (
        ...
        'price_monitor',
        'price_monitor.product_advertising_api',
        'rest_framework',
    )

Then migrate:

::

    python manage.py migrate

Adjust the settings appropriately, `see next chapter <#settings>`__.

Include the url configuration.

Setup celery - you'll need the beat and a worker.

Settings
~~~~~~~~

*The values of the following displayed settings are their default
values. If the value is '...' then there is no default value.*

Must have settings
^^^^^^^^^^^^^^^^^^

The following settings are absolutely necessary to the price monitor
running, please set them:

Celery
''''''

You need to have a broker and a result backend set.

::

    CELERY_BROKER_URL = ...
    CELERY_RESULT_BACKEND = ...
      
    # some additional settings
    CELERY_ACCEPT_CONTENT = ['pickle', 'json']
    CELERY_CHORD_PROPAGATES = True

Rest-Framework
''''''''''''''

We use Rest-Framework for Angular frontend:

::

    REST_FRAMEWORK = {
        'PAGINATE_BY': 50,
        'PAGINATE_BY_PARAM': 'page_size',
        'MAX_PAGINATE_BY': 100,
    }

Site URL
''''''''
Specify the base URL under which your site will be available. Defaults to: *http://localhost:8000*
Necessary for creating links to the site within the notification emails.

::

    # base url to the site
    PRICE_MONITOR_BASE_URL = 'https://....'

AWS and Product Advertising API credentials
'''''''''''''''''''''''''''''''''''''''''''

::

    # your Amazon Web Services access key id
    PRICE_MONITOR_AWS_ACCESS_KEY_ID = '...'

    # your Amazon Web Services secret access key
    PRICE_MONITOR_AWS_SECRET_ACCESS_KEY = '...'

    # the region endpoint you want to use.
    # Typically the country you'll run the price monitor in.
    # possible values: CA, CN, DE, ES, FR, IT, JP, UK, US
    PRICE_MONITOR_AMAZON_PRODUCT_API_REGION = '...'

    # the assoc tag of the Amazon Product Advertising API
    PRICE_MONITOR_AMAZON_PRODUCT_API_ASSOC_TAG = '...'

Amazon associates
'''''''''''''''''
As the links to Amazon will be affiliate links with your Amazon associate tag (see above), you have to set your name for the disclaimer
(see `https://partnernet.amazon.de/gp/associates/agreement <https://partnernet.amazon.de/gp/associates/agreement>`__).

::

    # name of you/your site
    PRICE_MONITOR_AMAZON_ASSOCIATE_NAME = 'name/sitename'
    # Amazon site being used, choose from on of the following
        'Amazon.co.uk'
        'Local.Amazon.co.uk'
        'Amazon.de'
        'de.BuyVIP.com'
        'Amazon.fr'
        'Amazon.it'
        'it.BuyVIP.com'
        'Amazon.es'
        'es.BuyVIP.com'
    PRICE_MONITOR_AMAZON_ASSOCIATE_SITE = '<ONE FROM ABOVE>'


Images protocol and domain
''''''''''''''''''''''''''

::

    # if to use the HTTPS URLs for Amazon images.
    # if you're running the monitor on SSL, set this to True
    # INFO:
    #  Product images are served directly from Amazon.
    #  This is a restriction when using the Amazon Product Advertising API
    PRICE_MONITOR_IMAGES_USE_SSL = True

    # domain to use for image serving.
    # typically analog to the api region following the URL pattern
    #  https://images-<REGION>.ssl-images-amazon.com
    PRICE_MONITOR_AMAZON_SSL_IMAGE_DOMAIN = 'https://images-eu.ssl-images-amazon.com'

Optional settings
^^^^^^^^^^^^^^^^^

The following settings can be adjusted but come with reasonable default
values.

Product synchronization
'''''''''''''''''''''''

::

    # time after which products shall be refreshed
    # Amazon only allows caching up to 24 hours, so the maximum value is 1440!
    PRICE_MONITOR_AMAZON_PRODUCT_REFRESH_THRESHOLD_MINUTES = 720  # 12 hours

Notifications
'''''''''''''

To be able to send out the notification emails, set up a proper email
backend (see `Django
documentation <https://docs.djangoproject.com/en/1.5/topics/email/#topic-email-backends>`__).

::

    # time after which to notify the user again about a price limit hit (in minutes)
    PRICE_MONITOR_SUBSCRIPTION_RENOTIFICATION_MINUTES = 10080  # 7 days

    # sender address of the notification email
    PRICE_MONITOR_EMAIL_SENDER = 'noreply@localhost'

    # currency name to use on notifications
    PRICE_MONITOR_DEFAULT_CURRENCY = 'EUR'

    # subject and body of the notification emails
    gettext = lambda x: x
    PRICE_MONITOR_I18N_EMAIL_NOTIFICATION_SUBJECT = gettext(
        'Price limit for %(product)s reached'
    )
    PRICE_MONITOR_I18N_EMAIL_NOTIFICATION_BODY = gettext(
        'The price limit of %(price_limit)0.2f %(currency)s has been reached for the '
        'article "%(product_title)s" - the current price is %(price)0.2f %(currency)s.'
        '\n\nPlease support our platform by using this '
        'link for buying: %(link)s\n\n\nRegards,\nThe Team'
    )

    # name of the site in notifications
    PRICE_MONITOR_SITENAME = 'Price Monitor'

Caching
'''''''

::

    # key of cache (according to project config) to use for graphs
    # None disables caching.
    PRICE_MONITOR_GRAPH_CACHE_NAME = None

    # prefix for cache key used for graphs
    PRICE_MONITOR_GRAPH_CACHE_KEY_PREFIX = 'graph_'

Celery settings
~~~~~~~~~~~~~~~
To be able to run the required Celery tasks, Celery itself has to be set up. Please see the `Celery Documentation <http://docs.celeryproject.org/en/latest/index.html>`__ about how to setup the whole thing. You'll need a broker and a result backend configured.

Development setup with Docker
-----------------------------
The package comes with an easy to use Docker setup - you just need ``docker`` and ``docker-compose``.

Structure
~~~~~~~~~
There are 5 containers:

====== =======================================================================
db     Postgres database
------ -----------------------------------------------------------------------
redis  Celery broker
------ -----------------------------------------------------------------------
web    a django project containing the ``django-amazon-price-monitor`` package
------ -----------------------------------------------------------------------
celery the celery for the django project
------ -----------------------------------------------------------------------
data   container for mounted volumes
====== =======================================================================

The ``web`` and ``celery`` containers are using a docker image being set up under ``docker/web``.

Image: base
^^^^^^^^^^^
Basic image with all necessary system packages and pre-installed ``lxml`` and ``psycopg2``.
The image can be found on `Docker Hub <https://hub.docker.com/r/pricemonitor/base/>`__.

Image: web
^^^^^^^^^^
It comes with a Django project with login/logout view, that can be found under ``docker/web/project``.
The image derives from ``pricemonitor/base`` from above.

The directory structure within the container is the following (base dir: ``/srv/``):
::

	root:/srv tree
	????????? logs		[log files]
	????????? media		[media files]
	????????? project		[the django project]
	????????? static		[static files]
	????????? pricemonitor	[the pricemonitor package]

Starts via the start script ``docker/web/web_run.sh`` that does migrations and the starts the ``runserver``.

Image: celery
^^^^^^^^^^^^^
Basically the same as ``web``, but starts the Celery worker with beat.

If you want to develop anything involving tasks, see the `Usage <_docker-usage-override-settings>`__ section below.

Volumes
^^^^^^^
The containers mount several paths:

+--------------------------+----------------------------------+----------------------------------------------------+
| Folder in container      | Folder on host                   | Information                                        |
+==========================+==================================+====================================================+
| /var/lib/postgresql/data | <PROJECTROOT>/docker/postgres    | * Postgres data directory                          |
|                          |                                  | * Keeps the DB data even if container is removed   |
+--------------------------+----------------------------------+----------------------------------------------------+
| /srv/logs                | <PROJECTROOT>/docker/logs        | Django logs (see project settings)                 |
+--------------------------+----------------------------------+----------------------------------------------------+
| /srv/media               | <PROJECTROOT>/docker/media       | Django media files                                 |
+--------------------------+----------------------------------+----------------------------------------------------+
| /srv/project             | <PROJECTROOT>/docker/web/project | * the Django project                               |
|                          |                                  | * is copied on Dockerfile to get it up and running |
|                          |                                  | * then mounted over (the copy is overwritten)      |
+--------------------------+----------------------------------+----------------------------------------------------+
| /srv/pricemonitor        | <PROJECTROOT>                    | * the ``django-amazon-price-monitor`` lib          |
|                          |                                  | * is copied on Dockerfile to get it up and running |
|                          |                                  | * then mounted over (the copy is overwritten)      |
+--------------------------+----------------------------------+----------------------------------------------------+

Usage
~~~~~

.. _docker-usage-override-settings:

Override settings
^^^^^^^^^^^^^^^^^
To override some settings as well as to set up the **required AWS settings** you can create a ``docker-compose.override.yml`` and fill with the specific values
(also see `docker-compose documentation <https://docs.docker.com/compose/extends/>`__).

Please see or adjust the ``docker\web\project\glue\settings.py`` for all settings that are read from the environment.
They can be overwritten.

A sample ``docker-compose.override.yml`` file could look like this:
::

	version: '3'
	services:
	  celery:
	    command: /bin/true
	    environment:
	      PRICE_MONITOR_AWS_ACCESS_KEY_ID: XXX
	      PRICE_MONITOR_AWS_SECRET_ACCESS_KEY: XXX
	      PRICE_MONITOR_AMAZON_PRODUCT_API_REGION: DE
	      PRICE_MONITOR_AMAZON_PRODUCT_API_ASSOC_TAG: XXX
	      PRICE_MONITOR_AMAZON_PRODUCT_REFRESH_THRESHOLD_MINUTES: 5
	      PRICE_MONITOR_SUBSCRIPTION_RENOTIFICATION_MINUTES: 60

It will avoid the automatic startup of celery (``command: /bin/true``) and set the required settings for AWS (in fact they are only needed in the celery
container). You can then manually start the container and execute celery which is quite useful if you develop anything that includes changes in the tasks and
thus requires the celery to be restarted (execute from the ``docker`` folder!):
::

	alex@tyrion:~/projects/github/django-amazon-price-monitor/docker$ docker-compose run celery bash
	Starting docker_data_1


	# check environment variables

	root@9d64bbd23e98:/srv/project# env
	HOSTNAME=9d64bbd23e98
	EMAIL_BACKEND=django.core.mail.backends.filebased.EmailBackend
	POSTGRES_DB=pm_db
	TERM=xterm
	PYTHONUNBUFFERED=1
	PRICE_MONITOR_SUBSCRIPTION_RENOTIFICATION_MINUTES=60
	POSTGRES_PASSWORD=6i2vmzq5C6BuSf5k33A6tmMSHwKKv0Pu
	PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
	SECRET_KEY=Vceev7yWMtEQzHaTZX52
	PWD=/srv/project
	CELERY_BROKER_URL=redis://redis/1
	C_FORCE_ROOT='True'
	PRICE_MONITOR_AWS_SECRET_ACCESS_KEY=XXX
	POSTGRES_USER=pm_user
	SHLVL=1
	HOME=/root
	PRICE_MONITOR_AMAZON_PRODUCT_REFRESH_THRESHOLD_MINUTES=5
	PRICE_MONITOR_AMAZON_PRODUCT_API_REGION=DE
	PRICE_MONITOR_AMAZON_PRODUCT_API_ASSOC_TAG=XXX
	DEBUG='True'
	PRICE_MONITOR_AWS_ACCESS_KEY_ID=XXX
	_=/usr/bin/env


	# start celery (worker and beat) (can also execute /srv/celery_run.sh)

	root@9d64bbd23e98:/srv/project# celery --beat -A glue worker

	 -------------- celery@9d64bbd23e98 v3.1.23 (Cipater)
	---- **** -----
	--- * ***  * -- Linux-3.16.0-4-amd64-x86_64-with-debian-8.0
	-- * - **** ---
	- ** ---------- [config]
	- ** ---------- .> app:         glue:0x7fc6b5269e10
	- ** ---------- .> transport:   redis://redis:6379/1
	- ** ---------- .> results:     disabled://
	- *** --- * --- .> concurrency: 8 (prefork)
	-- ******* ----
	--- ***** ----- [queues]
	 -------------- .> celery           exchange=celery(direct) key=celery

	[2016-03-20 10:02:26,776: WARNING/MainProcess] celery@9d64bbd23e98 ready.


Start/Stop/Build
^^^^^^^^^^^^^^^^
::

	cd docker

	# start
	docker-compose up -d

	# stop
	docker-compose stop

	# inspect
	docker-compose logs -f

A fixture with a Django user ``admin`` and the password ``password`` is loaded automatically.

To build the images, use the `Makefile` from the root directory.

Templates
---------
As the fronted is done by Angular, there is only a single template with very limited possibilities to adjust, ``price_monitor/angular_index_view.html``. You
can extends the template and adjust the following blocks.

footer
~~~~~~
Is rendered on the very bottom of the page. You have to use Bootstrap compatible markup, e.g.:
::

	{% block footer %}
		<div class="row">
			<div class="col-md-12">Additonal footer</div>
		</div>
	{% endblock %}

Management Commands
-------------------

price\_monitor\_batch\_create\_products
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A management command to batch create a number of products by providing
their ASIN:

::

    python manage.py price_monitor_batch_create_products <ASIN1> <ASIN2> <ASIN3>

price\_monitor\_recreate\_product
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Recreates a product with the given asin. If product already exists, it
is deleted. *Only use in development!*

::

    python manage.py price_monitor_recreate_product <ASIN>

price\_monitor\_search
~~~~~~~~~~~~~~~~~~~~~~

Searches for products at Amazon (not within the database) with the given
ASINs and prints out their details.

::

    python manage.py price_monitor_search <ASIN1> <ASIN2> ...

Loggers
-------

price\_monitor
~~~~~~~~~~~~~~

The app uses the logger "price\_monitor" to log all error and info
messages that are not included within a dedicated other logger. Please
see the `Django logging
documentation <https://docs.djangoproject.com/en/1.6/topics/logging/>`__
for how to setup loggers.

price\_monitor.product\_advertising\_api
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Logger for everything related to the ProductAdvertisingAPI wrapper class
that accesses the Amazon Product Advertising API through bottlenose.

price\_monitor.utils
~~~~~~~~~~~~~~~~~~~~

Logger for the utils module.

Tests
-----

Coverage
~~~~~~~~

|codecov-graph|

Internals
---------

Model graph
~~~~~~~~~~~

.. figure:: https://github.com/ponyriders/django-amazon-price-monitor/raw/master/models.png
   :alt: Model Graph

Product advertising api synchronization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Task workflow
^^^^^^^^^^^^^

.. figure:: https://raw.githubusercontent.com/ponyriders/django-amazon-price-monitor/master/docs/price_monitor.product_advertising_api.tasks.png
    :alt: Image of Product advertising api synchronization workflow

Image of Product advertising api synchronization workflow

.. |Build Status| image:: https://travis-ci.org/ponyriders/django-amazon-price-monitor.svg?branch=master
    :target: https://travis-ci.org/ponyriders/django-amazon-price-monitor
.. |codecov.io| image:: http://codecov.io/github/ponyriders/django-amazon-price-monitor/coverage.svg?branch=master
    :target: http://codecov.io/github/ponyriders/django-amazon-price-monitor?branch=master
.. |codecov-graph| image:: http://codecov.io/github/ponyriders/django-amazon-price-monitor/branch.svg?branch=master
.. |Requirements Status| image:: https://requires.io/github/ponyriders/django-amazon-price-monitor/requirements.svg?branch=master
    :target: https://requires.io/github/ponyriders/django-amazon-price-monitor/requirements/?branch=master
.. |Stories in Ready| image:: https://badge.waffle.io/ponyriders/django-amazon-price-monitor.png?label=ready&title=Ready
    :target: https://waffle.io/ponyriders/django-amazon-price-monitor
.. |Landscape| image:: https://landscape.io/github/ponyriders/django-amazon-price-monitor/master/landscape.svg?style=flat
    :target: https://landscape.io/github/ponyriders/django-amazon-price-monitor/master
    :alt: Code Health
