# webbies toolkit
## Description
A python3 asynchronous web recon and enumeration tool set. 

### Webbies
Given a list of host,port combinations, this tool will enumerate the service to determine if it is https or http, the title and banner information, and the presence of login forms. Additionally, it will perform asynchronous DNS lookups with a given resolver during both enumeration and retrieval. The tool will respect a given scope list that can be either by IP or in CIDR format. Upon completion, it will analyze the webbies and group the similar sites in order to allow the user to find the more interesting and unique sites faster. Last, a bing API key can be provided to attempt to find other ips or hostnames the target service may be running under. 

#### Features
* Respects scope (including redirects)
* Uses same DNS resolver for enumeration and retrieval by patching aiohttp TCPConnector
* Cached DNS requests by wrapping aiodns
* SSLContext can be modified for specific SSL versions
* Outputs a simple CSV for easy grep-fu of results
* Asynchronous http(s) and dns
* Specialized bingapi search on ip and hostname given bing key

### FDB
Given a list of hosts in url format, a list of extensions, and a word list this tool will dirbust the targets. Results are passed to a 404 detection object to determine if the response is a non-standard 404 response. The 404 detection currently uses a hash of gathered page responses as well as a hash of the pages structure before using expensive sequencematcher ratio. Output is saved in a CSV file and includes start and stop times.

#### Features
* Fast directory/web application eumeration
* Dir bust numerous hosts simultaneously and save all results in a directory in a CSV file per host
* Task control to limit requests per second
* Multiple progress bars for current status on running FDB's
* Include word list used, target, extensions, and start and stop times in CSV file
* 404 detection based on response structure and content

## TODO
* Add state saving feature to both tools

