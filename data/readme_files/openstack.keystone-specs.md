========================
Team and repository tags
========================

.. image:: https://governance.openstack.org/tc/badges/keystone-specs.svg
    :target: https://governance.openstack.org/tc/reference/tags/index.html

.. Change things from this point on

=================================
OpenStack Identity Specifications
=================================

This git repository is used to hold approved design specifications for additions
to the Keystone project. Reviews of the specs are done in gerrit, using a
similar workflow to how we review and merge changes to the code itself.

The layout of this repository for Keystone specifications is::

  specs/<release>/

The layout of this repository for Keystone Client is::

  specs/keystoneclient/

When a release of Keystone Client is cut, the implemented blueprints will be
moved to a directory specific to that release::

  specs/keystoneclient/<release>/

You can find an example spec in ``specs/template.rst``.

For specifications that have been reviewed and approved but have not been
implemented::

  specs/backlog/

Specifications in this directory indicate the original author has either
become unavailable, or has indicated that they are not going to implement the
specification. The specifications found here are available as projects for
people looking to get involved with Keystone. If you are interested in
claiming a spec, start by posting a review for the specification that moves it
from this directory to the next active release. Please set yourself as the new
`primary assignee` and maintain the original author in the `other contributors`
list.

Specifications are proposed for a given release by adding them to the
``specs/<release>`` directory and posting it for review.  Not all approved
blueprints will get fully implemented. The implementation status of a blueprint
for a given release can be found by looking at the blueprint in Launchpad::

  http://blueprints.launchpad.net/keystone/<blueprint-name>

.. WARNING::

    Specifications not accepted by the second milestone of a release will not
    be targeted for that release without an explicit exception granted. To
    request an exception, send an email to the developer mailing list with the
    details of the specification, why it should be accepted after the deadline,
    and any supporting documentation (e.g. proof of concept code) that will
    indicate to the core team it will be completed before feature freeze.

Incomplete specifications have to be re-proposed for every release.  The review
may be quick, but even if something was previously approved, it should be
re-reviewed to make sure it still makes sense as written.

Prior to the Juno development cycle, this repository was not used for spec
reviews.  Reviews prior to Juno were completed entirely through Launchpad
blueprints::

  http://blueprints.launchpad.net/keystone

Please note, Launchpad blueprints are still used for tracking the
current status of blueprints. For more information, see::

  https://wiki.openstack.org/wiki/Blueprints

For more information about working with gerrit, see::

  http://docs.openstack.org/infra/manual/developers.html#development-workflow

To validate that the specification is syntactically correct (i.e. get more
confidence in the Jenkins result), please execute the following command::

  $ tox

After running ``tox``, the documentation will be available for viewing in HTML
format in the ``doc/build/`` directory.
