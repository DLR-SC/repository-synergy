Django-Responsive
========================

.. image:: https://travis-ci.org/mlavin/django-responsive.svg?branch=master
    :target: https://travis-ci.org/mlavin/django-responsive


django-responsive a utility application for building responsive websites
in Django. This tool is meant to complement the use of CSS media queries and
help solve problems with fixed width elements such as advertisements or embedded video.

This project does *not* match devices based on user agent strings and instead
uses a small piece of javascript to make the device window size available on the server.
Once enabled you can access a ``device_info`` dictionary in your templates::

    {'width': 320, 'type': 'phone', 'height': 480}

Now you and conditionally render content based on the device size or type.


Installation
------------------------------------

django-responsive requires Python 2.6 or 2.7 and django>=1.3. There is experimental
support for Python 3.2 if using Django >= 1.5. It is easiest to install django-responsive from PyPi using pip::

    pip install django-responsive


Configuration
------------------------------------

To enable django-responsive you will need to update your ``MIDDLEWARE_CLASSES`` and
``TEMPLATE_CONTEXT_PROCESSORS`` settings.::

    MIDDLEWARE_CLASSES = (
        # Other middleware classes go here
        'responsive.middleware.DeviceInfoMiddleware',
    )

    TEMPLATE_CONTEXT_PROCESSORS = (
        # Other context processors included here
        'responsive.context_processors.device_info',
    )

Note that ``TEMPLATE_CONTEXT_PROCESSORS`` is not included in the default settings
and you should be careful to not lose the defaults when adding this additional
context processor.

There is an optional setting ``RESPONSIVE_BREAKPOINTS`` which is
used to determine the ``type`` included in the ``device_info`` dictionary. The
default breakpoints are::

    # Name, Max Width (inclusive)
    DEFAULT_BREAKPOINTS = {
        'phone': 480,
        'tablet': 767,
        'desktop': None,
    }

To overwrite the default breakpoints, include a ``RESPONSIVE_BREAKPOINTS`` 
dictionary in the project's settings.py file::

    # Name, Max Width (inclusive)
    RESPONSIVE_BREAKPOINTS = {
        'phone': 480,
        'tablet': 767,
        'desktop': None,
    }


License
--------------------------------------

django-responsive is released under the BSD License. See the 
`LICENSE <https://github.com/mlavin/django-responsive/blob/master/LICENSE>`_ file for more details.


Contributing
--------------------------------------

If you think you've found a bug or are interested in contributing to this project
check out `django-responsive on Github <https://github.com/mlavin/django-responsive>`_.


Running the Tests
------------------------------------

You can run the tests with via::

    python runtests.py

If you see any test failures please report them to the Github issue tracker.
