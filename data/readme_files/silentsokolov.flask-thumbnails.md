.. image:: https://travis-ci.org/silentsokolov/flask-thumbnails.svg?branch=master
   :target: https://travis-ci.org/silentsokolov/flask-thumbnails

.. image:: https://codecov.io/gh/silentsokolov/flask-thumbnails/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/silentsokolov/flask-thumbnails

flask-thumbnails
================

A simple extension to create a thumbs for the Flask


Installation
------------

Use your favorite Python package manager to install the app from PyPI, e.g.

Example:

``pip install flask-thumbnails``


Add ``Thumbnail`` to your extension file:

.. code:: python

    from flask import Flask
    from flask_thumbnails import Thumbnail

    app = Flask(__name__)

    thumb = Thumbnail(app)

Add ``THUMBNAIL_MEDIA_ROOT`` and ``THUMBNAIL_MEDIA_URL`` in your settings:

.. code:: python

    app.config['THUMBNAIL_MEDIA_ROOT'] = '/home/www/media'
    app.config['THUMBNAIL_MEDIA_URL'] = '/media/'


Example usage
-------------

Use in Jinja2 template:

 .. code:: html

    <img src="{{ 'image.jpg'|thumbnail('200x200') }}" alt="" />
    <img src="{{ 'image.jpg'|thumbnail('200x200', crop='fit', quality=100) }}" alt="" />


Options
~~~~~~~

``crop='fit'`` returns a sized and cropped version of the image, cropped to the requested aspect ratio and size, `read more <http://pillow.readthedocs.org/en/latest/reference/ImageOps.html#PIL.ImageOps.fit>`_.

``quality=XX`` changes the quality of the output JPEG thumbnail, default ``90``.


Develop and Production
----------------------

Production
~~~~~~~~~~

In production, you need to add media directory in you web server.


Develop
~~~~~~~

To service the uploaded files need a helper function, where ``/media/`` your settings ``app.config['THUMBNAIL_MEDIA_URL']``:

.. code:: python

    from flask import send_from_directory

    @app.route('/media/<regex("([\w\d_/-]+)?.(?:jpe?g|gif|png)"):filename>')
    def media_file(filename):
        return send_from_directory(app.config['THUMBNAIL_MEDIA_THUMBNAIL_ROOT'], filename)


Option settings
---------------

If you want to store the thumbnail in a folder other than the ``THUMBNAIL_MEDIA_THUMBNAIL_ROOT``, you need to set it manually:

.. code:: python

    app.config['THUMBNAIL_MEDIA_THUMBNAIL_ROOT'] = '/home/www/media/cache'
    app.config['THUMBNAIL_MEDIA_THUMBNAIL_URL'] = '/media/cache/'
    app.config['THUMBNAIL_STORAGE_BACKEND'] = 'flask_thumbnails.storage_backends.FilesystemStorageBackend'
    app.config['THUMBNAIL_DEFAUL_FORMAT'] = 'JPEG'


Migrate 0.X to 1.X
---------------

Since version 1.X all settings have a prefix ``THUMBNAIL_``. Example: ``MEDIA_ROOT`` -> ``THUMBNAIL_MEDIA_ROOT``.
