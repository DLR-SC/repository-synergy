Django REST Framework - JSON API
================================

A parser and renderer for `Django REST
Framework <http://www.django-rest-framework.org/>`__ that adds support
for the `JSON API <http://jsonapi.org/>`__ specification.

Build status: |Build Status|

Does this work?
---------------

**This package is currently being actively developed**, but is not
widely used in production. If you find any problems when using this
package, please create a bug report at the `issue
tracker <https://github.com/kevin-brown/drf-json-api/issues>`__ so we can figure out how to fix it.

How do I use this?
------------------

This is designed to be used as only a renderer and parser and does not
provide any additional functionality that may be expected by JSON API.

Specific to a view(set)
~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    from rest_framework import generics
    from rest_framework_json_api.renderers import JsonApiRenderer


    class ExampleView(generics.ListAPIView):
        renderer_classes = (JsonApiRenderer, )

The JSON API renderer is not limited to just list views and can be used
on any of the generic views. It supports viewsets as well as non-generic
views.

All views
~~~~~~~~~

The JSON API renderer can be used on all views by setting it as a
default renderer.

.. code:: python

    # ...
    REST_FRAMEWORK = {
        "DEFAULT_RENDERER_CLASSES": (
            "rest_framework_json_api.renderers.JsonApiRenderer",
            "rest_framework.renderers.BrowsableAPIRenderer",
            # Any other renderers
        ),
        "DEFAULT_PARSER_CLASSES": (
            "rest_framework_json_api.parsers.JsonApiParser",
            "rest_framework.parsers.FormParser",
            "rest_framework.parsers.MultiPartParser",
            # Any other parsers
        ),
    }
    #...

This may break the API root view of the `Default Router
<http://www.django-rest-framework.org/api-guide/routers#defaultrouter>`__, so
you may want to instead apply it to your viewsets.

What does this support?
-----------------------

The JSON API renderer supports all features of hyperlinked serializers
and will normalize attributes such as the `url
field <http://www.django-rest-framework.org/api-guide/settings#url_field_name>`__
to match the JSON API specification.

Introspected resource types
~~~~~~~~~~~~~~~~~~~~~~~~~~~

JSON API uses `resource
types <http://jsonapi.org/format/#document-structure-resource-types>`__
to determine what relations exist and how to better side-load resources
automatically. It is recommended that resource types match the URL
structure of the API and use a plural form. The resource type is
determined from the model, and is the plural form of the `verbose model
name <https://docs.djangoproject.com/en/dev/ref/models/options/#verbose-name-plural>`__.

If a verbose name cannot be determined, the generic key\ ``data`` will
be used for the resource type.

Hyperlinked relations
~~~~~~~~~~~~~~~~~~~~~

JSON API will detect hyperlinked relations and set up the `url
templates <http://jsonapi.org/format/#document-structure-url-templates>`__
to match the destinations and attribute names automatically.

Nested serializers
~~~~~~~~~~~~~~~~~~

JSON API will render nested serializers to match the `compound document
specification <http://jsonapi.org/format/#document-structure-compound-documents>`__.
This will theoretically support any depth of nested serializers, but
only a single level is tested and supported.

Pagination
~~~~~~~~~~
JSON API does not explicitly call out pagination within the
specification, but instead leaves it flexible for the developer to
implement. The JSON API renderer supports the default pagination provided
by Django REST Framework by adding it to the top level "meta" element.  This
can be overriden by using a modified render, or a paginator that relies on a
header, such as `the Link header based
paginator <https://github.com/kevin-brown/drf-link-pagination>`__.


What this will not easily support
---------------------------------

Due to limitations within the JSON API specification, as well as a need
to handle the most common easy cases, this JSON API renderer will not
work with all views. When designing views that work well with the JSON
API specification, there are a few needs that you should keep in mind.

Anything not related to rendering or parsing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This package is only designed to be used as a renderer and parser and
does not provide support for parts of the JSON API specification that
are not unique to the JSON API specification. This includes features
such as custom filtering of results and pagination that does not use the
response body. Features such as side-loading of data using query
parameters are also not supported.

Isn't JSON API being actively developed?
----------------------------------------

Yes it is, and we will try to keep this package as close to the running
specification as possible. This means that things may break during
version changes, and until JSON API becomes stable we cannot guarantee
backwards compatibility. Once JSON API stabilizes, a deprecation process
will be established to match the policies of the JSON API specification.

Recommended packages
--------------------

This parser/renderer combination is only meant to be used as one of many
packages that can be grouped together to create an API that supports the
JSON API specification.

Pagination
~~~~~~~~~~

`The Link header based
paginator <https://github.com/kevin-brown/drf-link-pagination>`__ will
work with the renderer provided by this package.

JSON Patch
~~~~~~~~~~

JSON API recommends using JSON Patch for `PATCH` requests, and allowing partial
updates through the `PUT` HTTP method.  JSON Patch support is available for
Django REST Framework through a `third party package
<https://github.com/kevin-brown/drf-json-patch`__ and should be compatible.

.. |Build Status| image:: https://travis-ci.org/kevin-brown/drf-json-api.svg?branch=master
   :target: https://travis-ci.org/kevin-brown/drf-json-api
