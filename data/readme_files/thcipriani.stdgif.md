stdgif
======

Standard output for gifs.

Dumps gifs to stdout or creates shell scripts that can be sourced from a
``.bashrc`` or other shell initialization file.

.. image:: http://tyler.zone/stdgif-bootie-dog.gif
   :alt: Bootie Dog approved

.. image:: http://tyler.zone/stdgif-readme.gif
   :alt: Jerimiah Johnson approved

.. image:: http://tyler.zone/stdgif-spiderman.gif
   :alt: Spiderman Mind Blown

The clever algorithm (that I had nothing to do with) that shows
amazing ANSI renderings of images was ported from Stefan Haustein's
TerminalImageViewer_.

.. _TerminalImageViewer: https://github.com/stefanhaustein/TerminalImageViewer

Use ``pip`` to install::

  pip install stdgif

Requirements:

* Requests_
* Pillow_

.. _Requests: http://docs.python-requests.org
.. _Pillow: https://python-pillow.org/

Usage::

  stdgif [-h] [-w WIDTH] [-f] [-d DELAY] [-o OUTPUT] [-s SEPERATOR] img


  -w <WIDTH>, --width <WIDTH>

     Set the output width of the resulting gif

  -f, --forever

      Loop the gif in the terminal until you hit Ctrl-C

  -d <DELAY>, --delay <DELAY>

      Delay in seconds between frames of the gif

  -o <FILE>, --output <FILE>

      Generate bash script path, if this option is passed, rather than output
      the gif on stdout, stdgif will generate a bash script that can be executed
      to show the gif. This bash script is, of course, suitable for sourcing
      from a ``.bashrc`` or other shell initialization file.

  -s <SEPERATOR>, --seperator <SEPERATOR>

      The value of <SEPERATOR> will be printed between each frame of the gif

  img

     The gif that you want to show
