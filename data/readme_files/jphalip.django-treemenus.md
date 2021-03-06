=================
Django Tree Menus
=================

.. image:: https://travis-ci.org/jphalip/django-treemenus.png

This is a simple and generic tree-like menuing system for Django_ with an
easy-to-use admin interface. It covers all the essentials for building
tree-structured menus and should be enough for a lot of projects.
It is also easily extendable if you need to add some special behaviour to
your menu items.

django-treemenus works with Django 1.0 and above and with python 2.5 and above.

.. _Django: http://www.djangoproject.com/

Installation
============

Installing an official release
------------------------------

django-treemenus is available on PyPI, and can be installed using Pip::

    pip install django-treemenus

Alternatively, official source releases are made available at https://pypi.python.org/pypi/django-treemenus

Download the .zip distribution file and unpack it. Inside is a script
named ``setup.py``. Run this command::

    python setup.py install

...and the package will install automatically.

Installing the development version
----------------------------------

If you prefer to update Django Tree Menus occasionally to get the latest bug
fixes and improvements before they are included in an official release, do a
git clone instead::

    git clone https://github.com/jphalip/django-treemenus

Then add the ``treemenus`` folder to your PYTHONPATH or symlink (junction, if
you're on Windows), such as in your Python's ``site-packages`` directory.

Hooking Tree Menus to your project
----------------------------------

1. Add ``treemenus`` to the ``INSTALLED_APPS`` setting of your
   Django project.

2. Create django-treemenus tables by running the following command from the
   root of your project::

    python manage.py syncdb

3. Create and add your custom templates to your project template folder. These
   templates are necessary to specify how you want your menus to be displayed
   on your site (See further below for more details on the use of templates).
   Some sample templates are also provided in the package to get you started.

Basic use
=========

To build a menu, log into the admin interface, and click "Menus" under
the Treemenus application section, then click "Add menu". Give your new
menu a name and then save.

Then, to create menu items, click on your menu in the menu list. You will
then see a table in the bottom part of the page with only one item: the
menu's root. Click "Add an item", select its parent (obviously, since this
is the first item you're creating you can only select the root). Fill out
the item's details and click "Save". The new item now shows up in the table.
Now keep going to build the whole structure of your tree menu by creating as
many branches as you like.

When you've finished building your menu from the admin interface, you will
have to write the appropriate templates to display the menu on your site
(see below).

Templates used by django-treemenus
==================================

The views included in django-treemenus use two templates. You need to create
your own templates into your template folder or any folder referenced in the
``TEMPLATE_DIRS`` setting of your project.

``treemenus/menu.html``
-----------------------

Template to specify how to display a menu.

**Context:**

* ``menu``
    Pointer to the menu to display. You can access its root item with
    ``menu.root_item``.

* ``menu_type`` (optional)
    This variable will only be present if it has been specified when
    calling the ``show_menu`` template tag. (See the "Template tags"
    section for more details).

**Example for this template**::

    {% load tree_menu_tags %}

    {% ifequal menu_type "unordered-list" %}
        <ul>
            {% for menu_item in menu.root_item.children %}
                {% show_menu_item menu_item %}
            {% endfor %}
        </ul>
    {% endifequal %}
    {% ifequal menu_type "ordered-list" %}
        <ol>
            {% for menu_item in menu.root_item.children %}
                {% show_menu_item menu_item %}
            {% endfor %}
        </ol>
    {% endifequal %}


``treemenus/menu_item.html``
----------------------------

Template to specify how to display a menu item.

**Context:**

* ``menu_item``
    Pointer to the menu_item to display. You can directly access all
    its methods and variables.

* ``menu_type`` (optional)
    This variable will only be accessible if it has been specified when
    calling the ``show_menu`` template tag (See the "Template tags"
    section for more details).

**Example for this template**::

    {% load tree_menu_tags %}
    <li><a href="{{ menu_item.url }}">{{ menu_item.caption }}</a>
        {% if menu_item.children %}
        <ul>
            {% for child_item in menu_item.children %}
            {% show_menu_item child_item %}
            {% endfor %}
        </ul>
        {% endif %}
    </li>


Template tags
=============

There a 3 template tags to let you display your menus. To be able to use them
you will first have to load the library they are contained in, with::

    {% load tree_menu_tags %}

``show_menu``
-------------

This is the starting point. Call it wherever you want to display your menu
(most of the time it will be in your site's base template).

There are two attributes:

* ``menu_name``
    Name of the menu to display, as it has been saved via the admin interface.
* ``menu_type``
    This attribute is optional. If it is given it is simply
    passed to the ``treemenus/menu.html`` template. It does
    not have any particular pre-defined function but can be
    tested with (% ifequal menu_type "sometype" %} to
    determine how to display the menu (See above example for
    the template ``treemenus/menu.html``).

**Example of use**::

    {% show_menu "TopMenu" %}
    ...
    {% show_menu "LeftMenu" "vertical" %}
    ...
    {% show_menu "RightMenu" "horizontal" %}

``show_menu_item``
------------------

This tag allows you to display a menu item, which is the only attribute.

**Example of use**::

    {% show_menu_item menu_item %}

``reverse_named_url``
---------------------

This tag allows you to reverse the named URL of a menu item, which is passed as a
single string. To know more about named URLs, refer to `the Django template documentation`_.
For example, the passed value could be 'latest_news' or 'show_profile user.id', and that
would be reversed to the corresponding URL (as defined in your URLConf).

.. _the Django template documentation: https://docs.djangoproject.com/en/dev/ref/templates/builtins/#url

**Example of use**::

    <li><a href="{% reverse_named_url menu_item.named_url %}">{{ menu_item.caption }}</a></li>

Attributes and methods
======================

As you've guessed it, you can manipulate two types of objects: menus and menu
items. In this section I present their attributes and methods, which you can use
in your templates.

Menu
----

There is only one attribute that is available: ``root_item``, which points to...
you got it, the menu's root item.

Menu item
---------

* ``menu``
    Returns the menu to which it belongs.

* ``url``
    Returns the item's url.

    **Example of use**::

        <li><a href="{{ menu_item.url }}">{{ menu_item.caption }}</a></li>

* ``parent``
    Returns the menu item's parent (that is, another menu item).

* ``rank``
    Returns the item's rank amongst its siblings. The first item of a branch has
    a rank of 0, the second one has a rank of 1, etc. To change an item's ranking
    you can move it up or down through the admin interface.

    **Example of use**::

        <li><a class="menuitem-{{ menu_item.rank }}" href="{{ menu_item.url }}">{{ menu_item.caption }}</a></li>

* ``level``
    Returns the item's level in the hierarchy. This is automatically calculated by
    the system. For example, the root item has a level 0, and its children have a
    level 1.

    **Example of use**::

        {% ifequal menu_item.level 1 %}
            <li><a class="top-item" href="{{ menu_item.url }}">{{ menu_item.caption }}</a></li>
        {% else %}
            <li><a href="{{ menu_item.url }}">{{ menu_item.caption }}</a></li>
        {% endifequal %}

* ``caption``
    Returns the item's caption.

* ``named_url``
    Use this attribute if you want to use named URLs instead of raw URLs.

    **Example of use**::

        <li><a href="{% reverse_named_url menu_item.named_url %}">{{ menu_item.caption }}</a></li>

* ``has_children``
    Returns True if the item has some children, False otherwise.

* ``children``
    Returns a list with the menu item's children, ordered by rank.

    **Example of use**::

        {% if menu_item.has_children %}
            <li><a class="daddy" href="{{ menu_item.url }}">{{ menu_item.caption }}</a>
                <ul>
                    {% for child in menu_item.children %}
                        {% show_menu_item child %}
                    {% endfor %}
                </ul>
            </li>
        {% else %}
            <li><a href="{{ menu_item.url }}">{{ menu_item.caption }}</a></li>
        {% endif %}

* ``siblings``
    Returns a list with the menu item's siblings (i.e all other items that have the
    same parent), ordered by rank.

Customizing/Extending
=====================

The attributes and methods enumerated above provide the essential behaviour for a
tree-structured menu. If that is not enough for you, it is also possible to add
customized behaviour by extending the menu item definition. To do so, you need to
create a model class that will contain all the extra attributes for your menu items.

To illustrate this, let's say that you'd like to add a ``published`` attribute to your
menu items so that they only show up on your site if ``published`` is turned to ``True``.

To do so, create a new application (let's call it ``menu_extension``), with the following
structure::

    menu_extension
        __init__.py
        models.py
        forms.py

Then, in ``menu_extension.models.py`` add the following::

    from django.db import models
    from treemenus.models import MenuItem

    class MenuItemExtension(models.Model):
        menu_item = models.OneToOneField (MenuItem, related_name="extension")
        published = models.BooleanField(default=False)

It is required that your extension object has the attribute ``menu_item`` that is a **unique** link
to a menu item object. This is what makes the extension possible.
Then you can notice our attribute ``published``, feel free to add any other attribute there to
customize your menu items.

You then need to create the database table that will store your extension data by adding
``menu_extension`` to the ``INSTALLED_APPS`` setting of your Django project, and then running
the following command from the root of your project::

    python manage.py syncdb

Now, you need to specify a form to let you edit those extra attributes from the admin interface.
In your project's ``admin.py`` or your extension menu app's ``admin.py``, add the following::

    from django.contrib import admin
    from treemenus.admin import MenuAdmin, MenuItemAdmin
    from treemenus.models import Menu
    from menu_extension.models import MenuItemExtension

    class MenuItemExtensionInline(admin.StackedInline):
        model = MenuItemExtension
        max_num = 1

    class CustomMenuItemAdmin(MenuItemAdmin):
        inlines = [MenuItemExtensionInline,]

    class CustomMenuAdmin(MenuAdmin):
        menu_item_admin_class = CustomMenuItemAdmin

    admin.site.unregister(Menu) # Unregister the standard admin options
    admin.site.register(Menu, CustomMenuAdmin) # Register the new, customized, admin options

And that's it! Now, when creating or editing a menu item, you'll see an inline form with
all the extension attributes (in this example, the ``published`` check box).

Now, if you want to use ``published`` attribute in your template, you need to use the
menu item's ``extension`` method, as follows::

    {% if menu_item.extension.published %}
        <li><a href="{{ menu_item.url }}">{{ menu_item.caption }}</a></li>
    {% endif %}

Your menu items will now only appear if their ``published`` check box has been ticked.

Using this technique, you can obviously extend your menu items with whatever attribute
you'd like. Other examples might be that you want to add special CSS styles to certain
menu items, or to make some of them show up only if the user is logged in, etc. Simply
add attributes in you extension model and make use of them in your templates to create
special behaviour. See the 'Tips and Tricks' section for more ideas.

Tips and tricks
===============

In this section I give some examples on using or extending menus.
These may just cover some of your own specific needs or at least inspire you and get
you started to make the most out of your menus.

Internationalization
--------------------

Making your menus multi-lingual is very easy if you use the `Django internationalization`_
module. What you can do is apply the translation to the ``caption`` attribute
of a menu_item. For example::

    {% load i18n %}
    ...
    <li><a href="{{ menu_item.url }}">{% trans menu_item.caption %}</a></li>

Then, add manually the translation entries in your ``*.po`` file.

.. _Django internationalization: https://docs.djangoproject.com/en/dev/topics/i18n/

If you use more complex or custom translation systems, you may simply define your
extension class (or create it if you don't already have one) with a method to manage
the translation, for example::

    class MenuItemExtension(models.Model):
        menu_item = models.OneToOneField (MenuItem, related_name="extension")
        ...

        def translation():
            translation = do_something_with(self.menu_item.caption)
            return translation

And then in your template::

    <li><a href="{{ menu_item.url }}">{% trans menu_item.extension.translation %}</a></li>

Login restriction
-----------------

If you want to make some of your menus items private and only available to logged in
users, that's simple! Simply define your extension class (or create it if you don't
already have one) like the following::

    class MenuItemExtension(models.Model):
        menu_item = models.OneToOneField (MenuItem, related_name="extension")
        protected = models.BooleanField(default=False)
        ...

And then in your template::

    {% if menu_item.extension.protected %}
        {% if user.is_authenticated %}
            <li><a href="{{ menu_item.url }}">{{ menu_item.caption }}</a></li>
        {% endif %}
    {% else %}
        <li><a href="{{ menu_item.url }}">{{ menu_item.caption }}</a></li>
    {% endif %}

(assuming that the context variable 'user' represents the currently logged-in user)

Automatically select menu items
-------------------------------

Here I'm going to explain how to automatically select a menu item when visiting
a given page of your site. This is a good example to illustrate the power of
extensions for customizing your menu's behaviour.
For this example, let's say that you'd like to visually select the menu item
'Contact' when visiting the url 'http://www.example.com/contact/'

First, define your extension class (or create it if you don't already have one)
like the following::

    class MenuItemExtension(models.Model):
        menu_item = models.OneToOneField (MenuItem, related_name="extension")
        selected_patterns = models.TextField(blank=True)

``selected_patterns`` is the attribute which will specify for what urls the menu
item should have the 'selected' status.
Refer to the section on extensions above to see how to hook your extension class
to your menus.

Now, in the admin section, edit the 'Contact' menu item and type the following
line in its ``selected_patterns`` textfield::

    ^/contact/$

Here we're using regular expressions so that gives us some flexibility to specify
our 'selected' url patterns. Refer to the official python documentation on
`regular expressions syntax`_ for more detailed information. In this example we're
only using one regular expression pattern (^/contact/$) but you could add as many
as you'd like by typing a different pattern on each line of the textfield.

.. _regular expressions syntax: http://docs.python.org/lib/re-syntax.html

Then, in your ``menu_item.html`` template, use the following 'if' statement::

    {% load menu_extension_filters %}
    ...
    <li><a href="{{ menu_item.url }}" class="{% if menu_item.extension.selected_patterns|match_path:request.path %}selected{% endif %}">{{ menu_item.caption }}</a></li>

With this code, every menu item whose attribute ``selected_patterns`` matches the
current url will be given the 'selected' CSS class (it's up to you to define in
your style sheet what that 'selected' class actually does - maybe change the colour
or the font?). In this example we're allocating a special style to visually
distinguish the selected menu items, but you're obviously free to use the 'if'
statement above to do any form of disctinction you like (for example displaying
all children of a selected menu, etc.)
Don't forget to load the ``menu_extension_filters`` module, which we're going to
create in a moment.

We now need to create the 'match_path' filter. In your ``menu_extension``
application (or whatever name you've given to your menu extension application)
create a directory ``templatetags`` containing two files: ``__init__.py`` (leave it
empty) and ``menu_extension_filters.py`` containing the following code::

    import re
    from django import template

    register = template.Library()

    def match_path(patterns, path):
        if patterns:
            for pattern in patterns.splitlines():
                if re.compile(pattern).match(path):
                    return True
        return False
    register.filter('match_path', match_path)

What it does is test each pattern on each line of our patterns (remember, you can
add one pattern on each line of the ``selected_patterns`` textfield) and returns
true if any of those matches the given path.

Finally, to be able to access the current url through ``request.path`` in your
template, you need to do 2 things:

1) Add ``django.core.context_processors.request`` to your
``TEMPLATE_CONTEXT_PROCESSORS`` setting (see the Django documentation on `context
processors`_ for more details).

.. _context processors: https://docs.djangoproject.com/en/dev/ref/templates/api/#django-core-context-processors-request

2) Use a RequestContext object in your views to pass to your templates. (see Django
documentation on RequestContext_).

.. _RequestContext: https://docs.djangoproject.com/en/dev/ref/templates/api/#subclassing-context-requestcontext

That's it!!
===========

Please log any issue or bug report at https://github.com/jphalip/django-treemenus/issues

Enjoy!

`Julien Phalip`_ (project developer)

.. _Julien Phalip: https://twitter.com/julienphalip
