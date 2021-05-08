# Introduction

This is an implementation of a userspace driver for using the Boogie Board Sync
as a tablet under linux.  There are two apps, one for usb input and one for
bluetooth.  It uses pyusb/pybluez to interface with the device and the UInput
system (via evdev for python) to generate input signals.  It's still early
days, so it may be unstable.

# Requirements

- python
- pyusb (for usb)
- pybluez (for bluetooth)
- evdev

# Usage

For the USB app, plug in the device and run the app. If you get timeout errors see the bugs below.

For bluetooth, it should scan for your device so simply running it should work.  If not, run blue.py with a specific address (e.g., ./blue.py 00:00:00:00:00:00) which you can discover using "hcitool scan".
