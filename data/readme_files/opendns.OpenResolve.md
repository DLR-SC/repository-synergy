OpenResolve
==================================================
[![Build Status](https://travis-ci.org/opendns/OpenResolve.svg?branch=master)](https://travis-ci.org/opendns/OpenResolve) [![Coverage Status](https://img.shields.io/coveralls/opendns/OpenResolve.svg)](https://coveralls.io/r/opendns/OpenResolve)


##### Fall 2014 USF Intern Project at OpenDNS

OpenResolve aims to address three issues in the realm of domain name lookup:

1. DNS lookup typically requires command line tools like dig, or manual interaction with an HTML interface. Our API makes DNS resolution available as a web service for any application. 

2. DNS lookups are typically conducted over UDP, which offers no security regarding the data being transferred. Performing DNS resolution over HTTP and SSL ensures the data has not been altered. 

3. Most DNS resolution returns output in a human readable format, but isn’t easily accessible programmatically. By transferring data in a commonly consumed format, JSON, we make it convenient for even high-level applications to use the data returned from a resolver.


Environment Variables:
--------------------------------------------------

RESOLVERS - A comma-separated list of resolver IPs to use. Defaults to OpenDNS IPv4 servers if this environment variable is not passed.

    export RESOLVERS='208.67.222.222,208.67.220.220'

RESOLVER_ENV - Running environment [prod, dev]. Defaults to 'prod'. This sets the flask debug to mode to True when in dev.

    export RESOLVER_ENV=dev

CORS_ORIGIN - Respond with Access-Control-Allow-Origin headers. Use * to accept all. Defaults to not using CORS.

    export CORS_ORIGIN=*
    

Tests:
--------------------------------------------------

	nosetests --with-coverage --cover-erase --cover-package=resolverapi


