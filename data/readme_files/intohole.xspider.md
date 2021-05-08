xspider 简单python抓取框架
============



xspider
----------------
+ 抓取单线程
+ 简单api使用
+ xpath/css/json提取器
+ 多种队列
+ 架构代码逻辑清晰，可以了解spider抓取过程
+ it's easy to crawl and extract web;

API
---------
+ [api文档](api.md)

```python
#coding=utf-8



from xspider.spider.spider import BaseSpider
from xspider.filters import UrlFilter 
from xspider.processor import PageProcessor
from xspider.selector import XPathSelector
from xspider.filters.CrawledFilter import SimpleCrawledFilter
from xspider import model
from b2 import system2
system2.reload_utf8()

class BuYiKr(PageProcessor.PageProcessor):


    def __init__(self):
        super(BuYiKr , self).__init__()
        self.title_extractor = XPathSelector.XpathSelector(path = "//title/text()")

    def process(self , page , spider):
        items = model.fileds.Fileds()
        items["title"] = self.title_extractor.find(page)
        items["url"] = page.url
        return items

if __name__ == "__main__":
    spider = BaseSpider(name = "buyikr",crawled_filter =  SimpleCrawledFilter(), page_processor = BuYiKr() , allow_site = ["buyiker.com"] , start_urls = ["http://buyiker.com/"])
    spider.start()
```         



抓取部分有以下工程代码
==========
+ [PhantomjsFetcher](https://github.com/2shou/PhantomjsFetcher)
+ [pyspider](https://github.com/binux/pyspider)
