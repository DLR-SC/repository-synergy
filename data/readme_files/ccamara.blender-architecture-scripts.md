Blender architecture scripts
============================

This repo contains a collection of Blender scripts and plugins specially useful for architecture. 
This repo serves these main purposes:

1. Make it easy to find all these scripts which are usually spread into different places (eg. dropbox folders, authors' blogs, blender wiki...) and thus difficult to find.
2. Provide a backup or a time-proof repository which don't rely on 3rd pary (I've been always concerned that those scripts could be lost sometime).
3. Benefit from Git and github's social features in order to make it easier to collaborate and improve plugins.


Please note that this doesn't mean that all these addons and scripts are necesarilly going to be mantained. This responsability, as well as their credits relies on each script's authors and mantainers.

[Visit this wiki page](https://github.com/ccamara/blender-architecture-scripts/wiki/List-of-available-addons) to see all the information regarding to the addons that have been included on this repo.

## Instructions

We provide two different ways to use this repo: basic usage (no git knowledge required) and advanced usage for those who want to benefit from all git's features such as cloning, forking, contributing, updating...

###Basic usage

1. Download this repo's content from the [download link](https://github.com/ccamara/blender-architecture-scripts/archive/master.zip)
2. Extract it into your blender's scripts' folder (this may be different depending on your operating system, so if in doubt, please check [this page](https://www.blender.org/manual/getting_started/installing/configuration/directories.html) to know where should you place them)
3. Enable the desired plugin from Blender's properties' dialog box.

###Advanced usage

1. Navigate to your blender's scripts' folder
2. Clone this repo using the following command: ```git clone git@github.com:ccamara/blender-architecture-scripts.git```
3. In case you want to update your local code from the latest code from this repo you have to execute the following commands 
4. `git pull` to retrieve all the files (Except all the files cloned from other repositories.
4. Since this repo uses gitsubmodules you'll have to perform some extra commands: `git submodule init` and then `git submodule update`

##More information/help
If you have doubts you can always read the [repo's wiki page](https://github.com/ccamara/blender-architecture-scripts/wiki) or check our [issue queue](https://github.com/ccamara/blender-architecture-scripts/issues)
