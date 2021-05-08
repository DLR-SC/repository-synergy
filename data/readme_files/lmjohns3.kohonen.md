kohonen
=======

This module contains some basic implementations of Kohonen-style vector
quantizers: Self-Organizing Map (SOM), Neural Gas, and Growing Neural Gas.
Kohonen-style vector quantizers use some sort of explicitly specified topology
to encourage good separation among prototype "neurons".

Vector quantizers are useful for learning discrete representations of a
distribution over continuous space, based solely on samples drawn from the
distribution. This process is also generally known as density estimation.

The source distribution includes an interactive test module that uses PyGTK and
Cairo to render a set of quantizers that move around in real time as samples are
drawn from a known distribution and fed to the quantizers. Run this test with::

    python kohonen_test.py

Documentation (currently a bit sparse) lives at http://pythonhosted.org/kohonen.
Have fun!
