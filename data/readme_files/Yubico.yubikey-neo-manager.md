== YubiKey NEO Manager

NOTE: This project is deprecated and is no longer being maintained.
Use YubiKey Manager (https://developers.yubico.com/yubikey-manager-qt/[GUI], https://developers.yubico.com/yubikey-manager/[CLI]) to configure a YubiKey device.

Tool for managing your YubiKey NEO configuration. Connecting multiple keys at
once is supported, but only if CCID mode is active for all of them.


Entypo pictograms by Daniel Bruce - www.entypo.com

[IMPORTANT]
====
Yubico has learned of a security issue with the OpenPGP Card applet project that is used in the YubiKey NEO. This vulnerability applies to you only if you are using OpenPGP, and you have the OpenPGP applet version 1.0.9 or earlier.
link:https://developers.yubico.com/ykneo-openpgp/SecurityAdvisory%202015-04-14.html[SecurityAdvisory 2015-04-14]
====

=== Installation
The recommended way to install this software including dependencies is by using
the provided precompiled binaries for your platform. For Windows and OS X (10.7 and above),
there are installers available for download
https://developers.yubico.com/yubikey-neo-manager/Releases/[here].
For Ubuntu we have a
https://launchpad.net/%7eyubico/+archive/ubuntu/stable[custom PPA] containing the 
https://launchpad.net/%7eyubico/+archive/ubuntu/stable/+packages?field.name_filter=yubikey-neo-manager&field.status_filter=published&field.series_filter=[yubikey-neo-manager]
package.

=== Dependencies
YubiKey NEO Manager requires PySide, libykneomgr, yubikey-personalization and
libu2f-host.

=== Running tests
Tests can be run using the "nosetests" command, from the python-nose package.
Alternatively "python setup.py test" can be used, but this will cause PySide
to be compiled from source, requiring the python-dev package.

=== Building binaries
Binaries for Windows and OSX are built using PyInstaller.

Get the source release file, yubikey-neo-manager-<version>.tar.gz, and extract
it. It should contain a single directory, henceforth refered to as the release
directory.

When building binaries for Windows or OS X, you will need to include
.dll/.dylib files from the libykneomgr, yubikey-personalization, and
libu2f-host projects. Create a subdirectory called "lib" in the release
directory.
Download the correct binary release for your architecture for each of the 
aforementioned projects from https://developers.yubico.com/ and extract the 
.dll/.dylib files for each of them together with the included dependencies to
the "lib" directory you created previously.

==== Windows
For Windows you will need python, PySide, PyCrypto, PyInstaller and Pywin32
installed (32 or 64-bit versions depending on the architecture of the binary
your are building).

To sign the executable you will need signtool.exe (from the Windows SDK) either
copied into the root as well or in a location in your PATH, as well as a
certificate in the Windows certificate store that you wish to sign with.

Run "python setup.py executable" from the main release directory."

With NSIS installed, a Windows installer will be built as well.

==== OSX
For OSX you need python, pyside, pycrypto, and pyinstaller installed. One way 
to install these dependencies is by using Homebrew:

  brew install python
  brew install pyside
  pip install PyInstaller
  pip install pycrypto

NOTE: Homebrew will build backwards-incompatible binaries, so the resulting
build will not run on an older version of OSX. For building distributable
releases you can use MacPorts instead.

Run "python setup.py executable" from the main release directory. This
will create an .app in the dist directory.

Sign the code using codesign:

  codesign -s 'Developer ID Application' dist/YubiKey\ NEO\ Manager.app --deep

There is also a project file for use with 
http://s.sudre.free.fr/Packaging.html[Packages]
located at `resources/neoman.pkgproj`.
This can be used to create an installer for distribution, which you should sign
prior to distribution:

  packagesbuild resources/osx-installer.pkgproj
  productsign --sign 'Developer ID Installer' dist/YubiKey\ NEO\ Manager.pkg dist/yubikey-neo-manager-mac.pkg

