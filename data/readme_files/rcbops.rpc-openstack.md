
# This project is EOL 

This project is retired with Rocky and releases forward are using native openstack-ansible.
Do not file any issues in this project


# Rackspace Private Cloud - OpenStack

The RPC-OpenStack repository contains additional scripts, variables, and
options for deploying an OpenStack cloud. It is a thin wrapper around the
[OpenStack-Ansible](https://github.com/openstack/openstack-ansible)
deployment framework that is part of the OpenStack namespace.

## Deployment options

There are two different types of RPC-OpenStack deployments available:

* **All-In-One (AIO) Deployment.** An AIO is a quick way to test a
  RPC-OpenStack deployment. All of the cloud's internal services are deployed
  on the same server, which could be a physical server or a virtual machine.

* **Production Deployment.** Production deployments should be done on more
  than one server with at least three nodes available to run the internal
  cloud services.

* **Upgrading the RPC-OpenStack Product.** Upgrading the RPC-OpenStack Product
  using intra-series releases.

### All-In-One (AIO) Deployment Quickstart

Clone the RPC-OpenStack repository:

``` shell
git clone https://github.com/rcbops/rpc-openstack /opt/rpc-openstack
```

Start a screen or tmux session (to ensure that the deployment continues even
if the ssh connection is broken) and run `deploy.sh`:

Run the ``deploy.sh`` script within a tmux or screen session:

``` shell
tmux
cd /opt/rpc-openstack
export DEPLOY_AIO=true
export RPC_PRODUCT_RELEASE="master"  # This is optional, if unset the current stable product will be used
./scripts/deploy.sh
```

The `deploy.sh` script will run all of the necessary playbooks to deploy an
AIO cloud and it normally completes in 90 to 120 minutes.

### Production Deployment Guide

Clone the RPC-OpenStack repository:

``` shell
git clone https://github.com/rcbops/rpc-openstack /opt/rpc-openstack
```

#### Run the basic system installation

Start a screen or tmux session (to ensure that the deployment continues even
if the ssh connection is broken) and run `deploy.sh`:

Run the ``deploy.sh`` script within a tmux or screen session:

``` shell
cd /opt/rpc-openstack
export RPC_PRODUCT_RELEASE="master"  # This is optional, if unset the current stable product will be used
./scripts/deploy.sh
```

#### Configure and deploy the cloud

To configure the installation please refer to the upstream OpenStack-Ansible
documentation regarding basic [system setup](https://docs.openstack.org/project-deploy-guide/openstack-ansible/latest/configure.html).

##### OpenStack-Ansible Installation

OpenStack-Ansible will need to be installed. While you can simply run the
`bootstrap-ansible.sh` script provided by the OpenStack-Ansible community
you may also run the `openstack-ansible-install.yml` playbook which was
created for convenience and will maintain impotency.

``` shell
cd /opt/rpc-openstack
export RPC_PRODUCT_RELEASE="master"  # This is optional, if unset the current stable product will be used
/opt/rpc-ansible/bin/ansible-playbook -i 'localhost,' playbooks/openstack-ansible-install.yml
```

###### Optional | Setting the OpenStack-Ansible release

It is possible to set the OSA release outside of the predefined "stable" release
curated by the RPC-OpenStack product. To set the release define the Ansible
variable `osa_release` to a SHA, Branch, or Tag and run the `site-release.yml`
and `openstack-ansible-install.yml` playbooks to install the correct version.

``` shell
openstack-ansible site-release.yml openstack-ansible-install.yml -e 'osa_release=master'
```

##### Running the playbooks

Once the deploy configuration has been completed please refer to the
OpenStack-Ansible documentation regarding [running the playbooks](https://docs.openstack.org/project-deploy-guide/openstack-ansible/latest/run-playbooks.html).

----

#### Deploy the Rackspace Value Added Services

Upon completion of the deployment run `scripts/deploy-rpco.sh` script to
apply the RPC-OpenStack value added services; you may also run the playbooks
`site-logging.yml` to accomplish much of the same things.

``` shell
cd /opt/rpc-openstack
openstack-ansible site-logging.yml
```

Post deployment run the **optional** `site-openstack.yml` playbooks to setup
default flavors and images.

``` shell
cd /opt/rpc-openstack
openstack-ansible site-openstack.yml
```

----

### Perform an Intra-Series Product Upgrade

To run a basic system upgrade set the `${RPC_PRODUCT_RELEASE}` option, re-run
`deploy.sh`.

``` shell
tmux
cd /opt/rpc-openstack
export RPC_PRODUCT_RELEASE="master"  # This is optional, if unset the current stable product will be used
./scripts/deploy.sh
openstack-ansible openstack-ansible-install.yml
```

Once basic system configuration has completed, [run through the upgrade process](https://docs.openstack.org/openstack-ansible/latest/user/minor-upgrade.html)
for the specified product release.  

### Perform a Major Product Upgrade (BETA)

To run a major upgrade set the `${RPC_PRODUCT_RELEASE}` option, re-run
`deploy.sh`.

``` shell
tmux
cd /opt/rpc-openstack
export RPC_PRODUCT_RELEASE="master"  # This needs to be set to the new product
./scripts/deploy.sh
openstack-ansible openstack-ansible-install.yml
```

Once the deployment is ready either [run the major upgrade script](https://docs.openstack.org/openstack-ansible/latest/user/script-upgrade.html)
or [run the manual upgrade](https://docs.openstack.org/openstack-ansible/latest/user/manual-upgrade.html)
process.


### Remove legacy ELK from an RPC-OpenStack deployment and deploy ELK 6x.

The following procedure will deactivate the legacy ELK tooling within an
environment and redeploy the new tools.

If the **optional** step to destroy the containers is not executed, the old
containers will remain online but will no longer receive any more data.

* Retrieve the ops tooling from openstack-ansible.

``` shell
git clone https://github.com/openstack/openstack-ansible-ops /opt/openstack-ansible-ops
```

* **OPTIONAL** | Destroy existing ELK related containers.

``` shell
cd /opt/openstack-ansible/playbooks || cd /opt/rpc-openstack/openstack-ansible/playbooks
ansible all -m service -a 'name=filebeat state=stopped'
openstack-ansible lxc-containers-destroy.yml --limit 'elasticsearch_all:kibana_all:logstash_all'
```

* Move old config files out of the way.

``` shell
rm /etc/openstack_deploy/env.d/{elasticsearch,kibana,logstash}.yml
```

* Ensure the legacy implementation of `filebeat` is stopped and removed.

``` shell
ansible -m apt -a 'name=filebeat state=absent' all
```

* Remove old containers from openstack-ansible inventory.

``` shell
for i in $(../scripts/inventory-manage.py -l | grep -e elastic -e kibana -e logstash | awk '{print $2}'); do
  echo "Removing $i"
  ../scripts/inventory-manage.py -r "${i}"
done
```

* Deploy the new ELK infrastructure

``` shell
cd /opt/rpc-openstack/playbooks
openstack-ansible deployment-elk.yml
```

### Testing and Gating

Please see the documentation in [rpc-gating/README.md](https://github.com/rcbops/rpc-gating/blob/master/README.md)
