## Future development of VPython has moved to a new project

This incarnation of VPython will not be developed further; see [this announcement](http://vpython.org/contents/announcements/evolution.html) for an explanation and [this history](https://matterandinteractions.wordpress.com/2016/04/27/a-time-line-for-vpython-development/) of the development of VPython. Development efforts are now focused on [VPython 7](https://github.com/BruceSherwood/vpython-jupyter), which runs with installed Python, including in a Jupyter notebook, and an in-browser version that requires no local installation at all and runs on mobile devices, at [glowscript.org](http://glowscript.org).

The home of vpython on the web is still at [vpython.org](http://vpython.org).

## Read on for more information about the old VPython...

vpython-wx
==========

[![Build Status](https://travis-ci.org/BruceSherwood/vpython-wx.png?branch=master,stable)](https://travis-ci.org/BruceSherwood/vpython-wx)

VPython 6, at [vpython.org](http://vpython.org), is based on the
cross-platform library wxPython. It improves VPython 5.74 and earlier by
eliminating most platform-dependent code and by eliminating the
threading associated with rendering.

The new version makes essential changes to the `rate` statement in VPython
programs:

* `rate` is now required; an animation loop **MUST** contain it.
* `rate` still limits the number of loop iterations per second.
* `rate` now updates the 3D scene when appropriate, about 30 times per second.
* `rate` now handles mouse and keyboard events.
* If the animation loop is missing the `rate` statement, the scene will not
   be updated until and unless the animation loop is completed.

The heart of the user-interface code, creating windows and handling events,
is the file *site-packages/visual_common/create_display.py*.  It is
imported by *visual/__init__.py* and by */vis/__init__.py*; *visual*
imports *math* and *numpy* for convenience whereas *vis* doesn't.

Please report issues to the
[Github repository](https://github.com/BruceSherwood/vpython-wx), or to the
[VPython forum](https://groups.google.com/forum/?fromgroups&hl=en#!forum/vpython-users).
