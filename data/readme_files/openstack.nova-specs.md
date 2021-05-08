=======
README
=======

OpenStack Nova Specifications
=============================


This git repository is used to hold approved design specifications for additions
to the Nova project.  Reviews of the specs are done in gerrit, using a similar
workflow to how we review and merge changes to the code itself. For specific
policies around specification review, refer to the end of this document.

The layout of this repository is::

  specs/<release>/

Where there are two sub-directories:

specs/<release>/approved
  specifications approved but not yet implemented

specs/<release>/implemented
  implemented specifications

This directory structure allows you to see what we thought about doing,
decided to do, and actually got done. Users interested in functionality in a
given release should only refer to the ``implemented`` directory.

The lifecycle of a specification
--------------------------------

Developers proposing a specification should propose a new file in the
``approved`` directory. `nova-specs-core
<https://review.opendev.org/#/admin/groups/302,members>`_ will review the
change in the usual manner for the OpenStack project, and eventually it will
get merged if a consensus is reached.

At this time the Launchpad blueprint is also "Definition" approved. The
developer is then free to propose code reviews to implement their
specification. These reviews should be sure to reference the Launchpad
blueprint in their commit message for tracking purposes.

.. note:: The launchpad blueprint's "Definition" approval indicates that the
          nova-specs-core team agrees with the technical aspects of the
          proposal ("if we are going to do this, this is how"). The blueprint's
          "Direction" approval is a separate indication of commitment to the
          targeted release ("we want to do this now"). It is possible to have a
          specification and blueprint "Definition" approved, but not have its
          "Direction" approved due to subsequent planning activities. In such
          cases, the blueprint (and any unmerged code) could be deferred for
          consideration in a future release.

.. todo:: Document the specifics of these "planning activities".

Once all code for the feature is merged into Nova, the Launchpad blueprint is
marked "Implemented" by a nova maintainer.

At the end of the release cycle, implemented specifications are moved from the
``approved`` directory to the ``implemented`` directory, creating redirects so
that existing links to the approved specification are not broken. (Redirects
aren't symbolic links, they are defined in a file which sphinx consumes. An
example is at ``specs/stein/redirects``.)

We use the ``tox -e move-implemented-specs`` target at the end of each release
to automatically move completed specs and populate the redirects file for that
release. For example::

  tox -r -e move-implemented-specs -- --dry-run --verbose train

Remove the ``--dry-run`` flag to perform the actual file moves/writes. Then
commit the changes and submit the review to gerrit as usual.

Example specifications
----------------------

You can find a spec template for a given release in
``specs/<release>-template.rst``.

Backlog specifications
----------------------

Additionally, we allow the proposal of specifications that either do not have a
developer assigned to them or are not targeted for the current release. These
are proposed for review in the same manner as above, but are added to::

  specs/backlog/approved

Specifications in this directory indicate the original author has either become
unavailable or has indicated that they are not going to implement the
specification. The specifications found here are available as projects for
people looking to get involved with Nova. Alternatively, they may be for ideas
generated during a given release cycle to begin design discussions, but not
intended to be implemented until a future cycle. If you are interested in
claiming an unassigned backlog spec, or are the assignee and are ready to
propose it for implementation in the current release, start by posting a review
for the specification that moves it from this directory to the next active
release. To ensure existing links are not broken, redirects must be created in
a fashion similar to the process for ``implemented`` specs above. The
``move-spec`` tox target is available to help with this. For example::

  tox -e move-spec -- --dry-run --verbose specs/backlog/my-great-idea.rst specs/train/approved

Remove the ``--dry-run`` option to perform the actual file moves/writes. Then
commit the changes and submit the review to gerrit as usual.

.. note:: Please do not use ``move-spec`` to repropose an unimplemented spec
          from one release to another. Instead follow the instructions at
          `Previously approved specifications`_

When claiming an unassigned backlog spec, please set yourself as the new
`primary assignee` and maintain the original author in the `other contributors`
list.

Abandoning a specification
--------------------------
.. note:: For now, this process should only be used to abandon backlog specs.
          Please do not use this process for specs in a real release's
          ``approved`` directory. Currently the indication that such a spec is
          abandoned is that it never appears in any release's ``implemented``
          directory. We may change this process in the future.

If it is decided that a ``backlog`` spec is "never" going to be implemented,
post a review moving the specification from ``specs/<release>/approved`` to
``specs/abandoned``. As with the above processes, redirects must be created to
ensure existing links are not broken. The ``abandon-spec`` tox target is
available to help with this. For example::

  tox -e abandon-spec -- --dry-run --verbose specs/backlog/it-was-a-great-idea.rst

Remove the ``--dry-run`` option to perform the actual file moves/writes.

Please add an explanation to the spec indicating why it is being abandoned, and
update the History section accordingly.

Design documents for releases prior to Juno
-------------------------------------------

Prior to the Juno development cycle, this repository was not used for spec
reviews.  Reviews prior to Juno were completed entirely through `Launchpad
blueprints <http://blueprints.launchpad.net/nova>`_

Please note, Launchpad blueprints are still used for tracking the
current status of blueprints. For more information, see
https://wiki.openstack.org/wiki/Blueprints

Working with gerrit and specification unit tests
------------------------------------------------

For more information about working with gerrit, see
http://docs.openstack.org/infra/manual/developers.html#development-workflow

To validate that the specification is syntactically correct (i.e. get more
confidence in the Zuul result), please execute the following command::

  $ tox

After running ``tox``, the documentation will be available for viewing in HTML
format in the ``doc/build/html/`` directory.

Specification review policies
=============================

There are a number of review policies which nova-specs-core will apply when
reviewing proposed specifications. They are:

Trivial specifications
----------------------

Proposed changes which are trivial (very small amounts of code) and don't
change any of our public APIs are sometimes not required to provide a
specification. In these cases a Launchpad blueprint is considered sufficient.
These proposals are approved during the `Open Discussion` portion of the
weekly `nova IRC meeting`_. If you think your proposed feature is trivial and
meets these requirements, we recommend you bring it up for discussion there
before writing a full specification.

Previously approved specifications
----------------------------------

**Specifications are only approved for a single release**. If your
specification was previously approved but not implemented (or not completely
implemented), then you must seek re-approval for the specification. You can
re-propose your specification by doing the following:

* Copy (not move) your specification to the right directory for the current release.
* Update the document to comply with the new template; modify the History
  section; select a new :ref:`feature liaison <feature-liaisons>` if needed.
* If there are no functional changes to the specification (only template
  changes) then add the ``Previously-approved: <release>`` tag to your commit
  message.
* Send for review.
* These specifications are subject to the same review process as any other.
  They need to be reevaluated to ensure the technical aspects are still valid
  and that we still wish to implement it given resource constraints and other
  priorities.

Specifications which depend on merging code in other OpenStack projects
-----------------------------------------------------------------------

For specifications **that depend on code in other OpenStack projects merging**
we will not approve the nova specification until the code in that other project
has merged. The best example of this is Cinder and Neutron drivers. To
indicate your specification is in this state, please use the Depends-On git
commit message tag. The correct format is ``Depends-On: <change id of other
work>``. nova-specs-core can approve the specification at any time, but it
won't merge until the code we need to land in the other project has merged as
well.

New libvirt image backends
--------------------------

There are some cases where an author might propose adding a new libvirt
driver image storage backend which does not require code in other OpenStack
projects. An example was the ceph image storage backend, if we treat that as
separate from the ceph volume support code. Implementing a new image storage
backend in the libvirt driver always requires a specification because of our
historical concerns around adequate CI testing.

.. todo:: Write a fleshed-out section on the roles and responsibilities of the
          nova team, including things like the two +2 rule, the same-company
          trifecta rule, whether +2ing a spec represents a commitment to review
          the corresponding code, etc.

.. _feature-liaisons:

Feature Liaison FAQ
===================

In Ussuri, a mandatory "Feature Liaison" section was added to the spec
template. This section attempts to address some of the questions around this
concept.

What does a Feature Liaison do?
  By signing up to be a feature liaison for a spec, you're agreeing to help
  shepherd the feature through the development process. This has different
  implications depending on the identity/role of the spec owner and your
  relative roles in the project. Some examples:

  * **Liaison for an inexperienced contributor:** This is the case for which
    the liaison concept was conceived. In this case the liaison's job is to
    mentor the spec owner, keep an eye on their progress, let them know when
    they're missing some obscure (or not-so-obscure) part of the process, help
    them understand what "review-ready" means, etc. You are also committing to
    reviewing their code -- or at the very least helping them track down
    suitable reviewers.
  * **Designating yourself as your own liaison:** If you're a nova core or
    experienced nova developer, you're already culturally indoctrinated. You
    know how to navigate the process. You know how to ask for reviews. You
    still can't +1/+2 your own code.
  * **Core or experienced nova dev procures separate liaison:** Since you don't
    need the mentorship aspect, your liaison in this case is really just
    committing to doing reviews. While not necessary, it might be nice to get
    that kind of commitment up front.

  The above is not exhaustive; clearly there is a lot of middle ground between
  an inexperienced contributor and a nova-core as a spec owner. It should
  hopefully be fairly obvious how the liaison's role shifts in that middle
  ground. If further clarification is necessary, please edit this doc.

Feature Liaison need not be a nova-core.
  The role of a liaison does not require +2 powers. A feature liaison should be
  taken to mean "experienced nova developer capable of doing the job". That
  said, whereas nova cores implicitly match that description by virtue of
  having been made cores, non-cores proposed as liaisons should be evaluated on
  a case-by-case basis (by the reviewers of the spec) as part of the spec
  review process to determine whether they qualify. For the most part, "we know
  who you are". (Note that in cases where an experienced non-core is a liaison
  for someone else's feature, they're still signing up to do reviews, which are
  still valuable despite maxing out at +1.)

How do I find a Feature Liaison?
  If you do not already have agreement from someone to act as your liaison,
  note this in your spec draft. You may accelerate the process by communicating
  with the nova development team on IRC (``#openstack-nova``), in a `nova IRC
  meeting`_, or via the `openstack-discuss`_ mailing list.

What about specless blueprints?
  We'll put the name of the feature liaison into the blueprint description.
  It's not as automatically-enforceable as the template checker, but oh well.

How does liaison-hood relate to blueprint approval and prioritization?
  It really doesn't. If you sign up to be a liaison for blueprint X, the nova
  team may still decide blueprint X is a nonstarter for technical reasons; or
  that we don't have the bandwidth to get it done this cycle in light of other
  priorities. You're really just saying, "If this goes, I'm on it."

How does liaison-hood relate to the gerrit review for the spec?
  A liaison can (and really should, though it's not a hard requirement (yet))
  review and +2/+1 a spec for which they're the liaison (but not the owner).
  However, everyone is still encouraged to review and approve other specs as
  well (otherwise nothing will get done) (also see below). (It would be nice if
  an upvote on a spec patch also acted as a commitment to review the
  corresponding code, but the liaison process does not attempt to address
  that (yet).)

Am I still allowed to care about / review / shepherd other approved features for which I didn't volunteer to be a liaison?
  Of course. The point of this is the converse: If you *don't* pay attention to
  features you *did* sign up for, people will draw moustaches on pictures of
  your face. Or horns, if you already have a moustache.

.. _`nova IRC meeting`: https://wiki.openstack.org/wiki/Meetings/Nova
.. _openstack-discuss: http://lists.openstack.org/cgi-bin/mailman/listinfo/openstack-discuss
