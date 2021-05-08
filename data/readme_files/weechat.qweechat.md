= QWeeChat
:author: Sébastien Helleu
:email: flashcode@flashtux.org
:lang: en


image:https://travis-ci.org/weechat/qweechat.svg?branch=master["Build Status", link="https://travis-ci.org/weechat/qweechat"]

QWeeChat is a Qt remote GUI for WeeChat written in Python.

Homepage: https://weechat.org/

== Features

* Multi-platform (GNU/Linux, *BSD, Mac OS X, QNX, Windows & others).
* Free software, released under GPLv3.

image::https://weechat.org/media/images/screenshots/relay/medium/qweechat_shadow.png[align="center"]

== Install

=== Dependencies

Following packages are *required*:

* WeeChat (version >= 0.3.7) on local or remote machine, with relay plugin
  enabled and listening on a port with protocol "weechat"
* Python 2.x >= 2.6
* PySide (recommended, packages: python.pyside.*) or PyQt4 (python-qt4)

=== Install via source distribution

----
$ python setup.py install
----

== WeeChat setup

You have to add a relay port in WeeChat, for example on port 1234:

----
/set relay.network.password "mypass"
/relay add weechat 1234
----

== Connect to WeeChat

In QWeeChat, click on connect and enter fields:

* _server_: the IP address or hostname of your machine with WeeChat running
* _port_: the relay port (defined in WeeChat)
* _password_: the relay password (defined in WeeChat)

Options can be changed in file _~/.qweechat/qweechat.conf_.

== Copyright

Copyright (C) 2011-2020 Sébastien Helleu <flashcode@flashtux.org>

This file is part of QWeeChat, a Qt remote GUI for WeeChat.

QWeeChat is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.

QWeeChat is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with QWeeChat.  If not, see <http://www.gnu.org/licenses/>.
