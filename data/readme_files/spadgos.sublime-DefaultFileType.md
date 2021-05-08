This package sets the default file type of new files to be either the same as the current file, or a predefined default.

This only affects files which are created with the `Ctrl+N` shortcut (`Cmd+N` on OSX).

## Installation ##

### With Package Control ###

If you have the [Package Control][package_control] package installed, you can install DefaultFileType from inside Sublime Text itself. Open the Command Palette and select "Package Control: Install Package", then search for DefaultFileType and you're done!

### Without Package Control ###

Go to your Sublime Text 2 Packages directory and clone the repository using the command below:

    git clone https://github.com/spadgos/sublime-DefaultFileType.git DefaultFileType

## Configuration ##

Create a file in your `Packages/User` directory called `default_file_type.sublime-settings` and you can set these options:

- `default_new_file_syntax` *(String)* This is the path, relative to the Sublime base directory to the language file you'd like to load as the default. Default value is `"Packages/Java/Java.tmLanguage"`
- `use_current_file_syntax` *(Boolean)* Set this to `true` to use the current file's syntax for the new file. If `false`, then the default (above) will always be used. Default value is `true`

Let me know if you have any problems or feature requests by adding an issue here: https://github.com/spadgos/sublime-DefaultFileType

[package_control]: http://wbond.net/sublime_packages/package_control
