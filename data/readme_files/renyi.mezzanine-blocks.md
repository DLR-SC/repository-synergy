Overview
========
A mezzanine flavored fork of [django-flatblocks] [1].
The goal of this project is to be able to easily create custom blocks of text/HTML
in the template, and can be editable via admin.


Features
===================
1. Raw Text Block, Rich Text Block, Image Block
2. Multisite support (via Mezzanine's Slugged).
3. Frontend inline editing.
4. Categories for easier block management.
5. Optional MPTT support for categories.
6. Optional unlimited passed arguments in the template
7. Compatibility with modeltranslation.


Requirements
============
Required
    - [Mezzanine CMS] [2]

Optional
    - [Django MPTT] [3]


Installation
============
1. Add mezzanine_blocks to your virtualenv or clone the repository :
```bash
    pip install git+git://github.com/renyi/mezzanine-blocks.git
```

2. Add "mezzanine_blocks" to INSTALLED_APPS:
```python
    INSTALLED_APPS = (
        "...",
        "mezzanine_blocks",
    )
```

3. Add blocks menu item to admin menu (Optional):
```python
    ADMIN_MENU_ORDER = (
        ("Content", (
                "pages.Page",
                "mezzanine_blocks.Block",
                "mezzanine_blocks.RichBlock",
                "mezzanine_blocks.ImageBlock",
                "blog.BlogPost",
                "blog.BlogCategory",
                "generic.ThreadedComment",
                ("Media Library", "fb_browse"),
            )
        ),
    )
```
4. Run `python manage.py createdb` or `python manage.py syncdb && python manage.py migrate`.

Usage
=====
1. Include block_tags in the template:

    {% load ... block_tags %}

2. Insert block anywhere in the template:

    {% flatblock "My Awesome Block" %}

    {% richflatblock "My Awesome HTML Block" %}

    {% imageflatblock "My Image Block" %}

3. You should see the blocks in the admin.

Options
=======
Options are similar to django-flatblocks.

    {% flatblock {block} %}
    {% flatblock {block} {timeout} %}
    {% flatblock {block} using {tpl_name} %}
    {% flatblock {block} using {tpl_name} {passed_args} %}
    {% flatblock {block} {timeout} using {tpl_name} %}
    {% flatblock {block} {timeout} using {tpl_name} {passed_args} %}

    {% richflatblock {block} %}
    {% richflatblock {block} {timeout} %}
    {% richflatblock {block} using {tpl_name} %}
    {% richflatblock {block} using {tpl_name} {passed_args} %}
    {% richflatblock {block} {timeout} using {tpl_name} %}
    {% richflatblock {block} {timeout} using {tpl_name} {passed_args} %}

    {% imageflatblock {block} %}
    {% imageflatblock {block} {timeout} %}
    {% imageflatblock {block} using {tpl_name} %}
    {% imageflatblock {block} using {tpl_name} {passed_args} %}
    {% imageflatblock {block} {timeout} using {tpl_name} %}
    {% imageflatblock {block} {timeout} using {tpl_name} {passed_args} %}

If you use {passed_args} to recover the arguments, add the tag {{passed_args}} in your template, if various
arguments exists, add loop on {{passed_args}} exemple:

{% for args in passed_args %}
    {{args}}
{% endfor%}

or directly by index:
{{passed_args.0}}
{{passed_args.1}}
etc.


Installation
============
Version 0.9.6
-----------
    - Bumped version
    - Compatibility with modeltranslation
Version 0.9.5
-----------
    - Bumped version to 0.9.5
    - Fixed error if caching args not exist

Version 0.9.4
-----------
    - Bumped version to 0.9.4
    - Added unlimited passed arguments in the template.

Version 0.9
-----------
    - Bumped version to 0.9.
    - Added Image Block.
    - Added Categories for easier block management (Optional MPTT).
    - Added frontend inline editing tags to templates.
    - Bugfix: Problem with slug when block title has whitespace.
    - Cache key prefix now editable in defaults.py.

Version 0.1
-----------
    - Initial Release
    - RawText block, and RichText block.
    - Multisite support.

[1]: https://github.com/zerok/django-flatblocks/ "django-flatblocks"
[2]: http://mezzanine.jupo.org "Mezzanine CMS"
[3]: https://github.com/django-mptt/django-mptt "Django MPTT"
