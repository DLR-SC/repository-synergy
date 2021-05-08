Super Calculator
================
* Author: Chiel Robben
* License: MIT
* Website: http://pephers.org

About
-----
Super Calculator is a plugin for Sublime Text 2 and Sublime Text 3 which lets you do inline calculations with a few keypresses. This is useful for example to subtract paddings from your widths in your CSS code.

Usage
-----
All you need to do is to press `Alt+C` and Super Calculator will select the mathematical expression closest to the cursor position so you can review what is going to be calculated. A second time `Alt+C` calculates the result and inserts it right away. Nice!

![](/images/usage.gif)

Configuration
-------------
By default, Super Calculator rounds the result down to two decimals. However, you can specify the number of decimals you would like in the user settings file for Super Calculator. The settings files can be found by navigating to `Preferences -> Package Settings -> Super Calculator`.

Installation
------------
**With Package Control:** The easiest way to install Super Calculator is by using the [Package Control plugin](http://wbond.net/sublime_packages/package_control).

**Without Git:** Download the latest source from [GitHub](https://github.com/Pephers/Super-Calculator) and copy the Super Calculator folder to your Sublime Text "Packages" directory.

**With Git:** Clone the repository in your Sublime Text "Packages" directory:

    git clone https://github.com/Pephers/Super-Calculator.git

The "Packages" directory can be found in the following locations:

* OS X:

        ~/Library/Application Support/Sublime Text 2/Packages/
        ~/Library/Application Support/Sublime Text 3/Packages/

* Linux:

        ~/.config/sublime-text-2/Packages/
        ~/.config/sublime-text-3/Packages/

* Windows:

        %APPDATA%/Sublime Text 2/Packages/
        %APPDATA%/Sublime Text 3/Packages/

