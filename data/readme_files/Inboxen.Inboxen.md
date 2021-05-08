Inboxen
=======

[![Build Status](https://travis-ci.org/Inboxen/Inboxen.svg?branch=master)](https://travis-ci.org/Inboxen/Inboxen)
[![Test coverage](http://codecov.io/github/Inboxen/Inboxen/coverage.svg?branch=master)](http://codecov.io/github/Inboxen/Inboxen?branch=master)

This is the complete system with everything you need to set up Inboxen.

Join us in our IRC channel! We're in the #inboxen channel on
[MegNet](https://www.megworld.co.uk/irc/)

GPG keys
--------

GPG keys used by Inboxen developers to sign releases:

```
Matt Molyneaux <moggers87@moggers87.co.uk>
    19F5 A8DC C917 FD00 E859   02F4 878B 5A2A 1D47 C084
```
Developing
----------

You'll need the following tools:

* Git
* Python (we strongly recommend you use virtualenv too)
* PostgreSQL
* NodeJS
* GNU Make
* [EditorConfig](http://editorconfig.org/) *(optional)*

This project comes with a `.editorconfig` file - we recommend installing it to
avoid things like mixing tabs/spaces or accidentally saving files with
DOS-style newlines.

Set yourself up with a virtual environment and run the following:

```
git clone https://github.com/Inboxen/Inboxen.git
cd Inboxen
make
```

When you've made your changes, remember to check your code
style and run unit tests.

Python tests:

```
python manage.py test
```

JS tests:

```
npx grunt karma
```

To check code style on Python:

```
tox -e isort,lint
```

And finally, check JS code style:

```
npx grunt jshint
```

### Local HTTP server

You'll need a `settings.ini` file, for example:

```
[general]
secret_key = some_random_string
debug=true
[tasks]
always_eager=true
```

If you want to start a local HTTP server to test out your changes, run the following:

```
python manage.py runserver
```

You can connect to it on <http://localhost:8000/>.

With `debug=true`, you'll have the Django Debug Toolbar enabled and you can
find the Inboxen styleguide at <http://localhost:8000/styleguide>

### Pinned Dependencies

Inboxen uses `pip-tools` to help manage its dependencies. The direct
requirements of Inboxen are kept in `requirements.in` and then we use the
following command to pin the entire dependency graph:

```
pip-compile --upgrade --output-file requirements.txt requirements.in
```

The resulting `requirements.txt` can be installed to a clean virtualenv with
`pip` to get the exact package versions that Inboxen uses in production. You
can also use the `pip-sync` (which comes with `pip-tools`) to update an
existing virtualenv as well as remove packages that are no longer required.

The same principal applies to `requirements-dev.txt`/`requirements-dev.txt` and
any files found in `extras/requirements`.

If for any reason you wish to bypass pinning dependencies, `requirements.in`
and `requirements-dev.in` are in the format expected by `pip`.

Committing and Branching
------------------------

### Branching

All development happens in branches off of `master`. Each branch should have an
associated issue - if there isn't one for what you're working on then create a
new issue first!

Branch names should be of the format `<issue>-<description>` where:

* `<issue>` is the issue you are working on
* `<description>` is a brief description of what's happening on that branch

For example, `129-pin-inboxes` was the branch used for implementing the [pin
inbox feature](https://github.com/Inboxen/Inboxen/issues/129)

Finished branches are then merged into `master`. If there is someone available
to review your branch, your branch should be reviewed and merged by them.
Remember to add a note to CHANGELOG.md when merging!

#### Hotfix branches

Hotfixes should be branched from the latest deploy tag, and then be tagged
themselves as a normal deployment before being merged back into `master`.

### Commit messages

You should follow the pattern of "summary, gap, details, gap, issue references"

For example:

```
Blah blah thing

Fixes this thing, changes how we should do something else

fix #345
touch #234
```

If you are committing on `master , then make sure to end your commit message
with "IN MASTER" so we know who to blame when stuff breaks.
