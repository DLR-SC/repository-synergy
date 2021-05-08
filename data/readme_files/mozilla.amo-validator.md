[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/)


:warning: This tool is now considered fully deprecated and is no longer maintained.


# addons.mozilla.org Validator


It is still used on addons.mozilla.org for legacy add-ons but once support for updates for legacy add-ons goes away from AMO this tool will be archived.

The AMO Validator is a tool designed to scan Mozilla add-on packages for
problems such as security vulnerabilities, exploits, spamware and badware,
and lots of other gunk. By using a combination of various techniques and
detection mechanisms, the validator is capable of being both efficient as well
as thorough.


## Setup

### Prerequisites

You can install everything you need for running and testing with

```bash
pip install -r requirements.txt
```


### Submodules

The validator may require some submodules to work. Make sure to run

```bash
git clone --recursive git://github.com/mozilla/amo-validator.git
```

so that you get all of the goodies inside.


### Spidermonkey

A working copy of Spidermonkey (debug or non-debug is fine) is required.  The
easiest way to do this is to just [download the binary](https://archive.mozilla.org/pub/firefox/nightly/latest-mozilla-central/jsshell-linux-x86_64.zip).

If you want to build it from scratch, [clone](http://hg.mozilla.org/mozilla-central/)
the mozilla-central repo or
[download the tip](http://hg.mozilla.org/mozilla-central/archive/tip.tar.bz2)
(which is faster). Then build it from source like this

```bash
cd mozilla-central
cd js/src
autoconf2.13
./configure
make
sudo cp dist/bin/js /usr/local/bin/js
```

You must use autoconf at *exactly* 2.13 or else it won't work. If you're using
`brew`_ on Mac OS X you can get autoconf2.13 with this

    brew install autoconf213

If you don't want to put the `js` executable in your `$PATH` or you want it
in a custom path, you can define it as `$SPIDERMONKEY_INSTALLATION` in
your environment.

### Using amo-validator as a contained app using docker

Check this instructions from [marceloandrader](https://github.com/marceloandrader/dockerfiles/blob/master/amo-validator/README.md)

## Running

Run the validator as follows

```
./addon-validator <path to xpi> [-t <expected type>] [-o <output type>] [-v]
    [--boring] [--selfhosted] [--determined]
```

The path to the XPI should point to an XPI file.

<dl>
    <dt>-t
    <dd>The type that you expect your add-on to be detected as. The list of
    types is listed below.
    <dt>-o
    <dd>The type of output to generate. Types are listed below.
    <dt>-v
    <dd>Enable verbose mode. Extra information will be displayed in verbose mode,
    namely notices (informational messages), Jetpack information if
    available, extra error info (like contexts, file data, etc.), and error
    descriptions. This only applies to `-o text`.
    <dt>--selfhosted
    <dd>Disables messages that are specific to add-ons hosted on AMO.
    <dt>--boring
    <dd>Disables colorful shell output.
    <dt>--determined
    <dd>Continue validating the remaining tiers of an add-on if one tier has
    failed. Certain high-tiered tests may inadvertently fail when this option
    is enabled for badly malformed add-ons.
    <dt>--target-maxversion
    <dd>Accepts a JSON string containing an object whose keys are GUIDs and
    values are version strings. This will override the max version that the
    add-on supports for the corresponding application GUID. E.g.:
    `{"{ec8030f7-c20a-464f-9b0e-13a3a9e97384}": "6.*"}`
    <dt>--target-minversion
    <dd>Identical to `--target-maxversion`, except overrides the min version
    instead of the max.
    <dt>--for-appversions
    <dd>Accepts a JSON string containing an object whose keys are GUIDs and
    values are lists of version strings. If this list is specified,
    non-inlinecompatibility tests will only be run if they specifically
    target the applications and veresions in this parameter. E.g.:
    `{"{ec8030f7-c20a-464f-9b0e-13a3a9e97384}": ["6.*"]}`
</dl>


### Expected Type:

The expected type should be one of the following values:

<dl>
    <dt>any (default)
    <dd>Accepts any extension
    <dt>extension
    <dd>Accepts only extensions
    <dt>theme
    <dd>Accepts only themes
    <dt>dictionary
    <dd>Accepts only dictionaries
    <dt>languagepack
    <dd>Accepts only language packs
    <dt>search
    <dd>Accepts only OpenSearch XML files (unpackaged)
    <dt>multi
    <dd>Accepts only multi-item XPI packages
</dl>

Specifying an expected type will throw an error if the validator
does not detect that particular type when scanning. All addon type
detection mechanisms are used to make this determination.


### Output Type:

The output type may be either of the following:

<dl>
    <dt>text (default)
    <dd>Outputs a textual summary of the addo-on analysis. Supports verbose mode.
    <dt>json
    <dd>Outputs a JSON snippet representing a full summary of the add-on analysis.
</dl>

## Output

### Text Output Mode (default; `text`)

In `text` output mode, output is structured in the format of one
message per line. The messages are prefixed by their priority level
(i.e.: "Warning: This is the message").

At the head of the text output is a block describing what the
add-on type was determined to be.


### JSON Output Mode (`json`)

In `JSON` output mode, output is formatted as a JSON snippet
containing all messages. The format for the JSON output is that of the
sample document below.

```js
{
    "detected_type": "extension",
    "errors": 2,
    "warnings": 1,
    "notices": 1,
    "success": false,
    "compatibility_summary": {
        "errors": 1,
        "warnings": 0,
        "notices": 0
    },
    "ending_tier": 4,
    "messages": [
        {
            "uid": "123456789",
            "id": ["module", "function", "error"],
            "type": "error",
            "message": "This is the error message text.",
            "description": ["Description of the error message.",
                            "Additional description text"],
            "file": ["chrome/foo.jar", "bar/zap.js"],
            "line": 12,
            "column": 50,
            "context": [
                "   if(foo = bar())",
                "       an_error_is_somewhere_on_this_line.prototy.eval(\"whatever\");",
                null
            ],
            "compatibility_type": "error",
            "for_appversions": {
                "{ec8030f7-c20a-464f-9b0e-13a3a9e97384}": ["5.0a2", "6.0a1"]
            },
            "tier": 2
        }
    ],
    "metadata": {
        "name": "Best Add-on Evar",
        "version": "9000",
        "guid": "foo@bar.com"
    }
}
```

#### JSON Notes:

##### File Hierarchy

When a subpackage exists, an angle bracket will delimit the subpackage
name and the message text.

If no applicable file is available (i.e.: when a file is missing), the
`file` value will be empty. If a `file` value is available within a
subpackage, then the `file` attribute will be a list containing the
name of the outermost subpackage's name, followed by each successive
concentric subpackage's name, followed by the name of the file that the
message was generated in. If no applicable file is available within a
subpackage, the `file` attribute is identical, except the last element
of the list in the `file` attribute is an empty string.

For instance, this tree would generate the following messages:

```
package_to_test.xpi
    |
    |-install.rdf
    |-chrome.manifest
    |-subpackage.xpi
    |  |
    |  |-subsubpackage.xpi
    |     |
    |     |-chrome.manifest
    |     |-install.rdf
    |
    |-subpackage.jar
       |
       |-install.rdf
```

```js
[
    {
        "type": "notice",
        "message": "<em:type> not found in install.rdf",
        "description": " ... ",
        "file": "install.rdf",
        "line": 0
    },
    {
        "type": "error",
        "message": "Invalid chrome.manifest subject: override",
        "description": " ... ",
        "file": "chrome.manifest",
        "line": 7
    },
    {
        "type": "error",
        "message": "subpackage.xpi > install.rdf missing from theme",
        "description": " ... ",
        "file": ["subpackage.xpi", ""],
        "line": 0
    },
    {
        "type": "error",
        "message": "subpackage.xpi > subsubpackage.xpi > Invalid chrome.manifest subject: sytle",
        "description": " ... ",
        "file": ["subpackage.xpi", "subsubpackage.xpi", "chrome.manifest"],
        "line": 5
    }
]
```

##### Line Numbers and Columns

Line numbers are 1-based. Column numbers are 0-based. This can be
confusing from a programmatic standpoint, but makes literal sense. "Line
one" would obviously refer to the first line of a file.

##### Contexts

The context attribute of messages will either be a list or null. Null
contexts represent the validator's inability to determine surrounding
code. As a list, there will always be three elements. Each element
represents a line surrounding the message's location.

The middle element of the context list represents the line of interest. If
an element of the context list is null, that line does not exist. For
instance, if an error is on the first line of a file, the context might
look like:

```js
[
    null,
    "This is the line with the error",
    "This is the second line of the file"
]
```

The same rule applies for the end of a file and for files with only one line.


## Testing

Tests can be run with

```bash
py.test tests/
```

Functional tests, which take longer, can be run with

 ```bash
py.test functional_tests/
 ```

Then make a cup of tea while all of those tests run. It takes a while. If you
have more than two cores on your machine or you don't mind pwnage, you can try
to increase the number of parallel processes used for testing.

## Releasing

Follow these steps to release a new version of the `amo-validator` Python package:

1. Increment the `__version__` attribute at the top of
   `./validator/__init__.py`.
2. Commit your change to the master branch and run `git push`.
3. Tag master with the new version number, such as `git tag 1.9.8`.
4. Push the new tag with `git push --tags`
5. TravisCI will build and release a new version of `amo-validator`
   to PyPI from your tag commit.
   [Here is an example](https://travis-ci.org/mozilla/amo-validator/builds/90333989).

## Updating

Some regular maintenance needs to be performed on the validator in order to
make sure that the results are accurate.


### App Versions

A list of Mozilla `<em:targetApplication>` values is stored in the
`validator/app_versions.json` file. This must be updated to include the latest
application versions. This information can be found on AMO:

    https://addons.mozilla.org/en-US/firefox/pages/appversions/


### JS Libraries

Lists of JS library hashes are kept to allow for whitelisting or warning. These
must be regenerated with each new library version. To update:

```bash
python extras/update_hashes.py
```

To add new libraries to the mix, edit `extras/jslibfetcher.py` and add the
version number to the appropriate tuple.


### Jetpack

In order to maintain Jetpack compatibility, the whitelist hashes need to be
regenerated with each successive Jetpack version. To rebuild the hash library,
simply run:

```bash
cd jetpack
./generate_jp_whitelist.sh
```

That's it!


### Language Packs

With every version of every app that's released, the language pack references
need to be updated.

We now have an automated tool to ease this tedious process. It is currently
designed to work on OS X with the OS X versions of Mozilla applications, though
it could conceivably run on any \*NIX platform against the OS X application
packages.

To run the tool, first create a new directory: `extras/language_controls/`

Put the `.app` packages for each updated product into this directory. Once
this is ready, simply run:

```bash
cd extras
python update_langpacks.py
```

That should be it. Note that this tool will fail horribly if any of the teams
change the locations that the various language files are stored in.

Also note that this tool should only be run against the en-US versions of these
applications.
