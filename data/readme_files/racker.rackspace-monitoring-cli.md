# Rackspace Monitoring CLI

Command line utility for [Rackspace Cloud Monitoring](https://monitoring.api.rackspacecloud.com/).

## Installation

Utility can be installed using `pip`:

```
$ sudo pip install rackspace-monitoring-cli
```

Note: If you don't use a virtual environment the library needs to be installed
under the user which has a write permission to `/usr/local/bin` where the script
files are installed.

## Settings Credentials

Credentials can be set (in order of precedence) as environment variables (RAXMON_USERNAME,
RAXMON_API_KEY, RAXMON_API_URL, RAXMON_AUTH_URL), in a configuration file or you can pass 
them manually to each command.

Default configuration file path is `~/.raxrc` but you can overrride it by
setting the `RAXMON_RAXRC` environment variable. For example:

`RAXMON_RAXRC=~/.raxrc.uk raxmon-entities-list`

Note:
* US API authentication end point is the default value and can be omitted
* UK API authentication end point is https://lon.identity.api.rackspacecloud.com/v2.0/tokens

### Example configuration file

```
[credentials]
username=foo
api_key=bar

[api]
url=https://monitoring.api.rackspacecloud.com/v1.0

[auth_api]
url=https://identity.api.rackspacecloud.com/v2.0/tokens

[ssl]
verify=true
```

## Using bash completion

`source contrib/optcomplete.sh`

## Usage

### General

`command [--username=<username>] [--api-key=<api key>] [--api-url=<api url>] [..options..]`

## View available options

`command --help`

### Specifying lists and dictionaries

#### List

Use a comma delimited string. For example:

`raxmon-checks-create --monitoring-zones=mzA,mzB,mzC`

#### Dictionary

Use a comma delimited string of key=value pairs. For example

`raxmon-entities-create --metadata="location=server room,tag=foobar"`

## View available commands

`raxmon`

# Issues, Feedback

Please use Github issue tracker or send an email to `monitoring@rackspace.com`.
