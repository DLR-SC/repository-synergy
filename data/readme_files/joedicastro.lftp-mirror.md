# LFTP MIRROR

It's a python script that allow us to synchronize a directory on a remote server
with a local directory via FTP. For this purpose makes use of the great program
'lftp' by [Alexander V. Lukyanov](http://lftp.yar.ru/), which is indispensable
to run this script.

Sometimes we need to keep two directories synced, one on a remote server and
another stored locally and only have FTP access to the server, with no
possibility of using most appropriate solutions via ssh as rsync. For example,
to back up a website in a shared hosting on which we have no more than an FTP
account to share files.

The problem then is that do this via FTP is slow, because in some ways forces us
to download entire contents of the directory each time or manually control the
changes. No addition, unlike rsync, the power to download only that part of the
file that has changed. Some FTP clients (mostly graphics) allow us to know which
files have changed and download these only, thus accelerating the process of
downloading and reducing network traffic. One of these, lftp, it is also one the
lightest and fastest out there, one of the few that -by default- incorporates
the functionality to synchronize two folders: mirror. This synchronization is
bidirectional, so it can be done in both directions, remote to local and local
to remote. As it is a command line program and supporting the import of settings
via script, is ideal for automating the entire process through a shell script
and crontab to make a fully automatic scheduled synchronization.

Since default lftp supports the use of scripts to automate ftp and programming
tasks automatically through cron is trivial, which is the need to create a
script like this?

Well, this script provides certain advantages over just using lftp:

* Provides a detailed activity log on disk that is human readable and can be
  emailed to one or more directions, either through a local mail server or an
  external one.
* Create a compressed copy of the local synchronized directory for each day of
  the week. This allow us to have the directory updated and a backup for each of
  the last seven days, in order to reverse any changes or accidental deletion.
* It provides (in the log) the size of the space occupied by the local directory
  and the backups in the hard drive.
* It focuses only on the synchronization between directories (mirror), ignoring
  the other options offered by lftp.
* Allows three different execution modes, making it very versatile:
    * As a scheduled task. In this mode the sync parameters are included
      directly in the script and is only necessary to schedule it to automate
      the process. Is perfect for a periodic synchronization for a single
      directory/FTP server.
    * Interactive. In this way the parameters are entered directly as arguments
      on the command line. It is ideal for occasional run a manual
      synchronization.
    * Importing parameters from a configuration file. This mode is similar to
      the first, with the difference that in this case we take the parameters
      from an external configuration file. This file that we create ourselves
      (served one as example) allows us to establish multiple synchronization
      operations that are executed sequentially one after another. So for
      example we can set it in one run synchronize multiple directories/FTP
      servers, without limit on the number of these. We would for example create
      several configuration files that could be programmed to run automatically
      at different time slots, so covering this complex situations that may
      interest synchronize different directories/FTP servers at different
      days/times. For example synchronize some directories (e.g. 10) at night
      and another at noon (e.g. 3) on weekdays, some different (e.g. 4) for the
      weekend. This could be automated with only three configuration files (one
      for each time slot) to synchronize the 17 directories/FTP servers,
      allowing us great flexibility without having to create different scripts
      for each directory/FTP server, just by setting parameters of each action.
* In operating systems that support it, shows pop-up notifications via libnotify
  library of script execution and successful completion. For example, through
  pop-up notifications of Ubuntu. Very useful to know when you are running a s
  cheduled task without shell output.
* If we use the non-interactive execution modes, uses base64 for minimal
  protection of FTP servers' passwords and avoid storing them in clear text. Is
  a weak security measure, but is the least that should be considered.



## FILES

* `lftp_mirror.py`

 The script file

* `sample.cfg`

 A configuration file's example

* `License.txt`

 The GPLv3 license text

* `LEEME.txt`

 This file in Spanish

* `README.txt`

 This file


## PRE-REQUISITES & DEPENDENCIES

### For Linux (not tested in Mac):

Obviously, first we need is python. If we are in Linux usually is installed by
default.

This script uses several modules included in the python standard library.

The python version required to run the script is 2.7. However, it is possible to
run the script in version 2.6 if you install the module argparse, who joined
the standard library in version 2.7.

Linux install is usually straightforward, as it comes included in many
distributions, for example to install in Debian/Ubuntu:

    $ sudo apt-get install python-argparse


### lftp

Obviously it is necessary to install this program, which is what makes the dirty
work.

Again, Linux install is usually straightforward, as it comes included in many
distributions, for example to install in Debian/Ubuntu:

    $ sudo apt-get install lftp


## INSTRUCTIONS

This is a script designed to work in the command line, given the nature of their
function, which is simply to automate a process that once started does not
require further intervention on our part.

If you run the program without arguments shows an error message:

    $ python lftp_mirror.py

    usage: lftp_mirror.py [-h] [-v] {cron,cfg,shell} ...
    lftp_mirror.py: error: too few arguments

That would mean that we need to employ at least some of these arguments: *cron*,
*cfg* or *shell* or options: *-h* or *-v*

These three arguments will be defining the manner of execution of the script, as
we mentioned in the introduction.


### cron

In this mode runs taking as parameters were included in the script itself. This
mode is useful when a synchronization is performed periodically on a single FTP
server/directory.

To run it any easier to locate a block like this in the script and modify the
entries that are between quotations marks, replacing the default values for the
values we need.

    #===========================================================================
    # SCRIPT PARAMATERS TO EXECUTE THE SCRIPT AS A PROGRAMMED TASK
    #===========================================================================

        # ftp user name ('user' by default)
        cron_user = 'user'
        # ftp password, with a minimum security measure, encoded by base64
        # ('password' by default)
        cron_pass = 'cGFzc3dvcmQ='
        # ftp server, name or ip ('localhost' by default)
        cron_site = 'localhost'
        # ftp server port. ('' by default)
        cron_port = ''
        # ftp directory
        cron_remote = 'directory'
        # local directory
        cron_local = '/your/path/to/your/local/directory/'
        # options, same as the shell mode. See shell mode help for more info
        cron_options = ''

    #===========================================================================
    # END PARAMETERS
    #===========================================================================


Finally, only need to add this entry to the crontab (scheduled tasks):

    lftp_mirror.py cron

### cfg

This mode is similar to the previous, except that the parameters are taken from
an external file and allows the execution of several consecutive synchronization
operations. This is ideal for running in a single operation, the synchronization
of multiple FTP servers/directories. Obviously this way could also be
implemented periodically through cron.

To use this mode is only necessary to create a text file with a particular
structure. It includes a sample configuration file as a template for us,
sample.cfg. This file does not necessarily need this extension, but serves to
identify it.

The structure is as follows:

    [section]
    site = {ftp server URL or IP}
    port = (ftp server port)
    remote = {remote directory}
    local = {local directory}
    user = (ftp server username)
    password = (user password encoded in base64)
    options = (other options)

Where *section* is an identifier for the synchronization operation. Would
normally be the name of the FTP server or directory to synchronize.

Values enclosed in parentheses are optional while enclosed in braces are
required. In case you do not specify a username and password, you must add the
*-a* option which specifies that the connection is made with the anonymous user.

You need to create a section like this for every sync operation we want to
perform.

A real example can be seen in **sample.cfg** content:

    [debian]
    site = ftp.debian.org
    port =
    remote = /debian/doc
    local = debian
    user =
    password =
    options = -aenP --exclude-glob '*.txt' --include-glob 'social*'

    [FreBSD]
    site = ftp.freebsd.org
    port =
    remote = /pub/FreeBSD/ERRATA
    local = FreeBSD
    user =
    password =
    options = -aenP

In this real example the two operations are executed sequentially, first
synchronize with the Debian server and would end with the FreeBSD server.

To run the sync operations in this configuration file would use this command:

    python lftp_mirror.py cfg sample.cfg

### shell

This mode is used to perform a synchronization operation specifying the
arguments directly into the command line. It is useful for occasional
synchronization.

For complete instructions, refer to the help built into the script:

    $ python lftp_mirror.py shell -h

Although it could be summarized in this command line:

    $ python lftp_mirror.py shell site remote local -l user password [options]

Where *site* is the FTP server, *remote* the remote directory and *local* the
local directory. *user* and *password* are the FTP server's user and password.

The set of arguments and options are detailed below:

#### Shell mode arguments:

* `site`

 The FTP Server, can be set as an URL or IP address

* `remote`

 Remote directory at FTP Server

* `local`

 Local directory


#### Lftp options available in shell mode:

* `-h, --help`

 Show this mode help

* `-l user password, --login user password`

 The ftp account's username and password

* `-a, --anon`

 Set user as anonymous

* `-p port, --port port`

 To specify a different port to standard FTP (21)

* `-s, --secure`

 Establishes a secure connection via SFTP instead of FTP

* `-e, --erase`

 Delete files in target that are no longer available at source

* `-n, --newer`

 Download only newer files

* `-P [N], --parallel [N]`

 Download N files in parallel, using multiple FTP connections simultaneously. N=2 if not provide any value

* `-r, --reverse`

 Reverse mode. Upload files from local to remote

* `--delete-first`

 Delete old files before transferring new ones

* `--depth-first`

 Descend into subdirectories, before transfer files

* `--no-empty-dirs`

 Do not creates in destiny empty directories that may exist in origin. Needs the `--depth-first` option

* `--no-recursion`

 Don't go to subdirectories

* `--dry-run`

 Simulation, don't execute anything. Writes to log

* `--use-cache`

 Use cached directory listings

* `--del-source`

 Delete files (not directories) in origin after transfer. **CAUTION!**

* `--only-missing`

 Download only missing files

* `--only-existing`

 Download only files already existing at target

* `--loop`

 Loop until no changes found

* `-ignore-size`

 Ignore size when deciding whether to download

* `--ignore-time`

 Ignore time when deciding whether to Download

* `--no-perms`

 Don't set file permissions

* `--no-umask`

 Don't apply umask to file modes

* `--no-symlinks`

 Don't create symbolic links

* `--allow-suid`

 Set suid/sgid bits according to remote site

* `--allow-chown`

 Try to set owner and group on files

* `--dereference`

 Download symbolic links as files

* `--exclude-glob GP`

 Exclude files that matcht the pattern. Where GP is a glob pattern, for example: `*. zip `

* `--include-glob GP`

 Include files that matcht the pattern. Where GP is a glob pattern, for example: `*. zip `


#### Script options that are not present in lftp:

* `-q, --quiet`

 This option allows you to specify the detailed output synchronization process
will not be displayed on the command line and will be added to the registration
of activity (in the file and in the mail).

* `--no-compress`

 With this option will disable the compressed backups of the local directory.

* `--no-email`

 Disables mail delivery with the activity log.


The mail is sent by default to the local user running the script, using the
local mail server. if you want to use a different mail server or send it to
other(s) recipient(s), then it is necessary to use the following options:

* `--smtp_server`

 The mail server that we want to use

* `--smtp_user`

 The mail server user

* `--smtp_pass`

 The password for that user

* `--from_addr`

 The email address to be included as the sender

* `--to_addrs email`

 The email address(es) of who we want to send mail


## REPOSITORY

The code is hosted in a Git repository at GitHub, use this to get a clone:

    git clone git://github.com/joedicastro/lftp-mirror.git


## FEATURES

Every time you complete a execution record is added to the log file that is
created in the local root folder and if not indicated otherwise send an email
with the same content to the local user. An example of this log can be seen in
this e-mail sent after running the sample configuration file, sample.cfg:

    From:       youruser@yourcomputer
    To:         youruser@yourcomputer
    Subject:    FTP Sync - wednesday 08/12/10, 13:52:13
    Date:       Wed, 08 Dec 2010 13:52:13 +0100


    SCRIPT =====================================================================
    lftp_mirror (ver. 0.7)
    http://joedicastro.com

    Connected to ftp.debian.org as anonymous
    Mirror /debian/doc to debian
    ============================================================================

    START TIME =================================================================
                                                    wednesday 08/12/10, 13:51:58
    ============================================================================

    CREATED NEW DIRECTORY ______________________________________________________

    debian


    LFTP OUTPUT ________________________________________________________________

    Sending file `debian-manifesto'
    Sending file `social-contract.txt'
    Replying directory `FAQ'
    Making directory `FAQ'
    Replying directory `dedication'
    Making directory `dedication'
    Sending file `FAQ/debian-faq.en.html.tar.gz'
    Sending file `FAQ/debian-faq.en.pdf.gz'
    Sending file `dedication/dedication-2.2.sigs.tar.gz'
    Sending file `FAQ/debian-faq.en.ps.gz'
    Sending file `dedication/dedication-5.0.sigs.tar.gz'
    Sending file `FAQ/debian-faq.en.txt.gz'



    ROTATE COMPRESSED COPIES ___________________________________________________

    Created file:

    /your/path/debian_08dic2010_13:52_wed.tar.gz


    DISK SPACE USED ============================================================
                                                                        1.35 MiB
    ============================================================================

    END TIME ===================================================================
                                                    wednesday 08/12/10, 13:52:06
    ============================================================================





    SCRIPT =====================================================================
    lftp_mirror (ver. 0.7)
    http://joedicastro.com

    Connected to ftp.freebsd.org as anonymous
    Mirror /pub/FreeBSD/ERRATA to FreeBSD
    ============================================================================

    START TIME =================================================================
                                                    wednesday 08/12/10, 13:52:06
    ============================================================================

    CREATED NEW DIRECTORY ______________________________________________________

    FreeBSD


    LFTP OUTPUT ________________________________________________________________

    Replying directory `notices'
    Replying directory `patches'
    Making directory `patches'
    Making directory `notices'
    Replying directory `patches/EN-04:01'
    Making directory `patches/EN-04:01'
    Sending file `notices/FreeBSD-EN-04:01.twe.asc'
    Sending file `notices/FreeBSD-EN-05:01.nfs.asc'
    Sending file `patches/EN-04:01/twe.patch'
    Sending file `notices/FreeBSD-EN-05:02.sk.asc'
    Sending file `notices/FreeBSD-EN-05:03.ipi.asc'
    Sending file `patches/EN-04:01/twe.patch.asc'
    Sending file `notices/FreeBSD-EN-05:04.nfs.asc'
    Sending file `notices/FreeBSD-EN-06:01.jail.asc'
    Sending file `notices/FreeBSD-EN-06:02.net.asc'



    ROTATE COMPRESSED COPIES ___________________________________________________

    Created file:

    /your/path/FreeBSD_08dic2010_13:52_wed.tar.gz


    DISK SPACE USED ============================================================
                                                                       38.18 KiB
    ============================================================================

    END TIME ===================================================================
                                                    wednesday 08/12/10, 13:52:13
    ============================================================================

## ALTERNATIVES


If my script do not match what you want, here's a summary of alternatives for
UNIX/Linux (which I know). Mine included as reference.

* __lftp-mirror__

  - Language: Python
  - Type: script
  - Features: The above mentioned
  - License: GPLv3
  - Author(s): Me

* __[lftp](http://lftp.yar.ru)__

  - Language: C++
  - Type: shell app
  - Features: Light, fast and powerful. Perhaps the best FTP client available for the command line. Full of options and very versatile
  - License: GPLv3
  - Author(s): Alexander V. Lukyanov

* __[wget -m](http://www.gnu.org/software/wget)__

  - Language: C
  - Type: shell app
  - Features: Only works in one direction: local to remote
  - License: GPLv3
  - Author(s): Hrvoje Nikšić, Mauro Tortonesi, Steven Schubiger, Micah Cowan, Giuseppe Scrivano

* __[csync](http://www.csync.org)__

  - Language: C
  - Type: shell app
  - Features: Bidirectional but only works with sftp. Not as configurable as lftp
  - License: GPLv2
  - Author(s): Andreas Schneider

* __[weex](http://weex.sourceforge.net/)__

  - Language: C
  - Type: shell app
  - Features: Only works in one direction: local to remote
  - License: GPLv2
  - Author(s): Yuuki Ninomiya, Ludovic Drolez

* __[ftpsync](http://sourceforge.net/projects/ftpsync)__

  - Language: Perl
  - Type: script
  - Features: Bidirectional, does not support sftp. Without many options as lftp
  - License: GPLv2
  - Author(s): Christoph Lechleitner

* __[ncftp](http://www.ncftp.com/ncftp)__

  - Language: C
  - Type: shell app
  - Features: Bidirectional. A little messy.
  - License: Clarified Artistic License
  - Author(s): Mike Gleason

* __[curlftpfs](http://curlftpfs.sourceforge.net) + [rsync](http://rsync.samba.org)__

  - Language: C
  - Type: shell app
  - Features: Curlftpfs used to mount a local file system pointed to the FTP server and then used rsync to synchronize
  - License: GPLv2 (curlftpfs) & GPLv3 (rsync)
  - Author(s): Robson Braga Araujo (curlftpfs) & Andrew Tridgell, Paul Mackerras, Wayne Davison (rsync)


## CONTRIBUTION

Contributions and Feedback are most welcome.
To contribute to the improvement and development of this scripts, you can send
suggestions or bugs via the issues.

## LICENSE

The script is distributed under the terms of the
[GPLv3 license](http://www.gnu.org/licenses/gpl.html)

###### *Apologies for any misspelling or syntax error, English isn't my mother tongue.*
