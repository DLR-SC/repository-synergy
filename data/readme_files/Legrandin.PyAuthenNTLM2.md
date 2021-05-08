PyAuthenNTLM2 is an authentication module for Apache.

It validates a user by means of the NTLM protocol and
a separate Domain Controller (or Active Directory server).

Introduction
============

The specific use case of PyAuthenNTLM2 is the following:

 * Users have valid accounts in an existing Windows domain, and you want such
   credentials to be used for HTTP authentication.
 * Apache runs on a server that is not part of the Windows domain.
 * Some of the users cannot use Kerberos. For instance, they connect via a proxy
   or they use machines that are not part of the domain. However, their client
   supports NTLM (all browsers do nowadays).
 * Some of the users can only use Basic, not even NTLM (possibly because they
   don't use a browser).
 * **[EXPERIMENTAL]** *Only users that belong to certain groups are authorized.
   The groups are defined on the Active Directory server.*

PyAuthenNTLM2 allows clients to authenticate via two schemes: NTLM or Basic.

As for several other authorization modules, PyAuthenNTLM2 will pass the username
to the underlying CGI application or webservice via the *REMOTE_USER* variable.
The user name is the Windows logon identifier, without the domain part
(that is, ``jdoe`` and not ``DOMAIN\jdoe`` or ``John Doe``).

Security
--------

Although Kerberos (including its Microsoft variant "Integrated Windows
Authentication") is the best option in terms of security for HTTP
authentication, the venerable NTLM protocol is still a good compromise, much
better than the widespread Basic protocol and marginally better than Digest.
With Basic, anybody can pick up your password from the messages sent to the
server (unless you use TLS), whereas with Digest the web server needs local
access to the actual password. With NTLM, the webserver can relay every
authorization requests to the (Domain Controller or Active Directory server):
it never has to neither see nor store the real passwords.

A typical message flow is the following. First, the server (Apache)
refuses any request on a new connection: ::

 Client ----[GET]---> Apache
 Client <---[401]---- Apache , WWW-Authenticate: NTLM

The client crafts a first NTLM message to negotiate the authentication
parameters. Such message (Type 1) is relayed straight to the Domain Controller: ::

 Client ----[GET]---> Apache , Authorization: TlRMT... (Type 1 message)
                      Apache ----[Type 1]---> DC

The Domain Controller generates a random challenge, completes the negotiation,
and sends back the message. The message (Type 2) is relayed to the client: ::

                      Apache <---[Type 2]---- DC
 Client <---[401]---- Apache , WWW-Authenticate: NTLM TlRMT... (Type 2 message)

The client presents the popup dialog to the user to acquire the credentials.
The password is only used to encrypt the challenge. The resulting message
(Type 3) is relayed to the Domain Controller, which will communicate to the
server if the user is authentic or not: ::

 Client ----[GET]---> Apache , Authorization: TlRMT... (Type 3 message)
                      Apache ----[Type 3]---> DC
                      Apache <---[Result]---- DC
 Client <---[200]---- Apache

The password is never disclosed by the client. However, several versions of
NTLM exist. NTLMv1 is based on cryptography that by today standards is very
weak. That means that the password can be still brute forced from the
encrypted challenge. In order to avoid that, ensure that your clients
always use NTLMv2 `[1]`_.

PyAuthenNTLM2 handles equally well all the various NTLM variants (such as
NTLMv2 Session, and NTLMv2).

.. _`[1]`: http://support.microsoft.com/kb/239869

Requirements
============

* Mod-python `[2]`_
* Python 2.x
* Apache 2.x
* PyCrypto 2.x (not required, but Basic auth will not be supported without it)

.. _`[2]`: http://www.modpython.org

Tests were carried out with:

- a server with mod-python 3.3.1, Apache 2.2, and Python 2.6. 
- clients with Internet Explorer 7/8, Firefox 7.0, and Chrome.
- Windows 2003 Domain Controller and Active Directory server

Installation
============
::

 python setup.py install -f

Usage
=====
Usage is best shown by an example of Apache configuration: ::

 <Directory /var/lib/some_directory>

    AuthType NTLM
    AuthName WDOMAIN
    require valid-user

    PythonAuthenHandler pyntlm
    PythonOption Domain WDOMAIN
    PythonOption PDC 192.1.2.45
    PythonOption BDC 192.1.2.46

    # Bypass authentication for local clients.
    # Comment these lines if they should authenticate too.
    Order deny,allow
    Deny  from all
    Allow from 127.0.0.1
    Satify any

 </Directory>

All non-local clients trying to access a URI mapped under the directory
``/var/lib/some_directory`` will be asked for credentials valid in the Windows
Domain ``WDOMAIN``. The user name to enter need to be in the format:
``wdomain\useridentifier`` (for instance ``windom\jbrown``).

Local clients (that is, those connecting from ``127.0.0.1``) will not be presented
with any request for authentication.

The following options exist:

=====================================  ======
Apache option                          Description
=====================================  ======
AuthType NTLM                          Always specify it like this.  
Require valid-user                     Always specify it like this.
Require user XYZ,WTY                   | Grants access only to users named XYZ or WTY.
                                       | Multiple "Require user" option lines can be specified.
AuthName *domain*                      Replace *domain* with the domain name to present to
                                       users in the pop-up dialog.
PythonAuthenHandler *pyntlm|path*      Use simply *pyntlm*, unless the actual `pyntlm.py` script
                                       is not in the search path for python for the mod-python
                                       interpreter. In that case, specify the complete file
                                       name (with absolute path) to the script.
PythonOption Domain *domain*           Replace *domain* with the Windows domain name (uppercase).
PythonOption PDC *pdc*                 Replace *pdc* with the address of the Primary
                                       Domain Controller (either IP or DNS name).
PythonOption BDC *bdc*                 Replace *bdc* with the address of the Backup
                                       Domain Controller (either IP or DNS name).
                                       This entry is optional.
PythonOption NameFmt SAM|LogOn         Set REMOTE_USER to the user name only (SAM) or to the
                                       legacy Logon format (domain\username).
                                       This entry is optional. SAM is the default.
=====================================  ======

Apache needs to be configured to send keep alives (directive ``KeepAlive On``).

For SSL-protected sites, comment out the statement: ::

    SetEnvIf User-Agent ".*MSIE.*" \
             nokeepalive ssl-unclean-shutdown \
             downgrade-1.0 force-response-1.0

from the default Apache virtual host, or Internet Explorer will not manage to
make use of NTLM.

Experimental
------------
The [pdc]/[bdc] settings may also refer to an Active Directory server.
The syntax becomes slightly more complex:

    ldap://server[/baseDN]

where ``server`` is the IP or DNS name of the Active Directory server, and the
optional ``baseDN`` is the base Distinguished Name for the queries (only needed
for authorization, see below). For instance:

    ldap://10.12.13.1/DC=nasa,DC=gov

or equivalently (but more in compliance to RFC4516):

    ldap://10.12.13.1/DC%3Dnasa%2CDC%3Dgov

When using an Active Directory server, it is also possible to check if the
user is authorized to access page. More precisely, it is possible to grant
access only if the user is member of one group.

The option ``Require group`` can be used to pass the comma-separated list of groups
the user must belong to. The group identifier is the logon name, that is,
the ``sAMAccountName`` attribute in Active Directory.

The check is performed *iteratively*. In other words, the check is successful
if the user belongs to a group with the given name, or to a sub-group (of
any order, up the hierarchy) who belongs to the sought group.

For instance, if you specified: ::

 <Directory /var/lib/some_directory>
    [ ... ]
    Require group Administrators,Power Users
    [ ... ]
 </Directory>

Only users that belong to ``Administrators`` or ``Power Users`` will be granted access.
If the user belonged to a sub-group of ``Power Users`` called
``Super Power Users``, they would pass the check too.
A user that does not belong to any of such groups is denied access, even if
its credentials were correct, unless its name is included in a ``Require user``
option.

Caching
-------

NTLM is a protocol that authenticates **TCP connections**, not the individual
request like Basic or Digest.

PyAuthenNTLM2 does not cache successful autentications.
Every time a new connection is established, you will see a query
to the Domain Controller or Active Directory from Apache. Browsers will
typically open several connections in parallel. Additionally, some browsers
may also trigger re-autentication within an established connection (e.g. Internet
Explorer for POST requests).

However, at the client side, browsers will do cache NTLM credentials, which
won't be asked again to ther user after the first time (which is the whole
point of Single Sign On!).

PyAuthenNTLM2 will cache positive group membership for 3 hours. That means that
if you remove a user from a group, such user will still be able to access
for up to 3 hours, unless you restart Apache. On the other hand, if you **add**
the user to a group, access should be granted immediately.

Logging
=======

All logs will show up in the Apache log file.

Troubleshooting
===============

Check list:

* Restart Apache each time you modify its configuration.
* Ensure that ``KeepAlive`` is ``On``.
* Verify with various browser brands and versions, not just with one.
* If use SSL and cannot access using Internet Explorer but other browsers work,
  ensure that the ``User-Agent MSIE`` setting (see Usage above) is commented out
  in your site configuration.
* Increase the level of verbosity for the Apache log up to ``Info``. Note that 
  the LogLevel may be specified in multiple places in the Apache configuration.
  Ensure you are not setting the log level too high in the directory hierarchy.
* Ensure that mod-python is installed and activated. In the log file you should
  see messages like this: ::

   [notice] mod_python: Creating 8 session mutexes based on 150 max processes and 0 max threads.

* Ensure that mod-python can find pyntlm.py. You should be able to see the
  following line for each a request, if the log level is set to ``Info``. ::

   [info] [client 127.0.0.1] PYNTLM: Handling connection 0x0 from address 127.0.0.1 for GET URI /mysite/request

* If you are using group authorization, try without it, so that all users with
  a valid account can access the pages.
* Ensure that the authentication code is compatible with your Domain Controller,
  at least if you use a DC. Use the ntlm_client.py utility with the same
  settings from the Apache configuration: ::

   python PyAuthenNTLM2/ntlm_client.py -u johndoe -p xxxxx -d DOMAINX -a 10.11.12.13 

  If you use an Active Directory server: ::

   python PyAuthenNTLM2/ntlm_client.py -u johndoe -p xxxxx -d DOMAINX -a ldap://10.11.12.13 

  You should see the message: ::

   User DOMAINX\johndoe was authenticated.

* Ensure that the browser is not using a configuration incompatible with
  the module. Use the http_client.py utility with the same settings
  from the Apache configuration. In case of NTLM autentication: ::

   python http_client.py -s johndoe -p xxxxx -d DOMAINX http://apachesite/path/to/page

  And in case of Basic authentication: ::

   python http_client.py -s johndoe -p xxxxx http://apachesite/path/to/page

  In either case you should see the message: ::

   OK.

* Ensure you are not using group authorization check with a Domain Controller;
  that is not currently supported. It only works with an Active Directory server.
* If you are using group authorization check with an ActiveDirectory server,
  ensure that the base DN is correct in the Apache configuration file. See `[3]`_.
* If you are using group authorization check with an ActiveDirectory server,
  check if LDAP signing is required in the server. That is not currently
  supported by this module.
* Ensure that the group authorization code is compatible with your Active
  Directory server. Use the ntlm_client.py utility with the same settings
  from the Apache configuration: ::

   python PyAuthenNTLM2/ntlm_client.py -u johndoe -p xxxxx -d DOMAINX -g Administrators -a ldap://10.11.12.13/DC=nasa,DC=gov

  You should see both 2 messages: ::

   User DOMAINX\johndoe was authenticated.
   User belongs to at least one group.

* If you have a problem of membership with a specific user you don't have the password
  for, you can explicit check what ntlm_client finds for that user, while authenticating
  with another accunt: ::

   python PyAuthenNTLM2/ntlm_client.py -u otheraccount -p xxxxx -d DOMAINX -g Administrators -a ldap://10.11.12.13/DC=nasa,DC=gov -m johndoe -v

  You should see plenty of messages with the various DNs of the groups the user ``johndoe``
  is found to be member of.

.. _`[3]`: http://roadzy.blogspot.com/2011/02/finding-your-base-dn-in-active.html

Thanks
======

| Microsoft for the large amount of technical specifications about NTLM and
  SMB it disclosed `[4]`_ . See also `[5]`_.
| Eric Glass for his long article about NTLM `[6]`_ .
  In several ways, it is more complete and precise than `[4]`_ .
| Gerald Ritcher and Shannon Eric Peevey for AuthenNTLM `[7]`_ , which
  inspired this module.

.. _`[4]`: http://msdn.microsoft.com/en-us/library/gg258393%28v=PROT.13%29.aspx
.. _`[5]`: http://technet.microsoft.com/en-us/magazine/2006.08.securitywatch.aspx
.. _`[6]`: http://davenport.sourceforge.net/ntlm.html
.. _`[7]`: http://search.cpan.org/~speeves/Apache2-AuthenNTLM-0.02/AuthenNTLM.pm

Contacts
========

Send an email to Legrandin <helderijs@gmail.com> or drop a
message at https://github.com/Legrandin/PyAuthenNTLM2.
