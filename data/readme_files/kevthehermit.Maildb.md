Maildb
======
Welcome to the Mail DataBase although it has expanded slightly now. Here is a list of all the things it does at the moment

### Submit email from PCAP, Text stream, IMAP or POP servers
- The email parser will read the headers extracting the main fields
- Links, Img tags and Iframes sources extracted and listed
- Any attatchments are extracted, Hashed stored and scanned with Yara, optionally you can include options to scan with Clam AV and submit to Virus Total
- All the information extracted above is stored in to a SQLite Database as a Task.
- All files are stored for further analysis
- Options to submit file attatchments to Sandboxs, Cuckoo or FireEyes, MAS

###Http PCAP files
- Extract all the streams
- Parse the HTTP Headers
- Extract all the HTTP Objects and files
- Replicate the Server Path structure
- Write the Header data to the SQLite Database as a Task

### Management System
- Micro management system allows you to track Tasks in the Database
- Add Comments to Tasks
- Set tasks as Reviewed, Events or Unchecked
- Generate, Weekly, Montly, Yearly reports on all Submitted tasks
- Trend analysis on all artefacts in the database


Requires:
=========

- Python 2.7
- Mako
- Bottle
- Yara
- BeautifulSoup (Included)


Recommended:
============

- Cuckoo
- SSDEEP
- python requests required for Cuckoo API 

INSTALL:
=========

- See the INSTALL file for installation details

Tested On
=========

- Ubuntu 12.04
- Windows 7 x64


To Do
=====
- Implement Cuckoo API
- Finish the VT Function
- Timer for the IMAP / POP Feeds
- More reports / trends.
