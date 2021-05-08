# Cloudera Altus Director Public Scripts

## Contributing Code

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Overview

Cloudera Altus Director can run custom user scripts at several points during the cluster creation and
termination processes. All scripts are run as root.

* Bootstrap scripts are run on an instance on startup, very soon after it becomes available.
* Deployment-level post-creation scripts run on a Cloudera Manager instance after its bootstrap is completed.
* Cluster instance-level post-creation scripts run on each cluster instance after cluster bootstrap is completed.
* Cluster-level post-creation scripts run on a single, arbitrary cluster instance after cluster bootstrap is completed.
* Cluster-level pre-termination scripts run on a single, arbitrary cluster instance before cluster termination begins.

This repository is a collection of freely available example scripts that Cloudera Altus Director users can use to
augment their clusters with advanced functionality.

Please refer to the Cloudera Altus Director documentation for more details about bootstrap scripts,
[post-creation scripts](https://www.cloudera.com/documentation/director/latest/topics/director_post_creation_scripts.html),
and pre-termination scripts.

Besides the scripts described below, look through the [example configuration files](configs) for other examples.

## Bootstrap scripts

* [Azure](azure-bootstrap-scripts) and [Azure DNS](azure-dns-scripts)
* [C6](c6)
* [Java 8](java8) (for Director 2.x only, 2.2 and higher)

Also, look through [reference configurations](configs) for examples of bootstrap scripts.

## Post-creation scripts

Look through [reference configurations](configs) for examples of post-creation scripts.

## Pre-termination scripts

Look through [reference configurations](configs) for examples of pre-termination scripts.

## Additional scripts

Other directories in this repository contain helpful scripts for a variety of tasks related to Altus Director.
Check out their README files and/or comments for more information.
