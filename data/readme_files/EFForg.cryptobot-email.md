![CryptoBot](/doc/images/cryptobot-large.png)

CryptoBot Email is an email bot that helps people learn how to use OpenPGP. You send CryptoBot a PGP-encrypted and signed email (probably using GnuPG) and it responds telling you how you do, and offering advice.

## Getting Started

Start by copying `config_template.py` into `config.py` and editing it.

    $ cp config_template.py config.py

Set all of these settings:

- `PGP_NAME`: The name part of the user ID for for the bot's OpenPGP keypair
- `PGP_EMAIL`: The email part of the user ID for for the bot's OpenPGP keypair. This should be the email address that users are expected to email.
- `GPG_HOMEDIR`: The directory in which the bot's keyring will be stored (it will be created by the bot if it does not exist). This should be in a location that is writeable by the bot.
- `USE_MAILDIR`: You can either use a Maildir or IMAP; set to False to use IMAP
- `MAILDIR`: If you're using a Maildir, this is the path to it
- `IMAP_SERVER`: The IMAP server to connect to, e.g. `imap.gmail.com`
- `IMAP_USERNAME`: The IMAP username
- `IMAP_PASSWORD`: The IMAP password
- `SMTP_SERVER`: The SMTP server to connect to, e.g. `smtp.gmail.com`
- `SMTP_USERNAME`: The SMTP username
- `SMTP_PASSWORD`: The SMTP password
- `DATABASE_URL`: URL for the unsubscribe database


This is a Python project with some external dependencies. We recommend using
virtualenv:

    $ virtualenv env
    $ . env/bin/activate
    (env) $ pip install -r requirements.txt
    (env) $ ./bot.py
    # when you're done
    (env) $ deactivate


## Unsubscribes

To avoid exploitation as an automated spam cannon, cryptobot can optionally
maintain a database of unsubscribers. It requires one additional setup step.
After installing requirements, uncomment the DATABASE_URL in config.py, and
run

```
./unsubscribe.py --setup
```

This will create the necessary database tables and generate a random salt for
hashing email addresses. Once that's done, you can add emails to the database
by running

```
./unsubscribe.py --add foo@example.com

```

Alternatively you can run the included Flask app to serve a simple unsubscribe
form for people to unsubscribe themselves.

```
./app.py    # http://localhost:5000/unsubscribe
```

For simplicity, you can use an sqlite database, which is created as a normal
file in the directory of your choosing, and does not incur any extra
dependencies. However, for better concurrency handling, you may want to install
and use postgresql, which will require the psycopg2 python module along with
some additional system configuration:

```
sudo apt-get install postgresql
sudo -u postgres createuser -P -s -e cryptobot
createdb cryptobot -O cryptobot
sudo apt-get install postgresql-server-dev-9.1
. env/bin/activate
pip install psycopg
deactivate
```


## Dev Notes

On linux systems: if you get an error while trying to install requirements.txt, like "fatal error: Python.h: No such file or directory"
    $ sudo apt-get install python-dev

To run the tests:

    $ ./test.py

By default, the tests skip key generation, which can be slow and use up
entropy. To include these tests, run:

    $ ./test.py --slow

Relevant specs:

* [RFC 4880 - OpenPGP Message Format](http://tools.ietf.org/html/rfc4880)
* [RFC 2045 - Multipurpose Internet Mail Extensions (MIME)](http://tools.ietf.org/html/rfc2045)
* [RFC 3156 - MIME Security with OpenPGP](http://tools.ietf.org/html/rfc3156)
