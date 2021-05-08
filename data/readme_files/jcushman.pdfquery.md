========
PDFQuery
========
------------------------------------------------------------
Concise, friendly PDF scraping using JQuery or XPath syntax.
------------------------------------------------------------

.. image:: https://travis-ci.org/jcushman/pdfquery.png
   :alt: Travis Build Status
   :target: https://travis-ci.org/jcushman/pdfquery
.. image:: https://ci.appveyor.com/api/projects/status/d9or9795d9b66ai7?svg=true
   :alt: Appveyor Build Status
   :target: https://ci.appveyor.com/project/jcushman/pdfquery


PDFQuery is a light wrapper around pdfminer, lxml and pyquery. It's designed to reliably extract data from sets of
PDFs with as little code as possible.

.. contents:: **Table of Contents**

Installation
============

``easy_install pdfquery`` or ``pip install pdfquery``.

Quick Start
===========

The basic idea is to transform a PDF document into an element tree so we can find items with JQuery-like selectors
using pyquery. Suppose we're trying to extract a name from a set of PDFs, but all we know is that it appears
underneath the words "Your first name and initial" in each PDF::

    >>> pdf = pdfquery.PDFQuery("tests/samples/IRS_1040A.pdf")
    >>> pdf.load()
    >>> label = pdf.pq('LTTextLineHorizontal:contains("Your first name and initial")')
    >>> left_corner = float(label.attr('x0'))
    >>> bottom_corner = float(label.attr('y0'))
    >>> name = pdf.pq('LTTextLineHorizontal:in_bbox("%s, %s, %s, %s")' % (left_corner, bottom_corner-30, left_corner+150, bottom_corner)).text()
    >>> name
    'John E.'

Note that we don't have to know where the name is on the page, or what page it's on,
or how the PDF has it stored internally.

*Performance Note:* The initial call to pdf.load() runs very slowly, because the underlying
pdfminer library has to compare every element on the page to every other element.
See the Caching section to avoid this on subsequent runs.

Now let's extract and format a bunch of data all at once::

    >>> pdf = pdfquery.PDFQuery("tests/samples/IRS_1040A.pdf")
    >>> pdf.extract( [
         ('with_parent', 'LTPage[pageid="1"]'),
         ('with_formatter', 'text'),

         ('last_name', 'LTTextLineHorizontal:in_bbox("315,680,395,700")'),
         ('spouse', 'LTTextLineHorizontal:in_bbox("170,650,220,680")'),

         ('with_parent', 'LTPage[pageid="2"]'),

         ('oath', 'LTTextLineHorizontal:contains("perjury")', lambda match: match.text()[:30]+"..."),
         ('year', 'LTTextLineHorizontal:contains("Form 1040A (")', lambda match: int(match.text()[-5:-1]))
     ])

Result::

    {'last_name': 'Michaels',
     'spouse': 'Susan R.',
     'year': 2007,
     'oath': 'Under penalties of perjury, I ...',}

------
Usage
------

Data Models
===========

PDFQuery works by loading a PDF as a pdfminer layout, converting the layout to an etree with lxml.etree,
and then applying a pyquery wrapper. All three underlying libraries are exposed, so you can use any of their
interfaces to get at the data you want.

First pdfminer opens the document and reads its layout.
You can access the pdfminer document at ``pdf.doc``::

    >>> pdf = pdfquery.PDFQuery("tests/samples/IRS_1040A.pdf")
    >>> pdf.doc
    <pdfminer.pdfparser.PDFDocument object at 0xd95c90>
    >>> pdf.doc.catalog # fetch attribute of underlying pdfminer document
    {'JT': <PDFObjRef:14>, 'PageLabels': <PDFObjRef:10>, 'Type': /Catalog, 'Pages': <PDFObjRef:12>, 'Metadata': <PDFObjRef:13>}

Next the layout is turned into an lxml.etree with a pyquery wrapper. After you call ``pdf.load()`` (by far the most
expensive operation in the process), you can access the etree at ``pdf.tree``, and the pyquery wrapper at ``pdf.pq``::

    >>> pdf.load()
    >>> pdf.tree
    <lxml.etree._ElementTree object at 0x106a285f0>
    >>> pdf.tree.write("test2.xml", pretty_print=True, encoding="utf-8")
    >>> pdf.tree.xpath('//*/LTPage')
    [<Element LTPage at 0x994cb0>, <Element LTPage at 0x994a58>]
    >>> pdf.pq('LTPage[pageid=1] :contains("Your first name")')
    [<LTTextLineHorizontal>]

You'll save some time and memory if you call ``load()`` with only the page numbers you need. For example::

    >>> pdf.load(0, 2, 3, range(4,8))

*Performance Note:* The initial call to pdf.load() runs very slowly, because the underlying
pdfminer library has to compare every element on the page to every other element.
See the Caching section to avoid this on subsequent runs.

Under the hood, pdf.tree is basically an XML representation of the layout tree generated by pdfminer.pdfinterp. By
default the tree is processed to combine individual character nodes, remove extra spaces,
and sort the tree spatially. You can always get back to the original pdfminer Layout object from an element fetched
by xpath or pyquery::

    >>> pdf.pq(':contains("Your first name and initial")')[0].layout
    <LTTextLineHorizontal 143.651,714.694,213.083,721.661 u'Your  first  name  and  initial\n'>

Finding what you want
=========================

PDFs are internally messy, so it's usually not helpful to find things based on document structure or element classes
the way you would with HTML. Instead the most reliable selectors are the static labels on the page,
which you can find by searching for their text contents, and physical location on the page. PDF coordinates are given
in points (72 to the inch) starting from the bottom left corner. PDFMiner (and so PDFQuery) describes page locations
in terms of bounding boxes, or bboxes. A bbox consists of four coordinates: the X and Y of the lower left
corner, and the X and Y of the upper right corner.

If you're scraping text that's always in the same place on the page, the easiest way is to use Acrobat Pro's
Measurement Tool, Photoshop, or a similar tool to measure distances (in points) from the lower left corner of the
page, and use those distances to craft a selector like ``:in_bbox("x0,y0,x1,y1")`` (see below for more on ``in_bbox``).

If you're scraping text that might be in different parts of the page, the same basic technique applies,
but you'll first have to find an element with consistent text that appears a consistent distance from the text you
want, and then calculate the bbox relative to that element. See the Quick Start for an example of that approach.

If both of those fail, your best bet is to dump the xml using ``pdf.tree.write(filename, pretty_print=True)``,
and see if you can find any other structure, tags or elements that reliably identify the part you're looking for.
This is also helpful when you're trying to figure out why your selectors don't match ...

Custom Selectors
====================

The version of pyquery returned by pdf.pq supports some PDF-specific selectors to find elements by location on the
page.

* \:in_bbox("x0,y0,x1,y1"): Matches only elements that fit entirely within the given bbox.

* \:overlaps_bbox("x0,y0,x1,y1"): Matches any elements that overlap the given bbox.

If you need a selector that isn't supported, you can write a filtering function returning a boolean::

    >>> def big_elements():
        return float(this.get('width',0)) * float(this.get('height',0)) > 40000
    >>> pdf.pq('LTPage[page_index="1"] *').filter(big_elements)
    [<LTTextBoxHorizontal>, <LTRect>, <LTRect>]

(If you come up with any particularly useful filters, patch them into pdfquery.py as selectors and submit a pull
request ...)

Caching
====================

PDFQuery accepts an optional caching argument that will store the results of PDF parsing,
so subsequent runs on the same file will be much quicker. For example::

    from pdfquery.cache import FileCache
    pdfquery.PDFQuery("tests/samples/IRS_1040A.pdf", parse_tree_cacher=FileCache("/tmp/"))

Bulk Data Scraping
====================

Often you're going to want to grab a bunch of different data from a PDF, using the same repetitive process:
(1) find an element of the document using a pyquery selector or Xpath; (2) parse the resulting text; and (3) store it
in a dict to be used later.

The ``extract`` method simplifies that process. Given a list of keywords and selectors::

    >>> pdf.extract([
          ('last_name', ':in_bbox("315,680,395,700")'),
          ('year', ':contains("Form 1040A (")', lambda match: int(match.text()[-5:-1]))
     ])

the ``extract`` method returns a dictionary (by default) with a pyquery result set for each keyword,
optionally processed through the supplied formatting function. In this example the result is::

    {'last_name': [<LTTextLineHorizontal>], 'year': 2007}

(It's often helpful to start with ``('with_formatter', 'text')`` so you get results like "Michaels" instead of
``[<LTTextLineHorizontal>]``. See Special Keywords below for more.)

Search Target
~~~~~~~~~~~~~

By default, ``extract`` searches the entire tree (or the part of the document loaded earlier by ``load()``,
if it was limited to particular pages). If you want to limit the search to a part of the tree that you fetched with
``pdf.pq()`` earlier, pass that in as the second parameter after the list of searches.

Formatting Functions
~~~~~~~~~~~~~~~~~~~~

Notice that the 'year' example above contains an optional third paramater -- a formatting function. The formatting
function will be passed a pyquery match result, so ``lambda match: match.text()`` will return the text contents of the
matched elements.

Filtering Functions
~~~~~~~~~~~~~~~~~~~

Instead of a string, the selector can be a filtering function returning a boolean::

    >>> pdf.extract([('big', big_elements)])
    {'big': [<LTPage>, <LTTextBoxHorizontal>, <LTRect>, <LTRect>, <LTPage>, <LTTextBoxHorizontal>, <LTRect>]}

(See Custom Selectors above for how to define functions like ``big_elements``.)

Special Keywords
~~~~~~~~~~~~~~~~

``extract`` also looks for two special keywords in the list of searches that set defaults for the searches listed
afterward. Note that you can include the same special keyword more than once to change the setting, as demonstrated
in the Quick Start section. The keywords are\:

with_parent
+++++++++++

 The ``with_parent`` keyword limits the following searches to children of the parent search. For example::

    >>> pdf.extract([
         ('with_parent','LTPage[page_index="1"]'),
         ('last_name', ':in_bbox("315,680,395,700")') # only matches elements on page 1
     ])

with_formatter
++++++++++++++

The ``with_formatter`` keyword sets a default formatting function that will be called unless a specific one is supplied.
For example::

    ('with_formatter', lambda match: int(match.text()))

will attempt to convert all of the following search results to integers. If you supply a string instead of a function,
it will be interpreted as a method name to call on the pyquery search results. For example, the following two lines
are equivalent::

    ('with_formatter', lambda match: match.text())
    ('with_formatter', 'text')

If you want to stop filtering results, you can use::

    ('with_formatter', None)

----------------
Object Reference
----------------

Public Methods
================

::

    PDFQuery(   file,
                merge_tags=('LTChar', 'LTAnon'),
                round_floats=True,
                round_digits=3,
                input_text_formatter=None,
                normalize_spaces=True,
                resort=True,
                parse_tree_cacher=None,
                laparams={'all_texts':True, 'detect_vertical':True})

Initialization function. Usually you'll only need to pass in the file (file object or path). The rest of the arguments
control preprocessing of the element tree:

*   merge_tags: consecutive runs of these elements will be merged together, with the text of following elements
    appended to the first element. This is useful for keeping the size of the tree down,
    but it might help to turn it off if you want to select individual characters regardless of their containers.

*   round_floats and round_digits: if round_floats is True, numbers will be rounded to round_digits places. This is
    almost always good.

*   input_text_formatter: a function that takes a string and returns a modified string,
    to be applied to the text content of elements.

*   normalize_spaces: if True (and input_text_formatter isn't otherwise set), sets input_text_formatter to replace \s+
    with a single space.

*   resort: if True, elements will be sorted such that any element fully within the bounding box of another element
    becomes a child of that element, and elements on the same level are sorted top to bottom, left to right.

*   parse_tree_cacher: an object that knows how to save and load results of parsing a given page range from a given PDF.
    Pass in FileCache('/tmp/') to save caches to the filesystem.

*   laparams: parameters for the ``pdfminer.layout.LAParams`` object used to initialize
    ``pdfminer.converter.PDFPageAggregator``. Can be `dict`, `LAParams()`, or `None`.

::

    extract(    searches,
                tree=None,
                as_dict=True)

See "Bulk Data Scraping."

* searches: list of searches to run, each consisting of a keyword, selector, and optional formatting function.
* tree: pyquery tree to run searches against. By default, targets entire tree loaded by pdf.load()
* as_dict: if changed to False, will return a list instead of a dict to preserve the order of the results.

::

    load(*page_numbers)

Initialize the pdf.tree and pdf.pq objects. This will be called implicitly by pdf.extract(),
but it's more efficient to call it explicitly with just the page numbers you need. Page numbers can be any
combination of integers and lists, e.g. ``pdf.load(0,2,3,[4,5,6],range(10,15))``.

You can call ``pdf.load(None)`` if for some reason you want to initialize without loading *any* pages
(like you are only interested in the document info).

Public But Less Useful Methods
================================

These are mostly used internally, but might be helpful sometimes ...

::

    get_layout(page)

Given a page number (zero-indexed) or pdfminer PDFPage object, return the LTPage layout object for that page.

::

    get_layouts()

Return list of all layouts (equivalent to calling get_layout() for each page).

::

    get_page(page_number)

Given a page number, return the appropriate pdfminer PDFPage object.

::

    get_pyquery(tree=None, page_numbers=[])

Wrap a given lxml element tree in pyquery.
If no tree is supplied, will generate one from given page numbers, or all page numbers.

::

    get_tree(*page_numbers)

Generate an etree for the given page numbers. ``*page_numbers`` can be the same form as in ``load()``.


----------------------------------------
Documentation for Underlying Libraries
----------------------------------------

* PDFMiner (pdf.doc): pdfminer_homepage_, pdfminer_documentation_.

.. _pdfminer_homepage: http://www.unixuser.org/~euske/python/pdfminer/
.. _pdfminer_documentation: http://www.unixuser.org/~euske/python/pdfminer/programming.html

* LXML.etree (pdf.tree): lxml_homepage_, tutorial_.

.. _lxml_homepage: http://lxml.de/index.html
.. _tutorial: http://lxml.de/tutorial.html

* PyQuery (pdf.pq): pyquery_documentation_.

.. _pyquery_documentation: http://packages.python.org/pyquery/