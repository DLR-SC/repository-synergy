![Travis build status](https://travis-ci.org/revmischa/udo.svg?branch=master)

## Project: *Unemployed DevOps* (UDO)

You have an application you want to deploy into AWS, taking advantage of all of the cool features and services generously provided by Amazon. You have an interest in doing things the Right Way, and not Reinventing The Wheel. You have some modest level of clue.

Have a look at the sample configurations ([simple](udo.sample.simple.yml), [full](udo.sample.yml)) to get an idea of what Udo will manage and how to configure it.

## Quickstart:  

#### Step 1: Configure boto with your AWS credentials
* See: http://boto.readthedocs.org/en/latest/boto_config_tut.html#details

#### Step 2: Install Udo
* `cd tmp; sudo pip install udo`

#### Step 3: Configure Udo
* Create a config file in our project's directory: `cd path/to/myapp/`
* Copy and paste the [sample udo.yml](udo.sample.simple.yml) file and edit it

#### Using Udo
```
$ udo
Valid commands are:
  * lc cloudinit - display cloud-init script
  * lc create - create a launch configuration
  * lc destroy - delete a launch configuration
  * asg instances - print instances in autoscaling groups
  * asg reload - destroy and create an autoscaling group to update the config
  * asg create - create an autoscaling group
  * asg destroy - delete an autoscaling group
  * asg updatelc - updates launchconfiguration in-place
  * asg scale - set desired number of instances
  * asg randomip - print IP address of random host in group
  * asg policies - print autoscaling policies for group
  * asg suspend - suspend autoscaling policies for group
  * asg resume - resume autoscaling policies for group
  * deploy list apps - view CodeDeploy applications
  * deploy list groups - view CodeDeploy application deployment groups
  * deploy list deployments - view CodeDeploy deployment statuses
  * deploy list configs - view CodeDeploy configurations
  * deploy create (group) (commit) - create new deployment for commit on group
  * deploy last - shows status of most recent deployment
  * deploy stop - cancel last deployment
  * version - view udo version installed from PyPI

# create a VPC from our config by name
$ cluster activate dev.webapp

# display our application launchconfig cloud-init script for the dev.webapp role
$ udo lc cloudinit dev.webapp   

# terminates all instances in the qa.webapp group via scaling policy, deletes ASgroup and LC
$ $ udo asg deactivate qa.webapp
Deleting... this may take a few minutes...
. . . . . . . . . . . .
Deleted ASgroup qa.webapp
Deleting launchconfig...
Deleted LaunchConfig qa.webapp

# delete and recreate ASgroup, super easy brain-dead way to reprovision a cluster
$ udo asg reload prod.worker
Are you sure you want to tear down the prod.worker ASgroup and recreate it? (y/n) y
Reloading ASgroup prod.worker
Deleting... this may take a few minutes...
. . . . . . . . . . . . 
Deleted ASgroup prod.worker
Deleting launchconfig...
Deleted LaunchConfig prod.worker
Creating LaunchConfig prod.worker
Activated LaunchConfig prod.worker
Using subnets subnet-cf9a87321, subnet-bfac8123
AZs: ['us-west-2a', 'us-west-2b']
Activated ASgroup prod.worker

# change asgroup desired instance capacity
$ udo asg scale prod.worker 10
Cannot scale: 10 is greater than max_size (7)
Increase max_size to 10? (y/n) y
Changed ASgroup prod.worker desired_capacity from 4 to 10

# deploy with CodeDeploy
$ udo deploy list groups
 - Group: MyApplicpation/stage
$ udo deploy stage 740800da74f1ebee37ed1ee        # N.B. "stage" can be deployment group name or cluster.role name 
Deploying commit 750800da74 to deployment group: stage
 - MyApplicpation/stage
     Created: Friday, 30. January 2015 10:56PM
     Status: InProgress
$ udo deploy list deployments
 - MyApplicpation/stage
     Created: Friday, 30. January 2015 10:56PM
     Status: Success
 [...]
$ udo/main.py deploy last qa.webapp
 - MyApplicpation/qa [d-XISPUQTMD]
     Created: Wednesday, 27 January 2016 12:17PM
     Status: Succeeded
     Message: 
     Commit: d41f2a3a61

# get random IP of an instance in a cluster
# (very handy for SSH)
$ udo asg randomip qa.webapp
52.27.24.11
$ ssh -l ec2-user `udo asg randomip qa.webapp`  # quick way to SSH to a host in a cluster.role

# view cluster status
asg instances stage.webapp
Group         ID          State     Status
stage-webapp  i-565272b1  InService HEALTHY
stage-webapp  i-515272af  InService HEALTHY
stage-webapp  i-e5584916  InService HEALTHY
stage-webapp  i-e1581917  InService HEALTHY

# bonus slack notifications (if configured)
< UdoBot> Changed ASgroup prod.worker desired_capacity from 4 to 10
< UdoBot> Reloading ASgroup prod.worker
< UdoBot> Deleted ASgroup prod.worker
< UdoBot> Deleted LaunchConfig prod.worker
< UdoBot> Activated LaunchConfig prod.worker
< UdoBot> Activated ASgroup prod.worker

# update launchconfig for an existing autoscaling group (bonus feature not provided by AWS or boto)
$ udo asg updatelc dev.webapp
```

# post_deploy_hook
```
    post_deploy_hook:
    - 'curl -X POST https://jenkins.google.com/job/build_job1/buildWithParameters\?DEPLOY_ENV\=production --user jenkins:secrettoken'
    - 'curl -X POST https://jenkins.google.com/job/build_job2/buildWithParameters\?DEPLOY_ENV\=production --user jenkins:secrettoken'
```

## What's all this then, eh?

### What does Udo do?
Udo is a small collection of useful tools for managing clusters in AWS. It uses the python [boto](http://docs.pythonboto.org/en/latest/) library to communicate with the AWS APIs to automate orchestration of clusters and instances, making full use of VPCs and AutoScaling Groups.  
Udo allows you to define your entire operational structure in a straightforward configuration file, and then use the Udo command-line tool to bring up and manage clusters and groups of instances. It takes the tedious work out of creating nearly identical clusters by hand, and automates actions like creating and managing LaunchConfigurations and AutoScaling Groups, parallelizing SSH commands by ASgroup (orchestration without the need for any running services or keeping track of instances), and performing graceful upgrades of instances in an autoscale group without downtime.
Conceptually, all instances in a cluster should be identical and operations should be performed on clusters, not instances. There is a hierarchy of configuration values that should be applied at different levels of clusters and sub-clusters, and the [configuration schema](config.sample.yml) takes that into account.  
Udo can be used to automate deployments with [AWS CodeDeploy](http://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html) and you don't even need to access your instances ever. Deploys commits straight from GitHub. [Deployment from S3 is a simple modification](http://docs.aws.amazon.com/codedeploy/latest/userguide/how-to-push-revision.html).


### What do _you_ do?
Most development projects utilize several distinct sets of environments, such as dev, qa, stage, production. These clusters are generally partitioned into different roles, such as a web application server, asynchronous worker machine, monitoring and so on.  
If you wish to set this up in AWS, you should script creating environments, provisioning instances based on roles and creating different parameters for each type of instance you want ("dev webapp servers should be of type m3.medium", "production workers should use an autoscaling policy with a minimum of 3 instances", etc..).
You *could* do all of this work yourself, or you could just use Udo.

### What _should_ you do?
EC2 is not a datacenter in the cloud. If you're using it like a traditional managed hosting company, you are probably doing things wrong. You should take advantage of the specialized infrastucture and APIs provided by AWS, like AutoScaling Groups and `boto`.  
If you're making an AMI per role, you may be doing things wrong. You should be able to automatically deploy your entire application onto a stock Amazon Linux AMI, though making one with some of your app already installed to save time isn't a bad idea.  
If you're using Ansible, Puppet, Chef, or care about keeping track of hostnames/IPs, you're almost definitely doing things wrong. You aren't maintaining machines that are going to necessairly exist for any length of time, and you should be able to kill off instances at will as well as spawn and fully provision a new instance from scratch without even thinking about it. There's no reason you should need to keep track of an individual instance.  
Configuration management tools impose extra overhead and complexity for the ability to diff between the state of a running machine and the desired state. This capability is unneeded when you can simply trash the instance and bring a new one up with imperative commands.  
Many people are continuing to do extra work by invoking these tools due to momentum. Please stop and ask yourself if they are necessary, and if so, what could you be doing to make your instances not require configuration management in the first place, such as CodeDeploy, cloud-init and AutoScaling groups. 

### Does this work?
We've been using this in production for a decent length of time with minimal trouble. It's been very handy for managing groups of instances without the need for any special services running on them. We mostly use it for turning QA clusters off when not in use, cleanly reprovisioning instances, and updating launchconfigurations in place on production (something you cannot currently do with the AWS GUI or CLI). 
Several Amazon engineers have reviewed Udo and given it their seal of approval. They said that many companies have similar internal tools, but they don't open-source them. Hopefully this code will save someone some effort and provide a central point where efforts can be focused. 


### Summary of a proper AWS setup:

#### Your job:
- Describe your architecture in `config.yml`.
- Create VPCs, LaunchConfigurations and Autoscaling Groups from your config with Udo
- Have some very simple way of setting up your app. One recommendation is to install your application and configs via RPMs, though this is not required.
- Optional: stick your RPMs in a private S3 repo and authenticate access via [yum-s3-iam](https://github.com/seporaitis/yum-s3-iam).
- Optional: create [CodeDeploy](http://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html) groups linked to GitHub and your Autoscaling Groups.

#### Udo takes care of:
- LaunchConfigs per role, in a VPC and AutoScaleGroup per cluster.
- Apply tags to instances to identify their roles.
- Bringing clusters up and down and reprovisioning them, using ASgroups to track membership and SSH for orchestration.
- Installing a cloud-init script to provision instances. You can add your own commands to it via config.
- Using RPMs to provision instances (optional)
- Updating launchconfig and asgroup parameters on the fly
- Scaling number of instances in an asgroup
- Automating CodeDeploy revision creation and monitoring

### Known Issues
#### CodeDeploy:
* When daemonizing in a CodeDeploy script hook, you must redirect stdout and stderr: `script.sh 1>/dev/null 2>&1 &` instead of `script.sh &` (For any jobs running in background)
* If the user linking a private repo that you deploy from loses permission, your deployments will fail with 404 errors. You need to re-link GitHub OAuth access via a secret button that can only be found if you re-create the deployment group. This is not really documented.
* For the current autoscaling behavior, When a new autoscaling instance spins up we deploy the last successfuly deployed revision for that deployment group to it and only put the instance in service if that deployment succeeded.For the GitHub case, it is possible to deploy a known commit to a deployment group however, we have yet to impliment branch tracking, so simply saying deploy HEAD is not supported at this time. We have filed a feature request with Amazon to support this.
* UPDATE: [Waiters are added](https://github.com/boto/botocore/pull/977) - @danhimalplanet says he is working on Udo support for them

### Waiters
* boto3 introduced "waiters" which allow you to wait for certain actions to complete. Unfortunately no waiters currently exist when performing AutoScaling or CodeDeploy actions. We have a feature request filed to support this.

### Credits
* Sponsored by [The DevOps League](http://devopsleague.com/)
