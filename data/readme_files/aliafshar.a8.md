
# a8, the Abominade IDE #

2019 Update: Enabled Vim-gtk3

(c) 2011, PIDA Authors
License GPL v3 (http://www.gnu.org/copyleft/gpl.html)

The One True IDE™, successor to the PIDA IDE. An ultra-lightweight IDE, that
embeds Vim, a terminal emulator, and a file browser and makes them work
together.

* [Installation](#installation)
* [Configuration](#configuration)
* [Keyboard Shortcuts](#keyboard-shortcuts)
* [Extensions](#extensions)
* [FAQ](#faq)
* [Intentional Breakages](#intentional-breakages)
* [SSH Tips and Tricks](#ssh-tips-and-tricks)

![a8 screenshot](https://lh4.googleusercontent.com/-PtipCpFvTcc/TvpPhtdtTeI/AAAAAAAADI0/tUVBvU3uLAA/s0-d/a8.png)

----

## Installation ##

⠠⠊⠝⠎⠞⠁⠇⠇⠁⠞⠊⠕⠝

```
$ pip install a8
```
Remember the system dependencies:
```
# apt-get install vim-gtk python-gtk2 python-vte python-dbus
```
(non debian distros, please drop me a line to add you.)

----

## Configuration


a8 is a bit configurable. Not so much because I never planned on using it in more than one way.

### Configuration file

Create a config file at `~/.a8/config.yaml`

As the name suggests it will be in Yaml, as a map of key values:
```
foo1: blah
foo2:
    foo3: blah
```

### Terminal Configuration ###

Is the biggest bit, terminal options live under the `temrinal` key, and these
are them, with default values if they exist (or Unset otherwise):
```
  terminal:
    'color_foreground': Unset,
    'color_background': Unset,
    'backspace_binding': Unset,
    'cursor_blink_mode': Unset,
    'cursor_shape': Unset,
    'font': Unset,
    'allow_bold': Unset,
    'audible_bell': Unset,
    'emulation': Unset,
    'pointer_autohide': Unset,
    'scroll_on_keystroke': Unset,
    'scroll_on_output': Unset,
    'scrollback_lines': 1000,
    'visible_bell': Unset,
    'word_chars': '-A-Za-z0-9,./?%&#:_',
```

### Window Configuration ###

To turn on the toolbar:
```
toolbar: true
```

### Session Configuration ###

Abominade 0.11 supports 3 session types:
```
session_type: 'none'   # don't remember sessions (alias for "session: false")
session_type: 'local'  # stores session in the ./.a8 wherever abominade runs
session_type: 'user'   # default, stores session in ~/.a8
```
To turn off sessions in 0.10 and earlier:
```
session: false
```

### Terminals in a separate window ###

Useful for multiple screens:
```
terminal_window: true
```
----

## Keyboard Shortcuts ##

⠠⠅⠑⠽⠃⠕⠁⠗⠙ ⠠⠎⠓⠕⠗⠞⠉⠥⠞⠎

Keyboard shortucts are of two types:

1. Internal a8 actions
2. Custom shell commands

Define keyboard shortcuts by creating the file:

`~/.a8/shortcuts.yaml`

This file should contain keys and values of the form:

`<action>: <shortcut>`

or of the form

`key: <shortcut>`

`[cmd: <command>]`

`[cwd: <working directory>]`

`[env: <environment>]`


Where action is a string defining the action to be performed, and shortcut is a shortcut string.

### Available actions ###

Available actions are (with defaults):

* `shell (<Alt>t)`
* `focus_vim (<Alt>e)`
* `focus_terminal (<Alt>r)`
* `focus_buffers (<Alt>b)`
* `focus_files (<Alt>m)`
* `focus_terminals (<Alt>i)`
* `focus_bookmarks (<Alt>k)`
* `prev_buffer (<Alt>Up)`
* `next_buffer (<Alt>Down)`
* `prev_terminal (<Alt>Left)`
* `next_terminal (<Alt>Right)`
* `refresh_files (<Alt>g)`
* `toggle_expanded_files (<Alt>x)` (0.11 and later)
* `close_all_buffers (<Alt>c)`
* `browse_home (<Alt>h)`

### Other hotkeys ###

* pressing `<Shift>Up` and `<Shift>Down` in terminals will jump to prev/next
prompt (or at least the scrollbar position where you last hit Enter)

### Shortcut format ###

The format looks like `<Control>a` or `<Shift><Alt>F1` or `<Release>z` (the last
one is for key release). The parser is fairly liberal and allows lower or upper
case, and also abbreviations such as `<Ctl>` and `<Ctrl>`. Keys such as `Up`,
`Down`, `Left`, `Right` etc are available, but be careful, the keypress will not
pass through to the underlying app, terminal or Vim.

### Custom shortcuts ###

These are custom shell commands bound to a keyboard shortcut. Their format is different from internal a8 shortcuts. They should be part of a list in the value of the `custom` key. Each item in the list should define at least the key `key` as a shortcut string in the format above. Additionally they may define `cmd`, `cwd` and `env` keys. These are used to execute a new terminal with the command.

### Example file ###

An example shortcut file might look like:

```
shell:     <Control>o
focus_vim: <Alt>Space

custom:
  - key: <Alt>j
    cmd: ifconfig
```
----

## Extensions ##
⠠⠑⠭⠞⠑⠝⠎⠊⠕⠝⠎

A8 is slightly extensible, to the absolute minimal degree to add functionality without having the burden of a massive framework. This is achieved by the concepts of:

1. Extensions
2. Signals

Since we are just using Python, all the a8 API is public to any Python code in the same process, and that is intentional. If you want to break it by abusing this, go for it, break it.

Extensions are any Python module or instance with a callable `setup` attribute. The signature of `setup` should be:

```
def setup(app):
   """My setup function."""
```

Of course this can be in an object where the signature would be:

```
class MyExtension(object):

  def setup(self, app):
    "My setup function."""
```

Extensions are listed in the configuration file under the `extensions` key, and should be importable names, such as `a8.a8_example_ext`, an example to get you started. If importing an attribute from a module, the `:` notation can be used, such as `path.mymodule:myattr`, which would be suitable for an instance as an extension.

The app that is passed to the `setup` function is an instance of `a8.app.Abominade` which is the main monolith for a8, i.e., it has access to everything. Terrible, but intentional.

The `setup` function can be used to create user interface features and to connect to signals, and as mentioned above, since all the API is public, anything can be achieved using this.

### Signals ###

A8 exports a number of signals for use by extensions. They are not used internally, so mostly behave as a no op. These are connected using `app.connect` and can be emitted by using `app.emit`. 

`app.connect` takes a signal name, and a callback to be called. Callbacks are only passed keyword arguments, so it is important to get the names of the arguments correct. here is an example of connecting to the `file-saved` signal in a plugin. All available signals and arguments are listed below.

```
def on_file_saved(filename):
  print filename, 'was saved.'

def setup(app):
  app.connect('file-saved', on_file_saved)
```

### Available Signals ###

| *Name*                | *Arguments*        | *Description*                                 |
|-----------------------|--------------------|-----------------------------------------------|
| `file-item-added`     | `filename`         | File item is shown in the file manager        |
| `file-opened`         | `filename`         | File opened in the editor                     |
| `file-closed`         | `filename`         | File closed in the editor                     |
| `bookmark-item-added` | `filename`         | Bookmark to `filename` is added               |
| `terminal-executed`   | `argv` `env` `cwd` | New terminal has been executed                |

If you need more signals, just let us know. Since they are not used internally, there is basically no cost.

----

## FAQ ##
⠠⠋⠠⠁⠠⠟

### What happened to my favourite PIDA feature? ###

Abominade doesn't hope to replace [http://pida.co.uk PIDA], how could it? So if
you require some special PIDA features, please go ahead and use PIDA.
[Intentional Breakages](#intentional-breakages)

### Does it work on a Mac? ###

Probably, with difficulty. You'll need X, Gtk, DBus, all with Python support. (and possibly psychiatric help)

----

## Intentional Breakages ##
⠠⠊⠝⠞⠑⠝⠞⠊⠕⠝⠁⠇ ⠠⠃⠗⠑⠁⠅⠁⠛⠑⠎

Features intentionally left out of Abominade that make it simpler, but
essentially a tool written for me. If you want a real application, try
[https://bitbucket.org/aafshar/pida-main/wiki/Home PIDA]. The motivation for
Abominade is to make an IDE that is tailor-made to me.

* Internationalization (I only ever use English)
* Non-Vim editors (I only ever use Vim)
* Language support (I don't find those outliners useful)
* Version control support (Command line is enough)
* Project support (Replaced with bookmarks)
* Gui configuration (Plain text is enough)
* Gui shortcut config (As Gui config)
* Window management (Detaching, moving, hovering, floating)
* Saving layout
* Documentation (ok, so PIDA doesn't have any, either!)
* Lots of options (No need to make stuff optional that I use.)
* GTK's Actions are a pain
* Glade/GTKBuilder is a pain
* GTK's stock icons are totally useless
* Statusbar/Toolbar/menubar

----

## SSH Tips and Tricks ##
⠠⠎⠠⠎⠠⠓⠀⠠⠞⠊⠏⠎⠀⠁⠝⠙⠀⠠⠞⠗⠊⠉⠅⠎

Abominade's features work surprisingly well for working remotely over SSH.

### SSHFS ###

If you edit a lot of code on remote hosts, you can mount your project directory
locally via SSHFS.

If you then SSH directly from a mounted local dir to the corresponding remote
dir, Abominade's terminal filename recognition will still catch relative
filenames. This will break if you cd in your SSH session so that relative paths
don't match your local current dir anymore, but if you configure SSH's
!EscapeChar setting, you can suspend SSH, cd locally, and resume SSH.

Another interesting trick is you start Abominade in an SSHFS dir while using
a local session, the session will be shared with remote instances at the same
path, and can be resumed on a different host.

### Screen/tmux ###

It's a good idea to use GNU screen or tmux for some terminals in Abominade's
terminals pane, since it's easy to accidentally close Abominade
and lose your terminal history.

### Vim's Built-in SSH Support ###

Haven't used this much in Abominade...
