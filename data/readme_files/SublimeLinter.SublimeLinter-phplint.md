SublimeLinter-phplint
=========================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-phplint.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-phplint)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [phplint](http://www.icosaedro.it/phplint/index.html).
It will be used with files that have the "PHP", "HTML", or "HTML 5" syntax.


## Installation

SublimeLinter must be installed in order to use this plugin. 

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before installing this plugin, ensure that `phplint` (2.0 or later) is installed on your system.
To install `phplint`, download and run the appropriate installer from the [download page](http://www.icosaedro.it/phplint/download.html). On Mac OS X, the best option is to install [Homebrew](http://brew.sh) and then enter the following in a terminal:

```sh
brew install phplint
```

If installation via `brew` fails, see [this page](http://georgemastro.com/gcc-4-8-error-unrecognized-command-line-option-fnested-functions/) for possible solutions.

Please make sure that the path to `phplint` is available to SublimeLinter.
The docs cover [troubleshooting PATH configuration](http://sublimelinter.com/en/latest/troubleshooting.html#finding-a-linter-executable).


## Settings

- SublimeLinter settings: http://sublimelinter.com/en/latest/settings.html
- Linter settings: http://sublimelinter.com/en/latest/linter_settings.html
