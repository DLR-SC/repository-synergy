## SEAL: SEAndroid Analytics Library for live device analysis
[SEAL](https://github.com/seandroid-analytics/seal/wiki) is a SEAndroid live device analysis tool. It can perform policy analysis on Android devices (real or emulated) connected through ADB.
Devices must be rooted or running a debug build. Running the tool on a non-rooted production device will yield incomplete results.
```
usage: seal [-h] [--adb ADB] [--device <DEVICE>]
               {polinfo,files,processes} ...

positional arguments:
  {polinfo,files,processes}
                        sub-command help
    polinfo             Show policy info from device
    files               List all files on the device
    processes           List all processes on the device

optional arguments:
  -h, --help            show this help message and exit
  --adb ADB             Path to your local root adb if not in your $PATH
  --device <DEVICE>     Specify a device to work with
```

The tool offers functionality through a set of subcommands. The current ones are:

* [polinfo](https://github.com/seandroid-analytics/seal/wiki#polinfo) - view policy statistics from a connected device
* [files](https://github.com/seandroid-analytics/seal/wiki#files) - list files on the device, optionally filtering to show only files a specific process has access to
* [processes](https://github.com/seandroid-analytics/seal/wiki#processes) - list processes on the device, optionally filtering to show only processes that have access to a specific file/path

A graphical frontend to the SEALv1 tool is available as [SEALX](https://github.com/seandroid-analytics/seal/wiki/SEALX). An equivalent graphical tool for SEALv2 is in the works.

## Obtaining SEAL
SEAL is available in two versions, SEALv1 and SEALv2. SEALv2 is the current version.
SEALv1 can deal with SELinux policies up to version 29, and with Android up to version 5.1; for more recent Android and SELinux policy versions, SEALv2 is required.

###SEALv2
SEALv2 may be obtained by cloning this repository. From the command line, do:

```
$ git clone git@github.com:seandroid-analytics/seal.git
```

The SEALv2 library requires the `setools` library from [SEToolsv4](https://github.com/TresysTechnology/setools).
The `setools` library is also distributed as part of the [AOSP tree](https://source.android.com/source/index.html), where it is distributed as a prebuilt. After [downloading the AOSP tree](https://source.android.com/source/downloading.html) in `$WORKING_DIRECTORY`, the `setools` package will be in
```
$WORKING_DIRECTORY/prebuilts/python/linux-x86/2.7.5/lib/python2.7/site-packages
```
To use this package, add this path to your `$PYTHONPATH`; for example, on Ubuntu 14.04 LTS add this to your `.profile`:
```
export PYTHONPATH="$WORKING_DIRECTORY/prebuilts/python/linux-x86/2.7.5/lib/python2.7/site-packages:$PYTHONPATH"
```

SEALv2 also requires the Android Debug Bridge to be installed and in your `$PATH`.
You may use the ADB which comes with the Android SDK (recommended), or install it through your distribution's package manager.

###SEALv1
SEALv1 is no longer being developed.
SEALv1 can be [downloaded from GitHub as a release](https://github.com/seandroid-analytics/seal/releases/tag/v1.0.0).

The SEALv1 library requires the Python bindings to libapol and libqpol from [SEToolsv3](https://github.com/TresysTechnology/setools3).
These can be obtained on Ubuntu 14.04 LTS by installing the `python-setools` package.
SEALv1 also requires the Android Debug Bridge to be installed and in your `$PATH`.
You may use the ADB which comes with the Android SDK (recommended), or install it through your distribution's package manager.


## Running SEAL
From the resulting directory, run:

```
$ python seal.py [GLOBAL OPTIONS] <subcommand> [OPTIONS]
```

## Reporting bugs
You can report bugs in the project [issue tracker](https://github.com/seandroid-analytics/seal/issues).

## License
Copyright (C) 2015 Aalto University

SEAL is licensed under the Apache License 2.0 (see LICENSE).

SEAL is an open source project being developed at Aalto University as part of the [Intel Collaborative Research Institute for Secure Computing (ICRI-SC)](http://www.icri-sc.org).
