PlagueScanner
=============
PlagueScanner is a multiple AV scanner framework for orchestrating a group of individual AV scanners into one contiguous scanner. There are two basic components in this initial release: Core and Agents.

All PlagueScanner components have the following dependencies:

1. Python3: https://www.python.org/
2. ZeroMQ: http://zeromq.org/
3. pyzmq: https://github.com/zeromq/pyzmq

The Agents have the following additional dependency:

1. Requests: http://docs.python-requests.org/en/latest/

And the Core has the following dependency.

5. Web Server (NGINX recommended): http://nginx.org/

In the same directory as each .py file, there needs to be a config file with the following format.
```
[PlagueScanner]
IP = 
Port = 5556
OutboundSamplesDir = /usr/local/www/plaguescanner
[ClamAV]
IP = 
[ESET]
IP = 
[Bitdefender]
IP = 
```

The scanners used were the following:

1. ClamAV: http://www.clamav.net/index.html
2. ESET: http://www.eset.com/us/business/server-antivirus/file-security-linux/
3. Bitdefender: http://www.bitdefender.com/business/antivirus-for-unices.html

**Note**: The Trend Micro agent is missing the regex. This will be fixed shortly.

The directory that NGINX serves needs to have group permissions set +w and the user that you run plaguescanner.py as added to that same group.

This has been tested with each scanner installed on separate VMs with the Core also separate. The Core and each of the other VMs should all be on the same closed network segment. After starting each agent, scan a file like so:

```
$ ./plaguescanner.py sample.exe
```
