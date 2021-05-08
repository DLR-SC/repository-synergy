=============
templatemaker
=============

Given a list of text files in a similar format, templatemaker creates a
template that can extract data from files in that same format.

The underlying longest-common-substring algorithm is implemented in C
for performance.

Installation
============

Because part of templatemaker is implemented in C, you'll need to compile the
C portion of it. Fortunately, Python makes this easy.

To install systemwide:

    sudo python setup.py install

To play around with it without having to install systemwide:

    python setup.py build
    cp build/lib*/_templatemaker.so .
    rm -rf build

Overview
========

The templatemaker.py module provides a class, Template, that is capable of two
things:

    * Given an arbitrary number of strings (called "Sample Strings"), it
      determines the "least-common denominator" template -- that is, a string
      representing all the common substrings, with placeholders ("holes") for
      areas in the Sample Strings that differ.

      For example, these three Sample Strings...
      
        '<b>this and that</b>'
        '<b>alex and sue</b>'
        '<b>fine and dandy</b>'

      ...would produce the following template, where "!" represents a "hole."

        '<b>! and !</b>'

    * Once you have a template, you can give it data that is formatted
      according to that template, and it will "extract" a tuple of the "hole"
      values for that particular string.
      
      Following the above example, giving the template the following data:
      
        '<b>larry and curly</b>'

      ...would produce the following tuple:
      
        ('larry', 'curly')

      You can interpret this as "Hole 0's value is 'larry', and hole 1's value
      is 'curly'."

Basic Python API
================

Here's how to express the above example in Python code:

    # Import the Template class.
    >>> from templatemaker import Template

    # Create a Template instance.
    >>> t = Template()

    # Learn a Sample String.
    >>> t.learn('<b>this and that</b>')

    # Output the template so far, using the "!" character to mark holes.
    # We've only learned a single string, so the template has no holes.
    >>> t.as_text('!')
    '<b>this and that</b>'

    # Learn another string. The True return value means the template gained
    # at least one hole.
    >>> t.learn('<b>alex and sue</b>')
    True

    # Sure enough, the template now has some holes.
    >>> t.as_text('!')
    '<b>! and !</b>'

    # Learn another string. This time, the return value is False, which means
    # the template didn't gain any holes.
    >>> t.learn('<b>fine and dandy</b>')
    False

    # The template is the same as before.
    >>> t.as_text('!')
    '<b>! and !</b>'

    # Now that we have a template, let's extract some data.
    >>> t.extract('<b>red and green</b>')
    ('red', 'green')
    >>> t.extract('<b>django and stephane</b>')
    ('django', 'stephane')

    # The extract() method is very literal. It doesn't magically trim
    # whitespace, nor does it have any knowledge of markup languages such as
    # HTML.
    >>> t.extract('<b>  spacy  and <u>underlined</u></b>')
    ('  spacy ', '<u>underlined</u>')

    # The extract() method will raise the NoMatch exception if the data
    # doesn't match the template. In this example, the data doesn't have the
    # leading and trailing "<b>" tags.
    >>> t.extract('this and that')
    Traceback (most recent call last):
    ...
    NoMatch

    # Use the extract_dict() method to get a dictionary instead of a tuple.
    # extract_dict() requires that you specify a tuple of field names.
    >>> t.extract_dict('<b>red and green</b>', ('value1', 'value2'))
    {'value1': 'red', 'value2': 'green'}

    # You can specify None as one or more of the field-name values in
    # extract_dict(). Any field whose value is None will *not* be included
    # in the resulting dictionary.
    >>> t.extract_dict('<b>red and green</b>', ('value1', None))
    {'value1': 'red'}
    >>> t.extract_dict('<b>red and green</b>', (None, 'value2'))
    {'value2': 'green'}

The as_text() method
====================

The as_text() method displays the template as a string, with holes represented
by a string of your choosing.

    >>> t = Template()
    >>> t.learn('123 and 456')
    >>> t.learn('456 and 789')
    True

    Get the template with "!" as the hole-representing string.
    >>> t.as_text('!')
    '! and !'

    Get the template with "{{ var }}" as the hole-representing string.
    >>> t.as_text('{{ var }}')
    '{{ var }} and {{ var }}'

Note that as_text() does *not* perform any escaping if your template contains
the hole-representing string:

    >>> t = Template()
    >>> t.learn('Yes!')
    >>> t.learn('No!')
    True

    Here, we use "!" as the hole-representing string, and the template contains
    a literal "!" character. The literal character is not escaped, so there is
    no way to tell apart the literal template character from the
    hole-representing string.
    >>> t.as_text('!')
    '!!'

    Here, we use an underscore to demonstrate that the template contains a
    literal "!" character. This wasn't detectable in the previous statement.
    >>> t.as_text('_')
    '_!'

With this in mind, you should choose a string in as_text() that is highly
unlikely to appear in your template. But, in any case, you shouldn't rely on
the output of as_text() for use in programs; it's solely intended to be a
visual aid for humans to see their templates. (The template-maker code has its
own internal way of representing holes, and it's guaranteed to be unambiguous.
See "The marker character" below.)

Tolerance
=========

This template-making algorithm can often be "too literal" for one's liking.
For example, given these three Sample Strings...

    'my favorite color is blue'
    'my favorite color is violet'
    'my favorite color is purple'

The color is the only text that changes, so one would assume the template would
be the following:

    'my favorite color is !'

Let's see what actually happens:

    >>> t = Template()
    >>> t.learn('my favorite color is blue')
    >>> t.learn('my favorite color is violet')
    True
    >>> t.learn('my favorite color is purple')
    False
    >>> t.as_text('!')
    'my favorite color is !l!e!'

Aha, the template-maker was a bit too literal -- it noticed that the strings
"blue", "violet" and "purple" all contain *something*, then the letter "l",
then *something*, then the letter "e", then *something*. Technically, that's
correct, but for most applications, this approach misses the forest for the
trees.

There are two ways to solve this problem:

    * Teach a template many, many Sample Strings. The more diverse your input,
      the less likely this will happen.

    * Use a feature called *tolerance*.

The template-maker algorithm lets you specify a tolerance -- the minimum
allowed length of text between holes. This gives you control over avoiding the
problem.

To specify tolerance, just pass the ``tolerance`` argument to the Template
constructor. Here's the above example with a tolerance=1.

    >>> t = Template(tolerance=1)
    >>> t.learn('my favorite color is blue')
    >>> t.learn('my favorite color is violet')
    True
    >>> t.learn('my favorite color is purple')
    False
    >>> t.as_text('!')
    'my favorite color is !'

Aha! Now, that's more like it.

Setting tolerance is useful for small cases like this, but note that there is a
risk of throwing the baby out with the bathwater, depending on how high your
tolerance is set. If the tolerance is set too high, your output template might
be "watered down" -- less accurate than it possibly could be.

For example, say we have a list of HTML strings representing significant
events:

    <p>My birthday is <span style="color: blue;">Dec. 11, 1954</span>.</p>
    <p>My wife's birthday is <span style="color: red;">Jan. 3, 1957</span>.</p>
    <p>Our wedding fell on <span style="color: green;">Sep. 24, 1982</span>.</p>

Say we'd like to extract five pieces of data from each string: the event, the
HTML color, the month, the day and the year. Here's what we might do in Python:

    >>> t = Template(tolerance=5)
    >>> t.learn('<p>My birthday is <span style="color: blue;">Dec. 11, 1954</span>.</p>')
    >>> t.learn('<p>My wife\'s birthday is <span style="color: red;">Jan. 3, 1957</span>.</p>')
    True
    >>> t.learn('<p>Our wedding fell on <span style="color: green;">Sep. 24, 1982</span>.</p>')
    True
    >>> t.as_text('!')
    '! <span style="color: !</span>.</p>'

This resulting template is correct, but it's watered down.

This template is, indeed, watered down. You can tell by extracting some data:

    >>> t.extract('<p>My sister\'s birthday is <span style="color: pink;">Jul. 12, 1952</span>.</p>')
    ("<p>My sister's birthday is", 'pink;">Jul. 12, 1952')

This data is messy. Namely, the color of the <span> is in the same data field
as the event date. Assuming we're interested in getting as granular as
possible in our parsing, it would be better to set a lower tolerance.

    >>> t = Template(tolerance=1)
    >>> t.learn('<p>My birthday is <span style="color: blue;">Dec. 11, 1954</span>.</p>')
    >>> t.learn('<p>My wife\'s birthday is <span style="color: red;">Jan. 3, 1957</span>.</p>')
    True
    >>> t.learn('<p>Our wedding fell on <span style="color: green;">Sep. 24, 1982</span>.</p>')
    False
    >>> t.as_text('!')
    '<p>! <span style="color: !;">!. !, 19!</span>.</p>'
    >>> t.extract('<p>My sister\'s birthday is <span style="color: pink;">Jul. 12, 1952</span>.</p>')
    ("My sister's birthday is", 'pink', 'Jul', '12', '52')

Much better.

Using tolerance is all about tradeoffs. To use this feature most effectively,
you'll need to experiment and consider the nature of the data you're parsing.

Versions
========

A Template instance keeps tracks of how many Sample Strings it has learned.
You can access this via the ``version`` attribute.

    >>> t = Template()
    >>> t.version
    0
    >>> t.learn('My name is Paul.')
    >>> t.version
    1
    >>> t.learn('My name is Jonas.')
    True
    >>> t.version
    2

The marker character
====================

The template-maker algorithm, implemented in C, works by comparing two strings
one byte at a time. Each time you call learn(some_string) on a template object,
the underlying C algorithm compares some_string to the *current template*.

A template internally represents each hole with a *marker character* -- a
character that is guaranteed not to appear in either string. This is set to the
character "\x1f".

In order to guarantee that the marker character doesn't appear in a string, the
Template's learn() method removes any occurrence of the marker character from
the input string before running the comparison algorithm.

The advantage of this "dumb" approach is its simplicity: the C implementation
doesn't have to treat markers as a special case. As a result, the C code is
cleaner and faster. Also, it was easier to write. :)

However, there are two disadvantages:

    * First, a template effectively cannot contain the literal marker
      character.

      In practice, this is *highly* unlikely to be a problem, because the
      marker character is obscure.

    * Two, in the slight chance that a template contains a multi-byte character
      (e.g., Unicode) that contains the marker character as one of its bytes,
      the template-maker algorithm will split that Unicode character at that
      byte. This happens because the underlying C implementation compares
      single bytes -- it is *not* Unicode-aware.

      In practice, this is *highly* unlikely to be a problem. In order to get
      bitten by this, you'd need an aforementioned multi-byte character to
      appear in your template (not just in a Sample String, but in your
      template -- i.e., in *each* Sample String).

      If it turns out there are significant multi-byte characters that contain
      the marker character "\x1f", you can change the MARKER value at the top
      of templatemaker.c and recompile it. Or, suggest a better character to
      the authors.

Change log
==========

2007-09-20    0.1.1    Created HTMLTemplate
2007-07-06    0.1      Initial release
