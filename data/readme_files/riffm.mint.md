====
mint
====

- about_

- usage_

- syntax_

  - tags_

  - attributes_

  - escaping_

  - python expressions_

  - loops_

  - conditions_

  - comments_

  - simplification_

- inheritance_

- utils_

- CLI_


.. _about:

-----
about
-----

**mint** - is small, fast and easy to use (x)html templates engine.
Implemented with python language.

Why use **mint**?:

single python module
    You can copy ``mint.py`` to your project package and use it.

minimalistic syntax
    Your templates will become smaller and more readable due to
    indent based syntax.

works fast
    **mint** uses ``ast`` python module from standard library
    (since python2.6, thank you Armin and co). So all templates compiles to
    optimized python byte code (during first call) which works fast.

smart
    **mint** knows about (x)html tags and attributes,
    so you get smart escaping. (There is a plan to implement html
    validation during rendering)

not standing in your way
    **mint** does't hide exceptions like some other template engines, and
    shows line in your template file where exception was raised

Template engine was inspired by haml (a template engine written in ruby),
but some concepts were redisigned for simplification and adoptation to python world.


Home page:     https://github.com/riffm/mint
Issue tracker: https://github.com/riffm/mint/issues

.. _usage:

-----
usage
-----

Simple API::

    >>> import mint
    >>> loader = mint.Loader('./templates', cache=True)
    >>> namespace = dict(a='a', b='b')
    >>> result = loader.get_template('index.mint').render(**namespace)

``mint.Loader`` accepts names of directories and then search for template files
by name provided in ``get_template(name)`` call.

.. _syntax:

------
syntax
------

**mint** syntax is based on indention, so you see the document structure and
update document fast. You can move blocks of code and do not search for
begining of parent tag and where it ends.


.. _tags:

tags
----

Just use ``@`` character before tag name to render a tag::

    @tagname

Why **mint** does't use ``%`` char, like haml do?
I think that ``@`` char is more readable and it is just third button on the keyboard,
so you type it by one hand (without finger gymnastics).
Next example shows tags structure::

    @html
        @head
        @body

Indented tags ``@head`` and ``@body`` are children for tag ``@html`` (parent tag).

Text is interpreted as text::

    @div
        @p
            Text of paragraph

So last example will be rendered as::

    <div>
        <p>
            Text of paragraph
        </p>
    </div>

By the way you can use short variant::

    @div
        @p Text of paragraph


.. _attributes:

attributes
----------

To define attribute **mint** uses concept similar to method calls::

    @div.id(content)

Previouse example will be rendered as::

    <div id="content"></div>

To define multiple attributes **mint** uses (so called) chaining::

    @img.alt().src(/img/my_picture.png)

Previouse example will be rendered as::

    <img alt="" src="/img/my_picture.png" />

Note that **mint** knows about selfclosed html tags.

Why do not use python dictionary declaration syntax instead?
Something like ``{alt:"", src:"/img/my_picture.png"}``

Because it is overloaded for html templating. "Chained-methods-call" like
syntax uses less chars to type.

**mint** alows to set/append value of tag attribute somewhere inside tag::

    @div.class(main)
        // set value of attribute
        @.class(header)

    @div.class(main)
        // append value to attribute
        @+class( header)

will be rendered as::

    <div class="header"></div>

    <div class="main header"></div>

This is very handy when you need to set content of tag and it's attributes based
on some condition.

.. _escaping:

escaping
--------

As you know there are some chars we need to escape in xml.  And **mint** does this
automatically for you. It escapes all text inside tags and attributes.
Autoescaping can't be turned off::

    @a.href(/docs?type=1&published=true) docs
    @p.class( ' " < > & )
        <div class="inside" />

Will be rendered as::

    <a href="/docs?type=1&amp;published=true">docs</a>
    <p class="&#39; &quot; &lt; &gt; &amp;">
        &lt;div class=&quot;inside&quot; /&gt;
    </p>


.. _expressions:

python expressions
------------------

Of course, template engine without possibility to insert python expressions is unusable.
So in **mint** you can do this with syntax similar to ``jinja2`` or ``django``::

    @html
        @head
            @title {{ doc.title }}
        @body
            @div.id(content)
                Here we have content {{ doc.content }}

Under the hood **mint** calls ``unicode`` on python expression
and escapes result.

Note that you can provide any valid python expression between tokens ``{{`` ``}}``.
Also note that you can use limited subset of python ``__builtins__``.

In **mint** templates expressions can be used inside text elements and inside attributes::

    @p.class(title {{ doc.main_doc_class }}).id({{ doc.id }}) {{ doc.body }}

As you remember all content inserted in tags (as text) and in attributes is
escaped by **mint**.  And this is good, but sometimes you need to insert
unescaped html.  For this purpose mint uses special class ``mint.Markup``, which
implements ``__html__`` method (this is something like convention). To insert
html inside templates you need to mark your python variables with
``mint.Markup`` inside your python code.

In previous example if ``doc.body`` has html we need attribute ``body`` to return
``mint.Markup(html_string)``. And that ``html_string`` will be inserted in template
without escaping. That is the preferred way to insert markup inside html template.

Also note that there are two contexts to insert markup - tag and attribute.
In case of tag ``mint.Markup`` instances will be inserted without modifications.
But if you attemted to insert markup in attribute it will be additionaly escaped.

For example we have such python code::

    class Doc(object):
        def __init__(self, title, body):
            self.title = mint.Markup(title)
            self.body = mint.Markup(body)

    doc = Doc('<b>title</b>', '<p>content of document</p>')

And such template::

    @div.class(doc)
        @p.class(title).title({{ doc.title }}) {{ doc.title }}
        {{ doc.body }}

The result will be::

    <div class="doc">
        <p class="title" title="&gt;b&lt;title&gt;/b&lt;">
            <b>title</b>
        </p>
        <p>content of document</p>
    </div>

This feature of **mint** is very handy.

.. _loops:

loops
-----

In **mint** you can use python statement ``for``::

    @ul
        #for img in images:
            @li @img.src({{ img.file }})

Note that::

    @li @img.src({{ img.file }})

is similar to::

    @li
        @img.src({{ img.file }})

This is inline tags notation.

.. _conditions:

conditions
----------

Conditions are easy to write too::

    #for doc in docs:
        #if doc.id != current_id:
            @a.href({{ url_for('doc', id=doc.id) }}) {{ doc.title }}
        #elif doc.title == 'I need paragraph':
            @p {{ doc.title }}
        #else:
            {{ doc.title }}


.. _comments:

comments
--------
To comment a line use token ``//``::

    // In this div we provide content, yours C.O.
    @div.id(content)

Xml comments are supported, use token ``--``::

    -- In this div we provide content, yours C.O.
    @div.id(content)

to get::

    <!-- In this div we provide content, yours C.O. -->
    <div id="content"></div>

Sometimes you need to use special tokens in text, so if a line starts with
token ``\`` line is not interpreted by **mint**::

    @p.class(title) Here we have title
    \@p.class(title) Here we have title

Will provide::

    <p class="title">Here we have title</p>
    @p.class(title) Here we have title


.. _simplification:

simplification
--------------

Simplification of syntax provides ambiguity. But it is very handy sometimes.
In **mint** templates you can write such things::

    @ul
        #for image in images:
            @li.class(image) @img.alt().src({{ image.path }})

This simplification alows to write nested tags in one line, one by one. In
previous example all ``img`` tags will be inside ``li``.

Remember rule #1: This records::

    @div.id(1) @div.id(2) @div.id(3)

    @div.id(1)
        @div.id(2) @div.id(3)

    @div.id(1)
        @div.id(2)
            @div.id(3)

are the same.

Rule #2: you can append text to and only to last tag when you use syntax
simplification::

    @ul
        #for doc in docs:
            @li @p.class(title) {{ doc.title }}
                @p.class(descr) {{ doc.description }}

``li`` will be rendered as::

    <li>
        <p class="title">...</p>
        <p class="descr">...</p>
    </li>

Be careful when using syntax simplification.

.. _inheritance:

-----------
inheritance
-----------

**mint** uses slots to implement template inheritance. Slot is nothing more but
python function that retuns markup. Slot can be defined and called anywhere in template::

    // layout.mint
    @html
        @head
            @title {{ title }}
        @body
            @div.id(content)

                #def content():
                    @p.class(title) {{ title }}
                    {{ text }}

                #content()

            @div.id(footer)

As you can see in previous example we define slot ``content`` and call it after that.
During call of slot it's content will be inserted in template. And if we need to insert
different content in that place we should inherit ``layout.mint`` and override ``content``
slot implementation::

    // news.mint
    #base: layout.mint

    #def content():
        #for item in news:
            @a.href({{ url_for('news-item', id=item.id) }}) {{ news.title }}

It is simple and powerful concept.

Slots are python functions, so they see all global variables passed to template and have
own scope. This is very handy, because sometimes people have problems with such things
in other templates engines.

For example we need a block inside ``for`` loop::

    // layout.mint
    @div.id(content)
        #for item in items:
            #loop_slot()

    // photos.mint
    #base: layout.mint

    #def loop_slot():
        @p.class(title) {{ item.title }}
        @img.alt().src({{ item.image.path }})

For **mint** this is natural behavior. And ``item`` is just global variable for
slot ``loop_slot``. But in this case it's better to provide ``item`` to slot
explicitly::

    // layout.mint
    @div.id(content)
        #for item in items:
            #loop_slot(item)

    // photos.mint
    #base: layout.mint

    #def loop_slot(item):
        @p.class(title) {{ item.title }}
        @img.alt().src({{ item.image.path }})

Also we can call base slot inside overrided slot. In our case base slot will
point to slot with same name in our base template. ``__base__`` variable points
inside current slot scope to implementation of current slot in parent template::

    // base.mint
    -- somewhere in head tag
    #def js():
        @script.type(text/javascript).src(/js/main.js)
    #js()


    // photos.mint
    #base: base.mint
    #def js():
        #__base__()
        @script.type(text/javascript).src(/js/photos.js)

This example will results in::

    <!-- somewhere in head tag -->
    <script type="text/javascript" scr="/js/main.js"></script>
    <script type="text/javascript" scr="/js/photos.js"></script>

Slots are plain python functions, slots returns ``Markup`` objects so we can pass slots
or result of slot call to other slots.

And more. We can use slots outside of templates. Lets take photos.mint from
example with ``for`` loop::

    >>> import mint
    >>> t = mint.Loader('.').get_template('photos.mint')
    >>> loop_slot = t.slot('loop_slot')
    >>> # lets take image somewhere
    >>> item = images.get(1)
    >>> loop_slot(item)
    Markup(u'<p class="title">...</p><img alt="" src="..." />')

But sometimes slots needs global variables, you must provide such variables
with kwargs in method ``slot(name, **globals)`` of ``Template`` object.


.. _utils:

-----
utils
-----

**mint** provides global variable ``utils`` which contains useful constants and helper
functions.

Doctype declarations

- ``utils.doctype.html_strict``
- ``utils.doctype.html_transitional``
- ``utils.doctype.xhtml_strict``
- ``utils.doctype.xhtml_transitional``

Example of usage::

    {{ utils.doctype.html_strict }}
    @html

Class ``mint.Markup`` is ``utils.markup`` (this is replacement for hack ``{{ var|safe }}``)

``utils.loop`` is helper function to use with ``for`` statement. It takes iterable
object and returns tuple of item and special object that consist of useful info for each
iteration::

    #for item, l in utils.loop(items):
        @a.href({{ item.url }})
            {{ item.title }} {{ (l.first, l.last, l.odd) }} {{ l.cycle('one', 'two', 'three') }}

In previous example ``l.cycle('one', 'two', 'three')`` will return one of values provided
in sequence. It is handy to colorize tables.

Html helpers

- ``utils.script``
- ``utils.scripts``
- ``utils.link``


.. _CLI:

----------------------
Command Line Interface
----------------------

``mint`` has a CLI. To list available options use ``--help`` flag::

    % python -m mint --help
    Usage: mint.py [options] [template]

    Options:
      -h, --help        show this help message and exit
      -c, --code        Show only python code of compiled template.
      -t, --tokenize    Show tokens stream of template.
      -r N, --repeat=N  Try to render template N times and display average time
                        result.
      -p, --pprint      Turn pretty print on.
      -m, --monitor     Monitor current directory and subdirectories for changes
                        in mint files. And render corresponding html files.

CLI works in two modes:

- rendering
- monitoring


That's all folks!
