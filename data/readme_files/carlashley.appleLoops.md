# appleloops
A utility to manage the deployment of the additional audio content Apple provides for GarageBand, Logic Pro X, and MainStage 3.

## What's New in v3.1.4+
- The `build.sh` script can be run with custom python paths provided.<br />
For example: `./build.sh --python="/usr/local/bin/python3.7"`

### What's New in v3.0.0+
- Supports Python 3 (tested on Python 3.7.3) and Python 2.7.10 (as ships with macOS).
- Now ships as a prebuilt `zipapp`.
- Pre built installer package is available. Installs to `/usr/local/bin`.
- Now using `/usr/bin/env python`. Beware of Python versions when deploying!.
- Supports deploying packages from a DMG file hosted over HTTP/HTTPS (use the `--pkg-server` flag and supply the full HTTP path to the DMG).
- Building a DMG file now uses a temporary sparse image file to download packages directly into, then converts it to a DMG.
  - APFS file system supported with the `--APFS` flag. Defaults to HFS+ file system.
  - DMG's are now read only, and compressed.
  - DMG's will be written over if the same filename is specified.
  - Specifying a custom volume name is not allowed. Volume name defaults to `appleloops` to facilitate deploying via DMG.
- Supports deploying packages for a specific application when using `--deployment` - use the `-a/--apps <appname>` argument.
- Downloading now replicates the source folder structure, regardless.
- Improved handling of scenarios where one package is considered mandatory for one application, but optional for another.
- Implemented additional file path check based on the information in the property lists to determine if the package is installed.
- Added flexibility to handle scenarios where Apple's "mirrored" source property list files are not kept updated inline with the file that ships with specific apps.
- Pure silent mode. No output at all (well, there _shouldn't_ be any).
- `Makefile` to build a package file for distribution (a package will be pre-built).
- Added new `--compare` argument to enable a basic comparison of one package 'release' to another 'release'.
- No longer requesting `Content-Size` header when analysing installed pacakges. This saves a teeny-tiny bit of time, but worth it.
- Logging will now default to `~/Library/Logs/appleloops.log` unless `sudo` is invoked, in which case the log output is `/var/log/appleloops.log`.
  - Logs automatically rollover on each run.
- Invoking `DEBUG` logging now requires using `--log-level DEBUG`.
- Default paths for package downloads should default to `/tmp/appleloops`
- Temporary working path for any downloaded property list files is `/var/folders/<incomprehensible gibberish>/com.github.carlashley.appleloops`.
  - This gets cleaned up once work is finished.
- No longer relying on sourcing the property list files from Apple's `audiocontentdownload` server when deploying or if the app is installed on the same system.
  - Note, if you do need to target the packages for a specific release, use the `--supported-plists` argument to identify which property list files can be used when using the `-p/--plist` argument.

## Whats Deprecated in v3.0.0+
A number of previous features are being deprecated from v3.0.0 onwards to avoid certain complexities.
- Hard-linking to already downloaded files (due to now replicating the Apple source folder path when downloading).
- "Flat" directory structures for downloaded content no longer supported.
- Specifying a disk space threshold to reserve.
  - When deploying, the goal is to ensure _all_ the packages of either mandatory/optional types get installed.
- No longer a fully self contained script (script is now split out into a python package). Script is now zipped using `zipapp` Python 3 built-in.
- Specifying a log path is no longer supported.
- Will install all mandatory packages in deployment mode or will not install them at all. Same for optional packages.
- `--debug` hard deprecated for `--log <level>`. For example: `--log DEBUG`.
- Python 2.x support will be dropped in a future release in keeping with Apple's stance on Python shipping in future macOS releases. Will require Python 3.x to be installed (I don't currently have plans to write this in Swift).
  - 2019-11-09 Note: When Apple removes Python 2 from macOS, this will only be tested/built against a Python 3 environment.
- Determining the `--pkg-server` path based on the `munki` configuration on a machine that is managed with `munki` is no longer supported.
- Automatically determining a Caching Server source to use is no longer supported. Specifying the server will be required if the `-c/--cache-server` argument is used.

## Requirements
- macOS.
- Any version of Python from 2.7.10 onwards.
  - Tested on Python 2.7.10 (macOS only, not guaranteed to work in macOS 10.15).
  - Tested on Python 3.7.3 (macOS only, _may_ be required if Python 2 does not ship with this release of macOS).
- Deploying packages will require any or a combination of these apps to be installed (the packages run checks at install time to check):
  - GarageBand.
  - Logic Pro X.
  - MainStage 3.
- If a local HTTP mirror is being used, `appleloops` expects to find the packages in the same folder path as they exist on the Apple audio content servers. For example, `https://example.org/appleloops/lp10_ms3_content_YYYY` where `YYYY` is a year value. If a file cannot be found here, it will fall back to the Apple audio content servers.
- If a local Caching Server is being used, you will need to provide the correct Caching Server address, such as `https://example.org:43012`.
- Your firewall/proxy must whitelist `https://audiocontentdownload.apple.com` - if your network team isn't already whitelisting _all_ of `17.0.0.0/8`, well, it's a good time to start whitelisting it.
- Whitelisting `https://raw.githubusercontent.com` is still (currently) a requirement.
- Access to `https://audiocontentdownload.apple.com` is a requirement.
- Proxies may need to be managed via environment variables set prior to running the utility.

## Building Your Own
To "build" your own version, you will need to have Python 3 installed for `zipapp` to work.
1. Clone this repo.
1. `cd appleloops`
1. `./build.sh`
1. Package gets built into `dist/pkg`

## Code Signing
This is _not_ code signed. Feel free to code sign at your own discretion for your use case.
*WARNING* Please inspect the source before code signing to ensure this is the right action for you.

## Notarization
This is _not_ notarized. Feel free to notarize at your own discretion for your use case.
*WARNING* Please inspect the source before notarizing to ensure this is the right action for you.

## Archived Version
An unsupported archived repository of the older versions of this utility is available here: https://github.com/carlashley/appleloops_archive.

## License
This is licensed using the Apache License, Version 2.0.
