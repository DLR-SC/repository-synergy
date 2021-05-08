sikuli_cpython
==============

A CPython wrapper around the sikuli standalone jar

Why
---
Sikuli is traditionally written in Jython, which is painful if you want to mix it with Selenium scripts. This module makes it possible for CPython to run the Jython scripts created by Sikuli-IDE.

How it works
------------
This module wraps the sikuli standalone jar using [pyjnius](https://github.com/kivy/pyjnius) from the Kivy project. Pyjnius allows us to use java classes in CPython.

Requirements
------------
* 32-bit JDK
* 32-bit Python 2.7
* cython 0.19.2
* pyjnius 1.1-dev

Installation
------------

###On Linux/Mac
Ensure your python instance (virtualenv or global) meets all the above requirements
Run `pip install sikuli`

###On Windows:
Simply run `pip install sikuli`, this will install cython if not already installed, pyjnius, and sikuli.
Make sure the path to a jvm.dll is in your PATH environment variable. The path should be: `C:\Program Files (x86)\Java\jdk[YOUR JDK VERSION]\jre\bin\server`

Troubleshooting
---------------
* If `pip install sikuli` times out, try `pip --default-timeout=100 install sikuli`. It's downloading a jar from PyPi, so it may take longer than your average module.
* pyjnius is known to be inconsistent in Window 7 64-bit. If you see a jvm memory error, try relogging into your profile.
