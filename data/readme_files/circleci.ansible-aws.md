ansible-aws
===========

The project demonstrates continuous integration and delivery of a simple python application using CircleCI, Ansible and AWS. Ansible is used to define everything about the deployment environment, from AWS resources to config files and application code, and CircleCI handles continuous integration and continuous deployment to AWS through Ansible Tower.

##Project overview
The project consists of two major sections: the app, which is a simple Flask-based web application, and the Ansible playbooks (the "config" directory), which follow [Ansible's recommended directory layout](http://docs.ansible.com/playbooks_best_practices.html#directory-layout). Because the application is deployed to the servers with a "push" model from Ansible Tower, the entire source tree is first pulled down to Ansible Tower, and then the python application code is pushed to the app servers using [synchronize module](http://docs.ansible.com/synchronize_module.html), which is just a wrapper around rsync (the are only needed on the Tower server, where the instruct Ansible what commands to run against the remote hosts).

##Running locally
To run the (very simple) Flask application locally, simply clone the repository, run `pip install -r requirements.txt` (optionally inside of a virtualenv), and then run `python app/hello/hello_app.py` to start the app on port 5000 (the `app.run` method takes an optional “port” keyword argument, which is not currently passed in from the command line args).

##Getting Ansible
Refer to [the Ansible docs](http://docs.ansible.com/) for detailed instructions on installing and running ansible.

Running from a git clone may truly be the easiest way to get started with Ansible:

```
$ git clone git://github.com/ansible/ansible.git
$ source ansible/hacking/env-setup
```

You will also need to install the following python dependencies for Ansible to work:

```
$ sudo pip install paramiko PyYAML jinja2 httplib2
```

See [the Ansible docs](http://docs.ansible.com/) for instructions on installing Ansible from various package managers.

##Configuring Ansible hosts
Ansible works by SSHing into your servers and running commands on them (or by simply using a “local” connection in the case of commands run on your local machine). There are a number of ways to configure which hosts Ansible tries to use, but one place Ansible looks by default is /etc/ansible/hosts, which can be either a file or a directory. If you are primarily using Ansible with AWS, it can be convenient to configure it to be a directory with the following structure:

```
└── hosts
    ├── ec2
    ├── ec2.ini
    └── local
```

Where ec2 is [this script](https://raw.github.com/ansible/ansible/devel/plugins/inventory/ec2.py), ec2.ini is [this file](https://raw.github.com/ansible/ansible/devel/plugins/inventory/ec2.ini), and the contents of “local” are as follows:

```
[local]
localhost ansible_connection=local
```

The ec2 script must be executable, so run `chmod +x /etc/ansible/ec2` once you download it.

The ec2 script is what Ansible calls a “dynamic inventory”, which means that its contents can fluctuate over time as VMs are provisioned and killed, which makes sense in the context of AWS.

There’s one more thing that needs to be done before the inventories are usable, which is to make your AWS credentials available to the boto library, which Ansible uses to interact with AWS. There are [a number of ways to do this](http://boto.readthedocs.org/en/latest/boto_config_tut.html), but one way is to create a file at ~/.boto with the following contents:

```
[Credentials]
aws_access_key_id = <your_access_key_here>
aws_secret_access_key = <your_secret_key_here>
```

With all of this done, you should be able to run `ansible all -m ping -u ubuntu` and see a response from both your local machine and the remote hosts (you will need to have SSH access to the remote machines, and replace “ubuntu” with the appropriate remote username).

##Deploying to a single EC2 server
You can now run `ansible-playbook config/dev_site.yml` to launch an ec2 server running the “Hello World” application. Note that the dev_site playbook assumes that you have an AWS security group called “ssh-http”, uses the us-west-2 AWS region, and uses the “ubuntu” remote user. You may need to change this to suit your needs.

##The production environment
The Ansible playbook included in the project creates an AWS Elastic Load Balancer (ELB) and an Auto Scaling Group (ASG). The ELB and ASG together ensure that traffic is always spread between a certain number of instances, and will take care of killing and replacing “unhealthy” instances. When an instance is replaced by auto scaling, it will execute a user data script that performs a callback to Ansible and triggers a re-run of the playbook. Since playbooks should be idempotent, this has no impact on existing servers, but fully installs the app on the newly provisioned server.

##Ansible Tower
The “production-style” Ansible playbook in this project assumes the use of an Ansible Tower server. Ansible Tower is free for managing up to 10 hosts. You can find out more about how to get it up and running [here](http://www.ansible.com/tower).

Note that these instructions assume the use of Ansible 1.6.5 and and Tower 1.4.11.

Once you have an Ansible Tower instance up and running, you will need to follow the following steps:

1. Setup at least one organization
2. Setup credentials for accessing AWS, Git, and EC2 instances via SSH.
3. Create a project that pulls from the Git repository and is set to “Update on Launch”
4. Create an inventory called, for example, “AWS” and in that inventory create a group called, for example, “ec2”, and configure the group to pull from EC2 using the AWS credentials setup in (2). Also, setup the group to “Update on Launch”
5. Create a job template that uses all of the information configured above (use the EC2 SSH key for the “Machine Credential”) and uses the playbook “config/prod_site.yml”.
6. Check the “Allow Callbacks” box, and add the full callback URL as “callback_url” and the “Host Config Key” as the “callback_key” in the “Extra Variables” section.
7. Add a “stack_name” extra variable calling the stack whatever you like, save the job template, and you should be able to launch the job.

##Deployment from CircleCI
The circle.yml file included in the project already specifies all of the test and deployment instructions necessary. However, there are several environment variables that must be specified in Circle for it to work correctly. These are:

* ANSIBLE_TOWER_JOB_TEMPLATE_ID

* ANSIBLE_TOWER_USER (must have permission to launch the job)

* ANSIBLE_TOWER_PASS

* ANSIBLE_TOWER_SERVER (full URL to the server)

When those environment variables are set, any CircleCI build on master will trigger a job launch and deployment to AWS.

##See Also
* The AWS docs on [Auto Scaling Groups](http://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/WhatIsAutoScaling.html) and [Elastic Load Balancing](http://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/SvcIntro.html)
* [The Ansible docs](http://docs.ansible.com/)
* [Ansible Tower](http://www.ansible.com/tower)
* [The Flask Quickstart](http://flask.pocoo.org/docs/quickstart/#quickstart)
* [Testing Flask Applications](http://flask.pocoo.org/docs/testing/) from the Flask docs
* [The nose documentation](https://nose.readthedocs.org/en/latest/) for more information about the nose test runner
