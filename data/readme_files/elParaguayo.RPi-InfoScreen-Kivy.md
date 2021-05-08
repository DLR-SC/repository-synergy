**Note: This project is no longer active development/maintenance so issues/pull requests may never get answered!**

RPI-Info-Screen
===============

Updated version of information screen. This branch is designed to work on the
official Raspberry Pi display and so currently has a hard-coded resolution and also relies
on touch screen for transition between screens.

Installation
------------

First off, you need to install Kivy. I used the instructions [here](https://github.com/mrichardson23/rpi-kivy-screen/blob/master/README.md). Make sure you see them through, in particular the comment about making sure Kivy recognises the touch screen (you may need to run Kivy once to create the ini file).

Two common dependencies for the screens are "[requests](https://www.raspberrypi.org/forums/viewtopic.php?f=91&t=79312#p563361)" and "[BeautifulSoup](https://www.howtoinstall.co/en/debian/wheezy/main/python-beautifulsoup/)" so you should install these too (see links).

I'd recommend using git to clone the repository but you can just downloan the zip file and extract to a location of your choice.

Unless you've got a good reason (e.g. testing new features) you should stick to the "Master" branch.

Configuration
-------------

Once you've downloaded (and extracted) the code you'll need to configure the screens.

Each screen (in the "screens" folder) should have a conf.json file and a README which explains how to configure the screen for your needs.

You can disable screens by changing the "enabled" parameter to "false" (without quotation marks).

Running
-------

I'd recommend testing the script before havng it start when your pi boots. So just run

First make the file executable (if it isn't already).

`chmod +x main.py`

Now just run the file by typing

`./main.py`

If there are any errors with your screens, these should be indicated on the screen when you run it (this screen only displays on loading the software, once you browse away it won't be visible again). If you've got any unmet dependencies then you should exit (ctrl+c) and install these.

Navigating screens
------------------

Navigation should be very straightforward, just touch the right or left edges of the screens to move to the next or previous screens.

Where screens have multiple views (e.g. weather forecast for more than one location) then these are found by touching the top or bottom edges of the screen.

Start on Boot
-------------

If it's all working well and you want it to run when you boot your screen then you need to set up the init.d script.

First, edit the infoscreen file and make sure the path to the script is correct.

Next, move the screen to the init.d folder and make it executable.

`sudo mv infoscreen /etc/init.d/`

`sudo chmod +x /etc/init.d/infoscreen`

And then, to install the script, run the following command:

`sudo update-rc.d infoscreen defaults`

Bug reporting
-------------

Bugs can be reported in one of two locations:

1) The [Github issues page](https://github.com/elParaguayo/RPi-InfoScreen-Kivy/issues); or

2) The [project thread](https://www.raspberrypi.org/forums/viewtopic.php?f=41&t=121392) on the Raspberry Pi forum.

Feature requests
----------------

Feature requests are very welcome and should be posted in either of the locations in the "Bug reporting" section.
