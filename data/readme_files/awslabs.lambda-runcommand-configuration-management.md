# What's That Smell?
This project, affectionately referred to as GARLC, is a demonstration of combining multiple [AWS](https://aws.amazon.com/) services.

Project GARLC is made up of:
* [Git](https://git-scm.com/) – for configuration storage and version control.  GitHub is used for the project currently but you could also use [AWS CodeCommit](https://aws.amazon.com/codecommit/).
* [Ansible](https://www.ansible.com/) – for configuration management.  Chef, Puppet, or Salt using their respective “masterless” or “solo” modes could also be used.
* [Amazon EC2 Run Command](https://aws.amazon.com/ec2/run-command/) – for executing Ansible without requiring SSH access to the instances.
* [AWS Lambda](https://aws.amazon.com/lambda/) – for executing logic and invoking RunCommand.
* [AWS CodePipeline](https://aws.amazon.com/codepipeline/) – for receiving changes from git and triggering Lambda.

The general idea is that configuration management is now done in the same way we do continuous delivery of applications today.  What makes GARLC really exciting though is that there are no central control/orchestration servers to maintain and we no longer need SSH access to the instances to configure them.  There are two modes to Project GARLC:  continuous and bootstrap.

## Continuous Mode
In this mode, configuration management of instances is done automatically, using the above technologies, as configurations are committed to version control.  Ansible is an agentless automation and management tool driven by the use of YAML based Playbooks. The idea is that you store idempotent Ansible Playbooks in GitHub and when changes are merged into the master branch CodePipeline picks them up.  

CodePipeline is a continuous delivery service that goes through a series of stages.  In the case of GARLC we use two stages: a Source stage that checks GitHub for changes and an Invoke stage that triggers an AWS Lambda function.  This AWS Lambda function does several things, including invoking Run Command.

Run Command is a service that allows you to easily execute scripts or commands on an EC2 Instance.  It requires an agent on each instance and can execute commands with administrative privilege on the system.  To speed things up, we recommend creating an AMI that already has the Run Command agent installed (the demo uses a public AMI with the agent pre-installed as well as Ansible).  For GARLC, we use Run Command to execute Ansible, in local mode, on each instance.  Ansible will configure each instance (e.g. install software, modify configuration files, etc) according to a set of roles that are associated with each instance (set via [Tags](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html)).  This allows for instances to be automatically updated in a continuous delivery style manner without requiring direct access to each instance.

## Bootstrap Mode
Bootstrap mode is done similarly to continuous mode except it includes the addition of [Amazon CloudWatch Events](http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatchEvents.html) and is performed outside the CodePipeline flow.  CloudWatch Events lets us define a Rule that takes action when something happens.  For GARLC, we create a Rule that invokes an AWS Lambda function any time any instance enters the “Running” state.  Like above, the Lambda function will trigger Run Command on the instance with commands to run Ansible locally and configure the host.  The latest artifact in the S3 bucket from continuous mode will be used for configuration.  The two modes together cover new instances starting up and changes to existing instances.

# Setup Instructions for a Demo
**WARNING:  Using this code may cost you money.  Please be sure you understand your current usage and the costs associated with this reference code before launching in your AWS account.**

1. Fork this repo.
* Install [Terraform](https://www.terraform.io/downloads.html) to help setup the infrastructure required for GARLC.
* Manually create a [CodePipeline using the AWS Console](http://docs.aws.amazon.com/codepipeline/latest/userguide/how-to-create-pipelines.html) with a single stage for now:
  * Source stage should fetch from your fork of this repo on the master branch.
    * Output should be "MyApp".
  * NOTE:  When using the AWS Console to create your Pipeline you will be forced to add a "Beta" stage which you can later delete and replace with the Invoke stage.  Just add whatever to get through the wizard.
* From the parent directory of your fork run the below to setup the infrastructure.  This will create IAM Roles, the Lambda function, and a couple Auto-Scaling Groups in us-west-2:
  1. `terraform get terraform`
  * `terraform plan terraform`
  * `terraform apply terraform`
* Go back to CodePipeline and add a second stage for an "Invoke" action on the "garlic" Lambda function created with Terraform in the previous step.
    * Input should be "MyApp".
* Update something in the repository (e.g. add something to an Ansible playbook) and then commit to the master branch and watch your changes flow and your instances update automagically :fire:.

# Additional Information

## More Details on AWS Lambda
There are two AWS Lambda functions in use with the continuous mode.  The [first Lambda function](https://github.com/awslabs/lambda-runcommand-configuration-management/blob/master/lambda/main.py) is basically a worker that puts all the pieces together so Run Command can do the heavy lifting.  The Lambda function does several things:

1.	The Lambda function will find all EC2 instances with a tag of “has_ssm_agent” and a value of “true” or “True”.  This is used to find instances that have the SSM agent (Run Command) installed and are configured with the proper [Instance Profile](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ssm-iam.html) that allows SSM to be run.  When you provision instances you should make sure each one gets this tag.
2.	It breaks the list of instances from Step 1 up into smaller chunks that will be processed by a second Lambda function I will talk about later.  This is done in order to scale the solution and stay under rate limits for the Run Command service.
3.	It parses the incoming event from CodePipeline which contains metadata about the location of the artifact.  The artifact is simply the content of the git repository zipped up and stored in [Amazon S3](https://aws.amazon.com/s3/).  The instances will fetch this later to execute the Ansible Playbook(s).
4.	The Lambda function will then build a list of commands that will be sent with Run Command.
  *	The first command connects to S3 to retrieve the artifact mentioned in step 2 above.
  * The next command unpacks the zip in the /tmp directory on the instance.
  * The next command runs a shell script to build an Ansible Inventory file locally.  More on this in the next section.
  * The final command runs ansible-playbook on the instance to configure it.
5.	The last part of the Lambda Function is an API call to invoke a second Lambda function which I will detail next.

The [second Lambda function](https://github.com/awslabs/lambda-runcommand-configuration-management/blob/master/lambda/runcommand_helper.py) is responsible for invoking Run Command via an API call.  This Lambda expects to be passed in a list of Instance ID’s broken down into chunks (a list of lists) and a list of commands to be sent to the instance.  The Lambda function will process one chunk, pop that chunk off the list, and then invoke a new instance of the same Lambda function to pick up the work.  The reason for doing this is it ensures we always stay under the Run Command API limits and we never have to worry about hitting the max timeout for an AWS Lambda function; we can infinitely scale the solution to however many instances we have.

In bootstrap mode there is only a [single AWS Lambda function](https://github.com/awslabs/lambda-runcommand-configuration-management/blob/master/lambda/bootstrap.py) that essentially combines the behavior of the two Lambda functions in continuous mode.  There are a few differences, though:
*	We are provided a single Instance ID per CloudWatch Event trigger, so we do not need to find Instances.  
*	We have to determine if the instance CloudWatch Event’s sent is actually an instance we should try to perform Run Command on (e.g. does it have the has_ssm_agent tag?).
*	We have to find the latest artifact from the CodePipeline bucket.  This artifact will be the one retrieved by the instance to configure itself.

This Lambda function deals with all of these and also includes retry logic in case the Run Command API limits have been exceeded.  

## Ansible for Configuration Management
If you need a primer on Ansible I highly recommend [this blog post](https://serversforhackers.com/an-ansible-tutorial).  Understanding Roles in Ansible is critical in fully recognizing how GARLC coordinates configuration of instances.

Ansible can be run locally and doesn’t require any sort of centralized master and this was important to get the “serverless” checkbox ticked.  To leverage Ansible with GARLC we need a few things in place:  an “Ansible_Roles” tag for each instance, playbook roles in Ansible equivalent to the roles defined in the Ansible_Roles tag, and a local Ansible inventory file on each instance.

When provisioning your instances, each one should get a tag named “Ansible_Roles” with a value that contains a comma separated list of role names.  For example, an instance might have an Ansible_Roles tag with the value “webserver, appserver, memcached” which would presumably indicate the instance should get the necessary software to be a web server that hosts an application along with some caching.  Using this example, we would then need at least three roles defined in our Ansible playbooks and committed to GitHub to build the instance.  These three roles should be named just like above:  webserver, appserver, and memcached.  

To tie this together a [script](https://github.com/awslabs/lambda-runcommand-configuration-management/blob/master/generate_inventory_file.sh) is run that builds a local Ansible inventory file describing which roles should be applied to the instance.  This inventory file is generated based on the Roles tag, mentioned above, and its values.  The script also sets the connection mode to [local](http://docs.ansible.com/ansible/intro_inventory.html) which bypasses an attempted SSH connection.  When ansible-playbook is run it will look for this local inventory file (/tmp/inventory) and then execute any playbooks associated with the roles.  If the Roles of an instance change, next run a new inventory file be generated and the instance will get updated appropriately.

## Performance and Shortcomings
In bootstrap mode a new instance takes about 1.5 seconds for the Lambda function and Run Command then usually configures the instance within a minute or two unless there are many jobs queued up.  With the continuous mode, it takes about 15 seconds for the first Lambda to handle 1,000 instances and about 1 second for each Run Command helper Lambda function to process a chunk.  A complete run for 1,000 instances takes about 5 minutes to process and then additional time for Run Command to complete (roughly 10 more minutes to get through all 1,000 in testing).

There is currently no reporting or visualization of Run Command jobs making it difficult to see what failed and when.  The Run Command console can be used, but when working in the hundreds or thousands of instance this quickly becomes unwieldy.

The example provided in this repository currently only supports Linux hosts that are capable of running the [SSM agent](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/install-ssm-agent.html).  However, Windows is a supported Operating System for both Ansible and Run Command.

Instances require Internet access in order for Run Command to work.

# Theme Song
No ssh here,  
sudo git me a beer,   
while I Ansible all the things.

Swaggin with RunCommand,  
Lambda don’t move a hand,   
flowin through the CodePipeline.  

Smells like GARLC, GARLC, GARLC…  
Smells like GARLC, GARLC, GARLC…  
Smells like GARLC, GARLC, GARLC…  

# License
Copyright 2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance with the License. A copy of the License is located at

    http://aws.amazon.com/apache2.0/

or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

Note: Other license terms may apply to certain, identified software files contained within or distributed with the accompanying software if such terms are included in the directory containing the accompanying software. Such other license terms will then apply in lieu of the terms of the software license above.
