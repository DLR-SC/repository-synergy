pipic
=====

Tools for Raspberry Pi photography


This repository contains scripts I am using for timelapse projects with the raspberry pi.
The important parts are:

timelapse.py:
    Takes photos at a specified interval.
    
deflicker.py:
    Touches up timelapsed photos by applying auto-levelling, brightness adjustment, and pixel averaging (if desired).


There are also some tools for getting the Pi ready to roll.

loadOut.py:
    Copy various configuration files onto a disk that will be used with the Pi.
    Also sets hostname, timezone, and does some other housekeeping.

--------------------------------------------------------------

We're also working on building a Django server for managing all your timelapse needs.  Feel free to try it out and tell us what you think!

There are a couple pre-requisites, though.   Use the python 'pip' installer to make sure you have recent versions of each.  

`sudo apt-get install python-pip`

Then:

`pip install -U django`

`pip install -U celery`

To get the Django app running, try adding the following three lines to your Pi's crontab:

`@reboot       	pi	/usr/bin/screen -dmS tlapse python /home/pi/pipic/djpilapse/manage.py runserver 192.168.0.5:8000`

`@reboot 	pi	/usr/bin/screen -dmS celery bash -c 'sleep 10; (cd /home/pi/pipic/djpilapse && exec celery -A djpilapse worker -l info )'`

`@reboot		pi	bash -c 'sleep 40; wget 192.168.0.5:8000/djpilapp/startlapse/'`

You will also need to manually set your Pi's IP address to 192.168.0.5 for ethernet.  (You can actually use any value you like; just make sure the crontab lin have amatching IP address.)  Then reboot.

You can then access the web interface in one of two ways.
a) Open a browser on the Pi and go to 192.168.0.5:8000, or
b) Set your laptop to manual IP address 192.168.0.10 (or any 192.168.0.X with X not equal to 5), connect an ethernet cable to the Pi, and then open a browser and navigate to 192.168.0.5:8000.
