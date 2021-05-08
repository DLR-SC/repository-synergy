<img src="https://camo.githubusercontent.com/9ac4a1f7f5ea0f573451b5ddc06e29c8aa113a85/68747470733a2f2f692e696d6775722e636f6d2f6948326a6468562e706e67" align="right">

Instagram Scraper
=================
[![PyPI](https://img.shields.io/pypi/v/instagram-scraper.svg)](https://pypi.python.org/pypi/instagram-scraper) [![Build Status](https://travis-ci.org/rarcega/instagram-scraper.svg?branch=master)](https://travis-ci.org/rarcega/instagram-scraper)

instagram-scraper is a command-line application written in Python that scrapes and downloads an instagram user's photos and videos. Use responsibly.

<img src="https://cloud.githubusercontent.com/assets/140931/26286476/8232e15e-3e34-11e7-9e1c-9ecda92950e1.gif">

Install
-------
To install instagram-scraper:
```bash
$ pip install instagram-scraper
```

To update instagram-scraper:
```bash
$ pip install instagram-scraper --upgrade
```
Alternatively, you can clone the project and run the following command to install:
Make sure you cd into the *instagram-scraper-master* folder before performing the command below.
```
$ python setup.py install
```


Usage
-----

To scrape a user's media:
```bash
$ instagram-scraper <username> -u <your username> -p <your password>             
```
*NOTE: To scrape a private user's media you must be an approved follower.*

*By default, downloaded media will be placed in `<current working directory>/<username>`.*


Providing username and password is optional, if not supplied the scraper runs as a guest. 
*Note: In this case all private user's media will be unavailable. All user's stories and high resolution profile pictures will also be unavailable.*


To scrape a hashtag for media:
```bash
$ instagram-scraper <hashtag without #> --tag          
```
*It may be useful to specify the `--maximum <#>` argument to limit the total number of items to scrape when scraping by hashtag.*


To specify multiple users, pass a delimited list of users:
```bash
$ instagram-scraper username1,username2,username3           
```

You can also supply a file containing a list of usernames:
```bash
$ instagram-scraper -f ig_users.txt           
```

```
# ig_users.txt

username1
username2
username3

# and so on...
```
*The usernames may be separated by newlines, commas, semicolons, or whitespace.*


OPTIONS
-------

```
--help -h               Show help message and exit.

--login-user  -u        Instagram login user.

--login-pass  -p        Instagram login password.

--followings-input      Use profiles followed by login-user as input

--followings-output     Output profiles from --followings-input to file

--filename    -f        Path to a file containing a list of users to scrape.

--destination -d        Specify the download destination. By default, media will 
                        be downloaded to <current working directory>/<username>.

--retain-username -n    Creates a username subdirectory when the destination flag is
                        set.

--media-types -t        Specify media types to scrape. Enter as space separated values. 
                        Valid values are image, video, story (story-image & story-video),
                        or none. Stories require a --login-user and --login-pass to be defined.
                      
--latest                Scrape only new media since the last scrape. Uses the last modified
                        time of the latest media item in the destination directory to compare.

--latest-stamps         Specify a file to save the timestamps of latest media scraped by user.
                        This works similarly to `--latest` except the file specified by
                        `--latest-stamps` will store the last modified time instead of using 
                        timestamps of media items in the destination directory. 
                        This allows the destination directories to be emptied whilst 
                        still maintaining history.

--cookiejar             File in which to store cookies so that they can be reused between runs.

--quiet       -q        Be quiet while scraping.

--maximum     -m        Maximum number of items to scrape.

--media-metadata        Saves the media metadata associated with the user's posts to 
                        <destination>/<username>.json. Can be combined with --media-types none
                        to only fetch the metadata without downloading the media.

--include-location      Includes location metadata when saving media metadata. 
                        Implicitly includes --media-metadata.

--profile-metadata      Saves the user profile metadata to  <destination>/<username>.json.

--proxies               Enable use of proxies, add a valid JSON with http or/and https urls.
                        Example: '{"http": "http://<ip>:<port>", "http": "https://<ip>:<port>" }'

--comments             Saves the comment metadata associated with the posts to 
                       <destination>/<username>.json. Implicitly includes --media-metadata.
                    
--interactive -i       Enables interactive login challenge solving. Has 2 modes: SMS and Email

--retry-forever        Retry download attempts endlessly when errors are received

--tag                   Scrapes the specified hashtag for media.

--filter                Scrapes the specified hashtag within a user's media.

--filter_location       Filter scrape queries by command line location(s) ids

--filter_location_file  Provide location ids by file to filter queries 

--location              Scrapes the specified instagram location-id for media.

--search-location       Search for a location by name. Useful for determining the location-id of 
                        a specific place.
                    
--template -T           Customize and format each file's name.
                        Default: {urlname}
                        Options:
                        {username}: Scraped user
                        {shortcode}: Post shortcode (profile_pic and story are empty)
                        {urlname}: Original file name from url.
                        {mediatype}: The type of media being downloaded.
                        {datetime}: Date and time of upload. (Format: 20180101 01h01m01s)
                        {date}: Date of upload. (Format: 20180101)
                        {year}: Year of upload. (Format: 2018)
                        {month}: Month of upload. (Format: 01-12)
                        {day}: Day of upload. (Format: 01-31)
                        {h}: Hour of upload. (Format: 00-23h)
                        {m}: Minute of upload. (Format: 00-59m)
                        {s}: Second of upload. (Format: 00-59s)

                        If the template is invalid, it will revert to the default.
                        Does not work with --tag and --location.
```

Develop
-------

Clone the repo and create a virtualenv 
```bash
$ virtualenv venv
$ source venv/bin/activate
$ python setup.py develop
```

Running Tests
-------------

```bash
$ python setup.py test

# or just 

$ nosetests
```

Contributing
------------

1. Check the open issues or open a new issue to start a discussion around
   your feature idea or the bug you found
2. Fork the repository, make your changes, and add yourself to [AUTHORS.md](AUTHORS.md)
3. Send a pull request

License
-------
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
