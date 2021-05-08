# chronam

chronam is the [Django](https://djangoproject.com) application that the
Library of Congress uses to make its
[Chronicling America](https://chroniclingamerica.loc.gov) website.
The Chronicling America website makes millions of pages of historic American
newspapers that have been digitized by the
[National Digital Newspaper Program (NDNP)](https://www.loc.gov/ndnp/)
browsable and searchable on the Web. A little bit of background is needed to
understand why this software is being made available.

NDNP is actually a partnership between the Library of Congress, the
[National Endowment for the Humanities (NEH)](https://www.neh.gov), and
cultural heritage organizations
([awardees](https://chroniclingamerica.loc.gov/awardees/)) across the
United States who have applied for grants to help digitize newspapers
in their state. Awardees digitize newspaper microfilm according
to a set of [specifications](https://www.loc.gov/ndnp/guidelines/)
and then ship the data back to the Library of Congress where it is
loaded into Chronicling America.

Awardee institutions are able to use this data however
they want, including creating their own websites that highlight their
newspaper content in the local context of their own collections. The idea of
making chronam available here on Github is to provide a technical option to
these awardees, or other interested parties who want to make their own websites
of NDNP newspaper content available. chronam provides a core set of functionality
for loading, modeling and indexing NDNP data, while allowing you to customize
the look and feel of the website to suit the needs of your organization.

The NDNP data is in the Public Domain and is itself [available](https://chroniclingamerica.loc.gov/data/batches/)
on the Web for anyone to use. The hope is that the chronam software can be
useful for others who want to work with and/or publish the content.

## Install

System level dependencies can be installed by following these operating system
specific instructions:

-   [install_ubuntu.md](install_ubuntu.md)
-   [install_redhat.md](install_redhat.md)

After you have installed the system level dependencies you will need to
install some application specific dependencies, and configure the application.

### Install dependent services

#### MySQL

You will need a MySQL database. If this is a new server, you will need to
start MySQL and assign it a root password:

    sudo service mysqld start
    /usr/bin/mysqladmin -u root password '' # pick a real password

You will probably want to change the password 'pick_one' in the example below
to something else:

    echo "DROP DATABASE IF EXISTS chronam; CREATE DATABASE chronam CHARACTER SET utf8mb4; CREATE USER 'chronam'@'localhost' IDENTIFIED BY 'pick_one'; GRANT ALL ON chronam.* to 'chronam'@'localhost'; GRANT ALL ON test_chronam.* TO 'chronam'@'localhost';" | mysql -u root -p

#### Solr

The [Ubuntu](install_ubuntu.md) and [Red Hat](install_redhat.md) guides have
instructions for installing and starting Solr manually. For developmeny you
may prefer to use Docker:

    cd solr
    docker build -t chronam-solr:latest .
    docker run -p8983:8983 chronam-solr:latest

### Install the application

First you will need to set up the local Python environment and install some
Python dependencies:

    cd /opt/chronam/
    virtualenv -p /usr/bin/python2.7 ENV
    source /opt/chronam/ENV/bin/activate
    cp conf/chronam.pth ENV/lib/python2.7/site-packages/chronam.pth
    pip install -r requirements.pip

Next you need to create some directories for data:

    mkdir /srv/chronam/batches
    mkdir /srv/chronam/cache
    mkdir /srv/chronam/bib

You will need to create a Django settings file which uses the default settings
and sets custom values specific to your site:

1.  Create a `settings.py` file in the chronam directory which imports the default values
    from the provided template for possible customization:

         echo 'from chronam.settings_template import *' > /opt/chronam/settings.py

1.  Ensure that the `DJANGO_SETTINGS_MODULE` environment variable is set to
    `chronam.settings` before you start a Django management command. This can be
    set as a user-wide default in your `~/.profile` or but the recommended way is
    simply to make it part of the virtualenv activation process::

         echo 'export DJANGO_SETTINGS_MODULE=chronam.settings' >> /opt/chronam/ENV/bin/activate

1.  Add your database password to the settings.py file following the standard
    Django [settings documentation](https://docs.djangoproject.com/en/1.8/ref/settings/#databases):

         DATABASES = {
             'default': {
                 'ENGINE': 'django.db.backends.mysql',
                 'NAME': 'chronam_db',
                 'USER': 'chronam_user',
                 'HOST': 'mysql.example.org',
                 'PASSWORD': 'NotTheRealPassword',
             }
         }

You should never edit the `settings_template.py` file since that may change in
the next release but you may wish to periodically review the list of
[changes to that file](https://github.com/LibraryOfCongress/chronam/commits/master/settings_template.py)
in case you need to update your local settings.

Next you will need to initialize database schema and load some initial data:

    django-admin.py migrate
    django-admin.py loaddata initial_data languages
    django-admin.py chronam_sync --skip-essays

And finally you will need to collect static files (stylesheets, images)
for serving up by Apache in production settings:

    django-admin.py collectstatic --noinput

## Load Data

As mentioned above, the NDNP data that awardees create and ship to the Library
of Congress is in the public domain and is made available on the Web as
`batches`. Each batch contains newsaper issues for one or more newspaper
titles. To use chronam you will need to have some of this batch data to load. If
you are an awardee you probably have this data on hand already, but if not
you can use a tool like [wget](http://www.gnu.org/software/wget/) to bulk
download the batches. For example:

    cd /srv/chronam/batches/
    wget --recursive --no-parent --no-host-directories --cut-dirs 2 --reject index.html* https://chroniclingamerica.loc.gov/data/batches/uuml_thys_ver01/

In order to load data you will need to run the load_batch management command by
passing it the full path to the batch directory. So assuming you have downloaded
batch_uuml_thys_ver01 you will want to:

    django-admin.py load_batch /srv/chronam/batches/uuml_thys_ver01

If this is a new server, you may need to start the web server:

    sudo service httpd start

After this completes you should be able to view the batch in the batches report
via the Web:

    http://www.example.org/batches/

## Caching

After loading data, you will need to clear the cache. If you are using a reverse proxie (like Varnish) you will need to also clear that, as well as any CDN you have. Below is a list of URLS that should be cleared based on what content you are loading.

All pages that contain a LCCN are tagged with that LCCN in the cache headers. This allows for purging by specific LCCN tag if there is a update to a batch.

# List of URLs to purge when loading new batch

-   All URLs tagged with `lccn=<LCCN>`
-   All URLs matching these patterns:
    ```
    chroniclingamerica.loc.gov/tabs
    chroniclingamerica.loc.gov/sitemap*
    chroniclingamerica.loc.gov/frontpages*
    chroniclingamerica.loc.gov/titles*
    chroniclingamerica.loc.gov/states*
    chroniclingamerica.loc.gov/counties*
    chroniclingamerica.loc.gov/states_counties*
    chroniclingamerica.loc.gov/cities*
    chroniclingamerica.loc.gov/batches/summary*
    chroniclingamerica.loc.gov/reels*
    chroniclingamerica.loc.gov/reel*
    chroniclingamerica.loc.gov/essays*
    ```

# List of URLs to purge when loading new Awardees

-   All URLs matching `chroniclingamerica.loc.gov/awardees*`

# List of URLs to purge when loading new basic data

-   All URLs matching `chroniclingamerica.loc.gov/institutions*`

# List of URLs to purge when loading code

-   All URLs matching these patterns:
    ```
    chroniclingamerica.loc.gov/ocr
    chroniclingamerica.loc.gov/about
    chroniclingamerica.loc.gov/about/api
    chroniclingamerica.loc.gov/help
    ```

## Run Unit Tests

For the unit tests to work you will need:

-   to have the batch_uuml_thys_ver01 available. You can use the wget command in the previous section to get get it.
-   A local SOLR instance running
-   A local MySQL database
-   Access to the Essay Editor Feed

After that you should be able to:

    cd /opt/chronam/
    django-admin.py test chronam.core.tests --settings=chronam.settings_test

## License

This software is in the Public Domain.
