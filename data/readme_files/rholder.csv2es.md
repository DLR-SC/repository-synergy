csv2es
=========================

.. image:: https://img.shields.io/pypi/v/csv2es.svg
    :target: https://pypi.python.org/pypi/csv2es

.. image:: https://img.shields.io/travis/rholder/csv2es.svg
    :target: https://travis-ci.org/rholder/csv2es

.. image:: https://img.shields.io/pypi/dm/csv2es.svg
    :target: https://pypi.python.org/pypi/csv2es

The csv2es project is an Apache 2.0 licensed commandline utility, written in
Python, to load a CSV (or TSV) file into an Elasticsearch instance. That's
pretty much it. That's all it does. The first row of the file should contain
the field names intended to be used for Elasticsearch documents otherwise things
will get weird. There's a little trick documented below to add a header row in
case the file is missing it.


Features
--------

- Minimal commandline interface
- Load CSV's or TSV's
- Customize the delimiter to something else
- Uses the Elasticsearch bulk API
- Parallel bulk uploads
- Retry on errors with exponential backoff


Installation
------------

To install csv2es, simply:

.. code-block:: bash

    $ pip install csv2es


Usage
-----
::

 Usage: csv2es [OPTIONS]

   Bulk import a delimited file into a target Elasticsearch instance. Common
   delimited files include things like CSV and TSV.

   Load a CSV file:
     csv2es --index-name potatoes --doc-type potato --import-file potatoes.csv

   For a TSV file, note the tab delimiter option
     csv2es --index-name tomatoes --doc-type tomato --import-file tomatoes.tsv --tab

   For a nifty pipe-delimited file (delimiters must be one character):
     csv2es --index-name pipes --doc-type pipe --import-file pipes.psv --delimiter '|'

 Options:
   --index-name TEXT          Index name to load data into           [required]
   --doc-type TEXT            The document type (like user_records)  [required]
   --import-file TEXT         File to import (or '-' for stdin)      [required]
   --mapping-file TEXT        JSON mapping file for index
   --delimiter TEXT           The field delimiter to use, defaults to CSV
   --tab                      Assume tab-separated, overrides delimiter
   --host TEXT                The Elasticsearch host (http://127.0.0.1:9200/)
   --docs-per-chunk INTEGER   The documents per chunk to upload (5000)
   --bytes-per-chunk INTEGER  The bytes per chunk to upload (100000)
   --parallel INTEGER         Parallel uploads to send at once, defaults to 1
   --delete-index             Delete existing index if it exists
   --quiet                    Minimize console output
   --version                  Show the version and exit.
   --help                     Show this message and exit.


Examples
--------

Let's say we've got a potatoes.csv file with a nice header that looks like this::

 potato_id,potato_type,description
 33,sweet,"kinda oval"
 17,regular,bumpy
 91,regular,"perfectly round"
 18,sweet,delightful
 42,fried,crispy
 37,"extra special",crispy

Now we can stuff it into Elasticsearch:

.. code-block:: bash

    csv2es --index-name potatoes --doc-type potato --import-file potatoes.csv

But what if it was tomatoes.tsv and separated by tabs? Well, we can do this:

.. code-block:: bash

    csv2es --index-name tomatoes --doc-type tomato --import-file tomatoes.tsv --tab


Advanced Examples
-----------------

What if we have a super cool pipe-delimited file and want to wipe out the
existing "pipes" index every time we load it up? This ought to handle that case:

.. code-block:: bash

    csv2es --index-name pipes --delete-index --doc-type pipe --import-file pipes.psv --delimiter '|'

Elasticsearch is great, but it's doing something strange to our documents when
we try to facet by certain fields. Let's create our own custom mapping file to
specify the fields used in Elasticsearch for that potatoes.csv called
potatoes.mapping.json:

.. code-block:: json

    {
        "dynamic": "true",
        "properties": {
            "potato_id": {"type": "long"},
            "potato_type": {"type": "string", "index" : "not_analyzed"},
            "description": {"type": "string", "index" : "not_analyzed"},
        }
    }

Now let's load the data with a custom mapping file:

.. code-block:: bash

    csv2es --index-name potatoes --doc-type potato --mapping-file potatoes.mapping.json --import-file potatoes.csv

What if my file is missing the header row, and it's super huge because there are
so many potatoes in it, and everything is terrible? We can use sed to tack on a
nice header with something like this:

.. code-block:: bash

    sed -i 1i"potato_id,potato_type,description" potatoes.csv

As long as you have more disk space than the size of the file, this should be fine.


Contribute
----------

#. Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug.
#. Fork `the repository`_ on GitHub to start making your changes to the **master** branch (or branch off of it).
#. Write a test which shows that the bug was fixed or that the feature works as expected.
#. Send a pull request and bug the maintainer until it gets merged and published. :) Make sure to add yourself to AUTHORS_.

.. _`the repository`: https://github.com/rholder/csv2es
.. _AUTHORS: https://github.com/rholder/csv2es/blob/master/AUTHORS.rst
