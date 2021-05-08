ABOUT THIS PROJECT
------------------
The xmlrpc interface to rTorrent is extremely unintuitive and has very little documentation, this project aims to make interfacing with rTorrent much easier.

NOTE: This project is considered beta, so expect the API to change. API changes will be noted in the changelog.

REQUIREMENTS
------------
- [Python](http://www.python.org/) 2.6 or higher, 3.0 or higher (might work on older versions, but these are the only ones I'm supporting).
- [rTorrent](http://libtorrent.rakshasa.no/) 0.8.1 or later, with xmlrpc-c support (see [this guide](http://libtorrent.rakshasa.no/wiki/RTorrentXMLRPCGuide)).
- [xmlrpc-c](http://xmlrpc-c.sourceforge.net/) 1.00 or later. 1.07 or later for 64bit integer support (highly recommended, download either the stable or advanced branches).
- [Apache](http://www.apache.org/) or [lighttpd](http://www.lighttpd.net/)

INSTALLATION
------------

If you're downloading the source:

```$ python setup.py install```

Or you can install directly from PyPI:

```$ pip install rtorrent-python```

ROADMAP
-------
- v0.3.0
  - Add option for fast RTorrent init (skip paranoid check)

- unknown
  - Logging support
  - Documentation and examples
  - Add support for views

CREDITS
-------

[fuzeman](https://github.com/fuzeman)
