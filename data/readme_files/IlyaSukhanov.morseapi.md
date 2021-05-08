# MorseAPI
`MorseAPI` is an unofficial (and unsanctioned) python library for controlling
[Wonder Workshop's](https://www.makewonder.com/)
[Dash and Dot](https://www.makewonder.com/?gclid=CPOO8bC8k8oCFdaRHwodPeMIZg)
robots.

The robots are controlled with commands sent over Bluetooth, specifically
[GATT](https://developer.bluetooth.org/TechnologyOverview/Pages/GATT.aspx).
MorseAPI abstracts out this communication protocol and, through python methods
exposes control of lights, motion and sensor data.

## Compatibility
MorseAPI has only been tested on GNU/Linux platforms. It should work with any
reasonably modern Distro. Limitation is mostly on the BlueZ version, and
bluetooth adapter compatibility. [Raspberry Pi](https://www.raspberrypi.org/)
is a particularly attractive platform for running MorseAPI. Its a small
enough package that it can be attached to the robot making for a fully
integrated, and portable package.
[Raspbian](https://www.raspberrypi.org/downloads/raspbian/) in particular
has been tested in this combination. Note, that Raspberry does not come
with a built in bluttooth module, so a USB bluetooth accessory is required.

In theory it should be possible to us MorseAPI on OSX. To do so you must
use [pygatt](https://github.com/peplin/pygatt)'s BGAPI backend. But it
does require a very special bluetooth adapter;
[BLED112](https://www.bluegiga.com/en-US/products/bled112-bluetooth-smart-dongle/).
Again OSX has not been tested.

## Motivation
There exist smartphone apps which allow remote-controlling Dash and Dot, and even "writing programs" for them.
However, the programming functionality is limited to drag-and-drop style and does not allow interaction with
any industry programming languages.

That doesn't need to be the case - young kids can get started with the simple
drag-and-drop interface to get some exposure and instill interest, then graduate to a programming API interface in order
to create more complicated and complete implementations of their creative ideas.

`MorseAPI` provides that programming interface, in a language that is easy to pick up even for non-engineers: Python.

## Installation
This is only tested on Debian, though it should work on other Linux flavors. OSX and Windows are NOT supported.

Steps:

 * `sudo apt-get install bluez`  # version 5+ is required by pygatt
 * clone this repo and `cd` into it
 * pip install -e . 

## Completeness
Dash and Dot have many different commands. Morse implements only fraction there of:

 * LED Lights:
  * Ears
  * Top of Head
  * Neck / Eye backlight
  * Individual iris LEDs
  * Iris brightness
  * ~~tail light~~
 * Motion (Dash only)
  * Head pitch and Yaw
  * Move back and forth
  * Turn left and right
 * Sound
  * Playback of built in sounds
  * ~~Uploading new sounds~~
 * Sensor feedback
  * Microphone volume
  * Proximity Sensing
  * Head pitch / yaw
  * wheel rotation
  * Dash sensing of Dot
  * Robot picked / bumped / toppled oved
  * Sound direction
  * Gyro pitch/yaw/roll
  * Vertical acceleration
  * Clap
  * ~~Battery state~~
 * ~~Robot discovery~~
   * feature discovery (Dash & Dot have different feature sets)


## Example
Run:

```
examples/clock.py C0:F0:84:3C:51:FA
```

where `C0:F0:84:3C:51:FA` should be the bluetooth address of your bot

```
$ python
>>> from morseapi import MorseRobot
>>> bot = MorseRobot("C0:F0:84:3C:51:FA")
>>> bot.reset()
>>> bot.connect()
>>> bot.say("hi")
>>> bot.move(100)
>>> bot.turn(45)
>>> bot.ear_color("red")
>>> bot.head_yaw(10)
>>> bot.eye(255)
>>> bot.eye(100)
```
