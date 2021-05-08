==================================
Python bindings for the Ironic API
==================================

Team and repository tags
------------------------

.. image:: https://governance.openstack.org/tc/badges/python-ironicclient.svg
    :target: https://governance.openstack.org/tc/reference/tags/index.html

Overview
--------

This is a client for the OpenStack `Bare Metal API
<https://docs.openstack.org/api-ref/baremetal/>`_. It provides:

* a Python API: the ``ironicclient`` module, and
* a command-line interfaces: ``openstack baremetal``

Development takes place via the usual OpenStack processes as outlined in the
`developer guide <https://docs.openstack.org/infra/manual/developers.html>`_.
The master repository is on `opendev.org
<https://opendev.org/openstack/python-ironicclient/>`_.

``python-ironicclient`` is licensed under the Apache License, Version 2.0,
like the rest of OpenStack.

.. contents:: Contents:
   :local:

Project resources
-----------------

* Documentation: https://docs.openstack.org/python-ironicclient/latest/
* Source: https://opendev.org/openstack/python-ironicclient
* Bugs: https://storyboard.openstack.org/#!/project/959
* Release notes: https://docs.openstack.org/releasenotes/python-ironicclient/

Python API
----------

Quick-start Example::

    >>> from ironicclient import client
    >>>
    >>> kwargs = {'os_auth_token': '3bcc3d3a03f44e3d8377f9247b0ad155',
    >>>           'ironic_url': 'http://ironic.example.org:6385/'}
    >>> ironic = client.get_client(1, **kwargs)


``openstack baremetal`` CLI
---------------------------

The ``openstack baremetal`` command line interface is available when the bare
metal plugin (included in this package) is used with the `OpenStackClient
<https://docs.openstack.org/python-openstackclient/latest/>`_.

There are two ways to install the OpenStackClient (python-openstackclient)
package:

* along with this python-ironicclient package::

  # pip install python-ironicclient[cli]

* directly::

  # pip install python-openstackclient

An example of creating a basic node with the ``ipmi`` driver::

    $ openstack baremetal node create --driver ipmi

An example of creating a port on a node::

    $ openstack baremetal port create --node <UUID> AA:BB:CC:DD:EE:FF

An example of updating driver properties for a node::

    $ openstack baremetal node set --driver-info ipmi_address=<IPaddress> <UUID or name>

For more information about the ``openstack baremetal`` command and
the subcommands available, run::

    $ openstack help baremetal
