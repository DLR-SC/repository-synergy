Raspberry Pi Photobooth Project
=====================

Here is my blog post with full instructions, pictures and a circuit diagram:

http://contractorwolf.com/raspberry-pi-high-def-photobooth/

This photobooth needs a folder called "/images" in the same path as the photobooth.py file, my version also has 4 buttons connected from a 315mhx receiver to operate.  Since the 315mhz outputs 5v and the RPI can only take 3v I have the lines running through 4 optoisolators and only the 3v from the RPi are run into the optoisolators.

You must also have PyGame and GPhoto2 installed at the minimum, and my full notes (sorry, they are rough) are here:

This project aim to replicate the functionality of a photobooth screen with the hardware of a Raspberry Pi and some other custom parts for wireless control and updating the cameras usage based on whether a person is standing in front of the screen or not.

The basic functionality will be the same as shown in this project:

http://www.youtube.com/watch?v=jiQrpruA4-E

Except the netbook running windows XP (to use the Canon SDK) and Arduino (for wireless control and PIR input) used in this video will be replaced with a single Raspberry Pi that will both listen for incoming wireless control and an onboard PIR sensor.  One USB is used to send commands to the camera over USB and one for the Wifi. 

The project has several functions that must be controlled by the Raspberry Pi:
connection to an HDMI monitor (or HDTV) to display the slideshow of images stored on the device as well as any photos that have already been taken.
listening to the wireless button controller to operate the cameras “capture image” functionality as well as controlling the slideshow (prev, next, show last, etc).
listening to the PIR sensor to control the cameras open and close lens functions, as well as turning the software from running as a photobooth to a slideshow only.  This is to protect the camera and save battery as well as hide the photobooth functionality until there are people to capture in images.

Cameras that work with gphoto2:

http://www.gphoto.org/proj/libgphoto2/support.php


PROCESS


Links:

Download Raspian

http://www.raspberrypi.org/downloads

Use WinDiskImager to flash the SD card with the disk image (.img file):

http://sourceforge.net/projects/win32diskimager/

Update/Upgrade

sudo apt-get update

sudo apt-get upgrade


Install GPhoto2

sudo apt-get install gphoto2

ISSUE: gphoto2 could not lock the device camera is already in use, app starts but shows last photo, doesnt stream
SOLUTION: pkill gvfs

http://gphoto-software.10949.n7.nabble.com/Nikon-D800-Camera-is-already-in-use-td13616.html


Update Gphoto2 to the latest version (currently 2.5.2)

https://github.com/gonzalo/gphoto2-updater


$sudo ./gphoto2-updater.sh

(for some reason their page doesn’t have the “./” but it errored when i didn’t use that specific path. even running it from inside that same folder, linux is weird

The updater basically solves all previous issues that I had previously with the RPi and gphoto2.  The camera no doesnt close after taking pictures, it remains in its ready state.


Install VSFTP

http://www.instantsupportsite.com/self-help/raspberry-pi/raspberry-install-ftp/

Install Adafruit GPIO Library

http://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/adafruit-pi-code

sudo apt-get install git

git clone http://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code.git

Install the Python GPIO libraries for accessing the pins in python

sudo apt-get install python-dev

sudo apt-get install python-rpi.gpio


Uploading to Google Drive (untested)

https://developers.google.com/drive/web/quickstart/quickstart-python

IMPORTANT: 

sudo apt-get install python-setuptools

(installs easy_install, and other tools)

sudo easy_install --upgrade google-api-python-client

(needs first step to install east_install to run second step)

------------------------------------------------
ADDITIONAL NOTES AND LINKS TO OTHER USEFUL PAGES BELOW
------------------------------------------------

To do:

CAPTURE

1) take a picture using capture-image-and-download

(done)

2) use capture-movie to capture stream of images 

status: the camera will capture-movie which stores the mjpg stream, but when trying to use that file in pygame it seems to only grab the first file and then reuse that file instead of grabbing it over and over.  this may just be a caching issue in pygame and there might be a way around it.

other ideas:

3) display stream from capture-movie


CONTROL

1) use pygame button to take a picture

2) connect 4 button wireless controller to raspberry pi GPIO 

3) take picture with the wireless controller (done)

4) show slideshow with images stored on the RPi (done)

5) flip between images using the wireless controller (done)







usage of capture-movie converting to a jpeg on the fly, try this

https://github.com/damyon/picam/blob/master/picam/gphoto2.py

gphoto2 --capture-movie --stdout | avconv -f mjpeg -timelimit 60 -i pipe:0 -vsync 1 -r 1 /var/lib/picam/preview/preview%02d.jpg

uses “avconv”


Use mplayer to show mjpg streams:

sudo apt-get install mplayer

gphoto2 --stdout --capture-movie | someotherprogram

gphoto2 --capture-movie --stdout>>/dev/fakevideo1


RESEARCH LINKS

virtual video device:

http://stackoverflow.com/questions/18011304/how-to-make-a-virtual-video-device-for-testing-and-debugging-which-has-dev-vide

creating a virtual video device:

http://moozing.wordpress.com/2011/12/26/ip-camera-gstreamer-and-virtual-video-devices/

using pygame camera module:

http://www.pygame.org/docs/tut/camera/CameraIntro.html


my post on nabble (gphoto):

http://gphoto-software.10949.n7.nabble.com/capture-preview-VS-liveview-on-gphoto-2-5-2-td13957.html#a13964

mjpg streaming on the rpi

http://blog.miguelgrinberg.com/post/how-to-build-and-run-mjpg-streamer-on-the-raspberry-pi


ffserver -f /etc/ffserver.conf | gphoto2 --stdout --capture-movie | ffmpeg -f mjpeg -r 2 -i - http://localhost:81/canon.ffm

I have found you need to set the permissions right:

i have made a new directory: /usr/local/www

sudo chmod 755 /usr/local/www

sudo chmod 644 /usr/local/www/*
mjpg_streamer -i "input_uvc.so -d /dev/video0" -o "output_http.so -p 8080 -w /usr/local/www"



FULL API C++ APP

https://github.com/scheckmedia/CameraControllerApi

