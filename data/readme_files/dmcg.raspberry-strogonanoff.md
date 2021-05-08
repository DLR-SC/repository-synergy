Raspberry Strogonanoff
======================

A Raspberry Pi Remote Mains Switcher, to switch these

http://www.maplin.co.uk/remote-controlled-mains-sockets-5-pack-348217

with one of these

http://proto-pic.co.uk/434mhz-rf-link-transmitter/

using the awesome reverse engineering detailed here

http://www.fanjita.org/serendipity/archives/53-Interfacing-with-radio-controlled-mains-sockets-part-2.html

Installation
------------

Requires WiringPi-Python

    git clone https://github.com/WiringPi/WiringPi-Python.git
    cd WiringPi-Python/
    git submodule update --init
    sudo apt-get install python2.7-dev python-setuptools
    sudo python setup.py install
    
Circuit
-------

You'll need something like this http://proto-pic.co.uk/434mhz-rf-link-transmitter/

Assuming that is the one you buy, the transmitter has 4 pins. Wire
<table>
<tr><th>Tx Pin</th><th>Raspberry Pi Header Pin</th></tr>
<tr><td>Pin 1 GND</td><td>Pin 6 0V (Ground)</td></tr> 
<tr><td>Pin 2 Data in</td><td>Pin 11 GPIO 0</td></tr> 
<tr><td>Pin 3 Vcc</td><td>Pin 2 5.0 VDC Power</td></tr> 
<tr><td>Pin 4 ANT</td><td>173mm antenna wire (not on the Pi!)</td></tr> 
</table>
where the Raspberry Pi Header Pin numbers are the little ones on the inside of the diagram below.

If you've had to read this section, please see the disclaimer below.

Running
-------

Needs to be run as root - 

    sudo ./strogonanoff_sender.py --channel 1 --button 3 --gpio 0 on 
    
where the GPIO pin number is 0 (the default) if wired as per the table above, or otherwise the big ones on this diagram ![](http://pi4j.com/images/p1header-large.png)

Disclaimer
----------

It works for me, but connecting stuff to your Raspberry Pi can destroy either end. If it does, no matter how negligent I've been, I'm sorry, but it's your problem.
