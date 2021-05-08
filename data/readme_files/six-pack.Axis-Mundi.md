NOTE: The Tails documentation better describes the install process for the moment.

Installation
============

1) If you do not have PIP installed then do that first from a terminal
    $ sudo apt-get install python-pip
2) Download client files from https://github.com/six-pack/axis-mundi/archive/master.zip
3) Extract to your chosen location
4) Open a terminal and change directory to the location you extracted the client to
4) If you have not already installed the pre-requisite python dependencies (you only have to do this once) then
do so now using the commands:

    $ sudo pip install -r requirements.txt

Running for First Time
======================

Make  sure you have generated a PGP key in your gpg keyring before running the client (you can use an existing one).

1) Execute axismundi.py
2) Use a web browser to access the client using address http://127.0.0.1:5000/
3) The first time the client is run you must select a PGP key to use as your identity,
[This initial set-up creates an encrypted database file (by default in the same directory as the
application) and a PGP encrypted file called secret which will go into ~/.dnmng/secret]
4) Login by selecting your PGP key in the drop-down box and supplying your PGP passphrase (you may want to use offline
mode for the first login if your SOCKS proxy is not tunning on 127.0.0.1:9050)

====================================

DO NOT LOSE THE 'secret' file OR YOUR PGP KEY. ANYTHING IN YOUR LOCAL DATABASE WILL BE LOST FOREVER.


Six Pack 2015
