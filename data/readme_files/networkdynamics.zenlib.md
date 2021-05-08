![Zen logo](http://www.networkdynamics.org/static/zen/zen_logo.png)

Zen is a Python library that provides a high-speed, easy-to-use API for analyzing, visualizing and manipulating networks.

Official site: http://zen.networkdynamics.org/

## Installation

To install zenlib do the following:

- ``git clone`` the repository
- Install: cython>=0.14, numpy>=1.6.1
- ``cd`` to ``src/`` and run ``python setup.py install``

Here is an example of the installation process using [virtualenv](http://www.virtualenv.org/en/latest/index.html) for
convenience:

    git clone https://github.com/networkdynamics/zenlib.git
    virtualenv --distribute zenlibenv
    (zenlibenv) pip install cython
    (zenlibenv) pip install numpy
    (zenlibenv) cd zenlib/src/
    (zenlibenv) python setup.py install

License: BSD
