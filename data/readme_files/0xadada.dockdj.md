# dockdj

> :ship: A recipe for building 12-factor Python / Django web apps with
multi-container Docker and deploying to Amazon AWS using Elastic Beanstalk.

[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/)

The aim of Dockdj is to provide an example of how to quickly create a
Django web application following the [Twelve Factor](https://12factor.net/)
App principals.

**The Twelve Factors**

1. **Codebase**<br>
  One codebase tracked in revision control, many deploys<br>
  :white_check_mark: Yup, GitHub
1. **Dependencies**<br>
  Explicitly declare and isolate dependencies<br>
  :white_check_mark: Yup, uses requirements.txt
1. **Config**<br>
  Store config in the environment<br>
  :white_check_mark: Yup, uses .env files
1. **Backing Services**<br>
  Treat backing services as attached resources<br>
  :white_check_mark: BYOBacking service
1. **Build, release, run**<br>
  Strictly separate build and run stages<br>
  :white_check_mark: gulp, bin/image, bin/stevedore, bin/deploy
1. **Processes**<br>
  Execute the app as one or more stateless processes<br>
  :white_check_mark: Thanks Docker!
1. **Port binding**<br>
  Export services via port binding<br>
  :white_check_mark: 80 & 8010
1. **Concurrency**<br>
  Scale out via the process model<br>
  :white_check_mark: Keep your sessions in Redis or DB
1. **Disposability**<br>
  Maximize robustness with fast startup and graceful shutdown<br>
  :white_check_mark: Thank Docker!
1. **Dev/Prod parity**<br>
  Keep development, staging, and production as similar as possible<br>
  :white_check_mark: Yup
1. **Logs**<br>
  Treat logs as event streams<br>
  :white_check_mark: Yup
1. **Admin Processes**<br>
  Run admin/management tasks as one-off processes<br>
  :no_entry_sign: Does not Apply



## Contents

This repo contains a simple Python Django 1.8 web app as well as the
configuration for both Django and NGINX Docker images. There are
also some Bash scripts to help automate the build, release and
deploy process.

**Stack**
* Python 3.4
* Django 1.8
* Gunicorn app server
* Nginx web server
* Sass css preprocessor
* Bootstrap 4-alpha CSS framework
* Gulp build system


## Get Started

This document assumes you are running OS X. These are the requirements
needed by the `bin/install` script;

* Bash
* XCode & command line utilities
* [Homebrew](http://brew.sh) 0.9+

Additionally these requirements are installed:

* [docker-machine](https://www.docker.com/docker-machine)
* Docker & [Docker-compose](https://docs.docker.com/compose/)
* Amazon Web Services [Elastic Beanstalk
CLI](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3.html)

These steps will get you running locally:

1. `./bin/install` will provision your local development machine for
  the first time. It will
  * install all requirements (if they don't exist)
  * creates and starts a Docker virtual machine
1. Copy `environments/dev/.env.example` to `environments/dev/.env` and
  edit the values. Please make sure to change the following keys:
  * `ENV_SECRET_KEY` create your own [Django secret
    key](https://docs.djangoproject.com/en/dev/ref/settings/#secret-key)
  * `ENV_CDN` to your Docker host IP: `docker-machine ip docker-vm`
  * Optionally:
    * `ENV_AWS_EB_ENVIRONMENT_NAME` to your Amazon AWS Elastic Beanstalk
      environment name
    * `ENV_DOCKER_HUB_REPO_PATH` to your Docker repo (Create one if you
      plan to publish images to Docker Hub.)
1. Create a dev python environment: `pyvenv environments/dev/pyvenv`
1. `./bin/image dev build` will create "dev" Docker images with all
   dependencies installed.
1. `./bin/stevedore dev start` will run the dev Docker containers, open
   the browser, and tail the logs. At this point you're viewing running
   source code!
  * `ctrl+c` stops the logs `./bin/stevedore dev stop` will stop the Docker
    containers.
  * `./bin/stevedore dev logs` resumes log tailing.
1. Optionally, to build frontend assets (CSS, images, etc):
  * Run `./bin/stevedore dev build:dev`

You can typically connect to your web application at:
http://192.168.99.100/xyzzy.

You should now be up and running. Welcome.


## Deployment

Read more about deploying with Amazon AWS Elastic Beanstalk, version
numbering, running deployments, hotfix / patch deployments, Docker Hub,
and more on the [Deployments](../../wiki/Deployments) wiki page.


## Testing & Code Quality Tooling

Read more about the set of [tools](../../wiki/Tooling) for managing,
testing and deploying.


## Authors

* [0xADADA](https://github.com/0xadada) -
  [@0xadada](http://twitter.com/0xadada)


## License

MIT
