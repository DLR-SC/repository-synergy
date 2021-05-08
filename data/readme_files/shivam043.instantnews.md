# instantnews
## Get news instantly! :notes: :newspaper: 
### Released v1.2.3
[![PyPI](https://img.shields.io/badge/instantnews-downloads-brightgreen.svg)](https://pypi.python.org/pypi?:action=display&name=instantnews&version=1.2.1)
[![Gitter](https://img.shields.io/gitter/room/nwjs/nw.js.svg)](https://gitter.im/instantnews/Lobby)

Install
=====

An API key from [newsapi](http://newsapi.org/) will be required and you can register for one [here](http://newsapi.com/register).

### Using `pip`

```bash
$ pip install instantnews
```
### Using `pip` upgrade

```bash
$ pip install instantnews --upgrade
```

Set your API key in an environment variable `IN_API_KEY`

For example:

```bash
export IN_API_KEY="<YOUR_API_TOKEN>"
```

### Build from source

```bash
$ git clone https://github.com/shivam043/instantnews.git
$ cd instantnew
$ python setup.py install
```
#### Note:
Python 2.7 and Python 3 compatible

Usage
====

### Get help

```bash
$ instantnews -h/--help  #Get Help
usage: instantnews [-h] [--show SHOW] [--show_all] [--news NEWS]

optional arguments:
  -h, --help            show this help message and exit
  --show SHOW, -s SHOW  Shows all the news channel codes category wise
  --show_all, -sa       Shows all the news channel codes
  --news NEWS, -n NEWS  Shows news
```

### Get news-code category-wise/all
```bash

$ instantnews -sa/--show_all
forexample:
instantnews --show_all
News Code: <abc-news-au> ABC News (AU)
News Code: <al-jazeera-english> Al Jazeera English
News Code: <ars-technica> Ars Technica
News Code: <associated-press> Associated Press
News Code: <bbc-news> BBC News
News Code: <bbc-sport> BBC Sport
News Code: <bild> Bild
News Code: <bloomberg> Bloomberg
News Code: <breitbart-news> Breitbart News .....

$ instantnews -s/--show business
forexample:
instantnews --show business  # Categories available-'business','entertainment','gaming','general','music','politics','science-and-nature','sport','technology'
News Code: <bloomberg> Bloomberg
News Code: <business-insider> Business Insider
News Code: <business-insider-uk> Business Insider (UK)
News Code: <cnbc> CNBC
News Code: <die-zeit> Die Zeit
News Code: <financial-times> Financial Times
News Code: <fortune> Fortune
News Code: <handelsblatt> Handelsblatt

```
### Get news 
```bash
$ instantnews -n/--news  [news-id]
forexample:
instantnews --news bbc-news
[0] Title: Trump denies NFL kneel row race-related
Author: BBC News
Summary: Donald Trump says his words about political protests at sport events had "nothing to do with race".
--------------------------------------------
[1] Title: Germany's AfD to fight 'foreign invasion'
Author: BBC News
Summary: Nationalists lay out their plans after winning nearly 13% of the vote, weakening Chancellor Merkel.
--------------------------------------------
........
Want to see the news that interests you/open in a webpage? Enter Y/N # See news in a webpage by enter the number present in the box
```


License
====
Open sourced under [MIT License](LICENSE)
