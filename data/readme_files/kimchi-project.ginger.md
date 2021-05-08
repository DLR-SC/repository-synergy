Ginger
======

Ginger is an open source host management plugin to Wok, Web Server Originated
from Kimchi, that provides an intuitive web panel with common tools for
configuring and operating Linux systems.

Wok is a cherrypy-based web framework with HTML5 support that is extended by
plugins which expose functionality through REST APIs.

The current features of Host Management of Linux system include:
 + retrieve system health (sensors) stats
 + user login account management,
 + network interface configuration,
 + configuration backup,
 + Power (ppc) firmware update,
 + Power policy management.

Browser Support
===============

Wok and its plugin can run in any web browser that supports HTML5. The
Kimchi community (responsible for Wok project) makes an effort to
test it with the latest versions of Chrome and Firefox browsers, but the
following list can be used as reference to browser support.

Desktop Browser Support:
-----------------------
* **Internet Explorer:** Current version
* **Chrome:** Current version
* **Firefox:** Current version
* **Safari:** Current version
* **Opera:** Current version

Mobile Browser Support:
-----------------------
* **Safari iOS:** Current version
* **Android Browser** Current version


Hypervisor Distro Support
=========================

Ginger might run on any GNU/Linux distribution that meets the conditions
described on the 'Getting Started' section below.

The Ginger community makes an effort to test it with the latest versions of
Fedora, RHEL, IBM PowerKVM, Ubuntu and OpenSUSE.

Getting Started
===============

All Ginger functionalities are provided to user by Wok infra-structure.
It's important to install Wok before any Ginger operation be enabled on
the system. In addition, Ginger also requires that Ginger Base be installed in
the system.

There are two ways to have Ginger and Wok + Ginger Base running together: by
their packages (latest stable release) or by source code (development release).

Installing From Packages
------------------------

Kimchi and Ginger teams provide packages of the latest stable release of Wok,
Ginger Base and Ginger. To install them, follow the install instructions
on:

http://kimchi-project.github.io/wok/downloads/

and

http://kimchi-project.github.io/gingerbase/downloads/

and

http://kimchi-project.github.io/ginger/downloads/

Installing from Source Code
---------------------------

Before anything, it's necessary install Wok and Ginger Base dependencies. To
install Wok dependencies, see Wok's README file at
https://github.com/kimchi-project/wok/blob/master/docs/README.md and to install
Ginger Base dependencies, see Ginger Base's READE file at
https://github.com/kimchi-project/gingerbase/blob/master/docs/README.md

To install Ginger dependencies, follow:

**For Fedora, RHEL and IBM PowerKVM :**

```
$ sudo yum install  hddtemp libuser-python python-augeas python-netaddr\
                    python-ethtool python-ipaddr python-magic \
                    tuned lm_sensors python2-crypto

# For IBM PowerKVM
$ sudo yum install powerpc-utils serviceable-event-provider

# These dependencies are only required if you want to run the tests:
$ sudo yum install python-mock
```

**For Debian/Ubuntu:**

```
$ sudo apt-get install  hddtemp python-libuser python-ethtool python-augeas \
                        python-ipaddr python-magic python-netaddr python-crypto

# These dependencies are only required if you want to run the tests:
$ sudo apt-get install python-mock
```

**For OpenSUSE:**

```
# Add repository for hddtemp:
$ sudo zypper ar -f http://download.opensuse.org/repositories/utilities/openSUSE_Leap_42.1/ utilities

# Add repository for python-parted:
$ sudo zypper ar -f http://download.opensuse.org/repositories/home:/GRNET:/synnefo/openSUSE_Leap_42.1/ home_GRNET_synnefo

# Add repository for python-ethtool:
$ sudo zypper ar -f http://download.opensuse.org/repositories/systemsmanagement:/spacewalk/openSUSE_Leap_42.1/ spacewalk

# Add repository for python-magic:
$ sudo zypper ar -f http://download.opensuse.org/repositories/home:/Simmphonie:/python/openSUSE_Leap_42.1/ home_Symmphonie_python

$ sudo zypper install hddtemp libuser-python python-augeas python-netaddr\
                      python-ethtool python-ipaddr python-magic python-pycrypto

# These dependencies are only required if you want to run the tests:
$ sudo zypper install python-mock
```

After install and resolve all dependencies, clone the source code of all
projects:

```
$ git clone --recursive https://github.com/kimchi-project/wok.git
$ cd wok
$ git submodule update --remote
$ ./build-all.sh
```

To run Ginger tests, execute:

```
$ cd src/wok/plugins/ginger
$ make check-local                      # check for i18n and formatting errors
$ sudo make check                       # execute unit tests
```
After all tests are executed, a summary will be displayed containing any
errors/failures which might have occurred.

Regarding UI development, make sure to update the CSS files when modifying the
SCSS files by running:

```
$ sudo make -C ui/css css
```

Run
---

To run Wok, Ginger Base and Ginger from the packages installed, execute:

```
$ sudo systemctl start wokd.service
```

After compile all source codes, from the wok directory cloned, execute:

```
$ sudo ./src/wokd --host=0.0.0.0
```

**Notes on Power policy management feature**

The power policy management feature uses the 'tuned' service to control the
power policies of the host. Problems have been reported with this package,
depending on the host configuration, such as SELinux denials and trouble
to communicate using DBUS with the 'tuned' service started from systemd.

If you find any problems with the power policy management feature, we
recommend following these steps (all steps requires 'sudo' privileges):

- put SELinux in permissive mode for 'tuned' (required if the version of the
package 'selinux-policy' is < 3.11):

```
$ sudo semanage permissive -a tuned_t
```

- disable the 'tuned' service from systemd and restart it by hand:

```
$ sudo systemctl stop tuned.service
$ sudo tuned -l -P -d
```

Remember to restart wokd service after these changes:

```
$ sudo systemctl restart wokd.service
```

If these steps do not solve the problem, try to update all 'tuned' related
packages and the packages'selinux-policy' and 'selinux-policy-targeted'.


Participating
-------------

All patches are sent through our mailing list.  More information can be found at:

https://github.com/kimchi-project/ginger/wiki/Communications

Patches should be sent using git-send-email to ginger-dev-list@googlegroups.com

**Copyright notice**

All the .gif and .png files in 'ui/css/base/images/' directory are licensed
as follows:

```
Copyright IBM Corp, 2015

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
```
