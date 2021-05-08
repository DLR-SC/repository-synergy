## Make Sublime Text Dark and Beautiful on GTK+ 3

This **Sublime Text 2/3 plugin** sets the [dark theme variant](https://developer.gnome.org/gtk3/3.0/GtkSettings.html#GtkSettings--gtk-application-prefer-dark-theme) for Sublime's windows on GTK+ 3-based systems that support it, such as recent GNOME distributions.

The result is a much more beautiful Sublime when using dark UI themes because the distracting contrast between title bar and chrome is eliminated. The window border also becomes dark, making the window blend into the desktop better.

### Before (Sublime Text 3 on Fedora 20)

![Before](https://raw.githubusercontent.com/p-e-w/GTKDarkThemeVariantSetter/images/before.png)

### After

![After](https://raw.githubusercontent.com/p-e-w/GTKDarkThemeVariantSetter/images/after.png)

## Installation

### Through Package Control (recommended)

1. Run "Package Control: Install Package" from the Sublime Text Command Palette (<kbd>Shift+Ctrl+P</kbd>)
2. In the list, select "GTKDarkThemeVariantSetter" and press <kbd>Return</kbd>

### Manually

1. `cd` into your Sublime Text packages directory (e.g. `.config/sublime-text-2/Packages`)
2. Run `git clone https://github.com/p-e-w/GTKDarkThemeVariantSetter.git`

## How it works

Sublime Text (like most other extensible applications) does not provide hooks into its low-level windowing logic. This plugin demonstrates a technique that nevertheless allows for fine-grained control over windows, provided that standard Linux and X.Org tools are present on the system:

1. Find the application's process ID by name with `pidof [NAME]`
2. Find all top-level windows (and their IDs) with `xprop -root _NET_CLIENT_LIST`
3. For each window ID thus found, get the associated process ID with `xprop -id [ID] _NET_WM_PID`
4. If the process ID thus obtained matches the application's process ID, set the dark theme variant for the window with `xprop -id [ID] -f _GTK_THEME_VARIANT 8u -set _GTK_THEME_VARIANT dark` (some background on this very poorly documented property can be found [here](https://mail.gnome.org/archives/commits-list/2011-May/msg05622.html) and [here](http://unix.stackexchange.com/a/24071))

## License

Copyright © 2014 Philipp Emanuel Weidmann (<pew@worldwidemann.com>)

Released under the terms of the [MIT License](http://opensource.org/licenses/MIT)
