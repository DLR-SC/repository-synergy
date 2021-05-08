Auto (Hard) Wrap for Sublime Text 2/3
====================
[![Build Status](https://travis-ci.org/randy3k/AutoWrap.svg?branch=master)](https://travis-ci.org/randy3k/AutoWrap)
[![Coverage Status](https://coveralls.io/repos/github/randy3k/AutoWrap/badge.svg?branch=master)](https://coveralls.io/github/randy3k/AutoWrap?branch=master)
<a href="https://packagecontrol.io/packages/AutoWrap"><img src="https://packagecontrol.herokuapp.com/downloads/AutoWrap.svg"></a>
<a href="https://www.paypal.me/randy3k/5usd" title="Donate to this project using Paypal"><img src="https://img.shields.io/badge/paypal-donate-blue.svg" /></a>
<a href="https://liberapay.com/randy3k/donate"><img src="http://img.shields.io/liberapay/receives/randy3k.svg?logo=liberapay"></a>

Automatic hard wrap beyond wrap width.  It could be useful for text documents. [Sublime-Wrap-Plus](https://github.com/ehuss/Sublime-Wrap-Plus) could be used together with AutoWrap for the best experience.

![](https://raw.githubusercontent.com/randy3k/AutoWrap/master/demo.gif)

### Installation
[Package Control](http://wbond.net/sublime_packages/package_control)


### Usage

#### To toggle Auto Wrap
Type `Auto Wrap` in command palette or Go to menu `Edit -> Auto Wrap`.

#### Control wrap width

Wrap width is detected in the following order

1. `auto_wrap_width`
2. `wrap_width`
3. `rulers`
4. default 80

### Settings

#### To activate Auto Wrap for a specific syntax at start up

Put the following in your syntax specific preference.<br>
Menu -> Preference -> Settings - More -> Syntax Specific - User

    {
        "auto_wrap" : true
    }

#### You can also change `auto_wrap_width` by

    {
        "auto_wrap_width" : 100
    }

#### Long words

In default, long word will break into a new line.
To disable this behavior, consider

    {
        "auto_wrap_break_long_word" : false
    }

#### Break beyond wrap width only

If true, long sentence will break only if the cursor is beyond wrap width.

    {
        "auto_wrap_beyond_only" : true
    }

#### Break patterns

Upon typing, AutoWrap searches for these characters (in regex, to be concatenate by `|`) and a line would break at (right before) a matched location. Note that Backslash has to be double escaped.

    {
        # it is the default
        "auto_wrap_break_patterns" :  ["\\[", "\\(", "\\{", " ", "\\n"]
    }
