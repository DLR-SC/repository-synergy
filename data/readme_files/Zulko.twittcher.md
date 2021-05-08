Twittcher
==========

Twittcher (for *twitter-watcher*) is a Python module to make bots that will watch a Twitter user page or search page, and react to the tweets they find.

It's simple, small (currently ~150 lines of code), and doesn't require any registration on Twitter or *dev.twitter.com*, as it doesn't depend on the Twitter API (instead it parses the HTML).

Twittcher is an open-source software originally written by Zulko_, and released under the MIT licence. The project is hosted on Github_, where you can report bugs, propose improvements, etc.

Install
--------

If you have `pip`, install twittcher by typing in a terminal:
::
    
    (sudo) pip install twittcher

Else, download the sources (on Github_ or PyPI_), and in the same directory as the `setup.py` file, type this in a terminal:
::
    
    (sudo) python setup.py install

Twittcher requires the Python package BeautifulSoup (a.k.a. bs4), which will be automatically installed when twittcher is installed.


Examples of use
----------------

There is currently no documentation for Twittcher, but the following examples should show you everything you need to get started.

1. Print the tweets of a given user
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Every 120 seconds, print all the new tweets by John D. Cook:
::
    
    from twittcher import UserWatcher
    UserWatcher("JohnDCook").watch_every(120)

Result:
::
    
    Kicking off some simulations before I quit work for the day. #dejavu
      Author: JohnDCook
      Date: 15:43 - 24 juil. 2014
      Link: https://twitter.com/JohnDCook/status/492440083073859585
    “Too often we enjoy the comfort of opinion without the discomfort of thought." -- John F. Kennedy,
      Author: JerryWeinberg
      Date: 13:18 - 24 juil. 2014
      Link: https://twitter.com/JerryWeinberg/status/492403371975114752

    
The default action of `UserWatcher` is to print the tweets, but you can ask any other action instead.
For instance, here is how to only print the tweets that are actually written by John D. Cook (not the ones he retweets):
::
    
    from twittcher import UserWatcher
    
    def my_action(tweet):
        if tweet.username == "JohnDCook":
            print(tweet)

    UserWatcher("JohnDCook", action=my_action).watch_every(120)


2. Control a distant machine through Twitter !
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Every 60 seconds, for any of my new tweets of the form ``cmd: my_command``, run ``my_command`` in a terminal.
Using simple tweets I can control any distant computer running this script.
::
    
    import subprocess
    from twittcher import UserWatcher

    def my_action(tweet):
        """ Execute the tweet's command, if any. """
        if tweet.text.startswith("cmd: "):
            subprocess.Popen( tweet.text[5:], shell=True )

    # Watch my account and react to my tweets
    bot = UserWatcher("Zulko___", action=my_action)
    bot.watch_every(60)

For instance, the tweet ``cmd: firefox`` will open Firefox on the computer, and the tweet ``cmd: echo "Hello"`` will have the computer print Hello in a terminal.


3. Watch search results and send alert mails
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Every 20 seconds, send me all the new tweets in the Twitter search results for `chocolate milk`.
::
    
    from twittcher import TweetSender, SearchWatcher
    sender = TweetSender(smtp="smtp.gmail.com", port=587,
                         login="tintin.zulko@gmail.com",
                         password="fibo112358", # be nice, don't try.
                         to_addrs="tintin.zulko@gmail.com", # where to send
                         sender_id = "chocolate milk")
    bot = SearchWatcher("chocolate milk", action=sender.send)
    bot.watch_every(20)

4. Multibot watching
~~~~~~~~~~~~~~~~~~~~~~~~

If you want to run several bots at once, make sure that you leave a few seconds between the requests of the different bots.
Here is how you print the new tweets of John D. Cook, Mathbabe, and Eolas. Each of them is watched every minute, with 20 seconds between the requests of two bots:
::
    
    import time
    import itertools
    from twittcher import UserWatcher
    
    bots = [ UserWatcher(user) for user in 
             ["JohnDCook", "mathbabedotorg",  "Maitre_Eolas"]]

    for bot in itertools.cycle(bots):
        bot.watch()
        time.sleep(20)


5. Saving the tweets
~~~~~~~~~~~~~~~~~~~~~~

A bot can save to a file the tweets that it has already seen, so that in future sessions it will remember not to process these tweets again, in case they still appear on the watched page.
::
    
    from twittcher import SearchWatcher
    bot = SearchWatcher("chocolate milk", database="choco.db")
    bot.watch_every(20)



.. _PyPI: https://pypi.python.org/pypi/twittcher
.. _Zulko : https://github.com/Zulko
.. _Github: https://github.com/Zulko/twittcher