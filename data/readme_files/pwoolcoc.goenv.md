[![Build Status](https://travis-ci.org/pwoolcoc/goenv.svg)](https://travis-ci.org/pwoolcoc/goenv)

# goenv - Set up a Golang environment

I got tired of manually setting my GOPATH when I went from one project to another,
so I wrote a small utility to set up my environment for me. It is similar in spirit to Python's
`virtualenv`, though it does less, and does it a little differently.

The main difference is that instead of an 'activate' script that sets up your environment,
this opens up a new subshell for you to work in. It will also download
and install the version of Go that you want it to.

## Installation

Currently goenv is written in python, so installation is a simple `pip
install` away:

    $ sudo pip install pygoenv

## Usage

    $ cd /path/to/project
    $ echo $GOPATH

    # simplest usage
    $ goenv
    Downloading http://go.googlecode.com/files/go1.2.linux-amd64.tar.gz
    Extracting /home/user/.cache/goenv/go1.2.linux-amd64.tar.gz to /home/user/.config/goenv/dists/1.2
    (golang-1.2) $ echo $GOPATH
    /path/to/project:/path/to/project/pkg/somepkg
    ^D
    $
    
    # You don't have to download a new go tarball every time...
    $ goenv
    Using existing tarball
    Go version 1.2 already exists, skipping extract
    (golang-1.2) $
    ^D
    $

    # specify Golang version
    $ goenv --go-version 1.1
    Downloading http://go.googlecode.com/files/go1.1.linux-amd64.tar.gz
    Extracting /home/user/.cache/goenv/go1.1.linux-amd64.tar.gz to /home/user/.config/goenv/dists/1.1
    (golang-1.1) $

## Contact

email: paul@woolcock.us

twitter: @pauldwoolcock

jabber: pauldwoolcock@dukgo.com

irc: duncan @ irc.mozilla.org
