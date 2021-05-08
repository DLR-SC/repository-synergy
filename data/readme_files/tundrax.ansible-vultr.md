# ansible-vultr
Ansible module for managing servers on [Vultr](http://www.vultr.com/?ref=6823697).
At the moment the module supports __only__ server __creation and destruction__.

## Installation
```sh
$ cd path-to-playbook-dir
$ mkdir library
$ git clone git@github.com:tundrax/ansible-vultr.git library/vultr
```

_NOTE:_ Ansible 2.x users must set `ANSIBLE_LIBRARY=./library`.

## Usage example

This is the main playbook for dynamic inventory provisioning using Vultr.
```yaml
---
- hosts: localhost
  connection: local
  gather_facts: false

  vars:
    api_key: YOUR_API_KEY
    servers:
      # ------------------------------------------------
      # - backend
      # ------------------------------------------------
      - { label: "api.example.com",  group: "lb" }
      - { label: "app1.example.com", group: "app" }
      - { label: "app2.example.com", group: "app" }
      - { label: "mdb1.example.com", group: "db" }
      # ------------------------------------------------
      # - frontend
      # ------------------------------------------------
      - { label: "example.com", group: "web" }
  tasks:
    - name: Provision Vultr servers
      vultr:
        command: server
        api_key: "{{ api_key }}"
        state: "{{ item.state | default('present') }}"
        label: "{{ item.label }}"
        DCID: "{{ item.DCID | default(25) }}" # Tokyo
        VPSPLANID: "{{ item.VPSPLANID | default(201) }}" # 1024MB / 25GB SSD
        OSID: "{{ item.OSID | default(167) }}" # CentOS 7x64
        SSHKEYID: "{{ item.SSHKEYID | default(YOUR_SSH_KEY_ID) }}"
        enable_private_network: yes
        unique_label: yes
      register: created_servers
      with_items: servers
    # ------------------------------------------------
    # - Append servers to corresponding groups
    # ------------------------------------------------
    - name: Add Vultr hosts to inventory groups
      add_host:
        name: "{{ item.1.server.main_ip }}"
        groups: "cloud,{{ servers[item.0].group }},{{ item.1.server.label }}"
        label: "{{ item.1.server.label }}"
        internal_ip: "{{ item.1.server.internal_ip }}"
      when: item.1.server is defined
      with_indexed_items: created_servers.results
```


## Example playbook for deploying a custom OS using a custom ISO

You will need the ISOID for any custom ISOs you've already uploaded to Vultr.
These are retrievable via the following command:

```sh
$ curl -H 'API-Key: YOUR_API_KEY' https://api.vultr.com/v1/iso/list
```

This is the main playbook for deploying a custom OS using a custom uploaded ISO.

```yaml
---
- hosts: localhost
  connection: local
  gather_facts: false

  vars:
    api_key: YOUR_API_KEY
    servers:
      - { label: "example.com", group: "web", OSID: "159", ISOID: YOUR_ISO_ID }
  tasks:
    - name: Provision Vultr servers
      vultr:
        command: server
        api_key: "{{ api_key }}"
        state: "{{ item.state | default('present') }}"
        label: "{{ item.label }}"
        DCID: "{{ item.DCID | default(25) }}" # Tokyo
        VPSPLANID: "{{ item.VPSPLANID | default(201) }}" # 1024MB / 25GB SSD
        OSID: "{{ item.OSID | default(159) }}" # Custom OS
        ISOID: "{{ item.ISOID | default(0) }}"
        SSHKEYID: "{{ item.SSHKEYID | default(YOUR_SSH_KEY_ID) }}"
        enable_private_network: yes
        unique_label: yes
      register: created_servers
      with_items: servers
    # ------------------------------------------------
    # - Append servers to corresponding groups
    # ------------------------------------------------
    - name: Add Vultr hosts to inventory groups
      add_host:
        name: "{{ item.1.server.main_ip }}"
        groups: "cloud,{{ servers[item.0].group }},{{ item.1.server.label }}"
        label: "{{ item.1.server.label }}"
        internal_ip: "{{ item.1.server.internal_ip }}"
      when: item.1.server is defined
      with_indexed_items: created_servers.results
```

## Optional Parameters

The following optional parameters may be passed along to the server command:
 * ISOID
 * hostname
 * tag
 * snapshotid
 * reservered_ip_v4
 * auto_backups
 * ddos_protection
 * notify_activate

## Known issues
When you deploy a __new__ server on Vultr, you should wait until initialization finishes.
In ansible we accomplish this using __wait_for__ module. Below, the first task that should run on all servers is **to wait for port 22** to become available.
Once port 22 is active - ping all servers. At this step port 22 may have become available, but your ssh key has not been copied to `authorized_keys` yet. Hence you will get __denied access error__. Rerun the playbook 2-3 seconds later, all should go fine.
```yaml
# ------------------------------------------------
# - Run below tasks on group 'cloud', which contains
# - all servers being provisioned
# ------------------------------------------------
- hosts: cloud
  remote_user: root

  tasks:
    - name: Wait for port 22 to become available
      local_action: "wait_for port=22 host={{ inventory_hostname }}"

    - name: Ping pong all hosts
      ping:

    - name: Ensure hostname is preserved in cloud-init
      lineinfile: "dest=/etc/cloud/cloud.cfg regexp='^preserve_hostname' line='preserve_hostname: true' state=present"

    - name: Set hostname in sysconfigs
      lineinfile: dest=/etc/sysconfig/network regexp="^HOSTNAME" line='HOSTNAME="{{ hostvars[inventory_hostname].label }}"' state=present
      register: hostname

    - name: Set hosts FQDN
      lineinfile: dest=/etc/hosts regexp=".*{{ hostvars[inventory_hostname].label }}$" line="{{ inventory_hostname }} {{ hostvars[inventory_hostname].label }}" state=present
      register: fqdn

    - name: Set hostname
      hostname: name={{ hostvars[inventory_hostname].label }}
      when: hostname.changed or fqdn.changed

    - name: Configure eth1 (private network)
      template: src=ifcfg-eth1.j2 dest=/etc/sysconfig/network-scripts/ifcfg-eth1
      register: ifcfg_eth1

    - name: Enable eth1 (private network)
      service: name=network state=restarted
      when: hostname.changed or fqdn.changed or ifcfg_eth1.changed
```
As stated in "Configure eth1 (private network)" task, below is the interface config file.
This file should be located in the same folder as the playbook.
```ini
# ifcgf-eth1.j2
DEVICE="eth1"
ONBOOT="yes"
NM_CONTROLLED="no"
BOOTPROTO="static"
IPADDR="{{ hostvars[inventory_hostname].internal_ip }}"
NETMASK="255.255.0.0"
IPV6INIT="no"
```
