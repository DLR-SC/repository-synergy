## THE SNIPER REPO HAS MOVED TO https://github.com/Rui-Zhang1997/sniper

# Introduction

[Sniper](http://sniper.rutgers.io) is an application that interfaces with the [Rutgers Schedule of Classes](http://sis.rutgers.edu/soc/) and notifies users via email/text when a course opens up.

It uses 
* [Flask](http://flask.pocoo.org) for the application framework
* [SQLAlchemy](http://www.sqlalchemy.org/) for ORM
* [Requests](http://docs.python-requests.org/en/latest/index.html) for interfacing with the Rutgers Schedule of Classes.
* [SendGrid](https://sendgrid.com) for email notifications.

You can check out the [live version](http://sniper.rutgers.io) if you want to simply use its functionality

# Installation

You can setup an instance of sniper on your own Linux machine.

1. Start by setting up a [python virtualenv](http://lmgtfy.com/?q=setting+up+a+python+virtualenv)
2. Install the python packages in `requirements.txt` by running `pip install -r requirements.txt`.
3. Create a `db/` directory in the `sniper` folder (alongside `app.py`).
4. Create empty database tables by running `python -c "from models import db; db.create_all()"`
5. Copy `secrets-example.py` to `secrets.py`. Edit the mail_username and mail_password fields to your SendGrid account details (if you want sniper to send you email).
6. Run app.py `python app.py`. You should be able to visit `http://localhost:5000/` and input a class to snipe.

When you input a snipe, you should see it under `db/production.db` in the user and snipe tables.

If you run cron.py (`python cron.py`), all the courses in the database will be checked and the corresponding users will be notified if the class is open.
You can run cron.py in a cronjob to automatically check for course openings. 

Example: Put ` */15 * * * * /path/to/virtualenv/bin/python cron.py ` into `crontab -e` to automatically check for openings every 15 minutes.
