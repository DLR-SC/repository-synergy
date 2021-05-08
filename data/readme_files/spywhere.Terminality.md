## Terminality

A Sublime Text 3 Plugin for Sublime Text's Internal Console

Branch|[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/spywhere/Terminality?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)|[![Release](https://img.shields.io/github/release/spywhere/Terminality.svg?style=flat)](https://github.com/spywhere/Terminality/releases)
:---:|:---:|:---:
release|[![Build Status](https://img.shields.io/travis/spywhere/Terminality/release.svg?style=flat)](https://travis-ci.org/spywhere/Terminality)|[![Issues](https://img.shields.io/github/issues/spywhere/Terminality.svg?style=flat)](https://github.com/spywhere/Terminality/issues)
master (develop)|[![Build Status](https://img.shields.io/travis/spywhere/Terminality/master.svg?style=flat)](https://travis-ci.org/spywhere/Terminality)|[![License](http://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat)](https://github.com/spywhere/Terminality/blob/master/LICENSE)

![Plugin in Action](http://spywhere.github.io/images/terminality/Terminality.gif)

### What is Terminality
Terminality is a plugin to allows Sublime Text to be used as Terminal. This included input and output from/to Sublime Text's buffer. Although Terminality can run many commands, it **is not gurranteed** that it can be used for all commands.

The command is language-based. Current version support the following languages...

- C
  - Compile and Run
- C++
  - Compile and Run
- Lua
  - Run
- Python
  - Run as Python 2 (`python` command)
  - Run as Python 3 (`python3` command)
- Rust (thanks to @divinites)
  - Run
- Ruby
  - Run
- Swift (OS X only)
  - Run

Is that it? No, Terminality allows you to add your own commands to be used inside Sublime Text. Please see the section belows for more informations.

### How to use it?
Just pressing `Ctrl+Key+R` and the menu will show up, let's you select which command to run.

If you want to pass arguments to command (depends on how each command use the arguments), pressing `Ctrl+Key+Shift+R` instead. This will let's you select the command first, then ask you for arguments input.

`Key` is `Alt` in Windows, Linux, `Cmd` in OS X

**Note!** This key binding is conflicted with SFTP. You might have to override it yourself.

### Settings
Terminality is using a very complex settings system in which you can control how settings affect the whole Sublime Text or each project you want.

As you might already know, you can override default settings by set the desire settings inside user's settings file (can be access via `Preferences > Packages Settings > Terminality > Settings - User`).

But if you want to override the settings for particular project, you can add the `terminality` dictionary to the .sublime-project file. Under this dictionary, it works like a user's settings file but for that project instead.

To summarize, Terminality will look for any settings in your project settings file first, then user's settings file, and finally, the default package settings.

### How Terminality can helps my current workflow?
Good question! You might think Terminality is just a plugin that showing a list of commands which you already know how to use it. Sure, that what it is under the hood but Terminality does not stop there. Here are the list of somethings that Terminality can do for you...

- Run tests on your project
- Exclusively build and run your project without affecting another project
- Dynamically run Sublime Text's commands based on your project or current file
- One keystroke project deployment
- And much more...

### How can I created my own command to be used with Terminality?
You can create your own command to be used with Terminality by override the commands in which using only `execution_units` key in the settings. 

Or if you want to create and share some of your Terminality commands, use the Collections (See Collections section belows).

> In v0.3.7 or earlier, you must set it in `additional_execution_units` instead.  
> In v0.3.8 or later, `additional_execution_units` is deprecated and will be removed in v0.4.0

```javascript
// Settings file
{
	// ... Your other settings ...
	"execution_units": {
		// ... See Language Scopes section belows ...
	},
	// ... Your other settings ...
}
```

#### Language Scopes
Terminality use Sublime Text's syntax language scope in which you can look it up at the status bar when pressing `Ctrl+Alt+Shift+P` (Windows and Linux) and `Ctrl+Shift+P` (OSX).

Language Scope section is a dictionary contains commands which will available for specified language scope.

The key of the language scope is simply a scope name you want to specified. If you want the command to be available to all language just simply use the `*` as a language scope.

You cannot override the default language scope. However, you can remove the default commands for that language scope by set the value to non-dictionary type (such as `0`).

```javascript
"<Language Scope>": {
	// ... See Commands section belows ...
}
```

#### Commands
Command section is a dictionary contains informations about how to run the command.

The key of the command is simply a command name you want to use as a command reference (this will also be used as command name if you did not specified the `name` key).

You can override the command by use the exactly same command reference name of the command you want to override (included default one). And you can also remove the commands by set the value to non-dictionary type (such as `0`).

Each key is optional (exceptions in the Limitations/Rules section belows) and has the following meaning...

- `name` [macros string] A name of the command (which showing in the menu).
- `description` [macros string] A description of the command (which show as subtitle in the menu).
- `order` [string] A string which used for sorting menus
- `location` [macros string] A location path to run the command
- `required` [list] A list of macro name (without $) that have to be set before run the command (if any of the macro is not set, command will not run).
- `arguments` [string] A text to show when ask for arguments input.
- `command` [macros string] A macros string define the command that will be run.
- `window_command` [macros string] A macros string define the Sublime Text's window command (included any plugin you installed) that will be run.
- `view_command` [macros string] A macros string define the Sublime Text's view command (command in which only run within a view) that will be run.
- `args` [dict] A dictionary that will be passed to `window_command` or `view_command`. Each macro inside the dictionary's value will be parsed recursively.
- `platforms` [list] A list of supported platforms. In `<os>-<arch>`, `<os>` or `<arch>` format (`os` and `arch` are from Sublime Text's `sublime.platform()` and `sublime.arch()` command).
- `no_echo` [bool] Specify whether input will be echo (`false`) or not (`true`).
- `read_only` [bool] Specify whether running view can receives input from user (`false`) or not (`true`).
- `close_on_exit` [bool] Specify whether running view will be closed when command is terminated (`true`) or not (`false`).
- `macros` [dict] A dictionary contains custom macro definitions. See Custom Macros section belows.

```javascript
"<Command Reference>": {
	"name": "<Command Reference>",
	"description": "<Command Name> command",
	"order": "<Command Name>"
	"location": "$working",
	"required": [],
	"arguments": "Arguments",
	// You can use only one of "command", "window_command" or "view_command"
	"command": "<No default value>",
	"window_command": "<No default value>",
	"view_command": "<No default value>",
	// "args" will only use with "window_command" and "view_command"
	"args": {},
	"platforms": [<No default value>],
	"no_echo": false,
	"read_only": false,
	"close_on_exit": false,
	"macros": {}
}
```

##### Limitations/Rules

- Every macro name (except inside `required`) should have `$` prefix.
- Each action must contains only one of `command`, `window_command` and `view_command` (other can be omitted)
- `location`, `no_echo`, `read_only` and `close_on_exit` only works with `command` only
- `args` only works with `window_command` or `view_command` only

See example inside Terminality's user settings file (and also in Terminality's .sublime-project file itself!).

### Predefined Macros

- `file`: Path to current working file  
`file_relative`: Relative path of `file`
- `file_name`: Name of `file`
- `working`: This will use `working_project` but if not found it will use `project` and if still not found it will use `parent`  
`working_relative`: Relative path of `working`
- `working_name`: Name of `working`
- `working_project`: Project folder contains current working file  
`working_project_relative`: Relative path of `working_project`
- `working_project_name`: Name of `working_project`
- `project`: First project folder  
`project_relative`: Relative path of `project`
- `project_name`: Name of `project`
- `parent`: Parent folder contains current working file  
`parent_relative`: Relative path of `parent`
- `parent_name`: Name of `parent`
- `packages_path`: Path to Sublime Text's packages folder
- `raw_selection`: Raw text of last selection
- `selection`: Striped text of last selection
- `arguments`: A text which passed via arguments input
- `sep`: Path separator (`/` or `\` depends on your operating system)
- `$`: `$` symbol

### Custom Macros
You can create your own macro to be used with custom command by adding each macro to `macros` section in your execution unit (See Commands aboves). Each macro is a key-value pairs in which key indicated macro name (`a-zA-Z0-9_` without prefixed `$`) and value is a list of any combination of the following values...

- `"String and/or $macro"` This will be a parsed string (which must not contains self-recursion) if previous value is not found
- `["Start:End"]` This will substring the previous value (if any) from `start` to `end`
- `["RegEx Pattern", <Optional Capture Group>]` This will return a specified group (or default match if not specified) from previous value matching
- `["String and/or $macro", "Start:End"]` This will substring the specified string/macro from `start` to `end` if previous value is not found
- `["String and/or $macro", "RegEx Pattern", <Optional Capture Group>]` This will return a specified group (or default match if not specified) from specified string/macro matching if previous value is not found

Substring works just like Python's substring. You can omitted `start` or `end` as you like.

Macro works as a sequence, if current macro is not found it will look at the next macro.

Example:

```javascript
"CustomMacro": [
	"$file_name", // Get the file name from predefined macro
	[":-4"], // Remove the last 4 characters (if value is found)
	["$file", "\\w+"], // Get the result from parsing "$file" with RegEx if previous value is not found
	"" // If nothing can be used, use empty string
]
```

### Collections

> *Implemented in v0.3.8 and later*

Collections is a package contains Terminality commands which can be install by place in the `User` directory.

The structure of Collections file is simply a JSON file with .terminality-collections extension. Inside the file contains the following format...

```javascript
{
	"execution_units": {
		// ... See Language Scopes section aboves ...
	}
}
```

Please note that Collections is not a settings file (although it contains the same key name). Any other key will be ignored completely.

### Contributors
- @utensil
- @zmLGBBM
- @divinites
