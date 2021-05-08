# pbp

v0.3.2 - experimental

PBP[0] is a simple python wrapper and a command line interface around
libsodium, to provide basic functionality resembling PGP. It uses
scrypt for a KDF and a much simpler packet format, which should be
much harder to fingerprint, pbp also provides an experimental forward
secrecy mode and a multi-party DH mode.

## Installation

You possibly need to run (or an equivalent command) `sudo apt-get install git
python-virtualenv gcc python-dev libffi-dev scrypt` to satisfy all basic dependencies.
And install libsodium (http://doc.libsodium.org/installation/README.html).

    pip install pbp

optionally for PITCHFORK support also

    pip install pyusb==1.0.0b1

Design goals:

 1. use modern crypto
 2. provide similar functionality to PGP
 3. be extensible
 4. difficult to identify based on fingerprinting
 5. provide extensive testing
 6. strive for security

## Crypto

Cryptographic primitives are based on the NaCl library from
http://nacl.cr.yp.to. The KDF used is scrypt.

## PGP-like

Provides basic public key encrypt/decrypt, sign/verify and secret key
encrypt/decrypt modes, as well as the ability to sign, verify, list,
generate, export and import keys.

## Extensibility

using pbp and the underlying pysodium[1] library it's easy to extend
pbp.  Some examples are the experimental forward secrecy mode (see
description in doc/chaining-dh.txt), the support for ECDH key
exchanges from the command-line and generation of arbitrarily large
random byte streams.

[1] https://github.com/stef/pysodium also available on
    https://pypi.python.org/pypi/pysodium

## Fingerprinting

pbp tries to avoid to store any sensitive plaintext info, the
encrypted files all should look like random noise. for a description
of the packet formats see doc/fileformats.txt.

## Testing

All py files come with their internal tests, unit tests are in
tests.py, and commandline functionality is tested in test.sh.

## Security

pbp locks the process memory, so it cannot be swapped to disk. Also
pbp uses SecureString[2] to overwrite sensitive key material after
usage in memory, so keys have a short window of opportunity to leak.

[2] https://github.com/dnet/pysecstr

## Usage

Generate a key

    pbp -g -n alice

sending howdy.txt using public key encryption from alice to bob

    pbp -c -S alice -r bob -i howdy.txt

decrypt an encrypted file using public key crypto

    pbp -d -S bob -i howdy.txt.pbp

sending howdy.txt using secret key encryption

    pbp -c -i howdy.txt

decrypt an encrypted file using secret key crypto

    pbp -d -i howdy.txt.pbp

sign howdy.txt

    pbp -s -S alice -i /howdy.txt

verify howdy.txt

    pbp -v -i howdy.txt.sig

sign bobs key

    pbp -m -S alice -n bob

check sigs on carols key

    pbp -C -n carol

alice encrypts howdy.txt to bob using experimental forward secret mode

    pbp -e -S alice -r bob -i howdy.txt -o ./secret-message

bob decrypts howdy.txt from alice using experimental forward secret mode

    pbp -E -S bob -r alice -i ./secret-message

initiate ECDH key exchange

    pbp -D1

respond to ECDH key exchange

    pbp -D2 -Dp 'public component from D1'

finish ECDH key exchange

    pbp -D3 -Dp 'public component from D2' -De 'secret exponent from D1'

random streaming 23GByte of cryptographic randomness

    pbp -R -Rs 23G -o /mnt/huge_fs/random_data

participate in a 4-way DH exchange, 1st message

    pbp -Ds -Dp 4 -S alice -n 'friends001' -i oldkeychain -o newkeychain

participate in a 4-way DH exchange, 2nd message

    pbp -De -S alice -n 'friends001' -i oldkeychain -o newkeychain

this is one big pipe that creates a 3-way ECDH secret between alice, bob and carol:

    pbp -Ds -S alice -Dp 3 -n 'test-dh' -i /dev/null |
    pbp -Ds -S bob -Dp 3 -n 'test-dh' |
    pbp -Ds -S carol -Dp 3 -n 'test-dh' |
    pbp -De -S alice -Dp 3 -n 'test-dh' |
    pbp -De -S bob -Dp 3 -n 'test-dh'

of course instead of a pipe you could use any kind of transport mechanism

## Integration

you can add the following to your .vimrc

    map ;e :%!/bin/sh -c 'pbp -c 2>/dev/tty \| base64'<C-M>
    map ;d :%!/bin/sh -c 'base64 -d \| pbp -d 2>/dev/tty'<C-M>
    map ;s :,$! /bin/sh -c 'pbp -s -a -S stf 2>/dev/tty'<C-M>
    map ;v :,$! /bin/sh -c 'pbp -v -a 2>/dev/tty'<C-M>

(c) 2013, stf <s@ctrlc.hu>, dnet vsza@vsza.hu, AGPLv3.0+

[0] also it's very funny to say pbp with a mouth full of dry cookies.
don't try this in company!

[![Build Status](https://travis-ci.org/stef/pbp.svg?branch=master)](https://travis-ci.org/stef/pbp)
