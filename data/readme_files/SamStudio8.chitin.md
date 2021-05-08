chitin
======

**an awful shell for awful bioinformaticians**

`chitin` is a Python based wrapper around your system shell that attempts to keep track of commands and file manipulations to circumvent the problem of not knowing how any of the files in your ridiculously complicated bioinformatics pipeline came to be.

Why?
----

Because I am not a very organised bioinformatician, and despite your best efforts, you probably aren't either.

What does it do?
----------------

* Automatically keeps track of executed commands that yielded a change to the file system
    * Stores the command and information on the filesystem changes
* Checks file formats against some simple rules
    * *e.g.* Does a BAM have reads, and an index (that is up to date)?
* Can parse the `stdout` and `stderr` of commands to keep hold of important metadata
    * *e.g.* What was the overall alignment rate for a given run of say, `bowtie2`?
    * *e.g.* How long did it take to execute command `bar`?
* Can identify certain file formats and store additional metadata on them automatically
    * *e.g.* How many reads appear in a BAM?
    * *e.g.* How many SNPs are called in a VCF?
* Can describe the steps (commands, params and inputs) to reach a given file
    * *e.g.* What commands should I run to recreate file `foo`?
* Attempts to perform sanity checking of your working state
    * *e.g.* Has `foo` changed since it was last seen?
    * *e.g.* Are we about to clobber a file that has downstream importance?
    * *e.g.* Are any of our inputs malformed?

How do I start it?
------------------
Since I trashed version 1.0 of `chitin`, I haven't decided yet.

How does it work?
-----------------

Installing the Python package gives you the executable `chitin`, which launches the `chitin` pseudo-shell. Entered commands are executed underneath `chitin` by the system shell (probably `/bin/sh`). `chitin` attempts to keep track of files that are created, modified and deleted by each command, primarily by comparing their MD5 hashes and hammering members of Python's `os` module. A rather poor framework also permits the specification of handlers to be applied to the `stdout`, `stderr` and command strings of certain commands. It's also possible to specify handlers when certain file formats are encountered.

Why not just...
---------------

I've tried. I have scripts to generate inputs and results, but I forget to keep track of tweaks to them. Sometimes I try new data or parameters ad-hoc and forget to change them back, or make notes on why I made that change. Occasionally I have to edit files manually and can't easily document what I did. I never write down the data munging commands that I needed to co-erce a particular file through my pipeline that one time. I try and remember to take logs, but often they become detached from the output of the thing that they logged. I even went through a phase of just tarring up the entire directory for every shot at an experiment. None of this has proven effective for me.

`chitin` might not either, but who knows.

Is `chitin` for me?
-------------------
Probably, but not yet. Thanks for taking an interest, but `chitin` is a little while away from stable. The database schema, API and day-to-day functionality are all high-risk, check out Issue #38 (https://github.com/SamStudio8/chitin/issues/38) for progress.

License
-------
`chitin` is distributed under the MIT license, see LICENSE.
