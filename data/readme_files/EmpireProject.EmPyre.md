#EmPyre

EmPyre is a pure Python post-exploitation agent built on cryptologically-secure communications and a flexible architecture. It is based heavily on the controller and communication structure of Empire.

The Diffie Hellman implementation is from Mark Loiseau's project [here](https://github.com/lowazo/pyDHE), licensed under version 3.0 of the GNU General Public License.

The AES implementation is adapted from Richard Moore's project [here](https://github.com/ricmoo/pyaes), licensed under the MIT license.

The initial Python launcher code is inspired from MSF's Python Meterpreter launcher [here](https://github.com/rapid7/metasploit-framework/blob/master/lib/msf/core/payload/python/reverse_http.rb), licensed under the BSD-3-clause license.

The collection/osx/keylogger module was originally written by joev [here](https://github.com/gojhonny/metasploit-framework/blob/master/modules/post/osx/capture/keylog_recorder.rb) and licensed under the MSF_LICENSE/BSD 3-clause license.


## Key negotiation


* KEYs = staging key, set per server (used for RC4 and initial AES comms)
* KEYn = the DH-EKE negotiated key
* PUBc = the client-generated DH public key
* PUBs = the server-generated DH public key

The process is as follows:

1. client runs launcher.py that GETs stager.py from /stage0
    launcher.py implements a minimized RC4 decoding stub and negotiation key

2. server returns RC4(KEYs, stager.py) (key negotiation stager)
    stager.py contains minimized DH and AES

3. client generates DH key PUBc, and POSTs HMAC(AES(KEYs, PUBc)) posts to /stage1
    server generates a new DH key on each check in

4. server returns HMAC(AES(KEYs, nonce+PUBs))
    client calculates shared DH key KEYn

5. client POSTs HMAC(AES(KEYn, [nonce+1]+sysinfo) to /stage2

6. server returns HMAC(AES(KEYn, patched agent.py))

7. client sleeps on interval, and then GETs /tasking.uri

8. if no tasking, return standard looking page

9. if tasking, server returns HMAC(AES(KEYn, tasking))

10. client posts HMAC(AES(KEYn, tasking)) to /response.uri

EmPyre Tracker:
https://trello.com/b/NASrG4IW/empyre
