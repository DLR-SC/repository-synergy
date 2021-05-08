django-social-friends-finder
============================

An extension app for `django-social-auth` or `django-allauth` that fetches your friends from different social-networks.
It displays matched friends so you can suggest your users to add them as friend or follow them. 

Dependencies
------------

To use it with `django-social-auth`

  * django-social-auth>=0.7.10 and all its dependencies https://github.com/omab/django-social-auth.git

To use it with `django-allauth`

  * django-allauth>=0.8.3 and all its dependencies https://github.com/pennersr/django-allauth

Back-end dependencies

  * python-twitter>=0.8.2 for twitter backend http://code.google.com/p/python-twitter/
  * facebook-sdk for facebook backend https://github.com/pythonforfacebook/facebook-sdk.git

Available BackEnds
------------------

  * Facebook
  * Twitter
  * Vkontakte
  * Google

Installation
------------

There are 3 ways to install this app

    pip install django-social-friends-finder

or build from the source.

    python setup.py install

or add `social_friends_finder` to your path

Usage and Configuration
-----------------------

Add `social_friends_finder` to your APPS list in your settings file

    INSTALLED_APPS = (
        ...
        "social_friends_finder",
    )

Add urls to your url config

    urlpatterns = patterns('',
        ...
        url(r'^find-friends/', include('social_friends_finder.urls')),
    )

Have a look at following settings:

    SOCIAL_FRIENDS_USING_ALLAUTH: True if you use `django-allauth`. Default is False
    SF_REDIRECT_IF_NO_SOCIAL_ACCOUNT_FOUND: True if no social account found. Default is True
    REDIRECT_URL: The url to redirect if above setting is used. Default is "/"

Go to `/find-friends/list/` on your browser.

Contributions
-------------

Currently there are facebook and twitter backends are available. Please help to implement new backends.

Implementing backend classes are easy. Just create a class inherits from `BaseFriendsProvider` and implement two of its methods. 
See backends module for example implementations

The software design for back-ends needs to be tweaked a little. Encapsulating the allauth and social-auth behaviors in different subclasses would help.
Also a common interface for backends to load them silently is crucial. Now if there is a missing backend, we raise an error. Factory class that loads them is also very ugly.

I needed to implement this app for a real-world project with an impossible deadline, and now no time to refactor it. So if you can spend some time on the above issues, that'd be awesome.

Contributors
------------

  * `lizrice`
  * `vden`
  * `mike-grayhat`

Change Log
----------

See `CHANGES.txt` file for history


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/laplacesdemon/django-social-friends-finder/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

