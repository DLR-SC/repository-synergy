# Varnish Docker image

Varnish docker image with support for dynamic backends, Rancher DNS, auto-configure
and reload.

This image is generic, thus you can obviously re-use it within
your non-related EEA projects.

 - Debian Stretch
 - Varnish **4.1.11**
 - Varnish agent 2 **4.1.4**
 - Varnish dashboard
 - EXPOSE **6081 6085**

## Supported tags and respective Dockerfile links

  - `:latest` [*Dockerfile*](https://github.com/eea/eea.docker.varnish/blob/master/varnish/Dockerfile) (Debian Jessie, Varnish 4.1)

### Stable and immutable tags

  - `:4.1-6.4` [*Dockerfile*](https://github.com/eea/eea.docker.varnish/tree/4.1-6.3/varnish/Dockerfile) - Varnish: **4.1.11** Release: **6.4

See [older versions](https://github.com/eea/eea.docker.varnish/releases)

### Changes

 - [CHANGELOG.md](https://github.com/eea/eea.docker.varnish/blob/master/CHANGELOG.md)

## Base docker image

 - [hub.docker.com](https://registry.hub.docker.com/u/eeacms/varnish)

## Source code

  - [github.com](http://github.com/eea/eea.docker.varnish)


## Installation

1. Install [Docker](https://www.docker.com/).


## Usage

### Run with Docker Compose

Here is a basic example of a `docker-compose.yml` file using the `eeacms/varnish` docker image:

    version: "2"
    services:
      varnish:
        image: eeacms/varnish
        ports:
        - "80:6081"
        - "6085:6085"
        depends_on:
        - anon
        - auth
        - download
        environment:
          BACKENDS: "anon auth download"
          BACKENDS_PORT: "8080"
          DNS_ENABLED: "true"
          BACKENDS_PROBE_INTERVAL: "3s"
          BACKENDS_PROBE_TIMEOUT: "1s"
          BACKENDS_PROBE_WINDOW: "3"
          BACKENDS_PROBE_THRESHOLD: "2"
          DASHBOARD_USER: "admin"
          DASHBOARD_PASSWORD: "admin"
          DASHBOARD_SERVERS: "varnish"
          DASHBOARD_DNS_ENABLED: "true"
      anon:
        image: eeacms/hello
        environment:
          PORT: "8080"
      auth:
        image: eeacms/hello
        environment:
          PORT: "8080"
      download:
        image: eeacms/hello
        environment:
          PORT: "8080"


The application can be scaled to use more server instances as backends, with `docker-compose scale`:

    $ docker-compose up -d
    $ docker-compose scale anon=4 auth=2 varnish=2

An example of a more complex application using the `eeacms/varnish` with `docker-compose`
image is [EEA WWW](https://github.com/eea/eea.docker.www).


### Extend the image with a custom varnish.vcl file

The `default.vcl` file provided with this image is bare and only contains
the marker to specify the VCL version. If you plan on using a more
elaborate base configuration in your container and you want it shipped with
your image, you can extend the image in a Dockerfile, like this:

    FROM eeacms/varnish
    COPY varnish.vcl /etc/varnish/conf.d/

and then run

    $ docker build -t varnish-custom /path/to/Dockerfile

### Support for specifying probe request headers

Two environment variables support defining specific probe request headers.
The primary warning / tricky part is around the delimiter used for separating
the individual headers. Below is an example:

    BACKENDS_PROBE_REQUEST: 'GET / HTTP/1.1|Host: example.com|Connection: close|User-Agent: Varnish Health Probe'
    BACKENDS_PROBE_REQUEST_DELIMITER: '|'

The above will result in the probe being specified using the probe.request attribute
and will replace the default probe.url attribute completely.
The important point, of course, is that you need to pick an appropriate delimiter
that is not contained within any headers that you wish to pass.

The hostname of the current backend being probed can be specify using the `%(hostname)s` placeholder:

    BACKENDS_PROBE_REQUEST: 'GET / HTTP/1.1|Host: %(hostname)s|Connection: close|User-Agent: Varnish Health Probe'
    BACKENDS_PROBE_REQUEST_DELIMITER: '|'

### Change and reload configuration without restarting the container

If the configuration directory is mounted as a volume, you can modify
it from outside the container. In order for the modifications
to be loaded by the varnish daemon, you have to run the `reload` command,
as following:

    $ docker exec <container-name-or-id> reload

The command will load the new configuration, compile it, and if compilation
succeeds replace the old one with it. If compilation of the new configuration
fails, the varnish daemon will continue to use the old configuration.
Keep in mind that the only way to restore a previous configuration is to
restore the configuration files and then reload them.

### Support for stripping cookies for better caching
By default, if any cookies are present, the cache is bypassed. This section describes
new support for configuration of various cookie-based cache options. Configuration is
enabled with the COOKIES environment variable. If set, additional code
is executed that builds a cookie_config.vcl file containing additions to
the generated default.vcl file. The following cookie options are currently supported.

1. Whitelist of cookies - Allows stripping all but a small list of cookies
2. (Future) Remove cookies for listed static file types, so caching works

#### Whitelist of cookies
With this option you provide a regular expression describing those cookies that should
be passed through to the backend. All cookies not described by the expression will be
stripped from the headers. Here is an example.
```
COOKIES=true
COOKIES_WHITELIST=(SESS[a-z0-9]+|SSESS[a-z0-9]+|NO_CACHE)
```

### Upgrade

    $ docker pull eeacms/varnish

## Supported environment variables ##


As varnish has close to no purpose by itself, this image should be used
in combination with others with [Docker Compose](https://docs.docker.com/compose/).
The varnish daemon can be configured by modifying the following environment variables:

* `PRIVILEDGED_USER` Priviledge separation user id (e.g. `varnish`)
* `CACHE_SIZE` Size of the RAM cache storage (default `2G`)
* `CACHE_STORAGE` Override default RAM cache (e.g. `file,/var/lib/varnish/varnish_storage.bin,1G`)
* `ADDRESS_PORT` HTTP listen address and port (default `:6081`)
* `ADMIN_PORT` HTTP admin address and port (e.g. `:6082`)
* `PARAM_VALUE` A list of parameter-value pairs, each preceeded by the `-p` flag
* `BACKENDS` A list of `host[:port]` pairs separated by space
  (e.g. `BACKENDS="127.0.0.1 74.125.140.103:8080"`)
* `BACKENDS_PORT` Default port to be used for backends (defalut `80`)
* `BACKENDS_PROBE_ENABLED` Enable backend probe (default `True`)
* `BACKENDS_PROBE_URL` Backend probe URL (default `/`)
* `BACKENDS_PROBE_TIMEOUT` Backend probe timeout (defalut `1s`)
* `BACKENDS_PROBE_INTERVAL` Backend probe interval (defalut `1s`)
* `BACKENDS_PROBE_WINDOW` Backend probe window (defalut `3`)
* `BACKENDS_PROBE_THRESHOLD` Backend probe threshold (defalut `2`)
* `DNS_ENABLED` DNS lookup provided `BACKENDS`. Use this option when your backends are resolved by an internal/external DNS service (e.g. Rancher)
* `DNS_TTL` DNS lookup backends every $DNS_TTL minutes. Default 1 minute.
* `BACKENDS_SAINT_MODE` Register backends using [saintmode module](https://github.com/varnish/varnish-modules/blob/master/docs/saintmode.rst)
* `BACKENDS_PROBE_REQUEST` Backend probe request header list (default empty)
* `BACKENDS_PROBE_REQUEST_DELIMITER` Backend probe request headers delimiter (default `|`)
* `DASHBOARD_SERVERS` Include varnish services, space separated, within varnish dashboard. Useful when you want to scale varnish and see them all within varnish dashboard (e.g.: `DASHBOARD_SERVERS=varnish` and `docker-compose scale varnish=2`)
* `DASHBOARD_DNS_ENABLED` Convert `DASHBOARD_SERVERS` to ips in order to discover multiple varnish instances. (default `false`)
* `DASHBOARD_PORT` Run Varnish dashboard on this port inside container (default `6085`)
* `DASHBOARD_USER` User to access the varnish dashboard exposed on `DASHBOARD_PORT` (default `admin`)
* `DASHBOARD_PASSWORD` Password for the user to access the varnish dashboard exposed on `DASHBOARD_PORT`. (default `admin`)
* `COOKIES` Enables cookie configuration
* `COOKIES_WHITELIST` A regular expression describing cookies that are passed through, all others are stripped
* `AUTOKILL_CRON` Has to be used with healtchecks enabled on varnish ports, it will kill the varnish cache process ( which exposes the ports ) keeping the container running, uses Linux Crontab format `[Minute] [hour] [Day_of_the_Month] [Month_of_the_Year] [Day_of_the_Week]`, UTC time


## Copyright and license

The Initial Owner of the Original Code is European Environment Agency (EEA).
All Rights Reserved.

The Original Code is free software;
you can redistribute it and/or modify it under the terms of the GNU
General Public License as published by the Free Software Foundation;
either version 2 of the License, or (at your option) any later
version.


## Funding

[European Environment Agency (EU)](http://eea.europa.eu)
