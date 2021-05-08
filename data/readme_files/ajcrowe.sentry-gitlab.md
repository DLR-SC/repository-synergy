Sentry Gitlab
=============

A plugin for Sentry which allow you to create issues in your GitLab repositories from Sentry errors.

This module used the [sentry-github](https://github.com/getsentry/sentry-github) module as a basis for it structure.

Install
-------

Install the package via `pip`

```
pip install sentry-gitlab
```

Or you can clone to repository to your sentry install.

    git clone https://github.com/pancentric/sentry-gitlab.git

Then run the setup script to install the plugin and it's dependencies.

    python setup.py install

Restart Sentry and you should see a new plugin under `manage integrations` for your projects.

Configure
---------

Once enabled you can configure your settings for the project. You can also include default tags you wish to apply to issues created.

![settings](https://github.com/pancentric/sentry-gitlab/raw/master/docs/images/settings.png)

I would recommend you create a specific user for Sentry to use with only `Reporter` priviledges to your projects.

Bugs & Issues
-------------

If you find something that doesn't work please create an issue or even better fix it and submit a pull request!

Dependencies
------------

* [python-gitlab](https://github.com/gpocentek/python-gitlab)
* [requests](http://www.python-requests.org)
