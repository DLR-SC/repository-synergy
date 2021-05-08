# spin

a small utility to assist in setting usage modes of laptop-tablet devices

# features

- automatic palm rejection when using stylus
- automatic disable/enable of touchpad and nipple when device toggled between laptop and tablet states
- manual control of display orientation and input devices

# setup

This utility requires X11.

Install PyQt5. On Ubuntu 16.04 LTS, run the following:

```Bash
sudo apt install python-qt5
```

On Ubuntu 18.04 LTS, run the following:

```Bash
sudo apt install pyqt5-dev pyqt5-dev-tools
```

Now install spin by running the following:

```Bash
sudo pip install python_spin
```

To set up globally a Linux desktop launcher with icon, execute the following:

```Bash
sudo wget --content-disposition -N -P /usr/share/icons/ https://raw.githubusercontent.com/wdbm/spin/master/python_spin/static/spin.svg

sudo wget --content-disposition -N -P /usr/share/applications/ https://raw.githubusercontent.com/wdbm/spin/master/python_spin/static/spin.desktop
```

# quick start

This utility can be run in its default graphical mode or in a non-graphical mode. The graphical mode is engaged by running

```Bash
spin
```

while the non-graphical mode is engaged by using the option `--no_GUI`:

```Bash
spin --no_GUI
```

There are other options which are described by `spin --help`.

By default, this utility disables the touchscreen on detecting the stylus in proximity and it changes between the laptop and tablet modes on detecting toggling between the laptop and tablet usage configurations. These default behaviours are provided by both the graphical and non-graphical modes of this utility. This utility should be initiated in the laptop usage configuration.

# compatibility

|**computer model**|**operating system and setup**|**comment**                                     |
|------------------|------------------------------|------------------------------------------------|
|ThinkPad S1 Yoga  |Ubuntu 16.04 (X11, Unity)     |working                                         |
|ThinkPad S120 Yoga|Ubuntu 16.04 (X11, Unity)     |working                                         |
|ThinkPad Yoga 14  |Ubuntu 16.04 (X11, Unity)     |possibly working with some reduced functionality|
|ThinkPad Yoga P40 |Ubuntu 16.04 (X11, Unity)     |possibly working                                |

# acceleration control

There is an experimental acceleration control included which is deactivated by default. It can be activated by selecting the appropriate button in the graphical mode.

# future

Under consideration is state recording in order to avoid execution of unnecessary commands and better handling of subprocesses.
