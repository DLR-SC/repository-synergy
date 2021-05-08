# SciPy2016 tutorial: Introduction to NumPy

This repository contains all the material needed by students registered for the
Numpy tutorial of SciPy 2016 on Monday, July 11th 2016.

For a smooth experience, you will need to make sure that you install or update
your Python distribution and download the tutorial material _before_ the day
of the tutorial as the Wi-Fi at the AT&T center can be flaky.


## Python distribution and Packages needed

If you don't already have a working python distribution, by far the easiest
way to get everything you need for this tutorial is to download Enthought
Canopy ([https://store.enthought.com/](https://store.enthought.com/),
the free version is sufficient), or Continuum's Anaconda
([http://continuum.io/downloads](http://continuum.io/downloads)).

If you have the choice, I recommend to use a Python 2.7 distribution, which
is what I will be using and my material as been tested with that. If you have
a Python 3.4+ version, you should be fine, though you might have to replace a
print statement (`print a`) by the print function (`print(a)`) in some of the
solution files.

To be able to run the examples, demoes and exercises, you must have the
following packages installed:

- numpy 1.10+
- matplotlib 1.5+
- ipython 4.0+ (for running, experimenting and doing exercises)
- nose (only to test your distribution, see below)

If you use Canopy, everything you need will be installed by default. If you
use `conda`, you can create a new environment using the following command:

    $ conda create -n numpy-tutorial python=2 numpy matplotlib nose ipython

To test your installation, please execute the `check_env.py` script. The
output should look something like this:

    $ python check_env.py
    ....
    ----------------------------------------------------------------------
    Ran 4 tests in 0.162 s

    OK


## Content needed

This GitHub repository is all that is needed in terms of tutorial content. The simplest solution is to download the material using this link:

https://github.com/enthought/Numpy-Tutorial-SciPyConf-2016/archive/master.zip

If you're familiar with Git, you can also clone this repository with:

    $ git clone https://github.com/enthought/Numpy-Tutorial-SciPyConf-2016.git

It will create a new folder named SciPy2016_numpy_tutorial/ with all the
content you will need: the slides I will go through (`slides.pdf`), and a folder
of exercises.

As you get closer to the day of the tutorial, it is highly recommended to
update this repository, as I will be improving it this week. To update it, open
a command prompt, move **into** the SciPy2016_numpy_tutorial/ folder and run:

    $ git pull


Questions? Problems?
====================
Questions? Problems? Don't wait, shoot me and the rest of the group an email on
the tutorial mailing list: https://groups.google.com/forum/#!forum/scipy-2016-numpy-tutorial
