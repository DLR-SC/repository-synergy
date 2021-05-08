# TIFU (Today I Fucked Up)

## Overview

TIFU is a tool that helps to restore commits erased by a force push on
Github, Gitlab and Bitbucket.

## Requirements

Python 3.5+

## Installation

Just clone, install dependencies, and you're ready to go!

```bash
git clone git@github.com:c0riolis/tifu.git
cd tifu
pip3 install -r requirements.txt --user
./tifu.py --help
```

## How to use it?

The simplest way to run the tool is to launch it with a remote as argument:

```bash
./tifu.py git@github.com:namespace/project.git
```

Or

```bash
./tifu.py https://github.com/namespace/project.git
```

It will automatically infer the API, repository name and hostname to use.

If you want to run it on your own instance of Gitlab for example, this will
fail since the tool can't determine which API to use. Just specify it:

```bash
./tifu.py git@mydomain.com:namespace/project.git --api gitlab
```

This is equivalent to the following command:

```bash
./tifu.py --api gitlab --host mydomain.com --repo namespace/project
```

You can also just connect to a specific API and select the repository
interactively:

```bash
./tifu.py --api bitbucket
```

Which works for your own instances as well:

```bash
./tifu.py --api github --host mydomain.com
```

## Usage

```raw
usage: tifu.py [-h] [-a] [--host HOST] [-n REPO] [remote]

positional arguments:
  remote                git remote

optional arguments:
  -h, --help            show this help message and exit
  -a , --api            API to use (github, gitlab, bitbucket)
  --host HOST           server hostname
  -r REPO, --repo REPO  repository name (namespace/project)
```

## How does it work?

Git repository managers are usually using event systems to build users' threads.
These events are accessible via APIs and are providing various pieces of information.

In this case, we are using events generated on push to get the ID of the
previous HEAD and create a branch pointing to it.

Old HEAD's objects are usually still available since they are not removed until
the repository is garbage collected on the server side.
