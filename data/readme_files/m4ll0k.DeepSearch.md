
 Konan - Advanced Web Application Dir Scanner (beta v.0.1.0)
 ---

![screen](https://i.imgur.com/w3bQRoW.png)

__Konan__ is an advanced open source tool designed to brute force directories and files names on web/application servers. 


Installation
---

Download *Konan* by cloning the Git repository:

`git clone https://github.com/m4ll0k/Konan.git konan`

Install requirements with `pip`

`cd konan && pip install -r requirements.txt`

Run *Konan*

`python konan.py`


Support Platforms
---
 - Linux
 - Windows
 - MacOSX


Features
---

 Features| Konan | dirsearch | dirb | gobuster |
 ------- | ----- | --------- | ---- | -------  |
| MultiThreaded | yes | yes |yes | yes |
| Multiple Extensions | yes | yes | no | no |
| HTTP Proxy Support | yes | yes | yes | yes |
| Reporting | yes (text and json) | yes (text and json) | yes (text) | no |
| User-Agent randomization | yes | yes | no | no |
| Ignore word in wordlist using `regexp` | yes | no | no | no |
| Split extension in wordlist  | yes | no | no | no |
| Multiple Methods  | yes | yes (POST only) | no | no |
| Response Size Process | yes | no | no | no |
| Provide Sub-Dir for Brute Force | yes | yes | no | no |
| Provide Dir for Recursively Brute Force | yes | yes | no | no |
| URL Injection Point | yes | no | no | no |


Usage
---

_Basic:_

 - `python konan.py -u/--url http://example.com/`
 
```
URL: http://testphp.vulnweb.com/

PERCENT	 -   TIME   - CODE  -   METHOD  - LENGTH - URL
-------------------------------------------------------
0.39%    - 01:32:50 -  200  -	GET	-  4958    - http://testphp.vulnweb.com/index.php 
0.43%    - 01:32:52 -  200  -	GET	-  4732    - http://testphp.vulnweb.com/search.php 
0.54%    - 01:32:57 -  200  -	GET	-  5523    - http://testphp.vulnweb.com/login.php 
0.81%    - 01:33:12 -  200  -	GET	-  4830    - http://testphp.vulnweb.com/logout.php 
8.77%    - 01:40:02 -  302  -	GET	-  14      - http://testphp.vulnweb.com/userinfo.php  -> login.php

```

_Injection Point:_

 - `python konan.py -u/--url http://example.com/%%/index.php`
 
```
URL: http://testphp.vulnweb.com/%%/index.php

PERCENT	 -   TIME   - CODE  -   METHOD  - LENGTH - URL
-------------------------------------------------------
0.39%    - 01:32:50 -  200  -	GET	-  4958    - http://testphp.vulnweb.com/test/index.php 
0.43%    - 01:32:52 -  200  -	GET	-  4732    - http://testphp.vulnweb.com/search/index.php 

```

 - `python konan.py -u/--url http://example.com/test%% -w /root/numbers.txt`

```
URL: http://testphp.vulnweb.com/test%%

PERCENT	 -   TIME   - CODE  -   METHOD  - LENGTH - URL
-------------------------------------------------------
0.39%    - 01:32:50 -  200  -	GET	-  4958    - http://testphp.vulnweb.com/test12
0.43%    - 01:32:52 -  200  -	GET	-  4732    - http://testphp.vulnweb.com/test34 

```
 
 _Provide wordlist, default `/db/dict.txt`:_

 - `python konan.py -u/--url http://example.com/ -w/--wordlist /root/dict.txt `

_Provide extensions with `-e/--extension` option and force extension for every wordlist entry with `-f/--force` option:_

 - `python konan.py -u/--url http://example.com/ -e/--extension php,html -f/--force`
 
 ```
 URL: http://testphp.vulnweb.com/

PERCENT	 -   TIME   - CODE  -   METHOD  - LENGTH - URL
-------------------------------------------------------
0.39%    - 02:00:21 -  200  -	GET	-  4958    - http://testphp.vulnweb.com/index.html 
0.43%    - 02:00:23 -  200  -	GET	-  4732    - http://testphp.vulnweb.com/search.php 
0.54%    - 02:00:30 -  200  -	GET	-  5523    - http://testphp.vulnweb.com/login.php 
0.81%    - 02:00:46 -  200  -	GET	-  4830    - http://testphp.vulnweb.com/logout.html 
0.87%    - 02:00:50 -  200  -	GET	-  6115    - http://testphp.vulnweb.com/categories.html
 ```
 
 
 
 _Provide status code exclusion:_

 - `python konan.py -u/--url http://example.com/ -x/--exclude 400,403,401`

_Provide only status code for output:_

 - `python konan.py -u/--url http://example.com/ -o/--only 200,301,302`
 
 _Wordlist lowercase (isATest -> isatest) and uppercase (isAtest -> ISATEST):_

 - `python konan.py -u/--url http://example.com/ -w/--wordlist /root/dict.txt [-l/--lowercase OR -p/--uppercase]` 

_Wordlist split (test.php -> to -> test):_

 - `python konan.py -u/--url http://example.com/ -w/--wordlist /root/dict.txt -s/--split`

_Wordlist Ignore word,letters,number,..etc provided by regexp (`\w*.php|\w*.html`,`^[0-9_-]+`):__

 - `python konan.py -u/--url http://example.com/ -w/--wordlist -I/--ignore "\?+"`
 
Output without `-I/--ignore` options:
 
 ```
 URL: http://testphp.vulnweb.com/

PERCENT	 -   TIME   - CODE  -   METHOD  - LENGTH - URL
-------------------------------------------------------
0.39%    - 02:06:31 -  200  -	GET	-  4958    - http://testphp.vulnweb.com/???.php 
0.43%    - 02:06:32 -  200  -	GET	-  4732    - http://testphp.vulnweb.com/??????????? 
0.54%    - 02:06:35 -  200  -	GET	-  5523    - http://testphp.vulnweb.com/admin/ 
 ```
 
Output with `-I/--ignore` (in this case `\?+`) options:
 
```
 URL: http://testphp.vulnweb.com/

PERCENT	 -   TIME   - CODE  -   METHOD  - LENGTH - URL
-------------------------------------------------------
0.54%    - 02:06:35 -  200  -	GET	-  5523    - http://testphp.vulnweb.com/admin/ 
 ```
 
 _Recursive:_

 - `python konan.py -u/--url http://example.com/ -E/--recursive`
 
 _Recursive directory found and directory provided by `-D/--dir-rec`:_

 - `python konan.py -u/--url http://example.com/ -E/--recursive -D/--dir-rec "admin,tests,dev,internal"`
 
 _Brute Force directory provided by `-S/--sub-dir`:_

 - `python konan.py -u/--url http://example.com/ -S/--sub-dir "admin,test,internal,dev"`
 
 _Multiple Methods (check GET,POST,PUT and DELETE for word entry)_:
 
 Note: Much web application if not make the request with right method return 404 code, this option test all methods
 
  - `python konan.py -u/--url http://example.com/ -m/--methods"`
  
 _Content size process (show response if the response size is ">[number]","<[number]","=[number]"):_
 
 - `python konan.py -u/--url http://example.com/ -C/--length "<1000"`
 
 ```
 URL: http://testphp.vulnweb.com/

PERCENT	 -   TIME   - CODE  -   METHOD  - LENGTH - URL
-------------------------------------------------------
0.19%    - 02:11:46 -  301  -	GET	-  184     - http://testphp.vulnweb.com/admin  -> http://testphp.vulnweb.com/admin/
1.73%    - 02:12:37 -  301  -	GET	-  184     - http://testphp.vulnweb.com/images  -> http://testphp.vulnweb.com/images/

 ```
