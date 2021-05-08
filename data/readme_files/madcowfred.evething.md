 EVEthing
=========
EVEthing is a terribly named web application intended to ease the pain
of managing your [EVE Online](http://www.eveonline.com/) space empire.

Features
--------
- Handles all types of API key: account, character and corporation.
- Only crashes occasionally, honest.
- More than likely won't set your hard drive on fire.
- Home page: displays relevant information about all API keys attached
  to your account.
  [Screenshot](https://github.com/madcowfred/evething/raw/develop/doc-images/home.png).
  * Character name, wallet balance, API key 'name' (in brackets) and total SP easily visible. 
  * If the account is training, shows training skill, time remaining and training speed.
    Red completion bars have free room in the skill queue.
  * Red boxes highlight accounts with no characters in training.
  * Notification icons appear at the bottom of each character box and have basic tooltips,
    you can see the current types in the screenshot.
  * Wallet balances for any corporation keys are displayed underneath.
- Character page: displays character information similar to the
  in-game character sheet. If you've ever used
  [eveboard](http://eveboard.com) you should know what to expect.
  [Screenshot](https://github.com/madcowfred/evething/raw/develop/doc-images/character.png)
  (yes, that's me).
  * Basic info: portrait, corporation, wallet
    balance, total SP, clone limit, attributes and implants. 
  * Skill queue.
  * Filled stars for trained levels, hollow stars for
    partially trained levels, weird heart icons for level V skills.
  * Full control over public visibility of character and of each
    component. If you're not logged in to the account that owns a
    character you will only see what the owner says you can see, or a
    404 error if they choose to not be public.
  * Anonymous character support, accessed via a /character\_anon/blah URL. Character name,
    corporation, wallet balance and implants are not shown and your
    portrait is replaced with a terrible placeholder image.
- API key management page: list keys, add keys, simple interface to
  generate a new key with a feature set.
  [Screenshot](https://github.com/madcowfred/evething/raw/develop/doc-images/apikeys.png)
- Assets page: lists assets for all characters with the relevant API
  mask. Includes ship and container names with the Locations mask.
  Filtering is somewhat limited and search is non-existent but the
  basic functionality is in and working.
  [Screenshot](https://github.com/madcowfred/evething/raw/develop/doc-images/assets.png)
- Blueprints page: lets you add/delete/edit/view blueprints you have
  added to the system.
  [Screenshot](https://github.com/madcowfred/evething/raw/develop/doc-images/blueprints.png)
  * See useful information at a glance for every blueprint you own
    (assuming you could be bothered entering them all).
  * Mark a selection of blueprints to use with BPCalc.
- BPCalc page: displays detailed production information and allows you
  to filter based on things.
  [Screenshot](https://github.com/madcowfred/evething/raw/develop/doc-images/bpcalc.png)
  * Displays blueprints, total m3 of inputs/ouputs, expected profit
    values from both buys and sells, and estimated weekly volume.
  * Not particularly powerful filters on the data: 
    + Profit below a certain
  value
    + Movement above a certain value (so you don't make 300% of
  the weekly supply)
    + Limit slots to a certain value
    + Remove selected blueprints
  * Components table with IGB-clickable links for easy purchasing of items.
- Orders page: displays a summary of your market orders and a detailed
  list of all orders.
  [Screenshot](https://github.com/madcowfred/evething/raw/develop/doc-images/orders.png)
  * Summary table showing active order slots and total values involved.
  * Detailed active orders table listing all relevant information for each order, with
    clickable item names that lead to Transactions pages.
- Transactions page: displays a log of market transactions for all
  items or a specific item.
  [Screenshot](https://github.com/madcowfred/evething/raw/develop/doc-images/transactions.png)
  * All transactions page has clickable item links that lead to specific items.
- Trade page: displays a summary of all transactions by month and over
  specific 'Campaigns'.
  [Screenshot](https://github.com/madcowfred/evething/raw/develop/doc-images/trade.png)

Future Plans
------------
- Take over the universe.
- Skill plan creation.
- Industry Job tracking.
- CREST integration if CCP ever actually releases something.

Installation
------------
There are some common requirements for any install method, most of these
will be installed using pip in 'Common Install Steps' below:

- [Python](http://www.python.org) \>=2.7 <3.0
- [Django](http://www.djangoproject.com) \>=1.7 <1.8
- [Celery](http://docs.celeryproject.org/en/latest/) \>= 3.1 <3.2
  * This includes the celery[flavor] package that may be required for the
    [broker you choose](http://celery.readthedocs.org/en/latest/getting-started/first-steps-with-celery.html#choosing-a-broker). For example, if you wanted to use redis you would then run
    `pip install celery[redis]\<3.2`
- [Django MPTT](https://github.com/django-mptt/django-mptt/) \>=0.5
- [Coffin](https://github.com/coffin/coffin/) \>=0.3
- [Jinja2](http://jinja.pocoo.org/) \>=2.6
- A database server and relevant client library.
  - [SQLite](http://www.sqlite.org) is the simplest and is often included with Python.
  - [MySQL](http://www.mysql.com) is another option and highly likely to be available on shared
    hosting. You will need the [MySQLdb](http://mysql-python.sourceforge.net/MySQLdb.html) 
    client library, `pip install mysql-python`.
  - [PostgreSQL](http://www.postgresql.org) is the last option and would be my choice. You will
    need the [psycopg](http://initd.org/psycopg/) client library, `pip install psycopg2`.
- The current EVE Static Data Export imported into a database. The recommended course is to 
  get the SQLite conversion from [fuzzwork](http://www.fuzzwork.co.uk/dump/) and use that as
  your 'import' database. If you can't do that, [zofu](http://zofu.no-ip.de/) has MySQL and
  Postgres versions that take a long, long time to import.

Common Install Steps
--------------------
1.  Make a new virtualenv: `python virtualenv.py thingenv`.
2.  Activate the virtualenv: `cd thingenv`, `source bin/activate`.
3.  Clone the EVEthing git repository:
    `git clone -b develop git://github.com/madcowfred/evething.git`.
4.  Install the required libraries using pip: `cd evething`,
    `pip install -r requirements.txt`.
5.  Copy evething/local\_settings.example to evething/local\_settings.py
    then open local\_settings.py in some sort of text editor and edit
    settings.
6.  `python manage.py syncdb`, say NO when it asks if you would like to
    create an admin user.
7.  `python manage.py migrate --all`, this will apply database
    migrations in order.
8.  `python manage.py createsuperuser` to create a new superuser.
9. `python import.py` to import the initial data from the SDE database.

If you update EVEthing in the future, make sure to run
`python manage.py migrate thing` to apply any database schema changes!

Common Post-install Steps
-------------------------
1.  LEAVE DEBUG ENABLED FOR NOW - it will spit out tracebacks that
    should help you track down any problems.
2.  Log in as the superuser you created earlier.
3.  Click the username dropdown in the top right and head to Account
    Management.
4.  Add one or more API keys.

Celery Worker Setup
-------------------

This is my third take on the API update process. v1 was api\_updater.py
with a single thread, this worked relatively well for small numbers of
keys but broke badly under load. v2 was api\_updater.py with multiple
threads. After a lot of messing about with exciting threading bugs, I
gave up and learned about the wonders of
[Celery](http://celery.readthedocs.org/en/latest/index.html).

EVEthing will presently place jobs in 3 queues:
- et_high: internal tasks such as spawning jobs, cleaning up the API cache, resetting 
  'broken' tasks.
- et_low: low priority tasks, only APIKeyInfo calls right now.
- et_medium: everything else.

There are a few possible ways to run the workers:
- Single worker group (development, small installations):  
    `celery worker -A evething -B -Q et_high,et_medium,et_low -c 2`
- Two worker groups (medium installations):  
    `celery worker -A evething -B -Q et_high -c 1`  
     `celery worker -A evething -Q et_medium,et_low -c 4`
  - This has been fine with up to 300 keys so far.
- Three worker groups (large installations):  
    `celery worker -A evething -B -Q et_high -c 1`  
     `celery worker -A evething -B -Q et_low -c 1`  
     `celery worker -A evething -B -Q et_medium -c 5`
  - This keeps up with the 1070 key GoonFleet hosted version.

Local Install
-------------

This is for messing about with EVEthing and seeing what the hell it
does, never use this for a publicly accessible site (see: [Django
docs](https://docs.djangoproject.com/en/dev/ref/django-admin/#runserver-port-or-address-port)).

1.  `python manage.py runserver ip:port`.
2.  Open [http://ip:port/](http://ip:port/) in a web browser.

Apache Install
--------------

You will need to install Apache and [mod_wsgi](http://code.google.com/p/modwsgi/).

1. Make a directory somewhere to act as the site root. Do NOT use the same directory you placed the EVEthing
   files earlier.
2. Make a 'static' sub-directory inside this directory.
3. Add a vhost to your Apache config with these extra directives:
   ```apache
  Alias /static/ /www/whatever/static/

  <Directory /www/whatever>
      Order allow,deny
      Allow from all
  </Directory>

  WSGIDaemonProcess evething threads=2 user=nobody python-path=/path/to/evething:/path/to/virtualenv/lib/python2.7/site-packages
  WSGIProcessGroup evething

  WSGIScriptAlias / /path/to/evething/evething/wsgi.py

  <Directory /path/to/evething>
      <Files wsgi.py>
          Order allow,deny
          Allow from all
     </Files>
  </Directory>
   ```
4. Reload Apache config.
5. Run `python manage.py collectstatic`, answer 'yes'.
6. Open <http://whatever/> in a web browser.
7. To force an EVEthing reload later (updated code or changed config)
   run `touch evething/wsgi.py` in the EVEthing directory.
