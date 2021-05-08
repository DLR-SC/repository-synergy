ssdeep Cluster
==============
ssdeep Cluster clusters files using ssdeep as a comparison algorithm.  Results are written out to a tar file, which puts
the files into a directory with the files its comparable to.  A file can be in multiple groups.  I have found this tool
to be helpful when needing to analyze a large number of samples, with an ever decreasing amount of time to do it in.

Included in the resulting tar file is a .gexf file.  This can be used to visualize the results in [Gephi](https://github.com/gephi/gephi).

Installation
============
    git clone https://github.com/bwall/ssdc.git
    cd ssdc
    sudo python setup.py install

Examples
========

help
----
    bwall@highwind:~$ ssdc -h
    usage: ssdc [-h] [-v] [-r] [-o [output]] [-s] [-d] path [path ...]

    Clusters files based on their ssdeep hash

    positional arguments:
      path                  Paths to files or directories to scan

    optional arguments:
      -h, --help            show this help message and exit
      -v, --version         show program's version number and exit
      -r, --recursive       Scan paths recursively
      -o [output], --output [output]
                            Path to write the resulting tarball to
                            (default=output.tar)
      -s, --storefiles      Store files in output tar
      -d, --dontcompute     Treat input as ssDeep hashes

    ssdc v1.2.0 by Brian Wallace (@botnet_hunter)
