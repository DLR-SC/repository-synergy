vim-pyunit
==========

Installation
------------
1. Install the following packages from PyPI:

   - nose_: the unit test runner;
   - nose_machineout_:  The ``machineout`` plugin formats the ``nose`` output
     so that Vim can parse it more easily;
   - vim_bridge_:  This is required for the vim plugin scripts, to call
     directly into Python functions.

   To run the unit tests for this project, you also need ``mock``:

   - mock_:  Required to mock out the ``vim`` object in our test cases.

2. Clone the git repository::

       git clone git://github.com/nvie/vim-pyunit.git
       cd vim-pyunit

3. Copy the file ``ftplugin/python_pyunit.vim`` to your ``~/.vim/ftplugin``
   directory

.. _nose: http://pypi.python.org/pypi/nose
.. _nose_machineout: http://pypi.python.org/pypi/nose_machineout
.. _vim_bridge: http://pypi.python.org/pypi/vim_bridge
.. _mock: http://pypi.python.org/pypi/mock


Usage
-----
1. Open a Python file (or its corresponding unit test file named
   ``test_<filename>.py``)
2. Press ``<F8>`` to run ``nosetests`` on it

It shows the errors inside a quickfix window, which will allow your to
quickly jump to the error locations by simply pressing ``[Enter]``.


Source files vs. test files
---------------------------
``vim-pyunit`` assumes that you have a single test file for each Python
source file.  The settings ``PyUnitTestPrefix``, ``PyUnitSourceRoot``,
``PyUnitTestsRoot``, and ``PyUnitTestsStructure`` determine how the plugin
finds which test files belong to which source files.

The ``PyUnitTestsStructure`` setting is the most important one, because it
determines where the PyUnit plugin searches for source and test files.
There are three options:

* **flat**: Put all test files in a single test directory.  File names are
  composed by resembling the source's module structure, using underscores
  as separators.  For example, the test file for the source file
  ``foo/bar.py`` is called ``tests/test_foo_bar.py``.
* **side-by-side**: Put all the test files in the same directory as the
  source files.  Test files are prefixed with ``test_``.  For example, the
  test file for the source file ``foo/bar.py`` is called
  ``foo/test_bar.py``.  Use this setting when testing Django apps.
* **follow-hierarchy**: Put all the test files in a separate test
  directory (specified by ``PyUnitTestsRoot``), but keep the same
  directory hierarchy as used in the source directory.
  For example, the test file for the source file ``foo/bar.py`` is called
  ``tests/test_foo/test_bar.py``.
* **nose**: Put all the test files in a separate test
  directory (specified by ``PyUnitTestsRoot``), but keep the same
  directory hierarchy as used in the source directory.  As opposed to the
  ``follow-hierarchy`` layout, the intermediate directories are not
  prefixed with ``test_``, only the last (file part) component is.
  For example, the test file for the source file ``foo/bar.py`` is called
  ``tests/foo/test_bar.py``.


Keyboard mappings
-----------------
By default, the ``vim-pyunit`` plugin defines the following keyboard
mappings:

+----------+------------------------------------------------------------+
| Keymap   | Description                                                |
+==========+============================================================+
| F8       | Run ``nosetests`` for the current file. This mapping can   |
|          | be used on both the source file, and on its corresponding  |
|          | test file. Calls ``PyUnitRunTests()``                      |
+----------+------------------------------------------------------------+
| Shift+F8 | Run ``nosetests`` for all test files in the project, this  |
|          | is equivalent to running ``nosetests`` in the root of your |
|          | project. Calls ``PyUnitRunAllTests()``                     |
+----------+------------------------------------------------------------+
| F9       | Switch between the source and the corresponding test file. |
|          | If the source or test file is not yet open, it is opened.  |
|          | The setting ``tests_split_window`` is used to determine    |
|          | where the file needs to be opened screen-wise. Calls       |
|          | ``PyUnitSwitchToCounterpart()``                            |
+----------+------------------------------------------------------------+

The plugin autodetects whether you have remapped the functions to custom
keyboard mappings.  If so, if does not register the default mappings.  So
to pick your own shortcut key mappings, simply add lines like this to your
``.vimrc``::

    noremap ,t :call PyUnitRunTests()<CR>
    noremap! ,t <Esc>:call PyUnitRunTests()<CR>

(Which would map the test runner to comma-T. ``<F8>`` then remains what it
was.)

If you wish to disable any automatic keyboard mapping, simply set::

    let no_pyunit_maps = 1


Configuration
-------------
The plugin supports setting of the following variables:

+-------------------------------+------------------------------------------------+---------------------------+-----------------------------------+
| Variable                      | Description                                    | Values                    | Default                           |
+===============================+================================================+===========================+===================================+
| ``PyUnitShowTests``           | Shows the tests.                               | 0 or 1                    | 1                                 |
+-------------------------------+------------------------------------------------+---------------------------+-----------------------------------+
| ``PyUnitCmd``                 | The command to run the unit test.              | any string                | "nosetests -q --with-machineout"  |
+-------------------------------+------------------------------------------------+---------------------------+-----------------------------------+
| ``ProjRootIndicators``        | List of filenames indicating the project root. | list of file names        | [".git", "setup.py", "setup.cfg"] |
+-------------------------------+------------------------------------------------+---------------------------+-----------------------------------+
| ``ProjRootStopAtHomeDir``     | Stop the search for the project root at the    | 0 or 1                    | 1                                 |
|                               | user's home dir.                               |                           |                                   |
+-------------------------------+------------------------------------------------+---------------------------+-----------------------------------+
| ``PyUnitTestPrefix``          | The filename prefix to use for test files.     | any string                | "test\_"                          |
+-------------------------------+------------------------------------------------+---------------------------+-----------------------------------+
| ``PyUnitTestSuffix``          | *Not implemented yet*                          | 0 or 1                    | n/a                               |
+-------------------------------+------------------------------------------------+---------------------------+-----------------------------------+
| ``PyUnitSourceRoot``          | The relative location where all source files   | directory spec, or empty  | ""                                |
|                               | live.                                          |                           |                                   |
+-------------------------------+------------------------------------------------+---------------------------+-----------------------------------+
| ``PyUnitTestsRoot``           | The relative location where all tests live.    | directory spec            | "tests"                           |
+-------------------------------+------------------------------------------------+---------------------------+-----------------------------------+
| ``PyUnitTestsStructure``      | Specifies how you wish to organise your tests. | flat, follow-hierarchy,   | "follow-hierarchy"                |
|                               |                                                | side-by-side              |                                   |
+-------------------------------+------------------------------------------------+---------------------------+-----------------------------------+
| ``PyUnitTestsSplitWindow``    | Specifies where test files should be opened,   | left, right, top, bottom, | "right"                           |
|                               | when oopened next to the source file. When set | no                        |                                   |
|                               | to ``no``, doesn't open a new window at all,   |                           |                                   |
|                               | but reuses the current buffer.                 |                           |                                   |
+-------------------------------+------------------------------------------------+---------------------------+-----------------------------------+
| ``PyUnitConfirmTestCreation`` | Ask to confirm creation of new test files.     | 0 or 1                    | 1                                 |
+-------------------------------+------------------------------------------------+---------------------------+-----------------------------------+


Tips
----
This plugin goes well together with the following plugin:

- flake8_ (Python static syntax checker under ``<F7>``)

.. _flake8: http://github.com/nvie/vim-flake8
