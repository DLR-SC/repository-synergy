Extension Auto-Installer (DEPRECATED!)
======================================

**IMPORTANT**: This extension is deprecated, it will not work in Firefox 57 and above. Providing comparable functionality in newer Firefox versions isn't possible.

Extension Auto-Installer is a helper for Firefox/SeaMonkey/Thunderbird extension developers: it allows automatically adding or updating browser extensions, e.g. via command line tools. This makes testing your changes easier. [Detailed description](https://palant.de/2012/01/13/extension-auto-installer)

Prerequisites
-------------
* [Python 2.7](https://www.python.org/downloads/)
* [Jinja2 module for Python](http://jinja.pocoo.org/docs/intro/#installation)

How to build
------------

Run the following command:

    python build.py build

This will create a development build with the file name like `autoinstaller-1.2.3.nnnn.xpi`. In order to create a release build use the following command:

    python build.py build --release

How to test
-----------

Testing your changes is easiest if you already have Extension Auto-Installer installed, e.g. the [stable version](https://addons.mozilla.org/addon/autoinstaller/). Then you can push the current repository state to your browser using the following command:

    python build.py autoinstall 8888

Extension Auto-Installer will be updated automatically, without any prompts or browser restarts.
