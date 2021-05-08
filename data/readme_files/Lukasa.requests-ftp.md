.. image:: https://travis-ci.org/Lukasa/requests-ftp.svg?branch=master
    :target: https://travis-ci.org/Lukasa/requests-ftp

Requests-FTP
============

Requests-FTP is an implementation of a very stupid FTP transport adapter for
use with the awesome `Requests`_ Python library.

This library is *not* intended to be an example of Transport Adapters best
practices. This library was cowboyed together in about 4 hours of total work,
has no tests, and relies on a few ugly hacks. Instead, it is intended as both
a starting point for future development and a useful example for how to
implement transport adapters.

Here's how you use it:

.. code-block:: pycon

    >>> import requests_ftp
    >>> s = requests_ftp.FTPSession()
    >>> resp = s.list('ftp://127.0.0.1/', auth=('Lukasa', 'notmypass'))
    >>> resp.status_code
    '226'
    >>> print resp.content
    ...snip...
    >>> resp = s.stor('ftp://127.0.0.1/test.txt', auth=('Lukasa', 'notmypass'),
                       files={'file': open('report.txt', 'rb')})


Features
--------

Almost none!

- Adds the FTP LIST, STOR, RETR and NLST verbs via a new FTP transport adapter.
- Provides a function that monkeypatches the Requests Session object, exposing
  helper methods much like the current ``Session.get()`` and ``Session.post()``
  methods.
- Piggybacks on standard Requests idioms: uses normal Requests models and
  access methods, including the tuple form of authentication.

Does not provide:

- Connection pooling! One new connection and multiple commands for each
  request, including authentication. **Super** inefficient.
- SFTP. Security is for the weak.
- Less common commands.

Monkey Patching
---------------

Sometimes you may want to call a library that uses requests with an ftp URL.
First, check whether the library takes a session parameter. If it does, you
can use either the FTPSession or FTPAdapter class directly, which is the preferred
approach:

.. code-block:: pycon

    >>> import requests_ftp
    >>> import some_library
    >>> s = requests_ftp.FTPSession()
    >>> resp = some_library.get('ftp://127.0.0.1/', auth=('Lukasa', 'notmypass'), session=s)

If they do not, either modify the library to add a session parameter, or as an absolute
last resort, use the `monkeypatch_session` function:

.. code-block:: pycon

    >>> import requests_ftp
    >>> requests_ftp.monkeypatch_session()
    >>> import some_library
    >>> resp = some_library.get('ftp://127.0.0.1/', auth=('Lukasa', 'notmypass'))

If you expect your code to be used as a library, take particular care to avoid the
`monkeypatch_session` option.

Important Notes
---------------

Many corners have been cut in my rush to get this code finished. The most
obvious problem is that this code does not have *any* tests. This is my highest
priority for fixing.

More notably, we have the following important caveats:

- The design of the Requests Transport Adapater means that the STOR method
  has to un-encode a multipart form-data encoded body to get the file. This is
  painful, and I haven't tested this thoroughly, so it might not work.
- **Massive** assumptions have been made in the use of the STOR method. This
  code assumes that there will only be one file included in the files argument.
  It also requires that you provide the filename to save as as part of the URL.
  This is single-handedly the most brittle part of this adapter.
- This code is not optimised for performance AT ALL. There is some low-hanging
  fruit here: we should be able to connection pool relatively easily, and we
  can probably avoid making some of the requests we do.

Contributing
------------

Please do! I would love for this to be developed further by anyone who is
interested. Wherever possible, please provide unit tests for your work (yes,
this is very much a 'do as I say, not as I do' kind of moment). Don't forget
to add your name to AUTHORS.

License
-------

To maximise compatibility with Requests, this code is licensed under the Apache
license. See LICENSE for more details.

.. _`Requests`: https://github.com/kennethreitz/requests
