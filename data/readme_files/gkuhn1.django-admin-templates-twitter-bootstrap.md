Django admin templates customized to use twitter bootstrap

Can be customized like defaults admin templates

AUTHOR
Guilherme Kuhn <g.kuhn0@gmail.com>

CONTRIBUTORS (Feel free to put your name here!)

REQUERIMENTS
Django V=1.3.1
Twitter Bootstrap v=2

INSTALLATION
1. run 'python setup.py install'
2. Add to INSTALLED_APPS in your settings.py before django.contrib.admin:
INSTALLED_APPS = (
    ...
    'admin_bootstrap',
    'django.contrib.admin',
    ...
)


