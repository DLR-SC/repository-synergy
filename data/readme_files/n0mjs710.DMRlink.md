---
### FOR SUPPORT, DISCUSSION, GETTING INVOLVED ###

Please join the DVSwitch group at groups.io for online forum support, discussion, and to become part of the development team.

DVSwitch@groups.io 

---
**FOR THE IMPATENT PLEASE AT LEAST READ THIS**

There are two ways to "install" DMRlink:

1) Use the mk-drmlink

2) Don't

The mk-dmrlink script will create a directory tree and copy all of the pertient files, making duplicates of some things so that each of the applications have a full set of all of the files they need, standalone.

Not using the mk-dmrlink leaves the structure as it existis in the repo, which is fully functional. It trades the autonomy of the file tree and duplicates for a simpler installation, and the ability to sync to new versions more easily.

The one you use is up to you -- just please don't blindly go download it and type "./mk-dmrlink" becuase that's just what you always do. Please think about it.


##PROJECT: Open Source IPSC Client.
**PURPOSE:** Understanding IPSC, building an open-source IPSC "stack", troubleshooting IPSC performance issues, and as a basis to easily write applications such as logging, bridging, etc.

**IMPACT:** Potential concern from Motorla Solutions, as IPSC is a proprietary protocol.

**METHOD:** Reverse engineering by pattern matching and process of elimination.
  
**PROPERTY:**  
This work represents the author's interpretation of the Motorola(tm) MOTOTRBO(tm) IPSC protocol. It is intended for academic purposes and not for commercial gain. It is not guaranteed to work, or be useful in any way, though it is intended to help IPSC users better understand, and thus maintain and operate, IPSC networks. This work is not affiliated with Motorola Solutions(tm), Inc. in any way. Motorola, Motorola Solutions, MOTOTRBO, ISPC and other terms in this document are registered trademarks of Motorola Solutions, Inc. Other registered trademark terms may be used. These are owned and held by their respective owners.  
  
**PRE-REQUISITE KNOWLEDGE:**  
This document assumes the reader is familiar with the concepts presented in the Motorola Solutions(tm), Inc. MOTOTRBO(tm) Systems Planner.  
  
**CONVENTIONS USED:**  
When communications exchanges are described, the symbols "->" and "<-" are used to denote the *direction* of the communcation. For example, "PEER -> MASTER" indicates communcation from the peer to the master. For each exchange outlined, the initiator of the particular communication will be on the left for the duration of the particular item being illustrated.

**HOW TO USE THIS SOFTWARE:**  
The primary objective is the IPSC "stack" itself, and is represended in dmrlink.py. It gets the majority of work, and the applicaitons are examples to show how dmrlink.py can be used. As such, dmrlink.py, dmrlink.cfg and the ipsc directory are pre-requisites for eveyrthing here. dmrlink.py does very little on it's own, but you should ALWAYS make sure it runs directly, as nothing else will work if it does not. Turn on the logging options, set the logger to DEBUG and watch to make sure everything works right **BEFORE** working with the application files.

dmrlink, optionally, uses three additional files to map DMR identifiers to understandable names. These are the .csv files for subscribers, peers (other repeaters, 3rd party console applications, etc.) and one for common talkgroups. These files are really only meaningful for logging and reporting.

The remaining files are sample applicaitons that sub-class dmrlink. Since dmrlink takes a default action on each packet type, overriding the class methods for particular packet types are how the examples are presented. For example, bridge.py only needs access to group voice packets, so the group_voice class method is overridden to perform the bridging function. In this particlar example, several other class methods are also overridden, but only to set them to do nothing.

**FILES:**  
+ ***dmrlink.py, dmrlink.cfg, ipsc (directory):*** Core files for dmrlink to work
+ ***talkgroup_ids.csv, subscriber_ids.csv, peer_ids.csv:*** DMR numeric ID to name mapping files (optional)
+ ***bridge.py, log.py, rcm.py, playback.py, playback.py, play_group.py, record.py, confbridge.py:*** Sample applications to demonstrate dmrlink's abilities
+ ***files with SAMPLE in the name:*** Configuration files for certain apps - remove "_SAMPLE" and customize to your needs to use. for example, "dmrlink_SAMPLE.cfg" becomes "dmrlink.cfg"

**SAMPLE APPLICATIONS:**

***bridge.py:*** This applicaiton allows DMRlink to function as an IPSC bridge. Bridging means connecting multiple IPSC networks together, and allowing only certain timeslot/group IDs, etc. to pass between them. Sometimes re-writing the talkgroup ID, etc. bridge.py does not have nearly the wealth of features that commercial IPSC bridges do, but works very, very well. One unique feature here is that bridge.py can be told the radio ID of other bridges and can operate in multiple bridge active/standby/standby... configurations -- which is to say, you may have TWO bridges configured in the same IPSC, set to bridge the same talkgroups, but only one will be active at a time, offering multiple-bridge redundancy to minimize service outages. When two or more instances of DMRlink are connected to each other, and they are the ONLY devices in the IPSC, you may trunk many more than 2 packet streams at once between them.

***confbridge.py*** This application This applicaiton allows DMRlink to function as an IPSC bridge. Bridging means connecting multiple IPSC networks together, and allowing only certain timeslot/group IDs, etc. to pass between them. Sometimes re-writing the talkgroup ID, etc.confbridge.py is very similar to bridge.py, except it implements a simpler rule file that works around the concept of a "conference bridge" not unlike you'd use on a telephone system. Or maybe like a "reflector" for those of you who are d$tar users. It's also a lot like a "bridge group" with integrated "super group" characteristics of a c-Bridge.

***log.py:*** This is a logging application based on gathering data from the actual call packet stream. It doesn't do a whole awful lot, but it is an example of the IPSC side of building a back-end data gathering applicaiton without screen-scraping or tcpdumping a c-Bridge, etc. As a sample app, it just logs to the screen, or a file, etc. but it would be trivial to have it log to a database for web presentation, a central syslog server, etc.

***rcm.py:*** Very similar to log.py, but this one uses a feature called "Repeater Call Monitor" to get nearly identical data, but puts a MUCH smaller load on the IPSC network, since user call datastreams aren't forwarded to DMRlink running as (and properly configured as) an RCM. All of the logging, almost none of the overhead. Again, beats the pants off of screen-scraping, tcpdumping, etc.

***playback.py:*** As of this writing, a large multi-national ham radio group has deployed this on TGID 9998 and dubbed it the "parrot". This application can listen to group and/or private voice transmissions and if you trasmit to the group and/or private IDs it's programmed to use, it will record the digital packet stream and then re-play it back. Handy for listening to your audio to see what you actually sound like on the air.

***play_group.py:*** NOT YET STABLE. This applicaiton is for playing back pre-recorded audio messages based on particlar events. Events could be IPSC-based (like a keyup on a particular TS/TGID combination, time of day, etc.). It works, but requires quite a bit of under-the-hood mucking about as of now.

***record.py:*** Companion applicaiton to play_group.py. This will never be "fancy", since it's intended as a utility for network operators to use to capture voice call packet streams to be played back later. It will be improved beyond where it is at now, but not a high priority.


**CONFIGURATION:**

The configuration file for dmrlink is in ".ini" format, and is self-documented. A warning not in the self-documentation: Don't enable features you do not undertand, it can break dmrlink or the target IPSC (nothing turning off dmrlink shouldn't fix). There are options avaialble because the IPSC protocol appears to make them available, but dmrlink doesn't yet understand them. For exmaple, dmrlink does not process XNL/XCMP. If you enable it, and other peers expect interaction with it, the results may be unpredictable. Chances are, you'll confuse applications like RDAC that require it. The advantage to dmrlink not processing XNL/XCMP is that it also cannot "brick" a repeater or subscriber, since all of these dangerous features use XNL/XCMP.

**NOTE:**

This is important: If you e-mail me asking about dmrlink and don't use the phrase "here I am, rock you like a hurricane" (at least initially), I will probably delete your e-mail without reading it. I need to be very clear. This software is NOT intended to be an out-of-box replacement for c-Bridge, SmartPTT, GenWatch, RDAC, etc. Please do not contact me with the express intent of wanting to know how to configure it to do the same thing as any of these fine products in a production environment, because it doesn't do all of the things that they do, and will likely never be something you can "just run" and peform those functions without more knowledge and patience. This is free software, shared with the world so that others can learn from it or do useful things with it. If you want something that is a c-Bridge or SmartPTT, then please go buy one of those products -- they work great, K0USY Group owns and uses both. If you're a tinkerer, or don't need a commercial grade solution, and want to get your "hands dirty", then DMRlink might be right for you. Using dmrlink requires only a very basic understanding of Python. If you have read this README.md, have looked for comments or other direction within the files themsleves, and still can't figure something out, then please e-mail me, and I'll try to help if I can.

***0x49 DE N0MJS***

Copyright (C) 2013-2017  Cortney T. Buffington, N0MJS <n0mjs@me.com>

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA
