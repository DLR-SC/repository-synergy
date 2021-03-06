# vim-pad

A quick notetaking plugin for vim.

It offers a similar way of managing notes to the one made popular by tools like
Notational Velocity, where file management is removed from the notetaking
workflow, being replaced by searching and sorting facilities, and where the
creation and searching of notes is integrated.

Notes in vim-pad are free-form; in fact it tries to make it easy to use any
format you want. It works great along other plugins like
[VimOutliner](https://github.com/vimoutliner/vimoutliner/) and
[quicktask](https://github.com/aaronbieber/quicktask).

**IMPORTANT**: `vim-pad` requires a reasonably recent version of Vim (7.4 is
recommended) with `+python` (`+python3` also works in `devel`) and `+conceal`
support. Check if the flags are enabled in `:version`. Currently, it also
requires either a `grep` with perl regexes support, which might not be the case
under OSX, `ack`, `ag` or `pt`. Windows is not supported.

![screen1](https://raw.githubusercontent.com/fmoralesc/vim-pad/devel/doc/ss-vim-pad.png)

![screen2](https://raw.githubusercontent.com/fmoralesc/vim-pad/devel/doc/ss-filter-query.png)

![screen3](https://raw.githubusercontent.com/fmoralesc/vim-pad/devel/doc/ss-incsearch.png)

## Branches

* `devel` contains the development version of the plugin.

Pull requests are to be done over `devel`. When submitting a bug, please tag
the affected versions.

## Configuration and Usage

**IMPORTANT**: you must set the g:pad#dir variable to a valid path. It is
recommended to use an empty folder for this.

### Creating a note

To create a new note you can either execute

~~~ vim
    :Pad new
~~~

or press `<Shift-Escape>` (`<leader>n` in the terminal)

### Listing the notes

To list the notes, use

~~~ vim
    :Pad ls
~~~

or press `<Control-Escape>` (`<leader><esc>` in the terminal). Press `<Enter>`
to open the note in the current line (you'll see this line is highlighted).

### Searching

If you are looking for something in particular within your notes, you'll want to
use vim-pad search utilities.

Open the notes list and press `<S-f>`. You'll see the prompt has changed to

    >>

You can now type a query. You'll see the list changes when you type, since it's
filtering. Once you have finished searching, press `<Enter>` to finish the
query, and then open the note as you've done before. You'll see the query is
highlighted.

#### Other ways to search

You can search non interactively, but without opening the notes list, with
`<leader>ss` . Pressing `<Enter>` after finishing the query will show the list
of matching notes.

### More on creating notes

There is yet another way to search for notes: If you press `<leader>s<leader>`
in any window, an interactive search will start. This is pretty similar to
`<leader>ss`, but it will also allow the user to create a new note if the query
is not found. If so, pressing `<Enter>` will open a new note with the query
pre-appended. This is a pretty convenient way of creating a new note very quick
and keep adding to it. If you don't need to open the note afterwards, you can
use `<Leader>s!` instead (even quicker!).

### Using different types of files for notes

Have you noticed that sitcky notes come both blank and pre-filled? Well, that is
because not all notes (like people) are born the same! You shouldn't have to
conform to any particular format. vim-pad does not impose any.

That said, it uses markdown by default, because it is a very good general
purpose format (also because vim comes with support for it by default). You can
change this default to your hearts desire by setting the `g:pad#default_format`
variable. For example, you can make your notes be LaTeX by default:

~~~ vim
    :let g:pad#default_format = "tex"
~~~

To change a particular note's format, you'll have to add a modeline. Doing so
by hand is tiresome, so you can press `<localleader>+m` to add one. You'll be
prompted for a filetype. Select one and press `<Enter>`. Voil??! The modeline is
added, and the filetype is set.

### Tags

If you write labels starting with # or @ in your file, they will be treated like
tags when you list the notes.

### Sorting

Sometimes you'll want to sort the notes in the list. For example, you might want
to sort alphabetically all the notes you have titled "recipe:...". To do this,
press `<S-s>` while the list is open, select the sorting method and press
`<Enter>`.

NOTE: Sorting won't undo a query you have previously entered, so you can search
for all notes mentioning "chicken" and then sort them alphabetically.

### Deleting notes, using sub-folders and archiving

Soon, you'll have a mess of notes. Let's see what you can do about it...

#### Deleting notes

From the notes list, select a note you want to delete and then press `dd`.
You'll be prompted to confirm.

If you are editing a note and discover you don't want it anymore (what were you
thinking!), you can press `<localleader><Del>`.

### Moving into sub-folders

Perhaps you'll want to organize the notes in groups. One option is to use tags,
which we've seen before, but that requires writing the tags in the files, and
you might not want that. Another option is to place your notes into topic
folders. You can do it manually (and vim-pad will show you the folders when
listing the notes), but there are better ways from within vim.

From the list, select a note and press `+f` . You'll be prompted for a folder
name to put the note in. If the folder doesn't exist, vim-pad will create it.

NOTE: Pressing the same combo within a note, with `<localleader>` prepended,
does the same.

NOTE: You can have subfolders to your subfolders.

If you want to move notes back to the root notes dir, you can use `-f`
(`<localleader>-f` within the note).

### Archiving

If you are an avid note-taker, you'll soon have a very large list of notes. But
some notes you simply don't want to have around all the time. For example, you
could have monthly TODO lists, or notes for proyects you've finished already, etc.
You want to keep this stuff, but keep it "away" too. For this, vim-pad features
an archive system. Any note in the special "archive/" folder will be treated as
archived, and won't be shown normaly by :Pad ls. To list the archive, you have
to put a ! after the command, like this

~~~ vim
    :Pad! ls
~~~

To put things on the archive, you can use `+a` (in both the list and the
notes).

### Local notes

So far, you've seen how to manage a global list of notes. But sometimes when you
work in a project, you want to keep notes about it which are only relevant to
it, and might not want to see them in the global list. For this, vim-pad has the
ability to detect local notes, which are saved in a folder in the current dir.
By default, this folder will be called "notes", but that can be changed by
setting the `g:pad#local_dir` variable.

To create a local note, use

~~~ vim
    :Pad! new
~~~

(notice the bang !).

To create a local note about the file you are currently working on, use

~~~ vim
    :Pad this
~~~

### Some extras

For formatting your notes, you might want to check some of these plugins:

- [vimoutliner](https://github.com/vimoutliner/vimoutliner)
- [quicktask](https://github.com/aaronbieber/quicktask)
- [vim-notes](https://github.com/xolox/vim-notes)
- [vim-orgmode](https://github.com/jceb/vim-orgmode)
- [vim-pandoc](https://github.com/vim-pandoc/vim-pandoc)

Some of these also have note management utilities, but I think you'll prefer
vim-pad ;)

For the full documentation, please consult

~~~ vim
    :help vim-pad
~~~

If you have [vim-tutor-mode](https://github.com/fmoralesc/vim-tutor-mode), you
can read a tutorial on using vim-pad (it is basically equivalent to this
README, but with exercises) with

~~~ vim
    :Tutor pad
~~~
