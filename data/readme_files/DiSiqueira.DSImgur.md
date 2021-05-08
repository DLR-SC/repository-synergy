# DSImgur ![Language Badge](https://img.shields.io/badge/Language-Python-red.svg) ![License Badge](https://img.shields.io/badge/License-MIT-blue.svg) ![Status Badge](https://img.shields.io/badge/Status-Stable-brightgreen.svg)

Easily download images, Albums, Galleries and entire Profiles from Imgur. The most powerful Imgur Downloader!! You can use as program or as module!

![](https://i.imgur.com/Sh2TKvy.gif)

## Features

- Download Single Images ex.: https://imgur.com/EJtc5ox or http://i.imgur.com/EJtc5ox.jpg
- Download Entire Albums ex.: https://imgur.com/a/iwWZm 
- Download Entire Galleries ex.: https://imgur.com/gallery/3ttnIn2
- Download Entire PROFILES ex.: https://imgur.com/user/azyrusmax/ or https://imgur.com/account/azyrusmax/
- Written in uncomplicated Python
- Easily download files in the fastest speed possible
- Download using Multi-Threaded Downloads
- Easy to [install](https://github.com/DiSiqueira/DSImgur#installation)
- Stupidly [easy to use](https://github.com/DiSiqueira/DSImgur#usage)
- Download 100 files in less than 40s

## Installation

### Option 1: [Pip](https://pip.pypa.io/en/stable/installing/)

```bash
$ pip install DSImgur
```

### Option 2: From source

```bash
$ git clone https://github.com/DiSiqueira/DSImgur.git
$ cd DSImgur/
$ python setup.py install
```

## Usage

### Basic usage

```bash
# Download a image
$ DSImgur https://imgur.com/eUrbKtO
# Download a direct
$ DSImgur https://i.imgur.com/eUrbKtO.jpg
# Download a Album
$ DSImgur https://imgur.com/a/iwWZm
# Download a Gallery
$ DSImgur https://imgur.com/gallery/3ttnIn2
# Download a Entire Profile
$ DSImgur https://imgur.com/user/azyrusmax
```

### Download using Workers

```bash
# Download 1 image and 2 albums using 2 Workers
$ DSImgur --workers 2 https://i.imgur.com/eUrbKtO.jpg https://imgur.com/a/iwWZm https://imgur.com/a/3ttnIn2
```

### Set output folder

```bash
# Download 1 image and put it in my-images folder
$ DSImgur --output my-images https://i.imgur.com/eUrbKtO.jpg
```

### Combine everything

```bash
# Download 1 image and 2 albums using 2 Workers and put on my-images folder
$ DSImgur --output my-images --workers 2 https://i.imgur.com/eUrbKtO.jpg https://imgur.com/a/iwWZm https://imgur.com/a/3ttnIn2
```

## Module Usage
The module allows you to download url lists in your own Python programs without going through the command line. Here's an example of it's usage:

###Example
```python
from DSImgur import DSImgur

urls = ['https://imgur.com/eUrbKtOg', 'https://i.imgur.com/eUrbKtO.jpg', 'https://imgur.com/a/iwWZm', 'https://imgur.com/gallery/3ttnIn2', 'https://imgur.com/user/azyrusmax']
workers = 2
output = 'My-Files'

DSImgur(urls, workers, output)
```
## Requirements

* [Python](https://www.python.org)
* [DSDownload](https://github.com/DiSiqueira/DSDownload)

## Program Help

![](https://i.imgur.com/mKHbLay.png)

## Contributing

### Bug Reports & Feature Requests

Please use the [issue tracker](https://github.com/DiSiqueira/DSImgur/issues) to report any bugs or file feature requests.

### Developing

PRs are welcome. To begin developing, do this:

```bash
$ git clone --recursive git@github.com:DiSiqueira/DSImgur.git
$ cd DSImgur/src/
```

## Social Coding

1. Create an issue to discuss about your idea
2. [Fork it] (https://github.com/DiSiqueira/DSImgur/fork)
3. Create your feature branch (`git checkout -b my-new-feature`)
4. Commit your changes (`git commit -am 'Add some feature'`)
5. Push to the branch (`git push origin my-new-feature`)
6. Create a new Pull Request
7. Profit! :white_check_mark:

## License

The MIT License (MIT)

Copyright (c) 2013-2017 Diego Siqueira

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
