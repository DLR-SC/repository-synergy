# Jenkins workflow for Alfred v2
A configurable workflow for Alfred v2 which lets you list Jenkins jobs and see their status.

![image](./alfred-jenkins-workflow-screenshot.png)

## Installation

You can install this workflow by dowloading the [Jenkins.alfredworkflow](https://github.com/jeroenseegers/alfred-jenkins-workflow/raw/master/Jenkins.alfredworkflow) file and either double-clicking it, or dragging it onto the Alfred Workflow screen.

After adding it to your workflow collection, be sure to set the correct URL to your Jenkins CI instance by double-clicking the `Script Filter` and replacing `URL_TO_YOUR_JENKINS_INSTANCE` with the actual URL of your Jenkins CI instance.

If your Jenkins instance requires authentication, just set the url to `https://USERNAME:PASSWORD@url_to_your_instance.com/`.

If your Jenkins instance requires authentication, but you're using Google Authentication (or prefer not to hardcode your password) in the script, you can use your API token (see below screenshot for navigating the Jenkins UI)

![image](./alfred-jenkins-google-auth-screenshot.png)

Plug in your user id and the API token and voila! `https://USERNAME:APITOKEN@url_to_your_instance.com/`

## Usage

The commands currently supported by this workflow are:

* **jenkins status {query}**
`This returns the current status for all jobs matching {query}`

## About

This workflow is developed by [@RevellNL](https://twitter.com/RevellNL)
