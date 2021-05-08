# scrape-itebooks

Developed using Python 3.4

Scrape the site https://it-ebooks.info/ and save all the books on the site. Currently does not backfill but will keep up with the latest uploads

*I am working on a way to backfill all of the data.


Must pass in a config file like so: `python3 it-ebooks.py -c ~/scrapers.conf`

See what the conf file needs to contain here: https://git.eddyhintze.com/xtream1101/scraper-lib

This scraper also requires this section in the config:
```
[it-ebooks]
# `scraper_key` is only needed if `scraper-monitor` is enabled
scraper_key =
```

## Setup

Run `pip3 install -r requirements.txt`
