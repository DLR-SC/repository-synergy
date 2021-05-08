journal2gelf
============

Export structured log records from the systemd journal and send them to a
Graylog2 server as GELF messages.

Tested on Python 2.7 and Fedora 17 (systemd-44-17) and Fedora 19 (systemd-204).

journalctl output format change
-------------------------------

Starting with systemd-190 journalctl switched to an easier to parse single-line
JSON format. This is now the default expected format as of journal2gelf v0.0.3.

For versions of systemd < 190, you must add the `-m` switch.

Run `journalctl --version` to get the systemd version.

Dependencies:
-------------

- graypy


Install
-------

On Fedora 17+ (or other systems with a version of systemd that includes journal
support):

```
sudo yum install git python-pip
pip-python install git+http://github.com/systemd/journal2gelf.git#egg=journal2gelf
```

Running as a service
--------------------

Copy and edit the included `examples/journal2gelf.service` to
`/etc/systemd/system`.

Usage:
------

By default, journal2gelf will look for input on stdin. eg:

- Send all logs and exit:

    journalctl -o json | journal2gelf

The `-t` flag can be specified and journal2gelf will automatically
start journalctl in tail mode. This makes it easier to run as a systemd service.

    journal2gelf -t

This is equivalent to running:

    journalctl -o json -f | journal2gelf

Graylog2 server and port can be specified with `-s` and `-p` flags.


License
-------
Copyright 2012 Joe Miller <https://github.com/joemiller>

Released under the MIT license, see LICENSE for details.
