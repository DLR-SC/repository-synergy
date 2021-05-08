# PythonScrapyBasicSetup
Basic setup with random user agents and proxy addresses for [Python Scrapy Framework](http://scrapy.org/).

### Setup
##### 1. Install Scrapy Framework

  ```
  pip install Scrapy
  ```
  [Detailed installation guide](https://doc.scrapy.org/en/1.3/intro/install.html)

##### 2. Install [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup) for proxy middleware based on proxydocker lists

  ```
  pip install beautifulsoup4
  ```
  [Detailed installation guide](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)
##### 3. Install [Tor](https://www.torproject.org/), [Stem](https://stem.torproject.org/) (controller library for Tor), and [Privoxy](https://www.privoxy.org/) (HTTP proxy server).

  ```
  apt-get install tor python-stem privoxy
  ```
  Hash a password with Tor:
  ```
  tor --hash-password secretPassword
  ```
  Then copy a hashed password and paste it with control port to ```/etc/tor/torrc```:
  ```
  ControlPort 9051
  HashedControlPassword 16:72C8ADB0E34F8DA1606BB154886604F708236C0D0A54557A07B00CAB73
  ```
  Restart Tor:
  ```
  sudo /etc/init.d/tor restart
  ```
  Enable Privoxy forwarding by adding next line to ```/etc/privoxy/config```:
  ```
  forward-socks5 / localhost:9050 .
  ```
  Restart Privoxy:
  ```
  sudo /etc/init.d/privoxy restart
  ```
  Both Tor and Privoxy should be up & running (check ```netstat -l```). If you used different password or control port, update ```settings.py```.

If you get some errors regarding the pyOpenSSL (check this [issue](https://github.com/scrapy/scrapy/issues/2473)), try to downgrade the Twisted engine:
  ```
  pip install Twisted==16.4.1
  ```

### Usage
To see what it does just:
  ```
  python run.py
  ```
Project contains three middleware classes in ```middlewares``` directory. ```ProxyMiddleware``` downloads IP proxy addresses and before every process request chooses one randomly. ```TorMiddleware``` has a similar purpose, but it relies on Tor network.  ```RandomUserAgentMiddleware``` downloads user agent strings and saves them into  ```'USER_AGENT_LIST'``` settings list. It also selects one UA randomly before every process request. Middlewares are activated in ```settings.py``` file.
This project also contains two spiders just for testing purposes, ```spiders/iptester.py``` and ```spiders/uatester.py```. You can run them individually:
```
scrapy crawl UAtester
scrapy crawl IPtester
```
```run.py``` file is a also good example how to include and run your spiders sequentially from one script.

If you have any questions or problems, feel free to create a new issue.
Scrap responsibly!
