The Travis CI cron trigger
==========================

This project permits to have [Travis CI](https://travis-ci.org/) builds triggered periodically, for example to test scrapers.

At Travis they will eventually implement cron (ref: [travis-ci/travis-ci#582](https://github.com/travis-ci/travis-ci/issues/582)), meanwhile, I hope this helps :)

## Technically

This project is made of two parts:

* A Django web app (running at http://traviscron.pythonanywhere.com) that lets users add new triggers to the queue.
* A Python module, `travis_ping`, that given a GH project name and a Travis OAuth token, triggers a rebuild.

The actual work is done by a continuously running process, crontab-like: `python manage.py runworker`.

Probably the first 3rd party app made using the [new Travis API](https://api.travis-ci.org/docs/)!