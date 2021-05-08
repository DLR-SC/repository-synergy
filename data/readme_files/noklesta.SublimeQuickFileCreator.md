# Quick File Creator plugin for Sublime Text

Plugin that lets you quickly create a file or a subdirectory using ST's fuzzy
matching feature.

Normally, in order to create a file or directory in ST, you have to navigate
to the parent directory in the side panel and right-click on it, or you can open a new
tab and save it using the operating system's save dialog (which may start in a
directory completely unrelated to your project if you don't have any files
already opened).

This plugin instead pops up a quick panel that lets you pick the directory for
the new file or subdirectory using the built-in fuzzy matching. If you are
currently editing a file, that file's directory will be located at the top of
the list to make it even easier to create the new file or subdirectory in the
same location. Select a directory, input the new name in the input panel at
the bottom of the window, and you're done!

The quick panel lists all the directories inside any open project folders,
including folders that have been added using the ST project menu.

The file/folder input panel supports recursive folder or file creation. If the
parent path does not exist then the path will be created.

## Installation

### Package Control

The easiest way to install this is with [Package
Control](http://wbond.net/sublime\_packages/package\_control).

 * If you just went and installed Package Control, you probably need to restart Sublime Text before doing this next bit.
 * Bring up the Command Palette (Command+Shift+p on OS X, Control+Shift+p on Linux/Windows).
 * Select "Package Control: Install Package" (it'll take a few seconds)
 * Select Quick File Creator when the list appears.

Package Control will automatically keep Quick File Creator up to date with the latest
version.

### Clone from GitHub

Alternatively, you can clone the repository directly from GitHub into your Packages directory:

    git clone http://github.com/noklesta/SublimeQuickFileCreator

## Usage

Bring up the Command Palette and select "Quick File Creator: Create file" or
"Quick File Creator: Create directory", or set up some key bindings as
explained below.

## Key bindings

The plugin now installs key bindings automatically. Alternatively you can set
up your own key bindings like this by adding to your user key bindings file:

    { "keys": ["super+ctrl+o"], "command": "quick_create_file" },
    { "keys": ["super+ctrl+d"], "command": "quick_create_directory" }

If you are using Vintage mode and want to use sequences of non-modifier keys,
you can restrict the key bindings to command mode like this:

    { "keys": [" ", "n"], "command": "quick_create_file", "context": [{"key": "setting.command_mode"}] },
    { "keys": [" ", "d"], "command": "quick_create_directory", "context": [{"key": "setting.command_mode"}] }

## Excluded directories

Some directories, such as those named ".svn" or ".git", are excluded by default
in order to make the directory listing easier to navigate. You can override
this setting by specifying a list of regular expressions either in
Packages/User/SublimeQuickFileCreator.sublime-settings or, for a particular
project, in the project file under a top-level "settings" key. It might be a
good idea to copy the list in
Packages/SublimeQuickFileCreator/SublimeQuickFileCreator.sublime-settings and
modify it.

Note that each pattern is anchored to the beginning and end of the directory
name, so you should not use ^ or $ in your patterns. Also, since ST does not
allow backslashes in settings files, use a vertical bar (|) instead of a
backslash to escape special regex symbols such as dots in directory names.

Example of setting the list of excluded directories in your user preferences file:

    {
      "SublimeQuickFileCreator": 
      {
        "excluded_dir_patterns": 
        [
          "tmp", "|.git", "|.svn"
        ]
      }
    }

...and in a project file:

    {
      "folders":
      [
        {
          "path": "/path/to/project"
        }
      ],
      "settings":
      {
        "SublimeQuickFileCreator":
          {
            "excluded_dir_patterns":
            [
              "tmp.*", "|.git", "|.svn", "|.hg"
            ]
          }
      }
    }

## Future work

It seems to me that ST does not currently support programmatically selecting
a directory in the side bar (please correct me if I'm wrong!). If ST includes
this ability in the future, I will make any newly created subdirectories
become immediately selected.

## Licence

All of SublimeQuickFileCreator is licensed under the MIT licence.

  Copyright (c) 2012 Anders Nøklestad

  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:

  The above copyright notice and this permission notice shall be included in
  all copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
  THE SOFTWARE.
