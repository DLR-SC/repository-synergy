Geograpy2
=========

Extract place names from a URL or text, and add context to those names -- for 
example distinguishing between a country, region or city. 


## Install & Setup

Grab the package using `pip` (this will take a few minutes)

    pip install geograpy2

Geograpy2 uses [NLTK](http://www.nltk.org/) for entity recognition, so you'll also need 
to download the models we're using. Fortunately there's a command that'll take 
care of this for you. 

    geograpy-nltk

## Basic Usage

Import the module, give some text or a URL, and presto.

    import geograpy2
    url = 'http://www.bbc.com/news/world-europe-26919928'
    places = geograpy2.get_place_context(url=url)


## Credits

Geograpy2 is a fork of [geograpy](https://github.com/ushahidi/geograpy) and inherits
most of it, but solves several problems (such as support for utf8, places names 
with multiple words, confusion over homonyms etc).

Geograpy2 uses the following excellent libraries:

* [NLTK](http://www.nltk.org/) for entity recognition
* [newspaper](https://github.com/codelucas/newspaper) for text extraction from HTML
* [jellyfish](https://github.com/sunlightlabs/jellyfish) for fuzzy text match
* [pycountry](https://pypi.python.org/pypi/pycountry) for country/region lookups

Geograpy uses the following data sources:

* [GeoLite2](http://dev.maxmind.com/geoip/geoip2/geolite2/) for city lookups
* [ISO3166ErrorDictionary](https://github.com/bodacea/countryname/blob/master/countryname/databases/ISO3166ErrorDictionary.csv) for common country mispellings _via [Sara-Jayne Terp](https://github.com/bodacea)_

Hat tip to [Chris Albon](https://github.com/chrisalbon) for the name.

Released under the MIT license.