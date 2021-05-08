# Jotmuch

Jotmuch is a bookmark manager that emphasizes privacy, preservation,
and organization.  It will be familiar to users of
[notmuch](http://notmuchmail.org/).


## Installation

Install the prerequisites.  Arch Linux:

    $ sudo pacman -S python2-pip python2-xapian python2-jinja python2-lxml python2-yaml webkitgtk

Debian/Ubuntu:

    $ sudo apt-get install python-pip python-xapian python-jinja2 python-lxml python-yaml libwebkit2gtk-3.0-dev

Install required Python libraries that are not available as packages:

    $ pip2 install --user arrow click

Configure Jotmuch by editing the `jot` Python script.
Install Jotmuch and urlsnap:

    $ gcc urlsnap.c $(pkg-config --cflags --libs webkit2gtk-3.0) -o urlsnap
    $ cp jot urlsnap ~/bin


## Usage

### Bookmarks

Bookmarks are YAML documents.  Here is an example bookmark:

    url: https://github.com/davidlazar/jotmuch
    title: davidlazar/jotmuch · GitHub
    tags: [bookmark, tagging, tool, opensource, python, xapian, archived]
    created: 2014-06-23 16:53:22 UTC
    archived: 2014-06-27 10:45:18 UTC
    notes: works well with tor browser

To bookmark a webpage run:

    $ jot bookmark http://example.com

This edits the bookmark (YAML) for the given URL using your `$EDITOR`.
This command does not connect to the internet unless `--fetch-title` or
`--archive` is used.  Otherwise, a new bookmark will not have a title
until it is archived or a title is entered manually.


### Searching

Jotmuch uses the [Xapian](http://xapian.org) search engine.
The [Xapian QueryParser](http://xapian.org/docs/queryparser.html)
documentation describes the search query syntax supported by several
Jotmuch commands, including **search**, **archive**, **view**, **edit**,
**dump**, and **random**. The [notmuch searching](http://notmuchmail.org/searching/)
documentation also gives a good overview of this syntax.

List all bookmarks:

    $ jot search

List bookmarks with the tags "history" and "typography":

    $ jot search tag:history and tag:typography

List bookmarks of a specific domain:

    $ jot search tag:crypto and site:github.com
    $ jot search site:edu  # .edu websites

List a specific bookmark by its short id (displayed in the search results),
or its full id:

    $ jot search z6utke24
    $ jot search id:z6utke24liq4ausyu2ji4zd374

Unprefixed search terms and phrases will match text from the HTML body
of an archived bookmark:

    $ jot search football or soccer
    $ jot search \"static analysis\"

Complex queries can be built from boolean operators and brackets:

    $ jot search 'tag:recipe and ((rice and "cashew nuts") or (noodles and tomatoes)) and not soup'

Search terms prefixed with **site:** or **id:** are implicitly connected by
logical OR and all other terms are implicitly connected by logical AND, when
explicit operators are not provided.  Thus, the following two commands are
equivalent:

    $ jot search tag:a site:j id:x foo tag:b site:k id:y bar
    $ jot search '(tag:a and tag:b) and (site:j or site:k) and (id:x or id:y) and (foo and bar)'

The `--format` option is used to customize the display of search results:

    $ jot search --format='{{url}} {{title}}'

The argument to `--format` is a [Jinja2 template](http://jinja.pocoo.org/docs/templates/).
The following variables are supported: id, sid (short id), url, title,
created and archived ([Arrow](http://crsmithdev.com/arrow/) objects),
pngpath and mhtmlpath (even if these files don't exist yet),
tags, and notes.

List all tags, sorted by frequency:

    $ jot search --format='{{tags|join("\n")}}' | sort | uniq -c | sort -n


### Archiving

To archive a bookmark means to save a snapshot of the associated webpage.
Jotmuch uses `urlsnap.c` to save an [MHTML](https://en.wikipedia.org/wiki/MHTML)
and PNG snapshot of a webpage.

The archive command takes a search query:

    $ jot archive tag:funny site:example.com

Any unarchived bookmarks matching the query are archived in order.
Newly archived bookmarks are opened in the `$EDITOR` to inspect and edit
new title values.

The view command opens the PNG snapshots of archived bookmarks matching
the given search query:

    $ jot view tag:\"sky diving\"

The paths to the PNG files of matching bookmarks are passed as command-line
arguments to the image viewer defined by `PNGVIEW` (feh by default).

The archive files for a bookmark with id `z6utke24liq4ausyu2ji4zd374`
are located at:

    ARCHIVE_DIR/z6utke24liq4ausyu2ji4zd374.{mhtml,png}


### Anonymous Archiving

Jotmuch works well with anonymous web browsing.
The bookmark command (without any options) does not connect to the internet,
so you can use it to bookmark pages that you visit anonymously.

To archive bookmarks anonymously, you can
[Torify](https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO)
urlsnap by running it behind a
[transparent proxy](https://trac.torproject.org/projects/tor/wiki/doc/TransparentProxy).
The `doc/torify.md` file has an example configuration.

You can avoid identity correlation by archiving bookmarks randomly:

    $ jot archive id:$(jot random not tag:archived --format={{id}})


### Other Commands

Edit multiple bookmarks at once with the edit command:

    $ jot edit site:wikipedia.org

Export bookmarks as YAML with the dump command:

    $ jot dump  # dumps all bookmarks
    $ jot dump tag:recipe

Import bookmarks exported as JSON from [Pinboard](https://pinboard.in/):

    $ jot import ~/bookmarks.json


## License

Jotmuch is free software released under the
GNU [GPL version 3](http://www.fsf.org/licensing/licenses/gpl.html).
