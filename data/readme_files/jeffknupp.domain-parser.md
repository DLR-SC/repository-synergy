# Python domain-parser

Parse domains using the TLD list maintained by publicsuffix.org.

Domains are parsed into their TLD, SLD, and subdomains. TLDs like 'co.uk' are
handled properly. The list of possible TLDs is generated from publicsuffix.org.
The first time the library is run, an HTTP request is made and a `.tld.pickle` file 
is created. Subsequent runs don't make an HTTP request. Rather, they load the
pickle file. If you want to refresh the list, simply delete the pickle file.

## TODO

There are tests, but not enough. I'm hoping that if people find this useful
they'll contribute test cases to the projects.

# New in version 0.0.4

* Use `pylru` and TLD_CACHE to speed up parsing in long-running programs 
