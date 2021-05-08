============================
Django Rest Framework Braces
============================

.. image:: https://badge.fury.io/py/django-rest-framework-braces.png
    :target: http://badge.fury.io/py/django-rest-framework-braces

.. image:: https://travis-ci.org/dealertrack/django-rest-framework-braces.svg?branch=master
    :target: https://travis-ci.org/dealertrack/django-rest-framework-braces

.. image:: https://coveralls.io/repos/dealertrack/django-rest-framework-braces/badge.svg
    :target: https://coveralls.io/r/dealertrack/django-rest-framework-braces

Collection of utilities for working with DRF. Name inspired by `django-braces <https://github.com/brack3t/django-braces>`_.

* Free software: MIT license
* GitHub: https://github.com/dealertrack/django-rest-framework-braces
* Documentation: https://django-rest-framework-braces.readthedocs.io.

Installing
----------

Easiest way to install ``django-rest-framework-braces`` is by using ``pip``::

    $ pip install django-rest-framework-braces

Usage
-----

Once installed, you can use any of the supplied utilities by simply importing them.
For example::

    from drf_braces.mixins import MultipleSerializersViewMixin

    class MyViewSet(MultipleSerializersViewMixin, GenericViewSet):
        def create(self, request):
            serializer = self.get_serializer(serializer_class=MySerializer)
            ...

For full list of available utilities, please refer to the `documentation <https://django-rest-framework-braces.readthedocs.io>`_.

Testing
-------

To run the tests you need to install testing requirements first::

    $ make install

Then to run tests, you can use use Makefile command::

    $ make test
