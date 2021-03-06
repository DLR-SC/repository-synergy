# Whiskython

* **Official page**: [http://whiskyton.herokuapp.com/](http://whiskyton.herokuapp.com/)
* **Authors**: [Eduardo Cuducos](http://cuducos.me) and [Gabriel Vicente](https://g4brielvs.me)

## About

This web based app uses [an open database about whisky](https://www.mathstat.strath.ac.uk/outreach/nessie/nessie_whisky.html) to help you find whiskys you'd probably like. It uses mathematics to run through the tastes classified in that database, and to find the best matches. We were inspired by [this data visualization shared on Reddit](http://www.reddit.com/r/dataisbeautiful/comments/1u747v/flavor_profiles_for_86_scotch_whiskies/).

## What really matters

This was our very first project in Python.

## Installation

1. Clone the repository:<br>`$ git clone git@github.com:cuducos/whiskyton.git`.
2. Go to the repository folder:<br>`$ cd whiskyton`<br>(if you want, get your [virtualenv](https://pypi.python.org/pypi/virtualenv) running there).
3. Install the dependencies:<br>`$ pip install -r requirements.txt`.
4. Create and feed the database:<br>`$ python manage.py db upgrade`.
5. Run the server:<br>`$ python manage.py runserver`.

## Tests

To run tests: `$ nosetests`.

[Nose](http://nose.readthedocs.org/en/latest/) has difficulties in finding tests in executable files. That said, you might wanna change the permissions of the tests files: `$ chmod -x $(find whiskyton/tests/ -name '*.py')`.

Some tests use your local [Firefox](http://mozilla.org/firefox/) through [Selenium](http://www.seleniumhq.org/). So get the server running before running tests.

## Managing the application

### Charts cache

If you want to get rid of all the cached SVG charts: `$ python manage.py charts delete`.

If you want to create all possible charts and cache the SVG files: `$ python manage.py charts create` (it is not necessary, the app creates and caches them on the fly; however pre-caching them can optimize page loading time).

### Page views data

If you want to export analytics data (date, whisky and page views) as a CSV file to an external FTP server, you will need to set these `ENV` variables: `FTP_SERVER`, `FTP_USER` and `FTP_PASSWORD`. Once you have these variables, just run: `$ python manage.py analytics save`.

Thanks
------

We had a lot of Python teachers, we are so glad we could count on you, guys:

* Joe Warren, Scott Rixner, John Greiner and Stephen Wong, from the [An Introduction to Interactive Programming in Python](https://www.coursera.org/course/interactivepython) course at [Coursera](https://www.coursera.org/)
* Allen B. Downey and Jeff Elkner, authors of [Think Python: How to Think Like a Computer Scientist](http://www.greenteapress.com/thinkpython/thinkpython.html)
* Miguel Grinberg and his [The Flask Mega-Tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
* Everyone who have ever contributed to [The Hitchhiker???s Guide to Python!](http://docs.python-guide.org/en/latest/)
* Everyone who helped at Reddit, mainly these guys [here](http://www.reddit.com/r/webdev/comments/1uec51/a_dinosaur_wants_to_code/) and [here](http://www.reddit.com/r/Python/comments/1rnfle/setting_up_a_web_development_environment/)

In sum, we had the best teachers of the world in Python. Any mistake here is completely our fault.

Also we are glad to have contributions from [Henrique Bastos](http://github.com/henriquebastos), [Lucretiel](http://github.com/Lucretiel), [Justin Velluppillai](http://github.com/justinvelluppillai) and [Chris Loverchio](http://github.com/cloverchio).
