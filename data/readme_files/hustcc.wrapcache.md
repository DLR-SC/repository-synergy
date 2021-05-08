# wrapcache

A python Function / Method OUTPUT cache system base on function Decorators. Supports to cache into `redis` or `LRU` memory. [中文README.md](README_zh.md)

[![Build Status](https://travis-ci.org/hustcc/wrapcache.svg)](https://travis-ci.org/hustcc/wrapcache) [![codecov Status](https://codecov.io/github/hustcc/wrapcache/coverage.svg?branch=master)](https://codecov.io/github/hustcc/wrapcache?branch=master) [![PyPi Status](https://img.shields.io/pypi/v/wrapcache.svg)](https://pypi.python.org/pypi/wrapcache) [![Python Versions](https://img.shields.io/pypi/pyversions/wrapcache.svg)](https://pypi.python.org/pypi/wrapcache) [![PyPi Downloads](https://img.shields.io/pypi/dm/wrapcache.svg)](https://pypi.python.org/pypi/wrapcache)

> [Homepage](http://git.atool.org/wrapcache/) | [Usage & Doc](http://git.atool.org/wrapcache/) | [Source Code](https://github.com/hustcc/wrapcache) | [Issue & Bug](https://github.com/hustcc/wrapcache/issues/new)


## What's wrapcache?

`wrapcache` is a decorator that enables caching of return values for functions.

The cache keys are dependent completely on the arguments passed to the function. very simple to use. 

Also has some `API` to `Programmatic` get cache or remove cache. `Support python 2.6 ~ python3.5`.

Here's an example of how you might use wrapcache:

```python

import wrapcache

from time import sleep
import random

@wrapcache.wrapcache(timeout = 3)
def need_cache_function(input, t = 2, o = 3):
    sleep(2)
    return random.randint(1, 100)

if __name__ == "__main__":
	for i in range(10):
		sleep(1)
		print(need_cache_function(1, t = 2, o = 3))
	
	#get cache Programmatic
	key_func = wrapcache.keyof(need_cache_function, 1, o = 3, t = 2)
	print(wrapcache.get(key_func))
	#remove cache Programmatic
	print(wrapcache.remove(wrapcache.keyof(need_cache_function, 1, o = 3, t = 2)))

```

Some config:

```python
@wrapcache.wrapcache(timeout = timeout, adapter = adapter)
```

 - **`timeout`**: how much seconds the cache exist. Default is `-1`, not cached.
 - **`adapter`**: cache where, now can be `RedisAdapter` and `MemoryAdapter`. Default is `MemoryAdapter`. 

 
When use `RedisAdapter`, you need to set redis instance before use. e.g.

```python
REDIS_POOL = redis.ConnectionPool(host = '10.246.13.1', port = 6379, password = 'redis_pwd', db = 1)
REDIS_INST = redis.Redis(connection_pool = REDIS_POOL, charset = 'utf8')
RedisAdapter.db = REDIS_INST
```

When use `MemoryAdapter`, you can set `Memory Storage Policy` before use, that is choose where to store. Default is store in `{}`, also it provide `LUR`(Supported by [jlhutch/pylru](https://github.com/jlhutch/pylru), add `dynamic` size.) algorithm. e.g.


```python
from wrapcache.database import LruCacheDB
lruDB = MemoryAdapter.db = LruCacheDB(size = 100)
RedisAdapter.db = lruDB
```

## How to Install and Use?

### Install

Three ways to install wrapcache: 

#### 1. Use tool install

 - `pip install wrapcache`

#### 2. Download to install

 - Download from [https://pypi.python.org/pypi/wrapcache/](https://pypi.python.org/pypi/wrapcache/), and run `python setup.py install`.

#### 3. Manual installation

 - Manual installation: Put `wrapcache` folder into current directory or `site-packages`, then `import wrapcache` to use.


### Usage

#### Decorators

```python

import wrapcache
@wrapcache.wrapcache(timeout = 3)
def need_cache_function():
	return 'hello wrapcache'

```

#### API

1. **`wrapcache.keyof(func, *args, **kws)`**: get the key of function output cache.
2. **`wrapcache.get(key, adapter = MemoryAdapter)`**: get the value of cache.
3. **`wrapcache.set(key, value, timeout = -1, adapter = MemoryAdapter)`**: set cache use code.
4. **`wrapcache.remove(key, adapter = MemoryAdapter)`**: remove a cache.
5. **`wrapcache.flush(adapter = MemoryAdapter)`**: clear all the cache.

The API 2~5, need to input a `adapter` to set which db to operate.


## TODO

 - usage wiki.