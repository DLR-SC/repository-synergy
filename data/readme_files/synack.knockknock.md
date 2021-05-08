Knock Knock - who's there?
==========
**KnockKnock** displays persistent items (scripts, commands, binaries, etc.), that are set to execute automatically on OS X. For a comprehensive presentation on OS X malware, persistence, and KnockKnock, see the following [slides](https://s3.amazonaws.com/s3.synack.com/Synack_Shakacon_OSX_Malware_Persistence.pdf).


**tl;dr/quick start:**
	
	#display persistent components
    $ python knockknock.py


#### details
KnockKnock is command line python script that displays persistent OS X binaries that are set to execute automatically at each boot. Since KnockKnock takes an unbiased approach it can generically detect persist OS X malware, both today, and in the future. It should be noted though, this approach will also list legitimate binaries. However, as KnockKnock by default, will filter out unmodified Apple-signed binaries, the output is greatly reduced, leaving a handful of binaries that quickly can be examined and manually verified.

KnockKnock requires no arguments to enumerate persistent binaries:
	
	#display persistent components
    $ python knockknock.py

However, various command line parameters can be used to control the scanning and output. To see these, run KnockKnock with the **-h** flag. 

	python knockknock.py -h

	optional arguments:
  	-h, --help            		show this help message and exit
  	-p PLUGIN, --plugin PLUGIN		name of plugin
  	-v, --verbosity       		enable verbose output
 	-a, --apple           		include Apple-signed binaries
  	-w, --whitelist       		include white-listed binaries
  	-l, --list            		list all plugins
  	-j, --json            		produce output in JSON format

The extra command line arguments are all optional, and hopefully self-explanatory. However, they are described here for completeness. 

The **-h** command, as previously mentioned provide a brief help, or usage statement.

The **-p** command, (which requires a plugin name), will cause KnockKnock to only execute a single plugin (the default is to run all plugins). This can be useful for testing/debugging purposes, or for limiting the overall output. Note, to enumerate the names of all registered plugins, run KnockKnock with the **-l** command.

The **-v** command enables verbose output. This produces some informational debugging output which may be helpful for testing/debugging, or just to get a behind-the-scenes look at what’s going on. 

The **-a** command instructs KnockKnock to include Apple signed binaries in its output. By default, KnockKnock will not display persistent binaries that are signed by Apple (and who’s signature is still verifiable).

The **-w** command instructs KnockKnock to include white-listed binaries and commands in its output. By default, KnockKnock will not display persistent commands or files that have been verified to be benign (e.g., 3rd-party binaries that included in a pristine install of OS X). 

The **-l** command lists all plugins that are registered with KnockKnock. (Recall that there generally is one plugin per persistence class). As previously mentioned this command is often ran to determine the name of a plugin to pass to the -p command.

The **-j** command instructs KnockKnock to produce output in JSON format. This may be useful for post processing the output.

#### (other) notes:

1. KnockKnock is currently in beta - please report any issues/suggestions/comments.

2. KnockKnock should be executed with the version of Python that was installed by Apple (/usr/bin/python) - as opposed to another version (e.g. Homebrew).
   It may work with other version, but requires the 'objc' python module. For a python installed with Homebrew, install the 'objc' python module via: pip install pyobjc
   
3. KnockKnock was designed for OS X Mavericks...it should work on older versions of the OS, but please report any issues!

4. KnockKnock will provide more comprehensive results if run with root privileges.
