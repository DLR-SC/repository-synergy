LibraryBox 2.0 Core script files.

Join the chat at https://gitter.im/LibraryBox-Dev/LibraryBox-core


Matthias Strubel 2013-07-24  matthias.strubel@aod-rpg.de
This sourcecode is licenced under GPL-3


Preparation of the core scripts for LibraryBox on RapsberryPI and OpenWRT.
The Scripts are designed for reusing and modificate only the base Piratebox Scripts instead of being a HARD fork from PBx.

To achieve this, LibraryBox uses the hook implementation (preprepared empty scripts for you own code) and exchanges a few files, if needed.


The workflow for creating the final source package is:

  - clone this project
  - do your modification in the "customization" folder
  - run the following command, which results the final "compilation" of all scripts into the directory "build" (changes made during build, see below)
    make build
  - To create an script package
     # OpenWRT imagefile:  make image
     # Script package   :  make targz
     # all together     :  make all

  - To cleanup your build environment:
     make clean


Folders
-------

  customization    =  All stuff which should be copied over

  customization/www_librarybox  ==> Replaces the normal www folder of piratebox
  					Contains internet detection
					Shoutbox Scripts
					(...) see below
  customization/www_content     ==> is moved to opt/piratebox/share/Content
  					Located on USB Stick
					Contains all the presentational stuff
					Contains presentation Templates for Statistic-Views

  customization/www_content/dir-images ==> Icons displayed on directory listing; file-Types
  						icons by famfamfam

  piratebox_origin =  git subtree of PirateBoxScripts_Webserver branch "librarybox_dev"  (see git subtree"
                      Normally you would choose some stable release, but because of LibraryBox is leapfrogging PirateBox I need to base on special branch to able to push changes back and other way around. This can be later changed to "stable" branch
  tmp_img	   =  Customization for images and mount points
  build_dir	   =  Folder for including piratebox + LibraryBox stuff to a complete cake
  LibraryBox-landingpage = git subtree of LibraryBox-landingpage branch master , contains the content of www_customization and others

Changes during build
--------------------

* Place normal configuration and script hooks, which are used
* Copy a template for the librarybox.us/  stuff (internet detection and so on)
* Copy a template for the content-folder librarybox.us/content 
* Changing SSD in hostapd
* Change hostname in piratebox.conf
* Enable custom directory-listing file
* Enable PHP in lighttpd with FastCGI


New Features in www folder
--------------------------

dir-generator.php	=> 	KittyKat dir Listing with customization for counting downloads
				Download-Statistics can be turned off here

  Download-Statistics
  -------------------
    dl_statistics.conf.php	=>	Configuration file for download Statistics
    dl_statistics.func.php	=>	Function pool for getting acces to dl-stats
    dl_statistics_counter.php	=>	Called by dir-generator.php if somebody downloads something
    					Redirects after counting to direct file-url
    dl_statistics_display.php	=>	Simple view into statistics (shows deleted files too)
    						http://librarybox.us/dl_statistics_display.php

    Located in content: dl_statistics.html.php
    				=>	Templates for display

    Creates a SQLite file in /opt/piratebox/share called dl_statistics.sqlite

  Visitor-Counter
  ---------------
    vc.conf.php			=>	Configuration file for Visitor counter
    vc.func.php			=>	Function Pool for visitor counter
    vc_counter.php		=>	Displays a transparent 1x1 gif and counts visitor
    vc_display.php		=>	Simple view into statistics
    						http://librarybox.us/vc_display.php

    Located in content: vc_statistics.html.php
    				=>	Templates for display


    Creates a SQLite file in /opt/piratebox/share called /opt/piratebox/share/vc_statistics.sqlite

