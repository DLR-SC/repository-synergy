# Deprecation Notice

This repository has been deprecated in favor of native Linux modules. For more information, see [this knowledge base article](https://support.cumulusnetworks.com/hc/en-us/articles/115010587028). 

---

This is the top level Git repository for Cumulus Linux Ansible Modules

The following modules can be found within the [library](library) folder.

- [cl_img_install](library/cl_img_install.py) — Install a different version of Cumulus Linux in the inactive slot.
- [cl_interface](library/cl_interface.py)  — Configures a front panel, bridge or bond interface on a Cumulus Linux switch.
- [cl_bond](library/cl_bond.py)  - Configures bond interface
- [cl_bridge](library/cl_bridge.py)  - Configures bridge interface
- [cl_interface_policy](library/cl_interface_policy.py)  - Configures Interface enforcement policy
- [cl_ports](library/cl_ports.py)  - Configure Switch Port Attributes, i.e. Breakout Ports defined in `/etc/cumulus/ports.conf`
- [cl_license](library/cl_license.py)  — Install a Cumulus Linux license.
- [cl_quagga_ospf](library/cl_quagga_ospf.py)  - Configures basic OSPFv2 global parameters and OSPFv2 interface configuration.
- [cl_quagga_protocol](library/cl_quagga_protocol.py)  - Enable Quagga services available on Cumulus Linux.

Documentation for each of the modules, along with examples, is included in each module as Python docstrings.

## INSTALLATION
A Cumulus Linux switch can be provisioned and operated, using Ansible, with no extra plugins. Cumulus Linux, by default, has SSH enabled with a BASH login.

Cumulus Networks Ansible Library is hosted on the Ansible Galaxy website under the role [CumulusLinux](https://galaxy.ansible.com/list#/roles/1875).

To download the CumulusLinux role to the Ansible host, execute the ansible-galaxy install command, and specify **cumulus.CumulusLinux**.

```
cumulus@ansible-vm:~$ sudo ansible-galaxy install cumulus.CumulusLinux
 downloading role 'CumulusLinux', owned by cumulus
 no version specified, installing master
 - downloading role from https://github.com/cumulusnetworks/cumulus-linux-ansible-modules/archive/master.tar.gz
 - extracting cumulus.CumulusLinux to /etc/ansible/roles/cumulus.CumulusLinux
cumulus.CumulusLinux was installed successfully
cumulus@ansible-vm:~$
```

For more detailed installation guide please refer to the [Cumulus Linux Knowledge Base](https://support.cumulusnetworks.com/hc/en-us/articles/204255593)

## REQUIREMENTS

Ansible 1.8 and higher. The modules require features supported in 1.8 and higher.


##EXAMPLE PLAYBOOKS

[OSPF Unnumbered topologies automated using Ansible](https://github.com/CumulusNetworks/example-ospfunnum-ansible)


## DEVELOPMENT

###CONTRIBUTING

1. Fork it.
2. Create your feature branch (`git checkout -b my-new-feature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin my-new-feature`).
5. Create new Pull Request.


###TESTING

All modules created have associated nose test cases. Test cases can be found in ``tests`` directory.
To run the tests execute the ``runtests.py`` script while in the root of this Git repository.  Before running a test, check that the python Mock and Nose packages are installed.


## LICENSE AND AUTHORS
Author:: Cumulus Networks Inc.

Copyright:: 2015 Cumulus Networks Inc.

---

![Cumulus icon](http://cumulusnetworks.com/static/cumulus/img/logo_2014.png)

### Cumulus Linux

Cumulus Linux is a software distribution that runs on top of industry standard
networking hardware. It enables the latest Linux applications and automation
tools on networking gear while delivering new levels of innovation and
ﬂexibility to the data center.

For further details please see: [cumulusnetworks.com](http://www.cumulusnetworks.com)

This project is licensed under the GNU General Public License, Version 2.0
