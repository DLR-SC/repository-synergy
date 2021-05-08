.. image:: https://travis-ci.org/pyjs/pyjs.png
    :target: https://travis-ci.org/pyjs/pyjs
    :alt: Build Status

Pyjs
====

Pyjs is a port of Google Web Toolkit to Python, and thus enables
the development of Rich Media AJAX applications in Python, with no
need for special browser plugins.  Pyjs contains a stand-alone
python-to-javascript compiler, and also a Widget Set API that looks
very similar to Desktop Widget Set APIs (such as PyQT4 or PyGTK2).

Pyjs also contains a Desktop Widget Set version, running as pure
python, with three useable Desktop ports available.  With web-engine
technology at it's core, HTML, CSS, plugins and other related features
work out-of-the-box.


Pyjs-Compiler
=============

Pyjs-Compiler is a collection of tools that are related to
  * compiling python code to javascript
  * linking compiled javascript modules into complete applications
  * converting java to python, etc.

Pyjs-Compiler runs your python application in a Web Browser (as javascript).


Pyjs-Widgets
============

Pyjs-Widgets is a collection of GUI widget libraries that can be run natively
as part of Pyjs-Native or can be compiled by Pyjs-Compiler to run in a browser.


Pyjs-Desktop
============

While Pyjs runs your python application in a Web Browser (as javascript),
Pyjs-Desktop runs exactly the same python application on the
Desktop (as pure python).  There are currently three engine
choices, with alternatives in development.

All ports of Pyjs-Desktop require a JSON library; simplejson is
recommended if the version of python is 2.5 or older.  Python 2.6
and above come with a json library installed by default.

1. XULRunner

   Install hulahop and python-xpcom.  Hulahop, from OLPC SugarLabs,
   is distributed with both Debian and Ubuntu; python-xpcom is part
   of XULRunner and is also distributed with both Debian and Ubuntu.
   Other users should investigate the installation instructions for
   python-xpcom and hulahop for the operating system of their choice
   on the appropriate web sites.

   Older versions of XULRunner must be used: versions 1.9.0 or 1.9.1 are
   known to be suitable, as is version 9.0.  Versions 10 and above are
   known to segfault.

2. GIWebKit (GObject Introspection)

   A 95% functional binding enabled via the dynamic GObject/Python bindings
   produced by https://wiki.gnome.org/GObjectIntrospection after scanning the
   annotated WebKit sources. This backend is missing a critical piece,
   window.addEventListener, from https://bugs.webkit.org/show_bug.cgi?id=77835
   but development is in progress to implement the missing binding via ctypes
   instead, due to a lack of interest by WebKit.

   This is intended to supercede XULRunner as the default on Linux once ready.

   GIWebKit must be explicitly enabled.  Create a $HOME/.pyjd/pyjdrc file
   containing the following two lines:

   [gui]
   engine=giwebkit

3. MSHTML

   For Windows users - all that's required, other than installing python
   and Internet Explorer, is one further tiny package: Win32 "comtypes".

   Win32 "comtypes" can be downloaded here:
   * http://sourceforge.net/projects/comtypes/

   Unlike the other ports, which can comprise a whopping great bundle
   of anything up to 30mb in size, the MSHTML port literally requires
   nothing more than comtypes, thanks to the far-sighted design of the
   MSHTML Trident Engine and its extensive COM interface.


Installation
===============

Access our "Getting Started" wiki (https://github.com/pyjs/pyjs/wiki/GettingStarted) for get information about installation, examples, troubleshooting, etc.

For more information and documentation, see:

* http://pyjs.org
* https://github.com/pyjs/pyjs/wiki

For issue tracking:

* https://github.com/pyjs/pyjs/issues

To join the mailing list:

* https://groups.google.com/group/pyjs-users

IRC:

:Server: irc.freenode.net
:Channel: #pyjs

