AutoDMGUpdateProfiles
=====================


This repository contains three utilities to help generate update profiles for [AutoDMG](https://github.com/MagerValp/AutoDMG)


~autodmg-rss.py~ (currently broken)
--------------

The rss parsing script is broken, hunt down updates from [Apple's Downloads page](https://support.apple.com/downloads) instead.
~`autodmg-rss.py` reads [Apple's RSS feed for software updates](http://rss.support.apple.com/?channel=DOWNLOADS) and creates a plist with the name and URL of each update. Not all updates have standard download buttons, and some updates are only available from Software Update, so some will still have to be added manually.~


autodmg-checksum.py
-------------------

`autodmg-checksum.py` takes the plist from `autodmg-rss.py` and downloads each update that doesn't have the sha1 checksum or size set. It also updates the PublicationDate to the current time, and it saves the updates for you in `AutoDMG/Updates`.


autodmg-verify.py
-------------------

`autodmg-verify.py` checks for common errors, such as plist syntax errors, unreferenced updates, or forgetting to update the PublicationDate.


Suggested Workflow
==================

0. [Fork this repository](https://help.github.com/articles/fork-a-repo/) and [check out your fork](https://help.github.com/desktop/guides/getting-started/) out on your admin machine.
1. Install a bare OS on a test machine, and perform initial setup.
2. Run `sudo softwareupdate -l -a`.
3. Note the updates and the order they appear in.
4. ~Run `./autodmg-rss.py updates.plist`.~
5. ~Use `updates.plist` to update AutoDMG's `UpdateProfiles.plist`, while paying attention to installation order.~
6. Manually add any updates that `autodmg-rss.py` doesn't find (see below), and remove deprecated updates.
7. Run `./autodmg-checksum.py UpdateProfiles.plist`.
8. Run `./autodmg-verify.py UpdateProfiles.plist`.
9. Run `./install.sh` to move `UpdateProfiles.plist` into `~/Library/Application Support/AutoDMG` for testing.
10. Build an image with updates applied.
11. Deploy it and verify that no additional updates are required.
12. Commit changes and submit a [pull request](https://help.github.com/articles/creating-a-pull-request-from-a-fork/).

Finding iTunes Updates
======================

The latest installer for iTunes can usually be found at [http://www.apple.com/itunes/download/](http://www.apple.com/itunes/download/). Start a download and then copy the URL from your browser's download dialog.


Downloading from sucatalogs
===========================

Some updates, notably Safari's, are never posted to Apple's rss feed. They are however posted to Apple's Software Update catalog, and there's a script in the repo to help you find them:

    $ ./sucatalog.sh
    $ egrep -i 'safari.*\.pkg' *.sucatalog | cut -d\> -f2-| cut -d\< -f1 | sort -u 
    http://swcdn.apple.com/content/downloads/17/39/031-72723/qjk9m4oqqk3jn16o5w4gupeta7uqek1lhi/Safari10.0YosemiteSeed.pkg
    http://swcdn.apple.com/content/downloads/18/14/091-9898/opy4mtpobcg21e1xj2l0uy9ayvq2ys59zs/Safari5.1.10SnowLeopard.pkg
    http://swcdn.apple.com/content/downloads/43/04/031-05867/xcrpn0l2nziw9mglb0gksv2rndu0nquggd/Safari6.1.6Lion.pkg
    http://swcdn.apple.com/content/downloads/45/36/031-28342/piu9tsargpvuaxdnlhf1s0dulnxiuxc8ee/Safari6.2.8MountainLion.pkg
    http://swcdn.apple.com/content/downloads/47/05/031-75479/smgdhqybff3jofycbq8uuciu5td7co45am/Safari9.1.3Mavericks.pkg
    http://swcdn.apple.com/content/downloads/50/48/031-74172/ysyvw0y92rsipxbxb4yxyw5mo2fqc9hcmq/SafariTechPreviewElCapitan.pkg
    http://swcdn.apple.com/content/downloads/62/05/031-75481/c10gu5qoz8bbbk1jczzzvxm9ih4fupo0wz/Safari9.1.3Yosemite.pkg
