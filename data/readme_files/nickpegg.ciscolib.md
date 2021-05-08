# Deprecation Notice

This project is officially deprecated. I haven't updated it in years, and it's
horribly basic (it only supports telent, which you should _not_ be using!).

I'm keeping this code around since someone might find it useful, but I don't
recommend using it as-is.

For doing network device automation, here are a couple of projects that I
recommend you check out:

* [Trigger](https://github.com/trigger/trigger)
* [Napalm](https://github.com/napalm-automation/napalm)

# ciscolib

A Python library for interacting with Cisco devices via command line. Only
telnet is supported at this time.

There is a lack of documentation at the moment, but this library is fairly
simple. If you dig through device.py, it should be fairly self-explanatory.
Just keep in mind that functions prefixed with an underscore are not meant
to be called directly.

See the LICENSE file for license information.

## Basic Usage

    import ciscolib
    switch = ciscolib.Device("hostname or ip", "login password", "optional login username")
    switch.connect()    # Defaults to port 23

    # There are some helper commands for common tasks
    print(switch.get_model())
    print(switch.get_ios_version())
    print(switch.get_neighbors())

    switch.enable("enable_password")

    # Or you can throw plain commands at the switch
    print(switch.cmd("show run"))
    switch.cmd("reload\n")
