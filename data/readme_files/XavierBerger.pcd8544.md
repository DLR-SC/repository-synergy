#pcd8544 Python library for Raspberry Pi


**This repository contains a python library to drive PCD8544 LCD (Nokia 5110)**

PCD8544 LCD screen is a small cheap screen originally used into Nokia 3110/5110 handset. This screen is still sold nowaday and can be easily purchased online. It fits very well with Raspberry Pi and opens the world of user interface.

![pcd8544](https://raw.github.com/XavierBerger/pcd8544/master/doc/PCD8544.png)

## Installing the dependencies

First, install *wiringpi2* from drogon.net

    git clone git://git.drogon.net/wiringPi
    cd wiringPi
    ./build

Once `wiringpi` is installed, it is possible to test it with the following command:

    gpio readall
     +-----+-------+------+----+-Rev2-----+----+------+-------+-----+
     | wPi |  Name | Mode | Val| Physical |Val | Mode | Name  | wPi |
     +-----+-------+------+----+----++----+----+------+-------+-----+
     |     |  3.3v |      |    |  1 || 2  |    |      | 5v    |     |
     |   8 |   SDA |   IN | Lo |  3 || 4  |    |      | 5V    |     |
     |   9 |   SCL |   IN | Lo |  5 || 6  |    |      | 0v    |     |
     |   7 | GPIO7 |   IN | Lo |  7 || 8  | Lo | ALT0 | TxD   | 15  |
     |     |    0v |      |    |  9 || 10 | Lo | ALT0 | RxD   | 16  |
     |   0 | GPIO0 |   IN | Hi | 11 || 12 | Hi | OUT  | GPIO1 | 1   |
     |   2 | GPIO2 |   IN | Lo | 13 || 14 |    |      | 0v    |     |
     |   3 | GPIO3 |   IN | Hi | 15 || 16 | Lo | OUT  | GPIO4 | 4   |
     |     |  3.3v |      |    | 17 || 18 | Lo | OUT  | GPIO5 | 5   |
     |  12 |  MOSI | ALT0 | Hi | 19 || 20 |    |      | 0v    |     |
     |  13 |  MISO | ALT0 | Hi | 21 || 22 | Hi | IN   | GPIO6 | 6   |
     |  14 |  SCLK | ALT0 | Hi | 23 || 24 | Lo | ALT0 | CE1   | 10  |
     |     |    0v |      |    | 25 || 26 | Lo | ALT0 | CE1   | 11  |
     +-----+-------+------+----+----++----+----+------+-------+-----+
Now, install the python binding of `wiringpi`:

    sudo apt-get install python-dev python-imaging python-imaging-tk python-pip
    sudo pip install wiringpi

The program we will use require `spidev` to be activated. The kernel module should then be activated.
To do so, comment the line `blacklist spi-bcm2708` by adding a heading `#` in the file `/etc/modprobe.d/raspi-blacklist.conf` then reboot the Raspberry Pi to activate this module.

Finally install spidev python library:

    sudo pip install spidev

## Building and installing the library

To install the library, execute the following commands:

    git clone https://github.com/XavierBerger/pcd8544.git
    cd pcd8544
    ./setup.py clean build 
    sudo ./setup.py install


## Wiring the LCD to the Raspberry Pi

The following schema represent how to connect the LCD screen to the Raspberry Pi

![Wiring Schematic](https://raw.github.com/XavierBerger/pcd8544/master/doc/PCD8544wiring.png)

**Note: Check carefully the pin order of your LCD screen, it may be different.**

*Schema made with Fritring (http://fritzing.org)*

## Examples

The library comes with [examples](https://github.com/XavierBerger/pcd8544/tree/master/examples) showing different feature and library usage.

[![pi_logo](https://raw.github.com/XavierBerger/pcd8544/master/doc/pi_logo.png)](https://github.com/XavierBerger/pcd8544/tree/master/examples)

## Special thanks and references

Special thanks goes to Raspberry Pi community:
 * http://www.raspberrypi.org/phpBB3/viewtopic.php?p=301522#p301522
 * https://github.com/rm-hull/pcd8544 

