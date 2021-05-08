rollbar-agent
=============

rollbar-agent is a Python daemon that can monitor log files and push messages to Rollbar. It can monitor:

- ``.rollbar`` files written by a Rollbar notifier library (currently supported in rollbar-php, pyrollbar, and rollbar-agent)
- Python-style log files

(Other log files formats are currently not supported out of the box.)

Who Should Use rollbar-agent
----------------------------

If you are trying to monitor your application's log files, we recommend using a Rollbar notifier library instead
(or in addition, in the case of PHP--see next paragraph). The Rollbar notifiers are easier to install and use and will gather more
context about each error. See https://rollbar.com/docs for a list of supported languages and links to notifiers.

Today, the primary use of rollbar-agent is to provide durable, asynchronous reporting from PHP applications
that are instrumented with rollbar-php. If you are using PHP and performance is important, you'll want to set up
rollbar-agent.

For almost everyone else, rollbar-agent is more complexity than needed when getting started; most other platforms
provide easier ways to do asynchronous reporting that don't require running a separate process. However, rollbar-agent
may still be desirable if:

- you want to minimize work done in your application process, even if it's in a background thread
- durability is important (i.e. it's important that reports to Rollbar succeed even if the main process dies, or that they eventually succeed if the network is temporarily unavailable)

Installing and configuring rollbar-agent will be much easier if you have a basic understanding of
Python virtualenvs and are comfortable editing the configuration files that control services
on your OS.


Requirements
------------
rollbar-agent requires:

- A unix-like system (tested on Fedora and Ubuntu Linux and Mac OS X)
- Python 2.6+
- requests 0.13.1+ (will be installed by pip or setup.py, below)
- a Rollbar_ account


Set up a virtualenv
-------------------

You can install rollbar-agent by using pip, by checking out the code from the GitHub repository, or by
downloading a tar file. In each case, you'll be installing rollbar-agent into a Python virtualenv. If
you don't already have an appropriate virtualenv set up, you should create one now. For more information
on Python virtual environments, see http://docs.python-guide.org/en/latest/dev/virtualenvs/

Install rollbar-agent
---------------------

Once you've created and activated your virualenv, install the rollbar-agent code and configuration files
into that environment using your preferred method below. Each method will install the rollbar-agent library
and put the configuration and service start up files you'll need into the root directory of your virtualenv.  

**Installing with pip**

If you're familiar with pip, you can install rollbar-agent with::

    pip install rollbar-agent

**Installing from source**

If you're comfortable with Git::

    git clone https://github.com/rollbar/rollbar-agent.git
    cd rollbar-agent

Or just grab the .tar.gz::

    wget https://github.com/rollbar/rollbar-agent/archive/v0.4.3.tar.gz
    tar -xzf v0.4.3
    cd rollbar-agent-0.4.3

Then install (may require sudo)::

    python setup.py install


Set up the rollbar-agent service
--------------------------------

Symlink the rollbar-agent executable to /usr/local/rollbar-agent::

    ln -s /path/to/virtualenv/rollbar-agent /usr/local/rollbar-agent

and symlink the rollbar-agent configuration file to /etc/rollbar-agent.conf::

    ln -s /path/to/virtualenv/rollbar-agent.conf /etc/rollbar-agent.conf

**init.d script**

rollbar-agent comes with an example init.d script, chkconfig compatible and tested on Fedora Linux, update-rc.d on Ubuntu Linux. You'll need
to edit this script and make sure the ``VIRTUALENV`` environment variable contains the path to the virtual environment you set up.

Once you've edited the rollbar-agent-init.sh script, symlink ``rollbar-agent-init.sh`` to ``/etc/init.d/rollbar-agent``::

    chmod +x /path/to/virtualenv/rollbar-agent-init.sh
    ln -s /path/to/virtualenv/rollbar-agent-init.sh /etc/init.d/rollbar-agent

On Ubuntu, you'll need to add to rc.d. Run the following::

    update-rc.d rollbar-agent defaults

On Fedora, add to chkconfig::

    chkconfig --add rollbar-agent
    chkconfig on rollbar-agent
    
On other systems, check your system's documentation for its equivalent of chkconfig.

Now, start the service::

    service rollbar-agent start

To check that it's running, tail its log file::

    tail -f /var/log/rollbar-agent.log

Configuration
-------------
Configuration options for rollbar-agent itself are in `rollbar-agent.conf`. If you're using the init script, it has a few of its own configuration variables inside which control how it runs.

**rollbar-agent.conf**
At the bare minimum, you will want to change the following variables:

- ``params.access_token`` -- your Rollbar access token, specifically an API token that allows "post_server_item"
- ``targets`` -- white-space-separated list of files or directories (non-recursive) to process.
- ``statefile`` -- path to a file where the state will be stored. File does not need to exist, but the directory does. This file should *not* be placed somewhere it is likely to be deleted, as that will trigger all files to be re-processed. ``/tmp`` is not a good location.

There are several parameters about formats, etc.; you do NOT need to do anything with these if you're only using rollbar-agent as a relay in combination with one of our other libraries.

Setting the following variables will improve integration:

- ``params.root`` -- path to your code root
- ``params.branch`` -- the current branch

If you're using rollbar-agent alongside rollbar-php, you'll want to enable:

- ``delete_processed_files`` -- when true, files are deleted once processing is complete. Default false.

If your logs are capturing terminal escape sequences such as color / boldness, you may want to set
``filter_chr_attr_sequences = true``.  This will clean all output of character attribute terminal sequences.

Other options are documented in the sample config file.

**rollbar-agent-init.sh**
Configuration variables should be self-explanatory. If you're not using a virtualenv, set ``VIRTUALENV=""``.


Contributing
------------

Contributions are welcome. The project is hosted on github at http://github.com/rollbar/rollbar-agent


Additional Help
---------------
If you have any questions, feedback, etc., drop us a line at team@rollbar.com


.. _Rollbar: http://rollbar.com/
.. _`download the zip`: https://github.com/rollbar/pyrollbar/zipball/master
.. _rollbar-agent: http://github.com/rollbar/rollbar-agent
.. _pip: http://www.pip-installer.org/en/latest/installing.html
