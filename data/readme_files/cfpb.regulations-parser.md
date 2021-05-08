Regulations Parser
==================

[![Build Status](https://travis-ci.org/cfpb/regulations-parser.png)](https://travis-ci.org/cfpb/regulations-parser)
[![Coverage Status](https://coveralls.io/repos/cfpb/regulations-parser/badge.png)](https://coveralls.io/r/cfpb/regulations-parser)

This library/tool parses Federal regulations (either plain text or XML) and
much of their associated content. It can write the results to JSON files, an
API, or even a git repository. The parser works hand-in-hand with
[regulations-core](https://github.com/cfpb/regulations-core), an API for hosting the parsed regulations, and
[regulation-site](https://github.com/cfpb/regulations-site), a front-end for the data structures generated.

This repository is part of a larger project. To read about it, please see
[http://cfpb.github.io/eRegulations/](http://cfpb.github.io/eRegulations/).

## Quick Start

Here's an example, using CFPB's regulation H.

1. `git clone https://github.com/cfpb/regulations-parser.git`
1. `cd regulations-parser`
1. `pip install -r requirements.txt`
1. `wget
   http://www.gpo.gov/fdsys/pkg/CFR-2012-title12-vol8/xml/CFR-2012-title12-vol8-part1004.xml`
1. `python build_from.py CFR-2012-title12-vol8-part1004.xml 12 2011-18676 15
   1693`

At the end, you will have new directories for `regulation`, `layer`,
`diff`, and `notice` which would mirror the JSON files sent to the API.

## Quick Start with Modified Documents

Here's an example using CFPB's regulation E, showing how documents can be
tweaked to pass the parser.

1. `git clone https://github.com/cfpb/regulations-parser.git`
1. `cd regulations-parser`
1. `git clone https://github.com/cfpb/fr-notices.git`
1. `pip install -r requirements.txt`
1. `echo "LOCAL_XML_PATHS = ['fr-notices/']" >> local_settings.py`
1. `python build_from.py fr-notices/articles/xml/201/131/725.xml 12 2011-31725 15 1693`

If you review the history of the `fr-notices` repo, you'll see some of the types of changes that need to be made.

## Troubleshooting

If you get the message `wget: command not found`, install `wget` using the following (we use [homebrew](http://brew.sh/)):

```shell
brew install wget
```

If you review the history of the `fr-notices` repo, you'll see some of the types
of changes that need to be made.

## Features

* **Split regulation** into paragraph-level chunks.
* **Create a hierarchical tree** which defines the relationship between these
  chunks.
* **External Citations Layer** -- links to Acts, Public Law, etc.
* **Graphics Layer** -- converting image references into federal register
  URLs.
* **Internal Citations Layer** -- links between parts of this regulation.
* **Interpretations Layer** -- connecting regulation text to the
  interpretations associated with it.
* **Key Terms Layer** -- pseudo headers for certain paragraphs.
* **Meta Info Layer** -- custom data (some pulled from federal notices).
* **Paragraph Markers Layer** -- specifying where the initial paragraph
  marker begins and ends for each paragraph.
* **Section-by-Section Analysis Layer** -- associated analyses (from FR
  notices) with the text they are analyzing.
* **Table of Contents Layer** -- a listing of headers.
* **Terms Layer** -- defined terms, including their scope.
* **Additional Formatting Layer** -- including tables, "notes", code blocks,
  and subscripts.
* **Build whole versions** of the regulation from the changes found in final
  rules.
* **Create diffs** between these versions of the regulations.

## Requirements

* lxml (3.2.0) - Used to parse out information XML from the federal register.
* pyparsing (1.5.7) - Used to do generic parsing on the plain text.
* inflection (0.1.2) - Helps determine pluralization (for terms layer).
* requests (1.2.3) - Client library for writing output to an API.
* requests_cache (0.4.4) - *Optional* - Library for caching request results
  (speeds up rebuilding regulations).
* GitPython (0.3.2.RC1) - Allows the regulation to be written as a git repo.
* python-constraint (1.2) - Used to determine paragraph depth.

If running tests:

* nose (1.2.1) - A pluggable test runner.
* mock (1.0.1) - Makes constructing mock objects/functions easy.
* coverage (3.6) - Reports on test coverage.
* cov-core (1.7) - Needed by coverage.
* nose-cov (1.6) - Connects nose to coverage.

## API Docs

[Read The Docs](https://regulation-parser.readthedocs.org/en/latest/)

## Installation

### Getting the Code and Development Libs

Download the source code from GitHub (e.g. `git clone [URL]`)

Make sure the `libxml` libraries are present. To install the libraries using [homebrew](http://brew.sh/), run `brew install libxml2`.
On Ubuntu/Debian, install
it via:

```bash
$ sudo apt-get install libxml2-dev libxslt-dev
```

### Create a virtual environment (optional)
If you want to encapsulate the dependencies in a virtual environment, run the following (note, you may not need to run the first line if your administrator already installed `virtualenvwrapper` on your machine):

```bash
$ sudo pip install virtualenvwrapper
$ mkvirtualenv parser
```

### Get the required libraries

```bash
$ cd regulations-parser
$ pip install -r requirements.txt
```

### Pull down the regulation text

The parser can generally read either plain-text or XML versions of a
regulation, though the XML version gives much better hints. If you have a
regulation as plain text, make sure to remove any table-of-contents and
superflous lines (e.g. "Link to an amendment" and "Back to Top", which might
appear if copy-pasting from
[e-CFR](http://www.ecfr.gov/cgi-bin/ECFR?page=browse).

A better strategy would be to parse using an XML file. This XML can come
from [annual editions](http://www.gpo.gov/fdsys/browse/collectionCfr.action)
of the regulations, or Federal Register notices, if the notice contains a
reissuance of the whole regulation (e.g. CFPB
[re-issued](https://www.federalregister.gov/articles/xml/201/131/725.xml)
regulation E).


### Run the parser (`build_from`)

The syntax is

```bash
$ python build_from.py regulation.xml title act_title act_section
```

For example, to match the reissuance above:
```bash
$ python build_from.py 725.xml 12 15 1693
```

Here ```12``` is the CFR title number (in our case, for "Banks and Banking"),
```15``` is the title of "the Act" and ```1693``` is the relevant section.
Wherever the phrase "the Act" is used in the regulation, the external link
parser will treat it as "15 U.S.C. 1693".

Running the command will generate four folders, ```regulation```,
```notice```, ``layer`` and possibly ``diff`` in the ```OUTPUT_DIR```
(current directory by default).

If you'd like to write the data to an api instead (most likely, one running
regulations-core), you can set the ```API_BASE``` setting (described below).

There are also some advanced flags which can be set when running the parser

* `--no-generate-diffs` Avoids the default behavior of generating additional
  versions of the regulation based on federal register rules. If this flag is
  set, the parser will produce a single tree and set of layers
* `--checkpoint CHECKPOINT_DIR` Defines a directory to store checkpoint
  information. It's always safe to not provide this, though you may improve
  performance when you do. See [Runtime](#runtime), below.
* `--version-identifier DOC_NUMBER` If you are trying to parse a version of
  the regulation issued before federalregister.gov has records (~2000), you
  may need to explicitly provide a version number. This will just be an
  identifier for the version; you may use "1997-annual", for example.

### Settings

All of the settings listed in ```settings.py``` can be overridden in a
```local_settings.py``` file. Current settings include:

* ```OUTPUT_DIR``` - a string with the path where the output files should be
  written. Only useful if the JSON files are to be written to disk.
* ```API_BASE``` - a string defining the url root of an API (if the output
  files are to be written to an API instead)
* ```GIT_OUTPUT_DIR``` - a string path which will be used to initialize a
  git repository when writing history
* ```META``` - a dictionary of extra info which will be included in the
  "meta" layer. This is free-form, but could be used for copyright
  information, attributions, etc.
* ```CFR_TITLES``` - array of CFR Title names (used in the meta layer); not
  required as those provided are current
* ```DEFAULT_IMAGE_URL``` - string format used in the graphics layer; not
  required as the default should be adequate
* ```IGNORE_DEFINITIONS_IN``` - a dictionary mapping CFR part numbers to a
  list of terms that should *not* contain definitions. For example, if
  'state' is a defined term, it may be useful to exclude the phrase 'shall
  state'. Terms associated with the constant, `ALL`, will be ignored in all
  CFR parts parsed.
* ```INCLUDE_DEFINITIONS_IN``` - a dictionary mapping CFR part numbers to a
  list of tuples containing (term, context) for terms that *are
  definitely definitions*. For example, a term that is succeeded by 
  subparagraphs that define it rather than phraseology like "is defined as". 
  Terms associated with the constant, `ALL`, will  be included in all CFR 
  parts parsed.
* ```OVERRIDES_SOURCES``` - a list of python modules (represented via
  string) which should be consulted when determining image urls. Useful if
  the Federal Register versions aren't pretty. Defaults to a `regcontent`
  module.
* ```MACRO_SOURCES``` - a list of python modules (represented via strings)
  which should be consulted if replacing chunks of XML in notices. This is
  more or less deprecated by `LOCAL_XML_PATHS`. Defaults to a `regcontent`
  module.
* ```REGPATCHES_SOURCES``` - a list of python modules (represented via
  strings) which should be consulted when determining changes to regulations
  made in final rules.  Defaults to a `regcontent` module
* ```LOCAL_XML_PATHS``` - a list of paths to search for notices from the
  Federal Register. This directory should match the folder structure of the
  Federal Register. If a notice is present in one of the local paths, that
  file will be used instead of retrieving the file, allowing for local
  edits, etc. to help the parser.

Settings can also be loaded from a module or package called `regconfig`
if it exists. See
[regulations-configs](http://github.com/cfpb/regulations-configs) for an
example of an external package that holds regulation-specific
configuration.

## Other Utilities

### Notice Order

When debugging, it can be helpful to know how notices will be grouped and
sequenced when compiling the regulation. The `notice_order.py` utility tells
you exactly that information, once it is given a CFR title and part.

```
$ python notice_order.py 12 1026
```

By default, this only includes notices which explicitly change the text of the
regulation. To include all final notices, add this flag:

```
$ python notice_order.py 12 1005 --include-notices-without-changes
```

### Watch Node

Tracing how a specific node changes over the life of a regulation can help
track down why the parser is failing (or exploding). The `watch_node.py`
utility does exactly that, stepping through the initial tree and all
subsequent notices. Whenever a node is changed (created, modified, deleted,
etc.) this utility will log some output.

```
$ python watch_node.py 1005-16-c path/to/regulation.xml 12
```

The first parameter is the label of the node you want to watch, the second is
the initial regulation XML file and the final parameter is the CFR title.


## Building the documentation

For most tweaks, you will simply need to run the Sphinx documentation
builder again.

```
$ pip install Sphinx
$ cd docs
$ make dirhtml
```

The output will be in ```docs/_build/dirhtml```.

If you are adding new modules, you may need to re-run the skeleton build
script first:

```
$ pip install Sphinx
$ sphinx-apidoc -F -o docs regparser/
```

##  Running Tests

As the parser is a complex beast, it has several hundred unit tests to help
catch regressions. To run those tests, make sure you have first added all of
the testing requirements:

```bash
$ pip install -r requirements_test.txt
```

Then, run nose on all of the available unit tests:

```bash
$ nosetests tests/*.py
```

If you'd like a report of test coverage, use the [nose-cov](https://pypi.python.org/pypi/nose-cov) plugin:

```bash
$ nosetests --with-cov --cov-report term-missing --cov regparser tests/*.py
```

Note also that this library is continuously tested via Travis. Pull requests
should rarely be merged unless Travis gives the green light.

## Additional Details

Here, we dive a bit deeper into some of the topics around the parser, so
that you may use it in a production setting.

### Parsing Workflow

The parser first reads the file passed to it as a parameter and attempts to
parse that into a structured tree of subparts, sections, paragraphs, etc.
Following this, it will make a call to the Federal Register's API,
retrieving a list of final rules (i.e. changes) that apply to this
regulation. It then writes/saves parsed versions of those notices.

If this all worked well, we save the the parsed regulation and then generate
and save all of the layers associated with its version. We then generate
additional whole regulation trees and their associated layers for each
final rule (i.e. each alteration to the regulation).

At the very end, we take all versions of the regulation we've built and
compare each pair (both going forwards and backwards). These diffs are
generated and then written to the API/filesystem/Git.

### Output

The parser has three options for what it does with the parsed documents it
creates. With no configuration, all of the objects it creates will be
pretty-printed as JSON files and stored in subfolders of the current
directory. Where the output is written can be configured via the
`OUTPUT_DIR` setting. Spitting out JSON files this way is a good way to
track how tweaks to the parser might have unexpected effects on the output
-- just diff two such directories.

If the `API_BASE` setting is configured, the output will be written to an API
(running `regulations-core`) rather than the file system. The same JSON
files are sent to the API as in the above method. This would be the method
used once you are comfortable with the results (by testing the filesystem
output).

A final method, a bit divergent from the other two, is to write the results
as a git repository. Using the `GIT_OUTPUT_DIR` setting, you can tell the
parser to write the versions of the regulation (*only*; layers, notices,
etc. are not written) as a git history. Each node in the parse tree will be
written as a markdown file, with hierarchical information encoded in
directories. This is an experimental feature, but has a great deal of
potential.

### Modifying Data

Our sources of data, through human and technical error, often contain
problems for our parser. Over the parser's development, we've created
several not-always-exclusive solutions. We have found that, in most cases,
the easiest fix is to download and edit a *local* version of the problematic
XML. Only if there's some complication in that method should you progress to
the more complex strategies.

All of the paths listed in `LOCAL_XML_PATHS` are checked when fetching
regulation notices. The file/directory names in these folders should mirror
those found on federalregister.gov, (e.g. `articles/xml/201/131/725.xml`). Any
changes you make to these documents (such as correcting XML tags, rewording
amendment paragraphs, etc.) will be used as if they came from the Federal
Register.

In addition, certain notices have *multiple* effective dates, meaning that
different parts of the notice go into effect at different times. This
complication is not handled automatically by the parser. Instead, you must
manually copy the notice into two (or more) versions, such that 503.xml
becomes 503-1.xml, 503-2.xml, etc. Each file must then be *manually*
modified to change the effective date and remove sections that are not
relevant to this date. We sometimes refer to this as "splitting" the notice.

While editing the notice is generally an effective strategy, there are
certain corner cases in which the parser simply does not support the logic
needed to determine what's going on. In these situations, you have the
option of using custom "patches" for notices, via the `REGPATCHES_SOURCES`
setting. The setting refers to a Python object that has keys and values
(e.g. a `dict`). The keys are notice document numbers (e.g. 2013-22752 or
2013-22752_20140110 for a split notice). When the changes associated with a
particular notice are consulted (to build the next regulation version), the
entries in the value are added to the list of notice `changes`. This
strategy is useful for certain appendix alterations.

### Appendix Parsing

The most complicated segments of a regulation are their appendices, at least
from a structural parsing perspective. This is because appendices are
free-form, often with unique variations on sub-sections, headings, paragraph
marker hierarchy, etc. Given all this, the parser does its best to
determine *an* ordering and *a* hierarchy for the subsections/paragraphs
contained within an appendix.

In general, if the parser can find a unique identifier or paragraph marker,
it will note the paragraph/section accordingly. So "Part I: Blah Blah"
becomes 1111-A-I, and "a. Some text" and "(a) Some text)" might become
1111-A-I-a. When the citable value of a paragraph cannot be determined (i.e.
it has no paragraph marker), the paragraph will be assigned a number and
prefaced with "p" (e.g. p1, p2). Similarly, headers become h1, h2, ...

This works out, but had numerous downsides. Most notably, as the citation
for such paragraphs is arbitrary, determining changes to appendices is quite
difficult (often requiring patches). Further, without guidance from
paragraph markers/headers, the parser must make assumptions about the
hierarchy of paragraphs. It currently uses some heuristics, such as headers
indicating a new depth level, but is not always accurate.

### Markdown/Plaintext-ifying

With some exceptions, we treat a plain-text version of the regulation as
canon. By this, we mean that the *words* of the regulation count for much
more than their presentation in the source documents. This allows us to
build better tables of content, export data in more formats, and the other
niceties associated with separating data from presentation.

At points, however, we need to encode non-plain text concepts into the
plain-text regulation. These include displaying images, tables, offsetting
blocks of text, and subscripting. To encode these concepts, we use a
variation of Markdown.

Images become

```
![Appendix A9](ER27DE11.000)
```

Tables become

```
| Header 1 | Header 2|
---
| Cell 1, 1 | Cell 1, 2 |
```

Subscripts become

```
P_{0}
```

etc.

### Runtime

A quick note of warning: the parser was not optimized for speed. It performs
many actions over and over, which can be *very* slow on very large
regulations (such as CFPB's regulation Z). Further, regulations that have
been amended a great deal cause further slow down, particularly when
generating diffs (currently an n**2 operation). Generally, parsing will take
less than ten minutes, but in the extreme example of reg Z, it currently
requires several hours.

There are a few methods to speed up this process. Installing `requests-cache`
will cache API-read calls (such as those made when calling the Federal
Register). The cache lives in an sqlite database (`fr_cache.sqlite`), which
can be safely removed without error. The `build_from.py` pipeline can also
include checkpoints -- that is, saving the state of the process up until some
point in time. To activate this feature, pass in a directory name to the
`--checkpoint` flag, e.g.

```bash
$ python build_from.py CFR-2012-title12-vol8-part1004.xml 12 15 1693 --checkpoint my-checkpoint-dir
```

### Parsing Error Example

Let's say you are already in a good steady state, that you can parse the
known versions of a regulation without problem. A new final rule is
published in the federal register affecting your regulation. To make this
concrete, we will use CFPB's regulation Z (12 CFR 1026), final rule
2014-18838.

The first step is to run the parser as we have before. We should configure
it to send output to a local directory (see above). Once it runs, it will
hit the federal register's API and should find the new notice. As described
above, the parser first parses the file you give it, then it heads over to
the federal register API, parses notices and rules found there, and then
proceeds to compile additional versions of the regulation from them. So, as
the parser is running (Z takes a long time), we can check its partial
output. Notably, we can check the `notice/2014-18838` JSON file for
accuracy.

In a browser, open https://www.federalregister.gov and search for the notice
in question (you can do this by using the 2014-18838 identifier). Scroll
through the
[page](https://www.federalregister.gov/articles/2014/08/15/2014-18838/truth-in-lending-regulation-z-annual-threshold-adjustments-card-act-hoepa-and-atrqm)
to find the list of changes -- they will generally begin with "PART ..." and
be offset from the rest of the text. In a text editor, look at the JSON file
mentioned before.

The JSON file that describes our parsed notice has two relevant fields.
The `amendments` field lists what *types* of changes are being made; it
corresponds to AMDPAR tags (for reference). Looking at the web page, you
should be able to map sentences like "Paragraph (b)(1)(ii)(A) and (B) are
revised" to an appropriate PUT/POST/DELETE/etc. entry in the `amendments`
field. If these do not match up, you know that there's an error parsing the
AMDPARs. You will need to alter the XML for this notice to read how the
parser can understand it. If the logic behind the change is too complicated,
e.g. "remove the third semicolon and replace the fourth sentence", you will
need to add a "patch" (see above).

In this case, the amendment parsing was correct, so we can continue to the
second relevant field. The `changes` field includes the *content* of changes
made (when adding or editing a paragraph). If all went well you should be
able to relate all of the PUT/POST entries in the `amendments` section with
an entry in the `changes` field, and the content of that entry should match
the content from the federal register. Note that a single `amendment` may
include multiple `changes` if the amendment is about a paragraph with
children (sub-paragraphs).

Here we hit a problem, and have a few tip-offs. One of the entries in
`amendments` was not present in the `changes` field. Further, one of the
`changes` entries was something like  "i. * * *". In addition, the
"child_labels" of one of the entries doesn't make sense -- it contains
children which should not be contained. The parser must have skipped over
some relevant information; we could try to deduce further but let's treat
the parser as a black box and see if we can't spot a problem in the
web-hosted rule, first. You see, federalregister.gov uses XSLTs to take the
raw XML (which we parse) to convert it into XHTML. If *we* have a problem,
they might also.

We'll zero in on where we know our problem begins (based on the information
investigating `changes`). We might notice that the text of the problem
section is in italics, while those arround it (other sections which *do*
parse correctly) are not. We might not. In any event, we need to look at the
XML. On the federal register's site, there is a 'DEV' icon in the right
sidebar and an 'XML' link in the modal. We're going to download this XML and
put it where our parser knows to look (see the `LOCAL_XML_PATHS` setting).
For example, if this setting is

```python
LOCAL_XML_PATHS = ['fr-notices/']
```

we would need to save the XML file to
`fr-notices/articles/xml/201/418/838.xml`, duplicating the directory
structure found on the federal register. I recommend using a git repository
and committing this "clean" version of the notice.

Now, edit the saved XML and jump to our problematic section. Does the XML
structure here match sections we know work? It does not. Our "italic" tip
off above was accurate. The problematic paragraphs are wrapped in `E` tags,
which should not be present. Delete them and re-run the parser. You will see
that this fixes our notice.

Generally, this will be the workflow. Something doesn't parse correctly and
you must investigate. Most often, the problems will reside in unexpected XML
structure. AMDPARs, which contain the list of changes may also need to be
simplified. If the same type of change needs to be made for multiple
documents, consider adding a corresponding rule to the parser -- just test
existing docs first.

### Integration with regulations-core and regulations-site

With the above examples, you should have been able to run the parser and
generate some output. "But where's the website?" you ask. The parser was
written to be as generic as possible, but integrating with [regulations-core](https://github.com/cfpb/regulations-core) and [regulations-site](https://github.com/cfpb/regulations-site) is likely where you'll want to end up. Here, we'll show one way to connect these applications up. See the individual repos for more configuration detail.

Let's set up [regulations-core](https://github.com/cfpb/regulations-core) first. This is an API which will be used to both store and query the regulation data.

 1. `git clone https://github.com/cfpb/regulations-core.git`
 1. `cd regulations-core`
 1. `pip install zc.buildout`
 1. `buildout   # pulls in python dependencies`
 1. `./bin/django syncdb --migrate`
 1. `./bin/django runserver 127.0.0.1:8888 &   # Starts the API`

Then, we can configure the parser to write to this API and run it, here using
the regulation H example above

 1. `cd /path/to/regulations-parser`
 1. `echo "API_BASE = 'http://127.0.0.1:8888/'" >> local_settings.py`
 1. `python build_from.py CFR-2012-title12-vol8-part1004.xml 12 2011-18676 15
   1693`

Next up, we set up [regulations-site](https://github.com/cfpb/regulations-site) to provide a webapp.

 1. `git clone https://github.com/cfpb/regulations-site.git`
 1. `cd regulations-site`
 1. `buildout`
 1. `echo "API_BASE = 'http://127.0.0.1:8888/'" >>
    regulations/settings/local_settings.py`
 1. `./run_server.sh`

Then, navigate to `http://localhost:8000/` in your browser to see the reg.
