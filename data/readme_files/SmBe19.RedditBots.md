# RedditBots
Reddit Bots by [/u/SmBe19](http://www.reddit.com/u/SmBe19)

To run any of those bots you need:
 - Python
 - PRAW (`pip install praw`)
 - OAuth2Util (`pip install praw-oauth2util`)

**You need PRAW 3** for the bots. They don't work anymore with PRAW 4 and PRAW 5. Due to missing time they won't be ported to new versions of PRAW, sorry.

If the bot uses OAuth2 you have to [register an app on Reddit](https://www.reddit.com/prefs/apps/), using `script` as app type and `http://127.0.0.1:65010/authorize_callback` as redirect uri. You then have to copy the file called `oauthtemplate.txt` to `oauth.ini` and enter the app id and app secret at the corresponding places. On first start up a webbrowser will be started where Reddit asks for permission. Make sure you are logged in with the user you want the bot to be run with when you click accept. If you want to run it on a server where you don't have a graphical browser you can try [server mode](https://github.com/SmBe19/praw-OAuth2Util/blob/master/OAuth2Util/README.md#server-mode) of `OAuth2Util`. Or you can run the bot the first time locally and then copy the `oauth.ini` file (which now contains all necessary tokens) to your server.

In the source code of the bots you will find at the top the `USER CONFIGURATION` and sometimes the `BOT CONFIGURATION`. In the `USER CONFIGURATION` section you should fill out every variable as they describe detailed what and where the bot should do (e.g. User Name, Subreddit to operate in, duration of sleep). The `BOT CONFIGURATION` section defines variables that you don't really have to change, but if you really have to, they are there. They are mostly constants for the bot (e.g. Name of config files).

You can set the variables set in the `USER CONFIGURATION` / `BOT CONFIGURATION` also in a separate file called `bot.py`, just use `key = value` (e.g. `username = "SmBe19"`). This way you don't have to edit the source directly (so it's easier to update) and you can exclude this file from git. Btw. it's a normal Python file, that get's executed, so you can use code as for example `password = getpass.getpass()`.
