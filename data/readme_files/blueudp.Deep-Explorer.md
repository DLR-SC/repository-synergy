# Deep Explorer
<a href="https://asciinema.org/a/SKw4WnRSoPiccWXSsNmBbKdGX" target="_blank"><img src="https://asciinema.org/a/SKw4WnRSoPiccWXSsNmBbKdGX.svg" /></a>
# Dependencies
     pip3 install -r requirements.txt
also you should have Tor installed    
# Usage

python3 deepexplorer.py STRING_TO_SEARCH NUMBER_OF_RESULTS TYPE_OF_CRAWL

Examples:

python3 deepexplorer.py "legal thing" 40 default legal (will crawl if results obtained in browser do not reach 40, also the script will show links which have "legal" string in html [like intext dork in google])

python3 deepexplorer.py "ilegal thing" 30 all dni(will crawl every link obtained in browser [ultil reachs 30], also the script will show links which have "dni" string in html [like intext dork in google])

python3 deepexplorer.py "legal thing" 30 none (do not crawl, only obtain links from browser)

# About
Deep Explorer is a tool designed to search (any) thing in a few seconds

Any idea, failure etc please report to telegram: blueudp

results.txt contains results obtaioned in previus search

Tested in ParrotOS and Kali Linux 2.0

# Type of Errors
+ Error importing... -> You should try manual pip install package
+ Error connecting to server -> Cant connect to ahmia browser
If deep explorer can not execute service ..., do it manually, deep explorer checks the tor instance at the beginning so it will skip that part
# Is this illegal?
It depends, Deep Explorer is not designed with the purpose of searching illegal things, remember that Tor it's a simple network

# Contact Me
Name: Eduardo Pérez-Malumbres

Telegram: @blueudp

Twitter: https://twitter.com/blueudp
