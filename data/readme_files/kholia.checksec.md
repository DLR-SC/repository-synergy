checksec.py
===========

This is a rough port of the checksec.sh script by Tobias Klein to Python.

My analysis code combines the original checksec (bash script), rpm-chksec
(Steve's script) and Grant's Go port into one Python code base.

The idea behind this exercise is to make analysis of packages easier and more
accessible. One of the cool things is that you can analyze packages for
different Operating System(s) seamlessly while running a single OS.

Additionally, my code works for all RHEL and Fedora versions (and even deb
based distributions).

The analysis code doesn't install any packages on the system, is host OS
agnostic and is quite fast (scales linearly).

Dependencies
------------

On Fedora 19 (or higher), the following command will install all the required
dependencies.

```
$ sudo yum install pkgwat python-xlwt rpm-python python-pyelftools \
	python-six libarchive-devel python-pip python-libarchive -y

```

Checks Done
-----------

* PIE, RELRO, BIND_NOW

* RPATH, TEMPPATHS, RUNPATH

* Stack Canaries, Non-executable stack

* FORTIFY_SOURCE

* File-based capabilities, setxid

* Polkit policy modification checks


Bulk Analysis Tools
-------------------

Check out scanner.py and scripts under the "scripts" folder.

```
$ ./scanner.py blueman-1.23-7.fc20.x86_64.rpm json # scan a package

$ ./scanner.py Packages/ # scan entire folders
```

Interactive Tools Demo
----------------------

```
✗ python rpm-shell.py
Loading database ...
read: 35229 packages (35229 suggested)

(Cmd) search sudo
texlive-sudoku
texlive-sudoku-doc
texlive-sudokubundle-doc
sudo-devel
ksudoku
libsss_sudo
sudo
sudoku-savant
texlive-sudokubundle
gnome-games-sudoku
gnome-sudoku
vdr-sudoku
libsss_sudo-devel

(Cmd) describe sudo
description: Sudo (superuser do) allows a system administrator to give certain
users (or groups of users) the ability to run some (or all) commands
as root while logging all commands and arguments. Sudo operates on a
per-command basis.  It is not a replacement for the shell.  Features
include: the ability to restrict what commands a user may run on a
per-host basis, copious logging of each command (providing a clear
audit trail of who did what), a configurable timeout of the sudo
command, and the ability to use the same configuration file (sudoers)
on many different machines.
group: Applications/System
ver + rel: 1.8.6p7 1.fc19

(Cmd) analyze sudo
{
    "build": "sudo-1.8.6p7-1.fc19.x86_64.rpm",
    "daemon": false,
    "files": [
        {
            "CANARY": "Enabled",
            "CATEGORY": "None",
            "NX": "Enabled",
            "PIE": "Enabled",
            "RELRO": "Enabled",
            "RPATH": "Disabled",
            "RUNPATH": "Disabled",
            "mode": 34889,
            "name": "/usr/bin/sudo",
            "size": 126608
        },
        {
            "CANARY": "Enabled",
            "CATEGORY": "None",
            "NX": "Enabled",
            "PIE": "Enabled",
            "RELRO": "Enabled",
            "RPATH": "Disabled",
            "RUNPATH": "Disabled",
            "mode": 32841,
            "name": "/usr/bin/sudoreplay",
            "size": 65744
        },
        {
            "CANARY": "Enabled",
            "CATEGORY": "None",
            "NX": "Enabled",
            "PIE": "Enabled",
            "RELRO": "Enabled",
            "RPATH": "Disabled",
            "RUNPATH": "Disabled",
            "mode": 33261,
            "name": "/usr/libexec/sesh",
            "size": 32640
        },
        {
            "CANARY": "Enabled",
            "CATEGORY": "None",
            "NX": "Enabled",
            "PIE": "Enabled",
            "RELRO": "Enabled",
            "RPATH": "Disabled",
            "RUNPATH": "Disabled",
            "mode": 33261,
            "name": "/usr/sbin/visudo",
            "size": 165944
        }
    ],
    "group": "Applications/System",
    "package": "sudo"
}
```

```
✗ python deb-shell.py
Loading ...multiverse/Packages.gz
Loading ...universe/Packages.gz
Loading ...restricted/Packages.gz
Loading ...main/Packages.gz

(Cmd) search sudo
sudo
...
kdesudo
...

(Cmd) analyze sudo
{
    "build": "sudo_1.8.6p3-0ubuntu3_amd64.deb",
    "daemon": true,
    "files": [
        {
            "CANARY": "Enabled",
            "CATEGORY": "None",
            "NX": "Enabled",
            "PIE": "Enabled",
            "RELRO": "Partial",
            "RPATH": "Disabled",
            "RUNPATH": "Disabled",
            "mode": 493,
            "name": "/usr/lib/sudo/sesh",
            "size": 27416
        },
        {
            "CANARY": "Enabled",
            "CATEGORY": "None",
            "NX": "Enabled",
            "PIE": "Enabled",
            "RELRO": "Partial",
            "RPATH": "Disabled",
            "RUNPATH": "Disabled",
            "mode": 493,
            "name": "/usr/sbin/visudo",
            "size": 155640
        },
        {
            "CANARY": "Enabled",
            "CATEGORY": "None",
            "NX": "Enabled",
            "PIE": "Enabled",
            "RELRO": "Partial",
            "RPATH": "Disabled",
            "RUNPATH": "Disabled",
            "mode": 2541,
            "name": "/usr/bin/sudo",
            "size": 121144
        },
        {
            "CANARY": "Enabled",
            "CATEGORY": "None",
            "NX": "Enabled",
            "PIE": "Enabled",
            "RELRO": "Partial",
            "RPATH": "Disabled",
            "RUNPATH": "Disabled",
            "mode": 493,
            "name": "/usr/bin/sudoreplay",
            "size": 64632
        }
    ],
    "group": "admin",
    "package": "sudo"
}
```

As usual, feedback is welcome :-)
