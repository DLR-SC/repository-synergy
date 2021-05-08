# Ansible provisioning for Symfony, Laravel and Node.js

## Your application within 1 hour in production with this tool: Tywin
Create easily your Ansible provisioning for Symfony, Laravel and Node.js projects.

![Ansible](https://upload.wikimedia.org/wikipedia/commons/0/05/Ansible_Logo.png)
![Symfony](http://symfony.com/images/v5/logos/sf-positive.svg)
![Laravel](http://laravelacademy.org/wp-content/uploads/2015/09/laravel-5-1-icon.png)
![Nodejs](https://avatars2.githubusercontent.com/u/9158694?v=3&s=200)

## Requirements
This have been tested with the Ubuntu OS. It should work with many other various Debian distribution. Feel free to share your advice for the other OS..
This is what you will need to install if you haven't done yet:

* **Python 2.7**
* [Ansible](http://docs.ansible.com/intro_installation.html) (>2.0)
* [Vagrant](http://www.vagrantup.com/downloads.html) I advise to download it from their website to have the last version.
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads).
* nfs `sudo apt-get install nfs-kernel-server`
* PyYAML and Jinja2 for python

## How to use it
1) Installation.

    git clone git@github.com:fansible/tywin.git ~/tywin

2) Generate the default conf

You can generate the default conf by running in the root directory of your project:

    python ~/tywin/generate.py

You can now find your provisioning in the `devops` directory

3) Create the VM
You can create the VM with `vagrant up`.

4) Log in your vagrant with `vagrant ssh` and put your ssh key in the .ssh/authorized_keys file.
Log out and try to log in again using `ssh ubuntu@IP_OF_YOUR_VAGRANT (MAYBE 10.0.0.10 check your Vagrantfile)`

If it's OK you can provision the VM

5) Provision the VM

Provision it with `ansible-playbook -i devops/provisioning/hosts/vagrant devops/provisioning/playbook.yml`.
If something goes wrong you can go inside your vagrant and try to execute manually in your shell the Ansible task that is failing.

After that, your VM is now ready! You can see your project in your browser at the IP's adress (10.0.0.10 if you haven't changed anything) =)

6) Now you can do the same for your staging/production environment.
Update the file in `devops/provisioning/hosts/staging` and add the IP or domain of your server.

### Database configuration
Change the value of the database configuration in `devops/provisioning/group_vars/vagrant`

### Go further: customize your provisioning
What you can do:

1) Add your roles in the `devops/provisioning/roles` directory.

2) Modify the playbook to call your roles.

3) Overide vars (in `devops/provisioning/vars`).

If you want to have more information on the use of Ansible/Vagrant for you development environment, I wrote a [blog post about it](http://cloudacademy.com/blog/deploy-web-applications-on-iaas-with-ansible/).

## Stay in touch

If you have any question ask me on [Twitter](https://twitter.com/maxthoon) !
