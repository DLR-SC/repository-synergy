Django-Spillway
===============

.. image:: https://travis-ci.org/bkg/django-spillway.svg?branch=master
    :target: https://travis-ci.org/bkg/django-spillway
.. image:: https://coveralls.io/repos/bkg/django-spillway/badge.svg?branch=master&service=github
    :target: https://coveralls.io/github/bkg/django-spillway?branch=master

`Django <http://www.djangoproject.com/>`_ and `Django REST Framework <http://www.django-rest-framework.org/>`_ integration of raster and feature based geodata.

Spillway builds on the immensely marvelous Django REST Framework by providing
facilities for the handling of geospatial formats such as GeoTIFF, GeoJSON, and
KML/KMZ.

Specific attention has been paid to speedy serialization of geometries from
spatial backends which avoids the cost of unnecessary re-serialization in
Python.


Basic Usage
-----------
Add vector response formats such as GeoJSON, KML/KMZ, and SVG to your API.

.. code-block:: python

    # models.py
    from django.contrib.gis.db import models
    from spillway.query import GeoQuerySet

    class Location(models.Model):
        slug = models.SlugField()
        geom = models.GeometryField()
        objects = GeoQuerySet.as_manager()

    # urls.py
    from django.conf.urls import url
    from spillway import generics
    from .models import Location

    urlpatterns = [
        url(r'^locations/(?P<slug>[\w-]+)/$',
            generics.GeoDetailView.as_view(queryset=Location.objects.all()),
            name='location'),
        url(r'^locations/$',
            generics.GeoListView.as_view(queryset=Location.objects.all()),
            name='location-list'),
    ]

Retrieve all locations as GeoJSON::

    curl -H 'Accept: application/vnd.geo+json' 127.0.0.1:8000/locations/

Simplify and reproject the geometries to another coordinate system::

    curl -H 'Accept: application/vnd.geo+json' '127.0.0.1:8000/locations/?srs=3857&simplify=100'

Any `spatial lookup
<https://docs.djangoproject.com/en/dev/ref/contrib/gis/geoquerysets/#spatial-lookups>`_
supported by the backend is available to search on. For instance, find the location which
intersects a particular point::

    curl -g '127.0.0.1:8000/locations/?intersects={"type":"Point","coordinates":[-120,38]}'

Raster data support is provided as well.

.. code-block:: python

    # models.py
    from spillway.models import AbstractRasterStore
    from spillway.query import GeoQuerySet

    class RasterStore(AbstractRasterStore):
        objects = GeoQuerySet.as_manager()

    # urls.py
    from django.conf.urls import url
    from spillway import generics
    from .models import RasterStore

    urlpatterns = [
        url(r'^rstores/(?P<slug>[\w-]+)/$',
            generics.RasterDetailView.as_view(queryset=RasterStore.objects.all()),
            name='rasterstore'),
        url(r'^rstores/$',
            generics.RasterListView.as_view(queryset=RasterStore.objects.all()),
            name='rasterstore-list'),
    ]

Return JSON containing a 2D array of pixel values for a given bounding box::

    curl 'http://127.0.0.1:8000/rstores/tasmax/?bbox=-107.74,37.39,-106.95,38.40'

One can crop raster images with a geometry and return a .zip archive of the
results::

    curl  -H 'Accept: application/zip' 'http://127.0.0.1:8000/rstores/?g=-107.74,37.39,-106.95,38.40'


Generic Views
-------------
Spillway extends REST framework generic views with GeoJSON and KML/KMZ
renderers for geographic data. This includes pagination of features and all
available spatial lookups/filters for the spatial backend in use.


ViewSets
--------
View sets exist for geo and raster enabled models following the familiar usage
pattern of Django REST Framework. Currently, a writable raster viewset needs to
be added and tested though the read-only variety is available.

.. code-block:: python

    from spillway import viewsets
    from .models import Location, RasterStore

    class LocationViewSet(viewsets.GeoModelViewSet):
        queryset = Location.objects.all()

    class RasterViewSet(viewsets.ReadOnlyRasterModelViewSet):
        queryset = RasterStore.objects.all()


Map Tiles
---------
`TileView` and `RasterTileView` are available respectively for generating
vector or image map tiles. Image tiles require the optional dependency Mapnik,
so be sure to have that installed. In this example, GeoJSON or PNG tiles can be
requested for the Location geo model, or PNG tiles for RasterStore data sets.
The urls presented here use a scheme of "/{z}/{x}/{y}.{format}".

.. code-block:: python

    from django.conf.urls import url
    from spillway import views, urls
    from .models import Location, RasterStore

    urlpatterns = [
        url(urls.tilepath('^locations/),
            views.TileView.as_view(queryset=Location.objects.all()),
            name='location-tiles'),
        url(urls.tilepath('^tiles/(?P<slug>\d+)/'),
            views.RasterTileView.as_view(queryset=RasterStore.objects.all()),
            name='map-tiles'),
    ]

Be sure to cache map tiles through configuration of your web server or Django's
cache framework when serving outside of development environments.


Renderers
---------
So far there are renderers for common raster and vector data formats, namely
zipped GeoTIFF, JPEG, PNG, and Erdas Imagine, plus GeoJSON, KML/KMZ, and SVG.


Tests
-----
Create a `virtualenv <https://virtualenv.pypa.io/en/latest/>`_ with
`virtualenvwrapper <https://virtualenvwrapper.readthedocs.org/en/latest/>`_,
install dependencies, and run the tests. On Python 2.7, running tests with
SpatiaLite requires a build of pysqlite with extension loading enabled. On 3.x,
all is well without it.

.. code-block:: shell

    mkvirtualenv spillway
    # Only the following when testing on 2.7, not needed with 3.x.
    pip install --global-option=build_ext --global-option='-USQLITE_OMIT_LOAD_EXTENSION' pysqlite
    pip install -r requirements.txt Pillow
    make check
