# Synopsis

This is a very sloppy project I made myself for a Raspberry Pi-powered smart thermostat. This is by no means a polished, complete project. I would be very happy to see people forking this and creating bigger and better versions. The project consists of three parts:

1. The HVAC controller (Raspberry Pi)
2. One or more temperature sensors (Raspberry Pi)
3. Remote web interface (LAMP stack)

I purposely separated the HVAC controller from the temperature sensors because I can add more, which will give a better "average" temperature throughout my living space, but it can also look at a single sensor if desired.

# Motivation

The thermostat that came with my apartment is not very predictable. Plus, I'm lazy, and I hate having to get up out of bed to adjust the temperature. I wanted something where I could adjust it from my phone or my laptop, wherever I happen to be. Plus, I wanted to be able to specify a temperatue range that would kick on either the air conditioner or the heater.

The best stuff comes from the pursuit of everyday convienence.

# Hardware

In addition to the [Raspberry Pi's](https://www.adafruit.com/products/1914) ($40 each,) you will need some additional hardware, and know some basic knowledge about them. The main components are:

* [SainSmart 4-channel relay module](http://www.amazon.com/gp/product/B0057OC5O8/ref=oh_aui_detailpage_o00_s01?ie=UTF8&psc=1) for the HVAC controller Pi (under $10)
* [DS18B20 Digital temperature sensor](http://www.adafruit.com/product/374) for the temperature sensor Pi's ($3.95 each)
* Necessary jumper wires to connect everything 


# HVAC 101

HVAC (heating, ventilating, and air conditioning) can be implemented in different ways within a house or apartment, and varies for different countries based on the wiring and such. I'm not an expert in HVAC systems, I pretty much just learned enough to get by for this project, but here's a pretty useful guide: [http://wiki.xtronics.com/index.php/Thermostat_signals_and_wiring](http://wiki.xtronics.com/index.php/Thermostat_signals_and_wiring)

My particular apartment uses a heat pump, which uses the very same compressor action for the air conditioner. The only difference is the air flow. This makes it possible to, in my case, use four wires from the HVAC panel behind the original thermostat for this project:

* **R (Red)**: This is the "common" wire, meaning that a circuit is completed when any of the other wires are connected to this one, hence the relay module.
* **G (Green)**: This is the signal for the fan, which becomes activated when connected to **R**.
* **Y (Yellow)**: This is the signal for the compressor. By default, the air flow is set to blow heat into the apartment.
* **O (Orange)**: This is the signal to reverse the air flow from the compressor. With **Y** and **O** both active, the flow changes to blow cool air into the apartment.

I broke this down to a pretty simple formula while I started writing the software for the controller:

**R** + **G** = Fan<br/>
**R** + **G** + **Y** = Heater<br/>
**R** + **G** + **Y** + **O** = Air conditioner

It's also very important to note that the wires coming out of my HVAC use a low voltage at 24V, not mains power. With a relay module completing the circuits, it should still work with mains electricity, but _**it is very dangerous and you should NOT mess with mains power unless you know exactly what you're doing! An accident involving high voltage and current can very easily kill you.**_

If your home HVAC does not use a compressor heat pump or for another reason you cannot use the same setup I'm using, you will have to do some research and potentially adjust the <code>hvaccontroller.py</code> script accordingly.


# Installation

### Web interface

After cloning the project, you should first set up the LAMP stack on your server. Note that as it is currently programmed, an SSL certificate is required. In the **Interface** directory, there is a file <code>db\_structure.sql</code> which defines the structure of the MySQL database this interface uses. This should _probably_ not be uploaded to your webserver.

Before continuing, you will need to add a row in the **controllers** table along with the **sensors** table in order for the scripts on the HVAC controller Pi and temperature sensor Pi, respectively, to make authenticated requests. Check out the functions in <code>config.php</code> to create the necessary key hashes and salts.

The rest of the files in the **Interface** directory are used in the actual web interface. You will need to modify the top and bottom of the <code>config.php</code> file to replace the placeholders with the required information.

### HVAC Controller Pi

The files for the HVAC controller are in the **HVAC Controller** directory. These files should be placed inside the <code>/home/pi/thermostat</code> directory of the Raspberry Pi running Raspbian.

Again, you will need to look through the files and replace any sections with placeholders (which I've denoted with **XXXXX** strings) with the proper information.

The HVAC controller uses three Python scripts, running simultaneously:

* <code>puller.py</code> which accesses the **get_settings.php** API enpoint from the web server.
* <code>hvaccontrol.py</code> which controls the relay panel. This is sort of the main brain of the project.
* <code>statuspusher.py</code> which updates the web server with the current status with information like what the fan is doing, what the compressor is doing, etc.

There is also a <code>hvaccontroller_cleanup.py</code> script which should be run in the event of the Raspberry Pi shutting down, just to ensure the relays all turn off.

If you've ever used the SainSmart relay module with a Raspberry Pi before, then wiring the relay to the Pi should be trivial. If not, I recommend watching [this video](https://www.youtube.com/watch?v=oaf_zQcrg7g). If you look at the top of the <code>hvaccontrol.py</code> script, you can see which pins are used for the relay:

   GPIO Pin     |       HVAC       | Relay Input 
--------------- | ---------------- | ----------- 
17 (BCM)        | G (Fan)          | IN 1
27 (BCM)        | Y (Compressor)   | IN 2
22 (BCM)        | O (Flow reverse) | IN 3
1 (Board 3.3v)  | --               | VCC IN
6 (Board Gnd)   | --               | GND

![Relay module](https://i.imgur.com/Ktlb2CL.png)
![Raspberry Pi GPIO](https://i.imgur.com/RVW04Mq.png)

### Temperature Sensor Pi

The files for the temperature sensors are in the **Sensor** directory. Similarly to the HVAC controller Pi, the temperature sensor Pi's require the placeholders to be changed to their proper values based on your database and file structures.

The sensors use only two Python scripts, also running simultaneously:

* <code>sensor.py</code> which reads from the DS18B20 Digital temperature sensor
* <code>temppusher.py</code> which updates its corresponding row in the **sensors** table of the remote database.

Installing the hardware for the sensor Pi is relatively simple, but does require a 4.7 kOhm resistor for safe usage of the DS18B20 sensor component. I used Adafruit's [DS18B20 component installation walkthrough](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing/hardware) to figure out how to wire the Pi to the sensor.

Please ensure that the data pin on the DS18B20 is connected to pin 4 (BCM mode) of the Pi's GPIO, as shown in Adafruit's instructions.


# Contributors

I'm really not too great with the whole open source thing, but feel free to add issues, pull requests, all that jazz.

Once again, I apologize how sloppy all of this is.

# License

The MIT License (MIT)

Copyright (c) 2014 William Thomas

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
