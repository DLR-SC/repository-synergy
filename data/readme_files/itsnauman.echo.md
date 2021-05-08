echo
====
[![Build Status](https://travis-ci.org/itsnauman/echo.svg?branch=master)](https://travis-ci.org/itsnauman/echo)

A micro library for retrying failing operations inspired by [retry](https://github.com/igorw/retry). It's just as simple as decorating the function. It will retry `n` number of times and then raise a `FailingTooHard` exception if it doesn't succeed.
```python
import requests
from pyecho import echo

@echo(10) # Retry function upto 10 times
def fetch():
	r = requests.get('http://google.com')
	return r.text

fetch()
```
## Installation
echo can be installed using Pypi, `pip install pyecho`

## License
`echo` is distributed under MIT license, see `LICENSE` for more details.
