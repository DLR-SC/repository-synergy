VirusTotal Maltego Transforms
=======
@author: Steven Weinstein  
@dayjob: Malware Researcher @ Lookingglass (lgscout.com)  

Copyright (c) 2014, Lookingglass Cyber Solutions, Inc. This file is subject to the terms and conditions of the BSD License. See the file LICENSE in the main directory for details.

1. Scope
-
This document describes each Maltego transform designed to use the VirusTotal Private API. Also included are instructions to set up Python 2.7.x and the Requests library, which are prerequisites to using the Maltego transforms. The Maltego transforms are able to run on any platform that runs Maltego and Python. The configuration file provided has been set up using Windows, and requires changes to be run on other operating systems.

<br>
2. Prerequisites: Python + Requests Library
-
In order to use the VirusTotal Maltego transforms, you must first install Python 2.7.x. If not already installed, please visit the following page for downloads and installation documentation:<br>

[https://www.python.org/downloads/](https://www.python.org/downloads/)  
Python 2.7.x License: [https://docs.python.org/2/license.html](https://docs.python.org/2/license.html)<br>


<b>Note: It will be helpful for later steps to install Python to: C:\Python27\ if you are using Windows. </b>


Once Python is installed, install the Requests library, which is an HTTP library for Python. These transforms have been created and tested successfully with Requests version 2.2. Please visit the following page for installation instructions:

[http://docs.python-requests.org/en/latest/user/install/#install](http://docs.python-requests.org/en/latest/user/install/#install)  
Requests License: [http://docs.python-requests.org/en/latest/user/intro/#apache2](http://docs.python-requests.org/en/latest/user/intro/#apache2)
<br>
3. Maltego Transform Setup
-
After the above steps have been taken to set up Python 2.7.x and the Requests library, you **must** add your API key to VTtransforms.py on line 45. You then need to put the following files into a new directory, which will become your working directory within Maltego (in the instructions below, we use the directory structure of “Maltego\Transforms”): <br>

* VTtransforms.py 
* MaltegoClass.py  
<br>


4. Maltego Transform Configuration
-
In order to use the transforms, you must import the Maltego configuration file, which is available for download here, called “vt_config_external_3.4_mmddyy” or "vt_config_external_carbon_mmddyy". This file contains the references to the transforms as well as the entities they use. You must download the configuration file for the version of Maltego which you use. If you still use Maltego 3.4.x, download the configuration file with "3.4" in it. Maltego Carbon (3.5.x) configurations are not able to be loaded in version 3.4.x. 

To import this file, open Maltego and click the Maltego “orb”, then “Import”, and then “Import Configuration”. Select the VT config file (appropriate to which version of Maltego you run), and finish the import wizard. The transforms, transform set, and entities should now all be imported. The transforms should show up in the right click -> “Run Transform” -> “VirusTotal” transform set menu. However, in order for them to run properly, you need to change the working directory (which you created in the above section) by completing the below step. 

To change the working directory, open the “Manage” tab, and click the “Manage Transforms” button. For each transform (transform names are found below in section 3.2), you must change the working directory listed to the <b>full path</b> of your working directory. 

Depending on what operating system you are using and where you installed Python, you may have to change the "Command line" transform input for each transform within the Manage Transforms window as well. The current configuration uses Python in C:\Python27\python.exe. If you installed Python elsewhere, change that transform input to the proper location.  
<br>

5. Transforms
-
The following transforms have been created for the VirusTotal transform set: 
 
1. **iocToHash**  - A transform that will return all SHA256 hashes of malware containing the Indicator of Compromise (behavioral analysis artifacts including IP addresses or domains, strings, registry keys, mutexes, file names, commands run, etc).  
	
	Required Maltego entity input: IOC  
	Maltego entity output: Hash

	
2. **hashToIP** - A transform that will return all IPv4 addresses which a given SHA256 hash of malware communicates with. 

	Required Maltego entity input: Hash  
	Maltego entity output: IPv4 Address

3. **hashToDomain** - A transform that will return all domains that a given SHA256 hash of malware communicates with.  

	Required Maltego entity input: Hash  
	Maltego entity output: Domain
	

4. **hashToURL** - A transform that will return all URLs that a given SHA256 hash of malware makes requests to (full request path on domains or IP addresses). Note: the output of this transform is of entity type "Domain", not "URL".  

	Required Maltego entity input: Hash  
	Maltego entity output: Domain

5. **ipToCommunicatingHash** - A transform that will return all SHA256 hashes of malware that have communicated with a given IP address.

	Required Maltego entity input: IPv4 address  
	Maltego entity output: Hash  

	
6. **domainToCommunicatingHash** - A transform that will return all SHA256 hashes of malware that have communicated with a given domain.  
	
	Required Maltego entity input: Domain  
	Maltego entity output: Hash

7. **domainToDownloadedHash** - A transform that will return all SHA256 hashes of malware that have been downloaded from a given domain.  

	Required Maltego entity input: Domain  
	Maltego entity output: Hash
	

8. **ipToDownloadedHash** - A transform that will return all SHA256 hashes of malware that have been downloaded from a given IP address.  

	Required Maltego entity input: IPv4 address  
	Maltego entity output: Hash

9. **domainToIP** - A transform that will return all IP addresses which a given domain has resolved to, based on passive DNS history.  

	Required Maltego entity input: Domain  
	Maltego entity output: IPv4 address

10. **ipToDomain** - A transform that will return all domains that have resolved to a given IP address based on passive DNS history.  

	Required Maltego entity input: IPv4 address  
	Maltego entity output: Domain

11. **hashToThreat** - A transform that will return the threat associated with a given SHA256 hash of Malware. Note: This transform is configured to return the Microsoft threat detection for each hash. If Microsoft has no detection, it checks TrendMicro, then Kaspersky, then Sophos are checked until a threat detection is found (only from those four choices). This transform can be customized to return the threat detections from the AV company of your choice.  

	Required Maltego entity input: Hash  
	Maltego entity output: Threat

12. **threatToHash** - A transform that will return all hashes that have been detected as a given threat. Note: This query is not specific to any AV company.  

	Required Maltego entity input: Threat  
	Maltego entity output: Hash

13. **hashToRegKey** - A transform that will return all registry keys associated with the behavior of a given SHA256 hash of malware.  

	Required Maltego entity input: Hash  
	Maltego entity output: IOC

14. **hashToBehavioralFileName** - A transform that will return all file names (and full paths) associated with the behavior of a given SHA256 hash of malware.  

	Required Maltego entity input: Hash  
	Maltego entity output: IOC


15. **hashToMutex** - A transform that will return all mutexes associated with the behavior of a given SHA256 hash of malware.  

	Required Maltego entity input: Hash  
	Maltego entity output: IOC


16. **hashToCommandRun** - A transform that will return all commands run via the CreateProcessInternalW API call made by a given SHA256 hash of malware.  

	Required Maltego entity input: Hash  
	Maltego entity output: IOC
	
17. **hashToDetectionRatio** - A transform that will return the detection ratio for a given SHA256 hash of malware.  

	Required Maltego entity input: Hash  
	Maltego entity output: Phrase

18. **hashToPositiveAVList** - A transform that will return all AV companies which have detected a given SHA256 hash of malware.  

	Required Maltego entity input: Hash  
	Maltego entity output: AV Company

19. **hashToScanDate** - A transform that will return the scan date and time for a given SHA256 hash of malware.  

	Required Maltego entity input: Hash  
	Maltego entity output: Phrase

20. **hashToRescan** - A transform that will rescan a given SHA256 hash of malware on VirusTotal. Note: Scans requested via the API are lower priority and can take several hours.  

	Required Maltego entity input: Hash  
	Maltego entity output: Phrase (confirmation that scan is queued)

21. **partialURLtoDownloadedHash** - A transform that will return all SHA256 hashes of malware which have been downloaded from a URL which has contains the given string. Note: VirusTotal is currently unable to handle a string which contains '&'.  

	Required Maltego entity input: IOC  
	Maltego entity output: Hash

22. **peSectionMD5toHash** - A transform that will return all SHA256 hashes of malware that have the given MD5 hash as a PE section. Note: The input must be in the IOC entity form.  

	Required Maltego entity input: IOC  
	Maltego entity output: Hash


23. **importHashToHash** - A transform that will all SHA256 hashes of malware that have the given import hash. Note: The input must be in the IOC entity form.  

	Required Maltego entity input: IOC  
	Maltego entity output: Hash

24. **exploitToHash** - A transform that will return all SHA256 hashes of malware that are tagged as the given exploit in CVE format (e.g, CVE-2014-1776).  

	Required Maltego entity input: Threat  
	Maltego entity output: Hash
	
25. **urlToDetectionRatio** - A transform that will return the detection ratio for a given URL. Note: The input must be in the Domain entity form.  

	Required Maltego entity input: Domain  
	Maltego entity output: Phrase

26. **urlToScan** - A transform that will scan a given URL. Note: Scans requested via the API are lower priority and can take several hours. The input must be in the Domain entity form.  

	Required Maltego entity input: Domain  
	Maltego entity output: Phrase (confirmation that scan is queued)
