
                     | | | (_) |              
      _ __ ___  _   _| | |_ _| |_ _   _ _ __  
     | '_ ` _ \| | | | | __| | __| | | | '_ \ 
     | | | | | | |_| | | |_| | |_| |_| | | | |
     |_| |_| |_|\____|_|\__|_|\__|\____|_| |_|


multitun v0.10 -- 'Tunnel all the things!'


Updates
==============

* Windows client (Windows server is experimental)
* BSD/Mac can be servers, in addition to Linux
* Covert WebSocket VPN -- clients can see each other


Introduction
============

Tunnel everything over a harmless looking WebSocket!

Multitun tunnels IPv4 over a WebSocket (RFC 6455), allowing bulk tunneling
through one connection on, for example, port 80.  One use for this is to
bypass strict firewalls.  Firewalls that allow web and HTML5 are assumed
to allow WebSockets as well, and multitun traffic quietly slips
past systems that do things like deep-packet inspection to find
conventional tunnels (e.g. ssh tunnel over port 80).

Multiple users can access the server at a time, and can see each other
if you want (effectively creating a covert VPN over WebSockets.)  See
how in 'Examples' below.

Only users with valid passwords can use the tunnel.  Multitun may be used
in conjunction with other common tools to enable port forwarding and
masquerading (see the Examples section below), and thus route arbitrary or
all client traffic through the Multitun server.

Multitun provides a simple web server to serve HTML to connecting clients that
don't know about or aren't using the WebSocket tunnel.


Installation
============

* Designed with Python 2.7

* Linux version tested under Fedora/CentOS, Arch, Ubuntu, BlackArch, Kali

* Mac/BSD client tested under MacOS X Yosemite, FreeBSD 10

* Windows client tested under Windows 7 and Windows 8

* See the INSTALL file

* Change the configuration file permissions to keep the password from others

* Note: Uses AES, so be aware of export laws, etc.


Usage
=====

* Edit the configuration files on both the server and client sides

* The program must have permission to make a TUN interface (e.g.
  run as root)

* Run multitun -s to start the server, then run multitun without
  options to start the client

* Make sure on the server side that the listen port is allowed through
  the host and network firewalls

* Adjust the webdir parameter in multitun.conf to specify the directory
  containing HTML to serve browsers who access the server without WS.

* If connections keep dropping, try running ping in the background for
  keep-alive

* If you try to connect more than one client with the same TUN IP
  (as set in the configuration file), only the first one will connect

* Clients can interact on the WebSocket net (ping each other, etc.)

* If you have especially sensitive things to do, use reputable, time-tested
  crypto beneath multitun (e.g. run an ssh tunnel over multitun).


Configuration
=============

* Configuration is straightforward.  Here is an example multitun.conf:

    [all]  
    serv_addr = 192.168.2.1  
    serv_port = 80  
    ws_loc = mt  
    tun_nm = 255.255.255.0  
    tun_mtu = 1500  
    logfile = /var/log/multitun  

    [server]  
    tun_dev = tun1  
    tun_addr = 10.10.0.1  
    p2paddr = 10.10.0.2  
    webdir = ./html  
    users = {'10.10.0.2': 'pass1', '10.10.0.3': 'pass2', '10.10.0.4': 'pass3'}  

    [client]  
    tun_dev = tun0  
    tun_addr = 10.10.0.2  
    password = pass1  


Examples
========

* Simple usage, access ssh on your server using multitun:  
	server# multitun -s  
	client# multitun  
	client# ssh 10.10.0.1  


* Use Linux as a NAT gateway for your host behind the firewall:

  *Configure the server*

   * Include the following in your multitun server iptables configuration.
     In this config, eth0 is the server external interface, tun1 is the
     server multitun interface, and 10.10.0.0/255.255.255.0 is the multitun
     IP range.

    *nat  
    -A POSTROUTING -s 10.10.0.0/255.255.255.0 -o eth0 -j MASQUERADE  
    COMMIT  

    -A INPUT -s 10.10.0.0/255.255.255.0 -j ACCEPT  
    -A FORWARD -i tun1 -j ACCEPT  
    -A FORWARD -s 10.10.0.0/255.255.255.0 -j ACCEPT  
    -A FORWARD -p ALL -m state --state ESTABLISH,RELATED -j ACCEPT  

   * Enable IP forwarding:

   echo 1 > /proc/sys/net/ipv4/ip_forward

  *Configure the client*
   
  * Take care of routing:
	
    ip route add [server ext. ip] via [client gw ip] dev [client dev] proto static  
    ip route del default  
    ip route add default via [client multitun local ip] dev [client tun] proto static  

* You can man a covert VPN over WebSockets by doing this on the server:

    iptables -t nat -A POSTROUTING -s 10.10.0.0/24 -o tun0 -j MASQUERADE  
     (tun0 is the server TUN interface)


Bugs
====
