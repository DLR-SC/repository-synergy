# CloudCV

[![Join the chat at https://gitter.im/Cloud-CV/Lobby](https://badges.gitter.im/Cloud-CV/Lobby.svg)](https://gitter.im/Cloud-CV/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)       [![Build Status](https://travis-ci.org/Cloud-CV/CloudCV.svg?branch=develop)](https://travis-ci.org/Cloud-CV/CloudCV)    [![Code Health](https://landscape.io/github/Cloud-CV/CloudCV/develop/landscape.svg?style=flat)](https://landscape.io/github/Cloud-CV/CloudCV/develop)    [![Coverage Status](https://coveralls.io/repos/github/Cloud-CV/CloudCV/badge.svg)](https://coveralls.io/github/Cloud-CV/CloudCV)

## How to Setup

1. Install [git](https://git-scm.com/downloads), [postgresql](https://www.postgresql.org/download/) version >= 9.4, [virtualenv](https://virtualenv.pypa.io/) and [Node.js](https://www.digitalocean.com/community/tutorials/how-to-install-node-js-with-nvm-node-version-manager-on-a-vps) version >= 6 in your computer, if you don't have it already.
*Please check that the python version you are using for the project is 2.7.x*.
*If you are having trouble with postgresql on Windows check this link [postgresqlhelp](http://bobbyong.com/blog/installing-postgresql-on-windoes/).*
2. Get the source code on your machine via git
    ```
    git clone git@github.com:Cloud-CV/CloudCV.git cloudcv
    ```
    If you have not added `ssh` keys to your GitHub account then get the source code by running the following command
    ```
    git clone https://github.com/Cloud-CV/CloudCV.git cloudcv
    ```
3. Create a python virtual environment and install python dependencies.
    ```
    cd cloudcv
    virtualenv venv
    source venv/bin/activate  # run this command everytime before working on project
    pip install -r requirements/dev.txt
    ```
4. Rename `settings/dev/settings.sample.py` as `settings/dev/settings.py` and change credentials in `settings/dev/settings.py`
    ```
    cp settings/dev/settings.sample.py settings/dev/settings.py
    ```
    Use your postgres username and password for fields `USER` and `PASSWORD` in `settings/dev/settings.py` file.
5. Create an empty postgres database and run database migration.
    ```
    sudo -i -u (username)
    createdb cloudcv
    python manage.py migrate --settings=settings.dev.settings
    ```
6. That's it. Now you can run development server at [http://127.0.0.1:8000](http://127.0.0.1:8000) (for serving backend)
    ```
    python manage.py runserver --settings=settings.dev.settings
    ```
7. Open a new terminal window with node(>=6) and ruby(gem) install on your machine and type
    ```
    cd frontend
    sudo npm install -g yarn
    yarn install
    ```
    If you running npm install behind a proxy server, use
    ```
    npm config set proxy http://proxy:port
    ```
8. Now to connect to dev server at [http://127.0.0.1:6003](http://127.0.0.1:6003) (for serving frontend)
    ```
    yarn run dev
    ```

## How to Setup on Windows

1. Install [git](https://git-scm.com/downloads), [postgresql](https://www.postgresql.org/download/windows); tested with [postgresql installer by bigsql](https://www.openscg.com/bigsql/postgresql/installers.jsp/)  version >= 9.4, and [Node.js](https://nodejs.org/en/download/) version >= 6 in your computer & [python 2.7.x](https://www.python.org/downloads/windows/) , if you don't have it already.
2. Get the source code on your machine via git
    ```
    git clone git@github.com:Cloud-CV/CloudCV.git cloudcv
    ```
    If you have not added `ssh` keys to your GitHub account then get the source code by running the following command
    ```
    git clone https://github.com/Cloud-CV/CloudCV.git cloudcv
    ```
3. Open a command prompt and Install python dependencies.
    ```
    cd cloudcv
    pip install -r requirements\dev.txt
    ```
4. Rename `settings/dev/settings.sample.py` as `settings/dev/settings.py` and change credentials in `settings/dev/settings.py`
    ```
    copy settings\dev\settings.sample.py settings\dev\settings.py
    ```
    Use your postgres username and password for fields `USER` and `PASSWORD` in `settings/dev/settings.py` file.
5. Create an empty postgres database and run database migration.
    ```
    Start Postgresql server
	Open psql prompt
    createdb cloudcv
	In the command prompt,
    python manage.py migrate --settings=settings.dev.settings
    ```
6. That's it. Now you can run development server at [http://127.0.0.1:8000](http://127.0.0.1:8000) (for serving backend),
    ```
    python manage.py runserver --settings=settings.dev.settings
    ```
7. Open a new terminal window with node(>=6) and ruby(gem) install on your machine and type
    ```
    cd frontend
    npm install -g yarn
    yarn install
    ```
    If you running npm install behind a proxy server, use
    ```
    npm config set proxy http://proxy:port
    ```
8. Now to connect to dev server at [http://127.0.0.1:6003](http://127.0.0.1:6003) (for serving frontend)
    ```
    yarn run dev
    ```

## Contribution guidelines

If you are interested in contributing to CloudCV, follow our [contribution guidelines](https://github.com/Cloud-CV/CloudCV/blob/master/.github/CONTRIBUTING.md).
