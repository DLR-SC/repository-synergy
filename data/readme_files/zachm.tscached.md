# tscached

![tscached logo]
(https://github.com/zachm/tscached/raw/master/logo/logo.png)

tscached is a smart caching proxy for time series data in the [KairosDB](https://kairosdb.github.io/) format. By engineering toward a drastic improvement in user experience, tscached makes dashboards and charts load over **100x faster** than a standard configuration of KairosDB.

## Motivation

KairosDB is a powerful, scalable solution for storing large amounts of time-series data. It's built on top of an off-the-shelf data store (Cassandra), it ingests data *really fast*, and it stores that data in a *lossless* schema.

Unfortunately, getting data back *out* of KairosDB can be challenging: read performance just isn't as good as write performance. The use cases bear this out: our sources write one datapoint at a time, but our consumers request **hours** of data from **thousands** of time series, which will be formatted into charts and dashboards. To design well for both scenarios is very difficult, so it makes sense to separate a read-performance solution into its own system.

## Design

If you're interested in the original design docs, you can find them [here](https://github.com/zachm/tscached/blob/master/DESIGN.md).

tscached makes a few assumptions:
* Most time series are **write once, read never.** Users care about a only small fraction of total data, but they need to be able to access all of it in a pinch.
* Grafana doesn't care what it's talking to: By reimplementing the KairosDB API, tscached is truly a drop-in solution.
* Consistent hashing is cheap: We can create easy Redis keys based on a query's semantic parts, including its grouping and  aggregation components.
* Redis is fast: We can have plenty of *O(n)* logic during processing because we've lowered our accesses to *O(1).*

tscached makes a few advancements, too:
* A previously issued (and cached) query will be reissued across **only the elapsed time since its
last execution.** While a one-hour tscached query first requires one hour's worth of KairosDB data, the same query made one minute later requires only one minute's worth of data. Dashboard refresh rate is the lowest common denominator!
* Caching **metadata** speeds up the user experience when making dashboards with Grafana. No more lag on dropdown menus!
* Dashboards can be **pre-cached,** eliminating the initial cold scenario, using a *readahead* script included with the service.
* Long queries are **chunked.** Splitting a six-hour query into six one-hour queries, for instance, can improve performance by up to 10x. The client never knows the difference.

Credit where credit is due: [arussellsaw/postcache](https://github.com/arussellsaw/postcache) was a huge inspiration. Postcache is a great solution if an office has 10 monitors all showing the same dashboard such that all load is exactly the same. However, if an office has hundreds of engineers loading thousands of different dashboards, postcache won't help much, since no two dashboards will create the same exact load nor have the same refresh rates.

There are several different frontends to use with a Kairos-compliant API like this one, but the most full-featured remains (as always) [Grafana](http://grafana.org/) with [this plugin](https://github.com/grafana/kairosdb-datasource) installed. And if you're looking to send system metrics *into* KairosDB, do check out [Fullerite](http://github.com/Yelp/fullerite/): it's cross-compatible with Diamond, super efficient, and supports KairosDB out of the box!

## High-Level Architecture
tscached is designed to fit well into a common scenario, where a frontend like Grafana sends read requests to a backing KairosDB cluster. From KairosDB's perspective, tscached behaves just like any other client. From Grafana's perspective, tscached behaves just like any other KairosDB server. This diagram shows one way to hook it all together.

![architecture](https://github.com/zachm/tscached/raw/master/example_architecture.png)


## Installation and Use

### Developing

Building is known to work on OS X (El Capitan) and on Ubuntu Trusty.

On OS X, you'll need to have these installed:
* ```make``` et al. (available from the XCode package)
* [Homebrew](http://brew.sh/), so you don't break the system Python.
```bash
brew install python
pip install virtualenv
make run
```

On Ubuntu, you pretty much just need python2.7 and the standard development packages.

You can also run a single-threaded server that will auto-refresh on code changes:
```bash
make debug
```


### Within a Container
If you're into Docker, the included Dockerfile is pretty self-explanatory.
```bash
$ docker build -t tscached .
$ docker run -d -p 8008:8008 --name=tscached tscached
```

### As a Debian Package
tscached can be deployed via .DEB files and the Upstart system init framework. You'll need [dh-virtualenv](https://github.com/spotify/dh-virtualenv), among other things, to build. The Debian packaging has been tested on **Ubuntu 14.04 Trusty only**, but do feel free to submit patches for other releases.
```bash
$ make package
```

### Configuration Files

```tscached.uwsgi.ini``` contains some uWSGI-specific details, such as port assignments and number of threads/processes to run. It will accept the standard uWSGI INI options.

```tscached.yaml``` contains all relevant configuration details. For initial use, you'll **definitely** want to adjust the host/port entries for Redis and KairosDB. Most of the rest is (moderately) self-explanatory.


# Contributing

Bug reports, success (or failure) stories, questions, suggestions, feature requests, and (documentation or code) patches are all very welcome.

Feel free to ping @zachtm on Twitter if you'd like help running/configuring/dealing with this software.

This project is released with a Contributor Code of Conduct. By participating in this project you agree to abide by its terms.

# Copyright

Copyright 2016 Zach Musgrave.

# License

GNU GPLv3 - See the included LICENSE file for more details.
