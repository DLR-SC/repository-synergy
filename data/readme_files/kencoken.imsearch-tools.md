Web Image Downloader Tools
============================================

Authors:

 + Ken Chatfield, University of Oxford – <ken@robots.ox.ac.uk>
 + Kevin McGuinness, Dublin City University – <kevin.mcguinness@eeng.dcu.ie>

Copyright 2010-2015, all rights reserved.

Release: v1.2.3 (October 2015)

License: MIT (see LICENSE.md)

Installation Instructions
-------------------------

First install all Python dependencies using:

    $ pip install -r requirements.txt

Following this:

 + Add `imsearchtools` directory to your `PYTHON_PATH`
 + Update `api_credentials.py` in the `/imsearchtools/engines` directory with appropriate
   API keys for each method you plan to use.

Usage Instructions
------------------

### 1. Querying web engine for image URLs

    >> import imsearchtools
    >> google_searcher = imsearchtools.query.GoogleWebSearch()
    >> results = google_searcher.query('car')
    >> results
    [{'image_id': '43e9644258865f9eedacf08e73f552fa',
      'url': 'http://asset3.cbsistatic.com/cnwk.1d/i/tim/2012/09/19/35446285_620x433.jpg'},
     {'image_id': 'cfd0ae160c4de2ebbd4b71fd9254d6df',
      'url': 'http://asset0.cbsistatic.com/cnwk.1d/i/tim/2012/08/15/35414204_620x433.jpg'},
     … ]

Currently the following search services are supported:

 + **GoogleWebSearch( )** – Image search using Google, extracted direct from the web
     - Preferred method for Google Image search
 + **GoogleAPISearch ( )** – Image search using Google, using the *Google Custom Search API*
     - A limit of 100 images per search is imposed
     - The results are different (slightly worse) than when using direct extraction
     - A 'custom search engine' must be created to use the API, with a list of sites to
       search specified during creation. However, selecting 'search these sites + entire
       web' in the options appears to give identical results to those returned by
       `GoogleAPISearch()`
     - Details and authentication key available at:
       <https://developers.google.com/custom-search/v1/overview/>
 + **GoogleOldAPISearch ( )** – Image search using Google, using the *Google Image Search API*
     - The *Google Image Search API* is now deprecated
     - A limit of 64 images per search is imposed
     - There is a higher default limit on number of free requests/day than with the
       new API
     - Details and authentication key available at:
       <https://developers.google.com/image-search/>
 + **BingAPISearch ( )** – Image search using Bing, using the *Bing Search API*
     - Details and authentication key available at:
       <http://www.bing.com/developers/>
 + **FlickrAPISearch ( )** – Image search using Flickr, using the *Flickr API*
     - Provides text search of Flickr photos by associated tags
     - Details and authentication key available at:
       <http://www.flickr.com/services/api/>

A test script `query_test.py` is provided which can be used to visualize the difference
between the methods:

    $ python query_test.py <query>

### 2. Verifying and downloading retrieved image URLs

Given the `results` array returned by `<web_service>.query(q)`, all URLs can be processed
and downloaded to local storage using the `process.ImageGetter()` class:

    ...
    >> getter = imsearchtools.process.ImageGetter()
    >> paths = getter.process_urls(results, '/path/to/save/images')
    >> paths
    [{'clean_fn': '/path/43e9644258865f9eedacf08e73f552fa-clean.jpg',
      'image_id': '43e9644258865f9eedacf08e73f552fa',
      'orig_fn': '/path/43e9644258865f9eedacf08e73f552fa.jpg',
      'thumb_fn': '/path/43e9644258865f9eedacf08e73f552fa-thumb-90x90.jpg',
      'url': 'http://asset3.cbsistatic.com/cnwk.1d/i/tim/2012/09/19/35446285_620x433.jpg'},
     {'clean_fn': '/path/cfd0ae160c4de2ebbd4b71fd9254d6df-clean.jpg',
      'image_id': 'cfd0ae160c4de2ebbd4b71fd9254d6df',
      'orig_fn': '/path/cfd0ae160c4de2ebbd4b71fd9254d6df.jpg',
      'thumb_fn': '/path/cfd0ae160c4de2ebbd4b71fd9254d6df-thumb-90x90.jpg',
      'url': 'http://asset0.cbsistatic.com/cnwk.1d/i/tim/2012/08/15/35414204_620x433.jpg'},
      … ]

`process_urls` returns a list of dictionaries, with each dictionary containing details of
images which were successfully downloaded:

 + `url` is the source URL for the image, the same as returned from `<web_service>.query(q)`
 + `image_id` is a unique identifier for the image, the same as returned from
   `<web_service>.query(q)`
 + `orig_fn` is the path of the original file downloaded direct from `url` – this image is
   unverified, and depending on the source URL may be corrupt
 + `clean_fn` is the path to a verified copy of `orig_fn`, which has been standardized
   according to the class options
 + `thumb_fn` is the path to a thumbnail version of `orig_fn`

A test script `download_test.py` is provided which can be used to demonstrate the usage of
the `process.ImageGetter()` class:

    $ python download_test.py

#### Configuring verification and download settings

Options for image verification and thumbnail generation can be customized by passing an
instance of the `process.ImageProcessorSettings` class to `process.ImageGetter()` during
initialization e.g.:

    >> opts = imsearchtools.process.ImageProcessorSettings()
    >> opts.filter['max_height'] = 600     # set maximum image size to 800x600
    >> opts.filter['max_width'] = 800      #    (discarding larger images)
    >> opts.conversion['format'] = 'png'   # change output format to png
    >> opts.conversion['max_height'] = 400 # set maximum image size to 600x400
    >> opts.conversion['max_width'] = 600  #    (downsizing larger images)
    >> opts.thumbnail['height'] = 50       # change width and height of thumbnails to 50x50
    >> opts.thumbnail['width'] = 50
    >> opts.thumbnail['pad_to_size'] = False # don't add padding to thumbnails
    >> getter = imsearchtools.process.ImageGetter(opts)

#### Adding a callback for post image download

Optionally, a callback function can be added which will be called immediately after each
image is downloaded and processed when using `process.ImageGetter.process_urls()`. To
do this, specify the callback when calling `process_urls()`:

    import imsearchtools

    def callback_func(out_dict, extra_prms=None):
        import json
        print extra_prms['extra_data']
        print json.dumps(out_dict)
        sleep(0.1)

    google_searcher = imsearchtools.query.GoogleWebSearch()
    results = google_searcher.query('car')

    getter = imsearchtools.process.ImageGetter()
    getter.process_urls(results, '/path/to/save/images',
                        completion_func=callback_func,
                        completion_extra_prms={'extra_data':'hello'},
                        completion_worker_count=8)

The form of the callback should be `f(out_dict)` where `out_dict` is a dictionary of the
same form as a single entry in the list returned from `process_urls()`.

The callbacks will be executed using a pool of worker processes, the size of which is
determined by the `completion_worker_count` parameter. If it is not specified, by default
*N* workers will be launched where *N* is the number of CPUs on the local system.

#### Notes about callbacks

Callbacks do not run in a separate CPU thread or process, but rather in the same thread
as the rest of the code in a gevent 'greenlet'. Greenlets allow many I/O bound operations
to run in parallel, but CPU-intensive code will cause problems as the main thread will
remain stuck in the callback giving very little CPU time to the module code.

As a result, callbacks should be restricted to code which *can be I/O intensive, but is
not CPU intensive* and is generally as short as possible. If CPU-intensive code must be
run, this can be achieved by using the callback to communicate with a separate 'runner'
process via TCP/IP / pipes / ZMQ etc. to launch the code.

HTTP Service
------------

A simple HTTP interface to the library is provided by `imsearch_http_service.py` and
can be launched by calling:

    python imsearch_http_service.py

For basic usage, the following function calls are provided:

 + `query` `GET` (*q='querytext', [engine='google_web', size='medium',
                  style='photo', num_results=100]*)
     - Returns JSON list of `image_id`+`url` pairs from the specified engine
 + `download` `POST` (*<query_json>*)
     - Accepts output from `query` and downloads the images, returning JSON output
       of the same format as the `ImageGetter` class
 + `get_engine_list` `GET`
     - Returns a list of the names of supported engines
       (e.g. `google_web`, `google_api` etc.)

#### Callbacks and advanced usage

As a callback function cannot be passed directly to the HTTP service, the concept of
*post-processing modules* has been introduced. These are a collection of pre-prepared
python scripts containing a callback function of the required format and which exist
within the `imsearchtools` module directory on the system where the server is running,
and any of them can be specified to run after each image has been downloaded.

For this functionality, and for more advanced usage (for example, to specify timeouts)
the following functions can be used:

 + `exec_pipeline` `POST`
     - Execute both the query and download stages with advanced options including
       support for callbacks. All of the parameters of the `query` function above
       are supported (`q`, `engine`, `size`, `style`, `num_results`) along with the
       following additional parameters:
           + `postproc_module` – the name of the post-processing module to run after each
             image has downloaded (use `get_postproc_module_list` for supported modules)
           + `postproc_extra_prms` – A JSON dictionary of additional parameters to pass to
             the post-processing module
           + `custom_local_path` – by default images are stored in the `static/` subdirectory
             of the server and URLs are returned (e.g. `http://server.com/static/result.jpg`).
             If this parameter is specified, a different path on the local system is used
             instead and the paths returned are local paths instead of URLs (e.g.
             `/my/custom/folder/result.jpg`)
           + `query_timeout` – timeout in seconds for the entire function call
           + `improc_timeout` – timeout in seconds for downloading each image
           + `resize_width` and `resize_height` – if specified, all downloaded images will be
              downsampled so that they are at most of width `resize_width`/height
              `resize_height`
           + `return_dfiles_list` – if specified, determines whether the paths to downloaded
             images should be returned (in the same way as the `download` function above) or
             only a shorter acknowledgement string should be returned instead. By default, if
             `postproc_module` has not been specified the full dictionary of paths is
             returned, and if it has then only the shorter acknowledgement string is returned
 + `get_postproc_module_list` `GET`
     - Returns a list of the names of supported post-processing modules

#### Writing your own post-processing modules

The code for all post-processing modules is stored in the `imsearchtools` package directory
at the following location:

    imsearchtools/postproc_modules/

Any `*.py` file placed in this directory will be used as an additional module. Refer to the
example in `example_textlog_module.py` for the required format of the module file.

Revision History
----------------

 + *Oct 2015* (1.2.3)
     - Cleaning up, demonstrate querying for variable number of images
 + *Apr 2015* (1.2.2)
     - Updated python dependencies and added server launch utilities
 + *Jun 2014* (1.2.1)
     - Switched from `requests` library for downloader to monkey-patched `urllib2`
       to make gevent greenlets work properly
 + *May 2014* (1.2)
     - Fixed `google-web` engine to work with updated Google search page
 + *Feb 2013*
     - Switched to pure gevent-based callbacks and fixed bugs in callback code
 + *Jan 2013*
     - Fixed issue with timeout by migrating from `restkit` to `requests` library
     - Added missing `gevent` monkey-patching to provide speed boost
     - Added HTTP service (including callback modules)
 + *Oct 2012*
     - Added support for Bing, the new Google API and Flickr, updated to new interface
     - Added `gevent` async support
     - Updated code for downloading and verification of images
     - Added documentation
 + *May 2011*
     - Updated Google web search method due to updates
 + *Nov 2010*
     - Original version with support for Google Image Search API + scraping
