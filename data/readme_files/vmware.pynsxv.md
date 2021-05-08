# VMware has ended active development of this project, this repository will no longer be updated.
# PyNSXv
PyNSXv is a high level python based library that exposes ready to use work-flows and a CLI tool that can be used to control VMware NSX for vSphere

PyNSXv can be used in two different ways, as a library by importing the files in the /library subdirectory into your code, or as a CLI tool by executing `pynsxv`on the command line after installation. To install PyNSXv you can use PIP on your system

### Table of Contents
**[Using PyNSXv as a CLI Tool](#Using PyNSXv as a CLI Tool)**  
**[Using PyNSXv as a Python Library](#Using PyNSXv as a Python Library)**  
**[Dependencies](#Dependencies)**   
**[Installing PyNSXv](#Installing PyNSXv)**   
**[Contributing](#Contributing)**   
**[License](#License)** 

<a name="Using PyNSXv as a CLI Tool"></a>
#Using PyNSXv as a CLI Tool

After you installed PyNSXv, the first thing you have to do is to create your a `ini` file that contains the host names and credentials of your vCenter and NSX Manager. 

If you have multiple NSX environments, you can create multiple `ini` files and reference to them using the `-i` command line option. By default PyNSXv will look for a file called `nsx.ini` in the path your are running the pynsxv command in.

The `ini` file has the following format:
```ini
# [nsxraml]
# nsxraml_file = <>
# Uncomment the above section and add the path to the raml spec you want to use instead of the bundled version

[nsxv]
nsx_manager = <nsx_manager_IP>
nsx_username = admin
nsx_password = <nsx_manager_password>

[vcenter]
vcenter = <VC_IP_or_Hostname>
vcenter_user = administrator@domain.local
vcenter_passwd = <vc_password>

[defaults]
transport_zone = <transport_zone_name>
datacenter_name = <vcenter datacenter name>
edge_datastore = <datastore name to deploy edges in>
edge_cluster = <vcenter cluster for edge gateways>
```

After placing the `nsx.ini` file in you path, you can run pynsxv from your shell or cmd prompt. On Linux and Mac simply use `pynsxv` followed by the subcommand. On Windows you will need to type `pynsxv.exe` followed by the subcommand:

```
▶ pynsxv -h
usage: pynsxv [-h] [-i INI] [-v] [-d] {lswitch,dlr,esg,dhcp,dfw,usage} ...

PyNSXv Command Line Client for NSX for vSphere

positional arguments:
  {lswitch,dlr,esg,dhcp,dfw,usage}
    lswitch             Functions for logical switches
    dlr                 Functions for distributed logical routers
    esg                 Functions for edge services gateways
    dhcp                Functions for Edge DHCP
    dfw                 Functions for distributed firewall
    usage               Functions to retrieve NSX-v usage statistics

optional arguments:
  -h, --help            show this help message and exit
  -i INI, --ini INI     nsx configuration file
  -v, --verbose         increase output verbosity
  -d, --debug           print low level debug of http transactions
```

Here is an example output using the lswitch subcommand:
```
▶ pynsxv lswitch list
+---------------------+----------------+
| LS name             | LS ID          |
|---------------------+----------------|
| edge_ls             | virtualwire-63 |
| dlr_ls              | virtualwire-64 |
+---------------------+----------------+
```

Each subcommand has its own set of subcommands, as well as arguments.  
You can see what is available by using `-h` after the first subcommand:
```
▶ pynsxv lswitch -h
usage: cli.py lswitch [-h] [-t TRANSPORT_ZONE] [-n NAME] command

Functions for logical switches

positional arguments:
  command
                            create: create a new logical switch
                            read:   return the virtual wire id of a logical switch
                            delete: delete a logical switch"
                            list:   return a list of all logical switches


optional arguments:
  -h, --help            show this help message and exit
  -t TRANSPORT_ZONE, --transport_zone TRANSPORT_ZONE
                        nsx transport zone
  -n NAME, --name NAME  logical switch name, needed for create, read and delete
```


You can also use the `-v` switch of the main pynsxv command to switch to a json formated output for use with shell scripts

<a name="Using PyNSXv as a Python Library"></a>
#Using PyNSXv as a Python Library

When using PyNSXv as a Python library you can either download the individual modules in `/library` of this repo and import them in your code, or you can install PyNSXv and import the modules from your python path for pip installed modules.   

To use the modules you will also need to have at least the `nsxramlclient` installed (https://github.com/vmware/nsxramlclient).  
You will also need a copy of the latest RAML API Spec of NSX for vSphere (https://github.com/vmware/nsxraml).

Import the module you want to use, as well as the NsxClient Class of the `nsxramlclient`.  
Then instantiate a session object of the NsxClient Class, and pass this session object to the function you want to use out of the module imported from PyNSXv. Here's an example:

```ipython
▶ ipython
Python 2.7.11 (default, Jun 17 2016, 20:01:51)
Type "copyright", "credits" or "license" for more information.

IPython 4.2.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: from pynsxv.library.nsx_logical_switch import logical_switch_list,logical_switch_create

In [2]: from nsxramlclient.client import NsxClient

In [3]: nsxraml_file = '/raml/nsxraml/nsxvapi.raml'
In [4]: nsxmanager = 'nsxmanager.invalid.org'
In [5]: nsx_username = 'admin'
In [6]: nsx_password = 'vmware'

In [7]: client_session = NsxClient(nsxraml_file, nsxmanager, nsx_username, nsx_password)

In [8]: lswitch_list = logical_switch_list(client_session)

In [9]: lswitch_list
Out[9]:
([('k8s-dlr-plr-transit', 'virtualwire-39'),
  ('k8s-minion-1', 'virtualwire-40'),
  ('k8s-minion-2', 'virtualwire-41'),
  ('vic-external', 'virtualwire-51'),
  ('vic-container-net1', 'virtualwire-52'),
  ('edge_ls', 'virtualwire-63'),
  ('dlr_ls', 'virtualwire-64')],
 [{'clientHandle': None,
   'controlPlaneMode': 'HYBRID_MODE',
   'ctrlLsUuid': 'e0c72e20-f39e-41ba-adb4-f0b191521c0c',
   'description': None,
   'extendedAttributes': None,
   'guestVlanAllowed': 'false',
   'isUniversal': 'false',

   .... Output truncated ....

In [10]: new_lswitch = logical_switch_create(client_session, 'TZ1', 'new_lswitch_name')

In [11]: new_lswitch
Out[12]: ('virtualwire-65', '/api/2.0/vdn/virtualwires/virtualwire-65')
```

All module function have inline documentation available to guide you through the needed parameters:

```
In [1]: help(logical_switch_list)

logical_switch_list(client_session)
    This function returns all logical switches found in NSX
    :param client_session: An instance of an NsxClient Session
    :return: returns a tuple, the first item is a list of tuples with item 0 containing the LS Name as string
             and item 1 containing the LS id as string. The second item contains a list of dictionaries containing
             all logical switch details
```

<a name="Dependencies"></a>
#Dependencies
PyNSXv has the following dependencies:
- pyvmomi (https://github.com/vmware/pyvmomi)
- nsxramlclient (https://github.com/vmware/nsxramlclient)
- tabulate (https://bitbucket.org/astanin/python-tabulate)

Please check the installation instructions of these projects if you run into installation issues

<a name="Installing PyNSXv"></a>
#Installing PyNSXv

PyNSXv can be installed using pip:
```shell
pip install pynsxv
```
  
**[Installing PyNSXv on Ubuntu](#Installing PyNSXv on Ubuntu)**   
**[Installing PyNSXv on a MAC](#Installing PyNSXv on a MAC)**  
**[Installing PyNSXv on Windows](#Installing PyNSXv on Windows)**    
**[Various caveats](#Various caveats)**   

<a name="Installing PyNSXv on Ubuntu"></a>
#Installing PyNSXv on Ubuntu

First update/upgrade using apt and install the python-openssl, libxml and libxslt dependencies of the `nsxramclient` using apt. Please also consult the Github page of the `nsxramclient` and `pyvmomi` in case you run into issues during the installation of these dependencies.

```shell
apt-get update && apt-get upgrade -y
apt-get install libssl-dev libffi-dev libxml2-dev libxslt-dev python-dev zlib1g-dev python-pip -y
```

After this you can simply install PyNSXv using pip:

```shell
sudo pip install pynsxv
```

<a name="Installing PyNSXv on a MAC"></a>
#Installing PyNSXv on a MAC

Make sure to install XCODE and its Command Line utilities:
https://itunes.apple.com/app/xcode/id497799835?mt=12 

```shell
xcode-select --install
```
If not yet present on your system, install python pip. The instructions on how to do so can be found here: https://pip.pypa.io/en/latest/installing/#install-or-upgrade-pip 
```shell
curl https://bootstrap.pypa.io/get-pip.py > get-pip.py
sudo python get-pip.py
```
If you don't have it yet, install homebrew on your system: http://brew.sh 
```shell
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
Now install some of the xml formating dependencies needed by PyNSXv and the underlying nsxramlclient
```shell
brew install libxml2
brew install libxslt
brew link libxml2 --force
brew link libxslt --force
```

Finaly we are ready to install PyNSXv using pip:
```shell
sudo pip install pynsxv
```

**NOTE**: OSX 10.11 El Capitan introduces problems due to an outdated dependency `six`. Due to OSX's new System Integrity Protection (SIP) pip cannot remove the outdated version and install the needed one:
http://apple.stackexchange.com/questions/209572/how-to-use-pip-after-the-os-x-el-capitan-upgrade/210021#210021
http://stackoverflow.com/questions/31900008/oserror-errno-1-operation-not-permitted-when-installing-scrapy-in-osx-10-11

If you run into this error:

`OSError: [Errno 1] Operation not permitted: '/tmp/pip-nIfswi-uninstall/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/six-1.4.1-py2.7.egg-info'` 

You should install a new non-bundled python version:
```shell
brew install python

sudo pip uninstall pynsxv
sudo pip uninstall six
sudo pip uninstall PyYAML
sudo pip uninstall pyraml-parser
sudo pip uninstall nsxramlclient

pip install pyopenssl
pip install pynsxv
```

<a name="Installing PyNSXv on Windows"></a>
#Installing PyNSXv on Windows

Install python 2.x on your Windows (https://www.python.org/downloads/). *Note: Attention do NOT install python 3.x.*

Add python installation folder in the Windows path to be able to run the pynsxv CLI from any folder (Under "Control Panel – Environment Variables", edit the System Variable "Path", and add the "Python27\Scripts" folder).

Install of pynsxv.
```
C:\>pip install pynsxv
```

You can find more details in the /docs folder [Windows Installation Details](docs/Install%20pynsxv-v1.0.pdf)

<a name="Various caveats"></a>
#Various caveats

Should you see this warning message:
`UserWarning: /home/vagrant/.python-eggs is writable by group/others and vulnerable to attack when used with get_resource_filename. Consider a more secure location (set with .set_extraction_path or the PYTHON_EGG_CACHE environment variable).`

You can solve this by changing the permissions of the .python-eggs folder:
```shell
chmod g-wx,o-wx ~/.python-eggs
```

<a name="Contributing"></a>
#Contributing

Everyone is more than welcome to contribute to PyNSXv. If you come up with any interesting additional subcommand, workflow, bugfix that you would like to share, you can simply send us a pull request. Should you be interested in helping us coding missing functionality, you can see what we are tracking as enhancements in the Github Issue tracker of this repository.
Before sending us your pull request, please make sure that you pull the latest code from the `devel` branch, and base your additions from this branch. Also note that you might be requested to sign a Contributor License Agreement before we can merge your code. This happens automatically when you submit your first pull request.

If you don't want to code, we still very much welcome any help with testing and requests for additional functionality. Please don't hesitate to contact us and open tickets in the Github Issue tracker if you need help using PyNSXv.

<a name="License"></a>
#License

Licensed under the X11 (MIT)license (the “License”) set forth below; you may not use this file except in compliance with the License. 

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an “AS IS” BASIS, without warranties or conditions of any kind, EITHER EXPRESS OR IMPLIED. See the License for the specific language governing permissions and limitations under the License.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
