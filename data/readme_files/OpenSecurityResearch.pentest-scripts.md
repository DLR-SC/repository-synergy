Basic Pentest Scripts
-----------------------------------

This is just a bunch of really basic pentest scripts
to help speed up manual validation of vulns and perhaps
leverage the outputs for further attack. No warranty here,
these scripts might be broken!


dns_src_port_check.sh - 
	by brad antoniewicz - Simple script to check if the 
	upstream server randomizes DNS source ports.

mail_relay_check.sh - 
	by brad antoniewicz - Script to check SMTP mail
	relays.

expectheader.sh - 
	by brad antoniewicz - Script to check if the server
	holds the "Expect" HTTP header.

ntpd-mode7-check.py - 
	by brad antoniewicz - script to check if the server
	is vulnerable to CVE-2009-3563.

ntp-CVE-2009-3563.rb -
	by Gursev Singh Kalra - script to check if the server
	is vulnerable to CVE-2009-3563.

hp_inite_tftp_checker.sh - 
	by brad antoniewicz - script to query HP-UX servers
	for specific files via TFTP that are outside of their
	TFTP root

kyocera_check.py - 
	by brad antoniewicz - script to pull directory structure
	from systems running the Kyocera Mita File Utilities.

smtp-vrfy-check.py - 
	by brad antoniewicz - script to do mass SMTP VRFYs 	



