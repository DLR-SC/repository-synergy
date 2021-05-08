# any-saas

The premise behind `any-saas` is more an implementation of something theoretical than it is practical to use.

In July, a site called Try RethinkDB was launched. The premise? Using [http://docker.io](Docker) containers, it was very simple to create a SaaS to allow people to use your software without any upfront investment. All a user had to do was click a button for their own sandboxed environment.

## So, what is this?

Using this package will allow you to have a starting point for creating your own SaaS for any Docker image of your choice.

I recently modified it (and the template shows) to be a MongoDB SaaS by default. In about 15 lines of code.

## Code Review

`api.py` is the main entrypoint. This code ensures the environment has been configured properly or exits if it hasn't. It sets up a main flask app and then starts it on port 5000 (defualt)

### api.new()

You could say here's where the magic happens. Using [http://github.com/dotcloud/docker-py](docker-py) we connect to the configured `DOCKER_HOST` to instantiate and get some information about a new Docker container.

Right now, dynamic routing is managed by [http://github.com/dotcloud/hipache](Hipache) - my favorite reverse proxy.

Configuration is managed by Redis, and adding the route is as simple as `rpush`ing some values to a key.


### launch

This file makes a few assumptions:

1. You're using hipache
2. You're deploying any-saas as a container (named trymongo-website)

Other than that, modifying a few keys is all that's needed to make your own mongodb SaaS work out of box.



