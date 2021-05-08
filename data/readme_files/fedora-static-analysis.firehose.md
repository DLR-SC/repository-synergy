"firehose" is a Python package intended for managing the results from
code analysis tools (e.g. compiler warnings, static analysis, linters,
etc).

It currently provides parsers for the output of gcc, clang-analyzer, cppcheck,
and findbugs.  These parsers convert the results into a common data model of
Python objects, with methods for lossless roundtrips through a provided
XML format.  There is also a JSON equivalent.

It is available on pypi here:
  https://pypi.python.org/pypi/firehose

and via git from:
  https://github.com/fedora-static-analysis/firehose

The mailing list is:
  https://admin.fedoraproject.org/mailman/listinfo/firehose-devel
  
Documentation can be read here:
  http://firehose.readthedocs.io/en/latest/

Firehose is Free Software, licensed under the LGPLv2.1 or (at your
option) any later version.

It requires Python 2.7 or 3.2 onwards, and has been successfully tested
with PyPy.

It is currently of alpha quality.

The API and serialization formats are not yet set in stone (and we're
keen on hearing feedback before we lock things down more).

Motivation: http://lists.fedoraproject.org/pipermail/devel/2012-December/175232.html

I want to slurp the results from static code analysis into a database,
which means coercing all of the results into some common interchange format,
codenamed "firehose" (which could also be the name of the database).

The idea is a common XML format that all tools can emit that:
  * describes a warning
  * gives source-code location of the warning: filename, function,
    line number.
  * optionally with a `CWE <http://cwe.mitre.org/about/index.html>`_
    identifier
  * potentially with other IDs and URLs, e.g. the ID "SIG30-C" with URL
    https://www.securecoding.cert.org/confluence/display/seccode/SIG30-C.+Call+only+asynchronous-safe+functions+within+signal+handlers
  * optionally describes code path to get there (potentially
    interprocedural across source files), potentially with "state"
    annotations (e.g. in the case of a reference-counting bug, it's useful
    to be able to annotate the changes to the refcount).

together with a simple Python API for working with the format as a
collection of Python objects (creating, write to XML, read from XML,
modification, etc)

I initially considered using JSON, but went with XML because if multiple
tools are going to emit this, it's good to be able to validate things
against a schema (see
`firehose.rng <https://github.com/fedora-static-analysis/firehose/blob/master/firehose.rng>`_,
a RELAX-NG schema).

References to source files in the format can include a hash of the source
file itself (e.g. SHA-1) so that you can uniquely identify which source file
you were talking about.

This format would be slurped into the DB for the web UI, and can have other
things done to it without needing a server:
e.g.:

  * convert it to the textual form of a gcc compilation error, so that
    Emacs etc can parse it and take you to the source
  * be turned into a simple HTML report locally on your workstation

Projects using Firehose:

  * `mock-with-analysis <https://github.com/fedora-static-analysis/mock-with-analysis>`_
    can rebuild a source RPM, capturing the results of 4 different code
    analysis tools in Firehose format (along with all source files that
    were mentioned in any report).
  * The `"firehose" branch
    <http://git.fedorahosted.org/cgit/gcc-python-plugin.git/log/?h=firehose>`_
    of
    `cpychecker <https://gcc-python-plugin.readthedocs.org/en/latest/cpychecker.html>`_
    can natively emit Firehose XML reports
  * https://github.com/paultag/storz/blob/master/wrappers/storz-lintian
