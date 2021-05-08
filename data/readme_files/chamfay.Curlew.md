Curlew Multimedia Converter:
----------------------------

Description:
------------

Easy to use, Free and Open-Source Multimedia converter for Linux.
Curlew written in python and GTK3 and it depends on (ffmpeg/avconv).

Main Features:

- Easy to use and clean user interface.
- Hide the advanced options with the ability to show them.
- Convert to more than 100 different formats.
- Edit formats.
- Shutdown or suspend PC after a conversion process.
- Show file information (duration, remaining time, estimated size, progress value).
- Show file details using mediainfo.
- Skip or remove file during conversion process.
- Preview file before conversion.
- Show video thumbnail.
- Convert a specified portion of file.
- Combine subtitle with video.
- Crop and pad video.
- Show error details if exist.
- And more ...


Dependencies:
-------------

For Curlew:

    - python >= 3.3
    - python3-gi >= 3.12
    - python3-dbus
    - gir1.2-gtk-3.0 >> 3.12
    - gir1.2-gstreamer-1.0
    - libav-tools >= 0.8 (or ffmpeg)
    - libavcodec-extra (Ubuntu/Debian)
    - xdg-utils
    - mediainfo
    - gnome-icon-theme-symbolic

For installer (setup.py):

    - librsvg2-bin (or something similar) to convert .svg to .png.
    - intltool-debian (or intltool) to compile translations files.

NB: This dependencies names may change if you are using another distribution than Ubuntu/Debian or its sons.


License:
--------

Waqf public license.
Please see: LICENSE-ar.txt/LICENSE-en.txt files for more information.


Installation:
-------------

In terminal, run the following (as root):
> python3 setup.py install --prefix=/usr
Or run script (as root):
> ./install


Remove (Uninstall):
-------------------

In terminal run the following (as root):
> python3 setup.py uninstall
Or run script (as root):
> ./uninstall


Clean Project:
--------------

> sudo python3 setup.py clean

