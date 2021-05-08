This project is a work in progress. Refer to dmsl/test/templates/ for additional syntax not covered here.

Follow development at http://github.com/dasacc22/dmsl or view this readme at http://damsel.dasa.cc

* `Building From Source`_
* `Running Unit Tests`_
* `Submitting Bugs`_
* `Speed Tests`_
* `Features and Examples`_

  * `Command Line Interface`_
  * `Django Example`_
  * `Generic Source Example`_

* `Language Features`_

  * `Elements and Attributes`_
  * `Embedding Python`_
  * `Filters`_
  * `Reusable Templates`_

Building From Source
====================
The latest version of dmsl on pypi is 0.4.1 and has no package dependencies. Python sources are required to compile
C extensions

::

  sudo pip install dmsl

If building from git, dmsl depends on Cython >= 0.15.1 so install as per your distribution, for example

::

  sudo easy_install cython

After satisfying cython dependency, clone the repo from github, build and install globally with the following

::

  git clone git://github.com/dasacc22/dmsl.git
  cd dmsl
  sudo python setup.py install

or if you wish to not install globally, you can build the C extensions in place
and use from directory

::

  python setup.py build_ext -i

Running Unit Tests
==================
To run unit tests, build in place and execute test/ directory

::

  python setup.py build_ext -i
  cd dmsl/
  python test/

Submitting Bugs
===============
Please submit bugs and feature requests to the github issue tracker.

Speed Tests
===========
Damsel is fast while keeping the codebase relatively small. Below are results
from the genshi svn benchmark bigtable.py for different template languages.

This test creates a table with 1000 rows, each containing 10 columns from calling
dict.values() and setting each as the column text. It's a silly test, but let's
look at how this can be handled in dmsl::

  %table for row in table:
      %tr for col in row.values():
          %td {col}

And the results::

  Damsel Template  44.45 ms
  Mako Template    21.64 ms
  Genshi Template  127.03 ms
  Django Template  274.57 ms

Features and Examples
=====================

Command Line Interface
----------------------
Damsel can run via command line. For python2.7

  python -m dmsl -h  # see for more info

For python2.6

  pip install argparse
  python -m dmsl.__main__ -h

Django Example
--------------
I'm not a django developer but I did run through a portion of the tutorial to
provide enough informationhere to get started.

Edit settings.py and add the following::

  import dmsl
  dmsl.set_template_dir('/path/to/dmsl/templates')

The following two samples are adapted from the polls example from django docs.
Edit views.py and render a response like this::

  from polls.models import Poll
  from django.http import HttpResponse
  import dmsl
  
  def index(request):
      latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
      context = {'latest_poll_list': latest_poll_list}

      # there's two ways to render the template depending on if you're implement a caching mechanism
      # dmsl.Template returns an object you can store in memory for rendering later
      # Note the ** to expand the dict as keyword arguments.
      response = dmsl.Template('index.dmsl').render(**context)
      # optionally you could simply do the following which simply calls the above
      # response = dmsl.parse('index.dmsl', **context)
      return HttpResponse(response)

The following is the contents of index.dmsl::

  %html %body
      if not latest_poll_list:
          %p No polls are available
  
      %ul for poll in latest_poll_list:
          %li %a[href="/polls/{poll.id}/"] {poll.question}

Errors in a template will throw a RenderException. Insepct the "Exception Value:" on the django error page for the dmsl file
and line number listed next to it.

That should be enough to get a savvy django developer started. I'll get a more complete example done in the future.

Generic Source Example
----------------------
To use in source::

  import dmsl
  dmsl.set_template_dir('./templates')
  dmsl.Template('index.dmsl').render(**{'content': 'Hello World'})

Language Features
=================

Elements and Attributes
-----------------------
Damsel features html outlining similar to css selectors. The most notable difference is using a percent (%) to specify a regular tag::

  %html
      %body Hello World

Damsel is indention based, but works just fine with variable indention with a minimum of two spaces and as long as blocks align as intended::

  %html
    %body
          %p This works just fine

Tags can also be inlined if they are only wrappers::

  %html %body %ul
      %li %span Home
      %li %span Page

Classes and IDs can be specified the same as CSS. If no tag is specified, a DIV is created by default::

  %html %body
      #top %h1.title Hello World
      #content %p.text

Attributes are specified as in CSS. Breaking attributes across multiple lines is not yet implemented::

  %html %body
      %img[border=0][style="margin: 20px;"]
      %a#home.link[href="http://www.dasa.cc"]

Embedding Python
----------------
Damsel also supports embedding python in the document. There's no special syntax for use aside from embedding a function call inline of a tag, starting the call with a colon (:). HTML outlining and python can be intermixed for different effect. Embedding a variable within an outline element is done via the standard python string `Formatter <http://docs.python.org/library/string.html#format-string-syntax>`_::
  
  n = 4
  greet = lambda x: 'Hello, '+x
  %html %body for x in range(n):
      y = x*2.5
      %p Number is {x}. :greet('Daniel'). Here's the number multiplied and formatted, {y:.2f}

str.format is also available but is not safe for formatting user input. In cases where you want to call this directly with safety checks, fmt is available in the sandbox::

  %html %body %ul
      [fmt('%li {0}', x) for x in range(10)]

By default, html sequences are escaped when using the python formatter. You can control this by using the two builtin conversion types, !r and !s. When repr an object, this will escape the item, while the latter leaves it as is::

  bad = '<strong> hello'
  %html %body
      %p This output will be escaped, {bad}
      %p This is same as above, {bad!r}
      %p This output will not be escaped, {bad!s} causing this text to be bold

Python can be used to control the flow of the document as well::

  val = False
  %html %body
      %p Test the value of val
      
      if val:
          %p val is True
      else:
          %p val is False

It's important to note how the document becomes aligned. Intermixed outline elements will be left-aligned to their nearest python counterpart. So above, %p val is False will be the resulting object, and will be properly aligned where the if statement is, placing it as a node of body.

The evaluation of python code takes place in a sandbox that can be extended with custom objects and functions. So for example, in your controller code::

  import pymongo.objectid
  import dmsl
  dmsl.extensions['ObjectId'] = pymongo.objectid.ObjectId

ObjectId will then be available for use in your dmsl templates.

Filters
-------
Another extensible feature of dmsl are filters. A filter allows you to write a slightly altered syntax for calling a python function. Take for example the builtin js filter used for specifying multiple javascript files in a particular location::

  def js(s, _locals):
      s = s.splitlines()
      n = s[0]
      s = s[1:]
      return ['%script[src={0}{1}][type="text/javascript"]'.format(n, x) for x in s]

In a dmsl template, this (as other filters) can be accessed like so::

  %html %head
      :js /js/lib/
          jquery.min.js
          jquery.defaultinput.js
          utils.js
          js.js

This would be the same as explicitly typing it out::

  %html %head
      %script[src="/js/lib/jquery.min.js"][type="text/javascript"]
      %script[src="/js/lib/jquery.defaultinput.js"][type="text/javascript"]
      %script[src="/js/lib/utils.js"][type="text/javascript"]
      %script[src="/js/lib/js.js"][type="text/javascript"]

Filters can be used for most anything from a docutils or markdown processor, automatic form generation based on keywords and variables, or to whatever you might imagine.

Reusable Templates
------------------
Being able to create templates are a must and there are two methods implemented in dmsl to do so. The first is the standard include statement. Consider the following file, top.dmsl::

  #top
      %h1 Hello World
      %p.desc This is a test.

This file can then be included into another, for example, overlay.dmsl::

  %html %body
      include('top.dmsl')
      #content
          %p One
          %p Two

The top.dmsl contents will be aligned appropriately based upon its location in overlay.dmsl. The second method for creating a proper template is the ability to extend a dmsl template. This is handled by a call to the extends function, and then specifying which portion of the template we want to extend. Specifying which portion to extend is based on the ID assigned to a tag. Take the overlay.dmsl example from above. There are two elements we can extend, #top and #content. We can either override the contents, or append new elements to them. Let's do this in index.dmsl::

  extends('overlay.dmsl')
  
  #top %h1 This will override all elements in top
  #content[super=]
      %p three

Here, we simply specify the the tag hash we want to access and then provide the nested content. If a super attribute is specified, this tells dmsl to append the content to the current element we're extending. This super attribute will **not** be a part of the final output. This method also forces strict conformance to a single ID per element, so if you're use to given multiple nodes the exact same ID, now is a good time to stop.

More examples coming soon, refer to test/templates for more.
