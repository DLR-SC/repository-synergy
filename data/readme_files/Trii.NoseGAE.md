NoseGAE: Nose for Google App Engine Testing
==================================================
[![PyPI](https://img.shields.io/pypi/v/NoseGAE.svg)](https://pypi.python.org/pypi/NoseGAE)
[![Downloads](https://img.shields.io/pypi/dm/NoseGAE.svg)](https://pypi.python.org/pypi/NoseGAE)
[![License](https://img.shields.io/pypi/l/NoseGAE.svg)](https://pypi.python.org/pypi/NoseGAE)
[![Build Status](https://travis-ci.org/Trii/NoseGAE.svg?branch=master)](https://travis-ci.org/Trii/NoseGAE)

## Installing

NoseGAE is available from the cheeseshop and can be installed easiest via `pip install nosegae`. While the library is actively maintained, no new features are being added at this time so development has stagnated. If you want to work on the library, or just like to clone and install you can use your choice of `python setup.py install` or `python setup.py develop` or even the `pip` equiv.

## Overview

NoseGAE is a [nose](http://nose.readthedocs.org/en/latest/index.html) plugin that makes it easier to
write functional and unit tests for [Google App Engine](https://cloud.google.com/appengine/) applications. 

1. [What does it do?](#what-does-it-do)
	1. [Functional tests](#functional-tests) 
	2. [Unit tests](#unit-tests) 
2. [Configuring the TestBed](#configuring-the-testbed)
	1. [Class Based Tests](#class-based-tests)
	2. [Function Tests](#function-tests)
	3. [Doctest](#doctest)
3. [Changes in 0.5.2](#changes-in-052)
4. [Changes in 0.4.0](#changes-in-040)


## What does it do?

NoseGAE sets up the GAE development environment before your test run. This means that you can easily
write functional tests for your application without having to actually start the dev server and test
over http. The plugin also configures and initializes a TestBed instance, your application_id based off
your `app.yaml`, and sets the proper paths using `dev_appserver.fix_sys_path()`.


### Functional tests

Consider the simple hello world application in `examples/helloworld`:


```python
import webapp2
from jinja2 import Environment


class Hello(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        env = Environment()
        template = env.from_string("Hello {{ greeting }}!")
        self.response.out.write(template.render(greeting='world'))

app = webapp2.WSGIApplication([('/', Hello)], debug=True)

```

And a simple functional test suite `examples/helloworld/test.py` for the application:

```python
from webtest import TestApp
import unittest
import helloworld

app = TestApp(helloworld.app)


class HelloWorldTest(unittest.TestCase):
    def test_index(self):
        """Tests that the index page for the application

        The page should be served as: Content-Type: text/plain
        The body content should contain the string: Hello world!
        """
        response = app.get('/')
        self.assertEqual(response.content_type, 'text/plain')
        self.assertIn('Hello world!', response.body)

```


Without NoseGAE, the test fails.

```
helloworld$ nosetests --logging-level=ERROR
E
======================================================================
ERROR: Failure: ImportError (No module named webapp2)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/Josh/Developer/Github/jj/lib/python2.7/site-packages/nose-1.3.4-py2.7.egg/nose/loader.py", line 414, in loadTestsFromName
    addr.filename, addr.module)
  File "/Users/Josh/Developer/Github/jj/lib/python2.7/site-packages/nose-1.3.4-py2.7.egg/nose/importer.py", line 47, in importFromPath
    return self.importFromDir(dir_path, fqname)
  File "/Users/Josh/Developer/Github/jj/lib/python2.7/site-packages/nose-1.3.4-py2.7.egg/nose/importer.py", line 94, in importFromDir
    mod = load_module(part_fqname, fh, filename, desc)
  File "/Users/Josh/Developer/Github/nosegae/examples/helloworld/test.py", line 2, in <module>
    import helloworld
  File "/Users/Josh/Developer/Github/nosegae/examples/helloworld/helloworld.py", line 1, in <module>
    import webapp2
ImportError: No module named webapp2

----------------------------------------------------------------------
Ran 1 test in 0.075s

FAILED (errors=1)
```

With NoseGAE, they pass.


```
helloworld$ nosetests --logging-level=ERROR --with-gae
.
----------------------------------------------------------------------
Ran 1 test in 0.264s

OK

```

### Unit tests

Functional tests are only one kind of test, of course. What if you
want to write unit tests for your data models? Normally, you can't use
your models at all outside of the dev environment, because the Google
App Engine datastore isn't available. However, since the NoseGAE
plugin sets up the development environment around your test run, you
can use models directly in your tests.

Consider the `examples/pets/models.py` file that includes some doctests:

```python
from google.appengine.ext import ndb

class Pet(ndb.Model):
    """The Pet class provides storage for pets.

    >>> # initialize testbed stubs
    >>> testbed.init_memcache_stub()
    >>> testbed.init_datastore_v3_stub()

    You can create a pet:
    >>> muffy = Pet(name=u'muffy', type=u'dog', breed=u"Shi'Tzu")
    >>> muffy # doctest: +ELLIPSIS
    Pet(name=u'muffy', type=u'dog', breed=u"Shi'Tzu", ...)
    >>> muffy_key = muffy.put()

    Once created, you can load a pet by its key:

    >>> muffy_key.get() # doctest: +ELLIPSIS
    Pet(name=u'muffy', type=u'dog', breed=u"Shi'Tzu", ...)

    Or by a query that selects the pet:

    >>> list(Pet.query(Pet.type == 'dog')) # doctest: +ELLIPSIS
    [Pet(name=u'muffy', ...)]

    To modify a pet, change one of its properties and ``put()`` it again.

    >>> muffy_2 = muffy
    >>> muffy_2.age = 10
    >>> muffy_key_2 = muffy_2.put()

    The pet's key doesn't change when it is updated.

    >>> bool(muffy_key == muffy_key_2)
    True
    """
    name = ndb.StringProperty(required=True)
    type = ndb.StringProperty(required=True, choices=("cat", "dog", "bird", "fish", "monkey"))
    breed = ndb.StringProperty()
    age = ndb.IntegerProperty()
    comments = ndb.TextProperty()
    created = ndb.DateTimeProperty(auto_now_add=True, required=True)

    def __repr__(self):
        return ("Pet(name=%r, type=%r, breed=%r, age=%r, "
                "comments=%r, created=%r)" %
                (self.name, self.type, self.breed, self.age,
                 self.comments, self.created))

```

Without NoseGAE, the doctests fail.

```
pets$ nosetests --with-doctest --logging-level=ERROR
F
======================================================================
FAIL: Doctest: models.Pet
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/doctest.py", line 2201, in runTest
    raise self.failureException(self.format_failure(new.getvalue()))
AssertionError: Failed doctest test for models.Pet
  File "/Users/Josh/Developer/Github/nosegae/examples/pets/models.py", line 4, in Pet

----------------------------------------------------------------------
File "/Users/Josh/Developer/Github/nosegae/examples/pets/models.py", line 15, in models.Pet
Failed example:
    muffy_key = muffy.put()
Exception raised:
    Traceback (most recent call last):
      File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/doctest.py", line 1289, in __run
        compileflags, 1) in test.globs
      File "<doctest models.Pet[2]>", line 1, in <module>
        muffy_key = muffy.put()
      File "/Applications/GoogleAppEngineLauncher.app/Contents/Resources/GoogleAppEngine-default.bundle/Contents/Resources/google_appengine/google/appengine/ext/ndb/model.py", line 3379, in _put
        return self._put_async(**ctx_options).get_result()
      File "/Applications/GoogleAppEngineLauncher.app/Contents/Resources/GoogleAppEngine-default.bundle/Contents/Resources/google_appengine/google/appengine/ext/ndb/tasklets.py", line 325, in get_result
        self.check_success()
      File "/Applications/GoogleAppEngineLauncher.app/Contents/Resources/GoogleAppEngine-default.bundle/Contents/Resources/google_appengine/google/appengine/ext/ndb/tasklets.py", line 368, in _help_tasklet_along
        value = gen.throw(exc.__class__, exc, tb)
      File "/Applications/GoogleAppEngineLauncher.app/Contents/Resources/GoogleAppEngine-default.bundle/Contents/Resources/google_appengine/google/appengine/ext/ndb/context.py", line 810, in put
        key = yield self._put_batcher.add(entity, options)
      File "/Applications/GoogleAppEngineLauncher.app/Contents/Resources/GoogleAppEngine-default.bundle/Contents/Resources/google_appengine/google/appengine/ext/ndb/tasklets.py", line 371, in _help_tasklet_along
        value = gen.send(val)
      File "/Applications/GoogleAppEngineLauncher.app/Contents/Resources/GoogleAppEngine-default.bundle/Contents/Resources/google_appengine/google/appengine/ext/ndb/context.py", line 343, in _put_tasklet
        keys = yield self._conn.async_put(options, datastore_entities)
      File "/Applications/GoogleAppEngineLauncher.app/Contents/Resources/GoogleAppEngine-default.bundle/Contents/Resources/google_appengine/google/appengine/datastore/datastore_rpc.py", line 1801, in async_put
        return make_put_call(base_req, pbs, extra_hook)
      File "/Applications/GoogleAppEngineLauncher.app/Contents/Resources/GoogleAppEngine-default.bundle/Contents/Resources/google_appengine/google/appengine/datastore/datastore_rpc.py", line 1784, in make_put_call
        service_name=self._api_version)
      File "/Applications/GoogleAppEngineLauncher.app/Contents/Resources/GoogleAppEngine-default.bundle/Contents/Resources/google_appengine/google/appengine/datastore/datastore_rpc.py", line 1310, in _make_rpc_call
        rpc = self._create_rpc(config, service_name)
      File "/Applications/GoogleAppEngineLauncher.app/Contents/Resources/GoogleAppEngine-default.bundle/Contents/Resources/google_appengine/google/appengine/datastore/datastore_rpc.py", line 1205, in _create_rpc
        rpc = apiproxy_stub_map.UserRPC(service_name, deadline, callback)
      File "/Applications/GoogleAppEngineLauncher.app/Contents/Resources/GoogleAppEngine-default.bundle/Contents/Resources/google_appengine/google/appengine/api/apiproxy_stub_map.py", line 414, in __init__
        self.__rpc = CreateRPC(service, stubmap)
      File "/Applications/GoogleAppEngineLauncher.app/Contents/Resources/GoogleAppEngine-default.bundle/Contents/Resources/google_appengine/google/appengine/api/apiproxy_stub_map.py", line 68, in CreateRPC
        assert stub, 'No api proxy found for service "%s"' % service
    AssertionError: No api proxy found for service "datastore_v3"
    
```
     
With NoseGAE, they pass.

```
pets$ nosetests --with-doctest --with-gae
.
----------------------------------------------------------------------
Ran 1 test in 0.228s

OK
```

## Configuring the TestBed

NoseGAE automatically configures your `TestBed` instance for you and then enables any stubs that you
may need for your tests to pass. There are two ways to enable and configure your stubs. The first and
most flexible way is to directly initialize the stub(s) on the `TestBed` instance injected into your
test case. The second, and simpler way, is to set the `nosegae_*` and optional `nosegae_*_kwargs`
attributes on your test case and let NoseGAE configure them for you. The following three sections describe
how to use the `TestBed` in your own tests. 

### Class Based Tests

The simplest of use cases is when your test class extends `unittest.TestCase`. The NoseGAE plugin injects an attribute
named `testbed` to the instance of your test class and configures it based upon any attributes matching the convention
`nosegae_<stubname>` and `nosegae_<stubname>_kwargs`.

This test uses the assigned `testbed` attribute to manually configure each test.

```python
class MyTest(unittest.TestCase):
    def test_using_memcache(self):
        """Unit test using memcache"""
        from google.appengine.api import memcache
        self.testbed.init_memcache_stub()
        memcache.set('test', True, 30)
        self.assertTrue(memcache.get('test'))
    
    def test_using_taskqueue(self):
        """Unit test using the taskqueue"""
        self.testbed.init_taskqueue_stub(root_path='/path/to/app')
        from google.appengine.api import taskqueue
        task_url = '/some/task'
        taskqueue.add(url=task_url)
        taskqueue_stub = self.testbed.get_stub('taskqueue')
        tasks = taskqueue_stub.get_filtered_tasks(url=task_url)
        self.assertEqual(1, len(tasks))
        self.assertEqual(task_url, tasks[0].url)
```

The following test case shows how to write a test that uses the datastore stub based on the simple configuration
method using `nosegae_<stubname>` and `nosegae_<stubname>_kwargs`.

```python
class DataTest(unittest.TestCase):
    # enable the datastore stub
    nosegae_datastore_v3 = True
    
    def test_get_entity(self):
        """Naively tests that we can fetch an entity from the datastore"""
        entity = MyModel.query().get()
        self.assertIsNotNone(entity)
    
```

### Function Tests

This test case uses the `testbed` instance assigned to the function to manually configure any needed stubs.
See `examples/function_manual_config`.

```python
def test_index():
    # test_index.testbed is assigned by the NoseGAE plugin
    test_index.testbed.init_taskqueue_stub(task_retry_seconds=42, root_path=os.path.dirname(__file__))
    # Assume the `/` route fires off a task queue and should pass without exceptions
    app = TestApp(helloworld.app)
    response = app.get('/')
    assert 'Hello world!' in str(response)
```

The following test shows how to use the simple method while passing kwargs to the taskqueue
stub's initialization method. See `examples/issue42_task-queue` for full example code.
 
```python
def test_index():
    # Assume the `/` route fires off a task queue and should pass without exceptions
    app = TestApp(app)
    response = app.get('/')
    assert 'Hello world!' in str(response)

# Enable any stubs needed as attributes off of the test function

# NoseGAE looks for queue.yaml in the root of the
# application when nosegae_taskqueue is True
test_index.nosegae_taskqueue = True

# ...or you can manually set the path and any additional arguments with the kwargs attribute
test_index.nosegae_taskqueue_kwargs = dict(task_retry_seconds=42, root_path=os.path.dirname(__file__))
```

### Doctest

Doctests are a whole other beast. They still work but all `TestBed` configuration has to be done manually.
NoseGAE uses the [nose doctest plugin](http://nose.readthedocs.org/en/latest/plugins/doctests.html) to inject
a global variable named `testbed` into your doctest scope that contains the current active `TestBed` instance.
See `examples/pets/models.py` for full example.

```python
class Pet(ndb.Model):
    """The Pet class provides storage for pets.

    >>> # Initialize stubs using the injected testbed instance
    >>> testbed.init_memcache_stub()
    >>> testbed.init_datastore_v3_stub()

    You can create a pet:
    >>> muffy = Pet(name=u'muffy', type=u'dog', breed=u"Shi'Tzu")
    >>> muffy_key = muffy.put()
    """
    name = ndb.StringProperty(required=True)
    type = ndb.StringProperty(required=True, choices=("cat", "dog", "bird", "fish", "monkey"))
    breed = ndb.StringProperty()
```
## Changes in 0.5.2

The 0.5.2 release introduces preliminary modules support by allowing multiple yaml or paths sent to the
`--gae-application` command line option.

```sh
nosetests --with-gae \
          --gae-application='app.yaml,mobile_frontend.yaml,static_backend.yaml,dispatch.yaml'
```

## Changes in 0.4.0

The 0.4.0 release is a major rewrite to support `dev_appserver2`. This release introduced two important changes listed
below.

### Sandbox is gone

Due to changes in the sandboxing mechanisms in dev_appserver2, it isn't possible for NoseGAE to simulate the deployed
environment any longer. The sandboxing feature had to be removed since there is no longer any way to toggle it between
`nose`s own internal workings.

This means that certain tests may pass locally but the code in question will fail in production due to restricted
modules and functions. As of now there is no workaround but pull requests are welcome!

### Testbed is set up for you

The new plugin automatically sets up the initial `google.appengine.ext.testbed.Testbed` instance and injects it into
your test cases for you.
