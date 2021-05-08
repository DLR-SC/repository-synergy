===============
django-pagemore
===============

KISS approach to a "Load more" style AJAX paginator

Requirements
============

- Django 1.3+
- jQuery

Features
========

- Non-intrusive: your Django view is completely unaware of dynamic
  load-more stuff going on.
- There is literally no code (no Python, no Javascript) required to
  get a fully AJAX style "load more" going.
- KISS


Quickstart
==========

- Write your view as usual, handing over an (unpaginated) list of
  items to a template.
- Render the list of items in your template as follows::

    {% load pagemore %}
    {% more_paginator items per_page=10 ordered_by="-created_at" as paginator %}
    
    {% for item in paginator.objects %}
    {% if forloop.first %}
    <div class="pagemore-container">
    {% endif %}
    {{item}}
    {% if forloop.last %}
    </div>
    {% if paginator.has_more %}
    <a class="pagemore-paginator" href="?{{paginator.next_query}}">More items...</a>
    {% endif %}
    {% endif %}
    {% endfor %}

    <script type="text/javascript" src="{{STATIC_URL}}pagemore/js/pagemore.js"></script>
    <script type="text/javascript">
        $(function() { $(".pagemore-paginator").pagemore(); });
    </script>

- That's all!

Pagination Strategies
=====================

When a user is paginating through a list of items, while at the same
time new items are being inserted, offset based slicing would result
in duplicate items being shown.  A way to circumvent this is to make
sure that the items are properly ordered and to filter on items after
a certain point. Both strategies are supported. 


Paginate by Slicing
-------------------

Usage::

    {% more_paginator ... strategy="slice" ... %}

Characteristics:

- Supports both querysets and lists

- Does not order the objects unless explicitly told to (`ordered_by`).

Paginate by Filtering
---------------------

Usage::

    {% more_paginator ... strategy="filter" ... %}

Characteristics:

- Only supports querysets

- Enforces an ordering of the objects passed (default on `id`, overridable 
  by `ordered_by`).
