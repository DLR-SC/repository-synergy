
WARNING
=======

This is pre-release software. It's only been testing by me on my personal
postfix server. Running this anywhere on a production machine might cost
you your job, although afterwards please do let me know how it failed you
so I can fix it.

openpgpkey-milter
-----------------

openpgpkey-milter is a sendmail/postfix milter service that will attempt
to automatically OpenPGP encrypt plaintext emails received by the MTA/MUA
before relaying the message further towards the recipient(s). These can be
messages received from the network, or generated locally.

Requirements
------------
Apart from requiring a milter compatible mail server (postfix or sendmail),
openpgpkey-milter requires:

* python-unbound / unbound-python (in all major distros)
* python-milter / python-pymilter (in all major distros)
* [python-gnupg](http://pythonhosted.org/python-gnupg/)
  (older versions might need a [patch](http://code.google.com/p/python-gnupg/issues/detail?id=94)
* gnupg, libmilter, etc which are dragged in dependancies by the above packages

Recommended
-----------

The [hash-slinger](http://people.redhat.com/pwouters/hash-slinger/)
package contains an "openpgpkey" command that allows you to generate and
verify your own OPENPGPKEY records.

How does it work
----------------

openpgpkey-milter detects when a message is not encrypted with gpg and
then checks all the recipients to see if they published the special
[OPENPGPKEY](http://tools.ietf.org/html/draft-ietf-dane-openpgpkey) DNS record.

Configuration of the milter service
-----------------------------------

To use openpgpkey-milter with postfix, add to `/etc/postfix/main.cf`

     smtpd_milters = inet:127.0.0.1:8890
     non_smtpd_milters = $smtpd_milters
     milter_default_action = tempfail
     milter_protocol = 2

If you run `opendkim`, ensure you add openpgpkey-milter **before** opendkim
or you'll break the opendkim signatures. For the fedora/rhel configuration
where opendkims uses port 8891, you can use the following:

     smtpd_milters = inet:127.0.0.1:8890, inet:127.0.0.1:8891
     non_smtpd_milters = $smtpd_milters
     milter_protocol = 2
     milter_default_action = accept

Mailing list and bug reports
----------------------------

There is no mailing list yet. Please send questions and bug reports
to paul@nohats.ca. However if you run openpgpkey-milter on your mail
server and it broke, you might be better of mailing me at the unsigned
domain paul@cypherpunks.ca.

