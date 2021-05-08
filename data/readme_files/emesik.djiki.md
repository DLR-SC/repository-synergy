Djiki
=====
Djiki is a lightweight, portable Wiki engine based on Django. It offers full functionality
of a wiki engine without any configuration, yet it might be easily customized to match
your preferred environment.

Features:

* Creole markup,
* anonymous and registered edits,
* automatic merges of parallel edits when possible,
* inclusion of images,
* diff views between revisions,
* reverts to any revision in the history,
* automatic undos of any historical revision, if possible.
* not strictly bound to Django user model and template engine, you may replace them

Requirements
------------
* google-diff-match-patch:
  http://code.google.com/p/google-diff-match-patch/

* WikiCreole parser in Python:
  http://oink.sheep.art.pl/WikiCreole%20parser%20in%20python
  *It is used in the example implementation, but not required by Djiki itself.
  You are free use any other markup or no markup at all.*

* sorl-thumbnail:
  https://github.com/sorl/sorl-thumbnail
  *It is used in the example templates, but you may run djiki
  with any other thumbnailing module or without one at all.*

Usage
-----
* Add 'djiki' and 'sorl.thumbnail' to your INSTALLED_APPS setting.
* Run './manage.py syncdb' in your project.
* Add the following to your URLconf::

    (r'wiki/', include('djiki.urls')),

* Add the required setting DJIKI_IMAGES_PATH
* Create a 'base.html' that Djiki expects to exist and acts as a base template
  for all the wiki pages. It must have a 'page' block. Alternatively, supply
  your own 'djiki/base.html' that overrides the supplied template.
* Optionally include/add the provided CSS in media/css/styles.css to your page
  template.

Settings
--------

The following settings configure Djiki's behavior:

``DJIKI_PARSER`` — a Python path to the markup parser. The default is
``djiki.parsers.wikicreole``.

``DJIKI_IMAGES_PATH`` — path to images, relative to MEDIA_ROOT.

``DJIKI_SPACES_AS_UNDERSCORES`` — makes Djiki replace whitespaces in
URLs by underscores. It's a choice between having nice or exact URLs.
Depending on the settings, the adresses may look as
``http://djiki.org/wiki/Main_Page`` or ``http://djiki.org/wiki/Main%20Page``
This setting will also squash multiple spaces into one. It affects image
names in the same way, too. Defaults to True.

``DJIKI_AUTHORIZATION_BACKEND`` — a Python path to authorization backend.
The default is ``djiki.auth.base.UnrestrictedAccess``, which grants full
read/write permissions to all clients. The other included backends are
``djiki.auth.base.OnlyAuthenticatedEdits`` and ``djiki.auth.base.OnlyAdminEdits``.

``DJIKI_TEPLATING_BACKEND`` — a Python path to a templating backend.
The default is ``djiki.templating.django_engine``, which is a light wrapper
over the standard Django template engine. Therefore you are not strictly bound
to the default implementation. The author, for example, uses *Jinja2* in some
of his projects.

``DJIKI_IMAGES_STORAGE`` — a Python path to file storage used to keep images.
If absent, ``DEFAULT_FILE_STORAGE`` will be used.

Parsers
-------

Djiki allows you to use custom markup parser and it is no longer required
to use Creole. The default behavior, however, is to pass all the page
contents through ``djiki.parsers.wikicreole`` module. The other choices are:

* ``djiki.parsers.raw`` — passes the content without modification, allowing
  for raw HTML. This should not be used in a public wiki, as users may
  enter malicious code.

* ``djiki.parsers.html.SafeHTML`` — it is a safer alternative, which
  filters the resulting content from dangerous HTML elements like scripts,
  CSS styles or annoying and invalid tags.

Images
------

The standard Creole markup has been extended to handle resizing of
images. The standard syntax of ``{{Image_name.jpg|Image title}}`` is
still valid, however you may add size by typing
``{{Image_name.jpg|300x200|Image title}}`` or even omit the title:
``{{Image_name.jpg|300x200}}``.

Templating
----------



Roadmap
-------

* more markup backends; MediaWiki is the main priority
* page operations: rename, delete
* multi-language support, interwiki links
* translations
