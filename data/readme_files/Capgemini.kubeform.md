Kubeform
========
[![wercker
status](https://app.wercker.com/status/d51be2fb5ae796055969b74d7924a059/s/master
"wercker
status")](https://app.wercker.com/project/bykey/d51be2fb5ae796055969b74d7924a059)

Deploy yourself a high-availability Kubernetes cluster, in minutes.
Built on Terraform, CoreOS and Ansible.

Our recipes for bootstrapping HA Kubernetes clusters on any cloud or on-premise.

Includes the following -

* CoreOS as the base operating system
* Kubernetes (in HA) mode (leader election using Podmaster)
* SSL certs/security for Kubernetes cluster components
* Flannel for networking
* Kubernetes Dashboard
* Sky/KubeDNS

and optionally -

* Prometheus for cluster monitoring (coming soon!)
* Fluentd, elasticsearch for cluster logging
* [Traefik](https://docs.traefik.io/toml/#kubernetes-ingress-backend) as the ingress controller for the edge-routers. For configuring it to use [letsencrypt](https://letsencrypt.org/) you can [edit this file](https://github.com/Capgemini/kubeform/blob/master/roles/addons/files/traefik.toml).

See our [Roadmap](/docs/roadmap.md) for future features and feel free to help us improve the project
by contributing a Pull Request, or raise an issue if you run into trouble!

## Getting started

Check out the instructions for provisioning on different clouds including:

* [AWS](/docs/getting-started-guides/aws/public.md)
* [Digitalocean](/docs/getting-started-guides/digitalocean.md)
* [Local Docker Compose](/docs/getting-started-guides/docker-compose.md)

## Demo

[Check out this demo deploying and scaling the backends for the ingress-controller on AWS and DigitalOcean](https://www.youtube.com/watch?v=Ejc5rKTzHiQ)

## Keep up to date...

Check out the [Capgemini UK Engineering blog](http://capgemini.github.io/) to find out more about the stuff we do!
