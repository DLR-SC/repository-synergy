Governance, Risk and Compliance (GGRC)
=========

Governance, Risk Management, and Compliance are activities necessary for any organization with regulatory or contractual obligations.

Governance refers to management structure, policies, procedures, shareholder relations, etc.

Risk Management is a process to identify business and technical risks as well as means to mitigate those.

Compliance refers to processes necessary to meet applicable regulations and communicate to stakeholders about it.

Many organizations operate in multiple jurisdictions worldwide, each of which has its own and often overlapping laws and regulations.   Organizational functions and information relating to risk management and compliance often tend to be managed in silos reflecting the multiple jurisdictions, scope, stakeholder diversity and historical basis.   This leads to inefficiency.

The GGRC project intends to provide an open source solution for managing some of these common problems.  The application provides a common system of record for information in this domain.   It provides the ability to capture the relationships and to understand how the pieces fit together.  It also provides workflow capability to manage processes in this domain.


Migrated from [Google](https://code.google.com/archive/p/compliance-management)
[Code](https://code.google.com/archive/p/ggrc-core).


## Requirements

The following software is required to stand up a GGRC-Core development
environment:

|               Prerequisite                       |                 Description              |
|--------------------------------------------------|------------------------------------------|
|[Docker](https://www.docker.com/)                 | Container management tool                |
|[Docker compose](https://docs.docker.com/compose/)| A tool for defining multi-container apps |

**NOTE for Windows/OSX users:** The easiest way of getting Docker is by installing the
[docker toolbox](https://www.docker.com/products/docker-toolbox).

## Quick Start

Getting started with GGRC-Core development should be fast and easy once you
have Docker up and running. Here are the steps:

**NOTE for Windows/OSX users:** Make sure `docker` is up and running by following the [windows guide](https://docs.docker.com/engine/installation/windows/#using-docker-from-windows-command-prompt-cmd-exe) / [osx guide](https://docs.docker.com/engine/installation/mac/#from-your-shell).

**NOTE:** Navigate to [main](https://github.com/google/ggrc-core/tree/main) branch to retrieve complete control functionality (such as create/edit/deprecate controls). Control functionality to create, edit & deprecate is unavailable on other branches.

* clone the repo
* cd to the project directory
* Set up the necessary keys:

``` sh
mv docker-compose.override.yml{.example,}
vim docker-compose.override.yml # Add the keys from cloud console
```
* Run the following:

``` sh
./bin/containers setup dev
```

To log into the container, run the following:

``` sh
./bin/containers connect
```

If you see download errors during the `docker-compose up -d` stage, or if any subsequent
step fails, try running `docker-compose build` (See [Reprovisioning a Docker container](#reprovisioning-a-docker-container) below for more).

If apt-get fails to install anything (for example `Could not resolve 'archive.ubuntu.com'`), try [this](#dns-issues).

_NOTE: Because Docker shared volumes do not have permission mappings, you should
not use git and other file-creating commands from inside the container, as these
files will be owned by root and may disrupt future git usage on the host
machine._


### Launching GGRC as Stand-alone Flask

Most development is done in a stand-alone flask. We strive to make getting up
and running as simple as possible; to that end, launching the application is
simple:

```sh
launch_ggrc
```

### Launching GGRC in Google App Engine SDK

We strive to make getting up and running as simple as possible; to that end,
launching the application in the Google App Engine SDK environment is simple:

```sh
launch_gae_ggrc
```

This requires `src/app.yaml` with settings and `src/packages` with
requirements. You can generate the YAML file with:

```sh
deploy_appengine extras/deploy_settings_local.sh
```

To (re-)generate the requirements, you can run:

```
make clean_appengine && make appengine
```

### Accessing the Application

The application will be accessible via this URL: <http://localhost:8080/>

If you're running the Google App Engine SDK, the App Engine management console
will be available via this URL: <http://localhost:8000/>. You can log in as
user@example.com with admin rights and setup other users later.

### Accessing MySQL query logs

If using the `docker-compose.yml` file, the mysql query logs are enabled
by default and can be monitored with:

```
docker exec $(docker container ls -f name=ggrccore_db_1 -q -a) tail -f /tmp/mysql.log
```

Error logs, with all deadlock information: 

```
docker exec $(docker container ls -f name=ggrccore_db_1 -q -a) tail -f /tmp/mysql_error.log
```

Or slow queries, that take more than 0.5s, with:

```
docker exec $(docker container ls -f name=ggrccore_db_1 -q -a) tail -f /tmp/slow_query.log
```

## Running Tests

Tests are your friend! Keep them running, keep them updated.

#### For JavaScript tests:

```sh
run_karma # To run karma with Chrome Headless
run_karma_chrome # To run karma in host browser (open http://localhost:9876)
```

`run_karma` is the default way of running tests as it automatically
builds the javascript assets on file changes. Use `run_karma_chrome` if you
need to debug an issue in the Chrome browser. For performance reasons
`run_karma_chrome` does not automatically build assets, so make sure you do it
manually by running `build_assets`.

#### For Python tests:

```sh
run_pytests
```

The script will run unit tests and integration tests.

For better usage of unit tests, you can use sniffer inside the test/unit folder.
This will run the tests on each file update.

```sh
cd test/unit; sniffer
```

You can drop into the ipdb debugger on failures by running:

```sh
run_pytests --ipdb-failures
```

#### For Selenium tests:

Up docker containers, prepare and launch dev server:
```sh
./bin/selenium_containers
```

Then you can run Selenium tests on your machine:

```sh
cd test/selenium
PYTHONPATH=src DEV_URL=http://localhost:8080 DEV_DESTRUCTIVE_URL=http://localhost:8080 pytest -n=0 --headless=False
```
(you can set these env variables and cmd options in IDE)

To run Selenium tests inside docker container you can do:

```sh
docker container exec -it $(docker container ls -f name=selenium_selenium_1 -q -a) bash
pytest -n=0
```

## Quickstart Breakdown


The quick start above gives a glimpse into the GGRC development environment.
It's worth noting where there is automation in GGRC, and where there isn't.
Often the lack of automation support for a step is intentional. Let's explore
each step in detail.

#### Reprovisioning a Docker container

To reprovision a docker container run the following:

Remove files that are not in the repository e.g. Python cache:
```sh
git clean -df
```
Start re-provisioning:
```sh
docker-compose build --pull --no-cache
./bin/containers setup
```


### Compiling JavaScript and Sass Templates

Since GGRC uses Webpack to bundle JavaScript and Sass Templates, the sources need to be compiled.
This has been automated via a script available in `$PATH in the virtual
machine:

```sh
build_assets
```

To have a process watch Javascript and Sass resources and compile them as they are changed
you could use this command:

```sh
watch_assets
```

### Importing Example Data

Example test data can be loaded with the following command:

```sh
db_reset backup-file.sql
```

## Gotchas

After syncing your local clone of GGRC-Core you may experience a failure when
trying to run the application due to a change (usually an addition) to the
prerequisites.

There are two primary classes of requirements for GGRC-Core: Python requirements
and other provision steps

There are two pip requirements files: a runtime requirements file,
`src/requirements.txt`, for application package dependencies and a
development requirements file, `src/requirements-dev.txt`, for additional
development-time package dependencies. The runtime requirements are deployed
with the application while the development requirements are only used in the
development environment (largely for testing purposes).

Most requirements changes should be in either `src/requirements.txt` or
`src/requirements-dev.txt` and would manifest as module import failures.

### DNS issues

Sometimes build fails due to `Could not resolve 'archive.ubuntu.com'`.

Solution 1:

On the host find out the primary and secondary DNS server addresses:
```
$ nmcli dev show | grep 'IP4.DNS'
IP4.DNS[1]:              10.0.0.2
IP4.DNS[2]:              10.0.0.3
```

NOTE: For older versions of `nmcli`, one should replace the first part of the
command above with `nmcli device list` (tested with nmcli version 0.9.8.8).

Using these addresses, create a file `/etc/docker/daemon.json`:
```
$ sudo su root
# cd /etc/docker
# touch daemon.json
```
Put this in `/etc/docker/daemon.json`:
```
{
   "dns": ["10.0.0.2", "10.0.0.3"]
}
```   
Exit from root:
```
# exit
```
Now restart docker:
```
$ sudo service docker restart
```

Solution 2:
- Uncomment the following line in `/etc/default/docker`: `DOCKER_OPTS="--dns 8.8.8.8 --dns 8.8.4.4"`
- Restart the Docker service `$ sudo service docker restart`
- Delete any images which have cached the invalid DNS settings.
- Build again and the problem should be solved.

### Unable to run Docker as non-root user

Please check the [Official documentation](https://docs.docker.com/engine/installation/linux/linux-postinstall/) on this.

### `IOError: Can not access file in context: /<ggrc-core>/src/packages`

Latest Docker (at least `Docker version 18.01.0-ce, build 03596f51b1`) tries to
resolve our symlinks in the project directory (which we use to store
dependencies installed from inside the container) on the host machine.

A workaround for this is to create the corresponding directories on the host
machine as a placeholder so the symlinks aren't considered broken:

```sh
$ sudo mkdir -p /vagrant-dev/node_modules
$ sudo mkdir -p /vagrant-dev/opt/gae_packages
```

Docker doesn't use these directories on the host machine.

### Environment Variables

*GGRC_SETTINGS_MODULE*:

GGRC uses this environment variable to define which module(s) within
`ggrc.settings` to use during the bootstrap phase. The value can be one
or more space-separated module names, which will be applied in the same
order they are specified. `source bin/init_env` will set this value to
`development`.

### Details About VM File Structure

`docker-compose build` installs several Debian packages globally within the
VM. All other project data is contained within two directories, specified by
environment variables (and defined in `/home/vagrant/.bashrc`).

*PREFIX*:

Points at root directory of the Git repository, and is automatically
detected if not present.

*DEV_PREFIX*:

Points at a directory containing `tmp` and `opt` directories. If not
defined, `DEV_PREFIX` defaults to the value of `PREFIX`. (In the VM,
it is defined to `/vagrant-dev` to avoid slowdown caused by the shared
filesystem at `/vagrant`.)

### Changes to Requirements Files

The first thing to try to resolve issues due to missing prerequisites is to
run the following command from within the project directory in the host
operating system:

```sh
docker-compose build
```

command *should* be an update Python virtualenv containing the Python packages
required by the application as well as any new development package
requirements.

To manually update the requirements, you can log in to docker container and run

```sh
pip install -r src/requirements-dev.txt
pip install --no-deps -r src/requirements.txt
```

Note that if you're using `launch_gae_ggrc`, then changes to
`src/requirements.txt` will require rebuilding the `src/packages` via

```
make appengine_packages
```

# Copyright Notice

Copyright (C) 2013-2018 Google Inc.
Licensed under the [Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0)
license (see the LICENSE file).
