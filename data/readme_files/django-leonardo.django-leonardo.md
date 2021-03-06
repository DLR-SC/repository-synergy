
|PypiVersion| |Doc badge| |Travis| |Pypi|

===============
Django-Leonardo
===============

Full featured platform for fast and easy building extensible web applications.

*Don't waste your time searching stable solution for daily problems.*

**Deploy and Enjoy ! No skills required !**

For Users
=========

* CMS, Page, Responsive, Layouts, Themes, Color Variations 
* Widgets, Plugins, 3rd party app integrations
* Frontend Edit, Install/Uninstall modules in one click !
* Store, Form Designer, Blog, News, Folio, Links, Navigations, ..
* Media, Folders, Files, Images, Documents, Import - Export, ..
* LIVE settings, Auto loading modules, editable templates, ..
* Authentification, 3rd party backends, SAML standard, ..

For Developers
==============

* Python, Django, FeinCMS, OpenStack Horizon
* AngularJS, React, Bootstrap, Compress, Bootswatch
* Crispy forms, Floppy forms, Select2
* Filer, DbTemplates, Reversion, Constance
* Haystack, Oscar, Django Admin Bootstrap
* and tons of other apps bundled as modules

Further reading:

* `Leonardo Site`_
* `Demo Site`_ (a reference build of an Leonardo project)
* `Demo Store`_ (a reference build of an Leonardo Store project)
* `Developer Documentation`_ (documentation for Django Developers)
* `User Documentation`_ (documentation for Leonardo end-users)
* `Modules`_ Leonardo modules
* `Continuous integration homepage`_

.. image:: https://badges.gitter.im/Join%20Chat.svg
   :alt: Join the chat at https://gitter.im/django-leonardo/django-leonardo
   :target: https://gitter.im/django-leonardo/django-leonardo?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge

.. image:: https://coveralls.io/repos/django-leonardo/django-leonardo/badge.svg?branch=master
   :alt: Coverage
   :target: https://coveralls.io/r/django-leonardo/django-leonardo?branch=master

.. _`Leonardo Site`: http://www.leonardo-cms.org
.. _`Demo Site`: http://demo.leonardo-cms.org
.. _`Modules`: http://github.com/leonardo-modules
.. _`Demo Store`: http://store.leonardo-cms.org
.. _`Continuous integration homepage`: http://travis-ci.org/django-leonardo/django-leonardo
.. _`Developer Documentation`: http://django-leonardo.readthedocs.org
.. _`User Documentation`: http://leonardo-documentation.rtfd.org

Installation
============

one liner

Wget

.. code-block:: bash

    wget -O - https://github.com/django-leonardo/django-leonardo/raw/master/contrib/scripts/install_leonardo.sh | sh


Install Blog

.. code-block:: bash

    wget -O - https://github.com/django-leonardo/django-leonardo/raw/master/contrib/scripts/install_blog.sh | sh

Install Store

.. code-block:: bash

    wget -O - https://github.com/django-leonardo/django-leonardo/raw/master/contrib/scripts/install_store.sh | sh

Python

.. code-block:: bash

    python -c 'import urllib; print urllib.urlopen("https://github.com/django-leonardo/django-leonardo/raw/master/contrib/scripts/install_leonardo_dev.sh").read()' > install_leonardo.sh
    sudo sh install_leonardo.sh

Command by command

.. code-block:: bash

    virtualenv -p /usr/bin/python2.7 leonardo_venv
    cd leonardo_venv
    . $PWD/bin/activate

    pip install -e git+https://github.com/django-leonardo/django-leonardo#egg=django-leonardo
    pip install -r $PWD/src/django-leonardo/requirements.txt
    django-admin startproject --template=https://github.com/django-leonardo/site-template/archive/master.zip myproject

    export PYTHONPATH=$PWD/myproject
    cd myproject

    python manage.py makemigrations --noinput
    python manage.py migrate --noinput
    python manage.py bootstrap_site --url=http://github.com/django-leonardo/django-leonardo/raw/master/contrib/bootstrap/demo.yaml

    echo "from django.contrib.auth.models import User; User.objects.create_superuser('root', 'mail@leonardo.cz', 'admin')" | python manage.py shell

    python manage.py runserver 0.0.0.0:80


Navigate your browser to your_ip/admin and login with ``root:admin``
For settings production mode could take inspiration from `Leonardo Documentation`_.

.. _`Leonardo Documentation`: http://django-leonardo.readthedocs.org/en/master/install/production.html

Core
====

Leonardo in default state has enabled some modules which provides basic stuff for common sites:

* Web - precise FeinCMS integration
* Navigation - common navigation components
* Media - Filer integration with media widgets
* Search - Haystack integration
* Auth - Basic auth with standard user actions
* Devel - Widgets for site developers

Installed
=========

These modules are included in default leonardo installation, but could be uninstalled anytime without affecting your DB:

* System - Common management stuff (listing installed packages, widgets version etc..)
* Sitestarter - simple site starter which handle missing site and create it from custom yaml template
* Admin - django admin
* Ckeditor - Default wysiwyg editor for now. Alternatives: Redactor,Summernote,Tinymce..

For uninstalling::

    pip uninstall leonardo-system
    pip uninstall leonardo-sitestarter

For switch wysiwyg::

    pip uninstall leonardo-ckeditor
    pip install leonardo-redactor

Extensions
==========

Leonardo in default state using module loader which allows you to easy installation of new packages.

All modules lives in `Package Index`_.

.. _`Package Index`: http://packages.leonardo.robotice.org/

Modules
-------

* `Admin`_ - Standard Django admin
* `Admin Honeypot`_ - Django admin honeypot
* `Bootstrap Admin`_ - Bootstrap Django admin
* `Material Admin`_ - Material Django admin
* `Analytics`_ -  Analytics service integration for Leonardo projects
* `Blog`_ - Elephant Blog integration
* `Celery`_ - Celery workers for Leonardo CMS
* `Multisite`_ - Multi site with security
* `Folio`_ - Portfolio app
* `Geo`_ - Some geolocation related widgets (Google maps,..)
* `Galleries`_ - Awesome galleries
* `Forms`_ - Stable Form Designer integration with Remote Forms
* `Store`_ - Oscar Ecommerce - FeinCMS integration
* `News`_ - Heavy FeinCMS News
* `Newswall`_ - Newswall
* `Links`_ - navigation helpers bundles as Leonardo module
* `Redactor`_ - A lightweight wysiwyg editor for Leonardo
* `Sentry`_ - end-user friendly error page
* `Page Permissions`_ - extend Page and provide new Navigation templates with permissions
* `Team`_ - team model and widgets
* `Oembed`_ - oembed objects with caching
* Static - client-side libraries like an AngularJS, React, D3.js, ..


.. _`Admin`: https://github.com/leonardo-modules/leonardo-admin
.. _`Admin Honeypot`: https://github.com/leonardo-modules/leonardo-admin-honeypot
.. _`Bootstrap Admin`: https://github.com/leonardo-modules/leonardo-bootstrap-admin
.. _`Material Admin`: https://github.com/leonardo-modules/leonardo-material-admin
.. _`Forms`: https://github.com/leonardo-modules/leonardo-module-forms
.. _`Blog`: https://github.com/leonardo-modules/leonardo-module-blog
.. _`Celery`: https://github.com/leonardo-modules/leonardo-celery
.. _`Multisite`: https://github.com/leonardo-modules/leonardo-multisite
.. _`Folio`: https://github.com/leonardo-modules/leonardo-module-folio
.. _`Geo`: https://github.com/leonardo-modules/leonardo-geo
.. _`Galleries`: https://github.com/leonardo-modules/leonardo-gallery
.. _`Store`: https://github.com/leonardo-modules/leonardo-store
.. _`News`: https://github.com/leonardo-modules/leonardo-module-news
.. _`Links`: https://github.com/leonardo-modules/leonardo-module-links
.. _`Redactor`: https://github.com/leonardo-modules/leonardo-module-redactor
.. _`Sentry`: https://github.com/leonardo-modules/leonardo-module-sentry
.. _`Page Permissions`: https://github.com/leonardo-modules/leonardo-module-pagepermissions
.. _`Analytics`: https://github.com/leonardo-modules/leonardo-module-analytics
.. _`Team`: https://github.com/leonardo-modules/leonardo-team
.. _`Oembed`: https://github.com/leonardo-modules/leonardo-oembed

Themes
------

* `Bootwatch`_
* `AdminLTE`_

.. _`Bootwatch`: https://github.com/leonardo-modules/leonardo-theme-bootswatch
.. _`AdminLTE`: https://github.com/leonardo-modules/leonardo-theme-adminlte

Cookiecutters
-------------

Our cookiecutters are a good start for creating new `Site`_, `Module`_ or `Theme`_.

* `Site`_
* `Module`_
* `Theme`_

.. _`Site`: https://github.com/django-leonardo/cookiecutter-site
.. _`Module`: https://github.com/django-leonardo/cookiecutter-module
.. _`Theme`: https://github.com/django-leonardo/cookiecutter-theme

Bundles
-------

Leonardo defines a group of bundles that can be used
to install Leonardo and the dependencies for a given feature.

You can specify these in your requirements or on the ``pip`` comand-line
by using brackets.  Multiple bundles can be specified by separating them by
commas.

.. code-block:: bash

    $ pip install "django-leonardo[multisite]"

    $ pip install "django-leonardo[blog,store,multisite]"

`Here`_ is current list of bundles.

.. _`Here`: https://github.com/django-leonardo/django-leonardo/blob/master/setup.cfg#L28

Looking for commercial support?
===============================

If you are interested in having an Leonardo project built for you, or for development of an existing Leonardo site. Please get in touch via mail@majklk.cz.

Read More
=========

* http://docs.openstack.org/developer/horizon/quickstart.html
* http://feincms-django-cms.readthedocs.org/en/latest/index.html
* https://django-oscar.readthedocs.org/en/releases-1.0/

.. |Doc badge| image:: https://readthedocs.org/projects/django-leonardo/badge/?version=master
.. |Pypi| image:: https://img.shields.io/pypi/dm/django-leonardo.svg?style=flat
.. |PypiVersion| image:: https://badge.fury.io/py/django-leonardo.svg?style=flat
.. |Travis| image:: https://travis-ci.org/django-leonardo/django-leonardo.svg?branch=master
