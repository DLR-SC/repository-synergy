Bookstore
=========

.. image:: https://badge.fury.io/py/bookstore.png
   :target: http://badge.fury.io/py/bookstore

.. image:: https://travis-ci.org/rgbkrk/bookstore.png?branch=master
   :target: https://travis-ci.org/rgbkrk/bookstore

⚠️ **This is the 1.x series of `bookstore`. The bookstore 2.x series lives on as a spiritual successor relying on S3, in https://github.com/nteract/bookstore** ⚠️

Stores IPython notebooks automagically onto OpenStack clouds through Swift.

*Add your provider with a pull request!*

**Note: Bookstore requires IPython 1.0+**

Bookstore currently has generic support for OpenStack Swift and simplified
authentication for Rackspace's CloudFiles. Bookstore also handles IPython notebook's
autosave/checkpoint feature and as of the latest release supports multiple checkpoints:

.. image:: https://pbs.twimg.com/media/BVD3olXCMAA2rzb.png
   :alt: Multiple checkpoints

Once installed and configured (added to an ipython profile), just launch
IPython notebook like normal:

.. code-block:: bash

    $ ipython notebook
    2013-08-01 13:44:19.199 [NotebookApp] Using existing profile dir: u'/Users/rgbkrk/.ipython/profile_default'
    2013-08-01 13:44:25.384 [NotebookApp] Using MathJax from CDN: http://cdn.mathjax.org/mathjax/latest/MathJax.js
    2013-08-01 13:44:25.400 [NotebookApp] Serving rgbkrk's notebooks on Rackspace CloudFiles from container: notebooks
    2013-08-01 13:44:25.400 [NotebookApp] The IPython Notebook is running at: http://127.0.0.1:9999/
    2013-08-01 13:44:25.400 [NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).

Installation
------------

Simply:

.. code-block:: bash

    $ pip install bookstore

Alternatively, you can always pull from the master branch if you're the adventurous type:

.. code-block:: bash

    $ pip install git+https://github.com/rgbkrk/bookstore.git

Installation isn't the end though. You need to configure your account details
as well as where you'll be storing the notebooks.

Configuration
-------------

Bookstore has to be added to an IPython profile and configured to work with
your OpenStack provider.

If you want to keep it simple, just add your configuration to the default configuration located at:

.. code-block:: bash

    ~/.ipython/profile_default/ipython_notebook_config.py

Alternatively, you can create a brand new notebook profile for bookstore:

.. code-block:: bash

    $ ipython profile create swiftstore
    [ProfileCreate] Generating default config file: u'/Users/theuser/.ipython/profile_swiftstore/ipython_config.py'
    [ProfileCreate] Generating default config file: u'/Users/theuser/.ipython/profile_swiftstore/ipython_notebook_config.py'

When launching, just set the custom profile you want to use

.. code-block:: bash

    $ ipython notebook --profile=swiftstore

Each provider has their own setup for authentication.

On OpenStack Swift using Keystone Authentication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

OpenStack (generic, non provider specific) has quite a few details you'll need
to configure, namely account name, account key, auth endpoint, and region.
You'll possibly need a tenant id and a tenant name.

Add this to your ipython notebook profile *ipython_notebook_config.py*, making
sure it comes after the config declaration ``c = get_config()``.

.. code-block:: python

    # Setup IPython Notebook to write notebooks to a Swift Cluster
    # that uses Keystone for authentication
    c.NotebookApp.notebook_manager_class = 'bookstore.swift.KeystoneNotebookManager'

    # Account details for OpenStack
    c.KeystoneNotebookManager.account_name = USER_NAME
    c.KeystoneNotebookManager.account_key = API_KEY
    c.KeystoneNotebookManager.auth_endpoint = u'127.0.0.1:8021'
    c.KeystoneNotebookManager.tenant_id = TENANT_ID
    c.KeystoneNotebookManager.tenant_name = TENANT_NAME
    c.KeystoneNotebookManager.region = 'RegionOne'

    # Container on OpenStack Swift
    c.KeystoneNotebookManager.container_name = u'notebooks'

On Rackspace's CloudFiles
~~~~~~~~~~~~~~~~~~~~~~~~~

The Rackspace CloudFileNotebookManager simply needs your ``USER_NAME`` and ``API_KEY``. You can also configure the region to store your notebooks (e.g. ``'SYD'``, ``'ORD'``, ``'DFW'``, ``'LON'``). Note: If you're using Rackspace UK, set your region to ``'LON'``.

Add this to your ipython notebook profile *ipython_notebook_config.py*, making
sure it comes after the config declaration ``c = get_config()``.

.. code-block:: python

    # Setup IPython Notebook to write notebooks to CloudFiles
    c.NotebookApp.notebook_manager_class = 'bookstore.cloudfiles.CloudFilesNotebookManager'

    # Set your user name and API Key
    c.CloudFilesNotebookManager.account_name = USER_NAME
    c.CloudFilesNotebookManager.account_key = API_KEY

    # Container on CloudFiles
    c.CloudFilesNotebookManager.container_name = u'notebooks'

Contributing
------------

Send a pull request on `GitHub <http://www.github.com/rgbkrk/bookstore>`_. It's
that simple. More than happy to respond to issues on GitHub as well.

