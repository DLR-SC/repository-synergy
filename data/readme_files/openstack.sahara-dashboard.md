========================
Team and repository tags
========================

.. image:: https://governance.openstack.org/tc/badges/sahara-dashboard.svg
    :target: https://governance.openstack.org/tc/reference/tags/index.html

.. Change things from this point on

OpenStack Dashboard plugin for Sahara project
=============================================

How to use with Horizon on server:
----------------------------------

Use pip to install the package on the server running Horizon. Then either copy
or link the files in sahara_dashboard/enabled to
openstack_dashboard/local/enabled. This step will cause the Horizon service to
pick up the Sahara plugin when it starts.

How to use with devstack:
-------------------------

Add the following to your devstack ``local.conf`` file::

    enable_plugin sahara-dashboard https://opendev.org/openstack/sahara-dashboard


To run unit tests:
------------------

./run_tests.sh

NOTE:
=====

As of the Mitaka release, the dashboard for sahara is now maintained
outside of the horizon codebase, in the repository.

Links:
------

Sahara project: https://opendev.org/openstack/sahara

Sahara at wiki.openstack.org: https://wiki.openstack.org/wiki/Sahara

Storyboard project: https://storyboard.openstack.org/#!/project/936

Sahara docs site: https://docs.openstack.org/sahara/latest/

Quickstart guide: https://docs.openstack.org/sahara/latest/user/quickstart.html

How to participate: https://docs.openstack.org/sahara/latest/contributor/how-to-participate.html

Release notes: https://docs.openstack.org/releasenotes/sahara-dashboard/

License
-------

Apache License Version 2.0 http://www.apache.org/licenses/LICENSE-2.0
