# A Sublime Text 2/3 plugin to show build output in a view.

[![Gratipay me!](https://img.shields.io/badge/Donate-gratipay-663300.svg)](https://gratipay.com/~rctay) [![Donate with Bitcoin](https://img.shields.io/badge/Donate-BTC-orange.svg)](https://blockchain.info/address/19xm5wFxyrue9Ncdhw3qLysmYAh7NSxbAc) [![Donate with Ethereum](https://img.shields.io/badge/Donate-ETH-blue.svg)](https://etherscan.io/address/0x1e4625a37f0bC6f37F6785e74Acdcb9C9473A3Ba)

In Sublime Text, build results are shown in a fixed horizontal panel; you
can't drag it to put it vertically next to your code, like in Eclipse, VS.

With this plugin, like any other view, you can put your build results where
you want:

![buildview vertical](https://github.com/rctay/sublime-text-2-buildview/raw/master/buildview.png)

This is super useful if you are repeatedly running a program on your code/
script and want to have its output handy. (You probably already have a
`.sublime-build` or `build_systems` entry in your `.sublime-project`.)

The core functionality is done in `pipe_views.PipeViews`, an abstraction
allowing Unix-like "pipes" to be created between Views in Sublime.

# Usage

The plugin hooks on to the keyboard shortcuts for launching builds; if you
have different shortcuts for them, change the `.sublime-keymap` files
accordingly. These bindings **must** have the following context:

	"context": [{"key": "build_fake", "operator":"equal", "operand":true}]

Several aspects of the plugin's behaviour can be changed as detailed below. They
can be changed on a per-view basis via the Command Palette in either the view
source code or with build output, or through settings under `"buildview"`.

Note: it seems settings set via Command Palette are persisted through sublime
exits/launches.


## Disabling

**Command Palette**:
- Disable/Enable buildview for this window

**key**: `"buildview.enabled"`
**values**: `true`/`false`

Sublime's [settings hierarchy](http://docs.sublimetext.info/en/latest/customization/settings.html#the-settings-hierarchy)
is respected. So you could, for example, enable the plugin only for selected
projects, by setting `"enabled"` to `false` in
`Packages/User/Preferences.sublime-settings`, and set it to `true` in your
`.sublime-project`.

For example, you can add this to your `Preferences.sublime-settings`:

    {
    	...
    	"buildview.enabled": false
    	...
    }

Then in the project's `.sublime-project` file:

    {
    	...
    	"folders": [...]
    	"settings": {
    		"buildview.enabled": true,
    		"buildview.scroll": "top"
    	}
    	...
    }

(`"scroll"` added for demonstration; for details on `"scroll"`, refer below.)



## Output scrolling

**Command Palette**:
- Build output always at top
- Build output always at end
- Build output stays at same position

**key**: `"buildview.scroll"`

**values**:
 - `"top"`
 - `"bottom"`
 - `"last"`

**default**: `"bottom"`

The plugin can scroll the output to the top, bottom, or the position before the
current build was launched. The default is to scroll to the bottom (ie.
continually show fresh output as it is emitted).


## "Save changes?" warning

**key**: `"buildview.silence_modified_warning"`

**values**: `true`/`false`

**default**: `true`.

Since version 90e2365182e9566b2fa79dd7dc79d6b0d7e433f6 (Package Control: 2014.01.27.15.16.48),
closing the build output view, directly, or indirectly, eg. by exiting
Sublime Text, no longer causes a "Save changes?" warning to be displayed.

If you wish to have the old behaviour (of having a warning displayed), set to
`false`.


## Suppress build results panel

The built-in build results view will display momentarily. To disable this, use
the User preference setting:

    {
    	...
    	"show_panel_on_build": false,
    	...
    }


# Known Issues/TODO

 - pin/unpin location, so that subsequent builds scrolls to the same location
 - build view is "forgotten" after restarting Sublime
 - improve disabling/enabling options (eg whitelists, blacklists)
 - improve namespacing of settings into a dictionary, once sublime supports
   merging of settings dictionaries through the hierarchy. For example, if
   buildview hypothetically read settings from a dictionary, and you had in your
   `Preferences.sublime-settings`

       {
       	...
       	"buildview": {
       		"enabled": false,
       		"scroll": "top"
       	}
       	...
       }

   and you then did this in the project's `.sublime-project` file

       {
       	...
       	"folders": [...]
       	"settings": {
       		"buildview": {
       			"enabled": true
       		}
       	}
       	...
       }

    buildview would behave as though the `"scroll"` setting was not defined
    because sublime does not automatically merge settings dictionaries through
    the settings hierarchy, so the `"scroll"` setting does not bubble up.


Pull requests welcome!

# Hacking notes

 - after editing `pipe_views.py`, restart Sublime or re-save `commands.py` 
   for the changes to take effect.
 - _who's view is it anyway?_ A variety of names are used for views in the
   source code, according to their different roles:
   - source view: the built-in view that shows up when you click Show Build
     Results
   - destination view: the view that mirrors the build output, the one with the
     title "Build Output"
   - otherwise, a view should generally refer to one holding the source for the
     build

# Donate

If you liked this plugin, you can donate here:  
[![Gratipay me!](https://img.shields.io/badge/Donate-gratipay-663300.svg)](https://gratipay.com/~rctay) [![Donate with Bitcoin](https://img.shields.io/badge/Donate-BTC-orange.svg)](https://blockchain.info/address/19xm5wFxyrue9Ncdhw3qLysmYAh7NSxbAc) [![Donate with Ethereum](https://img.shields.io/badge/Donate-ETH-blue.svg)](https://etherscan.io/address/0x1e4625a37f0bC6f37F6785e74Acdcb9C9473A3Ba)

