CUser, make email the USERNAME\_FIELD
=====================================

CUser makes it easy to use email address as your identification token
instead of a username.

CUser is a custom Django user model (extends ``AbstractBaseUser``) so it
takes a tiny amount of effort to use.

The only difference between CUser and the vanilla Django ``User`` is email
address is the ``USERNAME_FIELD`` (and username does not exist).

CUser supports Django 1.11, 2.0, 2.1, and 2.2. If you need to use CUser with
Django 1.8 - Django 1.10, you must install an older, unmaintained version of
CUser, as noted in the "Install & Set up" section.

Why use CUser?
--------------

Because you want everything in ``django.contrib.auth`` except for the
``username`` field and you also want users to **log in with email addresses**.
And you don't want to create your own custom user model or authentication
backend.

Install & Set up
----------------

**Important:** To keep things simple, the steps below will guide you through
the process of using CUser's ``CUser`` model for your Django project's user
model. However, it is strongly recommended that you set up a custom user model
that extends CUser's ``AbstractCUser`` class, even if CUser's ``CUser`` model
is sufficient for you (this way, you can customize the user model if the need
arises). If you would *not* like to follow this recommendation and just want to
use CUser's ``CUser`` model, simply follow the steps below (you can skip the
rest of this paragraph). If you *would* like to follow this recommendation, you
should still follow the steps below, but with the following adjustments: After
step 2, follow
`these instructions <https://docs.djangoproject.com/en/1.11/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project>`_,
but instead of using ``from django.contrib.auth.models import AbstractUser``
use ``from cuser.models import AbstractCUser`` and instead of using
``from django.contrib.auth.admin import UserAdmin`` use
``from cuser.admin import UserAdmin``. Then for step 3 of the steps below, you
should set ``AUTH_USER_MODEL`` to your custom user model instead of CUser's
``CUser`` model. You should then run ``python manage.py makemigrations``. After
that, you may follow the remaining steps below just the way they are.

0. If your Django project previously used Django's default user model,
   ``django.contrib.auth.models.User``, or if you are unfamiliar with using
   custom user models, jump to **Notes** first (then come
   back). Otherwise, continue onward!

1. Install with ``pip``:

   .. code-block:: shell

       # Django 2.0, 2.1, or 2.2
       pip install django-username-email

       # Django 1.11
       pip install "django-username-email<2.2"

       # Django 1.8 - Django 1.10 (unmaintained)
       pip install django-username-email==2.1.2

2. Add ``cuser`` to your ``INSTALLED_APPS`` setting:

   .. code-block:: python

       INSTALLED_APPS = [
           ...
           'cuser',
       ]

3. Specify the custom model as the default user model for your project
   using the ``AUTH_USER_MODEL`` setting in your settings.py:

   .. code-block:: python

       AUTH_USER_MODEL = 'cuser.CUser'

4. If you use Django's default ``AuthenticationForm`` class, it is
   strongly recommended that you replace it with the one included with
   CUser. This will make the ``<input>`` have its ``type`` attribute set
   to ``email`` and browsers' autocomplete feature will suggest email
   addresses instead of usernames. For example, if your project is using
   Django's default ``LoginView`` view (or ``login`` view in Django < 1.11), this is
   what you would put in your urls.py in order to make use of CUser's
   ``AuthenticationForm`` class:

   .. code-block:: python

       from cuser.forms import AuthenticationForm
       from django.conf.urls import include, url
       from django.contrib.auth.views import LoginView

       urlpatterns = [
           url(r'^accounts/login/$', LoginView.as_view(authentication_form=AuthenticationForm), name='login'),
           url(r'^accounts/', include('django.contrib.auth.urls')),
           ...
       ]

   Or if you're using Django < 1.11:

   .. code-block:: python

       from cuser.forms import AuthenticationForm
       from django.conf.urls import include, url
       from django.contrib.auth.views import login

       urlpatterns = [
           url(r'^accounts/login/$', login, {'authentication_form': AuthenticationForm}, name='login'),
           url(r'^accounts/', include('django.contrib.auth.urls')),
           ...
       ]

5. Run migrations.

   .. code-block:: shell

       python manage.py migrate

6. There is a good chance that you want foo@example.com and FOO@example.com to
   be treated as the same email address. There is a variety of ways to go about
   doing this. How you handle it will depend on the needs of your project and
   personal preference, so CUser does not provide a solution for this out of
   the box. You will need to address this yourself if this applies to you.

Configuration
-------------

To override any of the default settings, create a dictionary named ``CUSER`` in
your settings.py with each setting you want to override. For example:

.. code-block:: python

    CUSER = {
        'app_verbose_name': 'Authentication and Authorization',
        'register_proxy_auth_group_model': True,
    }

These are the settings:

``app_verbose_name`` (default: ``_("Custom User")``)
****************************************************

This controls the value that CUser will use for its ``AppConfig`` class'
``verbose_name``.

``register_proxy_auth_group_model`` (default: ``False``)
********************************************************

When set to ``True``, CUser's admin.py will unregister Django's default
``Group`` model and register its own proxy model of Django's default ``Group``
model (also named ``Group``). This is useful if you want Django's default
``Group`` model to appear in the same part of the admin as CUser's ``CUser``
model.

Notes
-----

If you have tables referencing Django's ``User`` model, you will have to
delete those table and migrations, then re-migrate. This will ensure
everything is set up correctly from the beginning.

Instead of referring to User directly, you should reference the user model
using ``django.contrib.auth.get_user_model()``

When you define a foreign key or many-to-many relations to the ``User``
model, you should specify the custom model using the ``AUTH_USER_MODEL``
setting.

For example:

.. code-block:: python

    from django.conf import settings
    from django.db import models

    class Profile(models.Model):
        user = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
    )

License
-------

Released under the MIT license. See LICENSE for details.

Questions, comments, or anything else?
--------------------------------------

-  Open an issue
-  `Twitter <https://twitter.com/tomfme>`__
-  tom@meagher.co
