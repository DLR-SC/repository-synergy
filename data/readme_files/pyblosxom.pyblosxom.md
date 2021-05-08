Master branch Build Status:

.. image:: https://travis-ci.org/pyblosxom/pyblosxom.svg?branch=master
   :target: https://travis-ci.org/pyblosxom/pyblosxom
   



Python3 version (In progress) : 

.. image:: https://travis-ci.org/pyblosxom/pyblosxom.svg?branch=python3
   :target: https://travis-ci.org/pyblosxom/pyblosxom
   
=================
 About Pyblosxom
=================

What is Pyblosxom
=================

Pyblosxom is a lightweight blog system.  It was originally a Python
clone of `Blosxom`_ but has since evolved into a blog system of its
own reminiscent of `Blosxom`_.

.. _Blosxom: http://www.blosxom.com/

Pyblosxom focuses on three things:

**simplicity**

  Pyblosxom stores all data on the file system in plain text files.
  This allows you to use any text editor to create, update and
  manipulate entries.  You can also use existing text-manipulation
  tools, version control, scripts, grep, ...  for managing your blog.

  Pyblosxom can run as a CGI script, WSGI component or you can use it
  to statically compile your website into HTML/XML files.

  Your workflow is your workflow.

**extensibility**

  Pyblosxom has a plugin framework enabling you to augment and enhance
  Pyblosxom's default behavior.  Plugins are written in Python.  We
  maintain a list of plugins in the plugin registry on the website.

  Plugins aren't hard to write.  We're happy to help you write
  plugins.

**community**

  There are several hundred Pyblosxom users out there all of whom have
  different needs.  Pyblosxom is used on a variety of operating
  systems in a variety of environments.  We have the standard open
  source project fare: mailing lists, IRC channel, wiki, ...

Pyblosxom is built to let you use existing text-manipulation tools
without having to build the whole ecology from scratch.

Pyblosxom can be run as:

* a "static renderer" and compile your blog
* a CGI script
* a WSGI application

You can learn more about Pyblosxom on the `website`_.

.. _website: http://pyblosxom.github.com/


Why you might not want to use Pyblosxom
=======================================

Pyblosxom is a small open source project and while there is a
community, it's pretty small.  Pyblosxom's features are great but make
it a niche blog system.

Pyblosxom is a *file-based* blog system.  Each blog entry is a
separate file stored in a directory hierarchy on your file system.  By
default, the hierarchy is a category tree meaning each blog entry
belongs in a single category.  By default, mtimes are used as the blog
entry timestamp.  There are plugins that change this behavior, but
require extra configuration to use.

There are a lot of other blog systems out there.  If it's apparent
that Pyblosxom won't work for you, don't force it---use something
else.


Overview of Pyblosxom
=====================

Entries, categories, storage:

* Pyblosxom stores everything as files on the file system---there is
  no database.
* Each blog entry is a file.
* Blog entry files are stored in a directory hierarchy in your *datadir*.
* Each subdirectory in your *datadir* corresponds to a category of
  your blog.

Themes:

* Themes in Pyblosxom are called *flavours*.
* A flavour consists of a set of *templates*.
* Flavours are stored in a directory called the *flavourdir*.
* Pyblosxom comes with several flavours: html, rss20, and atom.
* The `website <http://pyblosxom.github.com/>`_ maintains a flavour
  registry for flavours contributed by people like you.
* There's more information on flavours and templates in
  the Flavours and Templates chapter of the manual
  (``docs/flavours_and_templates.rst`` if you're looking at the source).

Plugins:

* Pyblosxom has a plugin system.
* Plugins are written in Python.
* Plugins are loaded using the ``plugin_dirs`` and ``load_plugins``
  configuration variables.
* The `website <http://pyblosxom.github.com/>`_ maintains a plugin
  registry for plugins submitted by people like you.
* For more information on using plugins, see Plugins in the manual
  (``docs/plugins.rst`` if you're looking at the source).
* For more information on writing plugins see Writing Plugins
  (``docs/dev_writing_plugins.rst`` if you're looking at the source).


.. _project-details-and-contact:

Project details, contact information, and where to go for help
==============================================================

See the `website <http://pyblosxom.github.com/>`_ for details on
the mailing lists, IRC, source code, issue tracker, and everything
else.


Requirements
============

* Python 2.5 or higher---does not work with Python 3 or higher
* (optional) Sphinx for building documentation
* (optional) other things depending on what plugins you install


How to install Pyblosxom
========================

If you're installing for the first time, be sure to read Installing
Pyblosxom in the manual (``INSTALL`` if you're looking at the source).

If you're upgrading from a previous Pyblosxom version, read Upgrading
Pyblosxom in the manual (``UPGRADE`` if you're looking at the source)
as well as What's New in the manual (``WHATSNEW`` if you're looking at
the source) which covers what's new in this version and what you'll
need to change in your blog.


How to find comprehensive documentation
=======================================

The source tarball comes with a ``docs/`` directory which contains the
Pyblosxom manual for that version of Pyblosxom.

The manual for the most current version and past versions of Pyblosxom
can be found on the `website <http://pyblosxom.github.com/>`_.


How to join the community
=========================

Pyblosxom is written for and by people like you.  If you're using
Pyblosxom, please contribute something back whether it's reporting a
bug, fixing something, adding a new flavour, blogging about Pyblosxom,
telling your friends, writing a plugin, or hanging out with us on IRC.

Details on where we hang out and such are on the `website
<http://pyblosxom.github.com/>`_.


How to report bugs, send in patches, fix problems
=================================================

If you have a problem with Pyblosxom, please report it!

There are several different ways to report a bug, but all bugs should
eventually make their way into our issue tracker.

1. Let someone know on IRC: #pyblosxom on irc.freenode.net

2. Send a mail to the pyblosxom-users or pyblosxom-devel mailing
   lists.  Details are on the `website
   <http://pyblosxom.github.com/>`_.

3. Write up a bug report in the issue tracker.  Details are on the
   `website <http://pyblosxom.github.com/>`_.

If you're able to fix the bug, that helps a ton!  Please attach a
patch file to the bug report or send the patch as an attachment to the
pyblosxom-devel mailing list.

When sending a patch, it helps a lot to know the details of the bug as
well as how you fixed it and whether there are outstanding issues.


How to run unit tests
=====================

Tests are written with the Python unittest module and don't require
any additional test frameworks.

To run the tests, do::

    python setup.py test

This will build Pyblosxom, then run the tests.

If you would like to add tests to the test suite, please do and send
us patches!
