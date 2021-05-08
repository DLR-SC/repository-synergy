========================
Team and repository tags
========================

.. image:: https://governance.openstack.org/tc/badges/ironic-specs.svg
    :target: https://governance.openstack.org/tc/reference/tags/index.html

.. Change things from this point on

===============================================
OpenStack Baremetal Provisioning Specifications
===============================================

This git repository is used to hold approved design specifications for
additions to the Baremetal Provisioning program, and in particular, the Ironic
project.  Reviews of the specs are done in gerrit, using a similar workflow to
how we review and merge changes to the code itself.

The layout of this repository is::

  specs/approved/
  specs/backlog/
  specs/not-implemented/
  specs/<release>/
  specs/<juno|kilo|liberty>-implemented/

There are also placeholder directories for old links that have been moved.

Specifications must follow the template which can be found at
`specs/template.rst`.

Specifications are proposed by adding them to the `specs/approved` directory,
adding a soft link to it from the `specs/not-implemented` directory, and
posting it for review. When a specification is fully implemented, the link in
`specs/not-implemented` directory should be moved to the appropriate
`specs/<release>` directory. Not all approved specifications will get
fully implemented.

Starting with the Mitaka development cycle, all approved specifications
(implemented and not-implemented) will reside in the `specs/approved`
directory.

Also starting with the Mitaka development cycle, our Launchpad bug tracking
system is used for tracking the work related to a specification. (This replaces
the use of Launchpad blueprints). The bug should be tagged with 'rfe', its
title should be prefixed with '[RFE]' and the Importance should be set to
'Wishlist'. For existing RFE bugs, see::

  https://bugs.launchpad.net/ironic/+bugs?field.tag=rfe

Prior to the Juno development cycle, this repository was not used for spec
reviews.  Reviews prior to Juno were completed entirely through Launchpad
blueprints::

  https://blueprints.launchpad.net/ironic

For more information about working with gerrit, see::

  https://docs.openstack.org/infra/manual/developers.html#development-workflow

To validate that the specification is syntactically correct (i.e. get more
confidence in the Jenkins result), please execute the following command::

  $ tox

After running ``tox``, the documentation will be available for viewing in HTML
format in the ``doc/build/`` directory.

To quickly preview just the rst syntax rendering (without Sphinx features)
of a single spec file execute the following command::

    $ tox -evenv rst2html.py <path-to-your-spec.rst> <path-to-output.html>

and open ``<path-to-output.html>`` in your browser.
Running full ``tox`` is still advised before submitting your patch.
