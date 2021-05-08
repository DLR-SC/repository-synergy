# Tracking the trackers. Draw connections between scripts and domains on website.

## Description
Kupa3 allows you to draw connections between scripts on specific website. It search for javascript code or source attribute, in html code, and crawls it in order to draw a dependency graph. This approach can help bug hunters to discover subdomains and examine javascript calls, OSINT researchers to check what companies are connected to each other or for tracking advertisement companies. At the end, graph is saved in gexf format for exploring it in Gephi.

Background: https://medium.com/@woj_ciech/tracking-the-trackers-draw-connections-between-scripts-and-domains-on-website-360bc6a306df

## Requirements
- Python 3
- BeautifulSoup
- NetworkX
- Matplotlib

```
pip3 install -r requirements.txt
```


## Usage
```
root@kali:~# python kupa3.py -h

           (                 ,&&&.
            )                .,.&&
           (  (              \=__/
               )             ,'-'.
         (    (  ,,      _.__|/ /|
          ) /\ -((------((_|___/ |
        (  // | (`'      ((  `'--|
      _ -.;_/ \--._      \ \-._/.
     (_;-// | \ \-'.\    <_,\_\`--'|
     ( `.__ _  ___,')      <_,-'__,'
jrei  `'(_ )_)(_)_)' asciiart.eu

Tracking the trackers. Draw connections between scripts and domains on website.
medium.com/@woj_ciech github.com/woj-ciech
example: python3 kupa3.py https://nsa.gov

usage: kupa3.py [-h] [--url URL]

optional arguments:
  -h, --help  show this help message and exit
  --url URL   URL of website (default: https://nsa.gov)
```

## Output
![Reddit.com](https://i.imgur.com/WcQKMKa.png "Graph for reddit.com")
