AS OF EARLY 2008, THIS INFORMATION IS OBSOLETE.
SEE INSTALL.txt instead.

The following notes were written by Jonathan Brandmeyer, June 2006.

This directory is a kind of sandbox that I'm using to build 
and test a new OpenGL rendering engine for VPython.
Dependancies (in Debian):
libboost-python-dev
libboost-thread-dev
ftgl-dev
libgle3-dev
libgtkglextmm1-dev
(Note: In Debian Sid, you will need to build gtkglextmm 1.2 from source, and
	apt-get install libgtkmm-2.4-dev)
scons

Notes for building:
Assuming you have all of the development packages that the new core expects,  
make sure that you edit the value of 'VISUAL_PREFIX' in include/vpython-config.h
to be the path to the source tree.  VPython uses SCons to build itself, and does
not include any kind of 'install' target, yet.  Instead, it builds its target
programs and libraries in-place in a layout similar to what you would find under
/usr

Directory layout
SConstruct
	A scons build file for this project.  Run `scons` to build the
	Python extension module.  Run 'scons bin/' to run the C++ tests.
run	A script that sets up environment variables to use the target libs and
	plugin.  ex: './run python2.3' will place site-packages/ in sys.path.
bin/  
	Programs are built in-place here.  To run any of the tests, prefix the
	command with the run script, like: './run bin/sphere_texture_test'.
	For a python program, say "./run python bin/bounce2.py'.
lib/
	Target libraries are built in-place here.
site-packages/
	The Python plugin module is built here.
site-packages/visual/
	The parts of the Python plugin that are written in Python are placed
	here.
include/
	Header files for the basic objects.
include/util/
	Header files for utility classes, like tmatrix, and vector.
include/gtk1/
	Classes for Gtk 1.2 + gtkglarea (defunct)
include/gtk2/
	Classes for Gtkmm + GtkGLExtmm
src/core/
	Implementations of classes defined in include/
src/core/util/
	same, for include/util/
src/gtk1/
	same, for include/gtk1
src/gtk2/
	same, for include/gtk2.  Also includes implemetations of some platform-
	specific utility classes for POSIX systems.
src/python/
	Implementations of the Boost.Python wrapper code.
src/test/
	A series of test programs used to excersize the individiual
	parts of this library.  These are written in pure C++.
	

TODO (*-ed items are must-do, w/l items are wishlist items):
	* Port to GTK on Windows (done)
	* Forward-port changes to support numeric/numarray (done)
	* Remove libgle dependancy; integrate advanced curve type (done)
	* Provide simple texture API (done)
	* Pango+texture text rendering; Remove FTGL dependancy (done)
	* Write simple icons for the toolbar widgets
	* Verify performance of the autoscaler, particularly with regards to
		frustum depth parameters. (done)
	* Autotoolize the project (done)
	* Fix any+all bugs identified in examples/*.py (in progress)
	* Provide compatability interface for lighting (done)
	* Update INSTALL.txt, NEWS.txt (done)
	-------- 4.0.BETA0 release here ---------
	* Write demo of display_kernel integration using PyGTK
	* Generic texture support for all objects.
	* Generic transparency for all objects.  Consider full-scene polygon sorting
		of translucent bodies.
	* Write documentation for new features
		- lighting
		- display_kernel
		- new scaling effects
		- texturing
	* Ability to disable the toolbar
	* Optimize away extra display_kernel::pick() calls
	* Investigate slowness (mostly done)
	* Add points object
		- support GL_POINT_SPRITE?
	* Additional features as users request
	* Fix bugs identified with ALPHA0 and BETA0
	