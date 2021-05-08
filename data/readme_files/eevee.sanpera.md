# sanpera

sanpera is an imaging library for Python, designed to expose a lot of power with an unsurprising and consistent API.  The goal is to do for image manipulation what requests has done for HTTP.

This is an **extreme** work in progress, but it does do a few useful things.  If it seems useful to you, feel free to give it a spin, and file tickets for whatever's missing or broken!

## Documentation

* [Overview](http://eevee.github.com/sanpera/) on GitHub Pages
* [Full documentation](http://sanpera.readthedocs.org/en/latest/) on readthedocs

## Tech

sanpera is written almost entirely in Cython, because hey, why not.

It's powered by [ImageMagick](http://www.imagemagick.org/script/index.php), but it **is not** a simple wrapper; ImageMagick is merely an implementation detail.

## Goals

* Expose everything ImageMagick can do, smoothing over its idiosyncracies wherever possible.
* Have simple, obvious behavior.
* Be reasonably fast and compact.
* Work with CPython and PyPy.
* Interop where useful: numpy, Cairo, etc.

### Non-goals

* Behave like ImageMagick.
* Work with IronPython or Jython.
* Be as fast or memory-efficient as C.
