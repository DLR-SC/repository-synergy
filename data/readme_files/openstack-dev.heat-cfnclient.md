===========================
Heat CloudFormation Clients
===========================

Heat server includes API implementations which aim to be CloudFormation and
CloudWatch compatible. This project contains client utilities which consume
these APIs. It is recommended that most interaction with Heat is done instead
through the native REST API, using a client such as python-heatclient.

Utilities in this repository include:
heat-cfn   - Manages heat templates via Heat's legacy CloudFormation API
heat-boto  - As for heat-cfn, but using the boto library to access 
             Heat's legacy CloudFormation API
heat-watch - An admin utility to manage alarms and metrics via Heat's minimal
             CloudWatch compatible API.

Related projects
----------------
* http://wiki.openstack.org/Heat
