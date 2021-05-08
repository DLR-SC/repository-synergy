Diffy
============================

This is a file comparison plugin for both Sublime 2 and 3. 

Enjoy!

### Installation
Please install Sublime [Package Control]("https://sublime.wbond.net/installation") first. Then inside *Package Control: Install Package*, type *Diffy* and then click to confirm.

### Usage
After installing the plugin, set the layout to be 2 columns via *View -> Layout -> Columns: 2*. And make sure you have files (or temporary files pasted from clipboard) opened side by side.

1. To compare and show the diffs, press **CTRL + k** followed by **CTRL + d**.
2. To clear the marked lines, press press **CTRL + k** followed by **CTRL + c**.

### Settings
#### The default key binding for Mac is

```
{ "keys": ["super+k", "super+d"], "command": "diffy" }
{ "keys": ["super+k", "super+c"], "command": "diffy", "args": {"action": "clear"} }
```

#### The default key binding for Windows / Linux is

```
{ "keys": ["ctrl+k", "ctrl+d"], "command": "diffy" }
{ "keys": ["ctrl+k", "ctrl+c"], "command": "diffy", "args": {"action": "clear"} }
```
