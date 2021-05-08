ChatExchange
============

[![Travis CI build status for master](https://travis-ci.org/Manishearth/ChatExchange.svg?branch=master)](https://travis-ci.org/Manishearth/ChatExchange)

A Python2 and Python3 cross-version API for talking to Stack Exchange chat.

 - Supported Python versions (Travis CI build run for each of these):  
    `2.7`, `3.4`, `3.5`, `3.6`, `3.7-dev`, `nightly` 
 - Unclear versions (not run on Travis CI as `pytest` does not support them):
    `2.6`, `3.2`, `3.3`

## Dependencies
**Make sure you use either `pip2` or `pip3` depending on which Python version you want to run this on.**


 - BeautifulSoup (`pip install beautifulsoup4`)
 - Requests (`pip install requests`). Usually there by default. Please upgrade it with `pip install requests --upgrade`  
   *Note that Ubuntu comes with an old version of `pip` that is not compatible any more with the latest version of `requests`. It will be broken after you installed `requests`, except if you update it before (or afterwards) with `easy_install pip` or `pip install --upgrade pip` (that one works only before).*
 - python-websockets for the experimental websocket listener (`pip install websocket-client`). This module is optional, without it `initSocket()` from SEChatBrowser will not work

## Shortcuts

1. `make install-dependencies` will install the necessary Python package dependencies into your current environment (active virtualenv or system site packages)
2. `make test` will run the tests
3. `make run-example` will run the example script
4. `make` will run the above three in order

## License

Licensed under either of

 * Apache License, Version 2.0, ([LICENSE-APACHE](LICENSE-APACHE) or http://www.apache.org/licenses/LICENSE-2.0)
 * MIT license ([LICENSE-MIT](LICENSE-MIT) or http://opensource.org/licenses/MIT)

at your option.

### Contribution

Unless you explicitly state otherwise, any contribution intentionally submitted
for inclusion in the work by you, as defined in the Apache-2.0 license, shall be dual licensed as above, without any
additional terms or conditions.
