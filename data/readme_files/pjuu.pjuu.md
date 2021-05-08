# Pjuu

An open-source social networking application which runs https://pjuu.com

![](https://github.com/pjuu/pjuu/workflows/main/badge.svg?branch=master) [![codecov.io](http://codecov.io/github/pjuu/pjuu/coverage.svg?branch=master)](http://codecov.io/github/pjuu/pjuu?branch=master) [![Requirements Status](https://requires.io/github/pjuu/pjuu/requirements.svg?branch=master)](https://requires.io/github/pjuu/pjuu/requirements/?branch=master) [![License](https://img.shields.io/badge/license-AGPLv3-brightgreen.svg)](http://www.gnu.org/licenses/agpl-3.0.en.html)

[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/pjuu/pjuu?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)


This is an open source project released under the GNU AGPLv3 license. See LICENSE for more details or visit the official GNU page at http://www.gnu.org/licenses/agpl-3.0.html.

### About

This is the primary code base for https://pjuu.com, the website is deployed directly from this respository.

The main goal of Pjuu as an application is privacy.

Pjuu is written in Python3/Flask and uses Redis and MongoDB as the data stores.

### Getting started

Getting started with Pjuu or deploying it yourself is quite easy if you are familiar with Python. We will only cover development here and the following documentation is for Debian 9 (Stretch) Linux (we are big fans). Pjuu should work with and any other Linux distribution, however you will need to change the commands to fit your envionment. It has also been tested with FreeBSD, but this is beyond the scope of the README.

For a fresh installation these commands will setup the environment:

```
$ sudo apt-get update

$ sudo apt-get install build-essential python3-dev python-virtualenv python-setuptools libmagickwand-dev redis-server mongodb

$ git clone https://github.com/pjuu/pjuu.git

$ cd pjuu

$ virtualenv -p python3 venv

$ source venv/bin/activate

$ pip install -r requirements-dev.txt
```

#### Testing

To run the unit tests with coverage the following commands can be used:

```
$ make test
```

To obtain a code coverage report

```
$ make coverage
```

Checking code quality and PEP8 compliance:

```
$ make flake
```

#### Development server

To Run the development server (Gunicorn with Gevent) type the following command:

```
$ make run
```

You can then view the site by visiting: http://localhost:5000

You can now play with the code base :)

#### Creating test accounts

**IMPORTANT Note:**
While testing You do NOT need to setup an SMTP server. To activate your account you can look in the response header for X-Pjuu-Token. If you copy this and visit `/activate/<token>` that will have the same effect as clicking the link in the activate account email. The same applies for any other action requiring confirmation (forgotten password), it will however be a different URL you need to append the token to.

This only works if `TESTING = True` in your settings.

### Contributing

We are open to all pull requests. Spend some time taking a look around, locate a bug, design issue or spelling mistake then send us a pull request :)

### Security

All software has bugs in and Pjuu is no different. These may have security implications. If you find one that you suspect could allow you to do something you shouldn't be able to please do not post it as an issue on Github. We would really appreciate it if you could send an e-mail to security@pjuu.com with the relevant details.

### Credits

James Rand - illustrating the original Otter logo.

Jonathan Trengrove - modernizing the Otter logo.
