Pyersinia: Network Attack Tool
==============================


Code | https://github.com/nottinghamprisateam/pyersinia
---- | ----------------------------------------------
Last version | 1.0.5
Issues | https://github.com/nottinghamprisateam/pyersinia/issues/
Python version | Python 2, Python 3


What's pyersinia?
-----------------

Pyersinia is a similar tool to Yersinia, but Pyersinia is implemented in Python using Scapy. The main objective is the realization of network attacks such as spoofing ARP, DHCP DoS , STP DoS among others. The community can add new attacks on the tool in a simple way, using plugins. This is because Pyersinia uses the STB (Security Tools Builder) framework.


What's new?
-----------

Adding new attacks on the tool is a simple task because we use the framework STB (Security Tool Builder). 
The new attacks are added by plugins. 


How to contribute to this project
---------------------------------
You can contribute for this project easily.
First you have to add your REQUIRED parameters into pyersinia.py file if they are not.
Second you have to add in the api file as a plugin your import attack.
At the end, you have to add your plugin in ./pyersinia_lib/libs/plugins folder. This plugin should have 2 functions at least:
- run_attack(config)
- run(your parameters)

In run function you will include your new attack.

![running](https://raw.githubusercontent.com/nottinghamprisateam/pyersinia/documentation/pyersinia_lib/doc/en/images/createPlugin.gif)


How to taste your plugins
-------------------------
If you need switch or router to taste your plugins, you will have to install gns3 to virtualize them.
- GNS3 Repository: https://github.com/GNS3/gns3-gui
- http://binarynature.blogspot.com.es/2015/11/install-configure-gns3-arch-linux.html
- https://community.gns3.com/community/connect/community-blog/blog/2015/11/11/setting-up-gns3-on-opensuse-leap


Installation
------------

Install pyersinia is so easy:

```
$ python -m pip install pyersinia
```

Or install from Pypi:

```
# pip install pyersinia
```


Quick start
-----------

You can display inline help writing:

```bash

> python pyersinia.py -h

#############################
####Pyersinia attack tool####
#############################

positional arguments:
  arp_spoof_TARGET
  arp_spoof_VICTIM

optional arguments:
  -h, --help              show this help message and exit
  -v, --verbosity         verbosity level
  -a ATTACK_TYPE          choose supported attack type
  -i IFACE                choose network interface
  -g GATEWAY              gateway ip for DHCP conf
  -s IPSERVER             DHCP ip server
  -n NETWORK              network address. Example: 192.168.1.0
  -m NETMASK              netmask. Example: 255.255.255.0
  --domain DOMAIN         domain name
  --sdomain SERVER_DOMAIN ip address of name server domain
                          

supported attacks:
        stp_root_role, dhcp_discover_dos, stp_bdpu_conf, dhcp_rogue, stp_tcn, arp_poison

examples:
        python pyersinia.py -a arp_spoof 127.0.0.1 127.0.0.1
        python pyersinia.py -a stp_root -i eth0


```

Licence
-------

This project is licensed as BSD license.


Author
------

Nottingham Prisa Team.


References
----------

- OMSTD (Open Methodology for Security Tool Developers): http://omstd.readthedocs.org
- STB (Security Tool Builder): https://github.com/abirtone/STB
- Yersinia: https://github.com/tomac/yersinia
