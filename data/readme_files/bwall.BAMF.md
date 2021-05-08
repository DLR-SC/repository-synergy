BAMF
====

Botnet Analysis Modular Framework

BAMF is a modular framework designed to be a platform to perform various forms of analysis against botnets.  Since botnets are an expansive and evolving form of malware, this framework is also expansive and evolving.  From gathering information from samples statically, to exploiting the command and control panels, this framework hopes to cover the whole process.

Note: Until I have more time to actually design a v1, I will mostly be uploading different PoCs to this repository into the IntegrationQueue folder.  The purpose of the IntegrationQueue is ideas to incorporate into the design and to store proof of concepts.

bamfdetect has moved to https://github.com/bwall/bamfdetect


Parts
=====
At this point in time, I have decided to break BAMF up into multiple interfacing scripts serving different purposes.  This makes designing quite a bit easier and decreases the requirements for a module.  The proposed parts are as follows (although more tools may be added in the future):

In Progress:

* bamfdetect - Parse binary files and scripts detecting known bots.  Also capable of extracting configuration information from the bot.  This project has moved to https://github.com/bwall/bamfdetect

Concept Only:

* bamfident - Identify botnet panel from URI
* bamfwatch - Parsing pcap or live traffic, identifying known botnet traffic and logging it
* bamfstalk - Monitor the external command structure for a botnet, essentially pretending to be a bot
* bamfbrute - Brute force login credentials to the botnet command and control
* bamfdump - Dump information from the command and control panel (database, credentials, logs, etc)

Versions
--------
Since this framework is still forming, and development is primarily done in limited free time, different parts of this project may be at varying states of stability.

* Stub - This means functionality is yet to exist, and any results returned may be purely for testing purposes.  The stub's interface may change.
* Experimental - This means functionality/design/execution are still being experimented with.  This means the interface may change, and may not be good to base other tools around.
* RC - Release candidates are closer to stable.  There are less chances of changes to the interface.  Changes are likely to be limited to additions.
