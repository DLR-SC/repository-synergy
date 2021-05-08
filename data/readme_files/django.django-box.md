django-box: A virtual machine for running the Django core test suite
====================================================================

Forked from djangocore-box (https://github.com/jphalip/djangocore-box)

**Django Version Support**: 2.1

**Release**: https://app.vagrantup.com/djangoproject/boxes/django-box-2.1

The django-box is a virtual machine (VM), based on Ubuntu 16.04, containing all
the programs and libraries required for running the Django core test suite in
multiple different environments.

Every supported version of Python is pre-installed, along with all supported
database backends, except for Oracle. Third party libraries like Memcached,
Sphinx, and Pillow are also provided.

This is particularly useful to anybody interested in contributing to Django
core without having to go through the trouble of installing and configuring all
the software required to run the tests in all these environments.

Preparation
-----------

### Software installation

First of all, you need to install the latest versions of
[Vagrant](https://www.vagrantup.com/downloads.html) (at version 2.0.1 as of
now) and [VirtualBox](https://www.virtualbox.org/wiki/Downloads) (currently at
version 5.2.4) on your host machine.

If you use Linux, you'll need to ensure proper support for NFS installed so the
Vagrant shared folders feature works. On Debian/ubuntu systems this can be
achieved with:

    $ sudo apt-get install nfs-kernel-server

On Fedora/CentOS systems you'll need to execute something like:

    $ sudo dnf install nfs-utils && sudo systemctl enable nfs-server

If you use a version of VirtualBox that isn't 5.2.4 you may run into problems
creating the NFS mount. You can either

* Upgrade to VirtualBox 5.2.4
* Or you can try to install the [vagrant-vbguest](https://github.com/dotless-de/vagrant-vbguest)
  plugin, which will attempt to install your local version of GuestAdditions
  into the VM:

      vagrant plugin install vagrant-share
      vagrant plugin install vagrant-vbguest

Booting the VM
--------------

_Legend:_ `(host)` is for commands to run on the host machine, and `(vm)` is
for commands to run inside the VM.

Setup the initial directory layout:

    (host) $ cd projects
    (host) $ git clone git@github.com:django/django.git
    (host) $ git clone git@github.com:django/django-box.git

It's important that django is cloned to a directory called `django` directly
beside the `django-box` directory. This is because the virtual machine will
mount `../django/`.

Then, either:

* If you have not already downloaded the box file separately, then run the
  following commands to boot the machine.

        (host) $ cd django-box
        (host) $ vagrant up

  This will automatically download the VM, which is about _1.2GB_ in size (be
  warned if you have a low bandwitdh Internet connection) and then boot it up.
  The download will only occur the first time you run `vagrant up`, as the image
  is saved.

* Or, if you have already downloaded the box file separately, then run the
  following command in order to import the box into vagrant and boot up the VM:

        (host) $ vagrant box add path/to/django-box-2.1.box --name djangoproject/django-box-2.1
        (host) $ cd django-box
        (host) $ vagrant up

  `vagrant box add` will copy the box file to `~/.vagrant.d/boxes`, so you may
  delete the file you've dowloaded if you'd like to save some space on your
  hard drive.

  You can download the box file directly from (make sure you update the version
  component):
  https://app.vagrantup.com/djangoproject/boxes/django-box-2.1/versions/1.0.0/providers/

  You can check what the latest released version is here:
  https://app.vagrantup.com/djangoproject/boxes/django-box-2.1/

As the VM boots up, it will prompt you to enter your host machine's
administrator password (the same that you use for logging into your host
machine). This is required so that Vagrant can setup the NFS shared folders.

Once the VM is up and running, type the following command to SSH into the VM
(still from inside the `django-box/` folder):

    (host) $ vagrant ssh

Once inside the VM, you can run the tests by typing any of the pre-defined
aliases. For example:

    (vm) $ runtests36-mysql
    (vm) $ runtests35-spatialite gis_tests
    (vm) $ runtests35-postgres admin_widgets --selenium chrome

Supported commands
------------------

```
runtests-isort    runtests35-sqlite3        runtests36-sqlite3
runtests-flake8   runtests35-spatialite     runtests36-spatialite
runtests-docs     runtests35-mysql          runtests36-mysql
                  runtests35-mysql_gis      runtests36-mysql_gis
                  runtests35-postgres       runtests36-postgres
                  runtests35-postgis        runtests36-postgis
```

Some of these names have changed in version 2.1 of django-box. Now they
mirror the naming convention used in our Jenkins CI setup. i.e.
`runtests3x-sqlite3-gis` is now `runtests3x-spatialite`,
`runtest3x-postgres-gis` is now `runtests3x-postgis` and
`runtest3x-mysql-gis` is now `runtests3x-mysql_gis`.

Examples
--------

The commands above that target databases all accept arguments and flags
consistent with the unit-tests documentation: https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/unit-tests/
What this means is that you can still run these tests with `--keepdb` to improve
testing performance, and target specific test modules.

```bash
# Run test modules related to expressions
runtests35-postgres --keepdb -v 2 queries expressions lookup aggregation annotations

# Run GIS tests
runtests35-postgis gis_tests

# Run selenium tests against chrome driver (no firefox available yet)
runtests36-sqlite3 admin_widgets --selenium chrome --parallel 1
```


Notes about the VM configuration
--------------------------------

Inside the VM, the `/django` folder is shared with the host and points to the
git clone that was created in the steps above. This way you can edit Django's
code using your favorite editor from your host machine and run the tests from
inside the VM. The repository clone for the django-box itself is also in a
shared folder at `/vagrant`.

The test settings are available in `/home/vagrant/djangodata/test_*.py`. These
files are put onto the `PYTHONPATH` when running the tests.

Chrome is pre-installed so that Django's selenium tests can be run in headless
mode with a virtual display (id `:99`). For example, you may run a specific test
like so:

    (vm) $ runtests36-sqlite3 admin_widgets --selenium chrome --parallel 1

The test suite will sometimes hang when running selenium tests in parallel mode.

Troubleshooting
---------------

### Strange errors when running tests

The `tox.ini` configuration file shipped with the Django source code directs
tox to create the virtual environments it uses for every test matrix
configuration below a `.tox` directory it creates on the Django source code top
directory.

django-box reuses Django's tox configuration, but executes tox inside the VM,
so that `.tox/` tree gets persisted between test runs and shared between a tox
copy you could use on the host and the django-box tox.

So it might happen than when faced with a mismatch between the version of Python
used to create a virtual environment and the version currently in use to run
the tests (e.g. Python micro version gets upgraded from 3.6.3 to 3.6.4 and this
upgrade reaches your Linux host and/or the repositories used by the django-box
VM), weird errors happen.

You can solve this by removing the virtualenv tree, e.g.:

    (host) $ rm -rf <Django souce code top dir>/.tox/py36-mysql
    (vm) $ rm -rf /django/.tox/py36-mysql

or more drastically, removing the `.tox` directory:

    (host) $ rm -rf <Django souce code top dir>/.tox
    (vm) $ rm -rf /django/.tox

This way the next time you run the tests, tox will rebuild the virtual
environment anew with the correct version of Python.

Building the documentation
--------------------------

To build the documentation, change to the docs directory and call a make task:


    (vm) $ cd /django/docs
    (vm) $ make html

You can then view the docs in your browser on the host:

    `(host) $ open django/docs/_build/html/index.html`

Vagrant command tips
--------------------

- To exit the VM and return to your host machine, simple type:

    `(vm) $ exit`

- To shutdown the VM, type:

    `(host) $ vagrant halt`

- To suspend the VM (i.e. freeze the VM's state), type:

    `(host) $ vagrant suspend`

- Once shutdown or suspended, a VM can be restarted with:

    `(host) $ vagrant up`

- To destroy the VM, simply type:

    `(host) $ vagrant destroy`

- To check if the VM is currently running, type:

    `(host) $ vagrant status`

- To re-run the provisioning after the VM has been started (if you have built
  the VM from scratch):

    `(host) $ vagrant provision`

- More information is available in the [Vagrant documentation](https://www.vagrantup.com/docs/).

Building a new version
----------------------

To upgrade or alter the original box, you'll need to recreate it. You'll need to
have Ansible 2.1 or greater installed, and django >= 2.1 in a folder beside the
django-box project as described above. You should also have
the [vagrant-vbguest](https://github.com/dotless-de/vagrant-vbguest) plugin
installed to ensure the correct GuestAdditions are configured within the image.

Make any required changes to the Ansible roles, and then create the box with:

    (host) $ VAGRANT_VAGRANTFILE=Vagrantfile-build vagrant up

The automatic build process will take about 20 minutes. If the new build should
be saved, then you can package the output:

    (host) $ VAGRANT_VAGRANTFILE=Vagrantfile-build vagrant package \
            --output django-box-2.1.box

    (host) $ vagrant box add django-box-2.1.box --name djangoproject/django-box-2.1 # optional - for testing

Note that compiling a new version should only be required when releasing a new
build to app.vagrantup.com.

To upload the new image, logon to the `djangoproject` account on vagrantup
here: https://app.vagrantup.com/djangoproject.

- Click through to the box you're updating
- Create a new version, bumping the release version, and adding release notes
- Create a new virtualbox provider for the new version
- Upload the .box file generated from the packaging command above

Credits
-------

django-box was originally authored by [Julien Phalip](https://twitter.com/julienphalip)
and [other contributors](AUTHORS) as djangocore-box.
