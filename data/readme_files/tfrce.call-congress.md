Call Congress
==============

A simple flask server that connects calls between citizens and their congress person using the Twilio API.


The server handles two cases:

* A phone call made to the campaign number
* A web-initiated call to connect a user's phone number to congress
    * can specify congress person(s) in the api call
    * can have the user punch in their zip code and look up their congressional members

### Incoming phone calls
Each new campaign's Twilio phone number needs to be [configured](http://twilio.com/user/account/phone-numbers/incoming) to point to:

    /incoming_call?campaignId=abc-1234

The user will be prompted to punch in their zip code, the server will locate their members of congress using the [Sunlight Labs locate data](http://sunlightlabs.github.io/congress/index.html#bulk-data/zip-codes-to-congressional-districts), and dial them.

### Web-initiated connection calls
These calls are made from a web form where the user enters their phone number to be connected to Congress (will be prompted for zip code):

    /create?campaignId=abc-123&userPhone=1234567890

or a specific member of congress:

    /create?campaignId=abc-123&userPhone=1234567890&repIds=P000197

or to member(s) based on zip code:

    /create?campaignId=abc-123&userPhone=1234567890&zipcode=98102

Required Params:
 
* **userPhone**
* **campaignId**

Optional Params: *(either or)*

* **zipcode**
* **repIds**: identifiers (can be more than one) from the Sunlight API's [**bioguide_id**](http://sunlightlabs.github.io/congress/legislators.html#fields/identifiers) field


Campaign Configuration
----------------------
Currently stored in ``/data/campaigns.yaml``, each campaign has the following optional fields. Defaults are given by the ``default`` campaign.

* **id**
* **number** (Twilio phone number)
* **target_house** include house members in lookups by location
* **target_senate** include senators in lookups by location
* **target_house_first** allows the campaign to target house members before senate members (default: target senate first)
* **repIds** (optional) list of rep. IDs to target
* **randomize_order** (optional, default false) randomize the order of the phone calls
* **overrides_google_spreadsheet_id** (optional) ID of publicly published Google Spreadsheet which can override the default campaign behaviors on a per-state basis (see [**section below**](#overriding-the-default-behaviors-with-a-google-spreadsheet))
* **skip_star_confirm** (optional, default false) Whether to skip the "press star to confirm" step for campaigns which don't gather zipcode
* **call_human_check** (optional, default false) Whether to check the recipient is not an answering machine. Note, will add a 3 second delay before your call begins.

Messages: Can be urls for recorded message to play or text for the robot to read. Text can be rendered as a mustache template. The following messages are the defaults and will be inherited by new campaigns unless overwritten.

* msg_intro: Hi. Welcome to call congress.
* msg_ask_zip: Please enter your zip code so we can lookup your Congress person.
* msg_invalid_zip: "Sorry, that zip code didn't work. Please try again."
* msg_call_block_intro: "We'll now connect you to {{n_reps}} representatives. Press # for next rep."
* msg_rep_intro: "We're now connecting you to {{name}}"
* msg_special_call_intro: Optional: if an extra first call number is specified in the remote Google Spreadsheet, this text can be used to introduce the extra call. It's optional, and if not specified, we'll fall back to _msg_rep_intro_.
* msg_between_thanks: You're doing great - here's the next call.
* msg_final_thanks: Thank you!


Overriding the default behaviors with a Google Spreadsheet
----------------------------------------------------------
Using the optional _overrides_google_spreadsheet_id_, each campaign can specify
a remote Google Spreadsheet to pull in for state-specific overrides. This allows
you to change the campaign's default behaviors on a per-state basis. Currently
the following features are supported:

* Change the order priority of the calls (House vs. Senate)
* Always call a particular legislator first (specified by last name)
* Call an arbitrary name/number before connecting to Congress. For example, you
  could use this to call a specific public-works department for a given state.

To get an idea of how this works, [**see this example spreadsheet.**](https://docs.google.com/spreadsheets/d/1SxJWmzjNAnpkcKrMDbbnUJjx4qBX6vsF5MiyOXwf-NM/edit?usp=sharing)

Specifically, the Google Spreadsheet must be public, and published (note the
distinction) and the first row must contain column labels in bold-faced and with
exactly the precise text as specified here:

1. **State**
2. **Target Senate**
3. **Target House**
4. **Target House First**
5. **Optional Target Individual first (lastname)**
6. **Optional Extra First Call Name**
7. **Optional Extra First Call Number**


Account Keys
------------

The app uses environment variables to store account keys. For development you will need to set:

* SUNLIGHTLABS_KEY
* TWILIO_DEV_ACCOUNT_SID
* TWILIO_DEV_AUTH_TOKEN
* TW_NUMBER
* REDISTOGO_URL (optional Redis URL for caching the Google Spreadsheet data)

and for production:

* SUNLIGHTLABS_KEY
* TWILIO_ACCOUNT_SID
* TWILIO_AUTH_TOKEN
* APPLICATION_ROOT (url for application server)
* TASKFORCE_KEY (used for querying statistics)

Development mode
-------------------
To install locally and run in debug mode use:

    # create ENV variables
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

    python app.py
    # for testing twilio, need internet-visible urls to do call handling
    ngrok -subdomain="1cf55a5a" 5000

When the dev server is running, the demo front-end will be accessible at [http://localhost:5000/demo](http://localhost:5000/demo).

Unit tests can also be run, using:

    python test_server.py

Production server
------------------
To run in production:

    # create ENV variables
    # open correct port
    iptables -A INPUT -p tcp --dport 80 -j ACCEPT
    # initialize the database
    python models.py
    # run server - will charge real $ and connect real calls
    foreman start

Updating for changes in congress
--------------------------------
Just download the latest data from Sunlight Congress API using:

    cd data && make -B
    git commit data/districts.csv data/legislators.csv
