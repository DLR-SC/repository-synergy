# docker-puller ![License MIT](https://go-shields.herokuapp.com/license-MIT-blue.png)

[![Travis-CI Status](https://secure.travis-ci.org/glowdigitalmedia/docker-puller.png?branch=master)](http://travis-ci.org/#!/glowdigitalmedia/docker-puller)

Listen for web hooks (i.e: from docker.io builds) and run a command after that.

Introduction
============

If you use docker.io (or any similar service) to build your Docker container, it may be possible that, once the new image is generated, you want your Docker host to automatically pull it and restart the container.

Docker.io gives you the possibility to set a web hook after a successful build. Basically it does a POST on a defined URL and send some informations in JSON format.

docker-puller listen to these web hooks and can be configured to run a particular script, given a specific hook.

Example web hook
================

In docker.io setup a web hook with an URL like this: https://myserver.com/dockerpuller?token=abc123&hook=myhook1

Example docker-puller configuration
===================================

    {
        "port": 8000,
        "token": "abc123",
        "hooks": {
            "myhook1": "restart-container-myhook1.sh"
        }
    }
