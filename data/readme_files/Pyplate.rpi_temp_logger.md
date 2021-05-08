Raspberry Pi Temperature Logger
===============================

This repo contains code for a Raspberry Pi temperature logger which uses SQLite to store data read from a DS18B20 sensor.  You can see more details here:
http://raspberrywebserver.com/cgiscripting/rpi-temperature-logger/building-an-sqlite-temperature-logger.html

In webgui.py, there are several lines that contain hardcoded dates so that you can use the script with the sample database provided.  There is an equivalent version of each of these lines that uses 'now' instead of a hardcoded timestamp.  If you want to view data you've collected yourself, you should uncomment the lines that use 'now', and comment out the lines that have a hardocded date. See webgui.py, lines 45, 117, 122, 127 and 148.
