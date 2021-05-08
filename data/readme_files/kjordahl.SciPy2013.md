This repository contains materials for the tutorial `Using Geospatial Data With Python`_ to be held Jun 25, 2013, at the SciPy 2013 conference.

.. _Using Geospatial Data With Python: http://kjordahl.github.io/SciPy2013

Required packages
-----------------

- `pyproj`_ python interface to PROJ.4 library
- `Basemap`_ plot on map projections using matplotlib
- `gdal`_ python bindings for Geospatial Data Abstraction Library (and OGR)
- `shapely`_ pythonic library for geometric tasks
- `fiona`_ pythonic interface to OGR data formats

Optional packages
------------------

- `Cartopy`_ Advanced mapping interface for python
- `Descartes`_ Create matplotlib Patch objects from Shapely geometries
- `geoJSON`_ reference implementation of the Python geo interface
- `psycopg2`_ for connection to PostgreSQL/PostGIS database
- `SQLAlchemy`_ Object Relational Model for SQL databases

.. _pyproj: http://code.google.com/p/pyproj
.. _Basemap: https://github.com/matplotlib/basemap
.. _Cartopy: http://scitools.org.uk/cartopy
.. _Descartes: https://pypi.python.org/pypi/descartes
.. _geoJSON: https://pypi.python.org/pypi/geojson
.. _gdal: https://pypi.python.org/pypi/GDAL
.. _shapely: http://toblerity.github.io/shapely
.. _fiona: http://toblerity.github.io/fiona
.. _psycopg2: https://pypi.python.org/pypi/psycopg2
.. _SQLAlchemy: http://www.sqlalchemy.org

Installation instructions
-------------------------

The standard `scientific python stack`_ is a prerequisite for this tutorial before installing the specific packages listed above.  I recommend starting with a standard scientific python distribution such as `Enthought Canopy`_ or `anaconda`_.  All students for SciPy tutorials will have received a free license for Canopy for a limited period of time (also free for `academic use`_, and anyone can use the free Canopy Express).  Other package managers such as Linux distribution tools or `homebrew` for OS X will work for a starting point as well, though I have not tested these.  On Windows you may be able to use `Christoph Golke's binary packages`_.

Install the above packages via your standard package manager when possible.  For packages not available in this way (or if you wish to use a different version than available), you may install directly with `pip` or `easy_install`.  For example, to install Shapely, you may use::

    pip install shapely

Finally, if all else fails, or you wish to be on the bleeding edge, you may install packages from source.  For example::

    git clone https://github.com/Toblerity/Shapely
    cd Shapely
    python setup.py install

will install the current development version of Shapely.

Serge Ray has shared `his setup notes`_ for OS X 10.8.4 and anaconda. 

.. _Enthought Canopy: https://www.enthought.com/products/canopy
.. _anaconda: https://store.continuum.io/cshop/anaconda
.. _scientific python stack: http://www.scipy.org/install.html
.. _academic use: https://www.enthought.com/products/canopy/academic
.. _Christoph Golke's binary packages: http://www.lfd.uci.edu/~gohlke/pythonlibs
.. _his setup notes: osx-anaconda.md

Known installation issues
-------------------------

- Importing shapely in Canopy version 1.0.1 on OS X `fails`_ while loading the GEOS library, and throws an exception of the form "OSError: Could not find library c or load any of its variants".  This can be fixed by upgrading to Canopy 1.0.3 (available soon) or worked around by setting the following environment variable::

    export DYLD_FALLBACK_LIBRARY_PATH=$(HOME)/lib:/usr/local/lib:/lib:/usr/lib

- The GDAL 1.9.0 package in Canopy fails to find the PROJ.4 library for some operations.  It should work for other use cases.

- GDAL binary libraries may not be found even when they are installed, particularly when installing fiona.  The fiona install process uses the command `gdal-config --cflags` to find header files.  This should match your GDAL install location.
You may need to install GDAL on your system.  A number of `binaries`_ are available, or you could use a package manager such as fink or apt-get, or build it from source.

- Dependency errors installing `psycopg2` in Canopy and EPD.  This may be overcome by downloading the `psycopg2` .egg file from the `Enthought PyPI mirror`_ and installing it manually with the `egginst` command, or with `pip install psycopg2`.  Windows users can try `this binary installer for psycopg2`_ which has been reported to work.

.. _fails: http://stackoverflow.com/questions/17072797/enthought-canopy-cytpes-util-find-library-cant-find-libc
.. _binaries: http://trac.osgeo.org/gdal/wiki/DownloadingGdalBinaries
.. _Enthought PyPI mirror: https://www.enthought.com/repo/pypi/eggs
.. _this binary installer for psycopg2: http://www.stickpeople.com/projects/python/win-psycopg/
