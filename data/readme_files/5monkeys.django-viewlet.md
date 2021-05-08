.. image:: https://www.5monkeys.se/img/django-viewlet.svg
    :width: 500px

Render template parts with extended cache control.

.. image:: https://travis-ci.org/5monkeys/django-viewlet.svg?branch=master
    :target: https://travis-ci.org/5monkeys/django-viewlet

.. image:: https://coveralls.io/repos/5monkeys/django-viewlet/badge.svg?branch=master
    :target: https://coveralls.io/r/5monkeys/django-viewlet?branch=master

.. image:: https://img.shields.io/pypi/v/django-viewlet.svg
    :target: https://pypi.python.org/pypi/django-viewlet/

.. image:: https://img.shields.io/pypi/pyversions/django-viewlet.svg
    :target: https://pypi.python.org/pypi/django-viewlet/


Installation
------------

Install django-viewlet in your python environment

.. code-block:: sh

    $ pip install django-viewlet

Supports ``Django`` versions 1.3 - 2.0 and ``Python`` versions 2.6 - 3.6.


Configuration
-------------

Add ``viewlet`` to your ``INSTALLED_APPS`` setting so Django can find the template tag

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'viewlet',
    )

Jinja2
______

If you're using ``Jinja2`` as your template engine for Django versions < 1.8,
put this in your Django settings:

.. code-block:: python

    VIEWLET_TEMPLATE_ENGINE = 'jinja2'


If you're using ``Coffin`` or ``Jingo``, add the ``ViewletExtension`` to their settings,
and optionally switch to their respective environment.

**Coffin:**

.. code-block:: python

    JINJA2_EXTENSIONS = (
        ...
        'viewlet.loaders.jinja2_loader.ViewletExtension',
    )

    VIEWLET_JINJA2_ENVIRONMENT = 'coffin.common.env'

**Jingo:**

.. code-block:: python

    JINJA_CONFIG = {
        'extensions': (
            ...
           'viewlet.loaders.jinja2_loader.ViewletExtension',
        ),
    }

    VIEWLET_JINJA2_ENVIRONMENT = 'jingo.get_env'

**Django 1.8+:**

Add ``ViewletExtension`` to the list of extensions of Jinja2 template engine

.. code-block:: python

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.jinja2.Jinja2',
            # ...
            'OPTIONS': {
                # ...
                'extensions': [
                    # ...
                    'viewlet.loaders.jinja2_loader.ViewletExtension',
                ],
            }
        }
    ],


Usage
-----

A viewlet is almost like a function based django view, taking a template context
as first argument instead of request.
Place your viewlets in ``viewlets.py`` or existing ``views.py`` in your django app directory.

.. code-block:: python

    from django.template.loader import render_to_string
    from viewlet import viewlet

    @viewlet
    def hello_user(context, name):
        return render_to_string('hello_user.html', {'name': name})


You can then render the viewlet with the ``viewlet`` template tag:

.. code-block:: html

    {% load viewlets %}
    <p>{% viewlet hello_user request.user.username %}</p>


... and in your Jinja2 templates:

.. code-block:: html

    <p>{% viewlet 'host_sponsors', host.id) %}</p>


Specifying cache backend
________________________

By default viewlet will try using ``viewlet`` cache alias, falling back to ``default``. You can specify
which alias should be used in settings:

.. code-block:: python

    VIEWLET_DEFAULT_CACHE_ALIAS = 'template_cache'

    CACHES = {
        # ...
        'template_cache': {
            # ...
        },
        # ...
    }

Additionally, you can override cache alias in viewlet decorator with ``using`` argument

.. code-block:: python

    @viewlet(using='super_cache')
    def hello_user(context, name):
        return render_to_string('hello_user.html', {'name': name})


Refreshing viewlets
___________________

A cached viewlet can be re-rendered and updated behind the scenes with ``viewlet.refresh``

.. code-block:: python

    import viewlet
    viewlet.refresh('hello_user', 'monkey')
    # or
    hello_user.refresh('monkey')


The decorator
_____________

.. code-block:: python

    @viewlet(name, template, key, timeout)


* name
    Optional reference name for the viewlet, defaults to function name.
* template
    Optional path to template. If specified the viewlet must return a context dict,
    otherwise it is responsible to return the rendered output itself.
* key
    Optional cache key, if not specified a dynamic key will be generated ``viewlet:name(args...)``
* timeout
    Cache timeout. Defaults to configured cache backend default timeout, None = eternal, 0 = uncached.


Examples
________

The content returned by the viewlet will by default be cached. Use the ``timeout`` argument to change this.

.. code-block:: python

    @viewlet(timeout=30*60)
    def hello_user(context, name):
        return render_to_string('hello_user.html', {'name': name})

..

    **Tip:** Set ``timeout`` to ``None`` to cache forever and use ``viewlet.refresh`` to update the cache.


Django viewlet will by default build a cache key ``viewlet:name(args...)``.
To customize this key pass a string to the viewlet decorator argument ``key`` that includes string mod operators for each
viewlet argument.

.. code-block:: python

    @viewlet(timeout=30*60, key='some_cache_key_%s')
    def hello_user(context, name):
        return render_to_string('hello_user.html', {'name': name})


Django viewlet will cache returned context instead of html by using the ``template`` decorator argument.
This is useful if cached html is too heavy, or your viewlet template needs to be rendered on every call.
The specified template will then be rendered with the viewlet context merged with the parent context, usually a ``RequestContext``.

.. code-block:: python

    @viewlet(template='hello_user.html', timeout=30*60)
    def hello_user(context, name):
        return {'name': name}

..

    **Note:** Return context dict for the template, not rendered html/text


If there is no need for caching, set the viewlet decorator argument ``timeout`` to 0.

.. code-block:: python

    @viewlet(timeout=0)
    def hello_user(context, name):
        return render_to_string('hello_user.html', {'name': name})


By default your viewlets will be named as the function. To override this you can set the decorator argument ``name``

.. code-block:: python

    @viewlet(name='greeting')
    def hello_user(context, name):
        return render_to_string('hello_user.html', {'name': name})


A powerful usage of ``viewlet.refresh`` is to use it together with Django signals:

.. code-block:: python

    class Product(Model):
        name = CharField(max_length=255)

    @viewlet(timeout=None)
    def product_teaser(context, id):
        product = get_context_object(Product, id, context)
        return render_to_string('product_teaser.html', locals())

    def refresh_product_teaser(instance, **kwargs):
        viewlet.refresh('product_teaser', instance.id)

    post_save.connect(refresh_product_teaser, Product)


Viewlets can also be accesses with AJAX by adding ``viewlet.urls`` to your Django root urls:

.. code-block:: python

    urlpatterns = patterns('',
        (r'^viewlet/', include('viewlet.urls')),
    )


The url ends with the viewlet name followed by a querystring used as ``kwargs`` to the viewlet:

..

    http://localhost:8000/viewlet/[name]/?arg=1...
