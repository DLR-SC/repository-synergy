mattersend |build-status| |cover-status|
========================================

CLI tool to send messages to the Incoming webhook of mattermost (http://www.mattermost.org/).

Help
----

::

	usage: mattersend [-h] [-V] [-C CONFIG] [-s SECTION] [-c CHANNEL] [-U URL]
	                  [-u USERNAME] [-i ICON] [-t [DIALECT] | -y SYNTAX] [-n]
	                  [-f FILE]

	Sends messages to mattermost's incoming webhooks via CLI

	optional arguments:
	  -h, --help            show this help message and exit
	  -V, --version         show program's version number and exit
	  -C CONFIG, --config CONFIG
	                        Use a different configuration file
	  -s SECTION, --section SECTION
	                        Configuration file section
	  -c CHANNEL, --channel CHANNEL
	                        Send to this channel or @username
	  -U URL, --url URL     Mattermost webhook URL
	  -u USERNAME, --username USERNAME
	                        Username
	  -i ICON, --icon ICON  Icon
	  -t [DIALECT], --tabular [DIALECT]
	                        Parse input as CSV and format it as a table (DIALECT
	                        can be one of sniff, excel, excel-tab, unix)
	  -y SYNTAX, --syntax SYNTAX
	  -n, --dry-run, --just-print
	                        Don't send, just print the payload
	  -f FILE, --file FILE  Read content from FILE. If - reads from standard input
	                        (DEFAULT: -)

Configuration file
------------------

The only required option to start sending messages to mattermost is the webhook url.
You can either set this in a configurations file (globally in */etc/mattersend.conf* or locally in *$HOME/.mattersend.conf*) or specify it on the CLI with the --url argument.

You can have multiple sections to override DEFAULT settings and later select them from the CLI with the --section argument.

This is an example of a configuration file for mattersend::

	[DEFAULT]
	url = https://mattermost.example.com/hooks/XXXXXXXXXXXXXXXXXXXXXXX
	icon = :ghost:
	username = This is a bot
	channel = @myself

	[angrybot]
	icon = :angry:
	username = AngryBot

Example usage
-------------

::

	echo "Hello world!" | mattersend -U https://mattermost.example.com/hooks/XXX

	# you can omit -U with mattersend.conf
	echo "Hello world!" | mattersend

	# send file content
	mattersend -f todo.txt

	# table data
	echo -e "ABC;DEF;GHI\nfoo;bar;baz" | mattersend -t

LICENSE
-------
Copyright (c) 2016 Massimiliano Torromeo

mattersend is free software released under the terms of the BSD license.

See the LICENSE file provided with the source distribution for full details.

Contacts
--------

* Massimiliano Torromeo <massimiliano.torromeo@gmail.com>

.. |build-status| image:: https://travis-ci.org/mtorromeo/mattersend.svg?branch=master
   :target: https://travis-ci.org/mtorromeo/mattersend
   :alt: Build status
.. |cover-status| image:: https://coveralls.io/repos/github/mtorromeo/mattersend/badge.svg?branch=master
   :target: https://coveralls.io/github/mtorromeo/mattersend?branch=master
