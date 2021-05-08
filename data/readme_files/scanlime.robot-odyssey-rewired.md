Robot Odyssey Rewired
=====================

Modernized browser port of a classic electronics adventure game.

This repository contains open source modifications which can be applied to the original game. This project was not created by nor endorsed by the game's original authors. Robot Odyssey is Copyright 1984 The Learning Company. The game itself is NOT part of this repository.


Game versions
-------------

Robot Odyssey was originally released for Apple II, with ports to DOS and Color Computer soon after. This project builds on the latest version of the DOS port (1.1), which is similar but not identical to the latest version of the Apple II port (2.0).

Notable differences include the "Robotropolis Preview" only available in Apple II, and the color palette differences. This port offers an extended color palette to emulate the Apple II or CGA palette styles, as well as palettes not possible with either system.


Dependencies
------------

- make
- git
- nasm
- node
- python3
- emscripten


Build Instructions
------------------

Set up dependencies:

- Place Robot Odyssey 1.1 for DOS game files in the "original" directory
- git submodule update --init --recursive
- npm install
- pip3 install -r requirements.txt

To build a static site into the `dist` directory:

- make

To run the development hot-reload server:

- make hotserve

Alternatively, you can just build the static site and serve it from `dist` without hot-reloading:

- make distserve
