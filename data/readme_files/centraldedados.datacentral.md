Data Central
============

This is a lightweight platform to easily publish and distribute datasets. It was created to be the base for [Central de Dados](http://centraldedados.pt), a repository of data packages related to Portugal. It also used for Data Expeditions and hackathons of [Opendata.ch](https://opendata.ch/).

It uses Open Knowledge's excellent [Data Package](http://frictionlessdata.io/specs/data-package/) specification as a
common format to provide datasets. See the [Frictionless Data
vision](http://frictionlessdata.io) document to understand why it's
crucial to think about dataset packaging and distribution.

The main design principle when coming up with Data Central was
portability and simplicity of deployment. It is a framework-less
approach, using Python scripts to gather and compile all datasets,
creating a static HTML web site. Static sites might not be terribly
sexy, but they're extremely useful for some purposes:

 * data workshops
 * offline work
 * easy deployment
 * portability and replication

We informally refer to this project as "the poor man's
[CKAN](http://ckan.org)".

Data Central even exposes a static JSON 'API', so that developers
have an easy access to the available datasets and their metadata
on the portal.

Installation and Usage
------------

1. **Install dependencies**. After cloning the repository, ensure that
   you have virtualenv installed with this command:

	$ pip show virtualenv

If it's not there, you can install it with:

	$ pip install --user virtualenv

   Now, change
   to the project directory and run `make install`. This will
   create a local virtualenv and install the necessary
   dependencies; it shouldn't be necessary to create a virtualenv
   since the `make` commands are all set to work with the venv
   that `make install` creates inside the Data Central dir.

(A) **Alternative installation**

It is also possible to use the more modern [pipenv](https://pipenv.readthedocs.io/en/latest/) tool to create the environment instead of running `make install`. You will need to copy `settings.conf.sample` to `settings.conf` by hand.   

2. **Edit settings**. Edit the newly created `settings.conf`
   to set your options and point to your data package
   repositories.

3. **Add content**. The sidebar is a good place to tell your visitors
   what this site is about in a few paragraphs. You can edit this in
   `content/welcome_text.md`. There is also a dedicated About page you
   can modify. Look and feel can be customised by editing the default
   theme or adding your own to the `themes` folder and changing settings.

4. **Generate the HTML output**. Just run `make build`!

5. **Push the static HTML output somewhere!**. The generated
   site is placed at the `_output` directory. Just copy the contents
   to your webserver, everything's included.

6. **Run a web server to see the output**. While developing, you
   can also run `make serve` to run a simple webserver, and then
   open the site by pointing your browser to `localhost:8002`.

7. **Upload to a remote web server to publish.** Using *rsync*, your
   portal contents are compressed and uploaded to a remote server with a
   command like `SSH_PATH="my.server.org:/my/remote/path" make deploy`.

Running tests
-------------

Datacentral uses Nose for testing. After installing it on your system or virtualenv, just run

    nosetests tests.py


TODO
----

 * Set up an English language base theme for the HTML output
 * Use [Hyde](http://pypi.python.org/pypi/hyde/) or
   [Pelican](http://getpelican.com) for a more solid static generator back-end
