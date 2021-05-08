# Tootbot

This is a Python bot that looks up posts from specified subreddits and automatically posts them on Twitter and/or [Mastodon](https://joinmastodon.org/). It is based on [reddit-twitter-bot](https://github.com/rhiever/reddit-twitter-bot). Tootbot is now used by [a wide variety of social media accounts](https://github.com/corbindavenport/tootbot/wiki/Accounts-using-Tootbot).

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

**NEW:** Subscribe to the Tootbot updates feed [via email](https://feedburner.google.com/fb/a/mailverify?uri=tootbot) or [with an RSS reader](http://feeds.feedburner.com/tootbot) to be notified when a new version is available.

**Features:**

* Tootbot can post to both Twitter and [Mastodon](https://joinmastodon.org/)
* Tootbot can either run locally, or in the cloud with a free Heroku account
* Media from direct links, Gfycat, Imgur, Reddit, and Giphy is automatically attached in the social media post
* Links that do not contain media can be skipped, ideal for meme accounts like [@badreactiongifs](https://twitter.com/badreactiongifs)
* NSFW content, spoilers, and self-posts can be filtered
* Tootbot can monitor multiple subreddits at once
* Tootbot is fully open-source, so you don't have to give an external service full access to your social media accounts

Tootbot uses the [tweepy](https://github.com/tweepy/tweepy), [PRAW](https://praw.readthedocs.io/en/latest/), [py-gfycat](https://github.com/ankeshanand/py-gfycat), [imgurpython](https://github.com/Imgur/imgurpython), [Pillow](https://github.com/python-pillow/Pillow), and [Mastodon.py](https://github.com/halcy/Mastodon.py) libraries. The Heroku version also uses the [redis-py](https://github.com/andymccurdy/redis-py) library.

## Disclaimer

The developers of Tootbot hold no liability for what you do with this script or what happens to you by using this script. Abusing this script *can* get you banned from Twitter and/or Mastodon, so make sure to read up on proper usage of the API for each site.

## Setup and usage

For instructions on setting up and using Tootbot, please visit [the wiki](https://github.com/corbindavenport/tootbot/wiki).