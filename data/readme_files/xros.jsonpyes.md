json-py-es
==========

[![Downloads](https://pepy.tech/badge/jsonpyes)](https://pepy.tech/project/jsonpyes)
[![Build Status](https://travis-ci.org/xros/jsonpyes.svg?branch=master)](https://travis-ci.org/xros/jsonpyes)
[![GitHub release](https://img.shields.io/github/release/xros/jsonpyes.svg)](https://github.com/xros/jsonpyes/releases)
[![GitHub license](https://img.shields.io/github/license/xros/jsonpyes.svg)](https://github.com/xros/jsonpyes/blob/master/LICENSE)

Alexander Liu

* To import raw JSON data files to ElasticSearch in one line of commands

![jsonpyes diagram](static/jsonpyes_data_processing_diagram.png)

Very fast -- 4 to 10 times faster when processing big data.


### Installation

```pip install jsonpyes```  

> **Notice**: Before using `pip` to install `jsonpyes`, firstly you need to install `python-pip` on your system. ( Supports Python2.7, 3,4, 3.5, 3.6 )


jsonpyes
--------

![user interface](https://raw.githubusercontent.com/xros/jsonpyes/master/static/snapshot236.png)

#### Instructions:
    There are 3 proccesses of importing raw JSON data to ElasticSearch
    1. Only validating raw JSON data
    2. Without validating ,just import data to ElasticSearch
    3. After validating successfully, then import data to ElasticSearch

    A valid JSON file here refers to a JSON file stacked with many lines of data
    
    file valid_data.json and its content

    {"key1": "valueA", "key2": {"sub_key1": "value2A", "sub_key2": ["Good", "Morning"]}}
    {"key1": "valueB", "key2": {"sub_key1": "value2B", "sub_key2": ["Good", "Afternoon"]}}
    ...
    {"key1": "valueC", "key2": {"sub_key1": "value2C", "sub_key2": ["Good", "Evening"]}}



Functions included
------------------

##### 1. Validating JSON format data

```jsonpyes --data raw_data.json --check```

If the json data file is valid: 

![json valid](https://raw.githubusercontent.com/xros/jsonpyes/master/static/snapshot98.jpg)

If the json data file is invalid: 

![json invalid](https://raw.githubusercontent.com/xros/jsonpyes/master/static/snapshot99.jpg)

##### 2. Only importing without validating

```jsonpyes --data raw_data.json --bulk http://localhost:9200 --import --index myindex2 --type mytype2```

Notice: If the raw JSON data file is invalid, `jsonpyes` will not import it.

Or enable multi-threads ```jsonpyes --data raw_data.json --bulk http://localhost:9200 --import --index myindex2 --type mytype2 --thread 8```

![no threads](https://raw.githubusercontent.com/xros/jsonpyes/master/static/snapshot102.jpg)

```jsonpyes``` supports multi-threads when importing data to elasticsearch


##### Multi-threads comparison

1. No multi-threads 

    ![benchmarks](https://raw.githubusercontent.com/xros/jsonpyes/master/static/snapshot237.png)

2. With 8 threads and `jsonpyes` cuts files into pieces, then destributes to workers fairly 

    ![use helpers.bulk API with multi-threads](https://raw.githubusercontent.com/xros/jsonpyes/master/static/snapshot235.png)

> As you can see these two containers have same docs loaded, if we use **_--thread 8_** it could be several times faster, usually 5 to 10 times faster.
> That really depends on your computer/server resources.
This was tested on a 4GB RAM / 2.4Ghz intel i5 Linux x64 laptop system.

And it works.

![it works](https://raw.githubusercontent.com/xros/jsonpyes/master/static/snapshot105.jpg)

##### 3. Both validating and importing

```jsonpyes --data raw_data.json --bulk http://localhost:9200 --import --index myindex1 --type mytype1 --check```

![validating and importing](https://raw.githubusercontent.com/xros/jsonpyes/master/static/snapshot135.png)

And it works.

![the results](https://raw.githubusercontent.com/xros/jsonpyes/master/static/snapshot101.jpg)


Reference
---------
* Algorithm handwritting

![handwritting](https://raw.githubusercontent.com/xros/jsonpyes/master/static/algo.png)

##### Happy hacking!
