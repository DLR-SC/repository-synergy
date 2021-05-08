# procSpy
DISCLAIMER: This tool is still in VERY early stages of development. Please contact me on twitter @kindredsec if you have any questions/concerns/requests. I will continue adding onto this project for the foreseeable future.

procSpy is a Python application that monitors user space commands being ran via /proc parsing, and records said commands in a "queriable" fashion for future investigation. The tool can to be utilized as both a defensive and offensive tool.

[![asciicast](https://asciinema.org/a/244739.svg)](https://asciinema.org/a/244739)

To see the utility in its most basic form, run the `python3 procspyd.py --mode stdout` command. 

WHAT IS PROCSPY DOING?
-------------------
procSpy operates very similarly to the ps utility in that it parses the /proc directory for process information. However, procSpy puts special focus on locating and monitoring user-ran commands specifically, and records said commands for future investigation (or simply output the commands being ran in real-time if desired). The ability to keep a detailed record of the commands being ran by system users makes this utility useful for both red teams and blue teams/system administrators.

DEPLOYMENT OPTIONS
-------------------
procSpy has three core "modes" that it can be ran in, file mode, stdout mode and database mode.
* File Mode: outputs detected commands into a specified output file that is designed to be parsable by the procSpy client at a later time.
* Stdout Mode: output in realtime the commands being detected to the terminal. Results are not "recorded" in any way.
* Database Mode: populates a locally established mySQL database with detected commands which can then be easily queried by the procSpy client.

These deployment modes are not mutually exclusive; for example, you can run procSpy in stdout and file modes at the same time, allowing you to see the commands being ran in realtime as well as having the monitoring session recorded for future investigation. You can even run all three in unision if desired.

Generally speaking, file mode is largely designed to be used in an offensive capacity; upon compromising a system, you can run procSpy on it over a long period of time to monitor the activity of the target system in order to gain deeper access. File mode makes it easy to pull your monitoring results to your attacking box, or simply interact and query the file directly on the target. In fact, in addition to the core procspyd.py file that hosts the core tool, there also exists the procspyd-light.py version which only consists of file mode and is sufficiently cut down in terms of overhead/dependencies to better fit operational needs. Either version will work perfectly for any offensive efforts.

Database mode, on the other hand, is more so designed to be used in a Defensive capacity. Since a local database must be established with the provided setup script, it is highly unadvisable to operate the utility in this way in an offensive capacity (though, I am planning to grant the ability to push procSpy files into a procSpy database independently in the future). With database mode, A system administrator can run procSpy essentially as a daemon, and have a local database constantly populated with the user commands being ran on the system to monitor for suspicious activity. 

WHATS INCLUDED?
----------------
The official repo consists of four main components:
* procspyd.py - The core python application that parses and records the commands on the system.
* procspyd-light.py - Same purpose as procspyd.py, though more so designed with less overhead/noise for offensive operations.
* procspyclient.py - A small python script that parses out procSpy files or the procSpy database. This parsing can be done manually if needed, though it is reccomended to use the client.
* dbsetup.sh - This script establishes the procSpy database. This will only be needed if you intend on using procSpy in database mode.

REQUIREMENTS
--------------
You will need:
* python3
* mysql-connector python module
* mysql-server

CONTACT ME
-------------
* Twitter: https://twitter.com/kindredsec
* Discord: https://discord.gg/CCZCJCu
* Youtube: https://www.youtube.com/channel/UCwTH3RkRCIE35RJ16Nh8V8Q




