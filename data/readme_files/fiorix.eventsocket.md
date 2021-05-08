===========
eventsocket
===========
:Info: See `the FreeSWITCH Event Socket documentation <http://wiki.freeswitch.org/wiki/Event_Socket>`_ for more information. See `github <http://github.com/fiorix/eventsocket/>`_ for the latest source.
:Author: Alexandre Fiori <fiorix@gmail.com>
:Author: Arnaldo M. Pereira <egghunt@gmail.com>

About
=====
`eventsocket` is a Twisted protocol for the FreeSWITCH's Event Socket. This protocol provides support for both Inbound and Outbound methods of the Event Socket in a single-file class.

It may be used for a wide variety of purposes. It aims to be simple and extensible, and to export all the functionality of the FreeSWITCH to Twisted-based applications.

Moreover, it's totally event-driven and allows easy implementation of complex applications aiming at controlling the FreeSWITCH through the Event Socket.

This code is part of the core of the `Nuswit Telephony API <http://nuswit.com>`_, a full featured web-based dialer currently operating in Brazil and Colombia.

Examples
========
Examples are available in the `examples/ <http://github.com/fiorix/eventsocket/tree/master/examples/>`_ directory.

Credits
=======
Thanks to (in no particular order):

- Nuswit Telephony API

  - Granting permission for this code to be published and sponsoring
