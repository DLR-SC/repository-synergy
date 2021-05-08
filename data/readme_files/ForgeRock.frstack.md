# Install the ForgeRock Open Identity Stack (OIS)

## Warning
**This code is not supported by ForgeRock and it is your responsibility to verify that the software is suitable and safe for use.**

# Project Status

This project is in maintenance mode and is not being actively
developed.   I am happy to accept pull requests if you have fixes or enhancements.

For a variety of reasons, I believe that using containers is a better long
term approach to rapidly creating a complete stack. If you want to
follow along with that work, please see this project:

https://github.com/ForgeRock/fretes  

Which contains Kubernetes manifests to run development instances of OpenAM,
OpenDJ, and OpenIDM. That project uses Dockerfiles that are being maintained
here:  https://stash.forgerock.org/login?next=/projects/DOCKER/repos/docker/browse

You will need a ForgeRock.org community account to view that Stash repository.






*NOTE: Currently in the process of modifying this to use Ansible 2.0.
You must install Ansible 2 from source*

Kubernetes assets have been moved to https://github.com/ForgeRock/fretes

Docker images are at https://github.com/ForgeRock/docker

This currently works on Fedora 23 using Vagrant. Google Compute Engine (GCE) and AWS are a
work in progress. Other combinations have not been tested.

This will be gradually moved to Docker / Kubernetes. Pull requests are welcome


## Installed products

After completion of the build, the guest will have the following configured:

* haproxy to route ports 80/443 to various backend services. A test SSL cert is installed
* openidm running on port 9080
* opendj running on port 389. This is the user profile store.
* openam running on port 8080
* openig running on port 2080
* Policy agents installed (but not configured) for Apache and tomcat

## Quick Start

* Install Ansible, VirtualBox and Vagrant. If you are on a
  mac you can install Ansible using

  ```brew install ansible```

* You **must** download all of the ForgeRock binaries to the staging directory: **vagrant/staging**. There
is a shell script provided **bin/getnightly.sh** that will auto download all of the nightly builds for you.
* Edit ansible/group_vars/all with any environment specific configuration.
* Do a *vagrant up** It should just work..

### Example:

```
cd vagrant
../bin/getnightly.sh
vagrant up
```

This may take a long time as the Vagrant VM must be downloaded. Be Patient!

If there are no errors from above you should be ready to test the VM.Put the IP address of the guest in your
hosts **/etc/hosts** file. The Vagrant image is configured to use a host only IP:

`192.168.56.11 openam.example.com openidm.example.com`

* Login to OpenAM at http://openam.example.com/openam  (amadmin/password)
* Login to OpenIDM at http://openidm.example.com/admin  (openidm-admin/openidm-admin)
* View the OpenIG landing page at http://openam.example.com/openig/  
* View the haproxy status page at https://openam.example.com/haproxy?stats
* View the default Apache landing page at https://openam.example.com/   (Currently protected  - so you will get a 403)
* ssh into the guest using `vagrant ssh`
* Using an ldap browser (Apache Directory Studio, for example) you can browse the user store at openam.example.com:389,   
  cn=Directory Manager / password

By default software is installed under /opt/ois. You can change this by editing ansible/group_vars/all

## Suspending or Destroying the environment

You can suspend the guest using:

   ```vagrant suspend```

If you want to destroy the VM and clean up all the resources:

   ```vagrant destroy```


## Shell scripts

Shell scripts are provided to re-run all or part of the provisioning process. For example,

```
cd vagrant
./frstack
```

Will run the entire frstack.yml playbook.

Ansible also supports the concept of "tags". If you want to run a subset of the playbook, provide a comma seperated value (no spaces) with a list of tags. For example:

```
cd vagrant
./frstack openam,openidm
```

Will run just those roles that pertain to OpenAM and OpenIDM

You can also re-run the vagrant ansible provisioner using:

```
vagrant provision
```
But note that this will not allow you to selectively provision using tags. This is essentially equivalent to runing ./frstack
with no tags.


## Staging files

For Vagrant installs, the "staging/" directory is mounted on the guest. Ansible assumes it has access
   to all of the binaries local to the guest being installed. If you are on an environment such as
   AWS or GCE, you will need some process to download the binaries.  See vagrant/getnightly.sh for an example.

   The binary product files are expected to be generic (openam.zip, not OpenAM-13.0) -but you can include a
   RELEASE file that lists the specific installed versions.



## The 'fr' ForgeRock user

The project runs an Ansible role called 'create-fr-user' that creates a ForgeRock user 'fr'.
This user owns the directories and runs most of the JDKs for the stack.

It may be handy to be able to ssh into the guest as the fr user:

```ssh fr@openam.example.com```

The ansible create-fr-user role attempts to copy your ssh public key in ~/.ssh/id_rsa.pub (on your local host)
to the guests /home/fr/.ssh/known_hosts. If you don't have
a public key in your ~.ssh directory create one following the
instructions here: [https://help.github.com/articles/generating-ssh-keys/]


## Troubleshooting

### SSH Issues

Ansible uses ssh to connect to the guest image. To debug connection issues you can use the -vvvv option when running the playbook.
Edit the frstack script to set this variable (uncomment the DEBUG line).


## VM Guest Services

The VM uses systemd to control all services. You can start / stop and get service status using
the command systemctl:

```systemctl [start|stop|status|restart]  service```

Where service is one of:

* openam
* openidm
* openig
* opendj
* apps
* haproxy


Use ```journalctl``` to view the system log. You can type "G" to skip to the end of the log.


## Implementation Notes

* The guest is currently Fedora 23. The scripts assume the use of systemd - so this should work on
other distros that also support systemd.
* For consistency between environments a forgerock user is created ("fr" - because no one likes to type
long names). Most services run under this account.
* To set up ssh for the fr user (so you can You can ```ssh fr@opename.example.com```)
 Add your public ssh key to roles/create-fr-user/files. Edit roles/create-fr-user/tasks/main.yml
 to reflect the name of your pub key files

### Current Issues

See https://github.com/ForgeRock/frstack/issues

* haproxy needs to be setup to route to the OpenIDM end user UI


### TODO

If you are looking to contribute pull requests are welcome. Things that need to be done:

* Start migration of instances to Docker, and then eventually to Kubernetes. The image now has docker installed ready to go
* Make this work on both Debian / Centos / Ubuntu 15.x etc. (anything that supports systemd).
* policy agents install is not working / not completing. It installs the agent software but does not configure
* looks like the HOSTNAME needs to be set to the fqdn on the machine /etc/sysconfig/network  or openam config bombs out
  This is fixed for Vagrant by setting config.vm.hostname. Will need a fix for other environments
* tomcat agent installer does not put filter in global web.xml. Need to fix up apps web.xml. Apparenty 4.0 deprecates global web.xml?
* Configure sample policies
* Add HA, multi-master replication, et
* Add some sample apps
* Configure openig as an agent
* Openig - gateway conf/ directory needs to be set to /opt/openig.
