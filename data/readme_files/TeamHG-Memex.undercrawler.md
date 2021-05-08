Undercrawler
============

[![Build Status](https://travis-ci.org/TeamHG-Memex/undercrawler.svg?branch=master)](https://travis-ci.org/TeamHG-Memex/undercrawler)
[![codecov.io](https://codecov.io/github/TeamHG-Memex/undercrawler/coverage.svg?branch=master)](https://codecov.io/github/TeamHG-Memex/undercrawler?branch=master)

This is a generic scrapy crawler. It is designed to handle a number
of challenges that are hard for traditional generic crawlers, such as
dynamic content, login and search forms, pagination. It crawls from the given
seed url in breadth first order,
exporting all carwled pages and documents into the CDRv2 format.

License is MIT.

Main features and used components are:

- By default, all pages are downloaded using [Splash](http://splash.readthedocs.io)
  which is a lightweight web browser with an HTTP API.
  [Aquarium](https://github.com/TeamHG-Memex/aquarium) can be used to
  add a load balancer for multiple Splash processes,
  compression for HTTP responses, Tor support (automatic for .onion links) and
  AdBlock Plus filters support.
- Headless Horseman Scripts help to reveal dynamic content
  such as infinite scrolls, removing overlays,
  elements revealed by clicking, etc.
  They are implemented as JS scripts that are injected into each rendered page,
  and Lua scripts that control the Splash browser.
- [Autologin](https://github.com/TeamHG-Memex/autologin) service can be used:
  it includes a UI for managing login credentials and a service that logs in
  and hands cookies to the crawler.
  It also includes a spider that finds login and registration forms
  to aid manual registration.
- [Autologin middleware](https://github.com/TeamHG-Memex/autologin-middleware)
  ensures that spider is crawling in logged-in state and avoids logouts.
- [Autopager](https://github.com/TeamHG-Memex/autopager) is used to detect
  pagination links. It allows the crawler to reach content via pagination
  faster and without hitting the depth limit,
  and to stay within the given soft "domain":
  if we start from a page with a paginator,
  we will crawl all the pages first before going elsewhere.
- Crazy Form Submitter discovers new content by performing searches.
  It uses predefined search terms (letters, digits and symbols) as well as
  user-supplied terms, and tries random refinements using checkbox controls.
- Links are additionally extracted links from iframes and onclick handlers.
- [MaybeDont](https://github.com/TeamHG-Memex/MaybeDont)
  tries to avoid duplicate content by learning which URL
  components do not alter the contents of the page, using MinHash LSH
  for duplicate detection.
- [Formasaurus](https://github.com/TeamHG-Memex/Formasaurus) is a library
  for form and field classification that is used by AutoLogin and
  Crazy Form Submitter.


Installation
------------

Requires Python 3.5:

    pip install -r requirements.txt
    formasaurus init

Install two optional services if you plan to use them:
[Splash](http://splash.readthedocs.io/) (see how to run it below)
and [Autologin](https://github.com/TeamHG-Memex/autologin).

There is also an option to run undercrawler with arachnado in a docker container:
see the [undercrawler-arachnado](./undercrawler-arachnado/README.md)
folder.


Run crawler
-----------

Start [Splash](http://splash.readthedocs.io/)
(or use [Aquarium](https://github.com/TeamHG-Memex/aquarium),
or disable Splash - see ``SPLASH_URL`` setting below):

    docker run -p 8050:8050 scrapinghub/splash

Start [Autologin](https://github.com/TeamHG-Memex/autologin) HTTP API
with the ``autologin-http-api`` command,
and the UI server with ``autologin-server``
(or disable autologin - see ``AUTOLOGIN_ENABLED`` below).

Specify url to crawl via the ``url`` param, and run the ``undercrawler`` spider:

    scrapy crawl undercrawler -a url=http://127.0.0.1:8001

Multiple urls can be passed from the command line using space (or tab, or newline)
delimiter, e.g ``-a url='example.com google.com'``.
You can also specify a file to read urls from, with ``-a url=./urls.txt``
(this can be an absolute path starting with "/" or a relative path starting with ".").
In case of multiple urls you must ensure that all urls use common authentication
(e.g. are from the same domain), or disable autologin.

Useful options to tweak (add to the above command via ``-s NAME=value``):

- ``ADBLOCK`` - set to 1 to enable AdBlock filters (they can make crawling faster)
- ``AVOID_DUP_CONTENT_ENABLED`` - set to 0 to disable avoiding duplicates
  based on urls
- ``AUTOLOGIN_ENABLED`` - set to 0 to disable autologin middleware
- ``AUTOLOGIN_URL`` - url of the autologin HTTP API
- ``AUTOLOGIN_USERNAME``, ``AUTOLOGIN_PASSWORD``, ``AUTOLOGIN_LOGIN_URL``
  - specify values to pass to autologin.
  Use them if you do not want to use autologin keychain UI.
  ``AUTOLOGIN_LOGIN_URL`` is a relative url.
- ``CDR_CRAWLER``, ``CDR_TEAM`` - CDR export metadata constants
- ``CRAZY_SEARCH_ENABLED`` - set to 0 to disable submitting search forms
- ``DOWNLOAD_DELAY`` - set to 0 when crawling local test server
- ``FILES_STORE`` - S3 location for saving extracted documents (including images),
  format is ``s3://bucket/prefix/`` for storing to S3 or a local path for storing
  media items locally (in case of local path, ``obj_stored_url`` will be relative
  to the ``FILES_STORE`` path).
- ``FOLLOW_LINKS`` - set to 0 to crawl only initial urls. Media items will still
  be crawled (if they should be crawled according to the rest of the settings)
- ``FORCE_TOR`` - crawl via tor to avoid blocking
- ``HARD_URL_CONSTRAINT`` - set to 1 to treat start urls as hard constraints
  (by default we start from given url but crawl the whole domain)
- ``IMAGES_ENABLED`` - set to 1 to enable loading images in splash.
  This affects only the screenshots (and speed), but not saving images.
- ``MAX_DOMAIN_SEARCH_FORMS`` - max number of search forms considered for domain
- ``PREFER_PAGINATION`` - set to 0 to disable pagination handling, or adjust
  as needed (value is in seconds).
- ``RUN_HH`` - set to 0 to skip running full headless-horseman scripts.
- ``SEARCH_TERMS_FILE`` - file with extra search terms to use (one per line)
- ``SCREENSHOT`` - set to 1 to save screenshots while crawling. Path to screenshot
   will be saved to ``screenshot`` field in the item metadata. It's relative by
   default, but will be absolute if you pass absolute path to ``SCREENSHOT_DEST``.
- ``SCREENSHOT_DEST`` - set path to folder where to store the screenshots
   ("screenshots" by default).
- ``SCREENSHOT_WIDTH``, ``SCREENSHOT_HEIGHT``: screenshot size.
   If ``SCREENSHOT_HEIGHT`` is set to 0, then the full page height is used for the
   screenshot. If not set, screenshot dimensions are equal to
 ``VIEWPORT_WIDTH`` and ``VIEWPORT_HEIGHT``.
- ``SCREENSHOT_PREFIX`` - set prefix for screenshot files, empty by default.
- ``SPLASH_URL`` - url of the splash instance
  (if empty, crawl without using splash)
- ``VIEWPORT_WIDTH``, ``VIEWPORT_HEIGHT``: viewport size for splash rendering.
  Note that these settings can affect resulting content, as
  many websites use a mobile version for smaller screens.
  Defaults are 1024 and 768.

Pages are stored in CDRv2 format, with the following custom fields inside
``extracted_metadata``:

- ``depth``: page depth
- ``extracted_at``: a page where this link was (first) extracted
- ``form``: forms metadata extracted by formasaurus
- ``from_search``: page was reached from search results
- ``is_iframe``: page url was extracted from an ``iframe``
- ``is_onclick``: page url was extracted from ``onclick``, not from a normal link
- ``is_page``: page was reached via pagination
- ``is_search``: this is a search result page
- ``screenshot``: path to saved screenshot, if any (see ``SCREENSHOT`` setting)

All documents (including images) are exported if ``FILES_STORE`` is set.

You can use ``./scripts/crawl_stats.py`` to analyze extracted metadata.

Scripts
-------

* ``./scripts/crawl_stats.py``:
  show crawling stats, including ``extracted_metadata``
* ``./scripts/gen_supervisor_configs.py``:
  generate supervisord configs for crawlers from a list of urls

Tests
-----

Run all tests with:

    tox

This assumes that splash is running on the default url http://127.0.0.1:8050
with ``--network host``.

Tests are run using py.test, you can pass arguments after ``--``:

    tox -- tests/test_spider.py

---

[![define hyperion gray](https://hyperiongray.s3.amazonaws.com/define-hg.svg)](https://www.hyperiongray.com/?pk_campaign=github&pk_kwd=undercrawler "Hyperion Gray")
