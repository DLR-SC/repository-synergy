# modDetective
DISCLAIMER: This tool is still in VERY early stages of development. Please contact me on twitter @kindredsec if you have any questions/concerns/requests. I will continue adding onto this project for the foreseeable future. In it's current implementation, walking the filesystem is done linearly and in one thread; I expect to try and expand this to implement multiple threads to make the tool more efficient. On normal systems, however, the tool is able to walk the entire filesystem in approximately 30 seconds, and that is not including the common exclusions most users will make (/usr, /lib, etc). Please proceed with caution when using this tool on very large systems; it may not be able to handle the load in its current implementation.

modDetective is a small Python tool that chronologizes files based on modification time in order to investigate recent system activity. This can be used in red team engagements and CTF's in order to pinpoint where escalation and attack vectors may exist. This is especially true in CTF's, in which files associated with the challenges often have a much newer modification date than standard files that exist from install. 

[![asciicast](https://asciinema.org/a/244741.svg)](https://asciinema.org/a/244741)

To see the tool in its most useful form, try running the command as follows: `python3 modDetective.py -i /usr/share,/usr/lib,/lib`. This will ignore the */usr/lib*, */usr/share*, and */lib* directories, which tend not to have anything of interest. Also note that by default the "dynamic" directories are ignored (*/proc*, */sys*, */run*, */snap*, */dev*).

# What is modDetective Doing?
modDetective is very elementary in how it operates. It simply walks the filesystem, with bounds determined by user specified options (-i is for ignore, meaning the tool will walk every directory EXCEPT for the ones specified in the -i option, and -e is for exclusive, meaning the tool will ONLY walk the directories specified). While walking, it picks up the modification times of each file, then orders these modification times in order to output them chronologically. 

Additionally, in the output you will potentially see some files highlighted red. These files are denoted as "Indicators of User Activity," Since recent modifications to these files indicate that a user is currently active. As of now, these files include *.swp* files, *.bash_history*, *.python_history* and .*viminfo*. This list will be extended as I brainstorm more files that indicate present user activity. 

# Requirements
modDetective currently works only with python3; python2 compatability will be completed shortly (hence the lack of f strings). Standard libraries should be fine.

# Contact Me
- Twitter: https://twitter.com/kindredsec
- Discord: https://discord.gg/CCZCJCu
- Youtube: https://www.youtube.com/channel/UCwTH3RkRCIE35RJ16Nh8V8Q
