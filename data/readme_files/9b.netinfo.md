NetInfo
=======
NetInfo is a simple IP enrichment service to provide additional data related to an IP address. The primary utility of NetInfo is to serve as a API wrapper and management system for the PyASN and MaxMind GeoIP libraries. NetInfo will automatically seek and download new update files, ensuring the databases are always up-to-date. The local API queries the PyASN and GeoIP instance and returns back enrichment data for an IP address.

Getting Started
---------------
Grab the dependencies::

    $ apt-get install redis-server rabbitmq-server

Check out netinfo to `/opt/`::

    $ cd /opt && git clone https://github.com/9b/netinfo.git

Change directory to the `netinfo` working directory::

    $ cd netinfo/

Setup the virtualenv::

    $ virtualenv -p python3 venv3

Activate the virtualenv::

    $ source venv3/bin/activate

Install the requirements::

    $ (venv3) pip install -r requirements.txt

Install the services and start them. 

    See `Services README`_.
    
Or start the Celery Daemon::

    $ (venv3) /opt/netinfo/venv3/bin/celery worker -A worker.celery --loglevel=info -B
    
And start the server::

    $ (venv3) /opt/netinfo/venv3/bin/uwsgi --ini wsgi.ini

You can then access the API through http://localhost:7777 for more details.

.. _Services README: https://github.com/9b/netinfo/blob/master/service/README.rst

Sample Output
-------------
When calling http://localhost:7777/lookup?ip=74.96.192.82::

    {
      "as_name": "UUNET - MCI Communications Services, Inc. d/b/a Verizon Business, US",
      "as_num": 701,
      "city": "Vienna",
      "country_iso": "US",
      "country_name": "United States",
      "ip": "74.96.192.82",
      "ip_hex": "0x4a60c052",
      "ip_version": 4,
      "latitude": 38.8977,
      "longitude": -77.288,
      "network": "74.96.0.0/16",
      "network_broadcast": "74.96.255.255",
      "network_hostmask": "0.0.255.255",
      "network_netmask": "255.255.0.0",
      "network_size": 65536,
      "postal_code": "22181",
      "region_iso": "VA",
      "region_name": "Virginia"
    }

Unlike the standard PyASN library, NetInfo will add the AS name to the response, additional network data and the original IP address that was requested.

API Endpoints
-------------
The following endpoints are available within the NetInfo service.

**/lookup?ip=8.8.8.8**

Get back AS, network information and geolocation for an IP address.

**/network-addresses?cidr=8.8.8.0/24**

Get back all IP addresses as part of a network range.

**/prefixes?asn=15169**

Get back all prefixes advertised for a specific AS network.

**/as-name?asn=15169**

Get back the name of the AS network.

**/geolocation?ip=8.8.8.8**

Get back geolocation information for an IP address.
