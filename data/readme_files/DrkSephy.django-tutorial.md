# django-tutorial

Django tutorial application built using Requests, Bower, Twitter Bootstrap and Github API

# Installation

To install the required libraries for this file, simply run the following:

    pip install -r requirements.txt

This project also requires using Bower, which requires NPM. In order to get NPM, simple install <a href="https://nodejs.org/download/">Node.js</a>. Once you have node, you can install <a href="http://bower.io/">Bower</a>:

    npm install -g bower

**Note**: On a Mac, you'll need to use:

    sudo npm install -g bower

With Bower, you can install the front-end dependencies by running:

    bower install

This will generate the **static** folder along with **bootstrap** and **jquery** inside it.

# Running the project

To run this project:

	# Navigate into directory containing manage.py
    cd demonstration

    # Setup the database
    python manage.py migrate
    python manage.py makemigrations

    # Run the server
    python manage.py runserver

You can now visit the following URLS:

	* http://127.0.0.1:8000/app/
	* http://127.0.0.1:8000/app/test/
	* http://127.0.0.1:8000/app/profile/

# Tests

Run the test suite:

    python manage.py test