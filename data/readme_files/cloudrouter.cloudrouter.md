# CloudRouter [![Join the chat at https://gitter.im/cloudrouter/cloudrouter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/cloudrouter/cloudrouter?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

![CloudRouter Logo](http://cloudrouter.org/wp-content/uploads/2015/01/CloudRouter-Logo-Regular.png)

## Overview

The CloudRouter Project is a collaborative open source project focused on bringing simplicity to network interconnection, a traditionally complex process. With the growing proliferation of performance and security issues occurring over the public Internet, there is an increasing demand for secure, direct network-to-network interconnection, including Enterprise to Cloud.  The CloudRouter community is developing and maintaining an open source software distribution of networking technologies.


### Features

- Full-stack SDN implementation including OpenDaylight
- Standards-based interfaces
- Built on the rock-solid foundation of Linux
- Monitoring and availability
- Support for Docker containers and OSv images
- Architecture & design goals

### Architecture & Design Goals

- Optimized for interconnection
- Run in the cloud or on-premise
- One size does not fit all: a choice of components and distribution formats
- Easy to use and configure
- Security as a core feature, not an afterthought
- High performance with minimal resource consumption
- Highly scalable

### Installation

CloudRouter can be run on a variety of cloud hosts. For local testing purposes, the KVM hypervisor with virt-manager is recommended. 

To install the image using virt-manager, follow these steps:

1. Uncompress the image: 

		$ unxz CloudRouter-Beta-20150120.x86_64.raw.xz

2. Verify that the SHA-512 checksum is correct:

		$ sha512sum CloudRouter-Beta-20150120.x86_64.raw.xz 8c4d0bb2723dc67e23bae363ac4ecc2ff7510d567ab7fa6d3077dfc95dc8d83c0d362ea7d5050e4366b9d6d1ab49e24b032e2f444e22e633863e9242925fc701 CloudRouter-Beta-20150120.x86_64.raw.xz

3. Create a new virtual machine in virt-manager. When prompted, select the “Import existing disk image” option. Select CloudRouter-Beta-20150116.x86_64.raw as the disk image. Alternatively, [use virsh](http://youtu.be/ISUJaYv0hg8).

4. Select appropriate memory and CPU resources. 2048MB memory and 2 vCPUs are recommended.

5. Start the virtual machine.

6. At this point you have CloudRouter running, but cannot login. For enhanced security, the CloudRouter image ships without any default credentials. The default “fedora” user is inherited from Fedora, but no password is set. To set a password, you must create a metadata ISO image.

7. Login & Enjoy!

##### Creating/Using a Metadata ISO

Create a metadata ISO based on the instructions in [this blog post](https://www.technovelty.org//linux/running-cloud-images-locally.html). 

Alternatively, download the [pre-built metadata ISO](http://cloudrouter.org/repo/beta/images/cr-init.iso). This ISO sets the fedora user’s password to “CloudRouter”. DO NOT use this ISO in production, it is strictly for test and demonstration purposes.

In virt-manager or VMware, attach the metadata ISO to the CloudRouter VM as a CDROM storage device.



#### Running OpenDayLight

CloudRouter 1.0 beta is based on the Fedora 20 cloud image, and includes a distribution of OpenDaylight Helium SR1.1. The video below demonstrates how to run OpenDaylight on CloudRouter.

[![Run OpenDayLight on CloudRouter](http://img.youtube.com/vi/Lq53clTFI4I/0.jpg)](http://www.youtube.com/watch?v=Lq53clTFI4I)

For more details on using OpenDaylight, see the [OpenDaylight Getting Started Guide](http://www.opendaylight.org/resources/getting-started-guide).

### Contributing

To contribute to the CloudRouter project, just fork the repo and send pull requests with any changes. We love getting pull requests! Frequent contributors will be granted access to commit directly to the CloudRouter repo.

### Community Resources

##### Usage

The <users@lists.cloudrouter.org> mailing list is a forum for discussing usage of CloudRouter, including problems, feature requests and general discussion. To subscribe to the users list, go to: <http://lists.cloudrouter.org/mailman/listinfo/users/>

##### Development

The <devel@lists.cloudrouter.org> mailing list is a forum for discussing development of CloudRouter and associated technologies. To subscribe to the devel list, go to: <http://lists.cloudrouter.org/mailman/listinfo/devel/>

##### Live Discussion

For more real-time discussion, join us on IRC: *irc.freenode.net* **#CloudRouter**

### More Information

For more information on the CloudRouter project, visit [CloudRouter.org](https://cloudrouter.org/).

---

*CloudRouter is a registered trademark of IIX Inc. All rights reserved. 
