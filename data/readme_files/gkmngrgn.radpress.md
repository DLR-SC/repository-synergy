::

     _____             _
    |  __ \           | |
    | |__) | __ _   __| | _ __   _ __  ___  ___  ___
    |  _  / / _` | / _` || '_ \ | '__|/ _ \/ __|/ __|
    | | \ \| (_| || (_| || |_) || |  |  __/\__ \\__ \
    |_|  \_\\__,_| \__,_|| .__/ |_|   \___||___/|___/
                         | |
                         |_|


.. image:: https://travis-ci.org/gkmngrgn/radpress.png
        :target: https://travis-ci.org/gkmngrgn/radpress

.. image:: https://pypip.in/d/radpress/badge.png
        :target: https://crate.io/packages/radpress

Radpress is a simple blog application for Djangonauts. It doesn't use a WYSIWYG
editor; the default markup syntax is `reStructuredText`_ and you can preview
your entry simply before publishing it. Radpress now ships with a `Markdown`_
renderer, too!

.. image:: https://rawgithub.com/twolfson/gittip-badge/0.2.0/dist/gittip.png
        :target: https://www.gittip.com/gokmen/

Radpress' default theme is based on `Author theme`_ by Mike McAlister. Thank
you for the support.

Features
--------
- Zen mode for writing articles
- Disqus support for comment and reactions
- Useful sidebar widgets; tag cloud, latest posts
- Adding page links in navigation bar
- Listing archives by date or tag
- Author information for articles
- Simple theme like in Octopress.

Supported markup languages
--------------------------
- reStructuredText
- Markdown

How to contribute?
------------------
I work with Python virtualenv. After I activated my virtualenv, I install
all requires with a command::

    $ pip install -r requirements/development.txt

Authors
-------
Gökmen Görgen, <gokmen[@]alageek.com>

Contributors
------------
Ben Stott, <bgbnbigben[@]contextualsystems.com>

Licensing
---------
Radpress is free software under terms of the MIT License. For more information,
see the LICENSE file.

.. _restructuredtext: http://docutils.sourceforge.net/rst.html
.. _Markdown: http://daringfireball.net/projects/markdown/
.. _Author theme: http://themes.okaythemes.com/author/
