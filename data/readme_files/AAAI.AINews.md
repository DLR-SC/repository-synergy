# NewsFinder

Full details of this software can be found at
[AITopics](http://aitopics.org/misc/about-newsfinder).

The main script `AINews.py` can be called with one of three
arguments:

<pre>
python AINews.py crawl
</pre>

This crawls the sources list and stores its results in the database
(table `urllist`).

<pre>
python AINews.py prepare
</pre>

This filters and processes the news, and creates an XML file export.

<pre>
python AINews.py email
</pre>

This generates the weekly email as an HTML submission form.

Our configuration has a script that uses the `crawl` and `prepare` (in
that order) commands once each day, and the `email` command once a
week. The email is sent manually using the generated submission form.

## Installation

NewsFinder is primarily coded in Python and requires the following libraries:

  - MySQL Python bindings (MySQLdb)
  - [libsvm2](http://www.csie.ntu.edu.tw/~cjlin/libsvm/)
  - [Justext](http://code.google.com/p/justext/)
  - [cheetah](http://www.cheetahtemplate.org/)
  - [nltk](http://www.nltk.org/)
  - [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/)
  - [PyRSS2Gen](http://www.dalkescientific.com/Python/PyRSS2Gen.html)
  - [feedparser](http://www.feedparser.org/)
  - [Unidecode](http://pypi.python.org/pypi/Unidecode)
  
Packages for Ubuntu:

<pre>
sudo apt-get install python-mysqldb libsvm-tools python-libsvm \
                     python-cheetah python-nltk python-beautifulsoup \
                     python-pyrss2gen python-feedparser python-unidecode
</pre>

"Installation" of NewsFinder should only involve downloading the code in
this repository. Assuming Python includes the NewsFinder code in its path,
execution of NewsFinder should be as simple as running `python AINews.py`

There are various supplementary files that NewsFinder expects. These files
can be obtained from another repository:
[AINewsSupplementary](https://github.com/AAAI/AINewsSupplementary)

In our working configuration, we have a directory in our home called
`NewsFinder`. In this directory are the AINewsSupplementary
directories (e.g. `templates`, `resource`, etc.). The NewsFinder code
found in this repository is stored in a `code` directory in the main
`NewsFinder` folder. In any event, the `paths.ini` file (in the
`config` directory of this project) can be modified to point to
whereever you keep your files.

## Database

Look at `tables.sql` to create tables needed by NewsFinder.

## Configuration

All configuration is provided in the `config/*.ini` files:

  - `config.ini` has miscellaneous configuration options, described in
    the file
  - `db.ini` has database connectivity information (host, username,
    password, etc.)
  - `paths.ini` stores the paths of various data and output
    directories used by NewsFinder. This file allows you to store data
    and output in whatever way makes sense for a particular
    installation (for example, data files should be outside of a
    webserver root)

Make a copy of the `.ini.sample` files (rename to `.ini`) to build
your own configuration.

## News sources

Sources are specified in a CSV file obtained from a URL provided in
the `paths.ini` config file. Here is an example short sources CSV file:

<pre>
"SourceID","Title","Link","Parser"
"62671","Forbes Technology","http://www.forbes.com/technology/index.xml","RSS"
"62673","BBC Technology","http://feeds.bbci.co.uk/news/technology/rss.xml","RSS"
</pre>

Only RSS sources are supported at this time.

# Authors

The most recent version (as of this writing) of NewsFinder was written
by [Joshua Eckroth](http://aitopics.org/editor/joshua-eckroth). The
prior iteration was written by Liang Dong. Before that, NewsFinder was
coded by Tom Charytoniuk. The project has been supervised by
[Bruce Buchanan](http://aitopics.org/editor/bruce-buchanan) and
[Reid Smith](http://aitopics.org/editor/reid-smith).

# License

Copyright (c) 2011 by the Association for the Advancement of
Artificial Intelligence. This program and parts of it may be used and
distributed without charge for non-commercial purposes as long as this
notice is included.

The file `arff.py` is pulled from the
[laic-arff](https://github.com/renatopp/liac-arff) package, which is
distributed under the MIT License.
