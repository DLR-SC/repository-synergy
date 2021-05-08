# `mog`

A different take on the UNIX tool `cat`.

![example](mog.gif)

[![Travis](https://img.shields.io/travis/witchard/mog.svg)](https://travis-ci.org/witchard/mog)
[![license](https://img.shields.io/github/license/witchard/mog.svg)](https://witchard.mit-license.org)
[![PyPI](https://img.shields.io/pypi/pyversions/mog.svg)](https://pypi.python.org/pypi/mog)
[![PyPI](https://img.shields.io/pypi/v/mog.svg)](https://pypi.python.org/pypi/mog)
[![AUR](https://img.shields.io/aur/version/mog-git.svg)](https://aur.archlinux.org/packages/mog-git/)

## What is this?

The man page for `cat` says that it can: concatenate files and print on the standard output. Often (at least for me) its main use is for the latter... `mog` tries to help you "print on the standard output" in a more intelligent way. For example, it can be configured to:

* Syntax highlight scripts
* Print a hex dump of binary files
* Show details of image files
* Perform `objdump` on executables
* List a directory

## Installation

The simplest way is to install via pip: `[sudo] pip install mog`.

Required dependencies are the `file` command (e.g. `sudo apt install file`).

If you plan on using the default configuration file, then you will also want `poppler-utils`, `binutils` and `mediainfo` installed (e.g. `sudo apt install poppler-utils binutils mediainfo` on a debian based machine). You'll also need `pygmentize` - this should be installed automatically with `pip install mog`, but some users have reported this not to be the case (e.g. issue #18) - if this happens a separate `pip install pygments` will hopefully do the trick.

@gregf has kindly provided an Arch Linux package: https://aur.archlinux.org/packages/mog-git/. There is also a FreeBSD port: https://www.freebsd.org/cgi/ports.cgi?query=%5Emog&stype=name&sektion=sysutils.

For the latest development version:
* `[sudo] pip install git+https://github.com/witchard/mog`
* Or clone this repository and then run `[sudo] python ./setup.py install`

## Default Config

If you don't give `mog` a configuration file, it will use the defaults. Here is what you will get (prioritised in the order below - i.e. the first thing to match is done)

* File extension is recognised by pygments - Format with `pygmentize` (http://pygments.org/)
* File mime type is recognisd by pygments - Format with `pygmentize` (http://pygments.org/)
* File type is ELF - Parse with `objdump -ft`
* File is not a file (i.e. directory / symlink / fifo) - List it using `ls -lh`
* File is of a video or image mime type - Summarise it with `mediainfo` (http://mediainfo.sourceforge.net)
* File is a PDF document - Print it as text using `pdftotext` (https://poppler.freedesktop.org/)
* File is a tar archive - List contents of tar using `tar --list`
* File extension is .deb - Show information using `dpkg -I`
* File extension is .rpm - Show information using `rpm -qip`
* File extension is .csv - Format it using `column -xt -s,`
* File extension is .tsv - Format it using `column -xt`
* File contains ASCII text - Print using `cat`
* Anything else - Assumed to be binary, print using `xxd`

## How does it work?

`mog` reads the `$HOME/.mogrc` config file which describes a series of operations it can do in an ordered manner. The config file can be overridden with the `--config` argument. Each operation has a match command and an action command. For each file you give to `mog` it will test each match command in turn, when one matches it will perform the action. A reasonably useful config file is generated when you first run it.

### Matches

Currently the following match commands are supported:

* `name=<regex>` - Check if the file name matches the regex
* `file=<regex>` - Check if the output of `file` matches the regex
* `file_mime=<regex>` - Check if the output of `file --mime` matches the regex
* `pygmentize=<regex>` - Check if the output of `pygmentize -N` matches the regex
* `pygmentsmime=<regex>` - Check if the pygments lexer for the files mimetype matches the regex. Always failes when there is no pygments lexer for the specified mimetype

Note, one can specify `invert_match`, you can use this to cause a match when the regex does not match.

### Actions

The following actions are supported:

* `arg=<program>` - Pass the file name as an argument to the program
* `argreplace=<program>` - Replace %F in `<program>` with the filename. Replace %N (where N is an integer) in `<program>` with matching capture group from match regex. Execute the result.

### Config file format

The config file is an ini style format defined as follows:

```ini
[settings]
showname=yes
showsection=no
viewinless=no
toponly=no
toplines=10
followsymlinks=no
recursive=no

[name-of-match-action-1]
match=arg
action=arg
invert_match=boolean

[name-of-match-action-2]
match=arg
action=arg
invert_match=boolean
```

The `settings` section may contain the following:

* `showname` - default: `True`. Show the name of each file before performing the action.
* `showsection` - default: `False`. Show config file section where match occurred next to file name. `showname` must be `True` for this to work.
* `viewinless` - default: `False`. Output everything in a pager (`less -S`).
* `toponly` - default: `False`. Output only the top few lines of each file.
* `toplines` - default: `10`. Number of lines to output in `toponly` mode.
* `followsymlinks` - default: `False`. Follow symbolic links when processing files.
* `recursive` - default: `False`. Recurse into directories to process the files within them.

The `invert_match` value is optional and will cause the match to be inverted - i.e. you can use this to cause a match when the regex does not match.

Matches and actions will be processed in the order found in the file.

It should be noted that `mog` uses the name of the script to determine what config file to read. So for example one can `ln -s mog feline` and then it would use the `$HOME/.felinerc` as the config file. This means you can have multiple configurations for different names.
