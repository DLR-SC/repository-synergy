# Pymodoro

## Running

### Xmobar

Put the files into a new folder called **.pymodoro** inside your home folder. Configure your xmobar to display pymodoro with

    Run CommandReader "~/.pymodoro/pymodoro.py" "pomodoro"

Then add it to your template.

### Dzen2

Add the following configuration to your Dzen2 configuration file to retrieve the current status of your Pomodoro and paste it in your display.

    ^fg(\#FFFFFF)${execi 10 python ~/.pymodoro/pymodoro.py -o}

### i3

The i3 module adds a little extra to pymodoro: it's using a color gradient to display the bar, from green to red depending on how may time is left.
For the gradient to work, you need the `colour` python library first.

    pip install colour

You then need to use [py3status](https://github.com/ultrabug/py3status) an i3status wrapper written in python.

In your `~/.i3/config` file, use `py3status` as your status command and give your pymodoro install directory as an include path:

    status_command py3status -i ~/.pymodoro/

Then add the module to your statusbar conf file (`~/.config/i3status/config` on my setup):

    order += "pymodoroi3"


## Install

To install Pymodoro system wide, run the setup.py script like this:

    python setup.py install
    
You can also install Pymodoro using pip, whithout having to download/clone the code manually:

    pip install git+https://github.com/dattanchu/pymodoro.git

## Usage

A new Pomodoro -- 25 minutes followed by a break of 5 minutes -- is started by changing the timestamp of ~/.pomodoro_session. This can be done by the shell command:

    touch ~/.pomodoro_session

If you want to use counters with different times, write them into the session file. The first number specifies the length of the Pomodoro in minutes, the second one the length of the break. Both numbers are optional. Example:

    echo "20 2" > ~/.pomodoro_session

### Keybindings

The easiest way is to define keybindings for the commands.

#### Xmonad

Configure xmonad to start a new Pomodoro session by adding this to your xmonad.hs:

    -- start a pomodoro
    , ((modMask, xK_n), spawn "touch ~/.pomodoro_session")

Or:

    -- start a pomodoro
    , ("M-n", spawn "touch ~/.pomodoro_session")

This way, whenever you hit modMask + n, you will start a new pomodoro.

#### i3

Here are some shortcuts examples for i3.

    # stop a pomodoro
    bindsym $mod+Shift+f exec rm ~/.pomodoro_session

    # start/reset a pomodoro
    bindsym $mod+Shift+h exec touch ~/.pomodoro_session

## Configure

You can set all the options via command line paramters. For a detailed description run:

    ~/.pymodoro.py --help

It is no longer needed to edit the script itself. If you still want to do it, open up the file **~/.pymodoro/pymodoro.py**.

## Hooks
There are currently two hooks, found in:

    ~/.pymodoro/hooks/start-pomodoro.py
    ~/.pymodoro/hooks/complete-pomodoro.py

Create these files and they will be executed once the pomodoro starts and stop respectively.

## Credits

* Thanks to Mirko Horstmann for [the ticking sound](http://www.freesound.org/people/m1rk0/sounds/50070/).
* Session and Break sounds from Soothing Alerts by [Adam Dachis](http://adachis.kinja.com)
