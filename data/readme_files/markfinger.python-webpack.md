Unmaintained
============

This project is unmaintained as it's a complicated solution to a simple problem.

You should try using either https://github.com/owais/django-webpack-loader or https://github.com/markfinger/python-webpack-manifest.


python-webpack
==============

[![Build Status](https://travis-ci.org/markfinger/python-webpack.svg?branch=master)](https://travis-ci.org/markfinger/python-webpack)

Python bindings to webpack, via [webpack-build](https://github.com/markfinger/webpack-build)


Documentation
-------------

- [Installation](#installation)
- [Basic usage](#basic-usage)
- [API](#api)
  - [webpack](#webpack)
  - [populate_manifest_file](#populate_manifest_file)
- [Config files](#config-files)
  - [Config functions](#config-functions)
  - [Configuring the build](#configuring-the-build)
  - [Passing data to the config layer](#passing-data-to-the-config-layer)
  - [Using relative paths to config files](#using-relative-paths-to-config-files)
  - [Output paths](#output-paths)
- [Build server](#build-server)
  - [Hot module replacement](#hot-module-replacement)
  - [Overriding the build server](#overriding-the-build-server)
- [Offline manifests](#offline-manifests)
  - [Generating manifests](#generating-manifests)
  - [Using context in a manifest](#using-context-in-a-manifest)
  - [Manifest keys](#manifest-keys)
  - [Overriding the manifest reader](#overriding-the-manifest-reader)
- [Settings](#settings)
- [Django integration](#django-integration)
- [Running the tests](#running-the-tests)


Installation
------------

```
pip install webpack
```

and install the JS dependencies with

```
npm install webpack webpack-build --save
```


Basic usage
-----------

python-webpack provides a high-level interface to a 
[webpack-build server](https://github.com/markfinger/webpack-build#build-server), enabling you to send 
build requests and receive an object describing the outcome.

To start the server, run 

```
node_modules/.bin/webpack-build -s
```

Build requests should provide a path to a config file

```python
from webpack.compiler import webpack

bundle = webpack('path/to/webpack.config.js')
```

The object returned can be passed directly into your template layer, enabling you to inject &lt;script&gt; 
and &lt;link&gt; elements into your page. The object provides two convenience methods, `render_js` and 
`render_css` which emit elements pointing to the generated assets.


API
---


### webpack

`webpack.compiler.webpack` allows you to request data from the build server and the manifest reader.

The function requires one argument: 

- `config_file` - a path to a config file

The following optional arguments are also accepted:

- `context` - a dictionary that provides context data that is passed to the config file. In most cases, the 
  `CONTEXT` setting should be used instead as it allows you to set global defaults.
- `settings` - a dictionary of keys which can be used to override settings. In most cases, you'll want to define 
  settings in `webpack.conf.settings`, but it can be useful to provide overrides without monkey-patching.
- `manifest` - an override for the default manifest reader. Should expose a `read` method.
- `compiler` - an override for the default compiler - a webpack-build build server. Should expose a `build` method.


### populate_manifest_file

`webpack.manifest.populate_manifest_file` generates a manifest file containing the contents of the `MANIFEST` 
setting, at the location specified by the `MANIFEST_PATH` setting.

If you want to override settings during the build process - for example to provide a different `STATIC_URL` setting - the `MANIFEST_SETTINGS` setting can be used.


Config files
------------

For webpack's config reference, refer to the [official docs](https://webpack.github.io/docs/configuration.html).


### Config functions

webpack-build uses config files which export a function that returns config objects. 

Using config functions provide a number of benefits:
  - functions can generate config objects which reflect the data sent from your python system
  - functions can generate multiple config objects, enabling your config files to act as templates
  - idempotent functions enable webpack-build to safely mutate the object without causing unintended side 
    effects for successive builds

If you are already using config files which export an object, wrap the generation of the object in a 
function. For example:

```javascript
// if you currently have
module.exports = {
  // ...
};

// rewrite it as
module.exports = function() {
  return {
    // ...
  };
};
```

To avoid unintended side-effects and inexplicable behaviour, ensure that your functions are both idempotent and
always return an entirely new object. Extending mutable objects is an easy recipe for unhappiness.


### Configuring the build

The data sent from python-webpack is available in your config function as the first argument, this enables
you to generate a config object which reflects the state of your python system. 

A typical use-case is injecting loaders that enable hot module replacement. For example, if you always want
to use the `babel-loader`, but you only want `react-hot-loader` when hot module replacement is available:

```javascript
module.exports = function(opts) {
  return {
    // ...
    module: {
      loaders: [
        {
          test: /\.jsx?$/,
      	  exclude: /(node_modules|bower_components)/,
      	  loader: (opts.hmr ? 'react-hot-loader!' : '') + 'babel-loader'
        }
      ]
    }
  };
};
```

The `opts` object provided to your functions is sent from python-webpack and follows 
[webpack-build's build options](https://github.com/markfinger/webpack-build#build-options).


### Passing data to the config layer

You can send extra data to your config function by specifying the `CONTEXT` setting. 

For example, if your `CONTEXT` setting looked like `{'COMPRESS': True}`, your function could use the 
`COMPRESS` flag to activate compression:

```javascript
var webpack = require('webpack');

module.exports = function(opts) {
  var config = {
    // ...
  };
  
  if (opts.context.COMPRESS) {
    config.plugins.push(
      new webpack.optimize.UglifyJsPlugin()
    );
  }
  
  return config;
};
```

The `CONTEXT` setting defines global defaults, but you can also specify per-build values by providing
the `context` argument to the `webpack` function.

Using context allows you to treat config functions as factories or templates, which can assist with 
reducing boilerplate and reusing config files across multiple contexts.


### Using relative paths to config files

If you want to use relative paths to config files, you should specify the `CONFIG_DIRS` setting. When
a relative path is provided, python-webpack looks sequentially through the directories until it finds 
a match.


### Output paths

Be aware that the `output.path` property on config objects is overridden automatically, you can leave
the setting undefined and webpack-build will redirect all output to your `OUTPUT_ROOT`.

To avoid file name collisions, builds are uniquely identified by hashing the options object sent to
webpack-build. By default, your assets are placed in a directory equivalent to 

```python
os.path.join(OUTPUT_ROOT, 'webpack_assets', options_hash)
```


Build server
------------

python-webpack relies on [webpack-build](https://github.com/markfinger/webpack-build) to expose a high-level 
API around webpack such that it can be easily integrated into an external system. webpack-build's 
[server](https://github.com/markfinger/webpack-build#build-server) is used to provide network access 
to the library's functionality.

A build server can be started with

```
node_modules/.bin/webpack-build -s
```

### Hot module replacement

If you set the `HMR` setting to True, assets that are rendered on the client-side will open sockets to the 
build server and listen for change notifications. When the assets have been rebuilt, they will attempt to
automatically update themselves within the browser. If they are unable to, they will log to the console 
indicating that you will need to refresh for the changes to be applied.

When `HMR` is True, webpack-build will automatically mutate config objects by: 
 - adding a HMR client to the generated bundle
 - adding a `HotModuleReplacementPlugin`
 - defining `output.publicPath`
 - defining `recordsPath`

If you want to change your config for situations where the python layer has requested HMR, use the `hmr` 
flag on the options argument provided to config functions.


### Overriding the build server

If you want to replace the build server with your own compiler, you can use the `compiler` argument on the
`webpack` function. Composing a wrapper around `webpack` is one solution, for example:

```python
from webpack.compiler import webpack

class MyCompiler:
    def build(config_file, *args, **kwargs):
        # ...
    
my_compiler = MyCompiler()
        
def my_webpack_function(*args, **kwargs):
    kwargs['compiler'] = my_compiler
    return webpack(*args, **kwargs)
```


Offline manifests
-----------------

Offline manifests are JSON files which allow python-webpack to cache the output from webpack-build. Manifests 
are useful as an optimisation for production environments where you do not want a build server running. 


### Generating manifests

The easiest way to generate manifests is to define the `MANIFEST` and `MANIFEST_PATH` settings.

The `MANIFEST` setting should an iterable containing config files. For example:

```python
(
    'path/to/some/webpack.config.js',
    'path/to/another/webpack.config.js',
)
```

The `MANIFEST_PATH` setting should be an absolute path to a file that the manifest will be written to and 
read from. For example:

```python
os.path.join(os.getcwd(), 'webpack.manifest.json')
```

To generate a manifest, call the `populate_manifest_file` function. For example:

```python
from webpack.manifest import populate_manifest_file

populate_manifest_file()
```

Once your manifest has been generated, the `USE_MANIFEST` setting is used to indicate that all data should
be served from the manifest file. When `USE_MANIFEST` is True, any requests which are not contained within
the manifest will cause errors to be raised.


### Using context in a manifest

If you want to generate a manifest which contains specific context for each config file, set `MANIFEST` to
a dictionary where the keys are config files and the values are iterables containing context objects. For 
example:

```python
{
    # Build this file with a context
    'path/to/some/webpack.config.js': (
        {'foo': True},
    ),
    # Build this file without context
    'path/to/another/webpack.config.js': (),
    # Build this file twice, with two different contexts
    'path/to/yet/another/webpack.config.js': (
        {'foo': True},
        {'bar': True},
    ),
}
```

Note: if you call `webpack` with the `USE_MANIFEST` setting activated, you **must** specify the exact same 
context as defined in the `MANIFEST` setting. 


### Manifest keys

Manifest keys are the paths to the config files. If you want to deploy your manifests to another environment,
you will likely need to use relative paths in coordination with the `CONFIG_DIRS` setting.

If have specified context for a config file, the keys are generated by appending a hash of the context to the 
path. Hence, you **must** specify the exact same context when calling `webpack`.


### Overriding the manifest reader

The manifest handler that ships with webpack depends heavily on path resolution and context hashes to map
requests to entries in the manifest. While this behaviour ensures an explicit and deterministic outcome, it 
can make it difficult to ensure portablity when deploying manifests to other locations or servers. 

If you want to use your own manifest reader, one solution is to compose a wrapper function around `webpack`
and override the `manifest` argument. For example:

```python
from webpack.compiler import webpack

class MyManifest():
    def read(config_file, context):
        """This method is called by the compiler and should return an object"""
        # ...
        
my_manifest = MyManifest()
        
def my_webpack_function(*args, **kwargs):
    kwargs['manifest'] = my_manifest
    return webpack(*args, **kwargs)
```


Settings
--------

Settings can be defined by calling `webpack.conf.settings.configure` with keyword arguments matching 
the setting that you want to define. For example:

```python
from webpack.conf import settings

DEBUG = True

settings.configure(
    OUTPUT_ROOT='/path/to/your/output_root',
    STATIC_URL='/static/',
    WATCH=DEBUG,
    HMR=DEBUG,
)
```

Note: in a Django project, you should declare the settings as keys in a dictionary named `WEBPACK` within 
your settings file. python-webpack introspects Django's settings during startup and will configure itself
from the `WEBPACK` dictionary.


### OUTPUT_ROOT

An absolute path to the root directory that you use for static assets. For example, 
`'/path/to/your/output_root'`.

This setting **must** be defined.

Default: `None`


### STATIC_URL

The root url that your static assets are served from. For example, `'/static/'`.

This setting **must** be defined.

Default: `None`


### BUILD_URL

The url that build requests are sent to, this url should expose webpack-build.

Default: `'http://127.0.0.1:9009/build'`


### CONFIG_DIRS

A list of directories that will be used to resolve relative paths to config files.

Default: `None`


### WATCH

A boolean flag which indicates that file watchers should be set to watch the assets's source
files. When a change is detected, the files which have changed are recompiled in the background
so that the assets are ready for the next request. Set this to `True` in development environments.

Default: `False`


### HMR

A boolean flag indicating that webpack-build should inject a hmr runtime into the generated assets.
Set this to `True` in development environments.

Default: `False`


### CONTEXT

The default context provided to config functions - you can use this to pass data and flags down to your 
config functions. If defined, the setting should be a dictionary.

Default: `None`


### CONFIG_DIRS

An iterable of directories that will be used to resolve relative paths to config files.

Default: `None`


### MANIFEST

An object containing config files which are used to populate an offline manifest. Can be either an iterable
of paths or a dictionary mapping paths to context objects.

Default: `None`


### USE_MANIFEST

A flag indicating that python-webpack should use the manifest file, rather than opening connections to a 
build server.

Default: `False`


### MANIFEST_PATH

An absolute path to the file used to store the manifest.

Default: `None`


### MANIFEST_SETTINGS

A dictionary of values that are used during manifest generation to override python-webpack's settings.

Default:
```python
{
	# Force the compiler to connect to the build server
	'USE_MANIFEST': False,
	# Ensure that the server does not add a hmr runtime
	'HMR': False,
}
```


### CACHE

A flag indicating that webpack-build should maintain a persistent file cache. The file cache is used to 
improve response times for builds that have already been completed.

Default: `True`


### CACHE_DIR

An override for the directory that webpack-build uses to store cache files.

Default: `None`


### OUTPUT_DIR

The directory in `OUTPUT_ROOT` which webpack will output all assets to.

Default: `'webpack_assets'`


### AGGREGATE_TIMEOUT

The delay between the detection of a change in your source files and the start of a compiler's
rebuild process.

Default: `200`


### POLL

If defined, this is a flag which indicates that watching compilers should poll for file changes, rather
than relying on the OS for notifications.

If the compiler is not detecting changes to your files, setting this to `True` may resolve the problem.

Default: `None`


Django integration
------------------

### Installation and configuration

The following configuration should be placed in your settings files to enable python-webpack to function 
with Django.

Add `'webpack'` to your `INSTALLED_APPS`

```python
INSTALLED_APPS = (
    # ...
    'webpack',
)
```

Add `'webpack.django_integration.WebpackFinder'` to your `STATICFILES_FINDERS`

```python
STATICFILES_FINDERS = (
    # ...
    'webpack.django_integration.WebpackFinder',
)
```

Configure webpack to respect your project's configuration

```python
WEBPACK = {
    'OUTPUT_ROOT': '/path/to/your/output_root',
    'STATIC_URL': STATIC_URL,
    'WATCH': DEBUG,
    'HMR': DEBUG,
}
```


### Template tags

A template tag is provided to integrate webpack at the template layer.

```html
{% load webpack %}

{% webpack 'path/to/webpack.config.js' as bundle %}

{{ bundle.render_css|safe }}

{{ bundle.render_js|safe }}
```


Running the tests
-----------------

```bash
pip install -r requirements.txt
npm install
python runtests.py
```
