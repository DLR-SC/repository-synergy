[![Build Status](https://travis-ci.org/Apstra/aeon-ztps.svg?branch=master)](https://travis-ci.org/Apstra/aeon-ztps)
[![Coverage Status](https://coveralls.io/repos/github/Apstra/aeon-ztps/badge.svg?branch=master&no-cache)](https://coveralls.io/github/Apstra/aeon-ztps?branch=master)
[![Documentation Status](https://readthedocs.org/projects/aeon-ztps/badge/?version=latest)](http://aeon-ztps.readthedocs.io/en/latest/?badge=latest)


# Aeon-ZTPS

Aeon-ZTPS is a universal Zero-Touch-Provisioning server for data center infrastructure systems.  Aeon-ZTPS was
developed specifically to address the need for network engineers to bootstrap their datacenter switches without
having to deal with the differences in the underlying NOS mechanisms.

Aeon-ZTPS runs as an Ubuntu 16.04LTS server using the Flask framework and a simple SQLite database.  The system
provides both a REST/JSON API and a GUI.  The Aeon-ZTPS can optionally provide the DHCP service (included, but not
enabled by default).

The complete documentation for Aeon-ZTPS can be found at [Read the Docs](http://aeon-ztps.readthedocs.io/en/latest/). You can also build the docs locally by running "python setup.py build_sphinx" in the project root directory. You can then access the docs by opening the file docs/_build/sphinx/html/index.html.

Questions? Comments? Please feel free to post on the github issues list.

# Supported Systems
The initial release of the Aeon-ZTP server supports the following NOS/hardware:

| NOS | Hardware | Process |
|-----|----------|---------|
|Cisco NX-OS     | 9K and 3K models | [POAP](http://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus3000/sw/fundamentals/503_U3_1/b_Nexus_3000_Fundamentals_Guide_Release_503_U3_1/using_power_on_auto_provisioning.pdf)        |
|Arista EOS      | All models       | [Arista ZTP](https://eos.arista.com/ztp-set-up-guide/)        |
|Cumulus Linux   | All models       | [ONIE](http://onie.org/) and [Cumulus AutoProvisioning](https://docs.cumulusnetworks.com/display/DOCS/Zero+Touch+Provisioning+-+ZTP)        |
|OpenSwitchOPX   | All models       | Via register URL
|Ubuntu Server   | 14.04 and 16.04  | Via register URL
# Installation
If you are using VirtualBox, you can build and install the Aeon-ZTP server by invoking "vagrant up" from within the install directory after configuring the setup files.  For the complete details on the installation process, please refer to the [installation guide](https://aeon-ztps.readthedocs.io/en/latest/installation-guide/installation-guide.html).

# Screenshots

Aeon-ZTPS includes a web-based GUI dashboards to provide visibility into the device bootstrap process.  The following
illustrates the devices dashboard:

![Dashbaord-Devices](docs/source/_static/dashboard-devices.png)

Aeon-ZTPS includes comprehensible logging.  The logging dashboard allows you to inspect and filter the various log
files that are used by the system:

![Dashbaord-Logs](docs/source/_static/dashboard-logs.png)

Aeon-ZTPS includes a REST/JSON based API.  The following illustrates the `/api/devices` output showing the device
ZTP status:

![API-devices](docs/source/_static/api-devices.png)



# License
Apache 2.0
