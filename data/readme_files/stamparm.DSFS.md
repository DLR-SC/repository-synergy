Damn Small FI Scanner [![Python 3.x](https://img.shields.io/badge/python-3.x-yellow.svg)](https://www.python.org/) [![License](https://img.shields.io/badge/license-Public_domain-red.svg)](https://wiki.creativecommons.org/wiki/Public_domain)
=========

**Damn Small FI Scanner** (DSFS) is a fully functional [File inclusion](https://en.wikipedia.org/wiki/File_inclusion_vulnerability) vulnerability scanner (supporting GET and POST parameters) written in under 100 lines of code.

![Vulnerable](https://i.imgur.com/pgYS6cW.png)

As of optional settings it supports HTTP proxy together with HTTP header values `User-Agent`, `Referer` and `Cookie`.

Sample runs
----

```
$ python dsfs.py -h
Damn Small FI Scanner (DSFS) < 100 LoC (Lines of Code) #v0.2a
 by: Miroslav Stampar (@stamparm)

Usage: dsfs.py [options]

Options:
  --version          show program's version number and exit
  -h, --help         show this help message and exit
  -u URL, --url=URL  Target URL (e.g. "http://www.target.com/page.php?id=1")
  --data=DATA        POST data (e.g. "query=test")
  --cookie=COOKIE    HTTP Cookie header value
  --user-agent=UA    HTTP User-Agent header value
  --random-agent     Use randomly selected HTTP User-Agent header value
  --referer=REFERER  HTTP Referer header value
  --proxy=PROXY      HTTP proxy address (e.g. "http://127.0.0.1:8080")
```

```
$ python dsfs.py -u http://testphp.vulnweb.com/showimage.php?file=./pictures/2.jpg
Damn Small FI Scanner (DSFS) < 100 LoC (Lines of Code) #v0.2a
 by: Miroslav Stampar (@stamparm)

* scanning GET parameter 'file'
 (i) GET parameter 'file' appears to be (R)FI vulnerable (e.g.: 'http://testphp.vulnweb.com/showimage.php?file=https%3A%2F%2Fraw.githubusercontent.com%2Fstamparm%2FDSFS%2Fmaster%2Ffiles%2Fconfig.php')
 (i) GET parameter 'file' appears to be (S)FI vulnerable (e.g.: 'http://testphp.vulnweb.com/showimage.php?file=data%3A%2F%2Ftext%2Fplain%3Bbase64%2CPD9waHAgZWNobyBiYXNlNjRfZGVjb2RlKCdUR1ZuWVd3Z1pHbHpZMnhoYVcxbGNqbz0nKTs%2FPg%3D%3D')

scan results: possible vulnerabilities found
```

Requirements
----
[Python](http://www.python.org/download/) version **3.x** is required for running this program.
