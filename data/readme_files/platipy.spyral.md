======
Spyral
======

Spyral is a library/engine for developing 2D games in Python 2.X, with a focus on rapid development and clean design. Any system that runs Pygame should be able to run Spyral. Instead of ``import pygame``, you'll just use ``import spyral`` instead.

Spyral was specifically designed for developing `XO laptop <http://laptop.org/en/laptop/>`_ games. Spyral's main source of documentation can be found at the Platipy project, which documents Spyral in the context of a university course for which it was developed. `Visit the Platipy Project <http://platipy.org>`_

What does Spyral offer?
-----------------------

* **Scenes and Sprites** : Scenes are stack-based containers for Sprites that make it easy to structure your game between different screens and levels.
* **Views** : Easily manipulate visual properties of collections of Sprites at the same time.
* **Rects and Vec2Ds** : Convenient container classes for managing two-tuples (think points) and four-tuples (think rectangles).
* **Improved support for Images** : No more fussing with Surfaces, just create Images (with a fluent interface!) and assign them.
* **Animations** : Animate properties of Sprites like the position, the image, visibility, or anything you need!
* **Event handling** : A sophisticated event delegator let's you register symbolic event names with functions, greatly enhancing the clarity of your code.
* **Forms and Widgets** : Need a button? Text input? Sophisticated tabbing? All our batteries are included!
* **Concurrency (Actors)** : Simple but incredibly powerful parallelism with a single MixIn - give each object it's own ``main`` function!
* **Styling** : Separate out content from your code with Styling.
* **Pythonic interface** : We tried to make things fun and easy for you, the developer.
* Plus other goodies like **Collision Handling**, **Layering**, **Game Clocks**, and more!

Pre-requisites
--------------

* `Pygame <http://www.pygame.org/download.shtml>`_
* `Parsley <https://pypi.python.org/pypi/Parsley>`_
* `Greenlets <https://pypi.python.org/pypi/greenlet>`_ (optional, if you want to use the powerful Actors feature for multi-processing)

Examples
--------

* `skel.py <https://github.com/platipy/spyral/blob/master/examples/skel.py>`_ : A simple starting point for a new Spyral-based program, with a custom Scene. If you're not developing for the XO, this is a good starting point.
* `events.py <https://github.com/platipy/spyral/blob/master/examples/events.py>`_ : Demonstration of registering keyboard and mouse events.
* `fonts.py <https://github.com/platipy/spyral/blob/master/examples/fonts.py>`_ : Demonstration of a couple properties of fonts, and how to get text on the screen.
* `forms.py <https://github.com/platipy/spyral/blob/master/examples/forms.py>`_ : Demonstration of the Forms feature, including buttons and text inputs.
* `style.py <https://github.com/platipy/spyral/blob/master/examples/style.py>`_ : Demonstration of using Style files to separate code from content.
* `concurrent.py <https://github.com/platipy/spyral/blob/master/examples/concurrent.py>`_ : Demonstration of the excellent Actors mixin, which allows quick and easy concurrency (requires greenlets). Press any key to step through it.
* `cursors.py <https://github.com/platipy/spyral/blob/master/examples/cursors.py>`_ : Demosntration of the cursors presently supported in Spyral through Pygame. Press the left mouse button to step through them.
* `collisions.py <https://github.com/platipy/spyral/blob/master/examples/collisions.py>`_ : Demonstration of two objects bouncing off each other.
* `animations.py <https://github.com/platipy/spyral/blob/master/examples/animations.py>`_ : Demonstration of the various kinds of Animations supported by Spyral. Use ``Space`` to walk through the steps.
* `view.py <https://github.com/platipy/spyral/blob/master/examples/view.py>`_ : Demonstration of the functionality of Views, which allow Sprites to be manipulated in groups. Use ``Space`` to walk through the steps.
* `minimal.py <https://github.com/platipy/spyral/blob/master/examples/minimal.py>`_ : The simplest possible Spyral program with no custom functionality. Not recommended, simply here to show off the simplicity.
* `artifical_events.py <https://github.com/platipy/spyral/blob/master/examples/artificial_events.py>`_ : An example showing off how to mock events, or send out your own custom ones.

Known Bugs
----------

Check out the `tracked issues on github <https://github.com/platipy/spyral/issues?state=open>`_ or the `Open Issues <http://platipy.readthedocs.org/en/latest/openproblems.html>`_ on Platipy for a listing of the things still needed.
