Google Closure Linter support for Sublime Text 2
========================

Sublime Text 2 (http://www.sublimetext.com/2) is a sophisticated text editor for code, html and prose. You'll love the slick user interface and extraordinary features.

The Closure Linter (http://code.google.com/p/closure-linter/) enforces the guidelines set by the [Google JavaScript Style Guide](http://google-styleguide.googlecode.com/svn/trunk/javascriptguide.xml). The linter handles style issues so that you can focus on the code.

This project provide a plugin to add Google Closure Linter support for Sublime Text 2.

Features
-------------

- Closure Linter: Run Closure Linter (ctrl+shift+j)

- Closure Linter: Show Closure Linter Result

- Closure Linter: Fix JavaScript Style

- Highlight error line by click on the result view

- Ignore specific Errors in result view

- Cross platform: support Windows, Linux and Mac OS X

Requirements
-------------

- Google Closure Linter http://code.google.com/p/closure-linter/

Installation
-------------

- Using Package Control http://wbond.net/sublime_packages/package_control
    - Add Repository: https://github.com/fbzhong/sublime-closure-linter

- Download and extract to Sublime Text 2 Packages folder
    - Windows:  %APPDATA%\Sublime Text 2\Packages
    - Mac OS X: ~/Library/Application Support/Sublime Text 2/Packages
    - Linux:    ~/.config/sublime-text-2/Packages

How to use?
-------------

- Using the Command Palette (Windows and Linux: Ctrl+Shift+P, OSX: Command+Shift+P) then search for:
    - Closure Linter: Run Closure Linter   (ctrl+shift+j)
    - Closure Linter: Fix JavaScript Style (ctrl+alt+shift+j)
    - Closure Linter: Show Closure Linter Result

- Find them in Tools menu:
    - Tools -> Lint -> Run Closure Linter
    - Tools -> Lint -> Fix JavaScript Style
    - Tools -> Lint -> Show Closure Linter Result

Open up a .js file and hit ctrl+shift+j to run Closure Linter. An new output panel will appear giving you the Closure Linter results:

Screenshots
-------------

![](https://github.com/fbzhong/sublime-closure-linter/raw/master/images/screenshot.png)

Settings
-------------

Settings can be opened via the Command Palette, or the Preferences > Package Settings > Closure Linter > Settings – User menu entry.

    {
        // Path to the gjslint.
        "gjslint_path": "gjslint",

        // Flags pass to gjslint.
        "gjslint_flags": "",

        // Path to the fixjsstyle.
        "fixjsstyle_path": "fixjsstyle",

        // Flags pass to fixjsstyle.
        "fixjsstyle_flags": "",

        // Ignore errors, regex.
        "ignore_errors":
        [
            // "Expected an identifier and instead saw 'undefined' \(a reserved word\)"
        ],

        // debug flag.
        "debug": false
    }

New BSD License
-------------

Copyright (c) 2011, Robin Zhong <fbzhong@gmail.com>
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of the Robin Zhong nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
