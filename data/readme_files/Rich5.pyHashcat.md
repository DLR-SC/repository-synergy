# pyhashcat

## This project is no longer under development. If you're interested in actively maintaining a fork let me know and I'll include a link here ##

Active Forks:
* https://github.com/f0cker/pyhashcat

Python bindings for hashcat
------

pyhashcat has been completely rewritten as a Python C extension to interface directly with libhashcat. The pyhashcat module now acts as direct bindings to hashcat.

VERSION: 2.0b2 


Requirements: 
* libhashcat
* Python 2.7

### Install libhashcat and pyhashcat:

```
git clone https://github.com/Rich5/pyHashcat.git
cd pyhashcat/pyhashcat
git clone https://github.com/hashcat/hashcat.git
cd hashcat/
git submodule init
git submodule update
sudo make install_library
sudo make install
cd ..
python setup.py build_ext -R /usr/local/lib
sudo python setup.py install
```

### Simple Test:

```
user@host:~/pyHashcat/pyhashcat$ python simple_mask.py
-------------------------------
---- Simple pyhashcat Test ----
-------------------------------
[+] Running hashcat
STATUS:  Cracked
8743b52063cd84097a65d1633f5c74f5  -->  hashcat
```

### Help:

```
import pyhashcat
help(pyhashcat)
```
