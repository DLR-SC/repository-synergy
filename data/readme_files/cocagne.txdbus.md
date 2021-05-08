TxDBus
======

.. image:: https://travis-ci.org/cocagne/txdbus.svg?branch=master
  :target: https://travis-ci.org/cocagne/txdbus
  :alt: Travis CI build status

.. image:: https://codecov.io/gh/cocagne/txdbus/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/cocagne/txdbus
  :alt: Codecov coverage report

.. image:: https://img.shields.io/pypi/v/txdbus.svg
  :target: https://pypi.python.org/pypi/txdbus
  :alt: version on pypi

.. image:: https://img.shields.io/pypi/l/txdbus.svg
  :target: https://github.com/cocagne/txdbus/blob/master/LICENCE
  :alt: licence

Tom Cocagne <tom.cocagne@gmail.com>
v1.1.0, July 2017

Introduction
------------

TxDBus is a native Python implementation of the `DBus protocol`_ for the
Twisted_ networking framework.

In addition to a tutorial_, and collection of examples_ the documentation for
this project also includes `An Overview of the DBus Protocol`_.

*License*: MIT_

.. _DBus Protocol: https://dbus.freedesktop.org/doc/dbus-specification.html
.. _Twisted: https://twistedmatrix.com/trac/
.. _Tutorial: https://packages.python.org/txdbus
.. _Examples: https://github.com/cocagne/txdbus/tree/master/doc/tutorial_examples
.. _An Overview of the DBus Protocol: https://packages.python.org/txdbus/dbus_overview.html
.. _MIT: https://choosealicense.com/licenses/mit/

Usage Example
-------------

.. code-block:: python

    #!/usr/bin/env python

    from twisted.internet import reactor, defer
    from txdbus import error, client

    @defer.inlineCallbacks
    def show_desktop_notification():
        '''
        Displays "Hello World!" in a desktop notification window for 3 seconds
        '''
        con = yield client.connect(reactor, 'session')

        notifier = yield con.getRemoteObject('org.freedesktop.Notifications',
                                             '/org/freedesktop/Notifications')

        nid = yield notifier.callRemote('Notify',
                                        'Example Application', 
                                        0,
                                        '',
                                        'Tx DBus Example',
                                        'Hello World!',
                                        [], dict(),
                                        3000)
        
        reactor.stop()

    reactor.callWhenRunning(show_desktop_notification)
    reactor.run()
