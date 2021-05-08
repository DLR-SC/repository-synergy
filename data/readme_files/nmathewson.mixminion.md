======================================================================
This is Mixminion version 0.0.8alpha3.

CONTENTS:
        I.    Overview
        II.   What's new in this version
        III.  How to upgrade
        IV.   How to install
        V.    How to send messages
        VI.   How to run a server
        VII.  How to report bugs and suggestions
        VIII. Future interoperability
        IX.   How to contribute

I. OVERVIEW
===========

Mixminion is the standard implementation of the Type III anonymous remailer
protocol, which lets you send very anonymous email.  This best-of-breed
remailer uses conservative design approaches to provide security against most
known attacks.  We chose a simple, extensible design so that we can provide a
robust core system and then experiment with new research features such as
dummy policies, directory servers, and reputation systems.

You can find the latest information at http://mixminion.net/, or on the
mailing list, archived at http://archives.seul.org/mixminion/dev/.  Please
consider subscribing, especially if you're going to run a node.

This is a testing alpha release.  You will probably only want to use it if
you are technically inclined, curious, and interested in helping the
Mixminion development effort.

WARNING!  Do NOT use this release if you require strong anonymity.  It has
known deficiencies, including some that make it possible for an adversary
to trace your message through the system.

II. WHAT'S NEW IN THIS VERSION?
===============================

NEW SINCE MIXMINION 0.0.7.1:
   - License changed from LGPL to the so-called "MIT" license. This has
     been planned for ages; see
       http://archives.seul.org/mixminion/dev/May-2004/msg00000.html
   - Numerous bugfixes:
     - Implement DESTDIR correctly.
     - Do not crash when run with python 2.4
     - Bump preferred openssl version to 0.9.8a
     - Work when umask setting is bizarre (0077, 0000, etc.)
     - Make -P and mbox work correctly together.
     - Catch over-long paths.
     - Tolerate missing /dev/null
     - Solve crash on mixminion clean-queue
     - Do not exit on a spurious protocol string from another MMTP host.
     - Do not use stdio to read /dev/urandom: This wastes entropy.
   - Security improvements
     - Regenerate SSL certificates more frequently.
     - Servers schedule and retry delivery on a per-address basis, not a
       per-message basis.
   - Drop support for pre-0.0.6 servers: Servers are now located by
     hostname.
   - Add a "count-packets" command to tell how many packets will be needed
     to send a message.  Some integrators need this.
   - Add a "SendmailCommand" option for invoking an external program to send
     email rather than simply connecting to an SMTP server.
   - Write much of ClientAPI, so Mixminion is easier to embed -- having this
     in a real release should make the Nymbaron team happy.
   - Experimental pinger code, using pysqlite as a data store and
     implementing the "Echolot" remailer reliability algorithm.
     More work is needed.
   - Partially implemented code for distributed coordinated voting directory
     servers.  Client side and data formats are done; glue remains.
     - Recommended versions are no longer hard-coded.
     - Refactor how we learn about servers and generate paths.
   - Split out option-parsing logic to make option lists more consistent.
   - Suppress prompt when reading messages from non-TTY fds.
   - Implement --status-fd option to dump info to would-be integrators.
   - Better errors on expired certs

STILL NOT IN THIS VERSION:
   - IP-based restrictions don't work.
   - No support for distributed directories.
   - Other stuff too numerous to mention; see TODO.

III. HOW TO UPGRADE FROM MIXMINION 0.0.7
========================================

First, follow the installation instructions from section IV to install the
new version of the software.

If you aren't running a server, you are done.

IV. HOW TO INSTALL MIXMINION
============================

The quick version: For Unix-clones, Mac OS X, or Windows with Cygwin
---------------------------------------------------------------------
  <download and unpack http://www.mixminion.net/dist/Mixminion-0.0.8alpha2.tar.gz>

  % cd Mixminion-0.0.8alpha2
  % make download-openssl
  % make build-openssl
  % make
  % make test
 EITHER:
    % su
    Password:
    # make install
 OR:
    % make install PREFIX=~

The verbose version: For Unix-clones, Max OS X, or Windows with Cygwin
-----------------------------------------------------------------------

  1) You must have Python version 2.0 or later installed on your system.  The
     binary may be called "python", "python2", "python2.X", or something else.
     If you don't have Python >=v2.0, go install it.  You can find source and
     binary distributions at http://www.python.org/.

  2) If you have OpenSSL version 0.9.7beta3 or later, go to step 5.
     Otherwise, continue.

  3) Run "make download-openssl".

  4) Run "make build-openssl".  If this step fails, OpenSSL didn't build
     correctly on your system.  Go read contrib/openssl/INSTALL, and make
     OpenSSL build.

  5) Run "make".  If you don't get any error messages, go to step 6.

     If you have OpenSSL 0.9.7 installed, but the build script doesn't find
     it, you can force it to look in a particular location (say, "/home/ssl")
     with:
            make OPENSSL_PREFIX=/home/ssl
     This will make the scripts look for headers in $OPENSSL_PREFIX/include
     and libraries in $OPENSSL_PREFIX/lib.

     If the scripts *still* can't find OpenSSL 0.9.7, you can override the
     compile and link options directly, like this:
            make OPENSSL_CFLAGS='-I/home/ssl/include' \
                 OPENSSL_LDFLAGS='-L/home/ssl/libraries -lssl097 -lcrypto097'

     If your C compiler knows where to find OpenSSL on its own, but the
     build script doesn't trust it, you can disable searching like this:
            make SKIP_OPENSSL_SEARCH=y

     If you get any other errors, please report them to <nickm@freehaven.net>.

  6) Run "make test" to run Mixminion's unit tests.  If you get any errors,
     please report them to <nickm@freehaven.net>.

  7) Run "make install" to install Mixminion.  You may need to be root to
     execute this command.  By default, Mixminion will install itself relative
     to your python distribution.  If you want to install somewhere else (e.g.
     /home/miniond/), run "make install PREFIX=/home/miniond".

     A script called "mixminion" will be created in the 'bin' directory
     relative to your prefix, or in the same directory as the python
     executable if no prefix is provided.  To make sure that everything was
     installed correctly, you can run "mixminion unittests".

The very easy version: For Windows
----------------------------------

   First, make sure that you're running Win98 or later.

   Download 'Mixminion-0.0.8alpha2.win32.zip", and unpack it anywhere you like.
   It will create a directory named 'mixminion'.

   Use mixminion.exe from that directory as your command-line client.

The slightly harder version: For Windows with Python 2.3
--------------------------------------------------------

   First, make sure that you have the latest official release of Python 2.3
   installed.  As of 5 Dec 2003, this is 2.3.2.

   Download and run "Mixminion-0.0.8alpha2.win32-py2.3.exe".  It will unpack
   its files into your Python directory.

   The script to invoke Mixminion will be stored in the 'Scripts'
   subdirectory of your Python directory.  Whenever the instructions below
   tell you to run 'mixminion', run "python Scripts\mixminion.py' instead,
   from the python directory.  (Future releases may include a batch file
   to make this easier, especially if somebody else contributes one.)

   Be sure to read the "NOTE TO ALL WINDOWS USERS" above.

The verbose version: How to build on Windows
--------------------------------------------

   (I have only tried this with Visual Studio 6 and Python 2.3.  Let me know
   if you succeed with any other compilers.  Also, let me know if these
   instructions don't work.)

   First, install Python version 2.0 or later, either from the official
   binary or by building it yourself.  When you build Mixminion, you will
   need to use the same compiler as was used to build Python: the standard
   distribution uses Visual Studio 6.

   Second, download an unpack the Mixminion source distribution.

   Third, get a compiled copy of OpenSSL version 0.9.7 or later (as of 2 Dec
   2005, the latest stable version is 0.9.8a).  You can either compile it
   yourself, or use a set of precompiled binaries (such as are available from
   XXXX).  Place the compiled libraries under the "contrib" directory in the
   Mixminion source directory, so that the include files are in
   "contrib\OpenSSL\include" and the libraries are in
   "contrib\OpenSSL\lib\VC".

   Now you are ready to build Mixminion!  Make sure that python.exe is on
   your path, then run:

         python setup.py build
         python setup.py run --subcommand=unittests

   If all the unit tests pass, you can either install the software locally
   and use it as described in 'the slightly harder version' above:

         python setup.py install

   Or you can make a windows installer for users with Python:

         python setup.py bdist_wininst

   Or, if you have the py2exe package installed, you can make a standalone
   binary that people can run without installing Python:

         python setup.py py2exe

   Finally, be sure to read the "NOTE TO ALL WINDOWS USERS" above.

V. HOW TO SEND MESSAGES VIA MIXMINION
=====================================

Just run one of the following command lines:

        mixminion send -t <email address> -i <filename to send>
    OR  mixminion send -t <email address>            (to read from stdin)
    OR  mixminion send -t <email address> -i -       (also reads from stdin)

For more options, see the manual page. (Type "man mixminion" on any Unix-like
computer, or see the latest version at http://mixminion.net/.)

VI. HOW TO RUN YOUR OWN MIXMINION SERVER
========================================

1) Create a copy of the "etc/mixminiond.conf" file from the
   mixminion distribution and place it where you like.  Mixminion will
   automatically look in ~/.mixminiond.conf, ~/etc/mixminiond.conf, and
   /etc/mixminiond.conf.  However, you can store it anywhere.

2) Edit mixminiond.conf to reflect your own system settings.

3) Run your server for the first time:

        "mixminiond start -f <path to mixminiond.conf>"

    (The -f flag and path are only necessary if you placed the
    configuration file somewhere other than ~/.mixminiond.conf,
    ~/etc/mixminiond.conf, or /etc/mixminiond.conf.)

5) To try out your server, clients will need a copy of your server
   descriptor, whose location is stored $SERVER_HOME/current-desc.

   For example, if your mixminiond.conf contains the following line:

           Homedir: /home/mixminion/spool

   Then if you read the contents of /home/mixminion/spool/current-desc,
   you will find a filename like:

           "/home/mixminion/spool/keys/key_0001/ServerDesc".

   This file is your current server descriptor.

   Mixminion supports a global directory of server descriptors.  Until you
   are listed in that directory, clients can import your ServerDesc file
   (if they have a copy) by hand by running:

           mixminion import-server <filename>

   They can also use your ServerDesc without importing it by using the
   filename as a part of their path:

           mixminion send -t <address> -P '<filename>,?,?'

6) When you're ready to advertise your server, edit 'mixminiond.conf' and set
   the 'Publish' option to 'yes'.  When you restart your server, it will
   advertise itself to the central directory.

   The first time you do this, your server will not be inserted automatically;
   the directory server holds your server's information separately until I
   confirm it (to prevent pseudospoofing).  Once your server is listed, future
   updates will be get into the directory automatically.

   WARNING: We don't have statistics yet, so the system isn't robust in the
   presence of unreliable servers in the directory.  Please don't publish a
   server if you don't think you can keep it up for a good while.

   {This step will be more automated in later versions.}

To shut down a server:
    mixminiond stop [-f configfile]

To make a server reload its configuration:
    mixminiond reload [-f configfile]

    (Right now, this just closes and re-opens the log files.)

Your server can be configured to keep track of the number of packets it
receives and other interesting statistics.  Ordinarily, it aggregates these
totals and flushes a report to disk at a configurable interval.  If you want
to see statistics in the _current_ interval, run:

    mixminiond stats [-f configfile]


VII. HOW TO REPORT BUGS AND SUGGEST NEW FEATURES
================================================

To report bugs, please use the Bugzilla pages at http://bugs.noreply.org.

For other correspondence, please email <nickm@freehaven.net>.

For help in debugging, please try to send a copy of:
        * What command you were running
        * The complete error you got, including stack trace (if any)

If your error occurred on a running server, please make a copy of your
log--it might be helpful.

VIII. FUTURE INTEROPERABILITY
=============================

Mixminion is not yet feature complete.  As the software moves closer to
official release, backwards-incompatible changes *WILL* be introduced.
Future versions of Mixminion, including future versions in the 0.x track, may
reject messages from older versions as additional security features are
added.

Furthermore, the present preview versions include necessary diagnostic
features that potentially compromise anonymity and would be inappropriate in
a production system; these features will be removed or disabled by 1.0.

IX. HOW TO CONTRIBUTE
=====================

Send patches to <nickm@freehaven.net>.  If you can, please submit unified
diffs against the latest version of the code in CVS.

Make sure to run 'make test' before you send in any patches, so you can see
whether your patch broke existing code.  (It's okay if you're not sure how to
fix the test, but please let me know when you send your patch.)
