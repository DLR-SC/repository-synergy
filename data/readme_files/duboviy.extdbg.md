<h1><img src="https://raw.githubusercontent.com/duboviy/extdbg/master/logo.png" height=85 alt="logo" title="logo"> extdbg</h1>

by [Eugene Duboviy](https://duboviy.github.io/)

[![Build Status](https://travis-ci.org/duboviy/extdbg.svg?branch=master)](https://travis-ci.org/duboviy/extdbg) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/b97c91e553724c369a3ec3b2d9ea50c6)](https://www.codacy.com/app/dubovoy/extdbg?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=duboviy/extdbg&amp;utm_campaign=Badge_Grade) [![PyPI](https://img.shields.io/pypi/v/extdbg.svg)](https://pypi.python.org/pypi/extdbg) [![Code Health](https://landscape.io/github/duboviy/extdbg/master/landscape.svg?style=flat)](https://landscape.io/github/duboviy/extdbg/master) [![Open Source Love](https://badges.frapsoft.com/os/mit/mit.svg?v=102)](https://github.com/duboviy/extdbg/) [![PRs & Issues Welcome](https://img.shields.io/badge/PRs%20&%20Issues-welcome-brightgreen.svg)](https://github.com/duboviy/extdbg/pulls) [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/duboviy/extdbg/)

Extended debugging python utilities



## Installation:

Install from PyPI:
```
pip install extdbg
```
Or using alternative command:
```
pip install https://github.com/duboviy/extdbg/archive/master.zip
```
Or from source use:
```
python setup.py install
```

## Supported python versions

  * 2.7
  * 3.3
  * 3.4
  * 3.5
  * PyPy

## PyPI

* [Package](https://pypi.python.org/pypi/extdbg)
* [Documentation](https://pythonhosted.org/extdbg/)

Contents
--------

```
from extdbg import ... (see variants in list below)
```

- `init_except_hook` - initialise extended traceback hook with local variables in exception message
- `add_watcher_attribute(name, watch_get=False)` - when called within some class (for example `add_watcher_attribute('name')`) - instances of that class will log every change to the attribute. Also tracks every access to attribute if `watch_get` is `True`.
- `where_is(object)` - return location of the object definition in code.
- `from_where_called()` - return location in code from where function which calls this is called
- `threaded` - allow you to decorate a function in your Python code, making it run in a separate thread
- `get_func_calls` - return all function calls from a python file
- `public and internal` - allow you to use additional context decorators (like public and private in other languages)
- `hackable_properties` - properties mock setter. Use this module to mock/stub any property of New Style Class
- `watch_for_output` - log location in code where some output is performed
- `bound_func` - bind any function/lambda as instance's method
- `save_object and load_object` - pickle/unpickle objects in/from files
- `enable_debug` - use on remote process to debug it using pycharm remote server run
 

... and many other features

Basic usage examples
--------

- `init_except_hook` - initialise extended traceback hook with local variables in exception message

```python
from extdbg import init_except_hook


init_except_hook()

def test(a, b):
    a / b

test(1, 0)
```

- `where_is(object)` - return location of the object definition in code

```python
from extdbg import where_is


location = where_is(where_is)

expected_filename = "navigate.py"
expected_line_no = 17

assert location.filename.endswith(expected_filename)
assert location.line_no == expected_line_no
```

- `from_where_called()` - return location in code from where function which calls this is called

```python
from extdbg import from_where_called


def f2():
    print(from_where_called())

def f1():
    f2()
    
f1()
```

- `threaded` - allow you to decorate a function in your Python code, making it run in a separate thread

```python
from extdbg import threaded


def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

print(fib(35))

@threaded(daemon=True)
def _fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

print(_fib(35))
```

- `get_func_calls` - return all function calls from a python file

```python
import ast

from extdbg import get_func_calls


filename = __file__
tree = ast.parse(open(__file__).read())
print(get_func_calls(tree))
```

- `public and internal` - allow you to use additional context decorators (like public and private in other languages). You can use decorator to wrap your code:

```python
from extdbg import public, internal


class A(object):

    @internal
    def m1(self):
        pass

    @public
    def m2(self):
        self.m1()

a = A()
a.m1()  # can't call API m1 is marked as internal!
a.m2()
```

- `hackable_properties` - properties mock setter. Use this module to mock/stub any property of New Style Class

```python
from extdbg import hackable_properties, ValueWrapper


class NewStyleCls(object):
    @property
    def prop_2_mock(self):
        raise RuntimeError("Unmocked property!")


@hackable_properties
class NewStyleClsMocked(NewStyleCls):
    def __init__(self, *args, **kwargs):
        super(NewStyleClsMocked, self).__init__(*args, **kwargs)
        self.prop_2_mock = ValueWrapper("MOCKING_PROP_VALUE")

mockable_cls = NewStyleClsMocked()
assert mockable_cls.prop_2_mock == "MOCKING_PROP_VALUE"
```

- `watch_for_output(condition=lambda x: True, stream='stdout')` - log location in code where some output is performed

```python
import unittest

from mock import Mock, patch


class TestWatchForOutput(unittest.TestCase):

    def test_works(self):
        from extdbg import watch_for_output

        mock_stdout = Mock()
        output = []

        def write(txt):
            output.append(txt)

        mock_stdout.write = write
        with patch('sys.stdout', mock_stdout):
            watch_for_output(lambda s: 'yes' in s)
            print('yes')

        self.assertIn('yes', output)
```

- `bound_func` - bind any function/lambda as instance's method

```python
import unittest
import inspect

from mock import Mock, patch


class TestBoundFunc(unittest.TestCase):

    def test_works(self):
        from extdbg import bound_func
        # Example of usage
        class Cls2Bound:
            pass

        instance2Bound = Cls2Bound()

        def func(*args, **kwargs):
            print(args, kwargs)

        l = lambda *args, **kwargs: None

        # bound method Cls2Bound.func
        bound_method1 = bound_func(func, instance2Bound, Cls2Bound)
        # bound method Cls2Bound.<lambda>
        bound_method2 = bound_func(l, instance2Bound, Cls2Bound)

        self.assertTrue(inspect.ismethod(bound_method1))
        self.assertTrue(inspect.ismethod(bound_method2))
```

- `enable_debug` - use on remote process to debug it using pycharm remote server run

```python
from extdbg import enable_debug


enable_debug("/home/<username>/pydev/debug-eggs/pycharm-debug.egg", 'localhost')
```

## License

**MIT** licensed library. See [LICENSE.txt](LICENSE.txt) for details.

## Contributing

If you have suggestions for improving the extdbg, please [open an issue or
pull request on GitHub](https://github.com/duboviy/extdbg/).

## Badges

[![forthebadge](http://forthebadge.com/images/badges/fuck-it-ship-it.svg)](https://github.com/duboviy/extdbg/)
[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](https://github.com/duboviy/extdbg/) [![forthebadge](http://forthebadge.com/images/badges/built-by-hipsters.svg)](https://github.com/duboviy/extdbg/) [![forthebadge](http://forthebadge.com/images/badges/built-with-swag.svg)](https://github.com/duboviy/extdbg/)

[![forthebadge](http://forthebadge.com/images/badges/powered-by-electricity.svg)](https://github.com/duboviy/extdbg/) [![forthebadge](http://forthebadge.com/images/badges/powered-by-oxygen.svg)](https://github.com/duboviy/extdbg/) [![forthebadge](http://forthebadge.com/images/badges/powered-by-water.svg)](https://github.com/duboviy/extdbg/) [![forthebadge](http://forthebadge.com/images/badges/powered-by-responsibility.svg)](https://github.com/duboviy/extdbg/)

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)

[![forthebadge](http://forthebadge.com/images/badges/makes-people-smile.svg)](https://github.com/duboviy/extdbg/)
