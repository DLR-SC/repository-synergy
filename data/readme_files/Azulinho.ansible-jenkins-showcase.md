This is an example of how Ansible can be used in an *infrastructure as code environment*,
where all your deployment and configuration data resides in one of more GIT repositories, and the whole environment could be rebuilt from scratch at any time.

The configuration for the different jenkins jobs, pipelines, views,
as well as the complete zabbix setup (including the monitored items) are all set in [group_vars/all.yaml](https://github.com/Azulinho/ansible-jenkins-showcase/blob/master/group_vars/all.yaml) at the root of this repository:

![configuration](https://github.com/Azulinho/ansible-jenkins-showcase/raw/master/videos/part0.gif)

This repo contains a demo of how ansible can be used to deploy and configure Continous Delivery pipelines using
a jenkins box.

It shows how different libraries can be used with ansible to deploy and update plugins, jobs, view, pipelines:

* [python jenkins-job-builder](https://wiki.jenkins-ci.org/display/JENKINS/Job+DSL+Plugin)
* [groovy jenkins job DSL](https://github.com/jenkinsci/job-dsl-plugin/wiki)
* [jinja2 XML templating](http://jinja.pocoo.org/)


The following roles are used in this demo,

* [Azulinho.azulinho-ansible](https://github.com/Azulinho/azulinho-ansible)
* [Azulinho.azulinho-apache](https://github.com/Azulinho/azulinho-apache)
* [Azulinho.azulinho-devel-packages](https://github.com/Azulinho/azulinho-devel-packages)
* [Azulinho.azulinho-git](https://github.com/Azulinho/azulinho-git)
* [Azulinho.azulinho-google-dns](https://github.com/Azulinho/azulinho-google-dns)
* [Azulinho.azulinho-java-openjdk-jdk](https://github.com/Azulinho/azulinho-java-openjdk-jdk)
* [Azulinho.azulinho-jenkins-job-builder](https://github.com/Azulinho/azulinho-jenkins-job-builder)
* [Azulinho.azulinho-jenkins-kick-pipelines](https://github.com/Azulinho/azulinho-jenkins-kick-pipelines)
* [Azulinho.azulinho-jenkins-plugins](https://github.com/Azulinho/azulinho-jenkins-plugins)
* [Azulinho.azulinho-jenkins-reconfigure-jobs-using-jinja2](https://github.com/Azulinho/azulinho-jenkins-reconfigure-jobs-using-jinja2)
* [Azulinho.azulinho-jenkins-reconfigure-jobs-using-job-builder](https://github.com/Azulinho/azulinho-jenkins-reconfigure-jobs-using-job-builder)
* [Azulinho.azulinho-jenkins-reconfigure-jobs-using-job-dsl](https://github.com/Azulinho/azulinho-jenkins-reconfigure-jobs-using-job-dsl)
* [Azulinho.azulinho-jenkins-server](https://github.com/Azulinho/azulinho-jenkins-server)
* [Azulinho.azulinho-mysql-server](https://github.com/Azulinho/azulinho-mysql-server)
* [Azulinho.azulinho-python27](https://github.com/Azulinho/azulinho-python27)
* [Azulinho.azulinho-ssh-keys](https://github.com/Azulinho/azulinho-ssh-keys)
* [Azulinho.azulinho-yum-plugin-versionlock](https://github.com/Azulinho/azulinho-yum-plugin-versionlock)
* [Azulinho.azulinho-yum-repo-epel](https://github.com/Azulinho/azulinho-yum-repo-epel)
* [Azulinho.azulinho-yum-repo-jenkins](https://github.com/Azulinho/azulinho-yum-repo-jenkins)
* [Azulinho.azulinho-yum-repo-rpmforge](https://github.com/Azulinho/azulinho-yum-repo-rpmforge)
* [Azulinho.azulinho-zabbix-agent](https://github.com/Azulinho/azulinho-zabbix-agent)
* [Azulinho.azulinho-zabbix-checks](https://github.com/Azulinho/azulinho-zabbix-checks)
* [Azulinho.azulinho-zabbix-server](https://github.com/Azulinho/azulinho-zabbix-server)
* [joshualund.ruby-2_1](https://github.com/jlund/ansible-ruby-2.1)
* [joshualund.ruby-common](https://github.com/jlund/ansible-ruby-common)


Simply run:

    rake

![vagrant_up](https://github.com/Azulinho/ansible-jenkins-showcase/raw/master/videos/part1.gif)

and then connect to [http://jenkins:8080](http://jenkins:8080)

you should see a fully deployed, configured jenkins with two pipelines and a series of jobs.

The second pipeline [PIPELINE2](http://jenkins:8080/view/PIPELINE2/) should be automatically initiated by an Ansible task,
this pipeline executes a job [jinja2_deploy_zabbix](http://jenkins:8080/job/jinja2_deploy_zabbix/) with provisions and configures a zabbix server using an Ansible playbook.


Then another job [jinja2_zabbix_checks](http://jenkins:8080/job/jinja2_zabbix_checks) will populate the zabbix server with templates, hosts, and items.
Upon completion the Zabbix server will be configured to monitor itself as well as the Jenkins box which provisioned the Zabbix Server.

Access to the zabbix box on [http://zabbix/zabbix/](http://zabbix/zabbix/) using username:admin password:zabbix


![boxes_up](https://github.com/Azulinho/ansible-jenkins-showcase/raw/master/videos/part2.gif)


Some limited support available for linode and LXC, simply use:

    rake default [linode|lxc]

My lxc conf looks like:

    \>cat /etc/lxc/default.conf
    lxc.network.type = veth
    lxc.network.link = lxcbr0
    lxc.network.flags = up
    lxc.network.hwaddr = 00:16:3e:xx:xx:xx
    lxc.autodev = true

and my dnsmasq file:
    \>cat /etc/dnsmasq-lxcbr0.conf
    interface=lxcbr0
    except-interface=lo
    bind-interfaces

    domain=lxc
    dhcp-range=10.0.3.2,10.0.3.100,12h

    host-record=lxchost.lxc,10.0.3.1
    local=/lxc/

for linode, you need to export your linode key:

    export linode_key="XXXXXXXX"
