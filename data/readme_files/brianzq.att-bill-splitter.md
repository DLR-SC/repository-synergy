**THIS PROJECT IS NO LONGER MAINTAINED!**

My original goal with this project was to automate the whole process of splitting AT&T family plan bills including the login, parsing, storage and SMS notification to each line, which now I found not realistic or maintainable because AT&T was updating their login process or bill format every few months. With this learning, now I use a hybrid approach which requires me to manually login, download the pdf bills, and copy some of the line items into a txt file, which is then parsed by a python script. Despite some manual effort, the total process takes less then 2 mins and I never have to update the script since it was first written more than a year ago.

I used a private repo for the new script so that I could upload all the raw and parsed data there. Drop me a line if you want to give it a try.

att-bill-splitter
=================

Are you an AT&T account holder for multiple wireless lines and tired of manually splitting the bill, typing into spreadsheet and sending each of your user text message every month? Now you can automate all of that with this application.

Overview
--------

This package is written in Python (works with both Python 2 and 3) and uses requests and beautifulsoup4 to login your AT&T account and parse the bills. peewee is used as the ORM and data are stored in a Sqlite database. Command line interface is built with click. It also has twilio integration to send auto-generated monthly billing details to each user.

Installation
------------

via pip
~~~~~~~
::

    [~] pip install att-bill-splitter


via source code
~~~~~~~~~~~~~~~
::

    [~] git clone https://github.com/brianzq/att-bill-splitter.git
    [~] cd att-bill-splitter
    [att-bill-splitter] pip install .

*I recommend using a virtualenv to isolate all the dependencies of this application from your local packages.*

Quick Start
-----------

Parse And Split Bills
~~~~~~~~~~~~~~~~~~~~~
This is the first thing you run. You will be prompted to input your AT&T username and password (within terminal). Once logged in, it will start parsing your previous bills, splitting them and storing data to database.
::

    [att-bill-splitter] att-split-bill

For example
::

    [att-bill-splitter] att-split-bill
    👤  AT&T Username: your_att_username
    🗝  AT&T Password:
    ▶  Login started...
    ✅  Login succeeded.
    🏃  Start splitting bill Sep 15 - Oct 14, 2016...
    🏁  Finished splitting bill Sep 15 - Oct 14, 2016.
    🏃  Start splitting bill Aug 15 - Sep 14, 2016...
    🏁  Finished splitting bill Aug 15 - Sep 14, 2016.
    🏃  Start splitting bill Jul 15 - Aug 14, 2016...
    🏁  Finished splitting bill Jul 15 - Aug 14, 2016.
    🏃  Start splitting bill Jun 15 - Jul 14, 2016...
    🏁  Finished splitting bill Jun 15 - Jul 14, 2016.
    🏃  Start splitting bill May 15 - Jun 14, 2016...
    🏁  Finished splitting bill May 15 - Jun 14, 2016.
    🏃  Start splitting bill Apr 15 - May 14, 2016...
    🏁  Finished splitting bill Apr 15 - May 14, 2016.

By default it parses all your previous bills. If you want to select a few bills to parse, you can use ``-l`` option. The value of the option is the lag of the bill compared to the most recent one. So ``0`` refers to the most recent bill, ``1`` is one month before that and so on. For example,
::

    [att-bill-splitter] att-split-bill -l 0
    👤  AT&T Username: your_att_username
    🗝  AT&T Password:
    ▶  Login started...
    ✅  Login succeeded.
    🏃  Start splitting bill Sep 15 - Oct 14, 2016...
    🏁  Finished splitting bill Sep 15 - Oct 14, 2016.

You can supply multiple ``-l`` options at once.

**NOTE**: If your users overused your plan's data, you will probably get charged $15 for each additional Gigabyte like I do. When that happens, the charges for the additional data usage are split among user who used more than their monthly share (monthly_total_allowance / number_of_user), proportionally to the extra amount used. The details will be printed when you run above command, like this:

::

    [att-bill-splitter] att-split-bill -l 0
    👤  AT&T Username: your_att_username
    🗝  AT&T Password:
    ▶  Login started...
    ✅  Login succeeded.
    🏃  Start splitting bill Sep 15 - Oct 14, 2016...
    User USER_NAME_1 over used 0.1 GB data, will be charged extra $0.68
    User USER_NAME_3 over used 0.69 GB data, will be charged extra $4.70
    User USER_NAME_4 over used 0.3 GB data, will be charged extra $2.06
    User USER_NAME_7 over used 3.31 GB data, will be charged extra $22.57
    🏁  Finished splitting bill Sep 15 - Oct 14, 2016.

View Monthly Charges Summary for Users
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
After you parsed the bills, you can view them in your terminal. The command below will print the monthly summary for each user.
::

    [att-bill-splitter] att-print-summary MONTH [year]

``MONTH`` (1-12) refers to the month of the end date of the billing cycle. For example if you want to view billing cycle is Sep 15 - Oct 14, ``MONTH`` should be ``10``. ``year`` (optional) should be 4-digit. For example,
::

    [att-bill-splitter] att-print-summary 8

    --------------------------------------------------------------
        Charge Summary for Billing Cycle Jul 15 - Aug 14, 2016
    --------------------------------------------------------------
           USER_NAME_1     (415-555-0001)      Total: 72.99
           USER_NAME_3     (415-555-0003)      Total: 62.67
           USER_NAME_4     (415-555-0004)      Total: 31.42
           USER_NAME_5     (415-555-0005)      Total: 31.42
           USER_NAME_6     (415-555-0006)      Total: 72.99
           USER_NAME_7     (415-555-0007)      Total: 32.42
           USER_NAME_8     (415-555-0008)      Total: 31.42
           USER_NAME_9     (415-555-0009)      Total: 61.42
    --------------------------------------------------------------
                                     Wireless Total: 444.52

View Monthly Charges Details for Users
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can also view itemized charge details for each user.
::

    [att-bill-splitter] att-print-details MONTH [year]

``MONTH`` (1-12) refers to the month of the end date of the billing cycle. For example if you want to view billing cycle is Sep 15 - Oct 14, ``MONTH`` should be ``10``. ``year`` (optional) should be 4-digit.

For example,
::

    [att-bill-splitter] att-print-details 8 -y 2016

        USER_NAME_1 (415-555-0001)
          - Monthly Charges                            15.00
          - Equipment Charges                          42.50
          - Surcharges & Fees                          2.69
          - Government Fees & Taxes                    2.66
          - Account Monthly Charges Share              10.14
          - Total                                      72.99

        USER_NAME_2 (415-555-0002)
          - Monthly Charges                            15.00
          - Equipment Charges                          37.50
          - Surcharges & Fees                          2.69
          - Government Fees & Taxes                    1.92
          - Account Monthly Charges Share              10.14
          - Total                                      67.25
      ...

Send Monthly Charge Details to Users via SMS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

View each user's monthly charge details (and total) and decide if you want to send it to the user via SMS.

During your first use, you will be prompted to input your Twilio number, account SID and authentication token. You can get them in a minute for free at www.twilio.com. You will also be asked to input a short message to put at the end of the text messages you send to your users, for instance, to tell your users how to pay you. All the info will be saved locally so you don't have to type them in the future, unless you want to update them.
::

    [att-bill-splitter] att-notify-users MONTH [YEAR]

``MONTH`` (1-12) refers to the month of the end date of the billing cycle. For example if you want to view billing cycle is Sep 15 - Oct 14, ``MONTH`` should be ``10``. ``YEAR`` (optional) should be 4-digit.

For example,
::

    [att-bill-splitter]  att-notify-users 8 --year 2016
    Twilio Number (e.g. +11234567890): your_twilio_number
    Twilio Account SID: your_account_sid
    Twilio Authentication Token: your_auth_token
    ✅  Twilio account added.
    You can enter a short message to put after the charge details to send to your users. (For example, letting your users know how to pay you)
    -> Please Venmo me at Brianz56.
    ✅  Payment message saved.

    415-555-0001
    Hi USER_NAME_1 (415-555-0001),
    Your AT&T Wireless Charges for Jul 15 - Aug 14, 2016:
      - Monthly Charges                15.00
      - Equipment Charges              42.50
      - Surcharges & Fees              2.69
      - Government Fees & Taxes        2.66
      - Account Monthly Charges Share  10.14
      - Total                          72.99 🤑

    Notify (y/n)?

If you type ``y``, it will call Twilio API to send the message to user 1 @ 415-555-0001 with the extra payment message you inputed upfront. At the mean time, all messages sent are logged in ``notif_history.log`` file in ``att-bill-splitter`` directory to help you manage all the history activities.

I'd like to hear your thoughts. You can `join our slack channel <https://join.slack.com/t/att-bill-splitter/shared_invite/enQtMjk5Mzc4NTQ4ODY5LWRmMWQzYjM2MWFmYzE1NjY1N2MzOTkyZGJhNDMzNGJjOWFhNzI4OTRkZTg4MmM3YzY0YzMwODMxZTI4NGYzZDI>`_ if you have any questions or just want to say hi.
