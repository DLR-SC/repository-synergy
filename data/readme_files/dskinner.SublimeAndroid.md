# SublimeAndroid

## NOTICE

This project is currently on hold (not discontinued) as much of the functionality
for completions are being continued here: https://github.com/quarnster/completion

This is a work in progress for SublimeText 3!

Expects a properly configured android project via sdk command line tools. From
project directory:

```
android update project -p ./
```

## Installation

This package depends on a submodule.

For a fresh install:

```
git clone --recursive git://github.com/dskinner/SublimeAndroid.git
```

If updating from a previous install without the submodule

```
git pull
git submodule init
git submodule update
```

## Features

* Automatically configures external packages.
	* SublimeJava
	* SublimeLinter
	* ADBView
* Identifies project directory and target platform for autocompletion.
* XML autocompletion (incomplete) in layouts for tags, attributes and values.
* Identifies multiple android projects in a sublime project.
* Build commands for ant
* Launch sdk tools

## Setup automatic builds

### Ant

Create a new target in `custom_rules.xml`:

```xml
<target name="compile" depends="-set-debug-mode, -compile"/>
```

Add the following to sublime project settings

```
"sublimeandroid_default_ant_target": "compile"
```

This will perform just enough to allow for quick builds and provide autocompletion via SublimeJava
