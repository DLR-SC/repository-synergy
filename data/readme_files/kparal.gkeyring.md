========
gkeyring
========

----

.. image:: http://unmaintained.tech/badge.svg
  :target: http://unmaintained.tech/
  :alt: No Maintenance Intended

**gkeyring is no longer maintained!**

This tool relies on an obsolete Python2-only library and slowly reached the end of its life. As a replacement, you can have a look at ``secret-tool`` command included in the `libsecret <https://wiki.gnome.org/Projects/Libsecret>`_ library or at the `keyring <https://pypi.org/project/keyring/>`_ library with a same-named command.

If you feel that gkeyring should be resurrected and modernized, please fork this project and work on your improvements. I'll gladly redirect people to your new version.

----

A small Python tool for shell access to GNOME keyring. It provides simple querying for and creating of keyring items.

Installation
============

Distribution packages
---------------------

There are some distribution packages you can use:

* Arch: `gkeyring <https://aur.archlinux.org/packages/gkeyring>`_
* Ubuntu: `gkeyring <https://launchpad.net/~kampka/+archive/ppa>`_

PyPI
----

You can install this tool from `PyPI <https://pypi.python.org/pypi/gkeyring>`_ (using `pip <http://pip.openplans.org/>`_, `setuptools <http://peak.telecommunity.com/DevCenter/setuptools>`_ or `distutils <http://docs.python.org/install/index.html#install-index>`_)::

  $ pip install --upgrade --user gkeyring

That will find, download and install the latest available version of the program into your home directory.

You might need to install some package dependencies when installing from PyPI:

* gnome-python2-gnomekeyring


... or, of course, you can check out this git repo directly.

Running
=======

Run::

  $ gkeyring --help

to see instructions how to control this program.

License
=======

This program is a free software, licensed under `GNU AGPL 3+ <http://www.gnu.org/licenses/agpl-3.0.html>`_.

Contact
=======

Visit `the program homepage <https://github.com/kparal/gkeyring>`_ and `the support forum <https://answers.launchpad.net/gkeyring>`_.

Please report all bugs to the `issue tracker <https://github.com/kparal/gkeyring/issues>`_, but don't request new features unless you have a patch for it. This program is maintained, but not further developed. If you want to work on this program, don't hesitate to contact me, I will gladly assign you to the development team.
