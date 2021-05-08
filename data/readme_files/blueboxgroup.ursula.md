

<div align="center"><img src="./ursula.png" alt="Ursula"></div><hr />

Ursula provides a series of Ansible playbooks for installing, managing, and
maintaining OpenStack powered clouds.

Ursula was originally created by a team at [Blue Box](https://www.blueboxcloud.com) and is
released under the MIT License (MIT).

The `ceph-monitor`, and `ceph-osd` roles were originally taken from
[ceph/ceph-ansible](https://github.com/ceph/ceph-ansible), but have since been
modified. `ceph/ceph-ansible` is released under the Apache License.

# Installation

## System Dependencies

The following system packages ( or their equivalents for your OS ) are
required to run `ursula`:

* python-pip
* python-dev
* libxml2-dev
* libxslt-dev
* libffi-dev
* libssl-dev

#### Mac OS X specific notes non installing dependencies

If you have already installed python via brew, you'll need to remove it so you can force the devel headers to be installed AND usable by your libraries.

```bash
brew uninstall python
```


Next, install python and pip if not already installed.

```bash
brew install --devel --framework python
pip install -U pip
```

If you've already attempted or installed libxml2 and/or libxslt unlink and uninstall those first.

```bash
brew unlink libxml2
brew unlink libxslt
brew uninstall libxml2
brew uninstall libxslt
```

Now, install libxml2 and force static dependencies to enabled linking to the installed devel headers.

```bash
brew install --with-python libxml2
STATIC_DEPS=true sudo pip install -U lxml
```

Install libxslt and relink the newly installed libraries. As we already forced libxml2 to link the headers libxslt should do so as well without further steps. 

```bash
brew install --with-python libxslt
brew link libxml2 --force
brew link libxslt --force
```


Install the remaining needed libraries.

```bash
brew install libffi
brew install openssl
```

## Python Environment

We recommend using [virtualenv](http://virtualenv.readthedocs.org/en/latest/) or
[virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/)
to isolate your Python environment.

If you're new to python, the following will install `virtualenvwrapper` and set
up a `virtualenv` for ursula:

```bash
$ pip install virtualenvwrapper
$ source /usr/local/bin/virtualenvwrapper.sh
$ mkvirtualenv ursula
```

Note: If you're using OSX El Capitan (version 10.11) or newer, you need to use `pip install --ignore-installed six virtualenvwrapper` to get pip to not attempt to uninstall the existing version of six which the system will not allow.

You will want to add `source /usr/local/bin/virtualenvwrapper.sh` to your shell startup file, changing the path to virtualenvwrapper.sh
depending on where it was installed by pip. For bash users on MaC OS X, use .bash_profile; if, like me, you've moved to Zsh, use .zshrc instead.

```bash
echo " " >> .bash_profile
echo "#sourcing statement for virtualenvwrapper" >> .bash_profile
echo "source /usr/local/bin/virtualenvwrapper.sh" >> .bash_profile

```

From now on to work with ursula you can run `$ workon ursula` to
enter the `virtualenv`

## Install ursula and dependencies:

Now that your python environment is ready, you can clone ursula and install
its prerequisites.

You'll need a modern version of pip, so if you're using a version <7,
run:

```
$ pip install -U pip
```

Now you can continue cloning and installing ursula:

```bash
$ cd ~/development
$ git clone git@github.com:blueboxgroup/ursula.git
$ cd ursula
$ pip install -r requirements.txt
```

These steps will have installed `ursula-cli`, the various openstack clients, and our
patched fork of `Ansible`.

# ursula-cli

Ursula was designed by [Blue Box](https://www.bluebox.net) to manage a large
number of OpenStack deployments. In order to do this efficiently we've made
some changes to how `ansible` works. As part of these changes we have a
wrapper tool called `ursula-cli` which was installed during the
`pip install -r requirements.txt` above.

Make sure `ursula-cli` is installed in your environment:

```
ursula -h
usage: ursula [-h] [--ursula-forward] [--ursula-test] [--ursula-debug]
              environment playbook

A CLI wrapper for ansible
...
...
```

There are two mandatory fields required by `ursula-cli`.  The first is
`environment` which will require some further explanation.
The second is `playbook` which will almost always be `site.yml`.

## openstack-envs

One of the modifications that we have made to `Ansible` is the ability to have
a seperate path that includes all of the configuration options for your
OpenStack deployment(s).   An example of this can be found in `/envs/example`

If you look in the `/envs/example` path, you'll see a `defaults.yml` file and a
series of directories each representing a different OpenStack deployment.

We then utilize the standard `Ansible` features by having `group_vars`,
`host_vars`, and a `hosts` file.

There are also some `vagrant.yml` files scattered around.  These are helper
files to make using `Vagrant` even easier with `ursula` to test your
environments in VMs.

### allinone

The simplest example deployment is `allinone` which is a single server
deployment that acts as both a `controller` and a `compute` node.

Whether or not you're using `Vagrant` if you look in the
`envs/example/allinone/vagrant.yml` file it will give you some hints on what
your server should look like.  If you do not wish to use `Vagrant` then you
should install Ubuntu 12.04 on a server and configure its networking as
described in the `vagrant.yml` file.

Next, look in the `hosts` file.  It's very simple in this case due to the fact
we have only a single server.  This file combined with the `site.yml` playbook
tells Ansible what roles to apply to which servers.

Finally, we have the `group_vars/all.yml` file.  This contains values that will
override the `defaults.yml` in the parent directory.  For example, we're
disabling Percona replication by setting `percona.replication: False`.

## Performing a deployment:

For the sake of simplicity, I recommend using `Vagrant` rather than `Manual` for your first install. 

If you want to install manually, do not use `envs/examples/*` without modifications as it contains several circuit breakers such
as invalid certificates and your installs will fail.

### Manually

If you're not running `Vagrant` and have installed ubuntu onto a server and
configured the networking then we need to tell our system how to talk to this
new server.  The easiest way is via an entry in your ssh config file in
`~/.ssh/config`.

```
Host allinone
  HostName 172.16.0.100
  User ubuntu
  IdentityFile ~/.ssh/private_key
```

```bash
$ ursula envs/example/allinone site.yml
```

### Vagrant

If you're running `Vagrant`, we have a wrapper script that stands up the
appropriate vagrant environment, saves it as an ssh config, and then calls
`ursula` for you.

To deploy your `allinone` environment via `Vagrant` simply run:

```bash
$ ursula --provisioner=vagrant envs/example/allinone site.yml
```

Note: The default OS for ursula is Ubuntu Trusty. If you want Precise, set
the env var `URSULA_BOX_NAME` to the name of your precise vagrant
box before running vagrant.

# Contributing

Contributions in the form of pull requests or issues are very welcome. We
ask that you review [Code Guidelines](./coding.md).

# More Docs

See the [/doc](https://github.com/blueboxgroup/ursula/tree/master/doc) directory of this repo.
