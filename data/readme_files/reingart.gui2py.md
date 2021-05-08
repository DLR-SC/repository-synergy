gui2py
======

gui2py is a GUI framework for building cross-platform "visual" desktop applications on Windows, Mac OS X, and Linux, 
using the Python language and the wxPython toolkit.

Its objetive is to evolve [PythonCard](http://pythoncard.sourceforge.net/) with [web2py's](http://www.web2py.com/) 
philosophy and facilities.

Its goals includes a KISS compact structure, visual tools (designer, inspector and property editor), 
HTML/Javascript-like capabilities, modern MVC patterns support, and compatibility with multiple versions of wxPython 
and Python (including py3k and the upcoming wx version 3.0 -a.k.a. Phoenix-). 

![gui2py visual designer in action](https://gui2py.googlecode.com/hg/screenshots/win8/designer.png)

For more information see the main project site: https://code.google.com/p/gui2py

Installation Instructions:
--------------------------

You need at least [wxPython 2.9.4](http://www.wxpython.org/download.php) to use the development tools, as they depends 
on the latest features added to wxWidgets.

Download & uncompress the [source code zip archive](https://github.com/reingart/gui2py/archive/master.zip),
or check out the git repository using mercurial [hg-git](http://hg-git.github.io/) (or git directly):

    hg clone git+https://github.com/reingart/gui2py.git
    cd gui2py
    python setup.py install

Then, try the minimal application the main directory, double clicking the minimal.pyw file or running:

    python minimal.pyw

Or, try the sample application in the same directory, double clicking the sample.pyw file or running:

    python sample.pyw

Also, you can start the GUI designer with:

    python -m gui.tools.designer

For the extensive instructions (including packages for each major O.S.), see the 
[Installation Guide](https://code.google.com/p/gui2py/wiki/InstallationGuide)
