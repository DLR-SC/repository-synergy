========================
Team and repository tags
========================

.. image:: https://governance.openstack.org/tc/badges/os-refresh-config.svg
    :target: https://governance.openstack.org/tc/reference/tags/index.html

.. Change things from this point on

=================
os-refresh-config
=================

`os-refresh-config` uses `dib-run-parts` to run scripts in a
pre-defined set of directories::

  /opt/stack/os-config-refresh/pre-configure.d
  /opt/stack/os-config-refresh/configure.d
  /opt/stack/os-config-refresh/post-configure.d
  /opt/stack/os-config-refresh/migration.d
  /opt/stack/os-config-refresh/error.d

`/opt/stack/os-config-refresh` is the default base directory. You can
set `OS_REFRESH_CONFIG_BASE_DIR` environment variable to override the
default one.

Its intended purpose is to separate scripts execution into 4 phases:

1. Quiesce(pre-configure.d),
2. Configure(configure.d),
3. Activate(post-configure.d).
4. Migrate(migration.d),

It runs through all the phases above to ensure configuration is applied
and enabled on a machine. It will run the scripts in error.d and then
exit with a non-zero exit status if any phase has a problem. The scripts
in each phase should not depend on each other having worked properly.

Note: Earlier versions of os-refresh-config ran migration before
post-configure. This was an oversight in the initial design, as
migrations are intended to be online migrations after the host is
fully configured.

For things which must happen while the service is quiesced, that should
be done in the post-configure scripts which control the service state.
