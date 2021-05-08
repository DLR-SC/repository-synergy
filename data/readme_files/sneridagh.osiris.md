Introduction
============

Osiris (/oʊˈsaɪərɨs/) is an Egyptian god, usually identified as the god of the
afterlife, the underworld and the dead. He is classically depicted as a green-
skinned man with a pharaoh's beard, partially mummy-wrapped at the legs, wearing
a distinctive crown with two large ostrich feathers at either side, and holding
a symbolic crook and flail. Osiris was the afterlife's judge, he weighed the
dead souls and compare them with the Feather of Truth. Those which weighed the
most were sent to Ammut (the soul devourer) and not heavy enough to Aaru (the
egyptian paradise).

Osiris is an oAuth 2.0 compliant server based on Pyramid. The current version
(1.0) it supports the `resource owner password credentials` authentication flow.
You can use your preferred authentication backend (LDAP, SQL, etc.) in order to
oAuth enable it with Osiris. You can also use your preferred backend storage as
Osiris uses a pluggable store factory to store the issued token information. The
current version includes the MongoDB one.


The `resource owner password credentials` flow
==============================================

This flow is not the most popular oAuth flow, but it's useful in case that we
want to oAuth enable an app or a set of apps in an scenario with an already
existing user backend. Using this flow you can use Osiris as a gateway between
your existing user store and oAuth enable it. Osiris will authenticate the user
credentials against your user store and if suceeds it will issue a oAuth token.
Then, an app can use it to impersonate the user's token to access an oAuth
enabled REST API, for example.

For that reason and out of the oAuth specification, Osiris features an
additional endpoint to allow remote applications and resource servers to check
previously issued tokens and users and validate it. This endpoint will respond
if the token is valid for the user specified and if the token is not expired or
revoked.

You can use Osiris as a standalone application or use it as a Pyramid plugin and
make your app Osiris enabled.


Setup
=====

This is the configuration to use it as a standalone Pyramid app, along with your
own one using Paste urlmap in your app .ini::

    [server:main]
    use = egg:Paste#http
    host = 0.0.0.0
    port = 80

    [composite:main]
    use = egg:Paste#urlmap
    / = YOURAPP
    /oauth2 = osiris

    [app:osiris]
    use = egg:osiris

    osiris.store = osiris.store.mongodb_store
    osiris.store.host = localhost
    osiris.store.port = 27017
    osiris.store.db = osiris
    osiris.store.collection = tokens
    osiris.tokenexpiry = 0

    osiris.whoconfig = %(here)s/who.ini
    osiris.ldap_enabled = false

    [app:YOURAPP]
    use = egg:YOURAPP
    full_stack = true
    static_files = true

You can also Osiris enable your own app, in your __init__.py::

    config.include(osiris)

and in the .ini::

    osiris.store = osiris.store.mongodb_store
    osiris.store.host = localhost
    osiris.store.port = 27017
    osiris.store.db = osiris
    osiris.store.collection = tokens
    osiris.tokenexpiry = 0

    osiris.whoconfig = %(here)s/who.ini
    osiris.ldap_enabled = false

Or use it standalone (see production.ini).


Options
=======

These are the .ini options available for Osiris:

osiris.store
    Currently only available ``osiris.store.mongodb_store``. Required.

osiris.store.host
    Defaults to 'localhost'. Optional.

osiris.store.port
    Defaults to '27017'. Optional.

osiris.store.db
    The name of the database. Defaults to 'osiris'. Optional.

osiris.store.collection
    The collection to store the tokens. Defaults to 'tokens'. Optional.

osiris.tokenexpiry
    The time in seconds that the token is valid. Defaults to 0 (unlimited). Optional.

osiris.whoconfig
    The pyramid_who (repoze.who) .ini with the configuration of the authentication backends. Required.


REST API for `resource owner password credentials` flow
=======================================================

Following the oAuth 2.0 authentication standard (draft 22), the `Resource owner
password credentials` flow must implement this web services and use these
parameters:

/token
    Method:
        POST

    Params:
        grant_type
            Required. Value must be set to password

        username
            Required. The resource owner username, encoded as UTF-8.

        password
            Required. The resource owner password, encoded as UTF-8.

        scope
            Optional. The scope of the access request.

    Content-Type:
        application/x-www-form-urlencoded

    Response:
        HTTP/1.1 200 OK
        Content-Type: application/json;charset=UTF-8
        Cache-Control: no-store
        Pragma: no-cache

        { "access_token":"Qwe1235rwersdgasdfghjkyuiyuihfgh",
        "token_type":"bearer",
        "expires_in":3600,
        "scope": "exampleScope" }

/checktoken
    Method:
        POST

    Params:
        access_token
            Required. Value of the token to be checked

        username
            Required. The resource owner username, encoded as UTF-8.

        scope
            Optional. The scope of the access request.

    Content-Type:
        application/x-www-form-urlencoded

    Response:
        If successful: HTTP/1.1 200 OK
        If not successful: HTTP/1.1 401 Unauthorized


Authentication backend
======================

You can choose between two authentication backend plugins: pyramid_ldap and
pyramid_who.

pyramid_ldap (for LDAP authentication backends)
-----------------------------------------------

pyramid_ldap is the defacto standard plugin when dealing with ldap in pyramid.

This is the configuration needed in the .ini to enable LDAP::

    osiris.ldap_enabled = true
    osiris.ldap.server = ldaps://your.ldap.uri
    osiris.ldap.userbind = cn=user.to.bind,ou=users,dc=my,dc=domain
    osiris.ldap.password = secret
    osiris.ldap.userbasedn = ou=users,dc=my,dc=domain
    osiris.ldap.userfilter = (cn=%+(login)s)
    osiris.ldap.userscope = SCOPE_ONELEVEL
    osiris.ldap.groupbasedn = ou=groups,dc=my,dc=domain
    osiris.ldap.groupfilter = (&(objectClass=groupOfNames)(member=%+(userdn)s))
    osiris.ldap.groupscope = SCOPE_SUBTREE
    osiris.ldap.groupcache = 600

Adjust them to match your LDAP configuration. For further information, see:
http://docs.pylonsproject.org/projects/pyramid_ldap/en/latest/

pyramid_who
-----------

pyramid_who is a plugin that provides a pluggable facility to connect with
several user backends (htpass, SQL, etc.) using repoze.who plugins.

In order to use it, you should not to enable ldap::

    osiris.ldap_enabled = false

and provide the path to your who.ini::

    osiris.whoconfig = %(here)s/who.ini

For more information see: http://docs.repoze.org/who/2.0/


To do
=====

Osiris features only one oAuth 2.0 authentication flow: the `Resource owner
password credentials` (http://tools.ietf.org/html/rfc6749#section-4.3). It's
ready to accomodate the remaining flows defined by oAuth 2.0. A similar case
happens with the available storage backends. The current version sports only the
MongoDB storage but Osiris support the use of a plugin storage model and can
accomodate more storage types.

Of course, any contribution is welcome. Please, feel free to contribute with
your own storage plugins and help implementing the remaining oAuth flows.


Credits
=======

Pluggable store factory inspired by Ben Bangert's Velruse
(https://github.com/bbangert/velruse). Borrowed error handling from pyramid-
oauth2 (http://code.google.com/p/pyramid-oauth2/) by Kevin Van Wilder et al.
