#mongol

Mongol.py is a tool that was inspired by a research paper[0] that described the physical location and number of routers
acting for the Great Firewall (GFW) of China 

Mongol is effectively a implementation of the research tool used by Xu etc all, with the intent to demystify some aspects of the GFW.
It is built using scapy[1] for some of the TCP header modification requirements


[0]  http://pam2011.gatech.edu/papers/pam2011--Xu.pdf

[1]  http://www.secdev.org/projects/scapy/

## UPDATE

User @fqrouter has been running with this concept and taken it far past my initial ideas.

Please check out his work at: https://github.com/fqrouter/qiang

##Usage

python mongol.py -i hostslist.txt -o outputfilename.txt

	hostslist.txt --- The input file is a newline seperated list of ip's and domain names of websites hosted within china.

	outputfilename.txt --- The output file will be location where ip addresses of found filtering devices will be printed.

##How it works

Mongol MUST be run on a device that is Internet facing, aka NOT behind a router or firewall.

Mongol works by stimulating the keyword filtering that the GFW uses.  First we create a test connection and check that the 
site is indeed hosting a webserver and is live.  Then by sending the stimulus 'tibetalk' the keyword filtering will become 
active.  Finally we run a TCP header traceroute and find the last hop before RST packets are sent back.  RST packets are the 
GFW's method of stopping connections with filtered keywords.

