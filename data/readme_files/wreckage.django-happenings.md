=================
Django Happenings
=================

|travis| |coverage| |version|

An event calendar app for Django.

Features:

* Repeating and non-repeating events
* Events that start and end on different days
* Support for cancelled events
* Upcoming events and current happenings lists
* AJAX support
* Default CSS & Javascript to help you get started

Coming soon:

* better integration of categories and tags
* more views, including an agenda view
* support for users
* ++ more


Note about upgrading from previous versions: Upgrading your version of the app
is a good idea, but be aware that some updates to the app involve changes
to models, which may cause problems with your database. For this reason
I've included south migrations to help make upgrading easier. But you
should always be cautious and make sure to backup your database before
upgrading. To see a list of changes made for each version view the CHANGELOG.

Dependencies
------------

Required:

* Django 1.6+
* Python 2.6+, 3+
* pytz

Optional:

* jQuery
* Twitter Bootstrap 3.0.0+ (w/ tooltip plugin)
* South (for database migrations)

jQuery is used for AJAX and the 'Today' button on the calendar.

TWBS is used to create popovers when an event is clicked on the calendar.

.. warning::

   django-happenings now use Django migrations by default. South users have to adjust their settings:

   .. code-block:: python

	SOUTH_MIGRATION_MODULES = {
	    'taggit': 'taggit.south_migrations',
	    'happenings': 'happenings.south_migrations',
	}

Quick Install
-------------

1. Install with ``pip``::

   $ pip install django-happenings

2. Add ``happenings`` to ``INSTALLED_APPS``:

   .. code-block:: python

	  INSTALLED_APPS = (
	    ...
	    'happenings',
	  )

3. Include the ``django-happenings`` URLconf in urls.py:
   
   .. code-block:: python

      url(r'^calendar/', include('happenings.urls', namespace='calendar'))
   
   If your are going to use different namespace then please set ``CALENDAR_URLS_NAMESPACE`` in settings

4. Make sure your ``TIME_ZONE`` is set correctly in settings.py.

5. Run ``python manage.py migrate`` to create the models (replace ``migrate`` with
   ``syncdb happenings`` if using older Django without South). If you're running MySQL, be sure that
   your database is properly configured to use time zones.

6. Run the development server and go to ``127.0.0.1:8000/admin/`` to create and manage events.

7. Check out the calendar at ``127.0.0.1:8000/calendar/``.

Customizing
-------------

The quickest way to begin customizing the app is to override the
``middle.html`` template by creating your own version in
<mytemplates>/happenings/middle.html (replace <mytemplates> with wherever
you keep your templates) and add the line ``{% extends 'base.html' %}``
(replace base.html with your base template). For a greater degree of customization,
you can copy and paste into your project all of the templates included in the app, and
change them to fit your needs.

Be sure to include the packaged css & javascript into your base template if you
want to use them. Loading the default style into your template would
look something like (assuming staticfiles has been loaded)::

    <link href=" {% static 'happenings/css/calendar.css' %}" rel="stylesheet">

And the default javascript something like::

    <script src="{% static 'happenings/js/calendar.js' %}"></script>

Template Tags
-------------

Template tags are available by loading ``happenings_tags`` into your template::

    {% load happenings_tags %}

This gives access to three template tags:
``show_calendar``, ``upcoming_events``, and ``current_happenings``.

Use ``show_calendar`` like this::

    <div id="event-calendar">
        {% show_calendar request %}
    </div>

to display a calendar like the one in ``/calendar/``, or like this::

    <div id="event-calendar" class="calendar-mini">
        {% show_calendar request mini=True %}
    </div>

to display a mini calendar. The ``<div>`` shown allows you to use the styles
included with the app, but you can omit or change them if you want to use
your own style. Note also that, because the request object needs to be
included in the tag, you must include "django.core.context_processors.request"
in TEMPLATE_CONTEXT_PROCESSORS in your settings.py.

If you are using custom templates for calendar and want to access all variables
from current template context then you can call ``show_calendar`` tag with
``inherit_context=True`` argument:

    <div id="event-calendar">
        {% show_calendar request inherit_context=True %}
    </div>

Include ``upcoming_events`` in your template like this::

    {% upcoming_events %}

to display a list of the next 5 (or less) upcoming events within the next 90 days.
If you'd like to show events that occur outside of 90 days, or show more events in the
list, use the ``finish`` and ``num`` options::

    {% upcoming_events finish=365 num=8 %}

Include ``current_happenings`` in your template like this::

    {% current_happenings %}

to display a list of events that are happening now.

Locale
-----------------

There are no translations from English yet, but if you'd like to display the calendar
and the event list in a different language, you can use ``CALENDAR_LOCALE``. The upcoming
events list won't be translated, though. For that you'll need to specify your ``LANGUAGE_CODE``
in the Django settings. Also note that to use ``CALENDAR_LOCALE`` you'll need to have the correct
locale pack installed for your system. Example of changing the language to German::

    CALENDAR_LOCALE = 'de_DE.utf8'

Example of changing to U.S. English::

    CALENDAR_LOCALE = 'en_US.utf8'

By default, the system's locale is used, so setting ``CALENDAR_LOCALE`` also ensures that you're
using the locale you want.

Optional Settings
-----------------

You can specify different settings for the app in your settings.py file.

Use ``CALENDAR_URLS_NAMESPACE`` if you included ``happenings.urls`` with namespace other than ``'calendar'``

Use ``CALENDAR_COLORS`` to add a custom color to the drop down in the admin when
creating an event. Example of setting the custom color 'fuchsia'::

    CALENDAR_COLORS = [('ff00ff', 'fuchsia')]

Use ``CALENDAR_START_DAY`` to change the day on which the calendar starts. Example
of starting the calendar on Sunday (instead of the default of Monday)::

    CALENDAR_START_DAY = 6

Default `time format <https://docs.djangoproject.com/en/1.7/ref/templates/builtins/#date>`_ is "TIME_FORMAT" (user locale dependend if  ``USE_L10N`` is used or default django format if not used). This can be changed with next setting::

	CALENDAR_TIME_FORMAT = 'H:i'
	## or
	# CALENDAR_HOUR_FORMAT = 'g:iA'  # 12 hour format with AM/PM

In titles of events minutes may be stripped from time when there are 0 minutes. This depends on i18 settings and your CALENDAR_TIME_FORMAT settings. You may set some specific value with next setting::

	CALENDAR_HOUR_FORMAT = 'H'
	## or
	# CALENDAR_HOUR_FORMAT = 'gA'  # 12 hour format with AM/PM

	## or if you do not want minutes to be stripped
	# CALENDAR_HOUR_FORMAT = 'H:i'


Upgrading from 0.2.X to 0.3.X
-----------------------------

Starting from 0.3.1 calendar rendering uses django templates to generate calendar
cells (``templates/happenings/partials/calendar/*.html```).
If you haven't customized anything and used default settings then everything will
still work out of the box.

If you have sublcassed ``EventCalendar`` or ``MiniEventCalendar`` calendar then you have 2 options:

* subclass ``LegacyEventCalendar`` or ``LegacyMiniEventCalendar``. You should also set ``CALENDAR_LEGACY_TIME_FORMAT`` in settings.
* copy ``templates/happenings/partials/calendar/*.html``` templates to your project ``templates``
  directory and customize them

If you are using custom ``CALENDAR_TIME_FORMAT`` setting then you also have 2 options:

* Just remove this setting and use default setting of django ``TIME_FORMAT``.
* change it from python strftime notation to `Django (PHP) notation <https://docs.djangoproject.com/en/1.7/ref/templates/builtins/#date>`_.  Specifying ``CALENDAR_HOUR_FORMAT`` is also a good idea:

  .. code-block:: python

	 # CALENDAR_TIME_FORMAT = '%H:%M'  # pre 0.3.1 version
	 CALENDAR_TIME_FORMAT = 'H:i'
	 CALENDAR_HOUR_FORMAT = 'H'

If you used ``event.l_start_date()``/``event.l_end_date()``/``event.start_end_diff()`` in your code:

* They are now cached_properties: use them without brackets or use ``get_FOO()`` (example: ``get_l_start_date()``)

Event details template (``tempaltes/happenings/event_detail.html``) now uses ``"SHORT_DATE_FORMAT"`` instead of ``"D F d, Y"`` format. To use old format either change SHORT_DATE_FORMAT in settings or copy templates and change them as you like.


Url to day details view (``EventDayView``) is now build using ``reverse``. This may have broken rendering for projects which included ``happenings.urls`` in their urlconf with namespace other than ``"calendar"``. In such case you have to set ``CALENDAR_URLS_NAMESPACE`` in settings to namespace that you use (empty string is allowed for those who do not use namespace).

Starting from 0.3.3 django happenings does not use ``locale.setlocale`` and fully utilizes
``i18n`` features if django. To set default calendar language you should set ``LANGUAGE_CODE``
in settings. If you have enabled language switching for your site then calendar 
will switch languages too. If you are not using legacy calendars then
``CALENDAR_LOCALE`` settings is not required anymore. 

Note that only month names and weekday names are translated for all languages supported by django.
Some django-happenings specific strings are only available in English (like "When/Description" in
event details). You can generate your own translations (pull requests are welcome) or you may copy
and change templates.


Tests
-------------

``Tox`` is used for testing.

``$ pip install tox``

``$ tox -e py27-django16``

More To Come!
-------------

.. |travis| image:: https://travis-ci.org/wreckage/django-happenings.svg?branch=master
   :alt: Build Status - master branch
   :target: https://travis-ci.org/wreckage/django-happenings
.. |coverage| image:: https://coveralls.io/repos/wreckage/django-happenings/badge.png?branch=master
   :alt: Coverage Status
   :target: https://coveralls.io/r/wreckage/django-happenings?branch=master
.. |version| image:: https://badge.fury.io/py/django-happenings.svg
   :alt: Pypi Version
   :target: https://badge.fury.io/py/django-happenings
