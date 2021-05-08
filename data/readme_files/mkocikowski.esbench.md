OBSOLETE / deprecated / decrepit?
--------
Hi, I am no longer supporting this. Leaving the code for reference, but will be removing the supporting s3 data, as I don't want to pay the transfer fees any more. **This code is old and I have no idea if it even runs on modern ES!** I suggest that for benchmarking you put a load on your system while monitoring with Marvel. I consult / optimize ES clusters for a living, so if you have a problem, get in touch (via issues). Also, come over to [our ES meetup](http://www.meetup.com/Elasticsearch-San-Francisco/)! Have a great day, Mik. 

Elasticsearch benchmarking tools
--------------------------------
'esbench' is a set of python 2.7 scripts for benchmarking Elasticsearch. The
two primary uses are for capacity planning (guessing how much oomph you need
to do what what you think you need to do), and for performance tuning (trying
out various index, mapping, and query settings in a consistent and
reproducible manner). 

Installation
------------

For now, since the project is under active development, I recommend that you
install from the 'dev' branch, with: 

    pip install https://github.com/mkocikowski/esbench/archive/dev.zip

This should give you a reasonable stable and reasonably current version. There
is always the 'master' (replace 'dev.zip' with 'master.zip' in the command
above), but I really think for now you are best off with 'dev'. 

Quick start
-----------
With an instance of elasticsearch running on localhost:9200, do: 

	esbench run
	
When the bench run has finished, you can review the results with: 

	esbench show

To get help: 
	
	esbench --help
	esbench <command> --help

Overview
--------
An Elasticsearch index is composed of a set of 1 or more Lucene indexes
(designated as primary and replica 'shards' by ES). The Elasticsearch cluster
routes incoming documents and search requests to individual Lucene indexes /
shards as needed. A single Lucene index is the basic unit on which indexing
and search operations are executed, and so the performance of individual
Lucene indexes largely determines the performance of a cluster. Lucene indexes
store data on disk in append-only 'segments', which can be periodically
cleaned up and merged. The number and size (bytes) of these segments, and the
disk IO, ultimately determine the speed at which data can be retrieved. Read
the
[merge](http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/
index-modules-merge.html) documentation on the ES site. 

The basic approach to benchmarking is to create an Elasticsearch index with 1
primary and no replica shards (a single Lucene index), load it with data, and
run representative use patterns against it, adding more data until the
performance drops below acceptable levels. That will determine the maximum
viable size of a single shard given the data, use patterns, and hardware.
Total expected data size divided by the viable single index size gives then
the number of required shards. With a rule of thumb of no more than 2 shards
per core, this allows for simple capacity planning. 

The 'run' command
-----------------
When the 'run' command is executed, a 'esbench_test' index is created on the
target ES host, populated with provided data, and queried at specified
intervals. The queries which will be executed against the index are provided
in the 'config.json' file. Observations taken while the benchmark is running
are recorded in the 'esbench_stats' index on the ES host. Each benchmark
results in one document of type 'bench' and one or more documents of type
'obs' (observation) added to the 'esbench_stats' index. 

When executed with default arguments, the 'run' command will result in a quick
(too small to be meaningful) benchmark run against the local ES instance,
using US Patent Application data downloaded from S3 (into /tmp, size 99MB).
The intention is to provide sample data to verify that the 'rig is working'
and to familiarize the user with observation data.

The first argument to play with is 'maxsize', the only non-keyword parameter,
which specifies the total number of documents to be inserted into the test
index, or the total byte size of data to be inserted. Default value is 1mb
allows the benchmark to run in just few seconds. Running: 

	esbench run 5gb

will result in an index of about 4.8GB, which starts to yield meaningful
performance information. Experimenting with queries, and the various
parameters (try adjusting the number of segments or optimize calls) will yield
interesting changes. Depending on the specified logging level, you will see
information somewhat like that when running the benchmark: 

	[...]
    INFO:esbench.bench:beginning observation no: 10, 2013-12-31T19:07:37Z
    INFO:esbench.bench:ran query 'match_description_facet_date_histogram' 100 times in 0.34s
    INFO:esbench.bench:ran query 'match_description_sorted_abstract' 100 times in 0.55s
    INFO:esbench.bench:ran query 'match_description' 100 times in 0.33s
    INFO:esbench.bench:finished observation no: 10, id: fc1596c0, time: 1.221
    INFO:esbench.bench:recorded observation into: http://localhost:9200/esbench_stats/obs/fc1596c0
    INFO:esbench.bench:load complete; loaded total 36 lines into index 'esbench_test', total size: 1396489 (1.00mb)
    INFO:esbench.bench:recorded benchmark into: http://localhost:9200/esbench_stats/bench/2a4fb87d
    [...]

As data is stored into the 'esbench_stats' index, you can access it raw (see
the last log line for the URL). This is the raw data, see the 'show' command
for more user-friendly way of looking at the results. 

The config file
---------------
The 'run' command uses a json config file for its index and query settings.
You can see the path to the default config file ('config.json') by running
'esbench run --help' and looking for the value of '--config-file-path'
argument. There are 3 sections to the config file: 

1. 'queries': here you define the queries which will be run against the test data. Each key is a human-readable name, and the value is an ES query. This is the section which you want to customize to match your use patterns; if you are using your own data source with structure different than the default data source, then you definitely need to change the queries. 
2. 'index': settings used for creating test 'esbench_test' index into which test data is loaded. Default shards 1/0, basic mapping. You can change this, specifically the mapping, if you want to experiment with different data sources. 
3. 'config': basic configuration, command line arguments override these settings.

You can specify the config file to use with the '--config-file-path' flag to
the 'run' command. 

Alternative data sources
------------------------
To use data other than the default USPTO Patent Application set, you need 2
things: a source of json documents (formatted in a way to be acceptable to
Elasticsearch), one document per line, and a config file with the 'queries'
section modified to match the data you are feeding in. Assuming that your data
is in a file 'mydata.json', and your config is in 'myconf.json', then this is
what you want to do (the two lines below are equivalent, but the second is
piping data into 'esbench run' on stdin, which you can use with tools like
'esdump' to feed data from a running index into a test rig): 

    esbench run --config-file-path myjson.json --data mydata.json
    cat mydata.json | esbench run --config-file-path myjson.json --data /dev/stdin 

So, let's say you have an index 'myindex' running on 'http://myhost:9200/',
and you want to take your 'real' data from that server, and feed it into your
benchmarking rig (you will need to install the
[esdump](https://github.com/mkocikowski/estools)):

    esdump --host myhost --port 9200 myindex | esbench run --config-file-path myjson.json --data /dev/stdin

Note that the 'size' control still works, so if you want to only get 10mb of data from the source, you do: 
    
    esdump --host myhost --port 9200 myindex | esbench run --config-file-path myjson.json --data /dev/stdin 10mb
    

The 'show' command
------------------
The 'show' command will retrieve previously recorded benchmark information
from an ES instance, and format it and display it as requested. Running it
without parameters will output data in csv format, with only most important
columns present. There are many options available, bun in general, if you are
not satisfied with what you get 'out of the box', the approach is to dump all
the data into a csv, and use whatever tools you prefer to graph / analyze the
data. When you run 'esbench show --help' you will get info on options
available. You can run: 

	esbench show --format tab

to get the data formatted in a table, but honestly, you will need a really big
screen (& tiny font) for that to be any use at this time. Since the data,
columns, orders of magnitude, will all change if you go with data sets / query
sets other than default, I'm not putting much time into 'canned' data
analysis. Put it out to csv files, analyze with outside tools.

Graphing
--------

	esbench show --help

The basic idea is that you dump the fields in which you are interested into a
csv file, and then use whatever tools you prefer to analyze and graph that
data. However, 'esbench show --help' will show you the command line commands
needed to graph the standard data (you will need to have gnuplot on your
system). Since you can access data on remote systems ('--host' and '--port'
arguments), you only need gnuplot on your workstation. 

The 'dump' command
------------------
Dump previously recorded benchmark data as a series of curl calls. These can
be replayed to populate a new index. The idea with this is that this way you
can easily share the raw benchmark data, say by dumping it into gist. Or you
can just copy and paste right in the terminal - it is just a series of curl
calls. To dump into a file:

    esbench dump > foo.curl

To load these into an elasticsearch index on localhost:

    . foo.curl

Data
----
The default data set is US Patent Applications fror years 2005-2012. These
have been pre-parsed and are available for download from S3. The downloading,
unzipping, etc all happens automagically courtesy of the 'esbench.data'
module. To get a sample document: 

    python -m esbench.data | head -1 | python -m json.tool

document counts / byte sizes are as follows: 

- 2005: 16gb, 289617 docs
- 2006: 13gb, 294540 docs
- 2007: 14gb, 300200 docs
- 2008: 15gb, 320525 docs
- 2009: 16gb, 328237 docs
- 2010: 16gb, 333211 docs
- 2011: 16gb, 321182 docs
- 2012: 17gb, 331583 docs

for a total of 123gb of raw data. These files are pre
parsed and stored in S3 so that there is a solid baseline immutable data set
which can be easily shared. 

Tests
-----
Once 'esbench' has been installed (no need for local Elasticsearch instance):

	python -m esbench.test.units

This may take few minutes as part of the test involves downloading a sample
data file from s3. 


License
-------

The project uses [the MIT license](http://opensource.org/licenses/MIT):

    Copyright (c) 2013 Mikolaj Kocikowski
    
    Permission is hereby granted, free of charge, to any person obtaining a
    copy of this software and associated documentation files (the "Software"),
    to deal in the Software without restriction, including without limitation
    the rights to use, copy, modify, merge, publish, distribute, sublicense,
    and/or sell copies of the Software, and to permit persons to whom the
    Software is furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
    THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
    DEALINGS IN THE SOFTWARE.
    
