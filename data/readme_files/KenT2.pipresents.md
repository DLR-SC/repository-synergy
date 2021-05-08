PI PRESENTS  - Version 1.1.2
============================

<b>IMPORTANT:</b> 26/2/2015 - [pipresents] is now two years old. [pipresents-next] is now the stable version of Pi Presents. If you are starting to use Pi Presents use [pipresents-next].

The [pipresents] github repository will not be deleted, but the code will not be fixed for changes to the supporting software. Consider upgrading to [pipresents-next] 

--------------------------------------------------------------------------------------------------------------------------

Ensure you read the Release Notes first.

Improvements from Version 1.1.1 are in changelog.txt

Pi Presents is a presentation application intended for Museums and Visitor Centres. I am involved with a couple of charity organisations that are museums or have visitor centres and have wanted a cost effective way to provide audio interpretation and slide/videoshow displays. Until the Raspberry Pi arrived buying or constructing even sound players was expensive. The Pi with its combination of Linux, GPIO and a powerful GPU is ideal for black box multi-media applications; all it needs is a program to harness its power in a way that could be used by non-programmers.

This early issue of Pi Presents offers some basic features but under the bonnet it is, I hope, a flexible modular application with simple to use editing facilities to configure it to your exact display requirements. The current features include:

*	Animation or interpretation of exhibits by triggering a sound, video, or slideshow from a PIR or button.

*	A repeating media show for a visitor centre. Images, videos, audio tracks, and messages can be displayed.

*	Allow media shows to be interrupted by the visitor and a menu of videos to be presented.

*	Showing 'Powerpoint' like presentations where progress is controlled by buttons or keyboard. The presentation may include images, text, audio tracks and videos.

*   A dynamic show capability (Liveshow) in which tracks to be played can be included and deleted while the show is running.

I have immediate plans to develop an audio player based on pulseaudio which should replace omxplayer for audio tracks and allow use of the 3.5mm jack without popping. Also the ability to asynchronously trigger a number of tracks from GPIO pins. Other ideas are animation of exhibits using GPIO outputs, synthetic speech, and display of animations using OpenGLES.

There are potentially many applications of Pi Presents and your input on real world experiences would be invaluable to me, both minor tweaks to the existing functionality and major improvements.

Licence
=======

See the licence.md file. Pi Presents is Careware to help support a small museum charity of which I am a Trustee and who are busy building themselves a larger premises https://www.facebook.com/MuseumOfTechnologyTheGreatWarWw11. Particularly if you are using Pi Presents in a profit making situation a donation would be appreciated.

Installation
============

The full manual is in the file manual.pdf. To download Pi Presents including the manual and get going follow the instructions below.

Install required applications (PIL and X Server utils)
------------------------------------------------------

         sudo apt-get update
         sudo apt-get install python-imaging
         sudo apt-get install python-imaging-tk
         sudo apt-get install x11-xserver-utils
		 sudo apt-get install unclutter

	   
Download and install pexpect
-----------------------------

Specified here http://www.noah.org/wiki/pexpect#Download_and_Installation and below.

From a terminal window open in your home directory type:

         wget http://pexpect.sourceforge.net/pexpect-2.3.tar.gz
         tar xzf pexpect-2.3.tar.gz
         cd pexpect-2.3
         sudo python ./setup.py install

Return the terminal window to the home directory.
	   
Download Pi Presents
--------------------

Pi Presents MUST be run from the LXDE desktop. From a terminal window open in your home directory type:

         wget https://github.com/KenT2/pipresents/tarball/master -O - | tar xz

There should now be a directory 'KenT2-pipresents-xxxx' in your home directory. Rename the directory to pipresents

Run Pi Presents to check the installation is successful. From a terminal window opened in the home directory type:

         python /home/pi/pipresents/pipresents.py

You will see a welcome message followed by an error message which is because you have no profiles. Exit Pi Presents using CTRL-BREAK or close the window.


Download and try an Example Profile
-----------------------------------

Warning: The download includes a 26MB video file.

Open a terminal window in your home directory and type:

         wget https://github.com/KenT2/pipresents-examples/tarball/master -O - | tar xz

There should now be a directory 'KenT2-pipresents-examples-xxxx' in your home directory. Open the directory and move the 'pp_home' directory and its contents to your home directory.

From the terminal window type:

         python /home/pi/pipresents/pipresents.py -p pp_mediashow
		 
to see a repeating multimedia show.

Now read the manual to try other examples.

Reading the Manual
==================

The manual in the pipresents directory is issued as a PDF because it was too large and unwieldy to be a text file. Raspbian has a pdf reader, mupdf, however it is somewhat limited. Raspbian will soon have the better xpdf installed as default but if its not with you yet:

         sudo apt-get install xpdf
		 

Updating Pi Presents
=====================

Open a terminal window in your home directory and type:

         wget https://github.com/KenT2/pipresents/tarball/master -O - | tar xz

There should now be a directory 'KenT2-pipresents-xxxx' in your home directory

Rename the existing pipresents directory to old-pipresents

Rename the new directory to pipresents.

Copy pp_editor.cfg from the old to new directories.

The profiles in pipresents-examples will be kept compatible with the latest version of Pi Presents. Beware, re-installing these will overwrite profiles you have made. The example profiles can be updated to be compatible with the updated version of Pi Presents by running them through the editor.

		 
Requirements
============
Pi Presents was developed on Raspbian using Python 2.7. It will run on a Rev.1 or Rev.2 Pi. On 256MB machines display of large images (.jpg etc.) will run out of RAM and crash the Pi.

I don't know the exact maximum but keep images in the 1 Megapixel range. Larger images, greater than the screen pixel size, will do nothing to improve the picture and will take longer to display even on 512MB machines.

omxplayer plays some videos using 64MB of RAM; others need 128MB, especially if you want sub-titles. 


Bug Reports and Feature Requests
================================
I am keen to develop Pi Presents further and would welcome bug reports and ideas for real world additional features and uses. 

Please use the Issues tab on Github https://github.com/KenT2/pipresents/issues or the Pi Presents thread http://www.raspberrypi.org/phpBB3/viewtopic.php?f=38&t=29397 on the Raspberry Pi forum.

