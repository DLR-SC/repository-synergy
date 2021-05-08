# **BareDroid** #

BareDroid allows for bare-metal analysis on Android devices. See the paper [here](https://www.cs.ucsb.edu/~vigna/publications/2015_ACSAC_Baredroid.pdf)

## Folders ##

**backup**: used to create a backup of the device. It is a bash script which stores a copy of:
* userdata
* system
* boot 
in the *store* partition (partition number 30). This is needed only when you want to setup a new device.

**restore**: used to restore a previous backup. It is a bash script which restore a) system, b) userdata and c) userdatanew partition.

**backup_and_restore**: used to create a backup and restore it. It is a merge of the previous scripts.

**setup_device**:
*	setup: used to setup a device. Basically, this script creates the new partitions;

---

**update**: contains the python scripts used to manage the infrastructure.
*	adb.py: provides APIs used to send command through adb shell;
*	device.py: contains information about the update_manager associated to the device (deprecated, not used in the next version);
*	analysis.py: it bridges the gap between the infrastructure and the experiments. For a detailed description see below;
*	util.py: provides utilities (deprecated);
*	manager.py: manages the command line interface;
*	updtae_manager.py: it is the core of the infrastructure. It is a separate process which manages the update and analysis process;
*	update_manager_device.py: represents a separate process used to update the device during the analysis;
*	update_manager_recovery.py: represents a separate process used to update the device during the reboot. it is used to perform a relabel of the userdata partition ( SELinux :) );

**update/config**: contains cfg and info files used to setup the python scripts.
*	config.cfg: contains the information about where to save the logs, and which scripts use to perform the analysis
*	devices.info: contains general information about the devices (e.g., user, AndroidId)

## How to backup ##
1.	connect the device
2.	run the "./script" file (the script reboots the device in recovery mode and run the script)
3.	reboot the device


## How to restore ##
1. connect the device
2. run the "./script" file (the script reboots the device in recovery mode and run the script)
3. reboot the device


## Analysis script ##
The goal of this script is to provide a wrapper between the experiment and the infrastructure, *SetupAndStart* is the main method and the only one called by the infrastructure (i.e., update_manager.py line 178). It setups the environment for the experiment (e.g., adb root) and run the experiment.
If you want to use your code in an experiment you need to:
1.	modify the config.cfg file. In the stanza 'Project' put the absolute path to the code that you want to use;
2.	create an python script containing the class used in the stanza 'class' of the config.cfg file;
3.	define a 'run' method in the config.cfg file. This is the method used by the wrapper to start the experiment.

## how to add a new device to the infrastructure ##

1.	see 'setup_device';
2.	run the backup and restore scripts;
3.	add info to the 'update/config/device.info' file (e.g., AndroidId); [mandatory]

general consideration:

4.	device -> Settings -> Storage -> USB computer connection -> disable  MTP
5.	device -> Security -> Screen lock -> None
6.	be sure you can install untrusted app (i.e., from outside the market)


## How to run an experiment ##
Architectural overview:

![alt tag](https://docs.google.com/drawings/d/1UXaQkFElMduaZckbcicz3zloDz9SOA5aap_CV0FFMhQ/pub?w=465&amp;h=259)


1.	to run an experiment you need to include the absolute path of the folder containing the samples to analyze;
2.	run the manager start script against the folder containing the apps to analyze;

example

```
./start_baredroid path/to/folder/containing/samples
```

3.	the script will prompt a command line interface which allows the user to interact with the infrastructure (e.g., start experiment);
4.	select option '2' to run the experiment;
5.	when the experiment is finished click on 'q';
6.	the results are stored in the 'update/experiment' folder.

---
*email:* simone.mutti@unibg.it
