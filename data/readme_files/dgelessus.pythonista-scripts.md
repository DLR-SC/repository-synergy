# pythonista-scripts
A collection of various Pythonista scripts by dgelessus.

## BaseNSudoku
A sudoku solver, originally written for a base 25 sudoku, but works with grids of any size. The number range can be adjusted freely, as well as the width and height of the number blocks to allow non-square blocks and grids. Technically it even works with uncertain (multiple solution) sudokus, however the result will then contain empty sets in place of unknown numbers.

## filenav
A simple file navigator with support for accessing the entire directory structure, not just the Script Library. Additional features include automatic file icons depending on type, analysis of a few basic file attributes, and opening files directly in the default editor.

## filenav_plugin
Plugin for [ShellistaExt](http://github.com/briarfox/ShellistaExt) by [briarfox](http://github.com/briarfox) that adds a filenav command, which opens filenav in either the given or current directory.

## importfinder
Find out where an importable module is located. First tries to find the path "manually" without importing the module, but falls back to `module.__file__` when necessary.

## KeyboardControl
A proof-of-concept for using an external keyboard to control a UI script.

## Multipanel
A way to have multiple views presented in panel mode at once. Due to the builtin-ness of the ui module this cannot directly monkey-patch ui.View.present, views have to be added manually to the multipanel.

## OHaiTerra
A basic hello world script that I put up to use for code download testing.

## PackUI
A means of distribution for .py and .pyui files without requiring any other scripts. The main script packages the two files into a new script, which will extract the files again when run.

## reload_all
Reloads all user modules (i. e. those located in ~/Documents and subfolders) that are currently loaded. Due to Pythonista not being able to properly reset the Python environment, this includes all modules that have been imported since the last time the app was restarted, either manually or after being closed for being inactive for too long.

## rename
A simple script for arbitrary file renaming and moving without Pythonista's default limitations.

## Terra
An extremely useful utility required by OHaiTerra.
