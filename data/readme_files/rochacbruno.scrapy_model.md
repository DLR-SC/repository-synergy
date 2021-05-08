Create scraper using Scrapy Selectors
============================================

> NOTE: Please consider using this another project https://github.com/ssteuteville/scrapyz better maintained and documented. But if you still find scrapy_model useful welcome!

[![Build
Status](https://travis-ci.org/rochacbruno/scrapy_model.png)](https://travis-ci.org/rochacbruno/scrapy_model)

[![PyPi version](https://img.shields.io/pypi/v/scrapy_model.svg)](https://pypi.python.org/pypi/scrapy_model/)
[![PyPi downloads](https://img.shields.io/pypi/dm/scrapy_model.svg)](https://pypi.python.org/pypi/scrapy_model/)


## What is Scrapy?

Scrapy is a fast high-level screen scraping and web crawling framework, used to crawl websites and extract structured data from their pages. It can be used for a wide range of purposes, from data mining to monitoring and automated testing.

http://scrapy.org/


## What is scrapy_model ?

It is just a helper to create scrapers using the Scrapy Selectors allowing you to select elements by CSS or by XPATH and structuring your scraper via Models (just like an ORM model) and plugable to an ORM model via ``populate`` method.

Import the BaseFetcherModel, CSSField or XPathField (you can use both)

```python
from scrapy_model import BaseFetcherModel, CSSField
```

Go to a webpage you want to scrap and use chrome dev tools or firebug to figure out the css paths then considering you want to get the following fragment from some page.

```html
    <span id="person">Bruno Rocha <a href="http://brunorocha.org">website</a></span>
```

```python
class MyFetcher(BaseFetcherModel):
    name = CSSField('span#person')
    website = CSSField('span#person a')
    # XPathField('//xpath_selector_here')
```

Fields can receive ``auto_extract=True`` parameter which auto extracts values from selector before calling the parse or processors. Also you can pass the ``takes_first=True`` which will for auto_extract and also tries to get the first element of the result, because scrapy selectors returns a list of matched elements.


### Multiple queries in a single field

You can use multiple queries for a single field

```python
name = XPathField(
    ['//*[@id="8"]/div[2]/div/div[2]/div[2]/ul',
     '//*[@id="8"]/div[2]/div/div[3]/div[2]/ul']
)
```

In that case, the parsing will try to fetch by the first query and returns if finds a match, else it will try the subsequent queries until it finds something, or it will return an empty selector.

#### Finding the best match by a query validator

If you want to run multiple queries and also validates the best match you can pass a validator function which will take the scrapy selector an should return a boolean.

Example, imagine you get the "name" field defined above and you want to validates each query to ensure it has a 'li' with a text "Schblaums" in there.

```python

def has_schblaums(selector):
    for li in selector.css('li'): # takes each <li> inside the ul selector
        li_text = li.css('::text').extract() # Extract only the text
        if "Schblaums" in li_text:  # check if "Schblaums" is there
            return True  # this selector is valid!
    return False  # invalid query, take the next or default value

class Fetcher(....):
    name = XPathField(
        ['//*[@id="8"]/div[2]/div/div[2]/div[2]/ul',
         '//*[@id="8"]/div[2]/div/div[3]/div[2]/ul'],
        query_validator=has_schblaums,
        default="undefined_name"  # optional
    )
```

In the above example if both queries are invalid, the "name" field will be filled with an empty_selector, or the value defined in "default" parameter.

> **NOTE:** if the field has a "default" and fails in all the matcher, the default value will be passed to "processor" and also to "parse_" methods.

Every method named ``parse_<field>`` will run after all the fields are fetched for each field.

```python
    def parse_name(self, selector):
        # here selector is the scrapy selector for 'span#person'
        name = selector.css('::text').extract()
        return name

    def parse_website(self, selector):
        # here selector is the scrapy selector for 'span#person a'
        website_url = selector.css('::attr(href)').extract()
        return website_url

```


after defined need to run the scraper


```python

fetcher = Myfetcher(url='http://.....')  # optionally you can use cached_fetch=True to cache requests on redis
fetcher.parse()
```

Now you can iterate ``_data``, ``_raw_data`` and atributes in fetcher

```python
>>> fetcher.name
<CSSField - name - Bruno Rocha>
>>> fetcher.name.value
Bruno Rocha
>>> fetcher._data
{"name": "Bruno Rocha", "website": "http://brunorocha.org"}
```

You can populate some object

```python
>>> obj = MyObject()
>>> fetcher.populate(obj)  # fields optional

>>> obj.name
Bruno Rocha
```

If you do not want to define each field explicitly in the class, you can use a json file to automate the process

```python
class MyFetcher(BaseFetcherModel):
   """ will load from json """

fetcher = MyFetcher(url='http://.....')
fetcher.load_mappings_from_file('path/to/file.json')
fetcher.parse()
```

In that case file.json should be

```json
{
   "name": {"css", "span#person"},
   "website": {"css": "span#person a"}
}
```

You can use ``{"xpath": "..."}`` in case you prefer select by xpath


### parse and processor

There are 2 ways of transforming or normalizing the data for each field

#### Processors

A processor is a function, or a list of functions which will be called in the given sequence against the field value, it receives the raw_selector or the value depending on auto_extract and takes_first arguments.

It can be used for Normalization, Clean, Transformation etc..

Example:

```python

def normalize_state(state_name):
    # query my database and return the first instance of state object
    return MyDatabase.State.Search(name=state_name).first()

def text_cleanup(state_name):
    return state_name.strip().replace('-', '').lower()

class MyFetcher(BaseFetcherModel):
    state = CSSField(
        "#state::text",
        takes_first=True,
        processor=[text_cleanup, normalize_state]
    )

fetcher = MyFetcher(url="http://....")
fetcher.parse()

fetcher._raw_data.state
'Sao-Paulo'
fetcher._data.state
<ORM Instance - State - São Paulo>
```

#### Parse methods

any method called ``parse_<field_name>`` will run after all the process of selecting and parsing, it receives the selector or the value depending on auto_extract and takes_first argument in that field.

example:

```python
def parse_name(self, selector):
   return selector.css('::text').extract()[0].upper()
```

In the above case, the name field returns the raw_selector and in the parse method we can build extra queries using ``css`` or ``xpath`` and also we need to extract() the values from the selector and optionally select the first element and apply any transformation we need.

### Caching the html fetch

In order to cache the html returned by the url fetching for future parsing and tests you specify a cache model, by default there is no cache but you can use the built in RedisCache passing

```python
    from scrapy_model import RedisCache
    fetcher = TestFetcher(cache_fetch=True,
                          cache=RedisCache,
                          cache_expire=1800)
```

or specifying arguments to the Redis client.

> it is a general Redis connection from python ``redis`` module

```python
    fetcher = TestFetcher(cache_fetch=True,
                          cache=RedisCache("192.168.0.12:9200"),
                          cache_expire=1800)
```

You can create your own caching structure, e.g: to cache htmls in memcached or s3

the cache class just need to implement ``get`` and ``set`` methods.

```python
from boto import connect_s3

class S3Cache(object):
    def __init__(self, *args, **kwargs):
        connection = connect_s3(ACCESS_KEY, SECRET_KEY)
        self.bucket = connection.get_bucket(BUCKET_ID)

    def get(self, key):
        value = self.bucket.get_key(key)
        return value.get_contents_as_string() if key else None

    def set(self, key, value, expire=None):
        self.bucket.set_contents(key, value, expire=expire)


fetcher = MyFetcher(url="http://...",
                    cache_fetch=True,
                    cache=S3cache,
                    cache_expire=1800)

```

### Instalation

easy to install

If running ubuntu maybe you need to run:

```bash
sudo apt-get install python-scrapy
sudo apt-get install libffi-dev
sudo apt-get install python-dev
```

then

```bash
pip install scrapy_model
```

or


```bash
git clone https://github.com/rochacbruno/scrapy_model
cd scrapy_model
pip install -r requirements.txt
python setup.py install
python example.py
```

Example code to fetch the url http://en.m.wikipedia.org/wiki/Guido_van_Rossum

```python
#coding: utf-8

from scrapy_model import BaseFetcherModel, CSSField, XPathField


class TestFetcher(BaseFetcherModel):
    photo_url = XPathField('//*[@id="content"]/div[1]/table/tr[2]/td/a')

    nationality = CSSField(
        '#content > div:nth-child(1) > table > tr:nth-child(4) > td > a',
    )

    links = CSSField(
        '#content > div:nth-child(11) > ul > li > a.external::attr(href)',
        auto_extract=True
    )

    def parse_photo_url(self, selector):
        return "http://en.m.wikipedia.org/{}".format(
            selector.xpath("@href").extract()[0]
        )

    def parse_nationality(self, selector):
        return selector.css("::text").extract()[0]

    def parse_name(self, selector):
        return selector.extract()[0]

    def pre_parse(self, selector=None):
        # this method is executed before the parsing
        # you can override it, take a look at the doc string

    def post_parse(self):
        # executed after all parsers
        # you can load any data on to self._data
        # access self._data and self._fields for current data
        # self.selector contains original page
        # self.fetch() returns original html
        self._data.url = self.url


class DummyModel(object):
    """
    For tests only, it can be a model in your database ORM
    """


if __name__ == "__main__":
    from pprint import pprint

    fetcher = TestFetcher(cache_fetch=True)
    fetcher.url = "http://en.m.wikipedia.org/wiki/Guido_van_Rossum"

    # Mappings can be loaded from a json file
    # fetcher.load_mappings_from_file('path/to/file')
    fetcher.mappings['name'] = {
        "css": ("#section_0::text")
    }

    fetcher.parse()

    print "Fetcher holds the data"
    print fetcher._data.name
    print fetcher._data

    # How to populate an object
    print "Populating an object"
    dummy = DummyModel()

    fetcher.populate(dummy, fields=["name", "nationality"])
    # fields attr is optional
    print dummy.nationality
    pprint(dummy.__dict__)

```

# outputs


```
Fetcher holds the data
Guido van Rossum
{'links': [u'http://www.python.org/~guido/',
           u'http://neopythonic.blogspot.com/',
           u'http://www.artima.com/weblogs/index.jsp?blogger=guido',
           u'http://python-history.blogspot.com/',
           u'http://www.python.org/doc/essays/cp4e.html',
           u'http://www.twit.tv/floss11',
           u'http://www.computerworld.com.au/index.php/id;66665771',
           u'http://www.stanford.edu/class/ee380/Abstracts/081105.html',
           u'http://stanford-online.stanford.edu/courses/ee380/081105-ee380-300.asx'],
 'name': u'Guido van Rossum',
 'nationality': u'Dutch',
 'photo_url': 'http://en.m.wikipedia.org//wiki/File:Guido_van_Rossum_OSCON_2006.jpg',
 'url': 'http://en.m.wikipedia.org/wiki/Guido_van_Rossum'}
Populating an object
Dutch
{'name': u'Guido van Rossum', 'nationality': u'Dutch'}
```
