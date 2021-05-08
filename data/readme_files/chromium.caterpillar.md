# Caterpillar

Given the recent interest in [progressive web
apps](https://developers.google.com/web/progressive-web-apps/),
this experimental project investigates whether it is feasible to automatically port [Chrome Apps](https://developer.chrome.com/apps/about_apps) to web sites that run offline in Chrome and other modern browsers. 

## Installation

Extract the code into a folder. Install dependencies with pip and npm:

    $ pip install -r requirements.txt && npm install

## Usage

```bash
./caterpillar.py config -i config.json
./caterpillar.py convert -c config.json my-chrome-app/ my-web-app/
```

This will convert an unpackaged Chrome App `my-chrome-app/` into a progressive
web app `my-web-app/` and generate a conversion report inside a subdirectory of
`my-web-app/` (depending on the configuration options you set).

For more detailed documentation, see [the manual](docs/manual.md).

## Running Tests

Running all tests:

```bash
./run_tests.py
```

Running Python tests only:

```bash
./run_tests.py py
```

Running specific Python tests:

```bash
./run_tests.py py module_test
./run_tests.py py module_test.TestClass
./run_tests.py py module_test.TestClass.test_function
```

Running JavaScript tests only:

```bash
./run_tests.py js
```

The JavaScript tests assume you have Chrome and Firefox (version 45 or greater).
If you want to run the tests on different browsers, edit karma.conf.js.

## Disclaimer

This is not an official Google product (experimental or otherwise), it is just
code that happens to be owned by Google.

Copyright 2016 Google Inc. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

> <http://www.apache.org/licenses/LICENSE-2.0>

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
