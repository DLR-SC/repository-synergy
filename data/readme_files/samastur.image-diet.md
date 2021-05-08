==========
image-diet
==========

image-diet is a Django application for removing unnecessary bytes from image
files.  It optimizes images without changing their look or visual quality
("losslessly").

It works on images in JPEG, GIF and PNG formats and will leave others
unchanged. Provides a seemless integration with easy-thumbnails app, but can
work with others too.

App was written and is being maintained by Marko Samastur (markos@gaivo.net)
and is licensed under MIT license.

**WARNING: Development of this app has stopped and moved to backwards 
incompatible** `image-diet2 <https://github.com/samastur/image-diet2>`_.


Installation
============
Add ``image_diet`` to ``INSTALLED_APPS`` setting::

    INSTALLED_APPS = (
        ...
        'image_diet',
    )

Check which tools are already installed by executing:

    ``python manage.py check_diet_tools``

Install those reported missing or disable them as described by command's
output (or ``Usage`` section). ``requirements.txt`` lists all tools together
with their home addresses and tips for installation.

If you are using recent version of easy-thumbnails, then you're done.
'image-diet' will automatically squeeze unnecessary bytes every time
a thumbnail is created.

If you aren't, then read further.


Usage
=====
``image-diet`` is used to remove unnecessary bytes from images. This means
every byte that will not change final display of the image including meta
information stored in EXIF etc. *DO NOT* use this app if this is not
acceptable or if your image storage is not a local file system.

Primary motivation for its development was seemless optimization of images
created by ``easy-thumbnails``. PIL is in many ways a great library, but its
output tends to be verbose.

If you are using a recent version of ``easy-thumbnails``, then you shouldn't
need to do anything more than described in ``Installation``. It is important
to disable tools that are not available since app for efficiency reasons
doesn't check during runtime.

You may use ``manage.py check_diet_tools`` action any time to check current
status of external utilities. Action also provides copy&paste ready list of
configuration options for disabling those that could not be found.

You may still be able to use ``image-diet`` even if you are not using
``easy-thumbnails``. Installation procedure is the same, but you will need
to trigger shrinking from your code (or let me know which public app you are
using so I can add support for it).

To do this import:

    ``from image_diet import squeeze``

And call ``squeeze(path_to_image)`` where ``path_to_image`` is an absolute
path to image you want to optimize. Function returns ``None`` if there was a
problem or path to squeezed image if it was successful.

Returned path is currently always the same as the one provided, but this may
change in the future (when GIF to PNG8 transformation gets added).

If you installed ``image-diet`` after you already processed some images, then
you can shrink them with ``manage.py diet_images`` command. Just pass paths
to directories you want to scan for images as command's argumentand it will
process all images that can be found in those directories or their
subdirectories.


Configuration options
---------------------
``DIET_DEBUG = True``
~~~~~~~~~~~~~~~~~~~~~
This will keep uncompressed versions of images on disk with
an extension ``.diet``. Defaults to ``False``.

``DIET_<TOOLNAME> = False``
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Disable use of ``TOOLNAME``. Name has to be written in uppercase so
``DIET_JPEGOPTIM = False`` will disable jpegoptim. Defaults to ``True``.


TODO/Wishlist
=============
- add extreme compressions (change to b&w, reduce color depth,
  change GIF to PNG8)
- add support for storage other than local file system
- stop depending on tools that processed image will actually be smaller
- add integrations for other image handling Django apps


Known bugs
==========
- app doesn't check if files exist so some operations could lead
  to data loss (if image folders contain files with .diet or .orig extension)
