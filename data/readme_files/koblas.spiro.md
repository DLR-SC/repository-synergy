spiro
=====

Tornado Web Crawler (Distributed)

I really just wanted a "simple" web crawlwer, something that could fetch ... say 100,000 pages without 
breaking a sweat and save them to some storage (MongoDB or Riak).  This is what I threw together.

Currently you are required to have MongoDB and Redis installed (the Riak store isn't complete).  MongoDB is used for 
both the settings portion of the UI and also for storing pages into after their crawled.

**Alpha** - This is a work in progress, the goal is to add functionality based on peoples real useage.
The core of the crawler - robots parsing, delays and other "friendly" factors should all work just fine.

Usage
-----

Looks like a Tornado app.

    ./main.py --debug --port=8000

Point your web browser at it.

Example map process on the crawled data (scan pages in MongoDB and do "something")

    python -m tools.map 

Basic Design
------------

Much of the design is inspired by these blog posts:

* [1] http://blog.semantics3.com/how-we-built-our-almost-distributed-web-crawler/
* [2] http://www.michaelnielsen.org/ddi/how-to-crawl-a-quarter-billion-webpages-in-40-hours/

MongoDB is used to store basic settings (crawler on, allowed domains, etc.etc.)  Most of the crawler
processing is managed via a Redis based Queue.  Which is sliced and locked based on domain name, once 
a specific instance has a queue it will crawl that as needed.

What I'm trying to avoid is where [1] uses Gearman to spawn jobs, is to allow Redis to really control
via locks what's happening and thus allow the Fetchers to be self sufficient.  If link finding is enabled
all links that are found are re-inserted into Redis to be crawlled at a later point, via a priority sorted 
list.

Other References
----------------

* http://dev.gbif.org/wiki/display/DEV/ZooKeeper+structure
* http://blog.marc-seeger.de/assets/papers/thesis_seeger-building_blocks_of_a_scalable_webcrawler.pdf

Techologies Used
----------------

* Tornado - Nonblocking Python Webserver - http://www.tornadoweb.org/
* Bootstrap - Pretty CSS - http://twitter.github.com/bootstrap/
* Backbone - JavaScript MVC - http://documentcloud.github.com/backbone/
* Distal - Backbone Views - https://github.com/koblas/distal
* MongoDB / Riak - KV NoSQL Database
* Highcharts - http://www.highcharts.com/products/highcharts
    - Note: Highsoft software products are not free for commercial use
