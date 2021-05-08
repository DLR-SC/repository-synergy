Warning this project is obsolete!
=================================

**Skype since version 4+ is using SQLite DB to store everything. Use can standard tools to extract anything you need.**

skypelog.py -- read and save Skype Linux chat history in Python.

Skype for Linux stores user chat history in binary *.dbb files.
skypelog.py implements classes to easily access data in these file in Python.

I couldn't find a working solution for Linux to export/backup chat history.
D-Bus API does not give access to old messages, at least I couldn't make it work.
(possibly a bug, in theory it should work and there is evidence that it did before).

The information on the structure of the DBB files is quite scarce. This script
can serve as a starting point to further investigate the format of these files.

Running the script directly will show two basic options
 --json {compact,full} dump chat messages into single js file (for each account)
        compact - saves only basic information, full - everything
        output is unsorted and lacks wrapping curly braces
 --html save conversations for each account/contact pair in a separate *.html file
        (relies on 'dialog_partner', so group chats are not handled properly)

One can use skypelog.py as a module, then the following classes will be useful:
(see example in apiuse.py)

class SkypeDBB -- generic DBB file reader
    __init__ requires file name and (optionally) maximum record size
        maximum record size can be determined from the file name if omitted
        (e.g. chatmsg512.dbb has maximum record size 512)
    records() -- iterates over all records in file
        returns dictionary with numeric field types as keys
    readrecord(NUM) -- returns dictionary for NUM'th record in file (counts from 0)

class SkypeObject -- base class for DBB records

class SkypeMsgDBB(SkypeDBB) -- chatmsgDDDD.dbb file reader
    reading methods return SkypeMsg instead of 'dict'

class SkypeMsg -- provides human-readable field names for chat message record
    formatting function to convert to full JSON (with all fields)
    and shortened versions of JSON and HTML (as in client UI)

class SkypeAccDBB(SkypeDBB) -- profileDDDD.dbb file reader
    reading methods return SkypeAcc instead of 'dict'

class SkypeAcc -- provides human-readable field names for account record

class SkypeContactDBB(SkypeDBB) -- userDDDD.dbb file reader
    reading methods return SkypeContact instead of 'dict'

class SkypeContact -- provides human-readable field names for contacts record


Interesting discussion of the *.dbb file format:
    http://www.hackerfactor.com/blog/index.php?/archives/231-Skype-Logs.html
    http://www.hackerfactor.com/blog/index.php?/archives/231-Skype-Logs.html#c1055
