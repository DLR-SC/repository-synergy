EVE Market Data Relay
=====================

:Author: Greg Taylor
:License: BSD
:Status: Unmaintained

**With the introduction of native-to-EVE market APIs, the EMDR project has ran its course. As of May 1, 2017, we have shuttered the network. This repo will remain in an archived state. Thanks to all who helped make EMDR a success!**

This project is a super-scalable, affordable way to
accept a large amount of user-submitted market data (via uploaders), and
re-broadcast said data in realtime to a number of subscribers.

The end result is that those writing market-data driven applications can
simply subscribe to a "firehose" of market data, and get going, without having
to hassle with uploaders or data submission APIs.

Additionally, the consumers may accept very large amounts of data without the
overhead associated with a ton of HTTP connections. EMDR's ZeroMQ underpinnings
are hugely more efficient.

Documentation
-------------

Make sure to read the Documentation_ for more details.

.. _Documentation: http://readthedocs.org/docs/eve-market-data-relay/

License
-------

This project, and all contributed code, are licensed under the BSD License.
A copy of the BSD License may be found in the repository.
