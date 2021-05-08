pyFosControl
============

Python interface to Foscam CGI API for HD models

Introduction
------------

The Foscam cameras can be controlled via a web interface.  There are browser plugins available for Firefox,
Chrome and IE, which are bundled with the camera firmware and can be downloaded using the cameras web interface.

However, these plugins are Windows only.  Without them only a few basic configuration options are available (network,
user accounts, firewall, etc.).  The bulk of the functionality including the display of the camera pictures,
controlling the ptz movements, motion detection, are not available on a Linux computer.

There is a [SDK](http://foscam.us/forum/cgi-sdk-for-hd-camera-t6045.html#p28979 "SDK for HD cameras") available
describing a CGI interface which seems to make most of these functions available. pyFosControl is intended as an
python interface.

Getting started
---------------

Create a new `cam.cfg` file using `cam.cfg.example` as template.

Run `camtest.py` from the command line to get some basic information (like model info, firmware and hardware version).

Please note
-----------

* This interface is far from complete.
* It's *mostly* tested on a FI9821W V2.
* The SDK documentation is inaccurate in places.
* The non HD cameras use a different set of CGI commands and are not covered in this implementation.
* The behaviour of the camera changes slightly with each new firmware version.  Please include model and firmware version when sending bug reports (run `camtest.py` from the command line).

Certificate checking
-------------------

Since version 2.7.9 Python is checking certificates used in https connections.

This works fine with most sites on the internet because their certificates are signed by major
certificate authorities and Python has the means to verify their signatures.

However, most cameras use self-signed certificates which will fail this check and throw an exception. 

The certificate checking is controlled by the parameter `context.` See `camtest.py` for an example.
This [blog entry](http://tuxpool.blogspot.de/2016/05/accessing-servers-with-self-signed.html) shows how to create a context that fits your camera.

Unfortunately the `context` parameter was first added in Python 3.4.3. Between Python 2.7.9 and 3.4.3 
you either have to refrain from using https with self-signed certs or you have to tweak your system 
(i.e. install the camera certificate yourself in the system, change the host file, etc) so that the check is 
successful without using `context`.    
