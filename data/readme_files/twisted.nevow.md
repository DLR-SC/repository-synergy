
Divmod Nevow
============

Divmod Nevow is a web application construction kit written in Python. It is
designed to allow the programmer to express as much of the view logic as
desired in Python, and includes a pure Python XML expression syntax named stan
to facilitate this. However it also provides rich support for designer-edited
templates, using a very small XML attribute language to provide bi-directional
template manipulation capability.

Nevow also includes Divmod Athena, a "two way web" or "`COMET`_"
implementation, providing a two-way bridge between Python code on the server
and JavaScript code on the client.  Modular portions of a page, known as
"athena fragments" in the server python and "athena widgets" in the client
javascript, can be individually developed and placed on any Nevow-rendered page
with a small template renderer.  Athena abstracts the intricacies of HTTP
communication, session security, and browser-specific bugs behind a simple
remote-method-call interface, where individual widgets or fragments can call
remote methods on their client or server peer with one method: "callRemote".

Installation
------------

Before installing Nevow, you should install `Twisted`_, unless you are going to
write very simple CGI applications. Nevow integrates fully with the twisted.web
server providing easy deployment.

Nevow uses the standard distutils method of installation::

    python setup.py install

If you do not have Twisted installed, you can run a subset of the tests using
the test.py script. If you have twisted installed, the test.py script will
issue the following trial command::

    trial -v nevow.test formless.test

.. _`Twisted`: http://twistedmatrix.com/

Documentation
-------------

More detailed introductory documentation is available in the doc/ directory,
along with the beginnings of a reference manual. A large number of examples are
available in the examples/ directory. These examples require Twisted to run. A
tac file (twisted application configuration) can be started by invoking twistd,
the twisted daemon::

    twistd -noy foo.tac

More Information
----------------

Information about `Nevow commits`_ is available on GitHub.
The Nevow git repository can be checked out using::

  git clone https://github.com/twisted/nevow.git

Discussion of Nevow occurs on the `twisted.web mailing list`_. The Nevow
developers are also often available for real-time help on the `#twisted.web
channel`_ on irc.freenode.net.

.. _`Nevow commits`: https://github.com/twisted/nevow/commits/master
.. _`twisted.web mailing list`: http://twistedmatrix.com/cgi-bin/mailman/listinfo/twisted-web
.. _`#twisted.web channel`: irc://irc.freenode.net/#twisted.web
.. _`COMET`: http://alex.dojotoolkit.org/?p=545
