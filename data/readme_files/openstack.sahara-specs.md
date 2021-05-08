========================
Team and repository tags
========================

.. image:: https://governance.openstack.org/tc/badges/sahara-specs.svg
    :target: https://governance.openstack.org/tc/reference/tags/index.html

.. Change things from this point on

===============================
OpenStack Sahara Specifications
===============================

This git repository is used to hold approved design specifications for additions
to the Sahara project. Reviews of the specs are done in gerrit, using a similar
workflow to how we review and merge changes to the code itself.

The layout of this repository for Sahara specifications is::

  specs/<release>/

The layout of this repository for Sahara Client is::

  specs/saharaclient/

When a new version of Sahara Client is released the implemented blueprints
will be moved to a directory specific to that release::

  specs/saharaclient/<release>/

The layout of this repository for Sahara Tests is::

  specs/sahara-tests/


You can find an example spec in ``specs/template.rst``.

For specifications that have been reviewed and approved but have not been
implemented::

  specs/backlog/

Specifications in this directory indicate the original author has either
become unavailable, or has indicated that they are not going to implement the
specification. The specifications found here are available as projects for
people looking to get involved with Sahara. If you are interested in
claiming a spec, start by posting a review for the specification that moves it
from this directory to the next active release. Please set yourself as the new
`primary assignee` and maintain the original author in the `other contributors`
list.

Specifications are proposed for a given release by adding them to the
``specs/<release>`` directory and posting it for review. Not all approved
blueprints will get fully implemented. The implementation status of a
blueprint for a given release can be found by looking at the tasks associated
to the corresponding story in Storyboard.

Incomplete specifications have to be re-proposed for every release. The review
may be quick, but even if something was previously approved, it should be
re-reviewed to make sure it still makes sense as written.

Prior to the Juno development cycle and for the Juno-1 development milestone,
this repository was not used for spec reviews. Reviews prior to Juno were
completed entirely through Launchpad blueprints::

  https://blueprints.launchpad.net/sahara

Launchpad blueprints are no more used for tracking the
current status of blueprints. For historical information, see::

  https://wiki.openstack.org/wiki/Blueprints

For more information about working with gerrit, see::

  https://docs.openstack.org/infra/manual/developers.html#development-workflow

To validate that the specification is syntactically correct (i.e. get more
confidence in the Jenkins result), please execute the following command::

  $ tox

After running ``tox``, the documentation will be available for viewing in HTML
format in the ``doc/build/`` directory.
