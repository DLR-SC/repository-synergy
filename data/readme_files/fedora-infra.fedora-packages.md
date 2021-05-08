**fedora-packages** allows to search for packages in Fedora.

## Documentation
Would be nice to have a bit more documentation.

### Hacking with docker-compose

We have a `docker-compose` setup for hacking on the fedora-packages app.
This setup matches the production deployment of fedora-packages (i.e.
Apache HTTP server with `mod_wsgi`) that is split over several Ansible
files in Fedora infrastructure repository.

* https://infrastructure.fedoraproject.org/cgit/ansible.git/tree/playbooks/groups/packages.yml
* https://infrastructure.fedoraproject.org/cgit/ansible.git/tree/roles/packages3/web

To bring the environment up you should first install the following.

	$ sudo dnf install docker-compose

And then make sure that the docker daemon is running.

	$ sudo systemctl start docker
	$ sudo systemctl enable docker

If you do not wish to run docker-compose using `sudo` you will need to add 
your user to the docker group as follow.

	$ sudo groupadd docker && sudo gpasswd -a $USER docker
	$ MYGRP=$(id -g) ; newgrp docker ; newgrp $MYGRP

This is has for effect to give root permission to users added to the docker
group.

Now from the devel directory you can run docker-compose.

	$ cd devel
	$ docker-compose up

The first time you execute this command, it will build a docker container and it will
take few minutes. Once the build is finish and the application is started you can access
the fedora-packages using this url http://127.0.0.1/packages

#### Reloading the application after code changes
Since we are using apache HTTP server to serve the application we need to run the following
command to reload the application to test some code changes.

	$ cd devel
	$ docker-compose exec web touch /usr/share/fedoracommunity/fedora-packages.wsgi

This will change the timestamp of the .wsgi file and ask apache to reload the application.

#### Running the unit tests
To execute the test suite simply run the following command

	$ docker-compose exec web py.test /usr/share/fedoracommunity/tests


### Hacking with Vagrant

We have a simple vagrant setup for hacking on the fedora-packages app.

First, install Ansible, Vagrant, the vagrant-sshfs plugin, and the
vagrant-libvirt plugin from the official Fedora repos:

    $ sudo dnf install ansible vagrant vagrant-libvirt vagrant-sshfs

Now, from within main directory (the one with the Vagrantfile in it)
of your git checkout of fedora-pacakges, run the vagrant up command to provision
your dev environment:

    $ vagrant up

When this command is completed (it may take a while) you will be able to
ssh into your dev VM with vagrant ssh and then run the command to start the fedora-packages server:

    $ vagrant ssh
    [vagrant@localhost ~]$ pushd /vagrant/; gearbox serve;

Once that is running, simply go to http://localhost:8080/ in your browser on
your host to see your running fedora-packages test instance.


## Create a new release.

To create a new release, you need to update `setup.py` and `fedora-packages.spec`
with the new version number and any dependencies added or removed.

The `CHANGELOG.rst` needs also to be updated with the commits and pull-requests
included in the release.

Once these 3 files have been updated and commited to the develop branch, you create a new
Git tag.

	$ git tag -a 4.1.0 -s -m 'Release 4.1.0'
	$ git push && git push --tag

Once the tag has been successfully pushed, a new release will be available in github.

## License
fedora-packages is free software; you can redistribute it and/or modify it under the terms of the GNU Affero General Public License v3.0. See COPYING included with the distribution for details.
