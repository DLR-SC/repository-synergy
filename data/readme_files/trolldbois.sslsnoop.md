HOWTO:
------
https://github.com/trolldbois/sslsnoop/wiki/Screencast

  $ sudo easy_install sslsnoop
  $ mkdir outputs

You really have to. Please.
  
  $ sudo sslsnoop    # try ssh, sshd and ssh-agent... for various things
  $ sudo sslsnoop-openssh live `pgrep ssh`       # dumps SSH decrypted traffic in outputs/
  $ sudo sslsnoop-openssh offline --help         # dumps SSH decrypted traffic in outputs/ from a pcap file
  $ sudo sslsnoop-openssl `pgrep ssh-agent` # dumps RSA and DSA keys

and go and check outputs/.

hints :
-------
a) works if scapy doesn't drop packets. using pcap instead of SOCK_RAW  helps a lot now.
b) works better on interactive traffic with no traffic at the time of the ptrace. It follows the flow, after that.
c) Dumps one file by fd in outputs/
d) Attaching a process is quickier with --addr 0xb788aa98 as provided by haystack
    INFO:abouchet:found instance <class 'ctypes_openssh.session_state'> @ 0xb788aa98
e) how to get a pickled session_state file :
  $ sudo haystack --pid `pgrep ssh` sslsnoop.ctypes_openssh.session_state search > ss.pickled


not so FAQ :
============

What does it do, really ?:
--------------------------
It dumps live session keys from an openssh , and decrypts the traffic on the fly.
Not all ciphers are implemented. 

Workings ciphers : aes128-ctr, aes192-ctr, aes256-ctr, blowfish-cbc, cast128-cbc
Partially workings ciphers (INBOUND only ?!): aes128-cbc,  aes192-cbc, aes256-cbc
Non workings ciphers : 3des-cbc, 3des, ssh1-blowfish, arcfour, arcfour1280

It can also dump DSA and RSA keys from ssh-agent or sshd ( or others ).

How do it knows that the structures is valid ? :
------------------------------------------------
You add some constraints ( expectedValues ) on the fields. Pointers are also a good start.

Yeah, but you have to be root, so what's the use ? :
----------------------------------------------------
Monitoring ssh traffic on honeypots ?
Monitoring encrypted traffic on honeypots ?
Monitoring encrypted traffic on ... somewhere your are root ?

It does not work on my openssh ? :
-----------------------------------
tested on OpenSSH 5.5.
Should work on most recent version.. I didn't check for structure modification. but that would explain a lot.
It work really good on intereactive session with no traffic at the time of execution. (clean cipher state in memory)
It can work on a busy ssh stream, *IF* a) the cipher state is clean, b) scapy doesn't loose packets (CPU ?).
-> yeah the GIL really sucks

How can i decrypt a pcap file ? :
----------------------------------
Use the offline mode.
 
Where does the idea comes from ? :
-----------------------------------
use http://www.hsc.fr/ressources/breves/passe-partout.html.fr  to get keys
use http://pauldotcom.com/2010/10/tsharkwireshark-ssl-decryption.html  
 or http://www.rtfm.com/ssldump/ to read streams
use scapy, because it's fun ? but we need IP reassembly . 
pynids could be more useful...
dsniff is now in python ?
flowgrep
use python.


What are the dependencies ? :
----------------------------
python-haystack (same author)
python-ptrace
scapy
python-pcap / python-xxxpcap ( recommended for perf issues )
paramiko (for ssh decryption) [ TODO, extract & kill dep. we only need Message and Packetizer ]
python-psutil 

Conclusion :
------------
poc done.
Next, `pgrep firefox`. 


Biblio
-------

Bringing volatility to Linux
http://dfsforensics.blogspot.com/2011/03/bringing-linux-support-to-volatility.html

Extracting truecrypt keys from memory
http://jessekornblum.com/tools/volatility/cryptoscan.py

python-ptrace ( hey, haypo again)
https://bitbucket.org/haypo/python-ptrace/wiki/Home
https://bitbucket.org/haypo/python-ptrace/wiki/Documentation

from ptrace.debugger.memory_mapping import readProcessMappings

openssl.py is passe-partout.py - OK - 04/03/2011

there is a 2008 paper on aes keys + software in debian
https://citp.princeton.edu/research/memory/

OpenSSH, testing ciphers
========================
     Ciphers
             Specifies the ciphers allowed for protocol version 2 in order of preference.  Multiple ciphers must be comma-separated.  The supported ciphers
             are ???3des-cbc???, ???aes128-cbc???, ???aes192-cbc???, ???aes256-cbc???, ???aes128-ctr???, ???aes192-ctr???, ???aes256-ctr???, ???arcfour128???, ???arcfour256???, ???arcfour???,
             ???blowfish-cbc???, and ???cast128-cbc???.  The default is:

                aes128-ctr,aes192-ctr,aes256-ctr,arcfour256,arcfour128,
                aes128-cbc,3des-cbc,blowfish-cbc,cast128-cbc,aes192-cbc,
                aes256-cbc,arcfour

force one :

ssh -c aes192-ctr log@host


firefox & NSS
=============
INFO:abouchet:found instance <class 'ctypes_nss_generated.CERTCertificateStr'> @ 0xbfe12c20   => sur la stack

INFO:abouchet:Looking at 0x85f00000-0x86000000 (rw-p)
INFO:abouchet:processed 6465536 bytes
ptrace.debugger.process_error.ProcessError: readBytes(0x84d28ae4, 392) error: [Errno 5] Input/output error
## weird ....

4894720


Architecture
============


openssh creates a OpenSSHLiveDecryptatator which inherits a OpenSSHKeysFinder
OpenSSHLiveDecryptatator :
 * connects to/launch a network.Sniffer. (scapy)
 * OpenSSHKeysFinder calls haystack to fetch the session_state
   - memory capture/ptrace is done in a subprocess
   - target process is not under ptrace anymore when openssh runs. 
   - keys are acquired
 * SessionCiphers are created from pickled values from haystack
   - one for inbound traffic
   - one for outbound traffic
 * each SessionCipher is coupled with :
   - a socket given by a TCPStream ( Inbound and Outbound TCPstate)
   - a paramiko Packetizer which is a ssh protocol handler.
 * a cipher engine is used by the paramiko.Packetizer to decrypt data from the TCPStream socket
 * the Packetizer uses :
   - the socket to read it's data from the 'network'.
   - the cipher to decrypt the data
 * a SSHStreamToFile is created for each stream and is given the packetizer and the overall context ( cipher, socket )
   - the SSHStreamToFile try to process the packetizer's outputs into a file.
 * a Supervisor is created to handle traffic ( select on socket )
   - both SSHStreamToFile are given to the Supervisor with their respective socket


TODO:

SSHStream uses the packets is orderedQueue and the cipher, to try to find a SSH packet
 - algo 1 : copy original cipher state, decrypt first block of packet [0], 
              if not valid, drop packet and loop to next one (for x packets) 
              if valid, switch to go-trough mode and queue current + all packets data to socket 

 - algo 2 : try to find a valid packet, block per block/long by long
              if valid, switch to go-trough mode and queue current + all packets data to socket 









