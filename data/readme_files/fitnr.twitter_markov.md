twitter markov
==============

Create markov chain ("_ebooks") accounts on Twitter.

The audience for this library is those with at least basic Python experience. Before you set this up, you'll need:

* A twitter account
* A twitter application (register at [dev.twitter.com](http://dev.twitter.com)) with authentication keys for the account ([read more](https://dev.twitter.com/oauth))
* A text for the bot to learn from, which can be a text file or a Twitter archive. Several thousand lines are needed to get decent results, with fewer than 100 or so it won't work at all.

## Install

Run `pip install twitter_markov`, or download/clone the package and run `python setup.py install`. Feel free to use a virtualenv, if you're into that.

## Setting up a bot

[See the docs](http://pythonhosted.org/twitter_markov) for a complete guide to setting up an ebooks bot. Here are the basics:

* Create a app and authenticate it with your new Twitter account
* [Create a corpus](http://pythonhosted.org/twitter_markov/corpus.html), a text file with one sentence or text per line
* [Create a `bots.yaml` config file](http://pythonhosted.org/twitter_markov/config.html)
* [Set up a task to tweet and reply](http://pythonhosted.org/twitter_markov/tweet.html)

## API

[See the docs](http://pythonhosted.org/twitter_markov/api.html).

## License

Copyright 2014-2016, Neil Freeman. This software is available under the GPL 3.0. See LICENSE for more information.