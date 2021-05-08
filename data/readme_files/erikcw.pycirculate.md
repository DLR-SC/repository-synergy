## pyCirculate

This is a Python wrapper library for interacting with the Anova 2 over Bluetooth LE.

It should work on any Linux with a working [BlueZ](http://www.bluez.org/) install.  Most of my testing and development took place on a Raspberry Pi.

## Installation

* Install libglib (`sudo apt-get install libglib2.0-dev`)
* Install [bluepy](https://github.com/IanHarvey/bluepy) (`pip install bluepy`).
* `pip install pycirculate`

## Usage
```python
from pycirculate.anova import AnovaController

# Your device's MAC address can be found with `sudo hcitool lescan`
anova = AnovaController("84:EB:18:6E:xx:xx")

anova.read_unit()
# -> 'c'
anova.read_temp()
# -> '14.9'

anova.set_temp(63.5)
anova.start_anova()

anova.anova_status()
# -> 'running'
```

Additional [examples](https://github.com/erikcw/pycirculate/tree/master/examples) can be found in the examples subdirectory.

## Status

*Alpha* -- everything seems to work, but needs more testing.

## TODO

* Add more features to the [REST API example](https://github.com/erikcw/pycirculate/blob/master/examples/rest/).
* More testing.


### Credits

I used the [Circulate](https://github.com/neilpa/circulate/) iOS library as a reference implementation for Anova commands.
