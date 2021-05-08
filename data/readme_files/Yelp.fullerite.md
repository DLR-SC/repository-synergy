# fullerite

[![Build Status](https://travis-ci.org/Yelp/fullerite.svg?branch=master)](https://travis-ci.org/Yelp/fullerite)
[![GoDoc](https://godoc.org/github.com/Yelp/fullerite?status.png)](https://godoc.org/github.com/Yelp/fullerite)

*Fullerite is a metrics collection tool*. It is different than other collection tools (e.g. diamond, collectd) in that it supports multidimensional metrics from its core. It is also meant to innately support easy concurrency. Collectors and handler are sufficiently isolated to avoid having one misbehaving component affect the rest of the system. Generally, an instance of fullerite runs as a daemon on a box collecting the configured metrics and reports them via different handlers to endpoints such as graphite, kairosdb, signalfx, or datadog. 

A summary of interesting features of fullerite include:
 * Fully compatible with diamond collectors
 * Written in Go for easy reliable concurrency
 * Configurable set of handlers and collectors
 * Native support for dimensionalized metrics
 * Internal metrics to track handler performance

Fullerite is also able to run [Diamond](https://github.com/python-diamond/Diamond) collectors natively. This means you don't need to port your python code over to Go. We'll do the heavy lifting for you.

## success story
  * Running on 1,000s of machines
  * Running on AWS and real hardware all over the world
  * Running 8-12 collectors and 1-2 handlers at the same time
  * Emitting over 5,000 metrics per flush interval on average per box
  * Well over 10 million metrics per minute

## how it works
Fullerite works by spawning a separate goroutines for each collector and handler then acting as the conduit between the two. Each collector and handler can be individually configured with a nested JSON map in the configuration. But sane defaults are provided. 

The `fullerite_diamond_server` is a process that starts each diamond collector in python as a separate process. The listening collector in go must also be configured on. Doing this each diamond collector will connect to the server and then start piping metrics to the collector. The server handles the transient connections and other such issues by spawning a new goroutine for each of the connecting collectors. 

![Alt text](/fullerite_arch.jpg?raw=true "Optional Title")

## using fullerite
Fullerite makes a deb package that can be installed onto a linux box. It has been tested a lot with Ubuntu trusty, lucid, and precise. Once installed it can be controlled like any normal service:

    $ service fullerite [status | start | stop]
    $ service fullerite_diamond_server [status | start | stop]

By default it logs out to `/var/log/fullerite/*`. It runs as user `fuller`. This can all be changed by editing the `/etc/default/fullerite.conf` file. See the upstart scripts for [fullerite](deb/etc/init/fullerite) and [fullerite_diamond_server](deb/etc/init/fullerite_diamond_server) for more info. 

You can also run fullerite directly using the commands: `run-fullerite.sh` and `run-diamond-collectors.sh`. These both have command line args that are good to use. 

Finally, fullerite is just a simple go binary. You can manually invoke it and pass it arguments as you'd like. 

## supported collectors
 * [fullerite collectors](src/fullerite/collector)
 * [diamond collectors](src/diamond/collectors)

## supported handlers
 * [Graphite](http://graphite.wikidot.com/)
 * [KairosDB](https://github.com/kairosdb/kairosdb)
 * [SignalFx](https://www.signalfx.com)
 * [Datadog](https://www.datadoghq.com)
 * [Scribe](https://github.com/facebookarchive/scribe)

# AdHoc collectors

Fullerite comes with a cli that makes it possible to run adhoc collectors from a file. All that
is required is for that file, once executed, to **write to stdout** a `JSON` object adhering to a certain [schema](examples/adhoc/schema.json).

The file can be written in the language of your choice **as long as**
you can provide a proper **[shebang](https://en.wikipedia.org/wiki/Shebang_(Unix))** for the kernel to know how to execute that file.

The following is the result of running `fullerite help visualize`:

    NAME:
    fullerite visualize - shortest path from your terminal to your graphs
    USAGE:
    fullerite visualize [command options] [arguments...]
    OPTIONS:
    --die-after, -d "600"                How long (in seconds) to run the collector
    --interval, -i "10"                  How frequent (in seconds) to run your collector
    --config, -c "/etc/fullerite.conf"   JSON formatted configuration file
    --log_level, -l "info"               Logging level (debug, info, warn, error, fatal, panic)
    --profile                            Enable profiling

Example adhoc collectors have been provided for a few languages:
 * [Bash](examples/adhoc/example.sh)
 * [Perl](examples/adhoc/example.pl)
 * [Python](examples/adhoc/example.py)
 * [Ruby](examples/adhoc/example.rb)
 
To run any an adhoc collector from a file you can simply:

    fullerite visualize -i 5 -d 30 examples/adhoc/example.pl

# Contributing to fullerite

We welcome all contribution to fullerite, If you have a feature request or you want to improve
existing functionality of fullerite - it is probably best to open a pull request with your changes.

## Adding new dependency

If you want to add new external dependency to fullerite, please make sure it is added to `src/fullerite/glide.yaml`.
Do not forget to specify `TAG` or `commit_id` of external git repository.  More information about
`glide` can be found at https://github.com/Masterminds/glide.

## Ensure code is formatted, tested and passes golint.

Running `make` should do all of the above. If you see any failures or errors while running `make`,
please fix them before opening a pull request.

## Building and compiling

Running `make` should build the fullerite go binary and place it in the `bin` directory.
