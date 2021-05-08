# pastebin_scraper
## Automated tool to monitor pastebin for interesting information
### Originally created by Jordan Wright
### Modified by Moez Janmohammad [@wedemmoez](http://www.twitter.com/wedemmoez)


For more overview, check out the blog post [here.](https://www.criticalstart.com/automated-tool-to-monitor-pastebin-for-interesting-information/)

This tool was heavily influenced by [dumpmon](http://www.github.com/jordan-wright/dumpmon). Since that bot is no longer active (as of October 7, 2018), Critical Start - Section 8 has set up our own to continue to monitor Pastebin for data leaks and dumps. In modifying dumpmon, we've also made changes and added features, listed below. 


## Changes made
* updated tool to use Python3 since Python2 will be deprecated in 2020
    * changing print statements
    * updated modified Queue library
    * added line to __init__.py to allow fix relative imports.
* removed slexy/pastie sites because they are no longer active
* removed all twitter components, this is not a feature we needed or will use
    * changed references to 'tweet' since we aren't tweeting
* changed logging
    * logs when interesting pastes are found, and what type
    * logs to both stdout and output.log files
* now uses Pastebin API instead of /archive page
    * now our IP won't be blacklisted
    * REQUIRES PASTEBIN PRO ACCOUNT
* removed redundant code in lib/Site.py and lib/(paste sites).py
* changed mongodb to MySQL 

## Quickstart Guide
To get up and running quickly with pastebin_scraper, do the following once you have cloned this repository:

        * cd pastebin_scraper
        * pip3 install -r requirements.txt
        * cp settings_example.py settings.py
        * python3 pastebin_scraper.py

## Setting up MySQL support
1. Set up a MySQL database with whatever name you want, add a user with write permissions for that db for the bot.
2. Use this command to create the table with the correct attributes:

    > create table pastes (pid char(10), text longblob, emails longblob, hashes longblob, num_emails int, num_hashes int, type char(10), db_keywords float, url char(60), author char(30));

This creates a table named *pastes* with the following attributes:

column name | [data type]
------------ | -------------
PID | [char(10)]
text | [longblob]
emails | [longblob]
hashes | [longblob]
num_emails | [int]
num_hashes | [int]
type | [char(10)]
db_keywords |[float]
URL | [varchar(60)]
Author | [char(30)]
3. rename settings_example.py to settings.py and update with the proper attributes
    pastebin_scraper can save pastes using MySQL.

        USE_DB = True

        DB_HOST = 'localhost' (or whatever the server IP is)

        DB_PORT = 3306

        DB_USER = 'pastebin_scraper' (generate your own user/pass)
        
        DB_PASS = 'botpassword'

        DB_DB = 'paste_db'

If you do not want to save pastes, set USE_DB to False

## Executing pastebin_scraper (REQUIRES PASTEBIN PRO ACCOUNT)
        python3 pastebin_scraper.py

## Disclaimer
This script was developed for educational purposes only. Critical Start is not responsible for any malicious use of the data collected by it. Moral of the story... don't do anything dumb.

## TO DO
* split emails and associated passwords up and save separately
* create script to automate database and table creation
* search for other hash types
* some type of statistics tracking or daily email? 
