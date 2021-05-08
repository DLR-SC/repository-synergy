:Author: `Mike Levin SEO in NYC, Commodore & 360i alum, HitTail creator, J2 Global employee. <http://mikelev.in>`_

Pipulate Free & Open Source SEO Software (Automate GSheets for Dashboards)
##########################################################################

.. image:: https://raw.githubusercontent.com/miklevin/Pipulate/master/pipulate-logo.svg?sanitize=true

- Do you use Google Spreadsheets to make Data Dashboards for Business?
- Are you using expensive plug-ins or products to keep these Reports Updated?
- Would you rather not have to pay and have even more creativity and control?

Then It's Time To Learn a Little Python!
========================================

Pipulate is designed to make playing with data in Jupyter Notebook easy, and
set the stage for you to move your code over to cheap generic Linux servers for
automation. The easiest way to install Pipulate from Jupyter is to execute
these commands from within a Notebook::

    import sys
    !{sys.executable} -m pip install --upgrade --no-cache-dir pipulate

If you're not using Anaconda, then you will have to install Pandas first. But
you should really be using Anaconda. The idea is that you experiment in Jupyter
Notebook, which is a great learning environment and move your scripts as they
mature over to a more automated generic Linux server.

The first time you import Pipulate, you will receive a Google OAuth prompt to
allow access to the Google Spreadsheet you want to edit. Click the big link
and paste the resulting token back into the field shown in Jupyter Notebook or
your command-line. Once this is done, the basic use is::

    import pipulate
    pipulate.sheet('119mnC8Day78KexU_yv7J_wfA3p7iZeXa0YEtmg1Igu4')  # replace with yours
    cl, df = pipulate.pull(tab=0, rows='A1:J10')
    df.loc[:,:] = 'foo'
    pipulate.push(0, cl, df)

This loads the rectangular region you defined with the rows and columns into
memory in a way where you can treat it a lot like a tab in Microsoft Excel or
table in SQL. You can manipulate the pandas "DataFrame" (abbreviated as df),
and then push the changes back out to the Google Sheet. This is very
open-ended, designed to make automation of traditional tedious tasks in SEO
much simpler. Once you're happy with your script, you can copy/paste it into a
.py file and schedule it with a standard Linux scheduler, which is another part
of this project I'll be expanding considerably (generic task-scheduling under
Linux).

There is some flexibility in the API and ability to assign column labels from
row 1, allowing you to adapt to your style. Here are some variations::

    cl, df = pipulate.pull('Sheet1', rows='A1:J5')                # Most common usage
    cl, df = pipulate.pull('Sheet1', rows='A1:J5', columns=True)  # Turn row 1 into column labels
    cl, df = pipulate.pull(tab=0, rows='A1:J5')                   # Address tab by index
    cl, df = pipulate.pull(0, rows='A1:J5')                       # Address tab by index, no label
    cl, df = pipulate.pull(0, rows='A1:J')                        # Automatically figure out number of rows
    cl, df = pipulate.pull(0, rows=(1,5), cols=('A','J'))         # Use the rows=, cols= interface
    cl, df = pipulate.pull(0, (1,5), ('A','J'))                   # Use row, col interface, no labels
    cl, df = pipulate.pull(0, (1,5), (1,10))                      # Use row, col with numeric column index
    cl, df = pipulate.pull(2, rows='A1:J5')                       # Work on the 3rd tab.
    cl, df = pipulate.pull(wksht, rows='A1:J5')                   # Use GSpread Worksheet object

Using argument labels is optional. The exact string-name, 0-based numerical
index or a GSpread Worksheet object-type must be in the first position. The 2nd
position is the "rows" value, which may either be an Excel-like range or a
row-range. If a row-range then you must also have a col-range in position 3 (or
label the argument "cols"). The details of how you do it will vary with your
project. It is often useful to name your tabs so you can do different
manipulations to different tabs without worrying about changing their order in
the spreadsheet Web user interface.

If you don't give any column labels, Pipulate will assign them automatically
using the Excel-like letter-labels for columns. If you want to name your
column, you can either use row 1 by setting your columns parameter to true or
you can provide your own list of column names::

    cols = ['one', 'two', 'three', 'four', 'five']
    cl, df = pipulate.pull(tab=0, rows='A1:J5', columns=cols)  # Set columns labels from list

After you make your cl (GSpread cell_list) and df (pandas DataFrame) selection,
you can modify your df and push it back into Google Sheets with the symmetrical
populate command::

    pipulate.push(0, cl, df)  # Works in most cases

Real Life Example
=================

Say you have a spreadsheet with a list of URLs that were provided to you from
some unreliable source in column A starting from A1. You don't know whether it
should have a www at the beginning or if the protocol is correct::

    amazon.com
    apple.com
    google.com

And now let's say you write a simple function that will test what the real
homepage URL is. This example uses the popular "Requests" package for making
http requests::

    import requests

    def cleanurl(provided):
        guess = provided
        if provided[:4].lower() != 'http':
            guess = 'https://%s' % provided
        try:
            r = requests.head(guess, allow_redirects=True)
            resolved = r.url
        except:
            resolved = "Can't find %s" % provided
        return resolved

To use Pipulate and Pandas to apply this function to each line of column A, you
would first select columns A & B into a Pandas DataFrame::

    import pipulate
    pipulate.sheet('119mnC8Day78KexU_yv7J_wfA3p7iZeXa0YEtmg1Igu4')
    cl, df = pipulate.pull(tab=0, rows='A1:B3')

Then you apply the function to each cell in column A of your DataFrame and put
the results in column B and push the results back up into Google Sheets::

    df['B'] = df['A'].apply(cleanurl)
    pipulate.push(0, cl, df)

And that's it! Column B will now contain::

    https://www.apple.com/
    https://www.google.com/
    https://www.amazon.com/

Imagine the utility! I addition to working magic in Google Sheets, you're
acquiring incredibly useful Python Pandas skills!

Parametrizing Your Arguments for Scheduling
===========================================

The time has come the Walrus said to talk about automation. After you get your
script working in Jupyter Notebook what are you going to do? Unless you want to
sit there and press a button every day like in Lost, then you're going to have
to put the code in some sort of scheduling system. When you do this, it is best
to do it in a parameterized fashion, meaning you can feed the one script
different sites, Google Analytics IDs, keywords, filters and whatnot; allowing
the same code to drive different dashboards. 

Generic Linux script scheduling is too much to cover here, but I may as well
show you how to develop with parameterized arguments in Jupyter Notebook then
have those same arguments able to be used on the command-line when invoked from
scheduling. So if you have filename.ipynb (A Jupyter Notebook) and you
copy/paste its content into filename.py, then you can change its internal
variable values by the way you run it form the Unix shell, thereby using it to
drive many different Google Sheet dashboards. You're welcome::

    (py36) MikeL@LunderVand:$ filename.py --kung "foo"
    kung: foo

You can alternatively use::

    (py36) MikeL@LunderVand:$ filename.py -k "foo"
    kung: foo

To support more arguments, just make more of the parser.add_argument() function
calls and access them through the args dictionary. Here's the code in
filename.py in the above commands. When this is run from Jupyter Notebook, the
"foo" value is set in the "if jn:" if-block. It's fairly likely you'll have
code like this at the top of any Pipulate script that starts out in Jupyter
Notebook and is destined for scheduling. Clear? Enjoy!::

    name = 'kung'
    jn = True
    try:
        get_ipython()
    except NameError:
        jn = False
    if jn:
        val = 'foo'
    else:
        import argparse
        parser = argparse.ArgumentParser(description='Parses args when run from console.')
        parser.add_argument('-k','--kung', default='foo', help='', required=False)
        args = vars(parser.parse_args())
        val = args[name]
    print('%s: %s' % (name, val))

Fear Is The Mind Killer
=======================

Why do I call Google Sheets automation components "SEO software"? It's because
this is the main missing ingredient in building all those custom reports
necessary to surface new actionable data every day. It's also your easy route
into data manipulation with Python/Pandas and the repurposing of your aging SEO
career into something simultaneously more timely and timeless. SEO is dead.
Long live SEO! Sound familiar? Well, the other shoe is finally dropping with
all the Machine Learning tricks ol' Uncle Google is learning, and if you're a
dinosaur then y'all better learn to fly. If you can do Excel macros, then you
can survive, evolve and thrive.

Learning Linux, Python, vim and git (LPvg) will set you on a good course for at
least the next 10-years. If you're still scared of the Unix shell, that old
text-based command-line interface which is both the past and future of tech,
then stick your hand into the Gom Jabbar pain-box of Linux and cut your teeth
on my other repo here on Github `Levinux <https://github.com/miklevin/levinux>`_.
Now repeat after me: I must not fear. Fear is the mind-killer. Fear is the
little-death that brings total obliteration. I will face my fear. I will permit
it to pass over me and through me.

.. image:: https://raw.githubusercontent.com/miklevin/Pipulate/master/mike-levin-seo-nyc.png
