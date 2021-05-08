== PyHSM - Python YubiHSM Project

=== Introduction
PyHSM is a Python package to talk to a YubiHSM.  The YubiHSM is Yubico's take
on the Hardware Security Module (HSM), designed for protecting secrets on
authentication servers, including cryptographic keys and passwords, at
unmatched simplicity and low cost.

=== License
The project is licensed under the BSD license, see the file COPYING for exact
wording.

=== Description
PyHSM aims to be a reference implementation implementing all the functions
available in the YubiHSM.

PyHSM also includes the regression test suite for the YubiHSM. Instructions on
running this test suite can be found in test/README.adoc.

In general, see the files in `examples/` to get an idea of how to use this
code.

In addition to the YubiHSM communication library, PyHSM also contains some
applications utilizing the YubiHSM:

* yhsm-val: a simple validation server supporting validation of YubiKey
  OTPs, OATH codes and password hashes.

* yubikey-ksm: ykval YubiKey OTP decryption backend using the YubiHSM.

Some smaller scripts are also available:

* yhsm-linux-add-entropy: Feed Linux kernel with random entropy from
  the TRNG on the YubiHSM.

* yhsm-keystore-unlock: Unlock the key storage in the YubiHSM with your HSM
  password. Use with incorrect password to lock it again.

* yhsm-daemon: Talk to the YubiHSM directly over TCP.

And some more in `examples/`:

* yhsm-sysinfo.py: Print basic system information about the connected YubiHSM.

* yhsm-monitor-exit.py: Get a YubiHSM *in debug mode* to enter configuration
  mode again, without having to press the little button while inserting it into
  the USB port.

* yhsm-password-auth.py: Example of how to turn passwords (or hashes of
  passwords if you like PBKDF2) into AEADs that can be used to verify the
  password later on.

=== Installation
PyHSM is known to work with Python 2.6 and 2.7, and is primarily tested using
Debian/Ubuntu, but is of course meant to work on as many platforms as possible.

NOTE: If you want to use any of the daemons (yhsm-validation-server,
yhsm-yubikey-ksm) you will want to use Python 2.7 or later. `SocketServer.py`
lacks critical timeout handling in Python 2.6.

The http://pyserial.sourceforge.net[pyserial] package is needed.

  Debian: apt-get install python-serial

You will also need http://www.pycrypto.org[pycrypto].

  Debian: apt-get install python-crypto

Please note that the pycrypto version has to be 2.1 or higher -- it is
known that RHEL6 has a lower version.

For database support http://www.sqlalchemy.org[SQLAlchemy] is needed.

  Debian: apt-get install python-sqlalchemy

PyHSM easily installed via pip, which will also take care of the dependencies
automatically, though some of these require other build dependencies to
correctly install (note the added optional dependencies needed for yubikey-ksm,
yhsm-val and tools):

  $ pip install pyhsm[db,daemon]

or, on Debian based systems (dependencies will also be handled automatically):

  $ sudo apt-get install python-pyhsm
  
additional Debian packages available are:

  yhsm-tools yhsm-yubikey-ksm yhsm-validation-server yhsm-daemon

=== Working with the source code repository
To work with the source code repository, if you wish to build your own release
or contribute pull requests, follow these steps to set up your environment. If
you just wish to install the application use the source release packages. This
project is developed on a Debian based system, other OSes may not be supported
for development.

==== Check out the code
Run these commands to check out the source code:

  git clone https://github.com/Yubico/python-pyhsm.git
  cd python-pyhsm
