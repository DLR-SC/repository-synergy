# Instabot.py 🤖 🌟

**Instabot.py** is an extremely light instagram bot that uses the undocumented Web API. Unlike other bots, Instabot.py does _not_ require Selenium or a WebDriver. Instead, it interacts with the API over simple HTTP Requests. It runs on most systems, including Raspberry Pi.

[![Chat on Telegram](https://img.shields.io/badge/Chat%20on-Telegram-brightgreen.svg)](https://t.me/joinchat/DYKH-0G_8hsDDoN_iE8ZlA)
[![Latest version on](https://badge.fury.io/py/instabot-py.svg)](https://badge.fury.io/py/instabot-py)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/instabot-py.svg)](https://pypi.org/project/instabot-py/)
[![Donate](https://img.shields.io/badge/PayPal-Donate%20to%20Author-blue.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=7BMM6JGE73322&lc=US)
<!-- [![Travis Pipelines build status](https://img.shields.io/travis/com/yurilaaziz/instabot-py.svg)](https://travis-ci.com/yurilaaziz/instabot-py/) -->

## Requirements

- Python v3.6 or greater
- Pip v18 or greater

## Quick Start 🚀

- **Make sure you have Python 3.6 or above installed**

  - `python3 --version`

On Windows you might have to use `python` without the version (`3`) suffix. Experienced users should use virtualenv.

- **If your version is below 3.6, we recommend you install the latest Python 3.7 or 3.8**

  - [Python on Windows](https://github.com/instabot-py/instabot.py/wiki/Installing-Python-on-Windows)
  - [Python on Mac](https://github.com/instabot-py/instabot.py/wiki/Installing-Python-3.7-on-macOS)
  - [Python on Raspberry Raspbian / Debian / Ubuntu](https://github.com/instabot-py/instabot.py/wiki/Installing-Python-3.7-on-Raspberry-Pi)

**Installation**

- From PyPi (Stable):

```
python3 -m pip install instabot-py
```
- From sources (Bleeding edge):

```
python3 -m pip install git+https://github.com/instabot-py/instabot.py
```
**Configuration** ⚙️

Run `instabot-py --create-config` command and a default configuration will be created in your current directory: `instabot.config.yml`. It should be modified according the needs.
You can also run the bot with a different configuration file using `-c` flag: `instabot-py -c myconfiguration.yml`

**Start the bot** 🏁

  - `instabot-py` or `python3 -m instabot_py`
  - `instabot-py -c myconfiguration.yml` or `python3 -m instabot_py -c myconfiguration.yml`


The `%username%.db` file contains records of posts the bot has liked, and the users who has been followed/unfollowed.

The `%username%.session` file stores your session with Instagram to avoid re-logins each time you start the bot.

## Upgrade ⬆️

- `python3 -m pip install instabot-py --no-cache-dir --upgrade`
- `pip3 install instabot-py --no-cache-dir --upgrade`


## Parameters
| Parameter            | Type|                Description                           |        Default value             |
|:--------------------:|:---:|:----------------------------------------------------:|:--------------------------------:|
| login                | str | Your instagram username                              |      |
| password             | str | Your instagram password                              |      |
| start\_at\_h         | int | Start program at the hour                            | 0    |
| start\_at\_m         | int | Start program at the min                             | 0    |
| end\_at\_h           | int | End program at the hour                              | 23   |
| end\_at\_m           | int | End program at the min                               | 59   |
| database             | dict| Contains the database configuration                  | {"type": "sql", "connection_string": "sqlite:///{{login}}.db"}   |
| session\_file        | str | change the name of session file so to avoid having to login every time. Set False to disable. | "username.session"   |
| user_agent           | str | Custom User Agent to look like a real browser        | None |
| like_per_day         | int | DEPRECATED, WILL BE REMOVED SOON, REPLACED BY like_per_run |  |
| like_per_run         | int | Number of photos to like per day (over 1000 may cause throttling) | 296 |
| like_followers_per_run | int | Number of your old followers to like their last photo per day (set to 0 to disable) | 0 |
| media_max_like       | int | Maximum number of likes on photos to like (set to 0 to disable) | 0    |
| media_min_like       | int | Minimum number of likes on photos to like (set to 0 to disable) | 0    |
| follow_per_day       | int | DEPRECATED, WILL BE REMOVED SOON, REPLACED BY follow_per_run                              | 0    |
| follow_per_run       | int | Users to follow per day                              | 156    |
| follow_time          | int | Seconds to wait before unfollowing                   | 5 * 60 * 60 |
| follow_attempts      | int | Attempts to make to follow someone                   | 10 |
| user_min_follow      | int | Check user before following them if they have X minimum of followers. Set 0 to disable                   | 0 |
| user_max_follow      | int | Check user before following them if they have X maximum of followers. Set 0 to disable                   | 0 |
| follow_time_enabled  | bool| REMOVED, TO DISBALE Follow_time, just set it to 0  | -- |
| unfollow_per_day     | int | DEPRECATED, WILL BE REMOVED SOON, REPLACED BY unfollow_per_run                            | 0    |
| unfollow_per_run     | int | Users to unfollow per day                            | 199    |
| unfollow_recent_feed | bool| If enabled, will populate database with users from recent feed and unfollow if they meet the conditions. Disable if you only want the bot to unfollow people it has previously followed. | True |
| unlike_per_day     | int | DEPRECATED, WILL BE REMOVED SOON, REPLACED BY unlike_per_run                          | 0    |
| unlike_per_run     | int | Number of media to unlike that the bot has previously liked. Set to 0 to disable.                           | 0    |
| time_till_unlike     | int | How long to wait after liking media before unliking them. | 3 * 24 * 60 * 60 (3 days) |
| comments_per_day     | int | Comments to post per day                             | 0    |
| comment_list         | [[str]] | List of word lists for comment generation. @username@ will be replaced by the media owner's username     | [['this', 'your'], ['photo', 'picture', 'pic', 'shot'], ['is', 'looks', 'is really'], ['great', 'super', 'good'], ['.', '...', '!', '!!']] |
| tag_list             | [str] | Tags to use for finding posts by hasthag or location(l:locationid from e.g. https://www.instagram.com/explore/locations/212999109/los-angeles-california/)                     | ['cat', 'car', 'dog', 'l:212999109'] |
| keywords             | [str] | Words to use for finding profiles with username or biography contain these words | [] |
| tag_blacklist        | [str] | Tags to ignore when liking posts                   | [] |
| user_blacklist       | {str: str} | Users whose posts to ignore. Example: `{"username": "", "username2": ""}` type only the key and leave value empty -- it will be populated with userids on startup.                | {} |
| max_like_for_one_tag | int | How many media of a given tag to like at once (out of 21) | 5 |
| unfollow_break_min   | int | Minimum seconds to break between unfollows           | 15 |
| unfollow_break_max   | int | Maximum seconds to break between unfollows           | 30 |
| log_mod              | int | Logging target (0 log to console, 1 log to file, 2 no log.) | 0 |
| proxies              | dict | Access instagram through a proxy. {"http_proxy":"http://IP:PORT", "https_proxy":"http://IP:PORT"} (host:port or user:password@host:port) | |
| unfollow_not_following   | bool | Unfollow Condition: Unfollow those who do not follow you back | True |
| unfollow_inactive   | bool | Unfollow Condition: Unfollow those who have not posted in a while (inactive) | True |
| unfollow_probably_fake  | bool | Unfollow Condition: Unfollow accounts which skewed follow/follower ratio (probably fake) | True |
| unfollow_selebgram  | bool | Unfollow Condition: Unfollow (celebrity) accounts with too many followers and not enough following | False |
| unfollow_everyone  | bool | Unfollow Condition: Will unfollow everyone in unfollow queue (wildcard condition) | False |

## Contributing
Please feel free to contribute and submit PR requests. All help is appreciated. Look for issues with the label [needs help](https://github.com/instabot-py/instabot.py/labels/needs%20help). If you want to be in developer team, please email me.

## Instabot with yaml config
By default, instabot looks for the configuration file `instabot.config.yml`.
 It could be changed by exporting environment variable with the full path:
````bash
export INSTABOT_CONFIG_FILE=/path/to/file/instabot2.config.yml
````


```yaml

---
login : "username"
password : "password"
debug: 1
#Send INFO notification to Telegram channel 
logging.handlers.telegram:
  level: INFO
  class: telegram_handler.TelegramHandler
  token: __YOUR__CHANNEL__TOKEN__
  chat_id: __CHAT_ID__
logging.loggers.InstaBot.handlers:
  - telegram
  - console
```

[Create Telegram bot for instabot](https://core.telegram.org/bots#3-how-do-i-create-a-bot)

## Community

- [Telegram Group](https://t.me/joinchat/DYKH-0G_8hsDDoN_iE8ZlA)

