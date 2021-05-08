# Kanna ASCII art bleeder script

[![ScreenShot](https://i.imgur.com/5L3OHCC.gif)](https://streamable.com/ojcd4)

Reddit user /u/2hu4u was inspired by the ascii art bleeding of Kanna
as found in the opening of the anime "Kobayashi-san Chi no Maid Dragon",
that they recreated one based on that.  Later someone in that Reddit
thread
[mentioned](https://www.reddit.com/r/anime/comments/5uxjn4/i_recreated_the_kanna_ascii_art_from_kobayashisan/ddxpkga/)
how this needs to be done in Python... and so here it is.

## Requirements

A standard Python installation with the `curses` library available, with
a big enough terminal with small fonts for best effects.  Tested to work
under Linux.  Should also work under OS X and Windows 10 with the WSL
(Windows Subsystem for Linux) installed.  For Windows 10, it was
reported to be working under `bash` inside `cmd`.

Will not work anywhere where the `curses` library is unavailable, i.e.
standard Windows installations, will result in an import error like so:

```
C:\Users\Demo\kanna>python asciibleed.py kanna1.txt
Traceback (most recent call last):
  File "asciibleed.py", line 8, in <module>
    from curses import setupterm
  File "C:\Python27\lib\curses\__init__.py", line 15, in <module>
    from _curses import *
ImportError: No module named _curses
```

## Usage

Clone (or download an archive of) this repository, then run it by
calling the file (original mode)

```
$ git clone https://github.com/metatoaster/kanna
$ cd kanna
$ clear  # clear the screen for best effect (Ctrl-L works too)
$ python asciibleed.py kanna.txt
```

For the scripted mode, the `-s` flag can be provided for the file that
defines the frames (basically a file with its first line being a list of
`:` separated filenames to text files, then a list of `,` separated
numbers denoting which frames to use per slide).  A `animated.txt` is
provided to make use of all four frames of Kanna provided.

```
$ python asciibleed.py -s animated.txt
```

Finally, run it with a background - the `maiddragon.txt` "monitor" is
also provided, run it like so:

```
$ python asciibleed.py -s animated.txt -b maiddragon.txt
```

If you don't want to see Kanna slide off the screen you can run it
in place by specifying the offset be 0

```
$ python asciibleed.py -s animated.txt -b maiddragon.txt -o 0
```

There are a couple other flags that can be toggled (try using `-h`).

## Credits

Naturally, the original art was done by /u/2hu4u so thank that user
otherwise this wouldn't have been possible.
