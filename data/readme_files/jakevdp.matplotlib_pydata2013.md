PyData 2013: Advanced Matplotlib
================================

Tutorial Material: https://github.com/jakevdp/matplotlib_pydata2013
------------------------------------------------------------------

*Instructor: Jake VanderPlas*

![Jake Vanderplas](https://api.twitter.com/1/users/profile_image/jakevdp?size=bigger)

- email: <jakevdp@cs.washington.edu>
- twitter: [@jakevdp](http://twitter.com/jakevdp)
- github: [jakevdp](http://github.com/jakevdp)

This repository contains notebooks and code snippets for the advanced
matplotlib tutorial at PyData 2013
(see the schedule [here](http://pydata.org/sv2013/schedule/))

This tutorial will focus on interactive aspects of matplotlib: how keyboard
callbacks, mouse callbacks, and widgets can be used to interact visually
with data.  Additionally, we'll look at using some of these ideas with
the new matplotlib animation package.

Towards the end, we'll take a look at some more complicated examples of
animations and interactive applications in matplotlib.
Several of the examples will be drawn from recent posts on my blog,
[Pythonic Perambulations](http://jakevdp.github.com).

Requirements
------------
This tutorial requires recent versions of numpy and scipy, as well as
matplotlib version 1.1+ (earlier versions will be sufficient for all but
the animation components).

Due to a bug in the current version of matplotlib, animation examples will
not function in the MacOSX matplotlib backend.  This is a known issue,
but is difficult to address
(see http://github.com/matplotlib/matplotlib/issues/531).

Notebook Static Views
---------------------

- [Introduction](http://nbviewer.ipython.org/urls/raw.github.com/jakevdp/matplotlib_pydata2013/master/notebooks/01_Introduction.ipynb)

- [Interactivity with Key Bindings](http://nbviewer.ipython.org/urls/raw.github.com/jakevdp/matplotlib_pydata2013/master/notebooks/02_Key_Bindings.ipynb)

- [Interactivity with Widgets](http://nbviewer.ipython.org/urls/raw.github.com/jakevdp/matplotlib_pydata2013/master/notebooks/03_Widgets.ipynb)

- [Example: Building a Color Picker](http://nbviewer.ipython.org/urls/raw.github.com/jakevdp/matplotlib_pydata2013/master/notebooks/04_Color_Picker.ipynb)

- [Animations in Matplotlib](http://nbviewer.ipython.org/urls/raw.github.com/jakevdp/matplotlib_pydata2013/master/notebooks/05_Animations.ipynb)

- [How Far Can You Go?  Extreme Matplotlib](http://nbviewer.ipython.org/urls/raw.github.com/jakevdp/matplotlib_pydata2013/master/notebooks/06_More_Examples.ipynb)