pyElectronics
=============

.. image:: https://travis-ci.org/MartijnBraam/pyElectronics.svg?branch=master
    :target: https://travis-ci.org/MartijnBraam/pyElectronics

.. image:: https://badge.fury.io/py/pyelectronics.svg
    :target: https://badge.fury.io/py/pyelectronics

This is a python library for using electronics (like i2c or spi devices) with a unified interface. It currently supports
connecting to stuff through the Raspberry Pi gpio with the i2c kernel driver and using the Bus Pirate.

Supported gateways
------------------

The gateways are the bridge between Linux and the hardware. Currently supported:

* Bus Pirate v3
* Raspberry Pi / other linux i2c_dev supported interfaces

Supported chips/devices
-----------------------

`Read the contributing guide`_ to add devices

.. _Read the contributing guide: http://pythonhosted.org/pyelectronics/contributing.html

* Bosch BMP180 Digital pressure sensor
* Honeywell 3-Axis Digital Compass IC HMC5883L
* MPU-6050 Six-Axis (Gyro + Accelerometer) MEMS MotionTrackingâ„˘ Device
* NXP LM75A Digital temperature sensor
* Microchip MCP23017 16-Bit I/O Expander
* 7-segment displays without multiplexing

Installation
------------

Install it from pypi::

    $ pip3 install pyelectronics

The various gateways have their own dependencies. Install the dependencies for the gateway you require::

    # Requirements for the Raspberry Pi
    $ pip3 install pysmbus

    # Requirements for the Bus Pirate
    $ pip3 install pyserial

To run the doctests you need all dependencies. You can install them with the doctest requirements file::

    $ pip3 install -r docs/doctest-requirements.txt

Usage
-----

Read the full docs at pythonhosted_.

.. _pythonhosted: https://pythonhosted.org/pyelectronics/index.html


First create a instance of a gateway::

    from electronics.gateways import BusPirate
    from electronics.gateways import LinuxDevice
    
    # Use a BusPirate to connect to a bus
    gw = BusPirate('/dev/ttyUSB0')
    
    # Use a i2c bus with a linux driver (like the raspberry pi)
    gw = LinuxDevice(1) # /dev/i2c-1

Create instances for components connected to the gateway::

    from electronics.devices import BMP180
    from electronics.devices import MPU6050I2C
    
    barometer = BMP180(gw, address=0x77) # Address is optional
    inertia = MPU6050(gw)
    
    # Do chip specific initialisation
    barometer.load_calibration()
    inertia.wakeup()

Read values from sensors::

    temperature = barometer.temperature()
    pressure = barometer.pressure()
    acceleration = inertia.acceleration()
    rotation = inertia.angular_rate()

Example with GPIO::

    # Red led conected to the aux pin of the bus pirate
    red_led = gw.get_aux_pin()
    # Turn the led on
    red_led.write(True)

    # An Microchip port expander connected through I2C
    expander = MCP23017I2C(gw, address=0x21)

    # Get the pins for the two other leds that are connected
    # to the port expander
    green_led = expander.get_pin('A0')
    blue_led = expander.get_pin('A1')

    # Bundle the leds to a bus so you can address 8 colours as an int
    # the pins on the port expander are open drain, they are inverted with the invert operator (~)
    bus = GPIOBus([red_led, ~green_led, ~blue_led])
    bus.write(0) # Black
    bus.write(7) # White

    # Disco!
    while True:
        for i in range(0,8):
            bus.write(i)
            sleep(0.2)