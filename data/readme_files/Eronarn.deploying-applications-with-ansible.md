# Deploying Applications with Ansible

*Automate your infrastructure in your data center and in the cloud*

[Slides are available here!](https://docs.google.com/presentation/d/1nqJtVU3tnK_THM2NG39-77dAsbWei67mFxRmvEL5sDk/edit#slide=id.g1f4c6c3756_0_145) Or check out slides.pdf in this repository for a copy as of 5/30.

## Introduction

Welcome to `Deploying Applications with Ansible`, a live training hosted by O'Reilly Media and taught by James Meickle.

> Ansible is a "batteries included" automation, configuration management, and orchestration tool that's fast to learn and flexible enough for any architecture. It's the perfect choice for automating repetitive tasks, increasing deployment frequency, and running infrastructure at scale. Companies are increasingly turning to Ansible to meet the challenges of transitioning from the data center to the cloud, from servers to containers, and from silos to devops.
> In this course you'll learn Ansible's key concepts and how to develop workflows that solve your challenges. The curriculum focuses on practical techniques, with an eye towards reusable and maintainable code. On completion you'll have enough hands-on experience with Ansible to feel comfortable using it in your own environment on a daily basis. 

## Course Outline

Day One:
- Cover course goals
- Introduce Ansible and its history
- Connect to training environment
- Ansible concepts:
  - Modules
  - Playbooks
  - Roles
- Practice writing playbooks and roles
- Deploy a single-node web application
- Compare Ansible to other tools

Day Two:
- Advanced module and role tips
- Explore cloud-focused features
- Deploy a multi-tier, multi-instance application in AWS
- Discuss code quality for Ansible
- Develop a custom Ansible module
- Learn about the Ansible ecosystem
- Recap what we've learned and revisit course goals

## Recommended Readings

Day One:

- [Use Case: Application Deployment](https://www.ansible.com/application-deployment): Why Ansible is valuable for application development.

- [How Ansible Works](https://www.ansible.com/how-ansible-works): This high-level document surveys Ansible's capabilities that we'll be examining in more depth.

- [YAML Syntax](http://docs.ansible.com/ansible/YAMLSyntax.html): We will be working with Ansible playbooks written in YAML, so please familiarize yourself with basic syntax.

- [All Modules](http://docs.ansible.com/ansible/list_of_all_modules.html): If you want to get an idea of Ansible's capabilities, you can skim through this list of all Ansible modules.

- Finally, if Ansible is your first configuration management or automation tools,
you may also benefit from viewing [Introduction to Ansible](https://www.safaribooksonline.com/library/view/introduction-to-ansible/9781491955956/), a [Safari](https://www.safaribooksonline.com/) recorded training. This course will cover more material, but solid grasp of Ansible basics.

Day Two:

- We will be discussing advanced tips and tricks for several key Ansible modules. You may wish to read the documentation in advance:
    - [file](http://docs.ansible.com/ansible/file_module.html)
    - [copy](http://docs.ansible.com/ansible/copy_module.html)
    - [template](http://docs.ansible.com/ansible/template_module.html)
    - [replace](http://docs.ansible.com/ansible/replace_module.html)
    - [lineinfile](http://docs.ansible.com/ansible/lineinfile_module.html)
    - [command](http://docs.ansible.com/ansible/command_module.html)
    - [shell](http://docs.ansible.com/ansible/shell_module.html)
    - [apt](http://docs.ansible.com/ansible/apt_module.html)
    - [service](http://docs.ansible.com/ansible/service_module.html)
    - [systemd](http://docs.ansible.com/ansible/systemd_module.html)
    - [ec2](http://docs.ansible.com/ansible/ec2_module.html)

- Since we will be writing more advanced playbooks and roles, you may want to learn more about the Jinja templating engine's capabilities:
    - [Variables](https://docs.ansible.com/ansible/playbooks_variables.html)
    - [Filters](https://docs.ansible.com/ansible/playbooks_filters.html)
    - [Tests](https://docs.ansible.com/ansible/playbooks_tests.html)

- This part of the course will interact with AWS, so you may be interested in reading [Integration: Ansible and AWS](https://www.ansible.com/aws) or [Amazon Web Services Guide](http://docs.ansible.com/ansible/guide_aws.html).

## About this repository

Assuming this repository is checked out to `~/ansible`:

- `ansible.cfg`: Configuration file used when your current directory is ~/ansible
- `environments/aws`: Inventory directory selected via ~/ansible/ansible.cfg
- `playbooks`: Each YAML file is a playbook
- `roles`: Each folder is a role
- `roles/requirements.yml`: For installing roles with ansible-galaxy
- `files`: Static files used in playbooks
- `templates`: Jinja template files used in playbooks
