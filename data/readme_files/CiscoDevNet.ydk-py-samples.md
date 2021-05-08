# Sample Apps for YDK-Py
This repository provides a collection of sample applications that use [YDK-Py](https://github.com/CiscoDevNet/ydk-py) for network programmability.  YDK-Py is the Python package for the Cisco YANG development kit (YDK) which provides model-driven APIs generated from a variety of YANG models.  

## A "hello, world" App
The [hello-ydk.py](hello-ydk.py) script illustrates a minimalistic app that prints the uptime of a device running Cisco IOS XR.  The script opens a NETCONF session to a device with address 10.0.0.1, reads the system time and prints the formatted uptime.

```python
# import providers, services and models
from ydk.services import CRUDService
from ydk.providers import NetconfServiceProvider
from ydk.models.cisco_ios_xr import Cisco_IOS_XR_shellutil_oper \
    as xr_shellutil_oper
from datetime import timedelta


if __name__ == "__main__":
    """Main execution path"""

    # create NETCONF session
    provider = NetconfServiceProvider(address="10.0.0.1",
                                      port=830,
                                      username="admin",
                                      password="admin",
                                      protocol="ssh")
    # create CRUD service
    crud = CRUDService()

    # create system time object
    system_time = xr_shellutil_oper.SystemTime()

    # read system time from device
    system_time = crud.read(provider, system_time)

    # print system uptime
    print("System uptime is " +
          str(timedelta(seconds=system_time.uptime.uptime)))

    exit()
```

Sample output
```
$ ./hello-ydk.py
System uptime is 5 days, 3:52:08
$
```

## Sample App Library
This repository includes a large number of [basic sample apps](samples/basic). They focus on a single model and have no or minimal programming logic (conditionals, loops, etc).  They should be your starting point if you don't have strong experience with models or programming.  They are grouped by service and model.

## Installation
The sample apps do not require any special installation.  You can [download](https://github.com/CiscoDevNet/ydk-py/archive/master.zip) the entire repository as a compressed file or you can clone it:
```
$ git clone https://github.com/CiscoDevNet/ydk-py-samples.git
```

## Running an App
Instructions for running the basic apps can be found in their [README](samples/basic/README.md) file.  Before you attempt to run any app, verify that your system supports Python 2.7 / 3.4 (or later):
```
$ python --version
Python 2.7.6
$
$ python3 --version
Python 3.5.2
$
```

Your system must also have YDK-Py installed, including the respective model bundle (e.g. Cisco IOS XR, Cisco IOS XE, OpenConfig or IETF):
```
$ pip list | grep ydk
ydk                     0.6.0        
ydk-models-cisco-ios-xe 16.6.1       
ydk-models-cisco-ios-xr 6.2.2        
ydk-models-ietf         0.1.3        
ydk-models-openconfig   0.1.3        
$
```

If you don't have YDK-Py installed, verify [your system requirements](https://github.com/CiscoDevNet/ydk-py#system-requirements) and then follow the [YDK-Py installation instructions](https://github.com/CiscoDevNet/ydk-py#quick-install).

The [release versions of this repository](https://github.com/CiscoDevNet/ydk-py-samples/releases) match the [release versions of YDK-Py](https://github.com/CiscoDevNet/ydk-py/releases) used to test the sample apps.  Note that using a different YDK-Py version may break some of the sample apps.  For Cisco IOS XR models, you will need a device running at least Cisco IOS XR 6.0.0.  For Cisco IOS XE models, you will need a Cisco IOS XE device running at least 16.5.1.  

## Vagrant Sandbox
You can instantiate a YDK-Py sandbox on your computer using Vagrant.  The sandbox will provide an Ubuntu VM with YDK-Py pre-installed.  Make sure you have these prerequisites installed on your computer:
* [Virtualbox](https://www.virtualbox.org/wiki/Downloads)
* [Vagrant](https://www.vagrantup.com/downloads.html)
* An ssh client
* ssh keys generated on your system

To create a sandbox, issue the following command from the directory where the `Vagrantfile` resides:
```
$ vagrant up
```

To verify the status of your sandbox use:
```
$ vagrant status
```

Once your sandbox is running, you can connect to it using:
```
$ vagrant ssh
```

Note that the `samples` and `projects` directories are shared between your host and your Vagrant box.  Any changes to those directories are seen in both environments.  Any other data in your Vagrant box is isolated from your host and will be lost if you destroy your Vagrant box.

You can suspend and resume your sandbox using:
```
$ vagrant suspend
$ vagrant resume
```

To destroy your sandbox, issue the following command:
```
$ vagrant destroy
```

If you previously instantiated a YDK-Py sandbox, you can check for updates using:
```
$ vagrant box outdated
```

If a newer version is available, you can update your sandbox automatically using:
```
$ vagrant box update
```

## Documentation and Support
Read the [API documentation](http://ydk.cisco.com/py/docs/) for details on how to use the API and specific models.  For support, join the [YDK community](https://communities.cisco.com/community/developer/ydk) to connect with other users and with the makers of YDK
