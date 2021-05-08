# Bumpster
The Unofficial Burp Extension for DNSDumpster.com

Yay my first Burp Extension! DNSDumpster.com is a staple when I'm performing recon on an external pentest. You simply supply a domain name and it returns a ton of DNS information and basically lays out the external network topology. It's also extremely useful for gathering subdomains on bug bounties. 

[@PaulWebSec](https://twitter.com/paulwebsec?lang=en) has released an [unofficial python API](https://github.com/PaulSec/API-dnsdumpster.com) for querying dnsdumpster.com programmatically and it's awesome! I decided to turn his API into a burp extension. 

## How it works 

- Select one or more domains in your SiteMap on the Target Tab
- Right Click, select "Add subdomains to scope via Bumpster"
- Bumpster will query dnsdumpster.com for each domain and place discovered subdomains into your Scope!

## Installation 
Confirmed to work on Kali Linux, it should on Ubuntu/Debian, etc. Not too sure about Mac or Windows yet, for Mac you'll have to figure out the Mac version of `pip install dnsdumpster -t .` for it to work. After that it should be a problem, it's just a matter of getting the dependencies to play nice together. Take a look at `install.sh` to see what I mean. 

```
git clone this repo
cd bumpster 
sh install.sh 
```

Now you just need to load bumpster.py into Burp on the Extender Tab, and hopefully you'll be good to go. If you find any issues please create a git issue or a PR :) 

## Dependencies 

DNSDumpsterAPI traditionally uses `requests` and `bs4 (BeautifulSoup)` but apparently Jython has some issues with urllib3 which is used by `requests`. Anyway, I had to refactor PaulWebSec's code to use urllib2, which explains why the installation script replaces the DNSDumpsterAPI.py that comes with the pip module with my custom one. With all that said, the only dependency you have to be aware of is:

```
dnsdumpster 
```

## Shoutout to Black Hat Python

It should be noted that about 50-60% of this code comes from the Black Hat Python book, since it's my first extension I stuck really closely to the book. Anyway shoutout to [@jms_dot_py](https://twitter.com/jms_dot_py) and his amazing book!

## Contribution

Of course, I'm open to any additions/revisions/corrections you guys see fit so submit pull requests and issues whenever!

Happy hacking! 

This project is licensed under the terms of the MIT license.
