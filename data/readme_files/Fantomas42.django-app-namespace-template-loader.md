====================================
Django App Namespace Template Loader
====================================

|travis-develop| |coverage-develop|

Provides a template loader that allows you to load a template from a
specific application. This allows you to both **extend** and **override** a
template at the same time.

The default Django loaders require you to copy the entire template you want
to override, even if you only want to override one small block.

This is the issue that this package tries to resolve.

Examples:
---------

You want to change the titles of the admin site, you would originally
created this template: ::

    $ cat my-project/templates/admin/base_site.html
    {% extends "admin/base.html" %}
    {% load i18n %}

    {% block title %}{{ title }} | My Project{% endblock %}

    {% block branding %}
    <h1 id="site-name">My Project</h1>
    {% endblock %}

    {% block nav-global %}{% endblock %}

Extend and override version with a namespace: ::

    $ cat my-project/templates/admin/base_site.html
    {% extends "admin:admin/base_site.html" %}

    {% block title %}{{ title }} - My Project{% endblock %}

    {% block branding %}
    <h1 id="site-name">My Project</h1>
    {% endblock %}

Note that in this version the block ``nav-global`` does not have to be
present because of the inheritance.

Shorter version without namespace: ::

    $ cat my-project/templates/admin/base_site.html
    {% extends ":admin/base_site.html" %}

    {% block title %}{{ title }} - My Project{% endblock %}

    {% block branding %}
    <h1 id="site-name">My Project</h1>
    {% endblock %}

If we do not specify the application namespace, the first matching template
will be used. This is useful when several applications provide the same
templates but with different features.

Example of multiple empty namespaces: ::

    $ cat my-project/application/templates/application/template.html
    {% block content %}
    <p>Application</p>
    {% endblock content %}

    $ cat my-project/application_extension/templates/application/template.html
    {% extends ":application/template.html" %}
    {% block content %}
    {{ block.super }}
    <p>Application extension</p>
    {% endblock content %}

    $ cat my-project/templates/application/template.html
    {% extends ":application/template.html" %}
    {% block content %}
    {{ block.super }}
    <p>Application project</p>
    {% endblock content %}

Will render: ::

    <p>Application</p>
    <p>Application extension</p>
    <p>Application project</p>

Installation
------------

First of all install ``django-app-namespace-template-loader`` with your
favorite package manager. Example : ::

    $ pip install django-app-namespace-template-loader

Once installed, add ``app_namespace.Loader`` to the ``TEMPLATE_LOADERS``
setting of your project. ::

    TEMPLATE_LOADERS = [
      'app_namespace.Loader',
      ... # Other template loaders
    ]

With Django >= 1.8 ``app_namespace.Loader`` should be added to the
``'loaders'`` section in the OPTIONS dict of the ``DjangoTemplates`` backend
instead. ::

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'OPTIONS': {
                'loaders': [
                    'app_namespace.Loader',
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ],
            },
        },
    ]

Note: With Django 1.8, ``app_namespace.Loader`` should be first in the list
of loaders.

Known limitations
=================

``app_namespace.Loader`` can not work properly if you use it in conjunction
with ``django.template.loaders.cached.Loader`` and inheritance based on
empty namespaces.

Notes
-----

Based originally on: http://djangosnippets.org/snippets/1376/

Requires: Django >= 1.8

Tested with Python 2.7, 3.3, 3.4.

If you want to use this application for previous versions of Django, use the
version 0.3.1 of the package.

If you want to use this application with Python 2.6, use the version 0.2 of
the package.

.. |travis-develop| image:: https://travis-ci.org/Fantomas42/django-app-namespace-template-loader.png?branch=develop
   :alt: Build Status - develop branch
   :target: http://travis-ci.org/Fantomas42/django-app-namespace-template-loader
.. |coverage-develop| image:: https://coveralls.io/repos/Fantomas42/django-app-namespace-template-loader/badge.png?branch=develop
   :alt: Coverage of the code
   :target: https://coveralls.io/r/Fantomas42/django-app-namespace-template-loader
