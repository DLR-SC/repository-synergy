<p align="center">
<a href="https://travis-ci.org/glucometers-tech/glucometerutils/builds/"><img alt="build status" src="https://img.shields.io/travis/glucometers-tech/glucometerutils"></a>
<a href="https://github.com/glucometers-tech/glucometerutils#license"><img alt="GitHub" src="https://img.shields.io/badge/license-MIT-green"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

# Glucometer Utilities

This repository includes a command line utility to interact with a number of
blood sugar meters (glucometer) models from various manufacturers.

While support varies by device, the actions that may be available are as
follows:

 * `info` shows the model, serial number, date and time, and configured glucose
   unit of the device.
 * `dump` export the recorded blood sugar or β-ketone readings from the device
   in comma-separated values format.
 * `datetime` reads or updates the date and time of the device clock.
 * `zero` deletes all the recorded readings (only implemented for few devices).

## Example Usage

Most of the drivers require optional dependencies, and those are listed in the
table below. If you do not want to install the dependencies manually, you should
be able to set this up using `virtualenv` and `pip`:

```shell
$ python3 -m venv $(pwd)/glucometerutils-venv
$ . glucometerutils-venv/bin/activate
(glucometerutils-venv) $ DRIVER=myglucometer-driver  # see table below
(glucometerutils-venv) $ pip install "git+https://github.com/glucometers-tech/glucometerutils.git#egg=glucometerutils[${DRIVER}]"
(glucometerutils-venv) $ glucometer --driver ${DRIVER} help
```

## Supported devices

Please see the following table for the driver for each device that is known and
supported.

| Manufacturer | Model Name                 | Driver             | Dependencies                      |
| ---          | ---                        | ---                | ---                               |
| LifeScan     | OneTouch Ultra 2           | `otultra2`         | [pyserial]                        |
| LifeScan     | OneTouch Ultra Easy        | `otultraeasy`      | [construct] [pyserial]            |
| LifeScan     | OneTouch Ultra Mini        | `otultraeasy`      | [construct] [pyserial]            |
| LifeScan     | OneTouch Verio IQ          | `otverioiq`        | [construct] [pyserial]            |
| LifeScan     | OneTouch Verio (USB)       | `otverio2015`      | [construct] [python-scsi]         |
| LifeScan     | OneTouch Select Plus       | `otverio2015`      | [construct] [python-scsi]         |
| LifeScan     | OneTouch Select Plus Flex¹ | `otverio2015`      | [construct] [python-scsi]         |
| Abbott       | FreeStyle InsuLinx†        | `fsinsulinx`       | [construct] [hidapi]‡             |
| Abbott       | FreeStyle Libre            | `fslibre`          | [construct] [hidapi]‡             |
| Abbott       | FreeStyle Optium           | `fsoptium`         | [pyserial]                        |
| Abbott       | FreeStyle Precision Neo    | `fsprecisionneo`   | [construct] [hidapi]‡             |
| Abbott       | FreeStyle Optium Neo       | `fsprecisionneo`   | [construct] [hidapi]‡             |
| Abbott       | FreeStyle Optium Neo H     | `fsprecisionneo`   | [construct] [hidapi]‡             |
| Roche        | Accu-Chek Mobile           | `accuchek_reports` |                                   |
| SD Biosensor | SD CodeFree                | `sdcodefree`       | [construct] [pyserial]            |
| TaiDoc       | TD-4277                    | `td4277`           | [construct] [pyserial]² [hidapi]  |
| GlucoRx      | Nexus                      | `td4277`           | [construct] [pyserial]² [hidapi]  |
| Menarini     | GlucoMen Nexus             | `td4277`           | [construct] [pyserial]² [hidapi]  |
| Aktivmed     | GlucoCheck XL              | `td4277`           | [construct] [pyserial]² [hidapi]  |
| Ascensia     | ContourUSB                 | `contourusb`       | [construct] [hidapi]‡             |

† Untested.

‡ Optional dependency on Linux; required on other operating systems.

¹ USB only, bluetooth not supported.

² Requires a version of pyserial supporting CP2110 bridges. See [this pyserial
pull request](https://github.com/pyserial/pyserial/pull/411).

To identify the supported features for each of the driver, query the `help`
action:

    glucometer.py --driver fslibre help

If you have knowledge of a protocol of a glucometer you would have supported,
please provide a reference, possibly by writing a specification and contribute
it to https://protocols.glucometers.tech/ .

[construct]: https://construct.readthedocs.io/en/latest/
[pyserial]: https://pythonhosted.org/pyserial/
[python-scsi]: https://github.com/rosjat/python-scsi
[hidapi]: https://pypi.python.org/pypi/hidapi

## Dump format

The `dump` action by default will output CSV-compatible format, with the
following fields:

 * date and time;
 * meter reading value;
 * before/after meal information, if known;
 * comment provided with the reading, if any.

Meal and comment information is provided by the meters supporting the
information. In the future, meal information could be guessed based on the time
of the reading.

The unit format used by the dump by default matches what the meter reports as
its display unit, which might differ from the one used by the meter for internal
representation and wire protocol. You can override the display unit with
`--unit`.

## Development

The tool is being written keeping in mind that different glucometers,
even if they are all from the same manufacturer, will use different
protocols.

If you want to contribute code, please note that the target language
is Python 3.6, and that the style to follow is for the most part PEP8
compatible.

To set up your development environment follow these guidelines:

```shell
$ git clone https://github.com/glucometers-tech/glucometerutils.git
$ cd glucometerutils
$ python3 -m venv --python=python3.6
$ . venv/bin/activate
$ pip install -e .[dev]
$ # If you want to work on a specific driver specify this after dev e.g.
$ # pip install -e .[dev,myglucometer-driver] # see table above
$ pre-commit install
```

## License

Copyright © 2013-2020 The glucometerutils Authors

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
