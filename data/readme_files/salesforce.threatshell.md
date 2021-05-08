Threatshell
===========

Threatshell is a python-based command line shell aimed at providing security
researchers with a single, integrated environment for gathering information
from various intelligence APIs and analysis scripts, and storing all of the
obtained information into one or more elasticsearch instances. The goal of
keeping the results in elasticsearch being to provide a historical search
mechanism for all of the gathered information, and to start building a clever
event analyzer to assist in hunting and analysis activities.


Notes
=======

Please see the docs for installation help and for threatshell usage details.

I recommend using python virtual environments (virtualenvs) if you don't
already. If you'd like to use a virtualenv, I detail (roughly) how to set one
up in [**the docs**](http://threatshell.readthedocs.io/en/latest/install.html),
and there are plenty of awesome tutorials for setting up and using virtualenvs
out there already if you still have questions.


Documentation
=================

Threatshell's documentation can be found
[**here**](http://threatshell.readthedocs.io/en/latest/index.html)


Quick Start
==============

You can get up and running with threatshell with the following few steps -

First, you'll need the GeoIP library for geocoding IP addresses.

On ubuntu:

    sudo apt-get install libgeoip-dev

On OSX:

    brew install GeoIP

Then activate your virtualenv if you're using one for the next commands

    # make sure pip is up to date if you want
    pip install --upgrade pip

    # you can install everything with
    # pip install -r requirements.txt
    # or
    # python setup.py install

    pip install -r requirements.txt

Now you can start up threatshell with

    python threatshell.py

If it's your first time running threatshell, it will create a config
directory, `$HOME/.threatshell`, and prompt you for a password for the
crypto key it generates to keep all of your config's secrets safe. Then,
once your key is generated, it asks for your API keys and other settings.
You can just enter through the prompts and set the keys later with the
[**config management commands**](http://threatshell.readthedocs.io/en/latest/commands.html#config-management-commands)
