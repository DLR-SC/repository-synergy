=====
django-private-media
=====

Overview
--------
By default, Django lets you specify a MEDIA_ROOT where your user (or admin)-uploaded media is placed.  It is accessible to all at the MEDIA_URL.

Using django-private-media, you can also specify a PRIVATE_MEDIA_ROOT and PRIVATE_MEDIA_URL.  Private files or images are uploaded using the provided PrivateMediaStorage() storage class.  They are served by a view which checks the user's authorization before serving them.

There are now three options for serving them, a default server useful for development, Apache's XSendFile, and nginx.  Setting up XSendFile at Webfaction (for example) is covered `here <http://community.webfaction.com/questions/12205/serving-static-files-with-django-using-xsendfile>`_.  By adapting code from Stephan Foulis's django-filer it would be easy to add an nginx server.

Motivation
----------
I have long wanted the capability for user uploads to be private, but couldn't find a guide to set it up.  When I looked into django-filer's approach to secure file downloads I finally understood how it could be done; however, I have an existing project and do not want to adopt the full functionality of django-filer.

I also wanted to be able to apply it to existing projects without any data migrations; with it, you only need to make sure your media files are relocated from the MEDIA_ROOT to the PRIVATE_MEDIA_ROOT.

Attribution
-----------
Key parts of this code are based on code by Stephan Foulis and contributors from 
`django-filer <https://github.com/stefanfoulis/django-filer>`_.

Caveats
-------
Although it works satisfactorily for my purposes so far, this is not a finished project. In particular, it does not have any tests. Yet.

Requirements
--------------
Django 1.5 or later.

Quick start
-----------
To upload to a private location, add to your `settings.py` e.g.::

    PRIVATE_MEDIA_URL = '/private/'
    if DEBUG:
        # dev
        import os
        PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
        PRIVATE_MEDIA_ROOT = os.path.join(PROJECT_PATH, 'private')
        PRIVATE_MEDIA_SERVER = 'private_media.servers.DefaultServer'
    else:
        # prod
        PRIVATE_MEDIA_ROOT = '/home/user/my/path/to/private/media'
        PRIVATE_MEDIA_SERVER = 'private_media.servers.ApacheXSendfileServer'
        #PRIVATE_MEDIA_SERVER_OPTIONS = {'arg1': 1, ...}  # (optional) kwargs to init server

The default permissioning is for authenticated staff members to see all, and no one else.
To generalise this, also add::

    PRIVATE_MEDIA_PERMISSIONS = 'myapp.permissions.MyPermissionClass'
    PRIVATE_MEDIA_PERMISSIONS_OPTIONS = {'arg1': 1, ...}  # (optional) kwargs to init

This permissions class must have the method::

    has_read_permission(self, request, path)

which returns True or False.


Add to your `INSTALLED_APPS`::

    INSTALLED_APPS = {
        ...
        'private_media',
        ...
    }


Add to `urls.py`::

       ...
       url(r'^', include('private_media.urls')),


In your `models.py`, to upload a specific file or image to a private area, use::

    from django.db import models
    from private_media.storages import PrivateMediaStorage

    class Car(models.Model):
        photo = models.ImageField(storage=PrivateMediaStorage())


Because the only information about the file available to the permissions method
is its path, you will need to encode the allowed permissioning into the path on upload.

E.g. you could use this to save the owner's primary key into the path::

    import os
    from django.db import models
    from django.contrib.auth.models import User
    from private_media.storages import PrivateMediaStorage

    def owner_file_name(instance, filename):
        return os.path.join('cars', "{0}".format(instance.user.pk), filename)

    class Car(models.Model):
        owner = models.ForeignKey(User)
        photo = models.ImageField(storage=PrivateMediaStorage(), upload_to=owner_file_name)

And then provide a permissioning class like this (which lets staff and the owner see it)::

    import os
    from django.http import Http404

    class OwnerPkPermissions(object):
        def has_read_permission(self, request, path):
            user = request.user
            if not user.is_authenticated():
                return False
            elif user.is_superuser:
                return True
            elif user.is_staff:
                return True
            else:
                try:
                    owner_pk = int(os.path.split(os.path.split(path)[0])[1])
                except ValueError:
                    raise Http404('File not found')
                return (user.pk==owner_pk)

Detailed documentation is provided at `<http://racingtadpole.com/blog/private-media-with-django>`_ and in the "docs" directory (pending).


