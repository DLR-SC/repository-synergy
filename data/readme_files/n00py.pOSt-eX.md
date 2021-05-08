### Now included in Empire 2.0 Beta
- bashdoor.py - Empire module to backdoor the sudo command
- mail.py - Empire Module to add mail rule persistence 
- piggyback.py - Empire Module for piggybacking off of sudo sessions
-  ard.py - Enables ScreenSharing to allow you to connect to the host via VNC.

It's recommended just to use the Empire modules, but I've left the other scripts I created when initially developing this.  

https://www.n00py.io/2016/10/using-email-for-persistence-on-os-x/

https://www.n00py.io/2016/10/privilege-escalation-on-os-x-without-exploits/

# pOSt-eX - OS X post-exploitation scripts
- mail.py - Creates a an ApleScript payload with Empire and configures a mail rule to launch it
- persist.py - EmPyre module implementation of mail.py
- monitor.py - Piggybacks off a user's sudo session to spawn an agent with root privileges 
- piggyback.py - EmPye module of monitor.py

## MailPersist - Post-exploitation script for OS X persistance 

## ABOUT:
This script creates a new rule in the OS X Mail application to automatically trigger an AppleScript payload when an email is recieved using a trigger word in the subject of the email.

The trigger email will be deleted before it is visible.  The Script Monitor will also be killed imediately after executing the python stager. There should not be any visual indicators. 

## INSTALL:

All dependancies are met on a default installation of OS X.  With that said, you will likely want to use EmPyre to create your AppleScript payload. 
https://github.com/adaptivethreat/EmPyre

## USAGE:
Creating an AppleScript payload with [Empyre](https://github.com/adaptivethreat/EmPyre):
```
(EmPyre) > listeners
(EmPyre: listeners) > set Name mylistener
(EmPyre: listeners) > execute
(EmPyre: listeners) > usestager applescript mylistener
(EmPyre: stager/applescript) > execute
```
Open mail.py and paste the output in the specified area.  Modify the trigger word as you see fit.  

When pasting the AppleScript payload from Empire, you need to make two modifications:
- Double up the backslash characters
- Remove the final double quote 


