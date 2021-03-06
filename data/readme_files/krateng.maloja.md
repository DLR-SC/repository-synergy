# Maloja

[![](https://img.shields.io/pypi/v/malojaserver?style=for-the-badge)](https://pypi.org/project/malojaserver/)
[![](https://img.shields.io/pypi/dm/malojaserver?style=for-the-badge)](https://pypi.org/project/malojaserver/)
[![](https://img.shields.io/github/stars/krateng/maloja?style=for-the-badge&color=purple)](https://github.com/krateng/maloja/stargazers)
[![](https://img.shields.io/pypi/l/malojaserver?style=for-the-badge)](https://github.com/krateng/maloja/blob/master/LICENSE)

Simple self-hosted music scrobble database to create personal listening statistics. No recommendations, no social network, no nonsense.

You can check [my own Maloja page](https://maloja.krateng.ch) to see what it looks like.


> **IMPORTANT**: With the update 2.0, Maloja has been refactored into a Python package and the old update script no longer works. If you're still on version 1, see [below](#update).

## Table of Contents
* [Why not Last.fm / Libre.fm / GNU FM?](#why-not-lastfm--librefm--gnu-fm)
* [How to install](#how-to-install)
	* [New Installation](#new-installation)
	* [Update](#update)
* [How to use](#how-to-use)
	* [Basic control](#basic-control)
	* [Data](#data)
	* [Customization](#customization)
* [How to scrobble](#how-to-scrobble)
	* [Native API](#native-api)
	* [Standard-compliant API](#standard-compliant-api)
	* [Manual](#manual)
* [How to extend](#how-to-extend)

## Why not Last.fm / Libre.fm / GNU FM?

Maloja is **self-hosted**. You will always be able to access your data in an easily-parseable format. Your library is not synced with any public or official music database, so you can **follow your own tagging schema** or even **group associated artists together** in your charts.

Maloja also gets **rid of all the extra stuff**: social networking, radios, recommendations, etc. It only keeps track of your listening history and lets you analyze it.

Maloja's database has one big advantage: It supports **multiple artists per track**. This means artists who are often just "featuring" in the track title get a place in your charts, and **collaborations between several artists finally get credited to all participants**. This allows you to get an actual idea of your artist preferences over time.

Also neat: You can use your **custom artist or track images**.


## How to install

### New Installation

1) Make sure you have Python 3.5 or higher installed. You also need some basic packages that should be present on most systems, but I've provided simple shell scripts for Alpine and Ubuntu to get everything you need.

2) If you'd like to display images, you will need API keys for [Last.fm](https://www.last.fm/api/account/create) and [Fanart.tv](https://fanart.tv/get-an-api-key/) (you need a project key, not a personal one). These are free of charge!

3) Download Maloja with the command `pip install malojaserver`. Make sure to use the correct python version (Use `pip3` if necessary).

4) (Recommended) Put your server behind a reverse proxy for SSL encryption. Make sure that you're proxying to the IPv6 address unless you changed your settings to use IPv4. If you're running Maloja in a container, make sure to expose port 32400 (or whichever port you have chosen in your settings).

5) (Recommended) Until I have a proper service implemented, I would recommend setting two cronjobs for maloja:

```
@reboot maloja start
42 0 * * * maloja restart
```


### Update

* If you use a version before 2.0 (1.x), install the package as described above, then manually copy all your user data to your `~/.local/share/maloja` folder.
* Otherwise, simply run the command `maloja update` or use `pip`s update mechanic.


## How to use

### Basic control

Start and stop the server with

	maloja start
	maloja stop
	maloja restart

If something is not working, you can try

	maloja debug

to run the server in the foreground.


### Data

* If you would like to import all your previous last.fm scrobbles, use [benfoxall's website](https://benjaminbenben.com/lastfm-to-csv/) ([GitHub page](https://github.com/benfoxall/lastfm-to-csv)). Use the command `maloja import *filename*`	to import the downloaded file into Maloja.

* To backup your data, run `maloja backup` or, to only backup essential data (no artwork etc), `maloja backup -l minimal`.

* To fix your database (e.g. after you've added new rules), use `maloja fix`.

### Customization

* Have a look at the `default.ini` file in the `~/.local/share/maloja/settings` folder to see what settings are available. Specify your own choices in `settings.ini`. You can also set each of these settings as an environment variable with the prefix `MALOJA_` (e.g. `MALOJA_SKIP_SETUP`).

* If you have activated admin mode in your web interface, you can upload custom images for artists or tracks by simply dragging them onto the existing image on the artist or track page. You can also manage custom images directly in the file system - consult `images.info` in the `~/.local/share/maloja/images` folder.

* To specify custom rules, consult the `rules.info` file in `~/.local/share/maloja/rules`. You can also apply some predefined rules on the `/setup` page of your server.


## How to scrobble

You can set up any amount of API keys in the file `authenticated_machines.tsv` in the `~/.local/share/maloja/clients` folder.

### Native API

If you use Plex Web, Spotify, Bandcamp, Soundcloud or Youtube Music on Chromium, you can use the included extension (also available on the [Chrome Web Store](https://chrome.google.com/webstore/detail/maloja-scrobbler/cfnbifdmgbnaalphodcbandoopgbfeeh)). Make sure to enter the random key Maloja generates on first startup in the extension settings.

If you want to implement your own method of scrobbling, it's very simple: You only need one POST request to `/api/newscrobble` with the keys `artist`, `title` and `key` - either as form-data or json.

### Standard-compliant API

You can use any third-party scrobbler that supports the audioscrobbler (GNUFM) or the ListenBrainz protocol. This is still very experimental, but give it a try with these settings:

GNU FM | &nbsp;
------ | ---------
Gnukebox URL | Your Maloja URL followed by `/api/s/audioscrobbler`
Username | Any name, doesn't matter
Password | Any of your API keys

ListenBrainz | &nbsp;
------ | ---------
API URL | Your Maloja URL followed by `/api/s/listenbrainz`
Username | Any name, doesn't matter
Auth Token | Any of your API keys

These are tested with the Pano Scrobbler and the Simple Last.fm Scrobbler for Android. I'm thankful for any feedback whether other scrobblers work!

It is recommended to define a different API key for every scrobbler you use in `clients/authenticated_machines.tsv` in your Maloja folder.

### Manual

If you can't automatically scrobble your music, you can always do it manually on the `/manual` page of your Maloja server.


## How to extend

If you'd like to implement anything on top of Maloja, visit `/api_explorer`.
