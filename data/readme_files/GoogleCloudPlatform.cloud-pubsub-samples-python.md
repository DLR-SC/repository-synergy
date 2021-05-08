# Cloud Pub/Sub samples for Python

## Overview

This repository contains several samples for Cloud Pub/Sub service
with Python.

- appengine-push

  A sample for push subscription running on [Google App Engine][1].

- cmdline-pull

  A command line sample for pull subscription.

- gce-cmdline-publisher

  A Python command-line script that publishes to a topic using data from a large traffic sensor dataset.

## Run tests

Here are instructions to run the tests. You need a cloud project with
Cloud Pub/Sub enabled.

```bash
$ pip install tox
$ export GOOGLE_APPLICATION_CREDENTIALS=your-service-account-json-file
$ export TEST_PROJECT_ID={YOUR_PROJECT_ID}
$ tox
```

## Licensing

See LICENSE

[1]: https://developers.google.com/appengine/
