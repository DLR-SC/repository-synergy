===============
django-viewsets
===============

.. contents::

Problematic
===========

When having a look at *Ruby on Rails*, I discovered a nice feature that was
missing in Django:
`controllers <http://guides.rubyonrails.org/action_controller_overview.html>`_.
Contrary to what I often read, views in Django are not really equivalent to
controllers in Rails.  A Rails controller basically is **a set of Django
views and Django URL patterns**.  Apart from driving off boring URL work, this
is a clean way to group views that belongs to the same model.

Any good djangonaut would make the connection with generic views − especially
`class-based <https://docs.djangoproject.com/en/1.5/topics/class-based-views/>`_.
This is the easiest solution to avoid repeating the same code with a few
changes.  But this is not simplifying URL patterns and we often have to define
such files:

::

    # views.py
    from django.views.generic import ListView, DetailView  # and so on…
    from .models import Example


    class ExampleListView(ListView):
        model = Example


    class ExampleDetailView(DetailView):
        model = Example

    # and so on…

::

    # urls.py
    from django.conf.urls import patterns, url
    from .views import *


    urlpatterns = patterns('',
        url('^examples/$', ExampleListView.as_view(), name='example_index'),
        url('^examples/(?P<pk>\d+)$', ExampleDetailView.as_view(),
            name='example_detail'),
        # and so on…
    )

With a single model, this looks easy.  With complex applications containing
dozens of models, **this looks painful** − and definitely not DRY [1]_.


Solution
========

*django-viewsets* proposes a solution inspired of Rails controllers.
``ViewSet`` is a class that builds a set of URL patterns from a set of
class-based generic views.  It is designed to be overridable, so that it fits
standard as well as advanced use.


Installation
============

``[sudo] pip install django-viewsets``

You don't have to change your project `settings.py`.


Usage
=====

``ModelViewSet``
----------------

Provided views and urls
.......................

============== ========================= ===================
 Generic view             URL                 URL name
-------------- ------------------------- -------------------
``ListView``   *your-models/*            *your-model_index*
``DetailView`` *your-models/[pk]*        *your-model_detail*
``CreateView`` *your-models/create/*     *your-model_create*
``UpdateView`` *your-models/[pk]/update* *your-model_update*
``DeleteView`` *your-models/[pk]/delete* *your-model_delete*
============== ========================= ===================

Basic use
.........

In your application (or project) `urls.py`::

    from django.conf.urls import patterns, url, include
    from viewsets import ModelViewSet
    from .models import YourModel

    urlpatterns = patterns('',
        url('', include(ModelViewSet(YourModel).urls)),
    )


You can also provide other `basic attributes`_ as keyword arguments.  For
example, if you want to use slugs instead of primary keys in URL patterns,
lines 2 and 6 become::

  from viewsets import ModelViewSet, SLUG  # line 2
  url('', include(ModelViewSet(YourModel, id_pattern=SLUG).urls)),  # line 6


Advanced use
............

This allow more customization.

In your application `views.py`::

    from viewsets import ModelViewSet
    from .models import YourModel

    class YourModelViewSet(ModelViewSet):
        model = YourModel


In your application (or project) `urls.py`::

    from django.conf.urls import patterns, url, include
    from .views import YourModelViewSet

    urlpatterns = patterns('',
        url('', include(YourModelViewSet().urls)),
    )


What is interesting in this use is that you can easily customize views and
urls.  Let's say you want to use primary keys in update and delete url
patterns, but you want to use slugs in detail view.  The fastest way to do it
is::

    from viewsets import ModelViewSet, SLUG

    class CustomModelViewSet(ModelViewSet):
        def __init__(self, *args, **kwargs):
            self.views['detail_view']['pattern'] = SLUG
            super(CustomModelViewSet, self).__init__(*args, **kwargs)


Here we don't set the ``model`` attribute, so that ``CustomModelViewSet`` can
be used for any of your models.  Of course, you can now use
``CustomModelViewSet`` with `basic use`_ as well as `Advanced use`_.  And we
could have set ``model``, if this viewset was meant to be used only with a
specific model.


Basic Attributes
................

``model``
  The model class from which ModelViewSet will create views and urls.  This is
  the only mandatory attribute.

``base_url_pattern``
  Overrides *your-models* in all URL patterns.  Calculated from
  ``model._meta.verbose_name_plural`` if unset.

``base_url_name``
  Overrides *your-model* in all URL names.  Calculated from
  ``model._meta.verbose_name`` if unset.

``id_pattern``
  Overrides *[pk]* in all URL patterns.  You can either use ``viewsets.PK`` or
  ``viewsets.SLUG``.

``excluded_views``
  A sequence of keys from the ``views``.  Unset by default.
  Example: ``('create_view', 'delete_view',)``.

``namespace``
  Set this if your application has a URL namespace.  It is used to redirect
  to ``main_view`` in delete_view.  You can also set ``main_url``.

``main_view``
  Used to calculate ``main_url``.  ``'list_view'`` by default.

``main_url``
  The main url where delete_view redirects.  If set, ``main_view`` is ignored.


Advanced attributes
...................

``views``
  Dictionary defining views and URLs.  CRUD [2]_ by default.


.. [1] Don't Repeat Yourself
.. [2] Create Read Update Delete
