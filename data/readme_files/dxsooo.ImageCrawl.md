# ImageCrawl

## Overview
Based on [Scrapy](https://github.com/scrapy/scrapy), ImageCrawl is a web image crawler that outputs images' origin url and downloads images automatically.  
Recently supports:  

* [Flickr](https://www.flickr.com/)  
* [Instagram](https://instagram.com/)
* [Google Image Search](https://www.google.com/imghp)
* [Bing Image Search](https://www.bing.com/images)

## Requirements  
* Python 2.7
* [Scrapy](http://scrapy.org/)
* GoAgent (if you are working in China mainland and disconnecting with the target websites )

## Documentation
You can go to the top level directory of this project and run:  

    scrapy crawl [spider name]

In this project, the spider name can be `Flickr`, `Instagram`, `GoogleSearch`,`BingSearch`(no brackets). But you need to edit the file `ImageCrawl/spiders/xxx_spider.py` before you run the command above.  

---
For ***Flickr***, you should have your own `api_key` (see [here](https://www.flickr.com/services/apps/create/apply/)), and decide your search tag. If you want to change other params, look at the file carefully or get help from [Flickr API](https://www.flickr.com/services/api/). 
```python
class FlickrSpider(scrapy.Spider):
    name = "Flickr"
    tag='your tag'
    api_key='your api_key'
```  
---
For ***Instagram***, you should have your own `access_token` (see [here](http://jelled.com/instagram/access-token)), and decide your search tag. If you want to change other params, look at the file carefully or get help from [Instagram API](https://instagram.com/developer/). 
```python
class InstagramSpider(scrapy.Spider):
    name = "Instagram"
    tag='your tag'
    params = {
        'access_token': 'your access_token',
    }
```
---
For ***Google Image Search***, you should decide your search key word. If you want to change other params, look at the file carefully or get help from [Google Image API](https://developers.google.com/image-search/v1/jsondevguide). 
```python
class GoogleSearchSpider(scrapy.Spider):
    name = "GoogleSearch"
    key_word='your key_word'
```
---
For ***Bing Image Search***, you should have your own `account Key` (see [here](https://datamarket.azure.com/dataset/bing/search)), and decide your search key word. If you want to change other params, look at the file carefully or get help from [Bing search API](http://go.microsoft.com/fwlink/?LinkID=272625&clcid=0x409). 
```python
class BingSearchSpider(scrapy.Spider):
    name = "BingSearch"
    key_word='your key_word'
    acctKey = 'your account Key'
```
You will get a `csv` folder that stores the crawl result(named with the beginning time of the program) and the images would be downloaded to folder `data` when the program finished.  
If you want to change the image download directory, edit the last line in file `ImageCrawl/settings.py`:  
```python
IMAGES_STORE = 'data'
```
**Note** the program works with GoAgent by default, please ensure your GoAgent pre-opened and works well, change or disable GoAgent, see [this](http://snipplr.com/view/74665/using-goagent-agent-in-scrapy/).