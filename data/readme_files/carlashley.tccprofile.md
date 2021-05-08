# tccprofile
`tccprofile.py` can be used to create a configuration profile containing Privacy Preferences Policy Control Payload's for code signed applications/binaries or code signed scripts on macOS Mojave 10.14.

## Table of Contents
- [Requirements](#requirements)
- [Installing Profiles](#installing-profiles)
- [Usage](#usage)
- [What are Privacy Preferences Policy Control Payloads?](#what-are-privacy-preferences-policy-control-payloads)
- [Other Notes](#other-notes)
    - [Deploying via JAMF](#deploying-via-jamf)
    - [File Paths](#file-paths)
    - [Determining Code Signing Requirements for Applications and Scripts](#determining-code-signing-requirements-for-applications-and-scripts)
    - [Scripts and Shebangs](#scripts-and-shebangs)
    - [Code Signing Scripts](#code-signing-scripts)
    - [Explicit or Generic Code Signing Requirements](#explicit-or-generic-code-signing-requirements)
    - [Camera and Microphone Payloads](#camera-and-microphone-payloads)
    - [Using the TCC databases for troubleshooting](#using-the-tcc-databases-for-troubleshooting)
- [Command Line Examples](#command-line-examples)
- [GUI Mode](#gui-mode)

## Requirements
- This script is targeted for use in python 2.7.10 as distributed with macOS

## Installing Profiles
Privacy Preferences Policy Control Payload profiles can only be installed on a device that is either:
- Enrolled in an MDM using DEP
- Enrolled in an MDM using User Approved MDM enrolment

## Usage
1. `git clone https://github.com/carlashley/tccprofile`
1. `cd tccprofile && chmod +x tccprofile.py`
1. Use `tccprofile.py --help` to view the available arguments

## What are Privacy Preferences Policy Control Payloads?
These are payloads avilable to configure whether apps can:
- Access _all_ protected files, including system administration files
- Access some files used in system administration
- Access the address book, calendar, reminders, photos, camera, or microphone
- Enable the app to be controled via Accessibility features
- Enable the app to send certain types of events to the system event stream
- Send AppleEvents to another process

## Other Notes
- `tccprofile.py` generates all the relevant payload values automatically based on what arguments are provided at the command line, or selections made in the GUI.
- When the `--allow` argument is used in the command line, _all_ payloads (except the camera and microphone) will be set to `Allowed = True`. If the `--allow` argument is not used, _all_ payloads will be set to `Allowed = False`. For any profile generated using the command line, if you need to allow and deny various apps in the one profile, you will need to manually change the relevant payload.
- The `StaticCode` key is not supported. Manually modify the profile if this is required for an app. If you're not sure what this is, the [man page](x-man-page://codesign) has details, as well as [this stackoverflow page](https://stackoverflow.com/questions/43623044/what-kind-of-dynamic-code-modification-does-dynamic-code-validity-check-protects).

### Deploying via JAMF
Profiles uploaded to versions of JAMF prior to the 10.7.1 release may need to be signed in order for the profile to be uploaded.

### File Paths
It is recommended that the item the profile is being created for should be installed or found in the same location that it will be on the target system.

If the path to the binary/script is in a different location on the machine generating the profiles, you will need to change any relevant file/folder paths to the correct path.

For example:
Creating an `AppleEvents` payload for `outset` that was located in the path `/Users/carl/Desktop/git/outset/pkgroot/usr/local/outset/outset` and saved to `Outset_PPPCP.mobileconfig` results in:

```
<dict>
	<key>AEReceiverCodeRequirement</key>
	<string>identifier "com.apple.systemevents" and anchor apple</string>
	<key>AEReceiverIdentifier</key>
	<string>com.apple.systemevents</string>
	<key>AEReceiverIdentifierType</key>
	<string>bundleID</string>
	<key>Allowed</key>
	<true/>
	<key>CodeRequirement</key>
	<string>identifier "com.github.outset" and anchor apple generic and certificate leaf[subject.CN] = "Mac Developer: foo@example.org (ABC01FFFGH)" and certificate 1[field.1.2.345.678901.234.5.6.7] /* exists */</string>
	<key>Comment</key>
	<string>Allow outset to send AppleEvents control to System Events</string>
	<key>Identifier</key>
	<string>/Users/carl/Desktop/git/outset/pkgroot/usr/local/outset/outset</string>
	<key>IdentifierType</key>
	<string>path</string>
</dict>
```
The `Identifer` path result will need to be updated to point to the correct location manually, or using something like `sed`:
```bash
sed -i '' 's/\/Users\/carl\/Desktop\/git\/outset\/pkgroot//g Outset_PPPCP.mobileconfig'
```

### Determining Code Signing Requirements for Applications and Scripts
`tccutil.py` will check to see if files are code signed, and if so, will use the code signing details it finds.

### Scripts and shebangs
If a script isn't code signed, it will attempt to find the code signing details for the shell or interpreter path in the script's shebang line.

Please note, it will not be able to determine the correct path of a shell or interpreter if a `#!/usr/bin/env <interpreter/shell>` style shebang is used.
- A `#!/usr/bin/env` style shebang will not guarantee that the interpreter or shell used by the script will be consistent depending on what a user has installed on their OS.
- Newer versions of shells or interpreters (for example, a bash 4.x shell, or python3 interpreter) may not be code signed.

### Code Signing Scripts
You can code sign your own scripts. Be aware that the code sign details for a "plain text" file are stored in extended attributes and may not be preserved when the script is deployed. [See this post for more details](https://carlashley.com/2018/09/23/code-signing-scripts-for-pppc-whitelisting/).

### Explicit or Generic Code Signing Requirements
When creating these profiles, `tccprofile.py` will always use the _complete_ code sign requirements for the binary or script being approved or blocked in the profile.

The use of generic code sign requirements is _not_ recommended, as this will make it easier for malicious apps to fake the code signing requirements of another app and potentially harm the system.

For example, the below code signing requirements are the complete requirements:
```
identifier "com.github.outset" and anchor apple generic and certificate leaf[subject.CN] = "Mac Developer: foo@example.org (ABC01FFFGH)" and certificate 1[field.1.2.345.678901.234.5.6.7] /* exists */
```

The below code signing requirements are a generic set of requirements:
```
identifier "com.github.outset" and anchor apple generic
```

### Camera and Microphone Payloads
Per Apple's [Configuration Profile Reference](https://developer.apple.com/enterprise/documentation/Configuration-Profile-Reference.pdf) documentation, the camera and microphone payloads will _always_ be set to `Deny`

### Using the TCC databases for troubleshooting
To assist in troubleshooting what PPPCP payloads to create for an application, the TCC databases (either in `~/Library/Application Support/com.apple.TCC/TCC.db` or `/Library/Application Support/com.apple.TCC/TCC.db`) can be read as long as the Terminal app (or terminal app of your choice) has been granted `Full Disk Access`.

To use (`sudo` is required if reading the database in `/Library/Application Support/com.apple.TCC`):
```
./tccdbRead.py <path to TCC database>
```

It will output something like:
```
-----------------------------------------------------------------------
 Service                             | Client
-----------------------------------------------------------------------
 kTCCServiceAccessibility            | com.adobe.Photoshop
 kTCCServiceAccessibility            | com.divisiblebyzero.Spectacle
 kTCCServiceAccessibility            | com.hegenberg.BetterSnapTool
 kTCCServiceAccessibility            | com.vmware.fusion
 kTCCServicePostEvent                | com.adobe.Photoshop
 kTCCServicePostEvent                | com.divisiblebyzero.Spectacle
 kTCCServicePostEvent                | com.hegenberg.BetterSnapTool
 kTCCServiceSystemPolicyAllFiles     | /usr/sbin/sshd
 kTCCServiceSystemPolicyAllFiles     | com.apple.Terminal
 ```

## Command Line Examples
```bash
./tccprofile.py --accessibility /Applications/Automator.app --allow --payload-description="Whitelist Apps" --payload-identifier="com.github.carlashley" --payload-name="TCC Whitelist" --payload-org="My Great Company" -o TCC_Accessibility_Profile_20180816_v1.mobileconfig
```

Example with signing:

```bash
./tccprofile.py --accessibility /Applications/Automator.app --allow --payload-description="Whitelist Apps" --payload-identifier="com.github.carlashley" --payload-name="TCC Whitelist" --payload-org="My Great Company" -o TCC_Accessibility_Profile_20180816_v1.mobileconfig --sign="Certificate Name"
```

To create an AppleEvent Payload, you must provide _both_ apps as comma separated. The first app is the app _sending_ the event, the second app is the app _receiving_ the event.

```bash
./tccprofile.py --apple-event /Applications/Adobe\ Photoshop\ CC\ 2018/Adobe\ Photoshop\ CC\ 2018.app,/System/Library/CoreServices/Finder.app --payload-description="TCC Whitelist for Adobe Photoshop" --payload-name="TCC Whitelist" --payload-org="My Great Company" --payload-identifier="com.carlashley.github" -o Adobe_Photoshop_TCC.mobileconfig --allow --sign="Certificate Name"
```

Create payloads for multiple types:

```bash
./tccprofile.py --apple-event /usr/local/outset/outset,/System/Library/CoreServices/System\ Events.app --allfiles /Applications/Utilities/Terminal.app /usr/sbin/installer --accessibility /Applications/Adobe\ Photoshop\ CC\ 2018/Adobe\ Photoshop\ CC\ 2018.app --payload-description="TCC Whitelist for various applications" --payload-name="TCC Whitelist" --payload-org="My Great Company" --payload-identifier="com.carlashley.github" -o TCC_Whitelists.mobileconfig --allow --sign="Certificate Name"
```

### GUI Mode
[@brysontyrrell](https://github.com/brysontyrrell) has created a GUI for `tccprofile.py` as an alternative to the CLI.

To launch the GUI, invoke the script without passing any command line arguments:
```bash
./tccprofile.py
```

Modify the default values for the `Payload Details` as needed. The `Sign Profile?` list will be autopopulated with all available signing certificates on your system.

Errors or incorrect inputs will cause a message to be displayed in red italic text below this section (as shown in the example screenshot).

As with the CLI, selecting an app or binary and a service will grant `ALLOW` permissions with the exception of the `Camera` and `Microphone` payloads (those are explictly `DENY`).

![TCC Profile GUI](images/tccprofile_gui.png)
