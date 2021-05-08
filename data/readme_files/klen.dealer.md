|logo| Dealer
#############

.. _description:

Dealer — SCM_ revision helper in your projects. Just add SCM_ revision to
your static paths and get automatic control at client browser caches:

Somewhere in templates: ::
    
    <script src='/main.js?{{ request.revision }}'

On clientside: ::

    <script src='/main.js?34jhfd45hd8'

Supported Git_, Mercurial_ and simple revision parse by file.

.. note:: You should install Mercurial_ for hg support.

.. note:: For Django<2 please use Dealer<2


.. _badges:

.. image:: http://img.shields.io/travis/klen/dealer.svg?style=flat-square
    :target: http://travis-ci.org/klen/dealer
    :alt: Build Status

.. image:: http://img.shields.io/coveralls/klen/dealer.svg?style=flat-square
    :target: https://coveralls.io/r/klen/dealer
    :alt: Coverals

.. image:: http://img.shields.io/pypi/v/dealer.svg?style=flat-square
    :target: https://pypi.python.org/pypi/dealer
    :alt: Version

.. image:: http://img.shields.io/pypi/dm/dealer.svg?style=flat-square
    :target: https://pypi.python.org/pypi/dealer
    :alt: Downloads

.. image:: http://img.shields.io/gratipay/klen.svg?style=flat-square
    :target: https://www.gratipay.com/klen/
    :alt: Donate


.. _contents:

.. contents::


.. _requirements:

Requirements
=============

- python 2.7, 3.5+

.. note:: For Django<2 please use Dealer<2


.. _installation:

Installation
=============

**Dealer** should be installed using pip: ::

    pip install dealer


.. _usage:

Usage
=====

Basic usage
-----------
::

    from dealer.git import git

    print git.revision

    print git.tag

::

    # Auto parse repository type
    from dealer.auto import auto
    print auto.revision

    print auto.tag


Manually create backend
----------------------

**path** — path to SCM_ repository (current dir by default)
::

    from dealer.mercurial import Backend

    hg = Backend('/path/to/hg/repo')


Django support
--------------

Settings
^^^^^^^^

**DEALER_TYPE** — Type of SCM_ repository ('auto', 'git', 'mercurial', 'simple', 'env', 'null'). By default 'auto';

**DEALER_PATH** — Path to SCM_. By default current dir;

**DEALER_SILENT** — Disable log warnings;

**DEALER_BACKENDS** — Backends for auto search by default ('git', 'mercurial', 'simple', 'env', 'null');


Context-processor
^^^^^^^^^^^^^^^^^

Append to your context processors: ::

    ...
    context_processors = ['dealer.contrib.django.context_processor']

And use the *REVISION* and *TAG* variables in your templates: ::

    <link href="/test.css?{{ REVISION }}" rel="stylesheet" type="text/css" media="screen" />
    <script src="/test.js?{{ REVISION }}"></script>

Middleware
^^^^^^^^^^
    
Append to your settings: ::

    MIDDLEWARE = ['dealer.contrib.django.Middleware']

And use in your views: ::

    def view(request):
        return request.revision

Or in your templates by `request.revision` var.


Flask support
-------------

Settings
^^^^^^^^

*DEALER_TYPE* — Type of SCM_ repository ('auto', 'git', 'mercurial', 'simple', 'env', 'null'). By default 'auto'
*DEALER_PARAMS* — Params for backend

Usage
^^^^^

In views::

        from flask import Flask, g
        from dealer.contrib.flask import Dealer

        app = Flask('test')
        Dealer(app)
        assert app.revision

        @app.route('/')
        def usage_in_view():
            return g.revision


In templates: ::

    <link href="/test.css?{{ REVISION }}" rel="stylesheet" type="text/css" media="screen" />

Pyramid support
---------------

::

    config.include('dealer.contrib.pyramid')

::

    def myview(request):
        revision = request.registry.dealer.revision
        tag = request.registry.dealer.tag

In templates

::

    Revision: {{DEALER_REVISION}}
    Tag: {{DEALER_TAG}}


Heroku support
-------------

Settings
^^^^^^^^

*DEALER_TYPE* = 'env'
*DEALER_PARAMS*:
    *revision_env_keyname* - Variable name for revision (default: DEALER_REVISION)
	*tag_env_keyname* - Variable name for tag (default: DEALER_TAG)

Usage
^^^^^

Setup your revision and tag value in envirement variables.
For example in Heroku.com:
::
    heroku config:set DEALER_REVISION='3ffb6b6'
    heroku config:set DEALER_TAG=v1_1

After that use dealer as described above.
 

.. _bagtracker:

Bug tracker
===========

If you have any suggestions, bug reports or
annoyances please report them to the issue tracker
at https://github.com/klen/Dealer/issues


.. _contributing:

Contributing
============

Development of dealer happens at github: https://github.com/klen/dealer


.. _contributors:

Contributors
=============

* klen_ (Kirill Klenov)


.. _license:

License
=======

Licensed under a `BSD license`_.


.. _links:

.. _BSD license: http://www.linfo.org/bsdlicense.html
.. _klen: http://klen.github.com/
.. _SCM: http://en.wikipedia.org/wiki/Source_Control_Management
.. _Git: http://en.wikipedia.org/wiki/Git_(oftware)
.. _Mercurial: http://en.wikipedia.org/wiki/Mercurial
.. |logo| image:: https://raw.github.com/klen/dealer/develop/docs/_static/logo.png
                  :width: 100
