![](meta/repo-banner.png)
[![](meta/repo-banner-bottom.png)][lionheart-url]

For information on how to use this project template, check out the [wiki](https://github.com/lionheart/django-template/wiki/Django-2.1).

# {{ project_name }}

### Table of Contents

* [Requirements](#requirements)
* [Local Setup](#local-setup)
* [Local Development](#local-development)

### Requirements

* [Homebrew](https://brew.sh) (not quite a "requirement" but recommended)

      /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

* [Python 3](https://www.python.org/downloads/release/python-365/)

      brew install python

* [pip](https://pip.pypa.io/en/stable/) (should come bundled when installing Python 3 via Homebrew)

* [PostgreSQL 10.4](https://www.postgresql.org/about/)

      brew install postgresql

## Local Development

1. Set up the Python virtual environment.

       python3 -m venv venv

2. Run the make setup task. This will install all requirements, link local settings, initialize the local development database, and run all migrations.

       make setup

2. Set up the Git hooks (optional).

       make setup-git-hooks

3. Start the local development server and Sass.

       foreman start -f Procfile.dev

    Map "local.{{ project_name }}.com" to 127.0.0.0 using DNS. If you haven't yet registered a domain, add the following line to your `/etc/hosts` file.

       127.0.0.1 local.{{ project_name }}.com

    After you've done that, open your browser and navigate to "[local.{{ project_name }}.com](http://local.{{ project_name }}.com)". Your project is now running!  


[lionheart-url]: https://lionheartsw.com/

