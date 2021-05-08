:authors: Antti Kaihola
:organization: Eniram Ltd
:copyright: 2013 Eniram Ltd. See the LICENSE file at the top-level
  directory of this distribution and at
  https://github.com/akaihola/lusmu/blob/master/LICENSE

Documentation_ | `Source code`_ | PyPI_ | Download_ | License_

Lusmu – a dataflow/reactive programming library for Python
==========================================================

Lusmu is a Python library for `reactive programming`_ (a form of
`dataflow programming`_).  Operations on data are done using a
`directed graph`_ which consists of input nodes and calculation nodes.

Lusmu uses the `invalidate/lazy-revalidate`_ evaluation model: reading
the value of a node triggers its calculation action and reads the
values of its inputs.  Thus, only required calculations are executed.

A minimal example
-----------------

::

    from lusmu.core import Input, Node, update_inputs

    root = Input()
    square = Node(action=lambda x: x ** 2,
                  inputs=Node.inputs(root))

    update_inputs([(root, 5)])
    print square.value

The output::

    25

See mouse.py_ and triangle.py_ for more comples examples.

.. _Documentation: http://lusmu.readthedocs.org/
.. _`Source code`: https://github.com/akaihola/lusmu
.. _PyPI: https://pypi.python.org/pypi/lusmu
.. _Download: https://pypi.python.org/packages/source/l/lusmu/
.. _License: https://github.com/akaihola/lusmu/blob/master/LICENSE
.. _`reactive programming`: https://en.wikipedia.org/wiki/Reactive_programming
.. _`dataflow programming`: https://en.wikipedia.org/wiki/Dataflow_programming
.. _`directed graph`: https://en.wikipedia.org/wiki/Directed_graph
.. _`invalidate/lazy-revalidate`: https://en.wikipedia.org/wiki/Reactive_programming#Evaluation_models_of_reactive_programming
.. _`mouse.py`: https://github.com/akaihola/lusmu/blob/master/lusmu/examples/mouse.py
.. _`triangle.py`: https://github.com/akaihola/lusmu/blob/master/lusmu/examples/triangle.py
