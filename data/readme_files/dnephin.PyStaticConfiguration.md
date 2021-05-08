PyStaticConfiguration
=====================

A python library for loading, validating and reading configuration from many
heterogeneous formats. Configuration is split into two phases.

Configuration Loading
---------------------

Configuration is read from files or python objects, flattened, and merged
into a container called a `namespace`. Namespaces are used to separate
unrelated configuration groups.

If configuration is changed frequently, it can also be reloaded easily
with very little change to the existing code.


Configuration Reading
---------------------

A configuration value is looked up in the `namespace`. It is validating and
converted to the requested type.


.. contents:: Contents
    :local:
    :depth: 1
    :backlinks: none



Build Status
------------

.. image:: https://travis-ci.org/dnephin/PyStaticConfiguration.svg?branch=master
    :target: https://travis-ci.org/dnephin/PyStaticConfiguration
    :alt: Travis CI build status

.. image:: https://img.shields.io/pypi/v/PyStaticConfiguration.svg
    :target: https://pypi.python.org/pypi/PyStaticConfiguration
    :alt: Latest PyPI version

.. image:: https://coveralls.io/repos/github/dnephin/PyStaticConfiguration/badge.svg?branch=master
    :target: https://coveralls.io/github/dnephin/PyStaticConfiguration?branch=master
    :alt: Code Test Coverage



Install
-------

* PyStaticConfiguration is available on pypi: https://pypi.python.org/pypi/PyStaticConfiguration
* The source is hosted on github: https://github.com/dnephin/PyStaticConfiguration

.. code-block:: bash

    $ pip install PyStaticConfiguration


Also see the 
`release notes <http://pythonhosted.org/PyStaticConfiguration/release_notes.html>`_.

Documentation
-------------

http://pythonhosted.org/PyStaticConfiguration/


Examples
--------

A common minimal use of staticconf would be to use a single yaml configuration
file and read some values from it.

.. code-block:: python

    import staticconf

    filename = 'hosts.yaml'
    namespace = 'hosts'

    # Load configuration from the file into namespace `hosts`
    staticconf.YamlConfiguration(filename, namespace=namespace)
    ...

    # Some time later on, read values from that namespace
    print staticconf.read('database.slave', namespace=namespace)
    print staticconf.read('database.master', namespace=namespace)


`hosts.yaml` might look something like this:

.. code-block:: yaml

    database:
        slave: dbslave_1
        master: dbmaster_1


A more involved example would load configuration from multiple files, create
a watcher for reloading, and read some config values.

.. code-block:: python

    from functools import partial
    import os
    import staticconf


    def load_config(config_path, defaults='~/.myapp.yaml`)
        # First load global defaults if the file exists
        staticconf.INIConfiguration('/etc/myapp.ini', optional=True)

        # Next load user defaults
        staticconf.YamlConfiguration(defaults, optional=True)

        # Next load the specified configuration file
        staticconf.YamlConfiguration(config_path)

        # Now let's override it with some environment settings
        staticconf.DictConfiguration(
            (k[6:].lower(), v) for k, v in os.environ.items() if k.startswith('MYAPP_'))


    def build_watcher(filename):
        return staticconf.ConfigFacade.load(
            filenames, 'DEFAULT', partial(load_config, filename))

    def run(config_path):
        watcher = build_watcher(config_path)
        while is_work():
            watcher.reload_if_changed()

            current_threshold = staticconf.read_float('current_threshold')
            do_some_work(current_thresold)
