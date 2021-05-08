===========
django-seo2
===========

.. image:: https://travis-ci.org/romansalin/django-seo2.svg?branch=master
    :target: https://travis-ci.org/romansalin/django-seo2?branch=master

.. image:: https://coveralls.io/repos/romansalin/django-seo2/badge.svg?branch=master&service=github
    :target: https://coveralls.io/github/romansalin/django-seo2?branch=master

.. image:: https://landscape.io/github/romansalin/django-seo2/master/landscape.svg?style=flat
    :target: https://landscape.io/github/romansalin/django-seo2/master
    :alt: Code Health

.. image:: https://img.shields.io/pypi/v/django-seo2.svg
    :target: https://pypi.python.org/pypi/django-seo2

.. image:: https://readthedocs.org/projects/django-seo2/badge/?version=latest
    :target: http://django-seo2.readthedocs.org/en/latest/?badge=latest
    :alt: Documentation Status

Overview
--------

This is a set of powerful and flexible SEO tools for Django. It allows you
to associate metadata with:

* absolute paths
* model instances
* model classes
* views

Metadata can be edited in the Django Admin in a centralised place,
but also alongside any associated models.

This is however a framework, not an app. To use this library, you need to define
the metadata you want and add the output to your templates.
Everything else (retrieval, formatting, escaping, caching) is handled for you.
Therefore, you have complete control over the data you store.

As requirements change, it may become necessary to add new metadata fields.
Having the metadata definition confined to a single, short class means that it
is easy to update.

Requirements
------------

* Python (2.7, 3.3, 3.4, 3.5)
* Django (1.7, 1.8, 1.9)

Installation
------------

The easiest way to install django-seo2 is to use use ``pip``:

    pip install django-seo2

Example
-------

Here is an example of a definition:

.. code:: python

    from djangoseo import seo

    class BasicMetadata(seo.Metadata):
        title = seo.Tag(max_length=68, head=True)
        keywords = seo.KeywordTag()
        description = seo.MetaTag(max_length=155)
        heading = seo.Tag(name="h1")
        subheading = seo.Tag(name="h2")
        extra = seo.Raw(head=True)

        # Adding some fields for facebook (opengraph)
        og_title = seo.MetaTag(name="og:title",
                               populate_from="title",
                               verbose_name="facebook title")
        og_description = seo.MetaTag(name="og:description",
                                     populate_from="description",
                                     verbose_name='facebook description')

As you can see it is very flexible, but there is much more than this simple example.

The full documentation can be read online at http://django-seo2.readthedocs.org/.

History
-------

This is a fork of django-seo_, which is no longer maintained.

.. _django-seo: https://github.com/willhardy/django-seo
