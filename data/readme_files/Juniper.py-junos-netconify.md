The repo is under active development.  If you take a clone, you are getting the latest, and perhaps not entirely stable code.

## ABOUT

Junos console/bootstrap New-Out-Of-Box (NOOB) configuration automation. 

There are times when you MUST console into a Junos device to perform the NOOB configuration.  Generally this configuration is the bare minimum in takes to:

  * set the root password
  * set the host-name
  * set the management ipaddr
  * enable ssh and optionally NETCONF

The general use-case:

Primarily this library is used as a Console driver for the Junos Ansible Modules.

The `netconify` utility can be used perform configuration by logging into the serial console and pushing a configuration file to the device.


## USAGE

````

usage: netconify [-h] [--version] [-f JUNOS_CONF_FILE] [--merge] [--qfx-node]
                 [--qfx-switch] [--zeroize] [--shutdown {poweroff,reboot}]
                 [--facts] [--srx_cluster REQUEST_SRX_CLUSTER]
                 [--srx_cluster_disable] [-S [SAVEDIR]] [--no-save] [-p PORT]
                 [-b BAUD] [-t TELNET] [ -s SSH] [--timeout TIMEOUT] [-u USER]
                 [-P PASSWD] [-k] [-a ATTEMPTS]
                 [name]

positional arguments:
  name                  name of Junos device

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  --verbose VERBOSE     increase verbose levevel: 0 = default, 1 = login
                        debug, 2 = rpc reply debug

DEVICE options:
  -f JUNOS_CONF_FILE, --file JUNOS_CONF_FILE
                        Junos configuration file
  --merge               load-merge conf file, default is overwrite
  --qfx-node            Set QFX device into "node" mode
  --qfx-switch          Set QFX device into "switch" mode
  --zeroize             ZEROIZE the device
  --shutdown {poweroff,reboot}
                        SHUTDOWN or REBOOT the device
  --facts               Gather facts and save them into SAVEDIR
  --srx_cluster REQUEST_SRX_CLUSTER
                        cluster_id,node ... Invoke cluster on SRX device and
                        reboot
  --srx_cluster_disable
                        Disable cluster mode on SRX device and reboot

DIRECTORY options:
  -S [SAVEDIR], --savedir [SAVEDIR]
                        Files are saved into this directory, $CWD by default
  --no-save             Do not save facts and inventory files

CONSOLE options:
  -p PORT, --port PORT  serial port device
  -b BAUD, --baud BAUD  serial port baud rate
  -s SSH, --ssh SSH     ssh server, <host>,<port>,<user>,<password>
  -t TELNET, --telnet TELNET
                        terminal server, <host>,<port>
  --timeout TIMEOUT     TTY connection timeout (s)

LOGIN options:
  -u USER, --user USER  login user name, defaults to "root"
  -P PASSWD, --passwd PASSWD
                        login user password, *empty* for NOOB
  -k                    prompt for user password
  -a ATTEMPTS, --attempts ATTEMPTS
                        login attempts before giving up
````

## EXAMPLE

Junos NOOB devices can netconified:

###Telnet:
````
[rsherman@py-junos-netconify bin]$ ./netconify --telnet=host,23 -f host.conf
TTY:login:connecting to TTY:host:23 ...
TTY:login:logging in ...
TTY:login:starting NETCONF
conf:loading into device ...
conf:commit ... please be patient
conf:commit completed.
TTY:logout:logging out ...
````
The above example is connecting to the host via telnet on port 23 and loading the configuration file specified.
###SSH:
````
r2600r@r2600r-mbp15 [~]netconify --facts --ssh=console-server,19876,c-user,pass123 -u user --passwd "pass123"
TTY:login:connecting to TTY:console-server:19876:c-user:pass123 ...
TTY:login:logging to device ...
TTY:login: OK ... starting NETCONF
facts:retrieving device facts...
facts:saving: ./cfwj-lab1-0011a-facts.json
inventory:saving: ./cfwj-lab1-0011a-inventory.xml
TTY:logout:logging out ...
````
The above example is connecting to the host via ssh on port 19876 and gather device facts. Additonal options such as serial connectivity and device specific functions are identified in Usage. If ssh username and password for console are omited, -u/--passwd will be used instead for both console server authetication and device authetication --ssh=console-server,19876,, -u user --passwd "pass123"


## INSTALLATION

Installation requires Python 2.6 or 2.7 and associate `pip` tool

    pip install junos-netconify
	
Installing from Git is also supported (OS must have git installed).

	To install the latest MASTER code
	pip install git+https://github.com/Juniper/py-junos-netconify.git
	-or-
	To install a specific version, branch, tag, etc.
	pip install git+https://github.com/Juniper/py-junos-netconify.git@<branch,tag,commit>
	
## UPGRADE

Upgrading has the same requirements as installation and has the same format with the addition of -UPGRADE

	pip install -U junos-netconify

## DEPENDENCIES

This has been tested with Python 2.6 and 2.7.  The required modules are defined in `setup.py`.

## LICENSE

Apache 2.0
  
## CONTRIBUTORS

  - Jeremy Schulman (@nwkautomaniac), Core developer
  - Rick Sherman (@shermdog01)
  - Patrik Bok (@r2660r)
  - Ashley Burston
