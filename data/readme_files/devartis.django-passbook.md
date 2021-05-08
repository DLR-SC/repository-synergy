![Passbook](http://cl.ly/JPjc/title_passbook.png)

===============
django-passbook
===============

This application implements the specified API for passbook webservices. It handles pass registration, updates and logging. It may be easily plugged to you django application by just adding the installed app and importing the urls. It is based on Apple's specification and Mattt's rails example (https://github.com/mattt/passbook_rails_example)

> If you need to create passes (.pkpass files) in python you should check http.//github.com/devartis/passbook.

Requirements
============

- Django 1.4

Getting Started
===============

```
$ pip install django-passbook==0.1.0dev
```

Add 'django_passbook' to you installed apps in the settings.py file.

To use push notifications you need to specify the path to your certificate and key files in your settings.py file.

```
PASSBOOK_CERT = '/home/faramendi/my-site/cert.pem'
PASSBOOK_CERT_KEY = '/home/faramendi/my-site/key-nopass.pem'
```

You should also import the urls in your site urls.
```
from django_passbook import urls
urlpatterns = patterns('',
    url(r'^api/', include('django_passbook.urls')),
```

django-passbook signals certain events that might come handy in your application.
```
from django_passbook.views import pass_registered, pass_unregistered
@receiver(pass_registered)
def pass_registered(sender, **kwargs):
    pass

@receiver(pass_unregistered)
def pass_unregistered(sender, **kwargs):
    pass
```

Specification
=============

The complete specification can be found in the [Passbook Web Service Reference](https://developer.apple.com/library/prerelease/ios/#documentation/PassKit/Reference/PassKit_WebService/WebService.html).

Contact
=======

devartis

- http://devartis.com
- http://github.com/devartis
- http://twitter.com/devartis
- info@devartis.com
