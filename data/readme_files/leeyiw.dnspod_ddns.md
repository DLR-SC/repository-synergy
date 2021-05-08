Introduction
============

**dnspod_ddns** a Python tool to dynamic update DNS record at DNSPod.

Installing
==========

Clone the repo with `git` and install the requirements with `pip`:
```
$ git clone https://github.com/leeyiw/dnspod_ddns.git
$ cd dnspod_ddns
$ sudo pip install -r requirements.txt
```

Then edit `config.py`, replace the value of `LOGIN_EMAIL`, `LOGIN_PASSWORD`, `SUB_DOMAIN`, `DOMAIN` with your DNSPod account and the domain you want to dynamic update.

Usage
=====

Command line options are:
```
Usage:
  dnspod_ddns.py [options]

Options:
  -h --help      Show this screen.
  -t TIME        Check IP change every TIME seconds [default: 60].
  -d ACTION      Run this script as a daemon (e.g. start,stop,restart).
  -l LOG_PATH    Program log file [default: /var/log/dnspod_ddns.log].
  -p PID_FILE    Use PID_FILE as daemon's pid file [default: /var/run/dnspod_ddns.pid].
```

You can run this script as a daemon with command:
```
sudo python dnspod_ddns.py -d start
```

Or run it in foreground mode with the following command (`-l` and `-p` options will be ignored, and log will output to console):
```
python dnspod_ddns.py
```
