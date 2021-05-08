Supybot Git Plugin
==================

This is a plugin for the IRC bot Supybot that introduces the ability to
monitor Git repositories.  Features:

* Notifies IRC channel of new commits.
* Display a log of recent commits on command.
* Monitor as many repository/branch combinations as you like.
* Privacy: repositories are associated with a channel and cannot be seen from
  other channels.
* Highly configurable.

NEWS
----

### November 17, 2012

Interface changes:

* Several commands have been renamed.  Sorry for the inconvenience, but it was
  time to make some common sense usabliity improvements.
* Repository definitions now take a `channels` option instead of a single
  `channel` (although `channel` is supported for backwards compatibility).

Dependencies
------------

This plugin depends on the Python packages:

* GitPython (supports 0.1.x and 0.3.x)
* Mock (if you want to run the tests)

Dependencies are also listed in `requirements.txt`.  You can install them with
the command `pip install -r requirements.txt`.

Configuration
-------------

The Git plugin has a few standard configuration settings, but the primary
configuration - where the repositories are defined - lives in an INI file.
By default, it will look for the file 'git.ini' in the directory where you run
Supybot.  You can override this with "config plugins.Git.configFile
/path/to/file".

Here is an example of a repository definition:

    [Prototype]
    short name = prototype
    url = https://github.com/sstephenson/prototype.git
    commit link = https://github.com/sstephenson/prototype/commit/%c
    channels = #prototype

Most of this will be self-explanatory.  This defines a repository for the
Prototype JavaScript library, so the Git plugin will be able to fetch a copy
of it and display commits as they happen.

Let's break down the possible settings:

* `short name`: *Required.* This is the nickname you use in all commands that
  interact with the repository.

* `url`: *Required.* The URL to the git repository, which may be a path on
  disk, or a URL to a remote repository.

* `channels`: *Required.* A space-separated list of channels where
  notifications of new commits will appear.  If you provide more than one
  channel, all channels will receive commit messages.  This is also a weak
  privacy measure; people on other channels will not be able to request
  information about the repository. All interaction with the repository is
  limited to these channels.

* `branch`: *Optional.* The branch to follow for this repository. If you want
  to follow multiple branches, you need to define multiple repository sections
  with different nicknames.  Default: master.

* `commit link`: *Optional.* A format string describing how to link to a
  particular commit. These links may appear in commit notifications from the
  plugin.  Two format specifiers are supported: %c (7-digit SHA) and %C (full
  40-digit SHA).  Default: nothing.

* `commit message`: *Optional.* A format string describing how to display 
  commits in the channel.  See Commit Messages below for detail.  Default:
  `[%s|%b|%a] %m`

* `commit reply`: *Optional* A format string for displaying commits as replies
  to commands or SHA snarfing (user-triggered events, instead of
  polling-triggered events).  If empty, your `commit message` format will be
  used.  Default: (empty string)

Commit Messages
---------------

Commit messages are produced from a general format string that you define.
It uses the following substitution parameters:

    %a       Author name
    %b       Branch being watched
    %c       Commit SHA (first 7 digits)
    %C       Commit SHA (entire 40 digits)
    %e       Author email
    %l       Link to view commit on the web
    %m       Commit message (first line only)
    %n       Name of repository (config section heading)
    %s       Short name of repository
    %u       Git URL for repository
    %(fg)    IRC color code (foreground only)
    %(fg,bg) IRC color code (foreground and background)
    %!       Toggle bold
    %r       Reset text color and attributes
    %%       A literal percent sign.

The format string can span multiple lines, in which case, the plugin will
output multiple messages per commit.  Here is a format string that I am
partial to:

    commit message = %![%!%(14)%s%(15)%!|%!%(14)%b%(15)%!|%!%(14)%a%(15)%!]%! %m
                     View%!:%! %(4)%l

As noted above, the default is a simpler version of this:

    commit message = [%s|%b|%a] %m

Leading spaces in any line of the message are discarded, so you can format it
nicely in the file.

Configurable Values
-------------------

As mentioned above, there are a few things that can be configured within the
Supybot configuration framework.  For relative paths, they are relative to
where Supybot is invoked.  If you're unsure what that might be, just set them
to absolute paths.  The settings are found within `supybot.plugins.Git`:

* `configFile`: Path to the INI file.  Default: git.ini

* `repoDir`: Path where local clones of repositories will be kept.  This is a
  directory that will contain a copy of all repository being tracked.
  Default: git\_repositories

* `pollPeriod`: How often (in seconds) that repositories will be polled for
  changes.  Zero disables periodic polling.  If you change the value from zero
  to a positive value, call `rehash` to restart polling. Default: 120

* `maxCommitsAtOnce`: Limit how many commits can be displayed in one update.
  This will affect output from the periodic polling as well as the log
  command.  Default: 5

* `shaSnarfing`: Enables or disables SHA sharfing, a feature which watches the
  channel for mentions of a SHA and replies with the description of the
  matching commit, if found.  Default: True

How Notification Works
----------------------

The first time a repository is loaded from the INI file, a clone will be
performed and saved in the repoDir defined above.

**Warning #1:** If the repository is big and/or the network is slow, the
first load may take a very long time!

**Warning #2:** If the repositories you track are big, this plugin will use a
lot of disk space for its local clones.

After this, the poll operation involves a fetch (generally pretty quick), and
then a check for any commits that arrived since the last check.

Repository clones are never deleted. If you decide to stop tracking one, you
may want to go manually delete it to free up disk space.

Command List
------------

* `log`: Takes a repository nickname (aka "short name") and an optional
  count parameter (default 1).  Shows the last n commits on the branch tracked
  for that repository.  Only works if the repository is configured for the
  current channel.

* `repositories`: List any known repositories configured for the current
  channel.

* `rehash`: Reload the INI file, cloning any newly present repositories.
  Restarts any polling if applicable.

As usual with Supybot plugins, you can call these commands by themselves or
with the plugin name prefix, e.g. `@git log`.  The latter form is only
necessary if another plugin has a command called `log` as well, causing a
conflict.

Known Bugs
----------

In Supybot 0.83.4.1, the Owner plugin has a `log` command that might interfere
with this plugin's `log` command.  Not only that, but Owner's `log` is broken,
and raises this exception:

    TypeError: 'NoneType' object is not callable

If you see this, the simplest workaround is to set Git as the primary plugin
to handle the `log` command:

    @defaultplugin log Git

Alternatively, specify `@git log` instead of just `@log` when calling.
This was reported as issue #9.
