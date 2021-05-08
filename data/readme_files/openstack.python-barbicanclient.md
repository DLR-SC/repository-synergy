python-barbicanclient
=====================

.. image:: https://img.shields.io/pypi/v/python-barbicanclient.svg
    :target: https://pypi.org/project/python-barbicanclient/
    :alt: Latest Version

This is a client for the `Barbican <https://github.com/openstack/barbican>`__
Key Management API.  There is a Python library for accessing the API
(`barbicanclient` module), and a command-line script (`barbican`).

Installation
------------

The client is
`pip installable <https://pypi.org/project/python-barbicanclient>`__ as
follows:

.. code:: console

  pip install python-barbicanclient


barbicanclient - Python Library
-------------------------------

The full api is
`documented in the official OpenStack documentation site <https://docs.openstack.org/python-barbicanclient/latest/>`__.


Here's an example of storing a secret in barbican using the python library
with keystone authentication:

.. code:: python

    >>> from keystoneclient.auth import identity
    >>> from keystoneauth1 import session
    >>> from barbicanclient import client

    >>> # We'll use Keystone API v3 for authentication
    >>> auth = identity.v3.Password(auth_url=u'http://localhost:5000/v3',
    ...                             username=u'admin_user',
    ...                             user_domain_name=u'Default',
    ...                             password=u'password',
    ...                             project_name=u'demo',
    ...                             project_domain_name=u'Default')

    >>> # Next we'll create a Keystone session using the auth plugin we just created
    >>> sess = session.Session(auth=auth)

    >>> # Now we use the session to create a Barbican client
    >>> barbican = client.Client(session=sess)

    >>> # Let's create a Secret to store some sensitive data
    >>> secret = barbican.secrets.create(name=u'Self destruction sequence',
    ...                                  payload=u'the magic words are squeamish ossifrage')

    >>> # Now let's store the secret by using its store() method. This will send the secret data
    >>> # to Barbican, where it will be encrypted and stored securely in the cloud.
    >>> secret.store()
    u'http://localhost:9311/v1/secrets/85b220fd-f414-483f-94e4-2f422480f655'

    >>> # The URI returned by store() uniquely identifies your secret in the Barbican service.
    >>> # After a secret is stored, the URI is also available by accessing
    >>> # the secret_ref attribute.
    >>> print(secret.secret_ref)
    http://localhost:9311/v1/secrets/091adb32-4050-4980-8558-90833c531413

    >>> # When we need to retrieve our secret at a later time, we can use the secret_ref
    >>> retrieved_secret = barbican.secrets.get(u'http://localhost:9311/v1/secrets/091adb32-4050-4980-8558-90833c531413')
    >>> # We can access the secret payload by using the payload attribute.
    >>> # Barbican decrypts the secret and sends it back.
    >>> print(retrieved_secret.payload)
    the magic words are squeamish ossifrage

.. note::

    In order for the example above to work Barbican must be running and
    configured to use the Keystone Middleware. For more information on
    setting this up please visit:
    https://docs.openstack.org/barbican/latest/configuration/keystone.html [1]_

barbican - Command Line Client
------------------------------

The command line client is self-documenting. Use the --help flag to access the
usage options

.. code:: console

    $ barbican --help
    usage: barbican [--version] [-v] [--log-file LOG_FILE] [-q] [-h] [--debug]
                    [--no-auth] [--os-identity-api-version <identity-api-version>]
                    [--os-auth-url <auth-url>] [--os-username <auth-user-name>]
                    [--os-user-id <auth-user-id>] [--os-password <auth-password>]
                    [--os-user-domain-id <auth-user-domain-id>]
                    [--os-user-domain-name <auth-user-domain-name>]
                    [--os-tenant-name <auth-tenant-name>]
                    [--os-tenant-id <tenant-id>]
                    [--os-project-id <auth-project-id>]
                    [--os-project-name <auth-project-name>]
                    [--os-project-domain-id <auth-project-domain-id>]
                    [--os-project-domain-name <auth-project-domain-name>]
                    [--endpoint <barbican-url>] [--insecure]
                    [--os-cacert <ca-certificate>] [--os-cert <certificate>]
                    [--os-key <key>] [--timeout <seconds>]

    Command-line interface to the Barbican API.

    optional arguments:
      --version             show program's version number and exit
      -v, --verbose         Increase verbosity of output. Can be repeated.
      --log-file LOG_FILE   Specify a file to log output. Disabled by default.
      -q, --quiet           suppress output except warnings and errors
      -h, --help            show this help message and exit
      --debug               show trace backs on errors
      --no-auth, -N         Do not use authentication.
      --os-identity-api-version <identity-api-version>
                            Specify Identity API version to use. Defaults to
                            env[OS_IDENTITY_API_VERSION] or 3.

      --os-auth-url <auth-url>, -A <auth-url>
                            Defaults to env[OS_AUTH_URL].
      --os-username <auth-user-name>, -U <auth-user-name>
                            Defaults to env[OS_USERNAME].
      --os-user-id <auth-user-id>
                            Defaults to env[OS_USER_ID].
      --os-password <auth-password>, -P <auth-password>
                            Defaults to env[OS_PASSWORD].
      --os-user-domain-id <auth-user-domain-id>
                            Defaults to env[OS_USER_DOMAIN_ID].
      --os-user-domain-name <auth-user-domain-name>
                            Defaults to env[OS_USER_DOMAIN_NAME].
      --os-tenant-name <auth-tenant-name>, -T <auth-tenant-name>
                            Defaults to env[OS_TENANT_NAME].
      --os-tenant-id <tenant-id>, -I <tenant-id>
                            Defaults to env[OS_TENANT_ID].
      --os-project-id <auth-project-id>
                            Another way to specify tenant ID. This option is
                            mutually exclusive with --os-tenant-id. Defaults to
                            env[OS_PROJECT_ID].
      --os-project-name <auth-project-name>
                            Another way to specify tenant name. This option is
                            mutually exclusive with --os-tenant-name. Defaults to
                            env[OS_PROJECT_NAME].
      --os-project-domain-id <auth-project-domain-id>
                            Defaults to env[OS_PROJECT_DOMAIN_ID].
      --os-project-domain-name <auth-project-domain-name>
                            Defaults to env[OS_PROJECT_DOMAIN_NAME].
      --endpoint <barbican-url>, -E <barbican-url>
      --endpoint <barbican-url>, -E <barbican-url>
                            Defaults to env[BARBICAN_ENDPOINT].
      --insecure            Explicitly allow client to perform "insecure" TLS
                            (https) requests. The server's certificate will not be
                            verified against any certificate authorities. This
                            option should be used with caution.
      --os-cacert <ca-certificate>
                            Specify a CA bundle file to use in verifying a TLS
                            (https) server certificate. Defaults to
                            env[OS_CACERT].
      --os-cert <certificate>
                            Defaults to env[OS_CERT].
      --os-key <key>        Defaults to env[OS_KEY].
      --timeout <seconds>   Set request timeout (in seconds).

    See "barbican help COMMAND" for help on a specific command.

    Commands:
      acl get                  Retrieve ACLs for a secret or container by providing its href.
      acl delete               Delete ACLs for a secret or container as identified by its href.
      acl submit               Submit ACL on a secret or container as identified by its href.
      acl user add             Add ACL users to a secret or container as identified by its href.
      acl user remove          Remove ACL users from a secret or container as identified by its href.
      ca get                   Retrieve a CA by providing its URI.
      ca list                  List CAs.
      complete                 print bash completion command
      secret container create  Store a container in Barbican.
      secret container delete  Delete a container by providing its href.
      secret container get     Retrieve a container by providing its URI.
      secret container list    List containers.
      help                     print detailed help for another command
      secret order create      Create a new order.
      secret order delete      Delete an order by providing its href.
      secret order get         Retrieve an order by providing its URI.
      secret order list        List orders.
      secret delete            Delete an secret by providing its href.
      secret get               Retrieve a secret by providing its URI.
      secret list              List secrets.
      secret store             Store a secret in Barbican
      secret update            Update a secret with no payload in Barbican.

* License: Apache License, Version 2.0
* `PyPi`_ - package installation
* `Online Documentation`_
* `Launchpad project`_ - release management
* `Blueprints`_ - feature specifications
* `Bugs`_ - issue tracking
* `Source`_
* `Specs`_
* `Getting involved`_

.. _PyPi: https://pypi.org/project/python-barbicanclient/
.. _Online Documentation: https://docs.openstack.org/python-barbicanclient/latest/
.. _Launchpad project: https://launchpad.net/python-barbicanclient/
.. _Blueprints: https://blueprints.launchpad.net/python-barbicanclient/
.. _Bugs: https://storyboard.openstack.org/#!/project/984
.. _Source: https://git.openstack.org/cgit/openstack/python-barbicanclient/
.. _Getting involved: https://docs.openstack.org/barbican/latest/contributor/getting_involved.html
.. _Specs: https://specs.openstack.org/openstack/barbican-specs/


.. [1] Documentation in this link is currently incomplete. Please use the `devstack setup <https://docs.openstack.org/barbican/latest/contributor/devstack.html>`__.
