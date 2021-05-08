# Getting started with ECS

**Quick jump:**

* [Workshop overview](https://github.com/abby-fuller/ecs-demo/blob/master/README.md#overview-of-workshop)
* [Setting up the VPC](https://github.com/abby-fuller/ecs-demo/blob/master/README.md#setting-up-the-vpc)
* [Setting up the IAM Roles](https://github.com/abby-fuller/ecs-demo/blob/master/README.md#setting-up-your-iam-roles)
* [Configuring the AWS CLI](https://github.com/abby-fuller/ecs-demo/blob/master/README.md#configuring-the-aws-cli)
* [Creating the Container registries with ECR](https://github.com/abby-fuller/ecs-demo/blob/master/README.md#creating-the-container-registries-with-ecr)
* [Prepping our Docker Images](https://github.com/abby-fuller/ecs-demo/blob/master/README.md#prepping-our-docker-images)
* [Pushing our tested images to ECR](https://github.com/abby-fuller/ecs-demo/blob/master/README.md#pushing-our-tested-images-to-ecr)
* [Creating the ALB](https://github.com/abby-fuller/ecs-demo/blob/master/README.md#creating-the-alb)
* [Creating the Task Definitions](https://github.com/abby-fuller/ecs-demo/blob/master/README.md#create-your-task-definitions)
* [Create your Services](https://github.com/abby-fuller/ecs-demo/blob/master/README.md#create-your-services)
* [Testing our Service deployments from the Console and ALB](https://github.com/abby-fuller/ecs-demo/blob/master/README.md#testing-our-service-deployments-from-the-console-and-the-alb)
* [More in-depth logging with Cloudwatch](https://github.com/abby-fuller/ecs-demo/blob/master/README.md#more-in-depth-logging-with-cloudwatch)


## Overview of workshop

This workshop introduces the basics of working with [ECS](https://aws.amazon.com/ecs/).  This includes:  setting up the initial ECS cluster, and deploying two services, with traffic routed through an [ALB](https://aws.amazon.com/elasticloadbalancing/applicationloadbalancer/).

Prior to beginning the workshop, you'll need to complete a few set up steps: 

* [Have a working AWS account](<https://aws.amazon.com>)
* [Have a working Github account](<https://www.github.com>)
* [Install the AWS CLI](<http://docs.aws.amazon.com/cli/latest/userguide/installing.html>)
* [Have Docker installed locally](<https://docs.docker.com/engine/installation/>)

To check if you have the AWS CLI installed and configured:

    $ aws --version
    
This should return something like:

    $ aws --version
    aws-cli/1.11.36 Python/2.7.13 Darwin/16.4.0 botocore/1.4.93

To check if you have Docker installed:

    $  which docker

This should return something like:

    $ which docker
    /usr/bin/docker


Once you've completed these steps, you're ready to start the workshop!


## Setting up the VPC

Once you've signed into your AWS account, navigate to the [ECS console](https://console.aws.amazon.com/ecs/home?region=us-east-1#/clusters).  If you've never used ECS before, you can use the [first run wizard](https://console.aws.amazon.com/ecs/home#/firstRun) which will set up your cluster, a dummy service, and a VPC for you.  If you don't want to use the wizard, you can use the [Cloudformation template included in this repo](https://github.com/abby-fuller/ecs-demo/blob/master/ecs-demo-cf.yml), and create a new VPC.

Running the Cloudformation template or the first run wizard should result in something like this:

![cloudformation output](https://github.com/abby-fuller/ecs-demo/blob/master/images/cloudformation_output.png)

## Setting up your IAM roles

In order to work with the AWS CLI, you'll need an IAM role with the proper permissions set up.  To do this, we'll create both an IAM Group, and an IAM user.

To create the group, naviate to the IAM console, and select **Groups** > **Create New Group**.  Name the group "**ecs-demo**".  From the list of managed policies, add the following policies:

![add IAM group](https://github.com/abby-fuller/ecs-demo/blob/master/images/ecs_demo_iam_role.png)

Once you've created your group, you need to attach it to a user.  If you already have an existing user, you can add it to the ecs-group.  If you don't have a user, or need to create a new one, you can do so by going to **Users** > **Add User**:

![add new user](https://github.com/abby-fuller/ecs-demo/blob/master/images/new_iam_user.png)

Name your user something like "**ecs-demo-user**".  From the next step in the wizard, add your user to the "**ecs-demo**" group that we created in the previous step:

![add user to group](https://github.com/abby-fuller/ecs-demo/blob/master/images/add_user_iam_group.png)

When the wizard finishes, make sure to copy or download your access key and secret key.  You'll need them in the next step.

## Configuring the AWS CLI

If you've never configured the AWS CLI, the easiest way is by running:

    $ aws configure

This should drop you into a setup wizard:

    $ aws configure
    AWS Access Key ID [****************K2JA]: 
    AWS Secret Access Key [****************Oqx+]: 
    Default region name [us-east-1]: 
    Default output format [json]: 

If you already have a profile setup with the AWS CLI, you can also add a new profile to your credentials file.

You can test that your IAM user has the correct permissions, and that your CLI is setup to connect to your AWS account by running the command to obtain an ECR authentication token.  This will allow us to pull our registries in the next step:

    $ aws ecr get-login --region us-east-1

This should output something like:

    $ docker login -u AWS -p AQECAHhwm0YaISJeRtJm5n1G6uqeekXuoXXPe5UFce9Rq8/14wAAAy0wggMpBgkqhkiG9w0BBwagggMaMIIDFgIBADCCAw8GCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQM+76slnFaYrrZwLJyAgEQgIIC4LJKIDmvEDtJyr7jO661//6sX6cb2jeD/RP0IA03wh62YxFKqwRMk8gjOAc89ICxlNxQ6+cvwjewi+8/W+9xbv5+PPWfwGSAXQJSHx3IWfrbca4WSLXQf2BDq0CTtDc0+payiDdsXdR8gzvyM7YWIcKzgcRVjOjjoLJpXemQ9liPWe4HKp+D57zCcBvgUk131xCiwPzbmGTZ+xtE1GPK0tgNH3t9N5+XA2BYYhXQzkTGISVGGL6Wo1tiERz+WA2aRKE+Sb+FQ7YDDRDtOGj4MwZ3/uMnOZDcwu3uUfrURXdJVddTEdS3jfo3d7yVWhmXPet+3qwkISstIxG+V6IIzQyhtq3BXW/I7pwZB9ln/mDNlJVRh9Ps2jqoXUXg/j/shZxBPm33LV+MvUqiEBhkXa9cz3AaqIpc2gXyXYN3xgJUV7OupLVq2wrGQZWPVoBvHPwrt/DKsNs28oJ67L4kTiRoufye1KjZQAi3FIPtMLcUGjFf+ytxzEPuTvUk4Xfoc4A29qp9v2j98090Qx0CHD4ZKyj7bIL53jSpeeFDh9EXubeqp6idIwG9SpIL9AJfKxY7essZdk/0i/e4C+481XIM/IjiVkh/ZsJzuAPDIpa8fPRa5Gc8i9h0bioSHgYIpMlRkVmaAqH/Fmk+K00yG8USOAYtP6BmsFUvkBqmRtCJ/Sj+MHs+BrSP7VqPbO1ppTWZ6avl43DM0blG6W9uIxKC9SKBAqvPwr/CKz2LrOhyqn1WgtTXzaLFEd3ybilqhrcNtS16I5SFVI2ihmNbP3RRjmBeA6/QbreQsewQOfSk1u35YmwFxloqH3w/lPQrY1OD+kySrlGvXA3wupq6qlphGLEWeMC6CEQQKSiWbbQnLdFJazuwRUjSQlRvHDbe7XQTXdMzBZoBcC1Y99Kk4/nKprty2IeBvxPg+NRzg+1e0lkkqUu31oZ/AgdUcD8Db3qFjhXz4QhIZMGFogiJcmo= -e none https://<account_id>.dkr.ecr.us-east-1.amazonaws.com
 
To login to ECR, copy and paste that output or just run `` `aws ecr get-login --region us-east-1` `` which will tell your shell to execute the output of that command.  That should return something like:

    WARNING: login credentials saved in /home/vagrant/.dockercfg.
    Login Succeeded

Note:  if you are running Ubuntu, it is possible that you will need to preface your Docker commands with `sudo`.  For more information on this, see the [Docker documentation](https://docs.docker.com/engine/installation/linux/ubuntu/).

If you are unable to login to ECR, check your IAM user group permissions.


## Creating the container registries with ECR

Before we can build and push our images, we need somewhere to push them to.  In this case, we're going to create two repositories in [ECR](https://aws.amazon.com/ecr/).

To create a repository, navigate to the ECS console, and select **Repositories**.  From there, choose **Create repository**.

Name your first repository **ecs-demo-web**:

![create ecr repository](https://github.com/abby-fuller/ecs-demo/blob/master/images/ECR_repo_setup.png)

Once you've created the repository, it will display the push commands.  Take note of these, as you'll need them in the next step.  The push commands should like something like this:

![push commands](https://github.com/abby-fuller/ecs-demo/blob/master/images/push_commands.png)

Once you've created the ecs-demo-web, repeat the process for a second repository.  This one should be named **ecs-demo-api**.  Take note of the push commands for this second repository, also.  Push commands are unique per repository.


## Prepping our Docker images

If you haven't already, clone this repository:

    $ git clone git@github.com:abby-fuller/ecs-demo.git

Our first step is the build and test our containers locally.  If you've never worked with Docker before, there are a few basic commands that we'll use in this workshop, but you can find a more thorough list in the [Docker "Getting Started" documentation](https://docs.docker.com/engine/getstarted/).

To start your first container, go to the `web` directory in the project:

    $ cd <path/to/project>/ecs-demo/web

To build the container:

    $ docker build -t ecs-demo-web .

This should output steps that look something like this:

    $ docker build -t ecs-demo-web .
    Sending build context to Docker daemon 4.096 kB
    Sending build context to Docker daemon 
    Step 0 : FROM ubuntu:latest
     ---> 6aa0b6d7eb90
    Step 1 : MAINTAINER abbyfull@amazon.com
     ---> Using cache
     ---> 3f2b91d4e7a9
  
If the container builds successfully, the output should end with something like this:
 
     Removing intermediate container d2cd523c946a
     Successfully built ec59b8b825de
 
To run your container:
 
     $  docker run -d -p 3000:3000 ecs-demo-web
     
To check if your container is running:
 
     $ docker ps 

This should return a list of all the currently running containers.  In this example,  it should just return a single container, the one that we just started:

    CONTAINER ID        IMAGE                 COMMAND             CREATED              STATUS              PORTS                              NAMES
    fa922a2376d5        ecs-demo-web:latest   "python app.py"     About a minute ago   Up About a minute   3000/tcp,    0.0.0.0:3000->3000/tcp   clever_shockley   
  
To test the actual container output:
 
     $ curl localhost:3000/web
     
This should return:

     hi!  i'm served via Python + Flask.  i'm a web endpoint.
 

To test the api container, repeat the same process from the `/api` directory:

    $ cd <path/to/project>/ecs-demo/api 
    $ docker build -t ecs-demo-api .
    $ docker run -d -p 8000:8000 ecs-demo-api
    $ curl localhost:8000/api

The API container should return:

    hi!  i'm ALSO served via Python + Flask.  i'm a second web endpoint.


## Pushing our tested images to ECR

Now that we've tested our images locally, we need to tag them again, and push them to ECR.  This will allow us to use them in TaskDefinitions that can be deployed to an ECS cluster.  

You'll need your push commands that you saw during registry creation.  If you've misplaced your push commands, you can find them again by going back to the repository (**ECS Console** > **Repositories** > Select the Repository you want to see the commands for > **View Push Commands**.

To tag and push the web repository:

    $ docker tag ecs-demo-web:latest <account_id>.dkr.ecr.us-east-1.amazonaws.com/ecs-demo-web:latest
    $ docker push <account_id>.dkr.ecr.us-east-1.amazonaws.com/ecs-demo-web:latest

This should return something like this:

    The push refers to a repository [<account_id>.ecr.us-east-1.amazonaws.com/ecs-demo-web] (len: 1)
    ec59b8b825de: Image already exists 
    5158f10ac216: Image successfully pushed 
    860a4e60cdf8: Image successfully pushed 
    6fb890c93921: Image successfully pushed 

    aa78cde6a49b: Image successfully pushed 
    Digest: sha256:fa0601417fff4c3f3e067daa7e533fbed479c95e40ee96a24b3d63b24938cba8

To tag and push the api repository:

    $ docker tag ecs-demo-api:latest <account_id>.dkr.ecr.us-east-1.amazonaws.com/ecs-demo-api:latest
    $ docker push <account_id>.dkr.ecr.us-east-1.amazonaws.com/ecs-demo-api:latest


Note: why `:latest`?  This is the actual image tag.  In most production environments, you'd tag images for different schemes:  for example, you might tag the most up-to-date image with `:latest`, and all other versions of the same container with a commit SHA from a CI job.  If you push an image without a specific tag, it will default to `:latest`, and untag the previous image with that tag.  For more information on Docker tags, see the Docker [documentation](https://docs.docker.com/engine/getstarted/step_six/). 

You can see your pushed images by viewing the repository in the AWS Console.  Alternatively, you can use the CLI:

    $ aws ecr list-images --repository-name=ecs-demo-api
    {
        "imageIds": [
            {
                "imageTag": "latest", 
                "imageDigest": "sha256:f0819d27f73c7fa6329644efe8110644e23c248f2f3a9445cbbb6c84a01e108f"
            }  
        ]
    }

## Creating the ALB

Now that we've pushed our images, we need an Application Load Balancer (ALB)[https://aws.amazon.com/elasticloadbalancing/applicationloadbalancer/] to route traffic to our endpoints. Compared to a traditional load balancer, an ALB lets you direct traffic between different endpoints.  In our example, we'll use two separate endpoints:  `/web` and `/api`.

To create the ALB:

Navigate to the **EC2 Service Console**, and select **Load Balancers** from the left-hand menu.  Choose **Create Load Balancer**:

![choose ALB](https://github.com/abby-fuller/ecs-demo/blob/master/images/choose_ALB.png)

Name your ALB **ecs-demo** and add an HTTP listener on port 80:

![name ALB](https://github.com/abby-fuller/ecs-demo/blob/master/images/create_alb.png)

Note:  in a production environment, you should also have a secure listener on port 443.  This will require an SSL certificate, which can be obtained from [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/), or from your registrar/any CA.  For the purposes of this demo, we will only create the insecure HTTP listener.  DO NOT RUN THIS IN PRODUCTION.

Next, select your VPC and add at least two subnets for high availability.  Make sure to choose the VPC that we created during the ECS first-run wizard (or with the Cloudformation template).  If you have multiple VPC, and you're not sure which VPC is the correct one, you can find its ID from the VPC console, or by viewing the outputs of the Cloudformation stack.

![add VPC](https://github.com/abby-fuller/ecs-demo/blob/master/images/configure_elb.png)

Next, add a security group.  If you ran the ECS first run wizard, you should have an existing group called something like **EC2ContainerService-ecs-demo-EcsSecurityGroup**.  If you don't have this, check you've chosen the correct VPC, as security groups are VPC specific.  If you still don't have this, you can create a new security groups with the following rule:

    Ports	    Protocol	    Source	
     80	          tcp	       0.0.0.0/0	

Choose the security group, and continue to the next step:  adding routing.  For this initial setup, we're just adding a dummy healthcheck on `/`.  We'll add specific healthchecks for our service endpoints when we register them with the ALB.

![add routing](https://github.com/abby-fuller/ecs-demo/blob/master/images/configure_alb_routing.png)

Finally, skip the "Register targets" step, and continue to review. If your values look correct, click **Create**.

Note:  If you created your own security group, and only added a rule for port 80, you'll need to add one more.  Select your security group from the list > **Inbound** > **Edit** and add a rule to allow your ALB to access the port range for ECS (0-65535).  The final rules should look like:

     Type        Ports        Protocol        Source	
     HTTP          80	        tcp	         0.0.0.0/0
     All TCP      0-65535       tcp       <id of this security group>
     

## Create your Task Definitions

Before you can register a container to a service, it needs be a part of a Task Definition. Task Definitions define things like environment variables, the container image you wish to use, and the resources you want to allocate to the service (port, memory, CPU).  To create a Task Definition, choose **Task Definitions** from the ECS console menu.  Then, choose **Create a Task Definition**:

![create task def](https://github.com/abby-fuller/ecs-demo/blob/master/images/create_task_def.png)

At this point, you'll have the opportunity to **Create an Amazon EC2 Container Service Role in the IAM Console**.  Follow the link to create the role:

![create service role](https://github.com/abby-fuller/ecs-demo/blob/master/images/service_role.png)

Once you've created the role, you can refresh the Role list in the Task Definition creation wizard.  It should now appear in the dropdown.  Select your role, and continue to adding a container definition.  

![container def](https://github.com/abby-fuller/ecs-demo/blob/master/images/container_def.png)

A few things to note here:

- We've specified a specific container image, including the `:latest` tag.  Although it's not important for this demo, in a production environment where you were creating Task Definitions programmatically from a CI/CD pipeline, Task Definitions could include a specific SHA, or a more accurate tag.

- Under **Port Mappings**, we've specified a **Container Port** (3000), but left **Host Port** as 0.  This was intentional, and is used to faciliate dynamic port allocation.  This means that we don't need to map the Container Port to a specific Host Port in our Container Definition-  instead, we can let the ALB allocate a port during task placement.  To learn more about port allocation, check out the [ECS documentation here](http://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PortMapping.html).

Once you've specified your Port Mappings, scroll down and add a log driver.  There are a few options here, but for this demo, choose **awslogs**:

![aws log driver](https://github.com/abby-fuller/ecs-demo/blob/master/images/setup_logdriver.png)

For the web container, make sure the **awslogs-stream-prefix** is **web**.

Once you've added your log driver, save the Container Definition, and create the Task Definition. 

Repeat the Task Definition creation process with the API container, taking care to use the api container image registry, and the correct port (8000) for the **Container Port** option.  For the log driver, make sure the **awslogs-stream-prefix** is **api**.

## Create your Services

Navigate back to the ECS console, and choose the cluster that you created during the first run wizard.  This should be named **ecs-demo**.  If you don't have a cluster named **ecs-demo**, create one with the **Create Cluster** option.

Next, you'll need to create your web service.  From the cluster detail page, choose **Services** > **Create**.

![create service](https://github.com/abby-fuller/ecs-demo/blob/master/images/create_service.png)

Choose the web Task Definition you created in the previous section.  For the purposes of this demo, we'll only start one copy of each task.  In a production environment, you will always want more than one copy of each task running for reliability and availability.

You can keep the default **AZ Balanced Spread** for the Task Placement Policy.  To learn more about the different Task Placement Policies, see the [documentation](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-strategies.html), or this [blog post](https://aws.amazon.com/blogs/compute/introducing-amazon-ecs-task-placement-policies/).

Under **Optional Configurations**, choose **Configure ELB**:

![choose container to add to elb](https://github.com/abby-fuller/ecs-demo/blob/master/images/select_container_and_role.png)

Select the web container, choose **Add to ELB**.  

![add to ALB](https://github.com/abby-fuller/ecs-demo/blob/master/images/add_container_to_alb.png)

This final step allows you to configure the container with the ALB.  When we created our ALB, we only added a listener for HTTP:80.  Select this from the dropdown as the value for **Listener**.  For **Target Group Name**, enter a value that will make sense to you later, like **ecs-demo-web**.  For **Path Pattern**, the value should be **`/web*`**.  This is the route that we specified in our Python application.

If the values look correct, click **Save** to add your Container.  

Repeat this process for the API container and task definition.  

## Testing our service deployments from the console and the ALB

You can see service level events from the ECS console.  This includes deployment events. You can test that both of your services deployed, and registered properly with the ALB by looking at the service's **Events** tab:

![deployment event](https://github.com/abby-fuller/ecs-demo/blob/master/images/steady_state_service.png)

We can also test from the ALB itself.  To find the DNS A record for your ALB, navigate to the EC2 Console > **Load Balancers** > **Select your Load Balancer**.  Under **Description**, you can find details about your ALB, including a section for **DNS Name**.  You can enter this value in your browser, and append the endpoint of your service, to see your ALB and ECS Cluster in action:

![alb web test](https://github.com/abby-fuller/ecs-demo/blob/master/images/alb_web_response.png)

![alb api test](https://github.com/abby-fuller/ecs-demo/blob/master/images/alb_api_test.png)

You can see that the ALB routes traffic appropriately based on the paths we specified when we registered the containers:  `/web*/` requests go to our web service, and `/api*/` requests go to our API service.


## More in-depth logging with Cloudwatch

When we created our Container Definitions, we also added the awslogs driver, which sends logs to [Cloudwatch](https://aws.amazon.com/cloudwatch/).  You can see more details logs for your services by going to the Cloudwatch console, and selecting first our log group:

![log group](https://github.com/abby-fuller/ecs-demo/blob/master/images/loggroups.png)

And then choosing an individual stream:

![event streams](https://github.com/abby-fuller/ecs-demo/blob/master/images/event_streams.png)

## That's a wrap!

Congratulations!  You've deployed an ECS Cluster with two working endpoints.  



