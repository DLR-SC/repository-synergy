#ImpDump

This script will parse the output from Impacket's esentutl.py tool and decode user hashes/hash histories.

This script uses the awesome creddump project to perform the decription, and is heavily based on dshashdump.py code from creddump. Proper credit for the original work is under 'AUTHOR' and 'CREDITS' below.


To extract the hash datatable using in a way to minimize space used, run:
    esentutl.py /path/to/ntds.dit export -table datatable | grep -E "ATTk590689|ATTm3|ATTm590045|ATTr589970|ATTk589914|ATTk589879|ATTk589984|ATTk589918" > output

Or run ./extract.sh (just wraps the syntax for esentutl.py):
    ./extract.sh /path/to/ntds.dit


Then, to extract all users hashes:
    ./impdump.py SYSTEM output

To extract user hash histories:
    ./impdump.py SYSTEM output -history

To extract just the krbtgt hash:
    ./impdump.py SYSTEM output -krbtgt

To decode a specific user hash using raw data:
    ./impdump.py SYSTEM rawRid rawPekKey


## AUTHOR

I DID NOT WRITE CREDDUMP- all credit to the original author:
    creddump is written by Brendan Dolan-Gavitt (bdolangavitt@wesleyan.edu).
    For more information on Syskey, LSA secrets, cached domain credentials,
    and lots of information on volatile memory forensics and reverse
    engineering, check out: http://moyix.blogspot.com/ 

## CREDITS

* (from the creddump readme)
* AAron Walters. Much of the data type parsing code is taken from
  Volatility, an excellent memory analysis framework written in Python.
  He's also a really nice guy, and has helped me out a lot in my
  research.
  
  https://www.volatilesystems.com/default/volatility

* Massimiliano Montoro (mao), for reversing the mechanism Windows uses
  to derive the LSA key so that it can be computed directly from the
  hive files, as decribed in this post:
  
  http://oxid.netsons.org/phpBB2/viewtopic.php?t=149
  http://www.oxid.it/
  
* Jeremy Allison, for the details of the obfuscation applied to password
  hashes in the SAM, as implemented in the original pwdump.
  
  http://us4.samba.org/samba/ftp/pwdump/

* Nicola Cuomo, for his excellent description of the syskey mechanism
  and how it is used to encrypt the SAM in Windows 2000 and above.

  http://www.studenti.unina.it/~ncuomo/syskey/

* Eyas[at]xfocus.org, for x_dialupass2.cpp, which demonstrates how to
  read LSA secrets directly from the registry, given the LSA key.

  http://www.xfocus.net/articles/200411/749.html

  [Note: the above is in Chinese, but quite comprehensible if you use
   Google Translate and can read C ;)]

* Nicholas Ruff, for his perl implementation of des_set_odd_parity,
  which he apparently took from SSLEAY:

  http://seclists.org/pen-test/2005/Jan/0180.html

* Arnaud Pilon, for the details of how to retrieve cached domain, as
  implemented in cachedump.

  http://www.securiteam.com/tools/5JP0I2KFPA.html

* S�bastien Ke, for his cute hexdump recipe:

  http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/142812

LICENSE

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
