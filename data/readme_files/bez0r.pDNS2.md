pDNS2
=====

pDNS2 project

pDNS2 is yet another implementation of a passive DNS tool working with Redis as the database. pDNS2 means ‘passive DNS version2’ and favors speed in query over other database features.
pDNS2 is based on Florian Weimer’s original dnslogger with improved features for speed and specialization for analyst.


REQUIREMENTS
------------

Redis http://redis.io/

Redis API https://github.com/andymccurdy/redis-py

wireshark full install http://www.wireshark.org/




GETTING STARTED
---------------

This version has two simple python scripts to support the collection of DNS traffic as pdns2_collect.py and the other to query as pdns2_query.py

1. Ensure wireshare’s share is working and can collect on the desired interface or read pcap files.
2. Run redis-server and listening on local port 6379
3. run pdns2_collect.py with -i for an interface or -p for a pcap file
4. Anytime the collection is working, try pdns2_query.py with the options available.

below are are simply using a wildcard with -d for any domain

Sample query
python pdns2_query.py -d *


``` 
  Domain                                   ips             first     date      rr    ttl   count   
  w2.eff.org                               69.50.232.52    20120524  20120524  CNAME 300   3        
  web5.eff.org                             69.50.232.52    20120524  20120524  A     300   3        
  slashdot.org                             216.34.181.45   20120524  20120524  A     2278  1        
  csi.gstatic.com                          74.125.143.120  20120524  20120524  A     300   1        
  ssl.gstatic.com                          74.125.229.175  20120524  20120524  A     244   1        
  xkcd.com                                 107.6.106.82    20120524  20120524  A     600   1        
  imgs.xkcd.com                            69.9.191.19     20120524  20120524  CNAME 418   1        
  www.xkcd.com                             107.6.106.82    20120524  20120524  CNAME 600   1        
  craphound.com                            204.11.50.137   20120524  20120524  A     861   1        
  www.youtube.com                          173.194.37.4    20120524  20120524  CNAME 81588 1        
```

pDNS2 commands
--------------

DOMAIN EXAMPLES

```
arguments:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
  -i IP, --ip IP
  -da DATE, --date DATE
  -ips IP_SNIFF, --ip_sniff IP_SNIFF
  -ttl TTL, --ttl TTL
  -rr RRECORD, --rrecord RRECORD
  -l LOCAL, --local LOCAL
  -ac ACOUNT, --acount ACOUNT
  -c COUNT, --count COUNT
  -ipf IP_FLUX, --ip_flux IP_FLUX
  -ipr IP_REVERSE, --ip_reverse IP_REVERSE


-d *example.com     seeks all domains that end with example.com
-i 1.1.1.1          ip address search
-ttl 0              use a number like 0 or 100 to get all the TTL of a specific value search is based on domain not IP
-ac  *example.com            return by query, counts of counts (usage), or 'hits' for the domains in order, *.google.com or *.com are examples 

-l               search entire database local resolved IP addresses that resolve to 127.0.0.1 etc. 
-ipf *.com       return a COUNT of domains in the IP space for each instance of a domain, use with ip_reverse
-ipr * seattletimes.com use with ip_flux, enumerate domains in the IP space

-ips 192.168.1.1'    search the domain space for a specific IP address, different then searching by IP 
-da 20130101          return all records by date

ADMINISTRATIVE
delete_key('Domain:*delete*') Dangerous command, deletes a key, must use the entire key such as Domain: or IP:
raw_record('Domain:xalrbngb-0.t.nessus.org') view the raw record properties (no wildcards) use full key name
pDNS2 tracks current state and last known, it is a snapshot of organization perception, not a log.

```

AUTHOR
------

pDNS is developed and maintained 
terraplex at gmail.com


Errata
------

This is the basic version, if interested in the more advanced versions or specialized versions that work with scapy, let me know.
