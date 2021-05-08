<img src="/docs/waterbutler.png?raw=true" width="25%" style="float:left;">

# WaterButler

[![Documentation Status](https://readthedocs.org/projects/waterbutler/badge/?version=latest)](http://waterbutler.readthedocs.org/en/latest/?badge=latest)
[![Code Climate](https://codeclimate.com/github/CenterForOpenScience/waterbutler/badges/gpa.svg)](https://codeclimate.com/github/CenterForOpenScience/waterbutler)
[![Coverage Status](https://coveralls.io/repos/github/CenterForOpenScience/waterbutler/badge.svg)](https://coveralls.io/github/CenterForOpenScience/waterbutler)

`master` Build Status: [![Build Status](https://travis-ci.org/CenterForOpenScience/waterbutler.svg?branch=master)](https://travis-ci.org/CenterForOpenScience/waterbutler)

`develop` Build Status: [![Build Status](https://travis-ci.org/CenterForOpenScience/waterbutler.svg?branch=develop)](https://travis-ci.org/CenterForOpenScience/waterbutler)

### Compatibility

WaterButler is compatible with Python 3.6.

### Documentation

Documentation available at https://waterbutler.readthedocs.io/en/latest/

### Setting up

In order to run WaterButler, you must create a Python 3.6-based virtualenv for it.

For MacOSX, you can install the latest version of Python3 using:

```bash
brew install python3
```

For Ubuntu users:

```bash
apt-get install python3.6
```

After completing the installation of Python 3.6, you must create a virtual environment. This can be done with the following commands:

```bash
pip install virtualenv
pip install virtualenvwrapper
mkvirtualenv --python=python3.6 waterbutler

pip install setuptools=37.0.0
pip install invoke==0.13.0

invoke install
invoke server
```

The above code will get the virtualenv up and running for the first time.  After the initial setup, you can run waterbutler by running:

```bash
workon waterbutler
invoke server
```

Some tasks also require a running celery worker.  You will need to install `rabbitmq` and run a server:

```bash
brew install rabbitmq
# on Ubuntu:
# apt-get install rabbitmq-server
rabbitmq-server
```

Then in your WaterButler virtualenv:

```bash
invoke celery
```

### Configuring

WaterButler configuration is done through a JSON file (`waterbutler-test.json`) that lives in the `.cos` directory of your home directory.  If this is your first time setting up WaterButler or its sister project, [MFR](https://github.com/CenterForOpenScience/modular-file-renderer/), you probably do not have this directory and will need to create it:

```bash
mkdir ~/.cos
```

The data in `waterbutler-test.json` is used by the many Django-style `settings.py` files sprinkled about.  Most of these files define a top-level key that its specific configuration should be listed under.  For instance, if you wanted your local WaterButler server to listen on port 8989 instead of the default 7777, you would check the settings file for `waterbutler.server`.  That file looks for `HOST` and `DOMAIN` configuration keys under the `SERVER_CONFIG` top-level key.  Your configuration file would need to be updated to look like this:

```json
{
  "SERVER_CONFIG": {
    "PORT": 8989,
    "DOMAIN": "http://localhost:8989"
  }
}
```

If you then wanted to update the GitHub commit message WaterButler submits when deleting files, you would look in `waterbutler.providers.github.settings`. The `DELETE_FILE_MESSAGE` parameter should come under the `GITHUB_PROVIDER_CONFIG` key:

```json
{
  "SERVER_CONFIG": {
    "PORT": 8989,
    "DOMAIN": "http://localhost:8989"
  },
  "GITHUB_PROVIDER_CONFIG": {
    "DELETE_FILE_MESSAGE": "WaterButler deleted this. You're welcome."
  }
}
```

### Testing

Before running the tests, you will need to install some additional requirements. In your checkout, run:

```bash
workon waterbutler
invoke install --develop
invoke test
```

### Known issues

- **Updated, 2018-01-02:** *WB has been updated to work with setuptools==37.0.0, as of WB release v0.37. The following issue should not happen for new installs, but may occur if you downgrade to an older version.*  Running `invoke install -d` with setuptools v31 or greater can break WaterButler.  The symptom error message is: `"AttributeError: module 'waterbutler' has no attribute '__version__'"`.  If you encounter this, you will need to remove the file `waterbutler-nspkg.pth` from your virtualenv directory, run `pip install setuptools==30.4.0`, then re-run `invoke install -d`.

- `invoke $command` results in `'$command' did not receive all required positional arguments!`: this error message occurs when trying to run WB v0.30.0+ with `invoke<0.13.0`.  Run `pip install invoke==0.13.0`, then retry your command.

### License

Copyright 2013-2018 Center for Open Science

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

### COS is hiring!

Want to help save science? Want to get paid to develop free, open source software? [Check out our openings!](https://cos.io/our-communities/jobs/)
