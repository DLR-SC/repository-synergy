# Infra as Code for AWS IoT Greengrass
[![Build Status](https://travis-ci.org/dzimine/greengo.svg?branch=master)](https://travis-ci.org/dzimine/greengo)
![Python 2.7](https://img.shields.io/badge/python-2.7-blue.svg)
![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)
[![PyPI version](https://badge.fury.io/py/greengo.svg)](https://badge.fury.io/py/greengo)

<img src="https://github.com/dzimine/greengo/blob/master/misc/greengo.png?raw=true" width="50px"> Greengo: a tool, and a starter boilerplate project to bring up (and clean-up!) AWS Greengrass setup for play and profit. If you followed the [GreenGrass Getting Started Guide](https://docs.aws.amazon.com/greengrass/latest/developerguide/gg-gs.html), here you find it automated, as code.


Describe your Greengrass group in `group.yaml`, write Lambda functions and device clients, provision Greengrass Core in Vagrant VM, deploy, and clean up.

Inspired by [aws-iot-elf (Extremely Low Friction)](https://github.com/awslabs/aws-iot-elf) and [aws-greengrass-group-setup](https://github.com/awslabs/aws-greengrass-group-setup).

## Pre-requisits

* A computer with Linux/MacOS, Python, git (dah!)
* [Vagrant](https://www.vagrantup.com/docs/installation/) with [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
* AWS CLI [installed](http://docs.aws.amazon.com/cli/latest/userguide/installing.html) and [configured](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html). Consider using [named profiles](https://docs.aws.amazon.com/cli/latest/userguide/cli-multiple-profiles.html).


## Set it Up

Install `greengo` from PyPI:

```
$ pip install greengo
```

Manually [*] download GreenGrassCore binary and place it in the `./downloads` directory.
Sign in to the AWS Management Console, navigate to the AWS IoT console,
and download the AWS Greengrass
Core Software from [Software section](https://us-west-2.console.aws.amazon.com/iotv2/home?region=us-west-2#/
software/greengrass).
Yeah, manual sucks... I will automate it later. Or, submit your PR!


## Play

1. Create GreenGrass Group definition in AWS

    Fancy yourself with the group definitions in `group.yaml`, and run `greengo`:

    ```
    $ greengo create
    ```
    When runs with no errors, it creates all greengrass group artefacts on AWS
    and places certificates and `config.json` for GreenGrass Core in `./certs`
    and `./config` for Vagrant to use in provisioning on next step.


2. Provision VM with GreenGrass Core with Vagrant

    ```
    $ vagrant up
    ```

3. Deploy Greengrass Group to the Core on the VM.

    ```
    $ greengo deploy
    ```

4. Check that everything works - see the ["Check" section](#check-the-deployment)  below.

5. **Profit !**

    Work on it: create, change or remove Lambda functions, subscriptions, resources, and then update Greengrass.

    ```
    $ greengo update
    ```

    Apply your changes by deploying it again:

    ```
    $ greengo deploy
    ```

6. Clean-up when done playing.

    Remove the group definitions on AWS:

    ```
    $ greengo remove
    ```

    Ditch the Vagrant VM:

    ```
    $ vagrant destroy
    ```
For any of the above commands you may specify a different yaml file using
```
$ greengo --config_file <name>.yaml <command>
```
where \<name\> is the name of your yaml and \<command\> is whatever you wish to run

> NOTE: If you want to create a new group but keep the Greengrass Core in the same Vagrant VM,
> you must update it with newly generated certificates and `config.json` file
> before deploying the group, and also reset deployment by getting
> the `deployments/group/group.json` back to virgin.
>
> To do it: login to the Greengrass Vagrant VM and run `/vagrant/scripts/update_ggc.sh` on the Vagrant VM.

## Details

### Check the deployment
How to be sure ~~everything~~ something works? Follow this:

1. Create greengrass group in AWS IoT: `greengo create`.
2. Prepare GGC on the VM: update certificates, reset `group.json`, restart the `greengrassd`.
3. Deploy with `greengo deploy`. Check:
    * Check the deployment status, should be 'Success'
4. Explore Greengrass Core on your vagrant VM.
    * Login to Vagrant VM. You should nkow Vagrant but for the off case: `vagrant ssh`.
    * Check the GGC logs `runtime.log` and `python_runtime.log` under `/greengrass/ggc/var/log/system`. Runtime log should have a line about starting your lambda, or an error why the funtion is not started. In many cases (like not enough memory for Lambda), the deployment is 'Success' but the function fails to start. The errors can only be seen in the `runtime.log`.
      If the function starts successfully, `runtime.log` will contain a message like
    ```
    [2018-03-31T08:48:40.57Z][INFO]-Starting worker arn:aws:lambda:us-west-2:0000000000:function:GreengrassHelloWorld:12
    ```
    * Find and check your own Lambda log under `/greengrass/ggc/var/log/system`.
    * Check the greengrassd process: `ps aux | grep greengrassd`.
      Depending on deployment you might have several processes.       
5. In AWS console, check the MQTT topic with IoT MQTT Test page:
    ```
    REGION=`aws configure get region`; open https://$REGION.console.aws.amazon.com/iot/home?region=$REGION#/test
    ```
    Subscribe to the topic (e.g., `hello/world`), see the messages sent by the Greengrass Lambda function.


### When something goes wrong
At this time `greengo` is just a prototype, a work-in-progress. Therefore it's not *if* but *when* somethings throws out, leaving the setup in half-deployed,
and you gotta pick up the pieces. Remember:

* You are still not worse off doing this manually: you at least have all the `ARN`
and `Id` of all resources to clean-up.
* DON'T DELETE `.gg/gg_state.json` file: it contains references to everything you need to delete. Copy it somewhere and use the `Id` and `Arn` of created resources to clean up the pieces.
* Do what it takes to roll forward - if you're close to successful deployment, or roll-back - to clean things up and start from scratch.

Please pay forward: PR a patch to whatever broke for you to prevent it from happening again.

## Development

Clone the project, set up your environment, install dependencies and setup `greengo` CLI in dev mode:

```
$ git clone https://github.com/dzimine/greengo.git
$ cd greengo
$ virtualenv venv

$ . venv/bin/activate
$ pip install -r requirements.txt
$ pip install -e .
```

Run the unit tests:

```
pytest -s
```
