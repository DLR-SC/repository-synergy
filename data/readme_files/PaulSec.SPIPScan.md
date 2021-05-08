SPIPScan
========

SPIP (CMS) Scanner for penetration testing purpose written in Python, and released under MIT License.

This tool has been designed to perform detection of SPIP installs during penetration testing. 
Currently, the tool detects the version of the SPIP install and tries to detect if the platform uses some of the top 30 plugins (listed on their website)



Prerequisites
========
These packages need to be installed in order to use SPIPScan:

 * Python
 * Beautiful Soup 4

Example on Ubuntu:

```bash
$ sudo apt-get install python python-bs4 python3-bs4
```



Usage
========

```python
$ python spipscan.py 
Usage: spipscan [options]

Options:
  -h, --help            show this help message and exit
  -w WEBSITE, --website=WEBSITE
                        Website to pentest (default: "http://localhost")
  -d PATH, --path=PATH  Path for webapp (default: "/")
  -t, --themes          Detect themes installed
  -p, --plugins         Detect plugins installed
  -s, --vulns           Detect possible vulns
  -V, --version         Detect version
  -f, --sensitive_folders
                        Detect sensitive folders
  -u, --users           Bruteforce user logins
  -T BRUTEFORCE_THEMES_FILE, --bruteforce_themes_file=BRUTEFORCE_THEMES_FILE
                        Bruteforce theme file (eg. themes_name.db)
  -P BRUTEFORCE_PLUGINS_FILE, --bruteforce_plugins_file=BRUTEFORCE_PLUGINS_FILE
                        Bruteforce plugin file (eg. plugins_name.db)
  -U BRUTEFORCE_LOGINS_FILE, --bruteforce_logins_file=BRUTEFORCE_LOGINS_FILE
                        Bruteforce login file (eg. user_logins.db)
  -S, --scan            Like -Vtps
  -F, --force           Force the scan if SPIP version is not detected
  -v, --verbose         Verbose mode
```

                        

Version detection
========
```
$ python spipscan.py --website=http://127.0.0.1 --version
```

Result : <br />
```
Application is located here : http://127.0.0.1/
[!] Version is : 3.0.13
[!] Plugin folder is : plugins-dist/
```



Plugins detection
========
```python
$ python spipscan.py --website=http://127.0.0.1 --plugins
```

Result <br />
```python
[!] Plugin folder is : plugins-dist/
[!] folder plugins-dist/ is accessible
[!] Plugin breves detected. Version : 1.3.5
[!] Plugin compagnon detected. Version : 1.4.1
[!] Plugin compresseur detected. Version : 1.8.6
[!] Plugin dump detected. Version : 1.6.7
[!] Plugin filtres_images detected. Version : 1.1.7
[!] Plugin forum detected. Version : 1.8.29
[!] Plugin jquery_ui detected. Version : 1.8.21
[!] Plugin mediabox detected. Version : 0.8.4
[!] Plugin medias detected. Version : 2.7.51
[!] Plugin mots detected. Version : 2.4.10
[!] Plugin msie_compat detected. Versoin : 1.2.0
[!] Plugin organiseur detected. Version : 0.8.10
[!] Plugin petitions detected. Version : 1.4.4
[!] Plugin porte_plume detected. Version : 1.12.4
[!] Plugin revisions detected. Version : 1.7.6
[!] Plugin safehtml detected. Version : 1.4.0
[!] Plugin sites detected. Version : 1.7.10
[!] Plugin squelettes_par_rubrique detected. Version : 1.1.1
[!] Plugin statistiques detected. Version : 0.4.19
[!] Plugin svp detected. Version : 0.80.18
[!] Plugin textwheel detected. Version : 0.8.17
[!] Plugin urls_etendues detected. Version : 1.4.15
[!] Plugin vertebres detected. Version : 1.2.2
```


The next example performs brute force to detect existing plugins :

```python
$ python spipscan.py --website=http://website.com --plugins --bruteforce_plugins=plugins_name.db
```



Plugins bruteforce
========
```python
$ python spipscan.py --website=http://127.0.0.1 --bruteforce_plugins=plugins_name.db
```

Result <br />
```python
Application is located here : http://127.0.0.1/
[!] Plugin folder is : plugins/
[-] Access forbidden on folder.
[-] Trying : http://127.0.0.1/plugins/cfg/plugin.xml
[-] Trying : http://127.0.0.1/plugins/cfg/paquet.xml
[-] Trying : http://127.0.0.1/plugins/spip-bonux-3/plugin.xml
[-] Trying : http://127.0.0.1/plugins/spip-bonux-3/paquet.xml
[-] Trying : http://127.0.0.1/plugins/couteau_suisse/plugin.xml
[-] Trying : http://127.0.0.1/plugins/couteau_suisse/paquet.xml
[-] Trying : http://127.0.0.1/plugins/couteau_suisse_191/plugin.xml
[-] Trying : http://127.0.0.1/plugins/couteau_suisse_191/paquet.xml
[-] Trying : http://127.0.0.1/plugins/saisies/plugin.xml
[-] Trying : http://127.0.0.1/plugins/saisies/paquet.xml
```



Themes detection
========
```python
$ python spipscan.py --website=http://127.0.0.1 --themes
```

Result : <br />
```python
Application is located here : http://127.0.0.1/
[-] We haven't been able to locate the themes folder
```



Themes bruteforce
========
```python
$ python spipscan.py --website=http://127.0.0.1 --bruteforce_themes=themes_name.db
```

Result : <br />
```python
Application is located here : http://127.0.0.1/
[!] Theme folder is : themes/
[-] Access forbidden on folder.
[-] Trying : http://127.0.0.1/themes/scolaspip_3_0/plugin.xml
[-] Trying : http://127.0.0.1/themes/scolaspip_3_0/paquet.xml
[-] Trying : http://127.0.0.1/themes/theme_einsteiniumist/plugin.xml
[-] Trying : http://127.0.0.1/themes/theme_einsteiniumist/paquet.xml
[-] Trying : http://127.0.0.1/themes/theme_brownie/plugin.xml
[-] Trying : http://127.0.0.1/themes/theme_brownie/paquet.xml
[-] Trying : http://127.0.0.1/themes/theme_brownie_v1/plugin.xml
[-] Trying : http://127.0.0.1/themes/theme_brownie_v1/paquet.xml
[-] Trying : http://127.0.0.1/themes/theme_darmstadtiumoid/plugin.xml
[-] Trying : http://127.0.0.1/themes/theme_darmstadtiumoid/paquet.xml
[-] Trying : http://127.0.0.1/themes/squelette_darmstadtiumoid/plugin.xml
[-] Trying : http://127.0.0.1/themes/squelette_darmstadtiumoid/paquet.xml
[-] Trying : http://127.0.0.1/themes/theme_brominerary/plugin.xml
[-] Trying : http://127.0.0.1/themes/theme_brominerary/paquet.xml
[-] Trying : http://127.0.0.1/themes/theme_tincredible/plugin.xml
[-] Trying : http://127.0.0.1/themes/theme_tincredible/paquet.xml
[-] Trying : http://127.0.0.1/themes/theme_maparaan/plugin.xml
[-] Trying : http://127.0.0.1/themes/theme_maparaan/paquet.xml
[-] Trying : http://127.0.0.1/themes/theme_initializr/plugin.xml
[-] Trying : http://127.0.0.1/themes/theme_initializr/paquet.xml
[-] Trying : http://127.0.0.1/themes/theme_ooCSS/plugin.xml
[-] Trying : http://127.0.0.1/themes/theme_ooCSS/paquet.xml
[-] Trying : http://127.0.0.1/themes/theme_californiumite/plugin.xml
```



Vulnerabilities identification
========
```python
$ python spipscan.py --website=http://127.0.0.1 --vulns
```

Result : <br />
```python
Application is located here : http://127.0.0.1/
[!] Version is : 2.1.12
[!] Plugin folder is : plugins/
[!] Potential Vulnerability : (versions : 2.0.21/2.1.16/3.0.3), SPIP connect Parameter PHP Injection, details : http://www.exploit-db.com/exploits/27941/
```



Sensitive folder identification
========
```python
$ python spipscan.py --website=http://127.0.0.1 --sensitive_folders --verbose
```

Result : <br />
```python
Application is located here : http://127.0.0.1/
[!] Directory listing on folder : IMG/
[!] Directory listing on folder : prive/
[!] Directory listing on folder : local/
[!] Directory listing on folder : config/
[!] Directory listing on folder : local/
```



Bruteforce login on SPIP (v. 2.0.X)
========
```python
$ python spipscan.py --website=http://127.0.0.1 --path=/spip/ --users --bruteforce_logins_file=user_logins.db --verbose
```

Result : <br />
```python
Application is located here : http://127.0.0.1/spip/
[!] Version (in Headers) is : 2.0.24
Accessing http://127.0.0.1/spip/spip.php?page=login
Form action args grabbed : 22S1TEIR6Ic7X9s41uTT+P8ntpRsNhjruYi5UZ5P8VMJ5VjfgqFrBeoa5+xz/roi9UtxAqw+j7bSTZiHHwjtj/kkOnzorNLXOneOGWXYIgNJI3uZdvq374q8NtT5nL7n56mO4+rJePWrUAhEXw==
[!] Login found : admin
[-] Tried login : administrator
[-] Tried login : test
[-] Tried login : guest
[-] Tried login : root
[-] Tried login : backup
```
