Cookiecutter Django CRUD
=====================

A cookiecutter template to create a Django app within an existing Django project, with boilerplate including:
    * A barebones Django model.
    * Django CRUD views and templates using django-vanilla-views.
    * A Django ModelForm using bootstrap3.
    * Tests for all of the views using WebTest.
    * Model Mommy generated models for the tests.

Blog post walkthrough at http://wildfish.com/blog/2013/09/25/generating-django-crud-scaffolding-cookiecutter/

This template is now included in my Django project starter template at https://github.com/wildfish/wildfish-django-starter/. If you want to generate an entire Django project from scratch rather than just an app then take a look there.

Python 2 vs 3
==========

As of now I'm only testing with Python 3. The latest version to include the Python 2.7 compatibility decorators is in the `python2` branch. I don't expect I'll be continuing to maintain the python2 branch, but it should be straightforward and anyone else is welcome to.

It's time you were using Python 3 now!

Quickstart
==========

1. Install cookiecutter, and apps listed in requirements.txt for our generated app.  Install them all with:

.. code-block:: console

    pip install -r https://raw.github.com/wildfish/cookiecutter-django-crud/master/requirements.txt


2. Run cookiecutter using this template.  Note that **it will overwrite existing files without warning if you already have an app dir of the same name**, so make sure your code is checked in or backed up.

.. code-block:: console

    cookiecutter git@github.com:wildfish/cookiecutter-django-crud.git


3. You'll need to add bootstrap3 to your INSTALLED_APPS, along with your new app of course:

.. code-block:: python

    INSTALLED_APPS = (
        ..
        'bootstrap3',
        'yourproject.yourapp',
    )

4. And don't forget to hook up your urls.py:

.. code-block:: python

    url(r'^things/', include('yourproject.yourapp.urls', namespace='yourapp')),


5. Run your newly created tests:

.. code-block:: console

    python manage.py test yourproject.yourapp


Feel free to fork and make it your own, or send anything back up which you think may be generally useful.
