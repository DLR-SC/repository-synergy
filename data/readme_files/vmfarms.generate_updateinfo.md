UPDATEINFO.XML GENERATION
=========================

This utility eats an errata.latest.xml from the CEFS project [http://cefs.steve-meier.de]
and converts it in to a useable updateinfo.xml that you can inject in to your CentOS 
repositories. It is purpose built for a specific use case, but it can be modified to 
suit your particular needs.


Usage
-----
You must set the configuration variables in the header of the script first.
Once you've done this, simply run:

```bash
generate_updateinfo.py /path/to/errata.latest.xml
```

It will write out a number of updateinfo.xml files in the 
BUILD_PREFIX/updateinfo-RELEASES/ directory.

You can now take the appropriate updateinfo.xml file and inject it in your
repository using the /usr/bin/modifyrepo command.

*NOTE* that there is an 'other' release in the RELEASES variable. That is the directory where 
all packages that don't match a particular release number will be stored. You can use this for
debugging or other tracking purposes. You don't need to inject this in to any of your repos.

Example
-------
The following example illustrates how you would go about using this for a CentOS 6 repo.
The assumption is that you've set the BUILD_PREFIX=/security and that your CentOS-6-Updates
directory lives under /repositories/

```bash
wget -q -N -P/tmp http://cefs.steve-meier.de/errata.latest.xml.bz2

(cd /tmp/ && sha1sum -c <(wget -qO- http://cefs.steve-meier.de/errata.latest.sha1|grep bz2) )

generate_updateinfo.py <(bzip2 -dc /tmp/errata.latest.xml.bz2)

/usr/bin/modifyrepo /tmp/updateinfo-6/updateinfo.xml /repositories/CentOS-6-Updates/repodata
```

Now that your repos have the data they need you can install the yum-plugin-security package
and make use of it like so

```bash
yum install yum-plugin-security

yum security-list

Loaded plugins: changelog, fastestmirror, security
Loading mirror speeds from cached hostfile
CentOS-6-OS                                                                                                                                                                              | 1.2 kB     00:00
CentOS-6-Updates                                                                                                                                                                         | 1.2 kB     00:00

CESA_2013__1764        security    ruby-1.8.7.352-13.el6.x86_64
CESA_2013__1764        security    ruby-irb-1.8.7.352-13.el6.x86_64
CESA_2013__1764        security    ruby-libs-1.8.7.352-13.el6.x86_64
CESA_2013__1764        security    ruby-rdoc-1.8.7.352-13.el6.x86_64
CESA_2013__1806        security    samba-client-3.6.9-167.el6_5.x86_64
CESA_2013__1806        security    samba-common-3.6.9-167.el6_5.x86_64
CESA_2013__1806        security    samba-winbind-3.6.9-167.el6_5.x86_64
CESA_2013__1806        security    samba-winbind-clients-3.6.9-167.el6_5.x86_64
```

Authors
-------
Kristian Kostecky [http://vmfarms.com]


Copyright and license
---------------------

Copyright (C) 2013  Kristian K. [http://vmfarms.com] [kris@vmfarms.com]

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see [http://www.gnu.org/licenses/].
