# VeriPress

[![License](https://img.shields.io/github/license/veripress/veripress.svg)](LICENSE)
[![Build Status](https://travis-ci.org/veripress/veripress.svg?branch=master)](https://travis-ci.org/veripress/veripress)
[![Coverage Status](https://coveralls.io/repos/github/veripress/veripress/badge.svg?branch=master)](https://coveralls.io/github/veripress/veripress?branch=master)
[![PyPI](https://img.shields.io/pypi/v/veripress.svg)](https://pypi.python.org/pypi/veripress)
![Python](https://img.shields.io/badge/python-3.4%2B-blue.svg)
[![Tag](https://img.shields.io/github/tag/veripress/veripress.svg)](https://github.com/veripress/veripress/tags)
[![Docker Repository](https://img.shields.io/badge/docker-veripress/veripress-blue.svg)](https://hub.docker.com/r/veripress/veripress/)
[![Docker Pulls](https://img.shields.io/docker/pulls/veripress/veripress.svg)](https://hub.docker.com/r/veripress/veripress/)

VeriPress is a blog engine for hackers, which is very similar to Octopress and Hexo, but with some different features. It's written in Python 3.4+ based on Flask web framework. Here is a [demo](https://veripress.github.io/demo/).

## Features

- Supports three publish types: post, page, widget
- Theme management
- Custom post/page layout
- Supports Markdown, HTML and plain TXT
- Run as dynamic web app
- Generating static HTML pages
- API mode
- Atom feed
- and more...

## Quick Start

It's dead easy to get started with VeriPress:

```sh
$ pip3 install veripress  # Install VeriPress
$ mkdir ~/my-veripress  # Create an empty folder as a VeriPress instance
$ cd ~/my-veripress
$ veripress init  # Initialize the VeriPress instance
$ veripress theme install default  # Install the "default" theme
$ veripress preview  # Preview the instance
```

Run the above commands and then you can visit the very initial VeriPress instance at `http://127.0.0.1:8080/`.

See [documentation](https://veripress.github.io/docs/) for more information on how to use VeriPress.

## Documentation

Documentation is now available in [Simplified Chinese (简体中文)](https://veripress.github.io/docs/), and the English version is coming soon.

## Themes

There are some official themes [here](https://github.com/veripress/themes), and also a theme collection [here](https://stdrc.cc/post/2018/10/13/collection-of-veripress-themes/) (in Simplified Chinese).

## Contributing

If you want to help to develop VeriPress, fork this repo and send me a pull request. Source codes of docs and demo are also available in this repo, so if you find mistakes, feel free to send me a pull request too.

If you just have some questions or bug reports, you can also submit issues in this repo.

Thanks for your support and help.
