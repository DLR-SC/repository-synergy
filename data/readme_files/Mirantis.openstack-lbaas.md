This is the OpenStack LBaaS project.
* Project overview: https://docs.google.com/document/pub?id=1DRgQhZJ73EyzQ2KvzVQd7Li9YEL7fXWBp8reMdAEhiM
* Screencast: http://www.youtube.com/watch?v=NgAL-kfdbtE
* API draft: https://docs.google.com/document/pub?id=11WWy7MQN1RIK7XdvQtUwkC_EIrykEDproFy9Pekm3wI
* Roadmap: https://docs.google.com/document/pub?id=1yJZXI0WfpAZKhHaLQu7LaxGLrs4REmn0a5bYVbvsCTQ

# Getting started with LBaaS DevBox

LBaaS DevBox is Linux-based VM with pre-installed services to simplify development and testing.
It can be downloaded from https://docs.google.com/open?id=0B1mJ0eQoi7tEZmlYWHVyUjA3dlk

DevBox contents:
 * Ubuntu 12.04 Server 64-bit
 * LBaaS sources checked out at /home/developer/openstack-lbaas/
 * HAProxy service
 * Lighttpd service for back-end emulation
 * utils: git, curl, vim, mc

There are 2 users:
 * developer/swordfish for development purposes
 * user/swordfish for configuring haproxy service

## Get LBaaS sources

Log in as "developer". Then check-out new sources:
```bash
rm -rf openstack-lbaas
git clone https://github.com/Mirantis/openstack-lbaas.git
```

Source code layout:
 * balancer - LBaaS core  
    * api - API layer
    * common - common code and utils
    * core - LBaaS server core
    * db - DB layer
    * drivers - drivers for load balancers 
       * haproxy - driver for HAProxy
    * tests  
       * manual - manual tests for LBaaS API
       * unit - unit tests

## Initial Setup

### Make sure the following packeges are installed:
   gcc
   python-dev
   libsqlite3-dev

### Create virtualenv that required for executing code and tests
```bash
 cd openstack-lbaas
 ./run_tests -V -f
```
Note, virtualenv needs to be updated any time code dependencies are changed. Virtualenv is created in .venv folder
 
### Initialize database
```bash
 ./.venv/bin/python bin/balancer-api --dbsync
```
The database is located in balancer.sqlite

### Intergation with Keystone

Authorization in LBaaS is configured by setting pipeline in `balancer-api-paste.ini`:
```
pipeline = authtoken context apiv1app
```
This line makes Paste.deploy create a pipeline of wsgi filters (see http://pythonpaste.org/wsgifilter/) for request processing.
- authtoken (keystone wsgi filter), defined in ini-file authorizes user in keystone populating request with additional X-Auth- http headers containing various information about reuqest.
- context (ContextMiddleware class in lbaas) creates request context which later to be used in authorization decisions.
- apiv1app - LBaaS wsgi application

Default configuration:
```
pipeline = apiv1app
```
makes LBaaS work as if every request had admin privileges.

### Run and Test

#### Run LBaaS:
```bash
 ./.venv/bin/python ./bin/balancer-api --config-file etc/balancer-api-paste.ini --debug
```
By default the server is started on port 8181   

#### Add HA Proxy device to LBaaS database

Create file createDeviceHAProxy with the following content:

```json
{
 "name": "HAP-001",
 "type": "HAPROXY",
 "version": "1",
 "supports_ipv6": 0,
 "requires_vip_ip": 1,
 "ip": "192.168.19.245",
 "port": "22",
 "user": "user",
 "password": "swordfish",
 "capabilities":
 {
   "algorithms": ["RoundRobin"],
   "protocols": ["TCP","HTTP"]
 }
}
```

**Note:** ``ip`` needs to be changed to the address of the box where HAProxy is located.

Execute script:

```bash
./createDevice.sh HAProxy
```

If all is right, the information about newly created device will be returned:

```
{"device": {"name": "HAP-001", "has_acl": 1, "ip": "192.168.19.245", "requires_vip_ip": 1, "capabilities": {"algorithms": "RoundRobin"}, "id": "c1dfe0c69bff49d296fc0d613417efcf", "version": "1", "user": "user", "supports_ipv6": 0, "password": "swordfish", "type": "HAPROXY", "port": "22", "supports_vlan": 1}}
```

Write out value for device/id, it will be used later for creating load balancer

Check that device is added in DB
```bash
./listDevice.sh
```

#### Create load balancer

Create file createLBcommandHAProxy with the following content:

```json
{
    "device_id": "c1dfe0c69bff49d296fc0d613417efcf",
    "name": "testLB001",
    "protocol": "HTTP",
    "transport": "TCP",
    "algorithm": "RoundRobin",
    "virtualIps": [
        {
            "address": "0.0.0.0",
            "mask": "255.255.255.255",
            "type": "PUBLIC",
            "ipVersion": "IPv4",
            "port": "80",
            "ICMPreply": "True"
        }
    ],
    "nodes": [
        {
            "address": "127.0.0.1",
            "type": "host",
            "port": "8001",
            "weight": "1",
            "minCon": "100",
            "maxCon": "1000",
            "rateBandwidth": "12",
            "rateConnection": "1000",
            "status": "INSERVICE",
            "condition": "ENABLED"
        },
        {
            "address": "127.0.0.1",
            "type": "host",
            "port": "8002",
            "weight": "1",
            "minCon": "300",
            "maxCon": "400",
            "rateBandwidth": "12",
            "rateConnection": "1000",
            "status": "INSERVICE",
            "condition": "ENABLED"
        },
        {
            "address": "127.0.0.1",
            "type": "host",
            "port": "8003",
            "weight": "1",
            "minCon": "300",
            "maxCon": "400",
            "rateBandwidth": "12",
            "rateConnection": "1000",
            "status": "INSERVICE",
            "condition": "ENABLED"
        }
    ],
    "healthMonitor": [
        {
            "type": "ICMP",
            "delay": "15",
            "attemptsBeforeDeactivation": "6",
            "timeout": "20"
        },
        {
            "type": "HTTP",
            "delay": "30",
            "attemptsBeforeDeactivation": "5",
            "timeout": "30",
            "method": "GET",
            "path": "/",
            "expected": "200-204"
        }
    ]
}
```
Configuration above assumes there are three web applications running on the box with HAProxy on ports 8001, 8002, 8003.
Change node count or node addresses to whatever you actually have.

Execute script:

```bash
./createLB.sh HAProxy
```

This will deploy HAProxy configuration and restart HAProxy. 
Note that configuration is added to whatever configuration has been already deployed on the box.
In case of issues check the file /etc/haproxy/haproxy.cfg on the box with HAProxy

#### Check the load balancer

```bash
curl http://haproxy_ip:port/
```

HAProxy should return page content from backend nodes.

## Developers Documentation

Docs can be built by the following commands:

```bash
cd doc
./compile_docs.sh
```
To view docs, open `doc/html/index.html` in the browser.
