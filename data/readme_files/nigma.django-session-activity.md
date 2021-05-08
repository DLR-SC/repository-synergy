=======================
django-session-activity
=======================

.. image:: https://pypip.in/v/django-session-activity/badge.png
    :target: https://pypi.python.org/pypi/django-session-activity/
    :alt: Latest Version

.. image:: https://pypip.in/d/django-session-activity/badge.png
    :target: https://pypi.python.org/pypi/django-session-activity/
    :alt: Downloads

.. image:: https://pypip.in/license/django-session-activity/badge.png
    :target: https://pypi.python.org/pypi/django-session-activity/
    :alt: License

.. image:: http://b.repl.ca/v1/created_by-nigma-72a4b1.png
    :target: http://en.ig.ma/
    :alt: Built by

List all active sessions and sign-out from all sessions opened on other computers.

Developed at `en.ig.ma software shop <http://en.ig.ma>`_.

Overview
--------

This app records and shows last session activity and allows users to
sign-out from all active sessions, even remote ones.

In other words, it handles the following use case:

.. pull-quote::

    You come back home and realize that you forgot to
    log out on your work/university/other remote computer. What now?

    You take a look at the recent active sessions for your account
    and click a single button to deactivate all sessions
    opened on other computers.

.. image:: http://i.imgur.com/7LOMmJL.png


Quickstart
----------

1. Include ``django-session-activity`` in your ``requirements.txt`` file.

2. Add ``session_activity`` to ``INSTALLED_APPS`` and migrate/syncdb.

3. Add ``session_activity.middleware.SessionActivityMiddleware`` to ``MIDDLEWARE_CLASSES``
   after the ``django.contrib.sessions.middleware.SessionMiddleware`` and
   ``django.contrib.auth.middleware.AuthenticationMiddleware`` middleware classes.

4. Add url config for session list and sign-out views:

    .. code-block:: python

        url(r'^sessions/', include('session_activity.urls')),

   Then link to the main view using ``{% url "session_activity_list" %}`` template tag.

5. Optionally copy & modify the ``session_list.html`` template
   to match your look and feel expectations.

Dependencies
------------

``django-session-activity`` depends on ``django>=1.5.0``, ``django-appconf>=0.6``
and ``python-dateutil``.

Documentation
-------------

The full documentation is at http://django-session-activity.rtfd.org (TODO).

There's also an instant demo example that can be run from the cloned repository::

    python demo.py

License
-------

`django-session-activity` is released under the MIT license.

Other Resources
---------------

- GitHub repository - https://github.com/nigma/django-session-activity
- PyPi Package site - http://pypi.python.org/pypi/django-session-activity
