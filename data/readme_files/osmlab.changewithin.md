# Changewithin

*Daily emails of changes to buildings and addresses on OpenStreetMap.*

changewithin is a simple script that pulls [daily changes](http://planet.openstreetmap.org/)
from OpenStreetMap with `requests`, parses them with `lxml`, finds the ones that are inside
of a GeoJSON shape, sorts out the ones that are buildings, and emails a set of users
with [mailgun](http://www.mailgun.com/).

The one file that will require editing is [config.ini](https://github.com/migurski/changewithin/blob/master/config.ini).

At the top you will find a simple list of email addresses to which the script
will send reports. The email templates for both html and text can be edited within
the file `lib.py`. The report itself contains a summary of changes, then lists
each relevant changeset, its ID, and further details. These include the user who
made the change and their comment, individual element IDs for building footprint
and address changes that link to their history, and a map thumbnail that is centered
on the location where the edits were made.

### Geography

`nyc.geojson` contains sample boundaries for New York City.

You can configure a remote URL containing GeoJSON data. US Census places and
counties are available from [Code for America](http://codeforamerica.org),
referenced by GEOID. To find the GEOID for a county or place, start with one
of these Census lookup tools:

* http://www.census.gov/geo/reference/codes/cou.html (Counties)
* http://www.census.gov/geo/reference/codes/place.html (Places)

Each GEOID combines the state FIPS code (two digits) and
[ANSI code](http://www.census.gov/geo/reference/ansi.html).
For example, to find the GEOID of New York City, select New York State via the
[Place Lookup tool](http://www.census.gov/geo/reference/codes/place.html)
above and look for "New York City" [on the page](http://www.census.gov/geo/reference/codes/data/place/3600000.html).
Its ANSI code is 51000 and New York's state FIPS code is 36. Therefore, New
York City's GEOID is 3651000 and its GeoJSON URL is:

* http://forever.codeforamerica.org/Census-API/by-geoid/3651000.json

Example GeoJSON URLs for L.A. County, Washington DC, and Oakland CA:

* http://forever.codeforamerica.org/Census-API/by-geoid/06037.json
* http://forever.codeforamerica.org/Census-API/by-geoid/11001.json
* http://forever.codeforamerica.org/Census-API/by-geoid/0653000.json

## Installation

Requires [wget](http://www.gnu.org/software/wget/) or [cURL ](http://curl.haxx.se/).

cURL typically comes pre-installed.

For Mac use [homebrew](http://brew.sh/) and one of:

    brew install wget
    brew install curl

For Ubuntu/Linux one of:

    apt-get install wget
    apt-get install curl

Requires Python with [lxml](http://lxml.de/), [requests](http://docs.python-requests.org/),
[pystache](http://defunkt.io/pystache/), [PIL](http://effbot.org/imagingbook/),
and [ModestMaps](https://github.com/stamen/modestmaps-py).

Optionally [set up virtualenv](http://www.virtualenv.org/en/latest/#usage):

    virtualenv --no-site-packages venv-changewithin
    source venv-changewithin/bin/activate

Install libraries needed for fast XML processing and Python extensions.
For Ubuntu/Linux:

    apt-get install python-dev libxml2-dev libxslt1-dev

Install Python packages:
    
    pip install -r requirements.txt

Copy config-example.ini to config.ini and configure area of interest under `[area]` and email recipients under `[email]`.

## Running

    python changewithin.py

## Automating

Assuming the above installation, edit your [cron table](https://en.wikipedia.org/wiki/Cron) (`crontab -e`) to run the script once a day at 7:00am.

    0 7 * * * ~/path/to/changewithin/bin/python ~/path/to/changewithin/changewithin.py

