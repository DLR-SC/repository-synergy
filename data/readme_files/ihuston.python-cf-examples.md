Python Cloud Foundry Examples
=============================

Author: [Ian Huston](http://ianhuston.net) [@ianhuston](http://twitter.com/ianhuston)

License: See LICENSE.txt in each example code folder

First presented at [PyData London 2015](http://london.pydata.org).

This tutorial is an introduction to deploying Python applications
to [Cloud Foundry](http://cloudfoundry.org) and covers:

* Pushing your first application to Cloud Foundry
* Using a custom buildpack to use PyData packages in your app
* Adding data services like Redis to your app

Each example app is self-contained and can be deployed to a Cloud Foundry
instance with

    $ cf push

The slides are available [on Speakerdeck](https://speakerdeck.com/ihuston/pydata-london-2015-getting-started-with-cloud-foundry-for-data-science). There is also a [full length video](https://www.youtube.com/watch?v=lp2c05yDJko) of this tutorial from PyData London 2015.

A [shorter version of these notes](./helper-notes.md), which can be used by assistants in the tutorial
is also provided.

### Changes:

*Update 03/10/2016*: The official CF Python buildpack now includes support for the conda package manager.
This means there is no need to use a separate community buildpack to run apps using PyData packages.
The tutorial has been updated to reflect this.

*Update 23/11/2015*: These sample apps have been updated to use the [new Diego runtime](http://support.run.pivotal.io/entries/105844873-Migrating-Applications-from-DEAs-to-Diego). 
The main difference is that app instances all run on the same port inside different containers.
The first sample app has been changed to show the instance number rather than the port so that multiple instances can be recognised. 

### Getting Started

If you do not have an account on a Cloud Foundry installation you can
register for a free trial at [Pivotal Web Services (PWS)](http://run.pivotal.io).

Download the Cloud Foundry Command Line Interface from the CF management console
or [the CF Github repo](https://github.com/cloudfoundry/cli).
This provides the `cf` command which you will use to interact with a CF installation.

Target the CF installation API with `cf api`. For example for PWS:

    $ cf api https://api.run.pivotal.io

### Pushing your first app

The first app is in the folder `01-simple-python-app`.
Have a look at the code and then deploy using `cf push`.

    $ cd 01-simple-python-app
    $ cf push

You can inspect the app's streaming logs using `cf logs myapp`.

You can scale your app by changing the number of instances and the available RAM:

    $ cf scale myapp -i 5
    $ cf scale myapp -m 256M

### Pushing an app with PyData dependencies

The second app is in the folder `02-pydata-spyre-app`.
This app is built using [Spyre](https://github.com/adamhajari/spyre) by Adam Hajari.

This application uses a new feature of the official [Python buildpack](https://github.com/cloudfoundry/python-buildpack/)
to provision dependencies using `conda`.

The `environment.yml` file contains the `conda` environment specification.
The buildpack detects this file and uses `conda` instead of `pip` to install the dependencies.

Push the app using `cf push` and visit the app URL to see a simple interactive visualisation.

    $ cd ../02-pydata-spyre-app
    $ cf push

### Using data services

The third app is in the folder `03-services-redis`.

Services provide persistent storage and other useful resources for your applications.

First, create a free Redis service provided by Rediscloud:

    $ cf create-service rediscloud 30mb myredis

You can bind this to your apps making it available via the `VCAP_SERVICES`
environmental variable.

    $ cf bind-service myapp myredis

Look at the environmental variables your app has with `cf env myapp`.

Now you can push the third app which uses Redis as its backing store.

    $ cd ../03-services-redis
    $ cf push

The manifest specifies that this app should be bound to the myredis service instance that you just created.

### Putting it all together

The fourth app is in the folder `04-learning-api`.

We can put everything we've learned into practice by building our own simple
machine learning API.

    $ cd ../04-learning-api
    $ cf push

This is a simplified version of [a project](https://github.com/alexkago/ds-cfpylearning)
by [Alex Kagoshima](http://twitter.com/akagoshima).

**Don't forget to stop all your apps when you are finished by doing the following:**

    $ cf stop myapp
    $ cf stop sinewave
    $ cf stop testredis
    $ cf stop learning-api

### Resources

* [Cloud Foundry documentation](http://docs.cloudfoundry.org)
* [Pivotal Web Services](http://run.pivotal.io)
* [CF Summit Videos](https://www.youtube.com/playlist?list=PLhuMOCWn4P9g-UMN5nzDiw78zgf5rJ4gR)
* [CF Meetups](http://cloud-foundry.meetup.com)
* [Slides for this tutorial](https://speakerdeck.com/ihuston/pydata-london-2015-getting-started-with-cloud-foundry-for-data-science)
* [Video of this tutorial](https://www.youtube.com/watch?v=lp2c05yDJko)
