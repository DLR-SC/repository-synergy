Introduction
============
A pure-Python library that can read and write Password Safe v3 
files. It includes full support for almost all current Password
Safe v3 database headers and record headers. 

History
=======
The library was initially written by Paulson McIntyre for
Symantec in 2009. It was later released by Symantec under the 
GPLv2 in 2011. Changes and updates have been made since by Paulson
McIntyre (GpMidi), Evan Deaubl (evandeaubl), and Sean Perry (shaleh).
Rony Shapiro maintains the project page and acts as gate keeper
for new patches.   

Known Issues
============ 
 1. Lack of documentation
 2. Unit tests are out-of-date
 3. There MAY be an issue with the order that NonDefaultPrefsHeader serializes preferences for HMAC validation in pypwsafe. Although the library validates HMACs fine at the moment, so who knows. 
 4. The version of python-mcrypt for Windows isn't compatible with this library. As a result, the pypwsafe library doesn't work in Windows. If anyone is able to get around this, please notify us. The library has not been tried under Cygwin.    
	 
Dependencies
============
 1. python-mcrypt
 2. hashlib OR pycrypto

Install Instructions
====================

RHEL/CentOS
-----------
 1. Install libmcrypt and it's dev package along with the Python dev package: 
	yum install libmcrypt-devel libmcrypt python-devel
	These packages are needed by the installer for python-mcrypt
 2. Install the standard Linux development tools. For RHEL/CentOS 5 and 6, `yum groupinstall 'Development tools'` can be used if your YUM repos have group information. 
 3. Use Pip or easy install to install python-mcrypt, hashlib, and pycrypto
 4. Run the setup script
	python setup.py install
 5. Test that the module loads
	python -c "import pypwsafe"

Windows
-------
Windows is not currently supported due to issues with python-mcrypt. A
pure-Python Twofish implementation will allow future support, if a bit
slower than a C-based implementation. 
	
Development Setup Instructions
------------------------------
FIXME: Fill this in

FAQ
===
### Why mcrypt and not use PyCrypto?
The pyCrypto library doesn't support TwoFish, which is a newer cipher based on Blowfish. Twofish is required to encrypt/decrypt Password Safe v3 files.  

### Where can I find details on the Password Safe file format?
The format spec is kept in the Password Safe project's SVN repo. Go 
to the password safe code base and check in /pwsafe/pwsafe/docs/formatV3.txt.
As of today, it can be found [here](http://sourceforge.net/p/passwordsafe/code/5210/tree/trunk/pwsafe/pwsafe/docs/) 
	
TODO
====
 1. Add support for using a pure-python TwoFish algorithm if mcrypt doesn't work.
    http://code.google.com/p/python-keysafe/source/browse/crypto/twofish.py
    http://www.bjrn.se/code/twofishpy.txt 
 2. Need to update against the latest version of the official psafe format v3 doc.
