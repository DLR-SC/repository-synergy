========================
Team and repository tags
========================

.. image:: https://governance.openstack.org/tc/badges/glance_store.svg
    :target: https://governance.openstack.org/tc/reference/tags/index.html
    :alt: The following tags have been asserted for the Glance Store
          Library:
          "project:official",
          "stable:follows-policy",
          "vulnerability:managed".
          Follow the link for an explanation of these tags.
.. NOTE(rosmaita): the alt text above will have to be updated when
   additional tags are asserted for glance_store.  (The SVG in the
   governance repo is updated automatically.)

.. Change things from this point on

Glance Store Library
====================

Glance's stores library

This library has been extracted from the Glance source code for the
specific use of the Glance and Glare projects.

The API it exposes is not stable, has some shortcomings, and is not a
general purpose interface. We would eventually like to change this,
but for now using this library outside of Glance or Glare will not be
supported by the core team.

* License: Apache License, Version 2.0
* Documentation: https://docs.openstack.org/glance_store/latest/
* Source: https://opendev.org/openstack/glance_store/
* Bugs: https://bugs.launchpad.net/glance-store
* Release notes: https://docs.openstack.org/releasenotes/glance_store/index.html
