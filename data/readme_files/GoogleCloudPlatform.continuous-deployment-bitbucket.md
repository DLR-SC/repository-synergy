# Google App Engine

This project is a sample,
demonstrating how to deploy from Bitbucket,
using Bitbucket Pipelines, to Google App Engine,
and run an end-to-end test against a staging environment.
See [documentation on Continuous Deployment to App Engine Using Bitbucket Pipelines](https://cloud.google.com/solutions/continuous-delivery-bitbucket-app-engine) for details.
Documentation should be considered sufficient only for developers
who already know both Bitbucket Pipelines and Google App Engine well.

## Prerequisites

* You have a Bitbucket account.
* You have a Google App Engine account and have created a project.

## Steps to deploy to your own App Engine project

Note that the Books API Key is a specific requirement of this app,
but is not generally necessary to deploy from Bitbucket Pipelines.
The service account credential is always necessary, 
in order to authenticate the `gcloud` command line tool.

* Enable your repo or fork of this repo for Bitbucket Pipelines.
* Enable the Books API.
* Enable the App Engine Admin API.

Configure the following environment variables for Bitbucket Pipelines:

* `CLOUDSDK_CORE_PROJECT`: Use the id of the Google App Engine project.
* `GOOGLE_API_KEY`: (Private) Create a new public Server API Key in the Google console.
* `GOOGLE_CLIENT_SECRET`: (Private) Create a new Service Account JSON file in the Google console. Copy the contents into this environment variable.

## Contributing changes

* See [CONTRIBUTING.md](CONTRIBUTING.md)

## Licensing

* See [LICENSE](LICENSE)