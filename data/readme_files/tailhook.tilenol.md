Tilenol
=======

Tilenol is a tiling manager. It's similar in look and feel to qtile, but
has much different implementation and configuration.

Features
--------

* Tiling WM, includes floating window support

* Written in pure python, simple small and extensible

* Configured with yaml files

* Includes hooks for python code if needed

* Supports multiple screens, with auto-update

* It's reparenting WM (so works with Java)

* Includes asynchronous main loop so no widgets can block entire WM

* Includes dmenu-like thing:

    * Starts instantly without skipping first few keystrokes

    * Some fuzzy matching is implemented, search not only with a prefix

* Has rich window classification rules to make windows floating and to put them
  into right places

* Tabs for window navigation (works for any layout)


Dependencies
------------

* python3
* python-greenlet
* xcb-proto (package containing `/usr/share/xcb/*.xml`)
* zorro (http://github.com/tailhook/zorro)
* pycairo from git (git://git.cairographics.org/git/pycairo)
* python-yaml

.. note::

    Tilenol includes pure-python implementation of xcb, so only xml files are
    needed


Running
-------

After installing python package. You may want to copy ``examples/*.yaml`` into
``/etc/xdg/tilenol`` or ``~/.config/tilenol`` before starting, as tilenol is
non-functional without a configuration.



