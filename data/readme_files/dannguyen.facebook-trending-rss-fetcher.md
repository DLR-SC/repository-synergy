# Facebook Trending RSS Feed Fetcher

A quickie Python 3.5 script that parses the [PDF-listing of RSS feeds](data/rss-urls.pdf) that Facebook uses to monitor for breaking news stories to add to its Trending Section.

# Background

On May 12, 2016, Gizmodo published an article titled, [Facebook Admits Its Trending Section Includes Topics Not Actually Trending on Facebook](http://gizmodo.com/facebook-admits-its-trending-section-includes-topics-no-1776319308), which covered the fallout from Gizmodo's previous reporting that [Facebook's Trending Section is mostly human-curated](http://gizmodo.com/former-facebook-workers-we-routinely-suppressed-conser-1775461006). As part of its response, Facebook released a list of 1,000 RSS feeds ([as a PDF file](https://fbnewsroomus.files.wordpress.com/2016/05/rss-urls.pdf)) that it says it uses to crawl for interesting news stories that may not have yet percolated through its social shares.

This repo contains code (and the results) to convert that PDF list into a machine-readable CSV ([data/rss-urls.csv](data/rss-urls.csv)) and then to fetch each RSS URL. A few of the URLs 404, but programmers who know how to parse XML can make use of the [retrieved data](data/feeds/) to do their own content analysis.

Note: There appears to be only __929__ lines in Facebook's list of RSS feeds, according to `wc -l data/rss-urls.csv`, not "1,000". And when counting uniques --

~~~sh
csvcut -c3 data/rss-urls.csv | sort | uniq | wc -l
~~~

The result is __888__ lines. 

Each URL is given a country and category. Here's the group count of those fields:

| count | country |     topic     |
|-------|---------|---------------|
|    11 | AU      | business      |
|    10 | AU      | entertainment |
|    20 | AU      | general       |
|    10 | AU      | health        |
|    13 | AU      | politics      |
|     7 | AU      | science       |
|    11 | AU      | sports        |
|     7 | AU      | tech          |
|    20 | CA      | business      |
|    35 | CA      | entertainment |
|     5 | CA      | gaming        |
|    30 | CA      | general       |
|    19 | CA      | health        |
|    15 | CA      | politics      |
|    13 | CA      | science       |
|    18 | CA      | sports        |
|    16 | CA      | tech          |
|    17 | GB      | business      |
|    39 | GB      | entertainment |
|     5 | GB      | gaming        |
|    25 | GB      | general       |
|    18 | GB      | health        |
|    21 | GB      | politics      |
|    13 | GB      | science       |
|    17 | GB      | sports        |
|    11 | GB      | tech          |
|    27 | IN      | business      |
|    21 | IN      | entertainment |
|     1 | IN      | gaming        |
|    33 | IN      | general       |
|    12 | IN      | health        |
|    29 | IN      | politics      |
|    10 | IN      | science       |
|    19 | IN      | sports        |
|    13 | IN      | tech          |
|    17 | US      | business      |
|    35 | US      | entertainment |
|    30 | US      | gaming        |
|    39 | US      | general       |
|    41 | US      | health        |
|    47 | US      | politics      |
|    48 | US      | science       |
|    14 | US      | sports        |
|    66 | US      | tech          |






# About the collected data

The [data/feeds/](data/feeds/) folder already includes results from a fetch on __2016-05-12__, read the [directions further below](#mark-own-fetch) if you want to run it from scratch. The [data/feeds/](data/feeds/) contains JSON files that include the __metadata__ when requesting a given RSS URL. If successful, the serialized JSON object contains the raw, unparsed XML in a field named `response_text` (i.e. I haven't extracted the individual news items from each valid RSS feed).

Here's an example of how http://deadline.com/feed (saved as: [data/deadline.com---feed.json](data/feeds/deadline.com---feed.json)) is serialized:

~~~json
{
  "requested_url": "http://deadline.com/feed/",
  "fetched_at": "2016-05-12T23:35:52.197688",
  "status_code": 200,
  "response_text": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><rss version=\"2.0\"\n\txmlns:content=\"http://purl.org/rss/1.0/modules/content/\"\n\txmlns:wfw=\"http://wellformedweb.org/CommentAPI/\"\n\txmlns:dc=\"http://purl.org/dc/elements/1.1/\"\n...</channel>\n</rss>\n",
  "headers": {
    "Date": "Fri, 13 May 2016 06:33:29 GMT",
    "Vary": "Accept-Encoding, Accept-Encoding",
    "Last-Modified": "Fri, 13 May 2016 06:30:23 GMT",
    "Content-Type": "application/rss+xml; charset=UTF-8",
    "Server": "nginx",
    "X-nc": "HIT bur 209",
    "X-UA-Compatible": "IE=Edge",
    "X-hacker": "If you're reading this, you should visit automattic.com/jobs and apply to join the fun, mention this header.",
    "Connection": "keep-alive",
    "Content-Encoding": "gzip",
    "X-ac": "4.sjc _bur",
    "Transfer-Encoding": "chunked"
  },
  "response_url": "http://deadline.com/feed/"
}
~~~


If you are looking to deserialize the XML, here's one way to do it (using the [xmltodict](https://github.com/martinblech/xmltodict) lib):

~~~py
import json
import xmltodict
jdata = json.load(open('data/feeds/deadline.com_feed.json'))
feed = xmltodict.parse(jdata['response_text'])
print(feed['rss']['channel']['title'])
# Deadline
items = feed['rss']['channel']['item']
len(items)
# 12
print(items[4]['title']) 
# The CW Looking To Redevelop Kevin Williamson Paranormal Drama
print(items[4]['link'])
# http://deadline.com/2016/05/kevin-williamson-paranormal-drama-pilot-redeveloped-the-cw-1201755022/
~~~

RSS feeds have different formats...which is why I haven't taken the time to write a deserializer myself, but I'm sure someone more familiar with RSS can do it easily.



<a id="mark-own-fetch"></a>

# Doing your own fetch

My scripts have some exotic dependencies even though they do little more than just fetch URLs:

- Python 3.5 (and its new standard library modules such as [pathlib](https://docs.python.org/3/library/pathlib.html))
- The [deco library](https://github.com/alex-sherman/deco) -- which has _just_ been updated to 3.5 -- for easy concurrency. You can remove the `@concurrent` and `@synchronized` decorators if you don't want the fuss. I had to install the egg straight from Github:

          pip install -e git+https://github.com/alex-sherman/deco.git#egg=deco

- The [scripts/fetch_pdf.py](scripts/fetch_pdf.py) script requires [Poppler](https://poppler.freedesktop.org/) to run pdftotext via the shell.



### Fetching and parsing the PDF of URLs


To re-fetch [Facebook's PDF](https://fbnewsroomus.files.wordpress.com/2016/05/rss-urls.pdf) and re-parse it into [data/rss-urls.csv](data/rss-urls.csv):

~~~sh
$ python scripts/fetch_pdf.py 
~~~


### Fetching each feed URL and serializing the response

The following script will run through each entry in [data/rss-urls.csv](data/rss-urls.csv) to fetch each RSS URL and save the response to a corresponding JSON file in [data/feeds/](data/feeds/):

~~~sh
$ python scripts/fetch_feeds.py 
~~~

The JSON file for each fetch attempt includes metadata -- such as the headers, HTTP status code, and datetime of the request -- as well as a `response_text` that contains the raw text of the server response. The HTTP request will automatically follow redirects, so everything is either a `200` or some kind of error code. However, there is a `requested_url` -- which corresponds to the URL that came from Facebook's original document -- and a `response_url`, which can be used to compare against `requested_url` to see if a redirect occurred. This is a hacky way to deal with some redirects not pointing to actual RSS resources, e.g [http://www.nationaljournal.com/?rss=1](http://www.nationaljournal.com/?rss=1).


## Metrics

There's a [scripts/metrics.py](scripts/metrics.py) that simply counts up the metadata:

~~~
Status code metrics:
792: 200
 44: 404
 23: ConnectionError
 20: 403
  3: 400
  1: 502
  1: InvalidSchema
  1: 500
  1: 429

Of the 792 requests that were successful, 109 were likely redirects
~~~
