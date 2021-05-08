Load Balanced Game Server on Google Compute Engine
==================================================


Copyright
---------

Copyright 2013 Google Inc. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

[http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.


Disclaimer
----------

This sample application is not an official Google product.

Please note that if you are storing any user information in your application,
you must comply with Google App Engine's & Google Compute Engine's
Terms of Service item 4.2.

##### Google App Engine Terms of Service

[https://developers.google.com/appengine/terms](https://developers.google.com/appengine/terms)

##### Google Compute Engine Terms of Service

[https://developers.google.com/compute/docs/terms](https://developers.google.com/compute/docs/terms)


Summary
-------

Sample application of App Engine that manages game server on Google Compute
Engine.

This sample illustrates use of App Engine as management system of Google
Compute Engine.  By the combination of different technologies, it enables
automatic scaling of Google Compute Engine instances.

This sample uses [Grits](https://code.google.com/p/gritsgame/) as
an game server example.

This sample application uses Google App Engine, Google Compute Engine and
Google Cloud Storage.  Google Compute Engine and Google Cloud Storage require
billing set up on the project.  Please refer to the following links about
how to activate
[Google Cloud Storage](https://developers.google.com/storage/docs/signup) and
[Google Compute Engine](https://developers.google.com/compute/docs/signup).


Setting Up the Sample
---------------------

#### Directory Structure for Set Up

The following set up instruction assumes that we work on the directory where
the sample applicaiton is retrieved/extracted.
The final view of the directory will be as follows.

    Current Directory
          |- solutions-load-balanced-gaming-server-on-google-compute-engine-master/
                |- static_files/
                |- worker/
          |- gritsgame/
          |- gritsgame.tar.gz
          |- google_appengine/
          |- google_appengine_1.7.5.zip
          |- google_appengine_1.7.5.tar.gz
          |- node-v0.10.0-linux-x64.tar.gz


#### Download Grits package

Grits is distributed [here](https://code.google.com/p/gritsgame/).
Since Grits package is not necessary to App Engine application, it is
recommended to create Grits package outside the sample application directory
to avoid unnecessary file upload to App Engine.

git can be downloaded from [here](http://git-scm.com/downloads), or OS may
provide easier way to install it.

    git clone https://code.google.com/p/gritsgame/
    (cd gritsgame; git checkout 4462f1dd8d87)


#### Patch Grits

We need slight modification to Grits so that both frontend and backend
of grits work on the same Google Compute Engine instance.
The sample application includes the patch file to apply to Grits package
in `solutions-load-balanced-gaming-server-on-google-compute-engine-master` directory.

    patch -p0 < solutions-load-balanced-gaming-server-on-google-compute-engine-master/gritsgame.patch
    tar zcf gritsgame.tar.gz gritsgame


#### Download App Engine and Node.js packages

Download App Engine SDK and Node.js.  They are required to run Grits
on Google Compute Engine.  These packages can be downloaded to the same
directory as the sample is uncompressed, where gritsgame.tar.gz is
generated in the previous step.
The files may be downloaded by Web browser,
or the download can be performed by the following commands.
If the system doesn't have `wget`, `curl` command can be used
with -O option instead, as `curl -O <URL>`.

    wget https://storage.googleapis.com/appengine-sdks/deprecated/175/google_appengine_1.7.5.zip
    wget http://nodejs.org/dist/v0.10.0/node-v0.10.0-linux-x64.tar.gz

Note the sample uses App Engine development server as Grits game server
platform on Google Compute Engine instances.  The SDK package is not relevant
to the main App Engine application, but the sample requires App Engine SDK
installed on the development environment.
Also note App Engine 1.7.6 (or later) is not compatible with Grits game server.
Since App Engine SDK on the development environment and one on Google Compute
Engine is not relevant, it's fine to have different versions for them.

App Engine SDK must be repackaged to gzipped tar file before the package is
uploaded to the Google Cloud Storage.

    unzip -q google_appengine_1.7.5.zip
    tar zcf google_appengine_1.7.5.tar.gz google_appengine


#### Prepare Google Cloud Storage

Create Google Cloud Storage bucket and upload Grits, App Engine and Node.js
packages there.  Google Compute Engine instances will download these packages
from the bucket, and install them.  Make sure to have the Google Cloud Storage
bucket in the same project as Google Compute Engine, so that Compute Engine
instances can access the bucket without ACL configuration.

You can either:

* Use an existing bucket.
* Create new bucket from Google Cloud Storage Web UI.  Cloud Storage UI is
accessible from [Google Cloud Console](https://cloud.google.com/console).
* Use
[gsutil command line tool](https://developers.google.com/storage/docs/gsutil).
`gsutil mb gs://<bucket name>`

Upload packages to the Google Cloud Storage bucket.

    gsutil -m cp gritsgame.tar.gz  \
                 google_appengine_1.7.5.tar.gz  \
                 node-v0.10.0-linux-x64.tar.gz  \
                 gs://<bucket name>


#### Modify Sample Application for your Project and Google Cloud Storage Bucket

Replace bucket name in `compute_engine_controller.py` in the sample application.
Change value of `CLOUD_STORAGE_DIR` class variable of `ComputeEngineController`.
Also set the right `PROJECT_ID`.  Project ID is found on "Overview" tab of
[Google APIs Console](https://code.google.com/apis/console/).

    PROJECT_ID = '{{{{ project_id }}}}'
    CLOUD_STORAGE_DIR = 'gs://{{{{ bucket }}}}'


#### Google Compute Engine Instance Parameters

The sample application uses `us-central1-a` and `n1-standard-1` instance type.
The parameters can be changed by modifying value of `DEFAULT_ZONE` and
`DEFAULT_MACHINE_TYPE` variables in `compute_engine_controller.py`.


#### Prepare App Engine application

Create new App Engine application on appspot.com from
[App Engine console](https://appengine.google.com/).

Since Game Server needs to communicate with App Engine application,
make sure to create an application where authentication is not required,
such as one on appspot.com.

Also the application should be accessible by everybody.
When you choose Authentication Options, make sure to select
"Open to all Google Accounts users".  This authentication method
without access restriction makes the application public to everybody.

Fill application ID just created in `app.yaml`.

    application: {{{{ app_id }}}}


#### Create client ID and client secret

Client ID and client secret are required by OAuth2 authorization
to identify the sample application.  It is required in order for the
application to access Google API (in this example, Google Compute Engine API)
on behalf of the user.

Client ID and client secret can be set up from
[API Access](https://code.google.com/apis/console/#access)
page of Google APIs Console.

Choose "Web Application" as application type.  Set redirect URIs to
`https://<application ID>.appspot.com/oauth2callback`.

Replace `client_id` and `client_secret` values in the parameter list of
`OAuth2Decorator` in `handlers.py` with the actual values from
Google APIs Console.

    client_id = '{{{{ client_id }}}}',
    client_secret = '{{{{ client_secret }}}}',


#### Google Client API

[Google Client API](http://code.google.com/p/google-api-python-client/)
is library to access various Google's services via API.
This sample uses the library to access Google Compute Engine.

Download google-api-python-client-gae-1.1.zip from
[download page](http://code.google.com/p/google-api-python-client/downloads/list),
or download by command line.

    wget https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/google-api-python-client/google-api-python-client-gae-1.1.zip

Set up the library in the sample application root directory.

    (cd solutions-load-balanced-gaming-server-on-google-compute-engine-master; unzip ../google-api-python-client-gae-1.1.zip)


#### Set up Firewall on Google Compute Engine Network

Grits requires direct access from browser to the Google Compute Engine instance
where the game server runs.  The firewall rule must be added to allow
access to TCP port 8000 to 20000 range.  The firewall can be created from
"Networks" menu of Google Compute Engine Web UI.  The firewall may also be
created by the following command.

    gcutil addfirewall --project <project ID> --allowed tcp:8000-20000 gritsgame


#### Deploy

The sample application can be deployed to App Engine now.
The deployment is done by App Engine Launcher, or by appcfg.py command
included in App Engine SDK.

    appcfg.py [--oauth2] update solutions-load-balanced-gaming-server-on-google-compute-engine-master


Verification
------------

`http://<application ID>.appspot.com/` shows user's page to choose game server
to log in (or let App Engine choose one by "Quick Game").
`http://<application ID>.appspot.com/stats` (also linked from the top page)
requires administrator log in, and enables to start and shut down game
server cluster.

Before starting the game, the game server cluster must be started from `stats`
page.  Until game servers are started and warmed up, "Quick Game" from the
top page fails.  When game servers are listed on the top page, user can choose
which game server to log in, or "Quick Game" automatically chooses one of the
game servers with low resource usage.

In this sample, each Grits game server can host up to 8 players.  Therefore,
one player is translated to 12.5% of the resource of the instance.

`stats` page allows administrator to simulate high-load condition.
Artificial resource usage percentage can be set (and reset) for each game
server.  Set resource usage high, so that average usage is >80%.
App Engine cron task checks the average resource usage of all instances
every minute.
If the resource usage is >80%, the App Engine cron task automatically spins up
more Google Compute Engine instances, to keep the average resource usage low.
