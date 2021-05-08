MobilePASSER
============

MobilePASSER is a reimplementation of the MobilePASS client in Python.

Installation
------------

```
python setup.py install
```

Usage
-----

```
usage: mobilepasser [-h] [-k ACTIVATION_KEY] [-x INDEX] [-p POLICY]
                    [-l OTP_LENGTH] [-a]

optional arguments:
  -h, --help            show this help message and exit
  -k ACTIVATION_KEY, --activation-key ACTIVATION_KEY
                        The string the MobilePass client generated.
  -x INDEX, --index INDEX
                        The index of the token to generate.
  -p POLICY, --policy POLICY
                        Policy for the token.
  -l OTP_LENGTH, --otp-length OTP_LENGTH
                        Length of the returned OTP.
  -a, --auto-update-index
                        Automatically bump the index by 1 and save to config
                        file.
```

Configuration
-------------
The configuration file is read form `~/.mobilepasser.cfg`. An example config file can be found in the examples folder.
