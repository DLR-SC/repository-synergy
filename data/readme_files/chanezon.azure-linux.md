# P@'s Linux on Azure tutorials

<img src="/img/Microsoft-Loves-Linux.png"/>

Documentation and examples for how to leverage various linux technologies with Microsoft Azure.

I write tutorials with a bit of automation code about things I didn't see documented elsewhere, or where I want to add context and details to existing docs and blog posts. I also list a set of links to relevant docs or blog posts that I found useful.

These tutorials use many tools: docker, python, pip, Azure Python SDK, Azure Cross platform CLI, docker machine... In order to make it easier for anyone to follow the tutorials, I packaged all these tools in a Docker container. See [Using the chanezon/azure-linux Dockerfile](/docker/usingdockerfile.md) for how to use it.

## Docker

### Tutorials

* [Provisioning Docker containers on Azure with Docker machine](/docker/machine.md)
* [Provisioning a Docker Swarm cluster on Azure](/docker/swarm.md)

### Interesting links

I assume you already know Docker basics: there are plenty of resources and tutorials out there about it. If you don't, get started with @kartar's excellent book [The Docker book - Containerization is the new virtualization](http://www.dockerbook.com/), then read the official docs.

Here are resources to understand how Docker works internally, where it is going, and what kind of innovation is happening in different part of the ecosystem as it matures: orchestration, networking, storage, management and monitoring.

* [Creating a Docker host machine on Azure](https://docs.docker.com/installation/azure/#creating-a-docker-host-machine-on-azure) from Docker official docs
* [Provisioning an Ubuntu Docker VM from the Azure marketplace in the Azure portal](http://azure.microsoft.com/blog/2015/01/08/introducing-docker-in-microsoft-azure-marketplace/): this is the easiest way to get started with Docker on Azure.
* Azure Docs [Using the Docker VM Extension from Azure Cross-Platform Interface (xplat-cli)](http://azure.microsoft.com/en-us/documentation/articles/virtual-machines-docker-with-xplat-cli/)
* [Running ASP.NET 5 applications in Linux Containers with Docker](http://blogs.msdn.com/b/webdev/archive/2015/01/14/running-asp-net-5-applications-in-linux-containers-with-docker.aspx): One word: "Inconceivable!" Try out @ahmetalpbalkan's excellent tutorial.
* [Creating containers](http://crosbymichael.com/creating-containers-part-1.html) @crosbymichael's series on the internals of what containers are is a very good read, to understand how Docker works.
* @jpetazzo's [articles](http://blog.docker.com/author/jerome/) and [decks](http://www.slideshare.net/jpetazzo/) also go pretty deep.
* [Using Fig and Flocker to build, test, deploy and migrate multi-server Dockerized apps](https://clusterhq.com/blog/fig-flocker-multi-server-docker-apps/) One area of innovation for Docker is storage. One issue with Docker is that stateless containers are easy to move to a different host (typically done by an orchestration engine), but stateful containers for database services are tied to a host. Flocker is an interesting answer to this issue, allowing you to snapshot and migrate your data volumes using a port of zfs for Linux. Flocker provides multi host container orchestration, supporting part of the fig format (which will be the format supported in Docker groups), but the most differentiating aspect they provide is the zfs based volume migration capability.
*  [Life and Docker networking](http://weaveblog.com/2014/11/13/life-and-docker-networking/) Networking is another big area of innovation in the Docker ecosystem. Thoughtful essay by @monadic about the various approaches to Docker networking these days, and the need for a plugin system for Docker.
* [Docker groups](https://github.com/docker/docker/issues/9175) The Docker stack composition proposal, for Docker native orchestration. There's a release implementing it that you can try. This is the replacement for Fig.
* [Docker clustering with swarm](https://github.com/docker/swarm)
* [Docker plugins proposal](https://github.com/docker/docker/pull/8968)
* [Docker hosts management with machine](https://github.com/docker/machine) there is an Azure driver for it

## CoreOS

### Tutorials

* [Installing a CoreOS cluster on Azure](/coreos/cloud-init/README.md) Docker orchestration with Fleet. Deploying a Java 8 application using Spring Boot and MongoDB on a CoreOS cluster on Azure, using Docker and Fleet. Deploying @NetflixOSS containers. This tutorial explains how to manually deploy VMs in your cluster. For a more automated process, see the cluster deployment tool tutorial below.
* [Azure CoreOS cluster deployment tool](/coreos/cluster/README.md) Python script to deploy a CoreOS cluster in one shot.
* [Installing Weave Docker virtual network on CoreOS on Azure](/coreos/weave/README.md). Weave allows you to manage networking for your Docker containers from the command line. It includes a dns service.
* [Installing Deis on a CoreOS cluster on Azure](/coreos/deis/README.md) Docker orchestration with Deis. Fun and games with DNS settings, then deploy a ruby app with git, and a Docker image for a Java 8 app.
* [Installing Kubernetes on a CoreOS cluster on Azure](/coreos/kubernetes/README.md) (Work in Progress), Docker orchestration with Kubernetes. Cf links below for 2 approaches to networking that need testing on Azure: Weave and Flannel.

### Interesting links

The main issue installing Kubernetes on Azure is networking: [Kubernetes needs to assign 1 IP address per pod](https://github.com/GoogleCloudPlatform/kubernetes/blob/master/docs/design/networking.md), which works fine on Google Cloud Platform, where [advanced routing](https://cloud.google.com/compute/docs/networking#routing) allows you to configure your VMs so that each get assigned a /24 address space. On Azure today, you need to leverage some kind of overlay network to accomplish that. There are different approaches in how to do this:

* [Kubernetes, Getting started on Microsoft Azure](https://github.com/GoogleCloudPlatform/kubernetes/blob/master/docs/getting-started-guides/azure.md) uses Ubuntu images, OpenVPN for networking.
* [Weave for Kubernetes on CoreOS](http://weaveblog.com/2014/11/11/weave-for-kubernetes/) seems promising, and should be a good approach for Azure
* [Deploying Kubernetes on CoreOS with Fleet and Flannel](https://github.com/kelseyhightower/kubernetes-fleet-tutorial/blob/master/README.md) the other main approach

## Ubuntu Core

[Snappy Ubuntu Core](http://www.ubuntu.com/cloud/tools/snappy) is a minimal server image of Ubuntu, coupled with a transactional OS update mechanism, similar to CoreOS, and an application model inspired by mobile app stores called snappy. It was announced 12/9/2014, with initial support for Azure first.

* [Getting started with Snappy Ubuntu Core on Azure](/ubuntu/README.md)
