# slashgif

The missing GIF Twitter bot. Simply tag [@slashgif](https://twitter.com/slashgif) in your tweet with a search term.

[![](http://i.imgur.com/kL8IWnz.png)](https://twitter.com/slashgif/status/630542797456609280)

### Where is this bot running?

Currently I'm running this bot on a 1GB [DigitalOcean](https://www.digitalocean.com/?refcode=422889a8186d) instance (yes, that's an affiliate link. Use that to get a free VPS for 2 months). The bot is not resource-intensive and uses a couple dozen MBs of RAM.

## Running

#### Requirements

- Python 3.4
- pip3
- sqlite3

#### Instructions 

Create a file called `config.py` that looks like `config_example.py`. Fill in the necessary values.

For Twitter config:

1. Register your app
2. Get your app's key and secret.
3. Create token and get the token and secret.
4. Get a Giphy API key.

Then, to run the bot:

```bash
$ pip3 install -r requirements.txt
$ python3 bot.py
```

## License 

Apache 2.0
