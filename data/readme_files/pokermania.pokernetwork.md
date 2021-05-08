Poker Network
=============


What is it ?
------------

poker-network includes a poker server, a client library, an abstract user
interface library and a client based on it.

The server deals the cards and checks the user actions using a poker game engine
(poker-engine). It listens on a TCP/IP port and understands a poker-network
specific protocol. The persistent informations (accounts, hand history etc.) are
stored in a MySQL database. The server was designed and tested to gracefully
handle 1000 simultaneous players on a single machine also running the MySQL
server.

The client library implements the poker-network protocol for the client. It runs
a poker-engine identical to the one used by the server and uses it to simplify
the implementation of a client. For instance it creates an event indicating that
the player lost position although the server does not send such a packet. A
simple minded bot is provided as an example usage of the client library.

The abstract user interface library provides a framework based on the client
library and suited to implement a user friendly client. A display is fed with
events such as give seat S to player P or get amount A from side pot P to player
P so that the rendering part of the user interface does not need to maintain
contextual game information. A toolkit is fed with high level interaction actions
such as ask login and password or display the following holdem tables. An
animation module is fed with events that can trigger animations or sounds such
as player P timeouted or player P wins the pot.


Development status : Production [![Build Status](https://travis-ci.org/pokermania/pokernetwork.png)](https://travis-ci.org/pokermania/pokernetwork)
-------------------------------

* Features may still be added
* The protocol is rarely changed (backwards compatible if possible)
* The classes API is not stable

Download, feedback and bug reports

http://github.com/pokermania/pokernetwork/


Installation
------------

> python setup.py configure -s test.example=example

will set config.json['test']['example'] to example

> python setup.py configure -b

will build the .in files

If this is your first installation, you need to fill the MySQL root user name
and password in ${pkgsysconfdir}/poker.server.xml. It will be used to create the
poker database and user.

Requirements
------------

* python 2.6, 2.7
* twisted >= 11.1
* pokerdistutils
* pokerpackets
* pokerengine
* reflogging
* MySQL-python
* simplejson
* python-memcached
* libxml2
* libxslt

License
-------

See file, LICENSE, in this directory, for full information about the
licensing of this software.
