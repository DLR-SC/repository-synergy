# Spinnaker Terraform, now with more Googles!

## Updates:
### 1/4/2017:
* Now requires Terraform 0.8.2 or above

## Several things to Note:
* Store your terraform state file and it's backup in a secure place. It's not a good idea to push it to a public repository.
* The script is designed to be run on the same host as where you would be creating the SSH tunnel and browsing Spinnaker from. You _CAN_ run the install from pretty much anywhere with the pre-requisites and access to the cloud provider however the tunneling instructions the script outputs will have to be modified based on where you would like to access the services from.
* These scripts were tested running on OS X and Ubuntu 14.04 desktop.

## What does this do?
This is a set of terraform files and scripts designed to create a cloud environment from scratch with an example Jenkins job and Spinnaker application and pipeline.

[AWS Instructions](docs/AWS.md)

[GCP Instructions](docs/GCP.md)

## TODO
* Remove unnecessary packages and services from the Bastion host.