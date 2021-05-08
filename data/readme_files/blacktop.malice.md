![malice logo][malice-logo]

malice (Deprecated) evolution continues here - https://github.com/maliceio/malice
===================
[![Build Status][travis-badge]](https://travis-ci.org/blacktop/malice)
[![Documentation Status][docs-badge]](http://malice.readthedocs.org/en/mongo/)
[![Code Health][health-badge]](https://landscape.io/github/blacktop/malice/master)
[![Coverage Status][cov-badge]](https://coveralls.io/r/blacktop/malice)
[![License][license]](http://www.apache.org/licenses/LICENSE-2.0)
[![Support blacktop via Gittip][gittip-badge]](https://www.gittip.com/blacktop/)
[![Gitter Chat][gitter-badge]](https://gitter.im/blacktop/malice)

VirusTotal Wanna Be

Malice's mission is to be a free open source version of VirusTotal that anyone can use at any scale from an independent researcher to a fortune 500 company.

It is a python Flask web app/api that can operate in standalone mode or as a distributed scalable web app.

I have been told that every serious information security team designs there own version of this tool.  I want to build one so well designed and easy to use that everyone will stop recreating the wheel and instead use that time sharing intel and plugins with each other.

Requirements
------------
1. [VirtualBox](https://www.virtualbox.org/wiki/Downloads) or [VMWare](https://www.vmware.com/products/fusion/)
2. [Vagrant](http://www.vagrantup.com/downloads.html)

##### Installing Requirements on OSX
 - Install [Homebrew](http://brew.sh)
```bash
$ brew install cask
$ brew cask install virtualbox
$ brew cask install vagrant
```

Installation
------------
```bash
$ git clone https://github.com/blacktop/malice.git
$ cd malice
$ vagrant up

wait...

$ vagrant ssh
$ source ~/malice/venv/bin/activate
(venv)$ python /vagrant/manage.py createdb
```
#### Note: for additional notes please see the Malice [wiki](https://github.com/blacktop/malice/wiki)
Usage
-----
(While ssh'd into the VM via ```vagrant ssh```)
```bash
$ source ~/malice/venv/bin/activate
(venv)$ python /vagrant/manage.py runserver
```

Then browse to http://127.0.0.1:5000

### Home
![malice logo][index]
### Samples
![malice logo][samples]
### Analysis
![malice logo][analysis]

Documentation
-------------
Documentation is comming soon.

Testing
-------
To run the tests (in the project directory):
```bash
$ pip install nose coverage
$ nosetests --with-coverage --cover-html -s
```

Road Map
--------

1) Get Malice to a stable 1.0 release
 - Finalize plugin arch
 - Finish default db arch (MongoDB)
 - Finalize python-rq distributed tasking
 - Finish documentation
 - Finish test suite
 - Integrate in to CI framework
 - Docker-ize Malice

2) Windows based AV scanners

3) Auto deployable Cuckoo Sandbox cluster that integrates into Malice
 - Create Salt or Ansible provisioners to auto spin up hardened Cuckoo VMs.

4) Design a cluster dashboard and admin interface so sys admins can monitor Malice’s health and be alerted to issues.  

5) Malice will be designed in a way to auto scale under load (similar to the way that AWS does with Lambda etc)

6) Possible make Malice’s default OS be CoreOS so that I can update the OS and all it’s plugins at the same time without interrupting processing allowing for zero downtime updates.

7) Redesign Salt provisioners (maybe switch to Ansible?)
 - Make them work on any environment and use the templates to make it easy for users to enter their subscriptions API keys and AV licenses etc at installation.

8) Redesign Web UI (maybe with ReactJS + Flex?)
 - I want to REALLY hipster it up and make it as performant as possible to MANY people can be using it at the same time without noticeable performance degradation (I will also be using load balancing and cacheing to achieve this)
 - As well as a full UI/UX revamp.

9) Redesign Distributed Task Engine using Docker and Orchestration framework (Mesos, Kubernetes or Swarm)
 - I want to use these new emerging technologies to make the whole internet seem as one computer to Malice.

10) Design a sharable IOC framework that works with Malice so that all Intel gained with Malice can easily be shared amongst users.
 - People hate sharing so I want to make it so easy to it will succeed.

11) Redesign plugin framework to user docker containers that have their own Github accounts to take advantage of their star system (similar to the way atom.io uses it)
 - I have always wanted the plugins to be containerized.  This will allow them to be easily integrated into Malice and allows for the idea of a Malice plugin market place where people could sell commercial plugins for Malice.
 - The plugins will also have built in test suites so that a non-functional or buggy plugin will never be mistakenly installed into Malice.

12) I have another repo 'parking space' for **Notorious** with is going to be the Intel Framework designed t be tightly integrated into Malice and will most likely be an ELK stake with some customized searching/hunting capabilities as well as alerting.  Essentially it will be VirusTotal Splunk.

13) Design a crowd sourced way to have a hosted server that community can use and have free access to all the data.  
 - Design the framework in a way so that anybody can host docker **workers** on their cloud or local machine to lend processing cycles to the Malice cluster.  This is like the bitcoin concept except for a web app, much care must be taken when having untrusted samples be analyzed on people’s machines (which might limited it to just sandboxed static analysis)  So instead of having to charge people for access to the data like how VirusTotal does, anyone that donate processing power to Malice get's full access to the private API.

14) Add volatile analysis by integrating into Volatility or Rekall to analyze memory dumps extracted from Cuckoo Sandboxes.

15) Add support for OSX analysis. Static, Dynamic and Volatile.

16) Add support for mobile (iOS, Android, Windows) analysis. Static, Dynamic and Volatile (if possible)

17) Add commenting and voting similar to the way that VirusTotal does it.

Contributing
------------
1. Fork it.
2. Create a branch (`git checkout -b my_malice`)
3. Commit your changes (`git commit -am "Added Something Cool"`)
4. Push to the branch (`git push origin my_malice`)
5. Open a [Pull Request](https://github.com/blacktop/malice/pulls)
6. Wait for me to figure out what the heck a pull request is...

<!-- Links -->
[malice-logo]: https://raw.githubusercontent.com/black-top/malice/master/app/static/img/logo/malice_logo.png
[travis-badge]: https://travis-ci.org/blacktop/malice.svg?branch=master
[docs-badge]: https://readthedocs.org/projects/malice/badge/?version=latest
[health-badge]: https://landscape.io/github/blacktop/malice/master/landscape.png
[cov-badge]: https://coveralls.io/repos/blacktop/malice/badge.svg?branch=master
[gittip-badge]: http://img.shields.io/gittip/blacktop.svg
[gitter-badge]: https://badges.gitter.im/blacktop/malice.png
[index]: https://raw.githubusercontent.com/blacktop/malice/master/docs/images/index.png
[samples]: https://raw.githubusercontent.com/blacktop/malice/master/docs/images/samples.png
[analysis]: https://raw.githubusercontent.com/blacktop/malice/master/docs/images/analysis.png
[license]: https://img.shields.io/badge/licence-Apache%202-blue.svg
[![Analytics](https://ga-beacon.appspot.com/UA-61764375-1/malice/readme?pixel)](https://github.com/igrigorik/ga-beacon)
