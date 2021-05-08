rarchives' album ripper
=======================

about
-----

download & provide zips for image albums on various websites.

implementation
--------------

[http://rip.rarchives.com/](http://rip.rarchives.com)

extensibility
-------------

rippers for various sites are in the [/sites/](https://github.com/4pr0n/rip/tree/master/sites) subdirectory.

all site rippers extend the [basesite.py](https://github.com/4pr0n/rip/blob/master/sites/basesite.py) super class. this file contains documentation about required overrides and other helper methods.

#### Wiki outlining the process of creating a new ripper:

### [wiki/Supporting-a-new-site](https://github.com/4pr0n/rip/wiki/Supporting-a-new-site)

installation
------------

Some webdevs have had issues installing the site on their own Apache servers. This guide clears up some known issues:

* [wiki/Installation](https://github.com/4pr0n/rip/wiki/Installation)

license
-------

licensed under the [GNU GPL v2](http://www.gnu.org/licenses/gpl-2.0.txt) public license.
