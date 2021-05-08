# Raspberry Pi Stranger Things Wall

This is set up to get around university wifi restrictions by hosting the server separately. 

**[If you want to run everything on the Pi, use this repo instead](https://github.com/CalebKussmaul/Stranger-Things-Integrated)**

#### In this GIT repo 

* **/website**: (optional) A simple HTML page with a form to send messages to the server
* **/server**: A flask server to recieve and hold messages, also includes the functionally of /website so you can just point your domain to this
* **/client**: A raspberry pi client to periodically poll the server for messages and display them on your wall

#### You will need

1. A second computer on a network that allows incoming traffic with python 2 installed
2. Raspberry pi - any model should work. [Zero W](https://www.adafruit.com/product/3400) + [GPIO header & adapters](https://www.amazon.com/dp/B075K7MG3F/) + [NOOBs](https://www.amazon.com/dp/B017JKJEAU) will be cheapest.
3. [Wifi dongle](https://www.amazon.com/gp/product/B003MTTJOY) if the pi does not have wifi chip
4. [5v Power supply](https://www.amazon.com/gp/product/B00MHV7576/) - DO NOT POWER LEDs DIRECTLY FROM THE PI
5. Breadboard and jumper wires (male/male and male/female)
6. [Level shifter](https://www.amazon.com/gp/product/B00XW2L39K/) (Reccomended, seems to work without it)
7. [WS2811 LEDs](https://www.amazon.com/gp/product/B01AG923GI/)
8. 3' x 4' posterboard, paint, command strips, clear tape

#### Server setup

1. Open terminal
2. Enter "git clone 'https://github.com/CalebKussmaul/Stranger-Things-Wall.git'"
3. Enter "cd Stranger-Things-Wall"
4. Enter "pip2 install -r server/requirements.txt"
5. Enter password and server IP into settings/settings.py
6. Enter "python2 -m server" to start the server
7. Check that it is running by going to \[your IP]:8080/stranger in a browser

#### Client setup

1. String wires on posterboard and paint letters corresponding to LEDs. Use clear tape to point the LEDs to the letters. I suggest putting the input on the 'z' end if you want to put the pi below the board. 
2. Install raspbian on pi
3. Connect pi and ws2811 LED strip to external 5v power source in parallel (see wiring below)
4. Connect LED data wire to the pi [GPIO 10](https://www.raspberrypi-spy.co.uk/wp-content/uploads/2012/06/Raspberry-Pi-GPIO-Layout-Model-B-Plus-rotated-2700x900.png) (actual pin number 19, I know it's confusing)
5. Install [rpi_ws281x library](https://github.com/jgarff/rpi_ws281x). Follow the special instructions for SPI if you're using a Pi 3.
6. From the ws2811 repo, install the [included python wrapper](https://github.com/jgarff/rpi_ws281x/tree/master/python) (run setup.py 'install' instead of 'build'). 
7. Open terminal
8. Enter "git clone 'https://github.com/CalebKussmaul/Stranger-Things-Wall.git'"
9. Enter "cd Stranger-Things-Wall/client"
10. Enter "pip2 install -r client/requirements.txt"
11. Copy settings.py from server, and in stranger.py and adjust character mapping to LEDs as necessary
12. Enter "python2 -m client" to start the client


#### Static webhost workaround

There is also an option to host the web form separately. You might use this if you have a webhost that only allows static content, and you don't want to point your domain directly at your home IP. You will still need to have the server running somewhere, and point the form action to that address. 

If you do not need this, simply point your domain to the server and the form will be accessible via http://yourdomain.com/stranger. 

#### Connecting it to the internet

If you want to allow messages from the internet, you will need to use your router to port-forward incoming traffic to your external IP to the pi's internal IP on port 80.

Note: technically the data wire takes 5v data, and the pi GPIO outputs on 3.3v. You may need to use [a level shifter](https://www.amazon.com/gp/product/B00XW2L39K/) however it seems to work fine without it for me.

#### Wiring:

![Wiring](https://i.imgur.com/Cjj0dxo.png)

but you can probably get away with this:

![Wiring without level shifter](https://i.imgur.com/Vnqq14C.png)
