# Table of Contents
- [Introduction](#introduction)
    - [Version](#version)
    - [Changelog](Changelog.md)
- [Hardware Requirements](#hardware-requirements)
    - [CPU](#cpu)
    - [Memory](#memory)
    - [Storage](#storage)
- [Contributing](#contributing)
- [Issues](#issues)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Configuration](#configuration)
  - [ACCESS](#access)
  - [QUEUE](#queue)
  - [TOPIC](#topic)
  - [Data Store](#data-store)
  - [BROKER](#broker)
  - [Disk usage](#disk-usage)
  - [JMX](#JMX)
  - [Avaible Configuration Parameters](#avaible-configuration-parameters)
  - [Advance configuration](#advance-configuration)
- [References](#references)

# Introduction

Dockerfile to build a ActiveMQ container image.

## Version

Current Version: **5.14.3**

# Hardware Requirements

## CPU

- No stats avaible to say the number of core in function of messages

## Memory

- 512MB is too little memory, i think is to use ActiveMQ on test environment
- **1GB** is the **standard** memory size

You can set the memory that you need :

```bash
docker run --name='activemq' -it --rm \
	-e 'ACTIVEMQ_MIN_MEMORY=512' \
	-e 'ACTIVEMQ_MAX_MEMORY=2048'\
        -P
	webcenter/activemq:latest
```
This sample lauch ActiveMQ in docker with 512 MB of memory, and then ACtiveMQ can take 2048 MB of max memory

## Storage

The necessary hard drive space depends if you use persistant message or not and the type of appender. Normaly, no need space for ActiveMQ because the most data are contains directly on memory.
I think it depends on how you use ActiveMQ ;)

# Contributing

If you find this image useful here's how you can help:

- Send a Pull Request with your awesome new features and bug fixes
- Help new users with [Issues](https://github.com/disaster37/activemq/issues) they may encounter
- Send me a tip via [Bitcoin](https://www.coinbase.com/disaster37) or using [Gratipay](https://gratipay.com/disaster37/)

# Issues

Docker is a relatively new project and is active being developed and tested by a thriving community of developers and testers and every release of docker features many enhancements and bugfixes.

Given the nature of the development and release cycle it is very important that you have the latest version of docker installed because any issue that you encounter might have already been fixed with a newer docker release.

For ubuntu users I suggest [installing docker](https://docs.docker.com/installation/ubuntulinux/) using docker's own package repository since the version of docker packaged in the ubuntu repositories are a little dated.

Here is the shortform of the installation of an updated version of docker on ubuntu.

```bash
sudo apt-get purge docker.io
curl -s https://get.docker.io/ubuntu/ | sudo sh
sudo apt-get update
sudo apt-get install lxc-docker
```

Fedora and RHEL/CentOS users should try disabling selinux with `setenforce 0` and check if resolves the issue. If it does than there is not much that I can help you with. You can either stick with selinux disabled (not recommended by redhat) or switch to using ubuntu.

If using the latest docker version and/or disabling selinux does not fix the issue then please file a issue request on the [issues](https://github.com/disaster/activemq/issues) page.

In your issue report please make sure you provide the following information:

- The host distribution and release version.
- Output of the `docker version` command
- Output of the `docker info` command
- The `docker run` command you used to run the image (mask out the sensitive bits).

# Installation

Pull the image from the docker index. This is the recommended method of installation as it is easier to update image. These builds are performed by the **Docker Trusted Build** service.

```bash
docker pull webcenter/activemq:5.14.3
```

You can also pull the `latest` tag which is built from the repository *HEAD*

```bash
docker pull webcenter/activemq:latest
```

Alternately you can build the image locally.

```bash
git clone https://github.com/disaster37/activemq.git
cd activemq
docker build --tag="$USER/activemq" .
```

# Quick Start

You can launch the image using the docker command line :

- **For test purpose :**

```bash
docker run --name='activemq' -it --rm -P \
webcenter/activemq:latest
```
The account admin is "admin" and password is "admin". All settings is the default ActiveMQ's settings.

- **For production purpose :**

```bash
docker run --name='activemq' -d \
-e 'ACTIVEMQ_NAME=amqp-srv1' \
-e 'ACTIVEMQ_REMOVE_DEFAULT_ACCOUNT=true' \
-e 'ACTIVEMQ_ADMIN_LOGIN=admin' -e 'ACTIVEMQ_ADMIN_PASSWORD=your_password' \
-e 'ACTIVEMQ_WRITE_LOGIN=producer_login' -e 'ACTIVEMQ_WRITE_PASSWORD=producer_password' \
-e 'ACTIVEMQ_READ_LOGIN=consumer_login' -e 'ACTIVEMQ_READ_PASSWORD=consumer_password' \
-e 'ACTIVEMQ_JMX_LOGIN=jmx_login' -e 'ACTIVEMQ_JMX_PASSWORD=jmx_password' \
-e 'ACTIVEMQ_STATIC_TOPICS=topic1;topic2;topic3' \
-e 'ACTIVEMQ_STATIC_QUEUES=queue1;queue2;queue3' \
-e 'ACTIVEMQ_MIN_MEMORY=1024' -e  'ACTIVEMQ_MAX_MEMORY=4096' \
-e 'ACTIVEMQ_ENABLED_SCHEDULER=true' \
-v /data/activemq:/data/activemq \
-v /var/log/activemq:/var/log/activemq \
-p 8161:8161 \
-p 61616:61616 \
-p 61613:61613 \
webcenter/activemq:5.14.3
```


Or you can use [fig](http://www.fig.sh/). Assuming you have fig installed,

```bash
wget https://raw.githubusercontent.com/disaster37/activemq/master/fig.yml
fig up
```

# Configuration

## ACCESS
todo


## QUEUE
todo

## TOPIC
todo

## Data Store
todo

## BROKER
todo

## Disk usage
todo

## JMX
todo

## Avaible Configuration Parameters

*Please refer the docker run command options for the `--env-file` flag where you can specify all required environment variables in a single file. This will save you from writing a potentially long docker run command. Alternately you can use fig.*

Below is the complete list of available options that can be used to customize your activemq installation.

- **ACTIVEMQ_NAME**: The hostname of ActiveMQ server. Default to `localhost`
- **ACTIVEMQ_LOGLEVEL**: The log level. Default to `INFO`
- **ACTIVEMQ_PENDING_MESSAGE_LIMIT**: It is used to prevent slow topic consumers to block producers and affect other consumers by limiting the number of messages that are retained. Default to `1000`
- **ACTIVEMQ_STORAGE_USAGE**: The maximum amount of space storage the broker will use before disabling caching and/or slowing down producers. Default to `100 gb`
- **ACTIVEMQ_TEMP_USAGE**: The maximum amount of space temp the broker will use before disabling caching and/or slowing down producers. Default to `50 gb`
- **ACTIVEMQ_MAX_CONNECTION**: It's DOS protection. It limit concurrent connections. Default to `1000`
- **ACTIVEMQ_FRAME_SIZE**: It's DOS protection. It limit the frame size. Default to `104857600` (100MB)
- **ACTIVEMQ_ENABLED_SCHEDULER**: Permit to enabled scheduler in ActiveMQ. Default to `true`
- **ACTIVEMQ_ENABLED_AUTH**: Permit to enabled the authentification in queue and topic (no anonymous access). Default to `false`
- **ACTIVEMQ_MIN_MEMORY**: The init memory in MB that ActiveMQ take when start (it's like XMS). Default to `128` (128 MB)
- **ACTIVEMQ_MAX_MEMORY**: The max memory in MB that ActiveMQ can take (it's like XMX). Default to `1024` (1024 MB)

- **ACTIVEMQ_REMOVE_DEFAULT_ACCOUNT**: It's permit to remove all default login on ActiveMQ (Webconsole, broker and JMX). Default to `false`
- **ACTIVEMQ_ADMIN_LOGIN**: The login for admin account (broker and web console). Default to `admin`
- **ACTIVEMQ_ADMIN_PASSWORD**: The password for admin account. Default to `admin`
- **ACTIVEMQ_USER_LOGIN**: The login to access on web console with user role (no right on broker). Default to `user`
- **ACTIVEMQ_USER_PASSWORD**: The password for user account. Default to `user`
- **ACTIVEMQ_READ_LOGIN**: The login to access with read only role on all queues and topics.
- **ACTIVEMQ_READ_PASSWORD**: The password for read account.
- **ACTIVEMQ_WRITE_LOGIN**: The login to access with write role on all queues and topics.
- **ACTIVEMQ_WRITE_PASSWORD**: The password for write account.
- **ACTIVEMQ_OWNER_LOGIN**: The login to access with admin role on all queues and topics.
- **ACTIVEMQ_OWNER_PASSWORD**: The password for owner account.
- **ACTIVEMQ_JMX_LOGIN**: The login to access with read / write role on JMX. Default to `admin`
- **ACTIVEMQ_JMX_PASSWORD**: The password for JMX account. Default to `activemq`

- **ACTIVEMQ_STATIC_TOPICS**: The list of topics separated by comma witch is created when ActiveMQ start.
- **ACTIVEMQ_STATIC_QUEUES**: The list of queues separated by comma witch is created when ActiveMQ start.


## Advance configuration

For advance configuration, the best way is to read ActiveMQ documentation and created your own setting file like activemq.xml.
Next, you can mount it when you run this image or you can create your own image (base on this image) and include your specifics config file.

The home of ActiveMQ is in /opt/activemq, so if you want to override all the setting, you can launch docker with ` -v /your_path/conf:/opt/activemq/conf`
