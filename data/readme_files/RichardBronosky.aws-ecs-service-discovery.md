# aws-ecs-service-discovery
Simple Service Discovery for Amazon EC2 Container Service

--------

## Introduction

### "Simple Service Discovery is not a Discovery Service."

With no changes to your software and no additional services running in your cluster, you can run everything on Amazon ECS just like you on a single monolithic servers. Party like it's 2006, Dawg!

### Primary Objective

This project aims to solve the need for service discovery on AWS ECS is then **simplest** possible manner. I know that's a tall order because service discovery can be a complex issue and there are lots of projects out there trying to solve it. More about my [Design Goals] later.

### What it does

1. Identify tasks that are services.
2. Get the internal IP of the host of each service.
3. Create or update a record in the Amazon Route53 private DNS to point to the service
4. **Die**\*

> \* Don't underestimate that last one. This is a short running process, not an ongoing service. You can run it anywhere.\*\*

> \*\* Anywhere sounds a bit bold, but I've tried really hard to make it simple. Here's how:

* This is written in Python using Amazon's boto library that powers their aws-cli project.
* It is packaged and installable from PyPi.
* It installs a console_script that you can use on your laptop, an ECS Container Instance, or an ECS Task Container.
* When run on ECS it needs no configuration. It can even figure out which of your clusters it is running on.
* It is a single Python module that you can import and use.
* I've created an [Automated Build Repository]: on Docker Hub and [it is simple].


### What you do

#### Usage 

As I said, there are a lot of options for how to use it.

I think the most unobtrusive it adding it as an additional container to your existing Task Definition:

    {
        "family": "redis",
        "containerDefinitions": [
            {
                "name": "redis-server",
                "image": "redis",
                "cpu": 10,
                "memory": 800,
                "essential": true
            }
        ]
    }

Task Definition with service discovery:

    {
        "family": "redis-service",
        "containerDefinitions": [
            {
                "name": "redis-server",
                "image": "redis",
                "cpu": 10,
                "memory": 800,
                "essential": true,
                "portMappings": [
                    {
                        "containerPort": 6379,
                        "hostPort": 6379
                    }
                ]
            },
            {
                "name": "service-discovery",
                "image": "richardbronosky/aws-ecs-service-discovery",
                "cpu": 2,
                "memory": 45,
                "entryPoint": ["awsesd"],
                "mountPoints": [
                    {
                        "sourceVolume": "ecs",
                        "containerPath": "/etc/ecs",
                        "readOnly": true
                    }
                ],
                "essential": false
            }

        ],
        "volumes": [
            {
                "name": "ecs",
                "host": {"sourcePath": "/etc/ecs"}
            }
        ]
    }

#### Explanation

1. Task Definition `family` gets `-service` added to the end of it. That's how we know it's a service.
2. Existing `containerDefinitions` entry got `portMappings` added to it.
3. `containerDefinitions` got a new entry for `service-discovery`
4. Task Definition got `volumes` added to it. This is only needed to read one line from one file, but it's an important one. The `ECS_CLUSTER` definition from `/etc/ecs/ecs.config`
 * That's the only way I could find to make this "NO CONFIGURATION NEEDED".

### What it's like

Back when you used to run your MySQL backed PHP app on a single server, you would just use `localhost` for everything. Eventually you realized that you needed to have separate servers for you app and the DB, so you split them up and hopefully skipped hardcoding IP Addresses in your code and went with hostnames. Connecting to mysql-master was easy in your app, and you could ping on the CLI.

But then Amazon came along with their elastic everything and now you never know what IP address anything has or which host it is running on until after it's started. So much for setting up an [Ambassador Pattern].

If all this Elastic Cloud SOA has you wishing it was 2006 again, I've got good news. If you follow a few naming conventions and add this container to your Task Definition files, you're back there. All the naming and addressing is handled for you. Not with a hack. With what is arguably the most power DNS solution on the planet. Amazon Route53.

### Design Goals

... Coming Soon

[Design Goals]: #design-goals
[Automated Build Repository]: https://registry.hub.docker.com/u/richardbronosky/aws-ecs-service-discovery/
[it is simple]: https://registry.hub.docker.com/u/richardbronosky/aws-ecs-service-discovery/dockerfile/
[Ambassador Pattern]: https://docs.docker.com/articles/ambassador_pattern_linking/
