# libgreader readme
libgreader is a Python library for authenticating and interacting with the unofficial Google Reader API. It currently supports all major user authentication methods (ClientLogin, OAuth2) and aims to simplify the many features that Google Reader offers. RSS ain't dead yet (but Google Reader may be)!

Licensed under the MIT license: [http://www.opensource.org/licenses/mit-license.php]()

## Current Status
As of March 2013, Google plans to shutdown down Google Reader on July 1st, 2013, which kind of makes this library not so useful.

There are plans to recreate the Google Reader API in several open source projects, so perhaps this library could be extended to support multiple APIs. At present, the author is waiting to see how things turn out and what course of action would make the most sense.


## Features

* Support for all Google recommended authentication methods, for easy integration with existing web or desktop applications
* Explanation of most of the Google Reader API endpoints, which Google has never really opened up
* Convenient functions and models for working with those endpoints
* A modest integration test suite!

## Usage

It's as simple as:


	>>> from libgreader import GoogleReader, ClientAuthMethod, Feed
	>>> auth = ClientAuthMethod('YOUR USERNAME','YOUR PASSWORD')
	>>> reader = GoogleReader(auth)
	>>> print reader.getUserInfo()
	{u'userName': u'Foo', u'userEmail': u'libgreadertest@gmail.com', u'userId': u'16058940398976999581', u'userProfileId': u'100275409503040726101', u'isBloggerUser': False, u'signupTimeSec': 0, u'isMultiLoginEnabled': False}`

For more examples with all of the authentication methods, see the [USAGE file](https://github.com/askedrelic/libgreader/blob/master/USAGE.md).

## Installation

libgreader is on pypi at [http://pypi.python.org/pypi/libgreader/](http://pypi.python.org/pypi/libgreader/)

	$ pip install libgreader

or 

	$ easy_install libgreader

## Testing and Contribution

Want to test it out or contribute some changes?

First, fork the repository on Github to make changes on your private branch.
Then, create a dev environment using a virtualenv:

	$ pip install virtualenvwrapper
	$ mkvirtualenv venv-libgreader --no-site-packages

Checkout your fork and then run the tests:

	$ python setup.py test

Now hack away! Write tests which show that a bug was fixed or that the feature works as expected. Then send a pull request and bug me until it gets merged in and published.


## Thanks

Originally created with help from:

[http://blog.martindoms.com/2009/08/15/using-the-google-reader-api-part-1/]()

[http://code.google.com/p/pyrfeed/wiki/GoogleReaderAPI]()

[http://groups.google.com/group/fougrapi]()

Since then, [many have contributed to the development of libgreader](https://github.com/askedrelic/libgreader/blob/master/AUTHORS.md).
