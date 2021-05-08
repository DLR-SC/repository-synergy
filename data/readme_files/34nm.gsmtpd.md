gsmtpd
======


.. image:: https://travis-ci.org/34nm/gsmtpd.svg?branch=master

SMTP servers impletement base on Gevent

Install
----------

`pip install gsmtpd`

Usage
---------

Basically gsmtpd is ported from Python standard lib *smtpd*,
you can it check from Doc_

however there is only one difference, you should add monkey patch of gevent

.. code-block:: python

    from gevent import monkey
    monkey.patch_all()

Example
-----------------

.. code-block:: python
        
    from gevent import monkey 
    monkey.patch_all()
    from gsmtpd.server import SMTPServer

    class DebuggingServer(SMTPServer):
        # Do something with the gathered message
        def process_message(self, peer, mailfrom, rcpttos, data):
            inheaders = 1
            lines = data.split('\n')
            print '---------- MESSAGE FOLLOWS ----------'
            for line in lines:
                # headers first
                if inheaders and not line:
                    print 'X-Peer:', peer[0]
                    inheaders = 0
                print line
            print '------------ END MESSAGE ------------'
    
    if __name__ == "__main__":
        
        server = DebuggingServer()
        server.serve_forever()

Performance
---------------

The charts below shows gsmtpd vs asyncore based smtpd in Python standrary lib.

.. note::

    Response per second = 0 means the program is crashed or refuse to connect



.. figure:: https://raw.githubusercontent.com/34nm/gsmtpd/master/helo_chart.png
    :scale: 100%

.. figure:: https://raw.githubusercontent.com/34nm/gsmtpd/master/mail_chart.png
    :scale: 100%


.. _Doc: http://gsmtpd.readthedocs.org
