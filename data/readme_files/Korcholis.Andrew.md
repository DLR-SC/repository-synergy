# Andrew #

Andrew is a lightweight Android Development Project for Sublime Text 2 and Sublime Text 3. It makes use of [Monitor](http://developer.android.com/tools/help/monitor.html) to get a fully functional environment for Android development, without the hassle of a big IDE.

## Recent Changes ##

###0.3.2###

* Added support for Windows (locate SDK, create/import projects, use of Monitor)
* Removed DDMS, Devices and SDK Manager, and changed them for Monitor (the mix of all of them from the latest versions of Android SDK)
* Import updates a project, so it can be used with Andrew and Sublime Text
* Added some shortcuts

###0.3.1###

* Moved to Github
* Removed Windows support (until it is finally on)

###0.3###

* `Refactor... > String` grabs a text in your opened file and refactors it into `res/values/strings.xml`

###0.2###

* Major menu restructuring.
* Debug compiling is done on background when `Andrew > Compile... > Compile on Save` is on.
* Added DDMS option, along with SDK Manager and Devices Manager.
* Resources is populated after an On-save compile or when empty. Now it loads faster and works with the last resources.

###0.1###
* First version

## Requirements ##

In order to use Andrew, you need:

* [Android SDK](http://developer.android.com/intl/es/sdk/index.html), installed into your computer and with an Android Platform version installed. Any requirement related to this is also a requirement here.
* For Linux users, set the permissions for your devices (See [here](http://developer.android.com/intl/es/tools/device.html#setting-up) how to do so).
* ant (you need this for compiling Android applications).

## First steps ##

Before you start coding, you should set your environment. 

1. Go to the `Andrew > Preferences > Locate SDK` command and choose whether you prefer to write it down manually or search it automatically.
2. Go to the `Andrew > Preferences > Workspace path` command and select where you want to create projects by default. More or less like the Eclipse workspace.
3. Check everything worked by clicking `Andrew > Android managers > Android SDK Manager`. If everything worked you should see the Android SDK Manager window. Otherwise, check the console in order to see any error.
4. Start coding:
	1. Create a project using Android > New Android Project and follow the steps, _or_
	2. Use your already created project by opening the project's root folder.
		1. If you do so, you'll have to run `<Android-SDK-Path>/tools/android update project --path /path/to/project` to generate a build.xml file.

## Coding Helps ##
### Layout Snippets ###

Use snippets for any layout item. This eases the development of layouts, letting you move across the typical parameters by using `Tab`

### Resources ###

Tired of writing R.id. _widgetid_ all the time? Hit `Ctrl+Shift+Alt+R` (or `Super+Shift+Alt+R` on Mac OS X) and decide what to put using a menu.

### Compile and send to Device ###

There's the option to compile as debug or release (and if you have a keystore, you can directly sign any release .apk), but you can also compile as debug and send it to the first device connected to the computer, automatically opening it when installed. Just the way you used to do in Eclipse, but with Sublime Text 2.

## At the moment ##

Andrew is at its earliest version, due to the time I can spend with it. That's why I encourage everybody who wants to improve this plugin to fork and create new features or get the existing ones better.

Actually, it only works at this moment for Unix based platforms (Linux/Mac OS X).

## Early future ##

The first thing to change is compiling asynchronously after every save. Well, actually working more on background and less on foreground.

## Contributors ##

Have you got a glorious feature you'd like to include? Have you found a bug and you fixed it? Are you giving Windows compatibility? Do you think you can improve this project (and, I tell you, you definitely can)? Fork the project and make a pull request. I'll check by myself and eventually merge with the project.

## License ##

This is an open git project for Sublime Text 2. Anyone can contribute here, fork, use this project however you want. It is free of charge, and comes with no warranty. Always use this along with a versioning system to avoid any problem. Use at your own risk.

[![githalytics.com alpha](https://cruel-carlota.pagodabox.com/11a8d94fa4fd2098219b0d8b5e069986 "githalytics.com")](http://githalytics.com/Korcholis/Andrew)