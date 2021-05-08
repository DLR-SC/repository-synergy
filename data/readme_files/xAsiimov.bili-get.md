# Encrypted-DNS
[![License](https://img.shields.io/github/license/Siujoeng-Lau/Encrypted-DNS.svg)](https://github.com/Siujoeng-Lau/Encrypted-DNS/blob/master/LICENSE)
[![Releases](https://img.shields.io/github/v/release/Siujoeng-Lau/Encrypted-DNS)](https://github.com/Siujoeng-Lau/Encrypted-DNS/releases)
[![Downloads](https://pepy.tech/badge/encrypted-dns)](https://pepy.tech/project/encrypted-dns)

Encrypted-DNS operates as a DNS server that forward DNS queries over UDP, TCP, TLS or HTTPS, thus preventing your device from DNS cache poisoning and censorship.
It could also cache DNS records to accelerate further queries, block specific client, and ignore particular domain names.

Languages: [English](https://github.com/Siujoeng-Lau/Encrypted-DNS/blob/master/README.md), [简体中文](https://github.com/Siujoeng-Lau/Encrypted-DNS/blob/master/README_zh.md).

### Usage

* Install [Python 3.7](https://www.python.org/downloads/).

* Install package via `pip`.

```
$ python3 -m pip install encrypted-dns
```

* Generate and edit config file.

```
$ sudo encrypted-dns
$ vim ~/.config/encrypted_dns/config.json
```

* Run Encrypted-DNS Resolver.

```
$ sudo encrypted-dns
```

* Test DNS Query.

```
Linux or MacOS:
$ dig @127.0.0.1 www.google.com

Windows:
$ nslookup www.google.com 127.0.0.1
```

* Change DNS Address to `127.0.0.1`.

### Configure

Encrypted-DNS will generate a JSON file within its directory.

#### Upstream DNS

The following JSON object is a typical Upstream DNS server.

Encrypted-DNS supports three protocols: `udp`, `tcp`, `tls`, and `https`. 

You may specify the ip address of DNS-over-HTTPS or DNS-over-TLS server to avoid DNS cache poisoning.

```
"upstream_dns": [
    {
        "protocol": "https",
        "address": "cloudflare-dns.com",
        "ip": "1.0.0.1",
        "port": 443,
        "weight": 0,
        "enable_http_proxy": False,
        "proxy_host": "localhost",
        "proxy_port": 8001
    },
    {
        "protocol": "tls",
        "address": "dns.google",
        "ip": "8.8.4.4",
        "port": 853,
        "weight": 100
    },
    {
        "protocol": "udp",
        "address": "9.9.9.9",
        "port": 53,
        "weight": 0
    },
    {
        "protocol": "tcp",
        "address": "8.8.4.4",
        "port": 53,
        "weight": 0
    }
}
```

If you add multiple upstream servers, each DNS query will be forwarded to a server based on random selection or weighted random selection.

#### Bootstrap DNS Address

Encrypted-DNS will send a UDP DNS query to the bootstrap DNS server to retrieve the ip address of DNS-over-HTTPS or DNS-over-TLS server unless you specify it.
```
"bootstrap_dns_address": {
    "address": "1.0.0.1",
    "port": 53
}
```

#### Client Blacklist

You may set the ip addresses of the clients which you want to ignore DNS queries sent by them.
```
"client_blacklist": [
    "1.0.0.1",
    "172.100.100.100"
]
```

#### DNS Bypass

You may specify a list of domain names which you don"t want to be forward to upstream DNS servers.

Queries will be sent to the bootstrap DNS server.

```
"dns_bypass": [
    "captive.apple.com",
    "connectivitycheck.gstatic.com",
    "detectportal.firefox.com",
    "msftconnecttest.com",
    "nmcheck.gnome.org",

    "pool.ntp.org",
    "time.apple.com",
    "time.asia.apple.com",
    "time.euro.apple.com",
    "time.nist.gov",
    "time.windows.com"
]
```

#### DNS Bypass China

If you set `dns_bypass_china` to `true`, all the queries related to domain names in China will be redirected to the bootstrap address, which could be set to a public DNS server located in China.

```
"dns_bypass_china": true
```

#### DNS Cache

If you set `enable_cache` to `true`, responses will be cached based on the TTL.

```
"enable_cache": true
```

#### Hosts

Manually set A or CNAME record for specific domain name.

```
"hosts": {
    "www.instagram.com": "31.13.82.174",
    "www.bbc.co.uk": "212.58.244.69"
}
```

#### Force SafeSearch

Enable SafeSearch Mode for Google, Bing, and Youtube to filter harmful content.

```
"force_safe_search": true
```

#### Block Ads

Block common advertisement domain names.

```
"block_ads": true
```
