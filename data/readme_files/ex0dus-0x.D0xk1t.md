# doxbox

[![Build Status](https://travis-ci.org/ex0dus-0x/doxbox.svg)](https://travis-ci.org/ex0dus-0x/doxbox)

OSINT and active reconaissance built into a web application

## intro

doxbox is a web application for OSINT and active reconaissance. It leverages various security tools
and library APIs in order to conduct info-gathering and threat modeling. Built on top of [Flask](http://flask.pocoo.org/),
it is perfect for self-hosting an instance during auditing.

## install

doxbox currently utilizes Python 2.7.x due to various dependency clashes and depreciation.

__Docker__:

```
$ docker build -t doxbox .
$ docker run -d -p 5000:5000 doxbox
```

__Manual:__

```
$ git clone https://github.com/ex0dus-0x/doxbox && cd doxbox
$ # Initialize virtualenv if you wish
$ pip install -r requirements.txt
$ python run.py
```

### config

Open `config.py`. Here, you will see all the environmental variables that the application utilizes. Three important fields you __MUST__ be aware of if you plan to deploy to the web.

```
GOOGLEMAPS_API_KEY = "YOUR_API_KEY_HERE"
SECRET_KEY = 'SECRET_KEY_HERE'
```

`GOOGLEMAPS_API_KEY` denotes the Google Maps API Key. This is essential for the GeoIP module. You can obtain it [here](https://developers.google.com/maps/) and change the variable accordingly.

`SECRET_KEY` is the private key utilized by WTForm's CSRF protection feature. If deployed, change it to your liking.

## modules

#### Dox

Comprehensive info-gathering database for target(s). Using this data, the tester will be able to effectively understand their target, which is a critical point in the attacker's kill chain.

* Secure database support, with delete and export (as `.csv`) options

#### GeoIP

Collects geolocation information on public IP addresses, in order to gather data on physical location during the reconaissance stage of the killchain.

* Google Maps for accurate GeoIP visualization
* API endpoint support

#### DNS Enum

Collections DNS information in the form of metadata, whether it be an address from a WHOIS lookup, or nameservers.

## contribute

Send a pull request if you feel that anything should be changed, removed, optimized, etc. Issues are also great for reporting bugs.

## license

[mit](https://codemuch.tech/license.txt)
