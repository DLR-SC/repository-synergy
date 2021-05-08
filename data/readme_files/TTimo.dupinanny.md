Dupinanny backup script
=======================

INTRODUCTION
============

Dupinanny is a simple backup script that drives the duplicity [1] backup
software. Duplicity is an encrypted bandwidth-efficient backup that
supports a number of remote backends such as rsync, Amazon S3 and others.

Dupinanny is released under the GPL, and the latest source code is
available at http://github.com/TTimo/dupinanny/tree/master [2]

Dupinanny was born out of my own need for an automated backup solution
to be deployed on several of my systems. I wanted to do offsite,
whole-system backups, to a windows-based remote storage running rsync.

I realized that I needed to work around some of duplicity's kinks, so
dupinanny was born to provide the following:

- Easily break down a whole-system backup into independent smaller
backups. Due to bandwidth constraints, a full backup to the offsite
location can take several days. If the connection is lost the whole
backup has to be restarted. Through dupinanny's configuration file
you can break your backups into several smaller pieces that are more
likely to backup completely without being interrupted.

- Easy to invoke from cron, with a full backup every once in a while
and smaller incremental backups in between. Duplicity does not support
"rolling incremental" backups so a full backup is needed on a regular
basis.

- Automatic cleanup of old/outdated backups on the backend.

It is likely that duplicity will support backup checkpoints, and rolling
incrementals at some point in the future. That will likely make this
script quite a bit less useful.

LICENSE
=======

Copyright (C) 2008 Timothee Besset
This software is released under the GNU GPL v3. See COPYING.txt.

USAGE
=====

$ ./backup.py --help
Usage: backup.py [options]

Options:
  -h, --help            show this help message and exit
  --dry-run             show commands, do not execute except collection-status
  --cleanup             cleanup only, implies --dry-run
  --remove-older=REMOVE_OLDER
                        run remove_old only, with the given value. implies
                        --dry-run (set the value in the config to customize
                        for each run and do other operations)
  --config=CONFIGFILE   use this config file
  --full                do a full backup

You will need to setup a configuration file, see config.cfg.example for
inspiration.

Last but not least: READ THE SOURCE (backup.py mostly)

Python isn't particularly hard to learn, and the script was designed to be
easy to extend. Dupinanny was mostly written to cover the features I needed
immediately, patches to make it more general and improve support for other
backends than rsync are most welcome.

LINKS
=====

[1] duplicity web site: http://duplicity.nongnu.org/
[2] dupinanny web site: http://github.com/TTimo/dupinanny/tree/master
