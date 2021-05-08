# GitNamed

GitNamed is a project that manage name server by git.

## Features

* A frame to manage your DNS server(s)
* Put all your DNS data into git, and you have a revision from which you can backup and restore easily
* It's easy to manage your DNS resource records, just edit and commit
* DNS manager needs no OS account on the DNS server, only a git account
* Using hooks to validate syntax of zone file when commting
* Using hooks to auto increcement serial of SOA when commting

## Overview

GitNamed is a project that manages your name server(s) by git. You can clone
the git repo to any workstation, edit zone file, commit and push the changes.
The data will be pushed to the master and slave name server on the fly.  

You don't need to touch name server any more, you have all your dat in a git repo with a history of your changes.  

If you need add a new zone, just create a new file in zones directory, zone file name should be the domain name.

```
vi zones/example.com
git add zones/example.com
git commit -m "add example.com"
```

Here is a example zone file:

```
$TTL 3600
@ 		IN	SOA	ns1.example.com. sysadm.example.com. (
			2012040812	; serial
			7200		; refresh
			1800		; retry
			1209600		; expire
			300 )		; minimum
		IN	NS	ns1.example.com.
		IN	NS	ns2.example.com.
		IN	A	61.160.235.206
$ORIGIN example.com.
ns1     172800    IN      A       61.160.235.206
ns2     172800    IN      A       61.160.235.203
www	IN	A   61.160.235.206
test	IN	A   61.160.235.200
*	IN	CNAME   example.com.
```

Any one whos has the access right of git repo can manage the name server now.


It's been tested on CentOS 6.2 and Debian 6.0.

If you find any problems, please contact me:

email: ppyy@pubyun.com  
weibo: http://weibo.com/refactor  
blog: http://www.pubyun.com/blog  
github: https://github.com/pubyun/gitnamed  


## Install Guide

### enviroment 

* install bind  on master and slave dns server

```
CentOS:
#yum -y install bind
Debian:
#aptitude -y install bind9
Mac OS X:
$brew install bind
```

### Setup master DNS server

* get source code

```
#git clone git://github.com/pubyun/gitnamed.git /home/named
#cd /home/named
```

* modify IP of domain name server in config file, and generate
key to transfer zone from master to slave:

```
#dnssec-keygen -a hmac-md5 -b 128 -n HOST master2slave
#vi script/settings.py
```

* runing setup file:

```
#./script/setup.py 
```

* start named

```
#service named start
```

### setup a private git Repo

I recommend gitolite:  
https://github.com/sitaramc/gitolite

* add a repo to it, here is part of conf/gitolite.conf:

```
repo    gitnamed
        RW     =   refactor
        R      =   gitnamed
```

NOTE:

please use the private key just generated in .ssh/id_rsa.pub for gitolite private key.

your private repo url is something like:

    ssh://git@git.pubyun.org/gitnamed.git

* push code to your private repo:

```
#su - named
$git remote add hub ssh://git@git.pubyun.org/gitnamed.git
$git push hub master
```

now you can test git pull:

```
#su - named
$git pull hub master
Already up-to-date.
```

### Setup slave DNS server

* copy code 

use a tool like rsync to copy /home/named/ to slave dns server, it must be same directory
as master dns.

* runing setup file:

```
#./script/setup.py slave
```

* start named

```
#service named start
```

### enable sync master to slave

* setup authorized_keys on all your slave dns

```
#su - named
$vi .ssh/authorized_keys 

# enable push from master name server
from="61.160.235.206",no-port-forwarding,no-X11-forwarding,no-agent-forwarding,no-pty ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEApclazU9YfjfahDYT2692PSWYvjTOoFMTfgyTRpN/c/bq+GNPrC9hBunpVrhHyQ439t3Zj4VIEweY4AOTRstf94+IRp7BvYC8etb4x+M7oPbsa0JQGnfFIYrzpo7e2+t3+i1VfRgO4OtqrQTwuB45a+8zL8uHV6rK1vbDNUKdfiO7NRmCQoelhWgREUJkhYn00NCQyUUhcBB+MtP4mk4vHHKT2ZdAU/DeNL5cKbet90t871enIrfOMxkIRiCRA5SLJVQp9vWlmfo2Da79DVjWohKIrngF6ydJ7zJd3Izw0bVt7ZoawvTfQhuIPdAd6bJ95kOYzoJbFjin0wY8ZF6Qkw== 
```

run syndns.py script on master dns server to test

```
#su - named
$ /home/named/script/syndns.py 
Already up-to-date.
server reload successful
reloading 61.160.235.203
named.conf.slave                                                                                                                               100%  150     0.2KB/s   00:00    
server reload successful
```

### enable push from git to master

* setup authorized_keys on all master dns

```
#su - named
$vi .ssh/authorized_keys 
# enable push from git server
from="61.160.235.208",no-port-forwarding,no-X11-forwarding,no-agent-forwarding,no-pty,command="/home/named/script/syndns.py"  ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEApclazU9YfjfahDYT2692PSWYvjTOoFMTfgyTRpN/c/bq+GNPrC9hBunpVrhHyQ439t3Zj4VIEweY4AOTRstf94+IRp7BvYC8etb4x+M7oPbsa0JQGnfFIYrzpo7e2+t3+i1VfRgO4OtqrQTwuB45a+8zL8uHV6rK1vbDNUKdfiO7NRmCQoelhWgREUJkhYn00NCQyUUhcBB+MtP4mk4vHHKT2ZdAU/DeNL5cKbet90t871enIrfOMxkIRiCRA5SLJVQp9vWlmfo2Da79DVjWohKIrngF6ydJ7zJd3Izw0bVt7ZoawvTfQhuIPdAd6bJ95kOYzoJbFjin0wY8ZF6Qkw== 
```

* test pushing data to master:

on git server, you can trigger the script on master dns server:

```
$/usr/bin/ssh -i /home/git/.ssh/gitnamed named@ns1.pubyun.org sleep 1
Already up-to-date.
server reload successful
server reload successful
```

add script to hooks:

```
$vi  ~git/repositories/gitnamed.git/hooks/post-receive
/usr/bin/ssh -i /home/git/.ssh/gitnamed named@ns1.pubyun.org sleep 1
```

### add pre-commit hook to check zone file and auto increment serial

ln -s ../../script/check.sh .git/hooks/pre-commit 

you should put the serial of SOA in separated line and end it with
a comment "; serial":

```
$TTL 3600
@ 		IN	SOA	ns1.example.com. sysadm.example.com. (
			2012040812	; serial
			7200		; refresh
			1800		; retry
			1209600		; expire
			300 )		; minimum
```

### it works now

you can clone the git repo to any workstation, edit zone file, commit and push it.  
the data will push to the master and slave name server now.

