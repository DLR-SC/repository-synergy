# pytograph

Reflect local filesystem changes on a remote system in real time, automatically.

*by [Josh Dick][1]*

*[https://github.com/joshdick/pytograph][2]*

## Introduction

### The Motivation

Ever been frustrated by these situations?

* You were editing code directly on a live system and had to remember which files to copy back to your own machine, in order to later get your changes into source control.
* You develop code on your own machine, but had to remember to manually transfer files to a live system to test changes.

Well, I sure have, and that's why I created pytograph.

In a nutshell, you instruct pytograph that there are directory structures on your machine that match directory structures on a remote machine. It monitors the directories on your local machine for changes, then makes identical changes on the remote machine in real time via SFTP. So, if you add/update/delete a file locally, that same file will be automatically added/updated/deleted on the remote machine. If you delete a directory locally, that same directory will be deleted from the remote machine. You get the picture.

### But Why's It Called That?

Pytograph is named after the [pantograph][3], an image duplication device. A pantograph uses the movements of a pen to simultaneously draw a duplicate image. Pytograph is like a pantograph for your files. Python + pantograph = pytograph. 'Nuff said.

### Can't I Just Use rsync?

Yes, you can, but pytograph only needs to be invoked once and automatically keeps things in sync after that. So there's no need to run something like rsync after every change you make locally. Just set it and forget it.

## Installation and Usage

Pytograph requires Python 2.7.

It depends on several third-party Python packages: config, pysftp, and watchdog. The easiest way to install these is via [pip][4]:

`$ pip install config pysftp watchdog`

Once pytograph's dependencies are installed, view the included sample configuration file, pytograph.cfg.dist. This file contains all of pytograph's settings with accompanying explanations.

Make a copy of pytograph.cfg.dist and edit it as appropriate for your environment, then save it as pytograph.cfg in the same directory as the script itself.

Then simply run `pytograph.py` and you're good to go!

*Note: By default, pytograph looks for a pytograph.cfg configuration file located in the same directory as the script itself, but you can specify a custom configuration file location using a command line argument. Run `pytograph.py -h` for details.*

## This Seems Far Too Awesome, What's The Catch?

Pytograph has only been tested against Python 2.7.2 on Mac OS X, but it should theoretically work with all versions of Python 2.7. It should work on Linux or any *NIX. It may even work on Windows...anything's possible! :)

**OBLIGATORY WARNING: Please back up any important data before using pytograph.** While pytograph has worked well for me, I take **no responsibility** if it causes data loss, strange storm patterns, indigestion, zombie attacks, global thermonuclear war, etc. **Use it at your own risk.** 

That said, I welcome questions, comments and GitHub pull requests!

pytograph is released under the Simplified BSD License.

## Now Try It Out Already! :)

  [1]: http://joshdick.net
  [2]: https://github.com/joshdick/pytograph
  [3]: http://en.wikipedia.org/wiki/Pantograph
  [4]: http://pip-installer.org
