Diese Readme-Datei hat Peter Vasen ins Deutsche übersetzt. Klicken Sie hier http://www.weser-echo.de/BitteLesen.pdf

PI PRESENTS  - Version 1.2.3
============================

This repository contains the previous version of Pi Presents. This version will be supported until June 2019.

Please use Pi Presents Gapless which is the current stable version.

Upgrade instructions are in the Pi Presents Gapless repsitory in the file upgrade_1p2_1p3.txt




TO UPGRADE FROM VERSION 1.1
============================
To upgrade follow the instructions in the 'Updating Pi Presents' section below. Before doing so keep a copy of the current Pi Presents and all the profiles:


PI PRESENTS
===========
Pi Presents is a display and animation control application intended for Museums and Visitor Centres. I am involved with a couple of charity organisations that are museums or have visitor centres and have wanted a cost effective way to provide audio interpretation and slide/videoshow displays. Until the Raspberry Pi arrived buying or constructing even sound players was expensive. The Pi with its combination of Linux, GPIO and a powerful GPU is ideal for black box multi-media applications; all it needs is a program to harness its power in a way that could be used by non-programmers.

This major upgrade of Pi Presents adds in features which you kind people have suggested to me. It is now a flexible toolkit for display and animation with a large range of features. This large range of features may seem to make it complicated, hopefully not so as most of them are optional.  I have tried to keep it simple for beginners by providing an editor with templates and a set of examples for basic applications. A extensive User Manual is also provided.

Pi Presents is basically five types of show, four media players for different types of track, a GPIO output sequencer, and something to handle external inputs.  These can be combined using a simple to use editor to serve a great variety of simple or complex applications. Applications include:

*	Audio-visual interpretation of exhibits by triggering a sound, video, or slideshow from GPIO, keyboard or buttons.

*	A repeating media show for a visitor centre. Images, videos, audio tracks, and messages can be displayed. Different shows can be scheduled at specified times of day.

*	Allow media shows to be interrupted by the visitor and a menu of shows or tracks to be presented.

*	Showing 'Powerpoint' like presentations where progress is controlled by buttons or keyboard. The presentation may include images, text, audio tracks and videos.

*   Control animation of exhibits by switching GPIO outputs synchronised with the playing of tracks.

*   A dynamic show capability (Liveshow) in which tracks to be played can be included and deleted while the show is running.

* A button controlled content chooser for kiosks.

* A touchscreen system as seen in many museums.

There are potentially many applications of Pi Presents and your input on real world experiences would be invaluable to me, both minor tweaks to the existing functionality and major improvements.

Licence
=======

See the licence.md file. Pi Presents is Careware to help support a small museum charity of which I am a Trustee and who are busy building themselves a larger premises http://www.museumoftechnology.org.uk  Particularly if you are using Pi Presents in a profit making situation a donation would be appreciated.

Installation
============

The full manual in English is here https://github.com/KenT2/pipresents-next/blob/master/manual.pdf

There is a German version of the manual written by Peter Vasen ( http://www.web-echo.de/ ) you can download it here 

http://www.weser-echo.de/pipresents_manual_1_2_3_de.pdf

To download Pi Presents including the manual and get going follow the instructions below.


Install required applications (MPlayer, PIL and X Server utils)
------------------------------------------------------

         sudo apt-get update
         sudo apt-get install python-pexpect
         sudo apt-get install python-imaging
         sudo apt-get install python-imaging-tk
         sudo apt-get install x11-xserver-utils
		 sudo apt-get install unclutter
		 sudo apt-get install mplayer
		 sudo apt-get install uzbl

	   
	   
Download Pi Presents
--------------------

Pi Presents MUST use Raspbian and be run from the desktop (startx). From a terminal window open in your home directory type:

         wget https://github.com/KenT2/pipresents-next/tarball/master -O - | tar xz

There should now be a directory 'KenT2-pipresents-next-xxxx' in your home directory. Rename the directory to pipresents

Run Pi Presents to check the installation is successful. From a terminal window opened in the home directory type:

         python /home/pi/pipresents/pipresents.py

You will see a welcome message followed by an error message which is because you have no profiles. Exit Pi Presents using CTRL-BREAK or close the window.


Download and try an Example Profile
-----------------------------------

Warning: The download includes a 26MB video file.

Open a terminal window in your home directory and type:

         wget https://github.com/KenT2/pipresents-next-examples/tarball/master -O - | tar xz

There should now be a directory 'KenT2-pipresents-next-examples-xxxx' in your home directory. Open the directory and move the 'pp_home' directory and its contents to your home directory.

From the terminal window type:

         python /home/pi/pipresents/pipresents.py -p pp_mediashow_1p2
		 
to see a repeating multimedia show.

Now read the manual to try other examples.


Updating Pi Presents from Version 1.1
======================================

Open a terminal window in your home directory and type:

         wget https://github.com/KenT2/pipresents-next/tarball/master -O - | tar xz

There should now be a directory 'KenT2-pipresents-next-xxxx' in your home directory

Rename the existing pipresents directory to old-pipresents

Rename the new directory to pipresents.

Copy pp_editor.cfg from the old to new directories.


Getting examples for this version.
----------------------------------

New to this version is a github repository [pipresents-next-examples]

Rename the existing pp_home directory to old_pp_home.

Open a terminal window in your home directory and type:

         wget https://github.com/KenT2/pipresents-next-examples/tarball/master -O - | tar xz

There should now be a directory 'KenT2-pipresents-next-examples-xxxx' in your home directory.

Open the directory and move the 'pp_home' directory and its contents to your home directory.

These examples are compatible with the version of  Pi Presents you have just downloaded. In addition you can update profiles from version 1.1.x [pipresents] to 1.2.3 by simply opening them in the editor (make a backup copy first):
	  
In either case you can use the tools>update all menu option to update all profiles in /pp_home

Lastly you will need to do a little manual updating of some of the field values as specified in  ReleaseNotes.txt. Start at the paragraph in releasenotes.txt that introduces version 1.2 and work backwards.

I have started a new thread on the forum for [pipresents-next], see below.

		 
Requirements
============
Pi Presents was developed on Raspbian using Python 2.7. It will run on a Rev.1 on all versions of Pi including Pi2. On 256MB machines display of large images (.jpg etc.) will run out of RAM and crash the Pi.

I don't know the exact maximum but keep images in the 1 Megapixel range. Larger images, greater than the screen pixel size, will do nothing to improve the picture and will take longer to display even on 512MB machines.

omxplayer plays some videos using 64MB of RAM; others need 128MB, especially if you want sub-titles. 


Bug Reports and Feature Requests
================================
I am keen to develop Pi Presents further and would welcome bug reports and ideas for real world additional features and uses. [pipresents-gapless] will be in beta test soon.

Please use the Issues tab on Github https://github.com/KenT2/pipresents-next/issues or the Pi Presents thread  http://www.raspberrypi.org/phpBB3/viewtopic.php?f=38&t=39985 on the Raspberry Pi forum.

For more information on how Pi Presents is being used, Hints and Tips on how to use it and all the latest news hop over to the Pi Presents website http://pipresents.wordpress.com/

