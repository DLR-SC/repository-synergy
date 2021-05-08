# README for Puli

## DESCRIPTION
Puli contains code for the dispatcher (server), worker (client) as well as some utilities to submit jobs and inspect what is happening in the network.

## SYSTEM PREREQUISITES
Currently, Puli is only supported on Linux (32 or 64 bits). The packages listed below are for Red Hat based distributions. Bot the central manager and the rendernode require Python 2.x

### Central manager
The manager is the main server component, it holds the following subsystems:

* a central db
* a dispatcher daemon

#### Packages:
   * python
   * python-tornado (<= 3.0.2)
   * MySQL-python
   * python-sqlobject
   * python-requests
   * mysql-server

### Render node

A render node is installed on each machine that can start a rendering process.
It holds the following subsystems:

   * a worker daemon
   * an optional commandwatcher process when a process is currently rendering

#### Packages
   * python-tornado (<= 3.0.2)
   * python-requests
   * python-psutil


#### Puli tools

Several tools come along with OpenRenderManagement that have specific requirements.
They can be installed on a separate computer to operate the system:
   * puliquery: command line request tools
   * puliexec: simplify submission of scripts and command line
   * pulistats: set of script to trace graphs based on server statistics
   * pulistatsviewer: GUI program to trace and display graphs

#### Packages :
   * python-tornado (<= 3.0.2)
   * numpy
   * python-pygal
   * PyQt4

# INSTALLATION

## Server
The required packages can be installed on the shell:
```shell
yum install mysql mysql-server python python-devel python-tornado MySQL-python python-sqlobject python-requests
```

alternatively you can also use a python virtual env:
```shell
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
pip install virtualenv
virtualenv puli_venv
cd puli_venv
source bin/activate
pip install tornado==3.0.2 sqlobject MySQL-python requests psutil formencode simplejson
```

### Database setup

Connect to your database:
```shell
service mysqld start
mysql -u root -p
```

Execute the following mysql commands to create the database and the dedicated user:

```sql
create database pulidb character set utf8;
create database pulistatdb character set utf8;

create user puliuser identified by 'yourpasswd';
grant all privileges on pulidb.* 
      to 'puliuser'@'localhost' 
      identified by 'yourpasswd' with grant option;

grant all privileges on pulistatdb.* 
      to 'puliuser'@'localhost' 
      identified by 'yourpasswd' with grant option;

```

### Installation and configuration
You can install Puli to wherever you like (for example `/opt/puli`) just make sure this dir is in your PYTHONPATH and all the settings are being adjusted.

```shell
cd
git checkout https://github.com/mikrosimage/OpenRenderManagement.git
mkdir /opt/puli
mkdir /opt/puli/conf
mkdir /opt/puli/logs
cp -R ~/OpenRenderManagement/Puli/src/octopus/ /opt/puli/
cp -R ~/OpenRenderManagement/Puli/scripts/ /opt/puli/
cp -R ~/OpenRenderManagement/Puli/etc/puli /opt/puli/conf/
export PYTHONPATH=/opt/puli:$PYTHONPATH
```

The settings are located in the file `/opt/puli/octopus/dispatcher/settings.py`.

Please check the following settings and adjust:
```ini
CONFDIR = /opt/puli/conf
LOGDIR = /opt/puli/logs
POOLS_BACKEND_TYPE = "file"
DB_ENABLE = True
DB_CLEAN_DATA = True
DB_URL = "mysql://puliuser:yourpasswd@127.0.0.1/pulidb"
STAT_DB_URL = "mysql://puliuser:yourpasswd@127.0.0.1/pulistatdb"
```
### First launch

To launch the dispatcher, execute the following command in a shell:

    python /opt/puli/scripts/dispatcherd.py --debug --console

Upon the first execution, Puli will create the appropriate tables in the database.

### Subsequent launches

For the following executions, change these parameters in the settings file to:

```ini
POOLS_BACKEND_TYPE = "db"
DB_ENABLE = True
DB_CLEAN_DATA = False
```
These will tell Puli to init itself with the database that was previously created, and it will enable the persistence of the jobs.

If you want to erase the database in order to have a clean start, reset these parameters to the values in the installation section.

## WORKER

While the dispatcher manages the joblist, the actual job is executed by the worker. You need at least one worker running. Workers are installed on every computer that you want to use for renderfarm needs.

Installing the worker is pretty similar to the dispatcher:

```shell
yum install python-tornado python-requests python-psutil
```

Launch:
```
export PYTHONPATH=/opt/puli:$PYTHONPATH
python /opt/puli/scripts/workerd.py --debug --console --server 192.168.1.2 --serverport 8004
```


#RELEASE NOTES
None


#KNOWN ISSUES


The model needs a bit of a refactoring. It has been designed several years ago to address some use-cases that are no longer relevant.
It can be more simple and straightforward than it is now.

Several aspects of the worker can be optimized (like the handling of status and completion update, and the interaction between the cmdwatcher and the process)


#LICENSING


Puli is distributed using the modified BSD license. Please read the "LICENSE" file for the legal wording.

Long story short, Puli is free, as well as freely modifiable and redistributable.

You may use part or all of it in your own applications, whether proprietary or open, free or commercial or not.

