# When (*when-command*)
**When** is a configurable user task scheduler for modern Gnome environments. It interacts with the user through a GUI, where the user can define tasks and conditions, as well as relationships of causality that bind conditions to tasks.

![Screenshot](https://raw.githubusercontent.com/almostearthling/when-command-docs/master/_static/when_screenshot_part.png)

The purpose of this small utility is to provide the user, possibly without administrative credentials, the ability to define conditions that do not only depend on time, but also on particular states of the session, result of commands run in a shell or other events that may occur while the system is being used. The scheduler runs in the background, and displays an indicator applet icon for user interaction.

It is not generally intended as a replacement to [_cron_](https://en.wikipedia.org/wiki/Cron) and the [Gnome Task Scheduler](http://gnome-schedule.sourceforge.net/), although to some extent these utilities might overlap. **When** is intended to be more flexible, although less precise, and to provide an alternative to more complicated solutions -- such as the implementation of _cron_ jobs that check for a particular condition and execute commands when the condition is verified. In such spirit, **When** is not as fine-grained in terms of doing things on a strict time schedule: the **When** approach is that "_when_ a certain condition is met, _then_ something has to be done". The condition is checked periodically, and the countermeasure is taken _subsequently_ in a relaxed fashion, which means that it might not occur _immediately_ in most cases.

[![Documentation Status](https://readthedocs.org/projects/when-documentation/badge/?version=latest)](http://when-documentation.readthedocs.io/en/latest/?badge=latest)

The complete documentation for **When** can be found online [here](http://when-documentation.readthedocs.io/). Documentation for contributors has a separate [site](http://contributing-to-when.readthedocs.io/).

## Installation
Besides manual installation from source as explained in the [documentation](http://when-documentation.readthedocs.io/en/latest/install.html#install-from-the-source), packages suitable for Ubuntu can be found in the [releases](https://github.com/almostearthling/when-command/releases) page. A PPA for Ubuntu is also available: to install from the PPA and get automatic updates, the following commands can be used from a terminal window:

```
$ sudo add-apt-repository ppa:franzg/when-command
$ sudo apt-get update
$ sudo apt-get install when-command
```

If the PPA is used, **When** can be started from the *Dash* immediately: once started, it can be configured for autostart using the *Settings* dialog box.

## Alternate Interface
Besides being fully configurable and accessible from both the command line interface and the graphical user interface, an alternate and more streamlined GUI for **When** is being actively developed: the [When Wizard](https://github.com/almostearthling/when-wizard) suite can be used to create actions in **When** in a possibly easier way.

## Credits
Open Source Software relies on collaboration, and I'm more than happy to receive help from other developers. Here I'll list the main contributions.
- Adolfo Jayme-Barrientos, aka [fitojb](https://github.com/fitojb), for the Spanish translation

Also, I'd like to thank everyone who contributes to the development of **When** by commenting, filing bugs, suggesting features and testing. Every kind of help is welcome.

The top panel icons and the emblems used in the application were selected within Google's [Material Design](https://materialdesignicons.com/) icon collection.

Application [icon](http://www.graphicsfuel.com/2012/08/alarm-clock-icon-psd/) by Rafi at [GraphicsFuel](http://www.graphicsfuel.com/).

## Resources
The resources that I have found particularly useful in the development of **When** are:
- [Python 3.x Documentation](https://docs.python.org/3/)
- [PyGTK 3.x Tutorial](http://python-gtk-3-tutorial.readthedocs.io/en/latest/index.html)
- [PyGTK 2.x Documentation](https://developer.gnome.org/pygtk/stable/)
- [PyGObject Documentation](https://developer.gnome.org/pygobject/stable/)
- [GTK 3.0 Documentation](http://lazka.github.io/pgi-docs/Gtk-3.0/index.html)
- [DBus Documentation](http://www.freedesktop.org/wiki/Software/dbus/)
- [pyinotify Documentation](https://github.com/seb-m/pyinotify/wiki)

The guidelines specified in [UnityLaunchersAndDesktopFiles](https://help.ubuntu.com/community/UnityLaunchersAndDesktopFiles) have been roughly followed to create the launcher from within the application.

Many hints taken on [StackOverflow](http://stackoverflow.com/) and the like.
