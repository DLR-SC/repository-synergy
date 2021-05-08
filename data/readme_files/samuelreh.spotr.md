===============================
Spotr
===============================

Spotr simplifies launching, snapshotting and destroying AWS spot instances.

It's designed for users wanting to use a spot instance as a development box, and persist the state in between sessions.

Quick Start
-----------
First, install the library and set a default region:

.. code-block:: sh

    $ pip install spotr

Next, set up credentials and region (in e.g. ``~/.aws/config``):

.. code-block:: ini

    [default]
    aws_access_key_id = YOUR_KEY
    aws_secret_access_key = YOUR_SECRET
    region=us-west-1

Then, launch an instance using:

.. code-block:: sh

  $ spotr launch --type p2.xlarge --max-bid .30 --ami ami-4bf20033

When you're done working, you can save the current state (take a snapshot) using:

.. code-block:: sh

  $ spotr snapshot

And then to terminate the instance:

.. code-block:: sh

  $ spotr destroy
  
Next time you launch an instance, leave out the `--ami` tag and you'll restore the most recent snapshot taken with spotr.

.. code-block:: sh

  $ spotr launch --type p2.xlarge --max-bid .30

You can specify default configurations in ``~/.spotr/config``:

.. code-block:: ini

    [config]
    max_bid=.30
    type=p2.xlarge
