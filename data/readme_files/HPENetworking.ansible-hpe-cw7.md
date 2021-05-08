# Introduction

This project contains Ansible modules that can be used to automate HP Comware 7 switches.  The modules rely on NETCONF to communicate with the device for making configuration changes and getting operational data back such as LLDP neighbors, OS, serial number, uptime, and active interfaces on the device.

A byproduct of the Ansible modules was the creation of a Python library that is being used to simplify each module, but also streamline communication between each module and the NETCONF interface of each HP COM7 switch.  The library can be found [here](https://github.com/HPENetworking/pyhpecw7).  While the library is being used for Ansible modules, it can also be used to create standalone applications.

  * [Introduction](#introduction)
  * [Modules](#modules)
  * [Getting Started](#getting-started)
    * Hands-on Examples
  * [Requirements](#requirements)
  * [Detailed Docs](https://hp-ansible.readthedocs.io/en/latest/index.html)

# Modules

The list of Ansible modules that has been developed can be broken down into two types of modules: read-only modules and read-write modules.  The read-write modules, or those that can implement a change on the system, can further be broken down into feature-level and system-level modules.

The list of modules can be seen below while a more detailed summary of each module can be found [here.](module_docs/module_docs.md)

## Read-Only Modules

The following modules gather data from the switches.  They do NOT impact system or feature level configuration.

* comware_facts - gathers device facts (characteristics) such as hostname, operating system (OS), serial number, uptime, localtime, list of interfaces, and hardware platform.
* comware_neighbors - gathers neighbor information
* comware_ping - tests remote reachability to specific destinations from the switch

## Read-Write Modules

### System Modules

Several modules can be used to modify system level change on the HP Com7 devices.  They are listed here:

* comware_file_copy - copy file from local Ansible machine to remote switch
* comware_install_config - copy a valid config file for the desired switch model from local Ansible machine to remote switch and activates it to be the running configuration
* comware_install_os - copy OS (bin or ipe files) from local Ansible machine to switch, set image to load on next boot, and reboots switch
* comware_reboot - reboots switch
* comware_save - saves current config
* comware_clean_erase - factory defaults the switch (be careful!)

### Feature Modules

Several modules can be used to modify feature level configuration on the HP COM 7 devices.  They are listed here:

* comware_command - send raw CLI command(s) to the device
* comware_interface - manage physical interface characteristics
* comware_ipinterface - manage Layer 3 interface attributes
* comware_switchport - manage Layer 2 interface attributes
* comware_vlan - manage VLAN attributes
* comware_portchannel - manage portchannels (LAGGs) and members
* comware_irf_members - manages IRF membership creation
* comware_irf_ports - manages IRF port creation and removal
* comware_vrrp - manage VRRP vrid (group) configuration
* comware_vrrp_global - manage VRRP global load-balancing method
* comware_l2vpn_global - enable/disable L2VPN globally
* comware_vxlan - manages the VXLAN to VSI mapping and associated tunnels
* comware_vxlan_tunnel - manages VXLAN tunnel interfaces (pre-req to comware_vxlan)
* comware_vxlan_svc_instance - manages interface level service instance and maps appropriate VSI, i.e. (xconnect)

# Getting Started

Follow these steps to get started with Ansible.  A few of these steps assume you will be working on an Ubuntu host.  If you are using a MAC or another version of Linux, please check the official Ansible [documentation](https://docs.ansible.com/ansible/intro_installation.html#installation) for help on getting Ansible installed. Most of these steps beyond installation will be the same regardless of version of Linux being used.

## Update /etc/hosts file

This step isn't a requirement, but if you want to use hostnames for your switches within Ansible, it's recommended to either have them setup in DNS, or update the `/etc/hosts` file with the appropriate mapping of name to switch IP address (preferably the IP address on the mgmt interface).  For a standalone small lab or test bed, updating the `/etc/hosts` file is usually the quickest.

Here is an example of a hosts file updated with two HP COM7 devices.

```
127.0.0.1   localhost
127.0.1.1   devhost

10.1.100.1    hp1
10.1.100.2    hp2


# The following lines are desirable for IPv6 capable hosts
::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters

```

## Prepare Switch for Ansible

### Create User Account
If a user account already exists on the switch that can be used to login via SSH and make changes, there is no need to create a new account.

If there isn't an account already created, here is an example of how to create one:

```
#
local-user hp
 password simple hp123
 service-type ssh http https
 authorization-attribute user-role network-admin
#
line vty 0 15
 authentication-mode scheme
 user-role network-admin

```

### Enable SSH

```
ssh server enable
ssh user hp service-type all authentication-type password
```

### Enable NETCONF

```
netconf ssh server enable
```

### Enable SCP

This step is only required when using specific Ansible modules that copy files from the local Ansible control host to the HP switch.  Three of these modules include: `comware_install_config`, `comware_install_os`, and `comware_file_copy`.

```
scp server enable
```


## Install Ansible

While in a terminal session on your Linux machine, execute the following commands:

```
$ sudo apt-get install python-pip
$ sudo pip install markupsafe
$ sudo pip install ansible
```

## Install HP Comware 7 Python Library

While in a terminal session on your Linux machine, execute one of the following blocks of commands:

**Latest From Source**

```
$ git clone https://github.com/HPENetworking/pyhpecw7.git
$ cd pyhpecw7
$ sudo python setup.py install
```

**Latest Stable Release via PIP (not supported yet)**

```
$ sudo pip install pyhpecw7
```

## Verify Library is Installed Correctly

Enter a new terminal session and enter the Python interpreter.

```
$ python
```

Import the HPCOM7 device object.  

```python
>>> from pyhpecw7.comware import HPCOM7
```

Prepare the arguments required to connect to the device.  These include the hostname or IP address of the switch, username and password used to login to the switch (these need to be pre-configured on the switch), and an optional port number.  By default, it's 830.

This example assumes the hostname of the switch is `hp1`.

```python
>>> 
>>> args = dict(host='hp1', username='hp', password='hp123', port=830)
>>> 
>>> device = HPCOM7(**args)
>>> 
```

Since this library is using NETCONF, which is connection-oriented, verify that the device object (HPCOM7) is not yet connected to the switch.

```python
>>> device.connected
False
```

**Note:** ensure you can ping your switch and ensure NETCONF is enabled!!!!

Initiate a connection to the switch, i.e. open a NETCONF session and verify it is now connected to the switch.

```python
>>> device.open()
<ncclient.manager.Manager object at 0x7fb2a3a2aa50>
>>> 
>>> device.connected
True
>>> 
```

You have now successfully verified the library has been installed and can connect to the switch.

An optional step is to use one of the feature libraries to gather configuration data such as that of a VLAN. 

**Note:** VLAN 20 was pre-configured on switch for this example.

```python
>>> from pyhpecw7.features.vlan import Vlan
>>> 
>>> vlan = Vlan(device, '20')
>>> 
>>> 
>>> vlan.get_config()
{'name': 'DEMO_VLAN', 'vlanid': '20', 'descr': 'VLAN 0020'}

```

Finally, close the connection to the device.

```python
>>> device.close()
```

## Install HP Ansible Modules

First go back to your home directory.
```
$ cd
```

Perform a clone of this project.

```
$ git clone https://github.com/HPENetworking/ansible-hpe-cw7
```

Navigate to the new `hp-ansible` directory.

```
$ cd hp-ansible
```

## Start Automating your HP Network

### Ansible Introduction & Example Playbook 1

This section will cover a high level introduction to Ansible by reviewing the first example playbook located in the `hp-ansible` directory that was also downloaded when you cloned the github repo.

There are a few pre-built Ansible playbooks in the `hp-ansible` directory that can be examined and executed to learn how to use Ansible to automate your HP network.  This section will serve as an introduction to Ansible as well as how to start executing and writing your own playbooks.

##### Note:
All exercises below assume your shell is in the `hp-ansible/` directory. If this isn't the case, some exercises may not work. Likewise, if you wants to experiment with custom playbooks, they should reside in the `hp-ansible/` directory.

Open the file called `hp-vlans.yml`.  This is a playbook that is automating VLAN provisioning across HP switches.

The following is the contents of the file `hp-vlans.yml`

```
---

  - name: VLAN Automation with Ansible on HP Com7 Devices
    hosts: hp1
    gather_facts: no
    connection: local

    vars:
      username: hp
      password: hp123

    tasks:

      - name: ensure VLAN 10 exists
        comware_vlan: vlanid=10 name=VLAN10_WEB descr=LOCALSEGMENT username={{ username }} password={{ password }} hostname={{ inventory_hostname }}

      - name: ensure VLAN 20 exists
        comware_vlan: vlanid=20 name=VLAN20 state=present username={{ username }} password={{ password }} hostname={{ inventory_hostname }}

      - name: ensure VLAN 10 does not exist
        comware_vlan: vlanid=10 state=absent username={{ username }} password={{ password }} hostname={{ inventory_hostname }}
```

Here are a few important details regarding this file.

* This file is an Ansible playbook.
* All playbooks use YAML as their structured data format
* All YAML files begin with three dashes or hyphens, i.e. `---`
* The first section of the file has a few parameters that include `name`, `hosts`, `gather_facts`, and `connection`.  This signifies the start of a play within the playbook.  Note: there can be multiple plays within a single playbook, but this is only showing one play.  An overview of these four parameters are as follows:
  * `name`:  this is arbitrary and a text description that is displayed to the terminal when running the playbook
  * `hosts`: this signifies the host or group of hosts that the automation tasks will be executed against.  The host or group of hosts are defined in the Ansible inventory file (covered next)
  * `gather_facts: no` and `connection: local` are required here since these modules are not using the default Ansible connection mechanism to communicate with the switches, i.e. SSH.  These modules are using NETCONF.  It is also possible to set these values once for a given environment in the `ansible.cfg` file.

Before moving on with detailing the playbook, the Ansible inventory file is reviewed.  The name of this file is arbitrary, but the file in the `hp-ansible` directory is called `hosts`.  Here is the example file, which you could also see if you open it up in a text editor.

```
[all:vars]
username=hp
password=hp123

[switches]
hp1
hp2

```

The first block has variables that can be used by all devices within a playbook.  Some of the example and test playbooks are pulling the hostname and password from the inventory file while others have them defined within the playbook.  This is being done to show a few of the options available to the user when using Ansible.

The second block represents one group and two hosts.  For this example, the names of the hosts match what is in the `/etc/hosts` file.  If DNS wasn't setup at all, it is possible to enter IP addresses here.  Multiple groups can be configured in the inventory as can variables for each particular group or host.

**Note**: make sure to use your correct hostnames and IP addresses if you didn't use `hp1` and `hp2` within your `/etc/hosts` file.

By now, you should have a good understanding for the *start* of the playbook and play as outlined in `hp-vlans.yml`. The next step is to review the tasks as outlined in the play.  The `vars` section will be reviewed below.

Each task is meant to be easily interpreted.  Just like the start of the play uses `name`, so does each task (although it's not a requirement).  `name` is plain text that is displayed on the terminal as the task is being executed.  The tasks in this play all use the module called `comware_vlan`.  This is where the modules come into action.  Modules are called and sent in parameters as shown.  A few of these parameters for the vlan module include: `vlanid`, `name`, and `descr`.  It should be self explanatory on what these values are, but they are for configuring a VLAN with those respective attributes.  

The other parameters such as `hostname`, `username`, `password` are required for all comware Ansible modules.  As you can see, there are curly braces around the values being assigned to these parameters.  These signify that they are variables.  You should be able to see two variables that were declared before the tasks in the `vars` section.

They are `username` and `password` and you can see they are referenced as such `username={{ username }}`.  It just so happens in this example the parameter of the module has the same name as the variable. As stated above, variables like this could be declared in the inventory, within a playbook, and from external files (not covered here). 

The one special case here is `inventory_hostname`.  This is a built-in Ansible variable that references the hostname of the host from the Ansible inventory file.  Since the `hosts` is set to `hp1` for this play, `inventory_hostname` will be equal to `hp1`.  If, at the top of the playbook, we used `switches` as the hosts group being automated, `inventory_hostname` would be set to `hp1` on the first execution and `hp2` on the second execution of the task.

**Note:** it's not recommended to store to the credentials in a playbook like this.  This is being done for demo purposes.  A better approach would be to store them in the hosts file, variables file, hidden file, or use Ansible vault.

One more detail about this module:

* The VLAN module is idempotent as most of the modules are.  The VLAN module ensures the VLAN is in the proper state. This means if the VLAN is already in the desired state (created, name of the VLAN, etc.), no change is made to the device

It's about time you get to run this playbook.  

While in the current directory where the `hp-vlans.yml` is located, execute the following command:

```
$ ansible-playbook -i hosts hp-vlans.yml 
```

You will then see the following output:

```
PLAY [VLAN Automation with Ansible on HP Com7 Devices] ************************ 

TASK: [ensure VLAN 10 exists] ************************************************* 
changed: [hp1]

TASK: [ensure VLAN 20 exists] ************************************************* 
changed: [hp1]

TASK: [ensure VLAN 10 does not exist] ***************************************** 
changed: [hp1]

PLAY RECAP ******************************************************************** 
hp1                        : ok=3    changed=3    unreachable=0    failed=0   
```

Note: `-i` is used to reference the inventory file you want to use for the playbook.  There is no need to always use the `-i` flag.  Another option is to set the `ANSIBLE_HOSTS` environment variable.  It can be done like this: 

```
$ export ANSIBLE_HOSTS=hosts
```

Execute the same playbook again.  You will now see this output:

```
PLAY [VLAN Automation with Ansible on HP Com7 Devices] ************************ 

TASK: [ensure VLAN 10 exists] ************************************************* 
changed: [hp1]

TASK: [ensure VLAN 20 exists] ************************************************* 
ok: [hp1]

TASK: [ensure VLAN 10 does not exist] ***************************************** 
changed: [hp1]

PLAY RECAP ******************************************************************** 
hp1                        : ok=3    changed=2    unreachable=0    failed=0  
```

Notice how VLAN 10 was changed again.  This is because we removed it in our last task with state=absent and re-added it again in the first task of the second execution.  Since we were still ensuring VLAN 20 exists on the switch and it already does, there was NO change to the switch, and you should have noticed the terminal output stayed green for VLAN 20.

### Example Playbook 2

In this next example, we'll look at physical attributes of interfaces. Two that will be shown are the type of interface, i.e. Layer 2 or Layer 3 and the description of the interface.

This playbook is the `hp-interfaces.yml` file.

```
---

  - name: Example for Configuration Interfaces
    hosts: hp1
    gather_facts: no
    connection: local

    vars:
      username: hp
      password: hp123

    tasks:

      - name: ensure these interfaces are routed
        comware_interface: name={{ item }} type=routed username={{ username }} password={{ password }} hostname={{ inventory_hostname }}
        with_items:
          - FortyGigE1/0/1
          - FortyGigE1/0/2
          - FortyGigE1/0/3
          - FortyGigE1/0/4

      - name: ensure the description for 1/0/1 is set
        comware_interface: name=FortyGigE1/0/1 description='ANSIBLE CONFIGURED THIS' username={{ username }} password={{ password }} hostname={{ inventory_hostname }}

      - name: ensure these interfaces are bridged
        comware_interface: name={{ item }} type=bridged username={{ username }} password={{ password }} hostname={{ inventory_hostname }}
        with_items:
          - FortyGigE1/0/9
          - FortyGigE1/0/10


```

As can be seen the playbook will almost always start with the same parameters.  The tasks in this example are using the `comware_interface` module.

When setting the port type to be `bridged` or `routed` no other configuration params (such as description) except those shown can be used.

As you should be able to tell, this playbook ensures that:
* FortyGigE1/0/1 - FortyGigE1/0/4 will be routed ports
* The description of "ANSIBLE CONFIGURED" will be on FortyGigE1/0/1
* FortyGigE1/0/9 - FortyGigE1/0/10 will be bridged interfaces

Run this playbook by entering the following command:

```
$ ansible-playbook -i hosts hp-interfaces.yml
```

Based on your system (these interface names exist on the HP 5930), you may have to change the names used to be compatible with the interfaces on your specific Comware 7 device.  You may also see different output based on the current state of the system.

Here is the output after running this playbook:

```
PLAY [Example for Configuration Interfaces] *********************************** 

TASK: [ensure these interfaces are routed] ************************************ 
changed: [hp1] => (item=FortyGigE1/0/1)
changed: [hp1] => (item=FortyGigE1/0/2)
changed: [hp1] => (item=FortyGigE1/0/3)
changed: [hp1] => (item=FortyGigE1/0/4)

TASK: [ensure the description for 1/0/1 is set] ******************************* 
changed: [hp1]

TASK: [ensure these interfaces are bridged]  ********************************** 
ok: [hp1] => (item=FortyGigE1/0/9)
ok: [hp1] => (item=FortyGigE1/0/10)

PLAY RECAP ******************************************************************** 
hp1                        : ok=3    changed=2    unreachable=0    failed=0   
```

Notice how the first four interfaces were changed, a description was configured, but the final two interfaces were not changed.  This is because FortyGigE1/0/9 and FortyGigE1/0/10 were already in bridged mode.

Run the playbook again and it should match this:

```
PLAY [Example for Configuration Interfaces] *********************************** 

TASK: [ensure these interfaces are routed] ************************************ 
ok: [hp1] => (item=FortyGigE1/0/1)
ok: [hp1] => (item=FortyGigE1/0/2)
ok: [hp1] => (item=FortyGigE1/0/3)
ok: [hp1] => (item=FortyGigE1/0/4)

TASK: [ensure the description for 1/0/1 is set] ******************************* 
ok: [hp1]

TASK: [ensure these interfaces are bridged]  ********************************** 
ok: [hp1] => (item=FortyGigE1/0/9)
ok: [hp1] => (item=FortyGigE1/0/10)

PLAY RECAP ******************************************************************** 
hp1                        : ok=3    changed=0    unreachable=0    failed=0   
```

Now notice that there were no changes made at all since the switch was already in the desired state for each task.

### Example Playbook 3

The next example shows how to create a bridged port-channel (aggregation-group).

```
---

  - name: Example for Configuration of Portchannels
    hosts: hp1
    gather_facts: no
    connection: local

    vars:
      username: hp
      password: hp123

    tasks:

      - name: ensure these interfaces are bridged
        comware_interface: name={{ item }} type=bridged username={{ username }} password={{ password }} hostname={{ inventory_hostname }}
        with_items:
          - FortyGigE1/0/1
          - FortyGigE1/0/2
          - FortyGigE1/0/3
          - FortyGigE1/0/4

      - comware_portchannel:
          group: 100
          members:
            - FortyGigE1/0/1
            - FortyGigE1/0/2
            - FortyGigE1/0/3
            - FortyGigE1/0/4
          type: bridged
          mode: dynamic
          lacp_mode: active
          min_ports: 2
          max_ports: 4
          username: "{{ username }}"
          password: "{{ password }}"
          hostname: "{{ inventory_hostname }}"
          state: present

```

Before configuring a port-channel, the first step should always be to ensure the interfaces are in the proper mode.  Since we want to configure a bridge-aggregation group, we need to make sure the interfaces are of type bridged.  This is done using the `comware_interface` module as was just shown in the previous example.

The next task uses the `comware_portchannel` module to ensure that bridged-aggregation group 100 exists, has 4 members, is dynamic, and the mode is set to dynamic.  Min and max ports are also configured.

Notice that a different syntax was used for this task.  This is using YAML syntax, which uses a 2-space indent under the module name with the parameter and value separate by a colon.  The reason this is being used is that this format is required when sending *complex* data types such as a list as the value for a parameter within a playbook, and as can be seen in the example above, a list is being sent in as the value for  `members`.  The other thing to realize is that when variables are passed in as values, they need to be surrounded by quotes as shown for `username`, `password`, and `hostname`.

Here is the output from running the `hp-portchannels.yml` playbook.

```
$ ansible-playbook -i hosts hp-portchannel.yml 

PLAY [Example for Configuration of Portchannels] ****************************** 

TASK: [ensure these interfaces are bridged]  ********************************** 
changed: [hp1] => (item=FortyGigE1/0/1)
changed: [hp1] => (item=FortyGigE1/0/2)
changed: [hp1] => (item=FortyGigE1/0/3)
changed: [hp1] => (item=FortyGigE1/0/4)

TASK: [comware_portchannel ] ************************************************** 
changed: [hp1]

PLAY RECAP ******************************************************************** 
hp1                        : ok=2    changed=2    unreachable=0    failed=0  

```


### Example Playbook 4

The next example shows how to apply a new configuration in real-time to be the new current-running configuration of the HP Comware7 switch.  Underneath the covers, it's using the rollback feature of the switch.

**Note:** the example given is using a config file for the HP 5930 switch.

**Note:** ensure the credentials that you are using to connect to the switch are not removed. Same goes for ensuring NETCONF stays enabled and the management IP address stays the same.

**WARNING WARNING WARNING**

DO NOT APPLY THE DEMO CONFIG TO YOUR SWITCH OR YOU WILL LOSE CONNECTIVITY WITHOUT MAKING THE REQUIRED CHANGES!

The config file that will be applied can be found at `configs/demo.cfg`

The file NEEDS to have the credentials, default route, management IP, etc. required to maintain connectivity with the device.  The demo file has ALL ports set to bridged mode, no port-channels configured, and no VLANs configured.  It is a *clean* switch config.  It is also changing the hostname of the device.

#### DO NOT PUSH THIS FILE TO YOUR DEVICE WITHOUT CHANGING THE CREDS, MGMT IP ADDRESS, AND ROUTE ACCORDINGLY.

Here is the contents of the file:

```
#
 version 7.1.045, ESS 2415
#
 sysname HP5930_DEMO_1
#
 clock protocol none
#
 irf mac-address persistent timer
 irf auto-update enable
 undo irf link-delay
 irf member 1 priority 1
 irf mode normal
#
 lldp global enable
#
 system-working-mode standard
 fan prefer-direction slot 1 port-to-power
 password-recovery enable
#
vlan 1
#
 stp global enable
#
interface NULL0
#
interface FortyGigE1/0/1
 port link-mode bridge
#
interface FortyGigE1/0/2
 port link-mode bridge
#
interface FortyGigE1/0/3
 port link-mode bridge
#
interface FortyGigE1/0/4
 port link-mode bridge
#
interface FortyGigE1/0/5
 port link-mode bridge
#
interface FortyGigE1/0/6
 port link-mode bridge
#
interface FortyGigE1/0/7
 port link-mode bridge
#
interface FortyGigE1/0/8
 port link-mode bridge
#
interface FortyGigE1/0/9
 port link-mode bridge
#
interface FortyGigE1/0/10
 port link-mode bridge
#
interface FortyGigE1/0/11
 port link-mode bridge
#
interface FortyGigE1/0/12
 port link-mode bridge
#
interface FortyGigE1/0/13
 port link-mode bridge
#
interface FortyGigE1/0/14
 port link-mode bridge
#
interface FortyGigE1/0/15
 port link-mode bridge
#
interface FortyGigE1/0/16
 port link-mode bridge
#
interface FortyGigE1/0/17
 port link-mode bridge
#
interface FortyGigE1/0/18
 port link-mode bridge
#
interface FortyGigE1/0/19
 port link-mode bridge
#
interface FortyGigE1/0/20
 port link-mode bridge
#
interface FortyGigE1/0/21
 port link-mode bridge
#
interface FortyGigE1/0/22
 port link-mode bridge
#
interface FortyGigE1/0/23
 port link-mode bridge
#
interface FortyGigE1/0/24
 port link-mode bridge
#
interface FortyGigE1/0/25
 port link-mode bridge
#
interface FortyGigE1/0/26
 port link-mode bridge
#
interface FortyGigE1/0/27
 port link-mode bridge
#
interface FortyGigE1/0/28
 port link-mode bridge
#
interface FortyGigE1/0/29
 port link-mode bridge
#
interface FortyGigE1/0/30
 port link-mode bridge
#
interface FortyGigE1/0/31
 port link-mode bridge
#
interface FortyGigE1/0/32
 port link-mode bridge
#
interface M-GigabitEthernet0/0/0
 ip address 10.1.100.40 255.255.255.0
#
 scheduler logfile size 16
#
line class aux
 user-role network-admin
#
line class vty
 user-role network-operator
#
line aux 0
 user-role network-admin
#
line vty 0 15
 authentication-mode scheme
 user-role network-admin
 user-role network-operator
 set authentication password hash $h$6$0pCOOSzAnWNbItO9$KfV0V1Jo1PVFMrG9lelj81GGw4IPX5u2kF6CmRpgOng3Ab1MS7gb84qKmHksuKSLDIr/0/X1Rbq+otiYniGwTg==
#
line vty 16 63
 user-role network-admin
 user-role network-operator
#
 ip route-static 0.0.0.0 0 10.1.100.1
#
 ssh server enable
 ssh user hp service-type all authentication-type password
 scp server enable
#
radius scheme system
 user-name-format without-domain
#
domain system
#
 aaa session-limit ftp 16
 aaa session-limit telnet 16
 aaa session-limit http 16
 aaa session-limit ssh 16
 aaa session-limit https 16
 domain default enable system
#
role name level-0
 description Predefined level-0 role
#
role name level-1
 description Predefined level-1 role
#
role name level-2
 description Predefined level-2 role
#
role name level-3
 description Predefined level-3 role
#
role name level-4
 description Predefined level-4 role
#
role name level-5
 description Predefined level-5 role
#
role name level-6
 description Predefined level-6 role
#
role name level-7
 description Predefined level-7 role
#
role name level-8
 description Predefined level-8 role
#
role name level-9
 description Predefined level-9 role
#
role name level-10
 description Predefined level-10 role
#
role name level-11
 description Predefined level-11 role
#
role name level-12
 description Predefined level-12 role
#
role name level-13
 description Predefined level-13 role
#
role name level-14
 description Predefined level-14 role
#
user-group system
#
local-user hp class manage
 password hash $h$6$/qN0r/IMnFFHtHRP$osdT3d7AmyPPa/KC0sdu6DCNwSuiNhBzoSGuf+YZxA1yJUOFOTxEH477c5OyA6sm4ZqvOzBLykuqBkT6xIxBlA==
 service-type ftp
 service-type ssh http https
 authorization-attribute user-role network-admin
 authorization-attribute user-role network-operator
#
 netconf soap http enable
 netconf ssh server enable
#
return

```

The playbook that will push this config file to switch is called `hp-install_config.yml`

It looks like this:

```
---

  - name: Example for using install config
    hosts: hp1
    gather_facts: no
    connection: local

    vars:
      username: hp
      password: hp123


    tasks:

      - name: install config file that will be the new running config
        comware_install_config:
          config_file='./configs/demo.cfg'
          diff_file='./configs/demo-diff.diff'
          commit_changes=true
          username={{ username }}
          password={{ password }}
          hostname={{ inventory_hostname }}
```

To install the config, the `comware_install_config` module is used.  The `config_file` parameter is required and is the full absolute path of the config file you want to push to the device.  The `diff_file` is optional, but will show the existing and new config files, and `commit_changes` is required as a safeguard.  If it's not set to true, the config will not be applied to the device.

Let's execute this playbook (remember to make sure your credentials, IP, and route are properly in YOUR config file).

Use the following command to execute the playbook:

```
$ ansible-playbook -i hosts hp-install_config.yml -v
```

This time we used the `-v` or verbose flag that shows a little more detail of what's happening.

Here is the response:

```

PLAY [Example for using install config] *************************************** 

TASK: [install config file that will be the new running config] *************** 
changed: [hp1] => {"active_files": {"backup": "flash:/safety_file.cfg", "config_applied": "flash:/demo.cfg", "startup": "flash:/startup.cfg"}, "changed": true, "commit_changes": true, "config_file": "/home/ansible/hp/configs/demo.cfg", "diff_file": "/home/hp/configs/demo-diff.diff"}

PLAY RECAP ******************************************************************** 
hp1                        : ok=1    changed=1    unreachable=0    failed=0   

```

What this module does is three things:

  1. Saves the current working config as flash:/safety_file.cfg
  2. Loads the config you passed in as the new current running config
  3. Saves the new running config to flash:/startup.cfg


That covers a few different types of examples using the modules to automate HP Comware 7 devices.  Additionally, there are a number of test playbooks that can be found in the `test-pbs` directory.  There is one test playbook per feature or module.  Each of these playbooks have numerous examples of how to use one or more modules, but are more importantly used to prove modules are working properly.

## Using ansible-doc

`ansible-doc` is a utility that offers users built-in "man-page-like" docs for Ansible modules.  The `-M` flag that is used with it specifies the directory in which the modules reside.

```
$ ansible-doc -M library/ comware_vlan
```

You will see the following output:

```
$ ansible-doc comware_vlan
> COMWARE_VLAN

  Manage VLAN resources and attributes for Comware v7 devices

Options (= is mandatory):

- descr
        Description for the VLAN (Choices: ) [Default: None]

= hostname
        IP Address or hostname of the Comware v7 device that has
        NETCONF enabled (Choices: ) [Default: None]

- name
        Name to configure for the specified VLAN ID (Choices: )
        [Default: None]

= password
        Password used to login to the switch (Choices: ) [Default:
        None]

= port
        NETCONF port number (Choices: ) [Default: 830]

= username
        Username used to login to the switch (Choices: ) [Default:
        None]

= vlanid
        VLAN ID to configure (Choices: ) [Default: None]


# ensure VLAN 10 exists
- comware_vlan: vlanid=10 name=VLAN10_WEB descr=LOCALSEGMENT state=present username={{ username }} password={{ pas

# update name and descr
- comware_vlan: vlanid=10 name=WEB10 descr=WEBDESCR state=present username={{ username }} password={{ password }} 

# ensure VLAN 10 does not exist
- comware_vlan: vlanid=10 state=absent username={{ username }} password={{ password }} hostname={{ inventory_hostn

```

When you start using modules, this is a great command line utility to reference to understand the parameters each module supports.  It can be used for not only the HP modules, but also any native Ansible module as well.

**Note:** The docs contained within the `ansible-doc` command line utility for the HP modules are the same docs that can be found on the web [here.](module_docs/module_docs.md) and even better docs can be found [here](https://hp-ansible.readthedocs.io/en/latest/index.html)

# Requirements

* Comware 7 switch that supports NETCONF over SSH (not SOAP)
* Modules require the pyhpecw7 library as described above
* Devices require NETCONF to be enabled
* All testing was performed on HP 5930 switches

