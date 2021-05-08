# dashman

DASH wallet/daemon management utilities - version 0.1.28

* This script installs, updates, and manages single-user dash daemons and wallets
* It is currently only compatible with 32/64 bit linux.
* Multi-user (system directory) installs are not supported

# Install/Usage

To install dashman do:

    sudo apt-get install python git unzip pv
    cd ~ && git clone https://github.com/moocowmoo/dashman

To update your existing version 12 32/64bit linux dash wallet to the latest
dashd, do:

    dashman/dashman update

To perform a new install of dash, do:

    dashman/dashman install

To overwrite an existing dash install, do:

    dashman/dashman reinstall

To update dashman to the latest version, do:

    dashman/dashman sync

To restart (or start) dashd, do:

    dashman/dashman restart

To get the current status of dashd, do:

    dashman/dashman status


# Commands

## sync

"dashman sync" updates dashman to the latest version from github

## install

"dashman install" downloads and initializes a fresh dash install into ~/.dashcore
unless already present

## reinstall

"dashman reinstall" downloads and overwrites existing dash executables, even if
already present

## update

where it all began, "dashman update" searches for your dashd/dash-cli
executibles in the current directory, ~/.dashcore, and $PATH.  It will prompt
to install in the first directory found containing both dashd and dash-cli.
Multiple wallet directories are not supported. The script assumes the host runs
a single instance of dashd.

## restart

"dashman restart [now]" restarts (or starts) dashd. Searches for dash-cli/dashd
the current directory, ~/.dashcore, and $PATH. It will prompt to restart if not
given the optional 'now' argument.

<a href="#restart-1">screencap</a>

## status

"dashman status" interrogates the locally running dashd and displays its status

<a href="#status-1">screencap</a>

# Dependencies

* bash version 4
* nc (netcat)
* curl
* perl
* pv
* python
* unzip
* dashd, dash-cli - version 12 or greater to update

# Screencaps

### install

<img src="https://raw.githubusercontent.com/moocowmoo/dashman/master/screencaps/dashman_0.1-install.png">

### update

<img src="https://raw.githubusercontent.com/moocowmoo/dashman/master/screencaps/dashman_0.1-update.png">

### reinstall

<img src="https://raw.githubusercontent.com/moocowmoo/dashman/master/screencaps/dashman_0.1-reinstall.png">

### restart

<img src="https://raw.githubusercontent.com/moocowmoo/dashman/master/screencaps/dashman_0.1-restart.png">

### status

<img src="https://raw.githubusercontent.com/moocowmoo/dashman/master/screencaps/dashman_0.1-status.png">

# Contact

Email me at moocowmoo@masternode.me or submit a pull request.
