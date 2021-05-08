# Hypermark!

[![PyPI](https://img.shields.io/pypi/v/hypermark?style=flat-square)](https://pypi.org/project/hypermark/)
[![License](https://img.shields.io/github/license/ryanccn/hypermark.svg?style=flat-square)](https://github.com/ryanccn/hypermark/blob/master/LICENSE)
[![Dependabot Status](https://img.shields.io/badge/Dependabot-enabled-success.svg?style=flat-square&logo=dependabot)](https://dependabot.com)
[![CodeFactor Grade](https://img.shields.io/codefactor/grade/github/ryanccn/hypermark.svg?style=flat-square)](https://www.codefactor.io/repository/github/ryanccn/hypermark)
[![Code style: black](https://img.shields.io/badge/code_style-black-black.svg?style=flat-square)](https://github.com/python/black)

Markdown is Hypertext.

Inspirational, fast, reversible,
extendable, and filterable.

![ॐ](https://img.shields.io/badge/zen-ॐ-9cf.svg?style=for-the-badge)

## Current Usage

```pycon
>>> import hypermark

>>> content = "# fuck yea\nhttp://github.com"

>>> d = hypermark.text(content)
'<HyperText 7c7706acb8>'

>>> d.links
['http://github.com']

>>> d.hash
u'03a392ef91826a3506fcc54a4e1fa7b022688ec42bc4d53b4c36a8b6f8058606'

>>> print(d.html)
<h1>fuck yea</h1>
<p><a href="http://github.com">http://github.com</a></p>

```

## Convert HTML to Markdown!

```pycon
>>> print(hypermark.html('<h1>test h1</h1>'))
# test h1
```

## Filters!

```pycon
>>> print(d.filter('bleach').html)
&lt;h1&gt;fuck yea&lt;/h1&gt;
&lt;p&gt;<a href="http://github.com">http://github.com</a>&lt;/p&gt;


>>> print(d.filter('transpose_headers', levels=1).html)
<h2>fuck yea</h2>
<p><a href="http://github.com">http://github.com</a></p>

>>> print(d.filter('anchors').html)
<h1 id="toc-1">fuck yea</h1>
<p><a href="http://github.com">http://github.com</a></p>
```

## Vision (Work in Progress)

Feature ideas:

- [x] link extraction
- [ ] diff generation
- [x] sha generation
- [x] md -> html, html -> md
- [ ] header transposing
- [ ] stripping?
- [ ] targets for headers
- [ ] expand tests
