Line Profile Panel for Flask Debug Toolbar
==========================================

.. image:: http://i.imgur.com/d5KaP.png

This is a panel for `flask_debugtoolbar`_ which enables the ability to view 
line profiling information from selected functions.

The line profile information comes from the `line_profiler`_ module, but you 
don't need to worry about that.

Installation
------------

First, you need to get the package. Install it with pip:

::

    pip install flask-debugtoolbar-lineprofilerpanel

Somewhere after you've set ``app.debug = True`` and before ``app.run``, you need
to specify the ``flask_debugtoolbar`` panels that you want to use and include
``'flask_debugtoolbar_lineprofilerpanel.panels.LineProfilerPanel'`` in that
list.

For example, here's a small flask app with the panel installed and with line 
profiling enabled for the `hello_world`:

::

    from flask import Flask
    app = Flask(__name__)

    import flask_debugtoolbar

    from flask_debugtoolbar_lineprofilerpanel.profile import line_profile

    @app.route('/')
    @line_profile
    def hello_world():
        return flask.render_template('hello_world.html')

    if __name__ == '__main__':
        app.debug = True

        # Specify the debug panels you want
        app.config['DEBUG_TB_PANELS'] = [
            'flask_debugtoolbar.panels.versions.VersionDebugPanel',
            'flask_debugtoolbar.panels.timer.TimerDebugPanel',
            'flask_debugtoolbar.panels.headers.HeaderDebugPanel',
            'flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel',
            'flask_debugtoolbar.panels.template.TemplateDebugPanel',
            'flask_debugtoolbar.panels.sqlalchemy.SQLAlchemyDebugPanel',
            'flask_debugtoolbar.panels.logger.LoggingPanel',
            'flask_debugtoolbar.panels.profiler.ProfilerDebugPanel',
            # Add the line profiling
            'flask_debugtoolbar_lineprofilerpanel.panels.LineProfilerPanel'
        ]
        toolbar = flask_debugtoolbar.DebugToolbarExtension(app)

        app.run()


Usage
-----

Unlike the regular profile panel that comes with ``flask_debugtoolbar``, the
line profiler will only profile functions you specifically tell it to. You can
either use it as a decorator or directly as a function.

::

    from flask_debugtoolbar_lineprofilerpanel.profile import line_profile

    # Using it as a decorator
    @app.route('/profile')
    @line_profile
    def profile_page():
        ...
        return flask.render_template('profile_page')

    # Explicit argument
    line_profile(some_function)

Note that if I had done ``line_profile(profile_page)`` in the example above, it
would've profiled the wrapper created by ``app.route``. In general, you probably
just want to use ``line_profile`` as a decorator.

Also note that the following will profile the decorator wrapper, not the inner
function.

::

    # Using it incorrectly as a decorator
    @line_profile
    @app.route('/profile')
    def profile_page():
        ...
        return flask.render_template('profile_page')

Always use ``@line_profile`` as the inner-most decorator.

.. _`flask_debugtoolbar`: https://github.com/mgood/flask-debugtoolbar
.. _`line_profiler`: https://github.com/certik/line_profiler


Using line_profiler with the Google AppEngine SDK
-------------------------------------------------

``line_profiler`` is implemented as a C extension.  Unfortunately, AppEngine does not support C extensions in the cloud, and ``dev_appserver`` simulates this restriction on your local machine.  If you'd like to use ``line_profiler`` on your local machine, you can monkey-patch the AppEngine SDK to permit it.  The Flask-DebugToolbar will make sure this plugin is disabled in production (it will catch any ImportErrors and disable the affected panel).

Simply open ``application/__init__.py``, which should look something like this::
    
    from __future__ import absolute_import

    from flask import Flask

    app = Flask('application')
    app.config.from_object('application.settings')

    if app.config['DEBUG']:
        from werkzeug.debug import DebuggedApplication
    
        app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)


        from flask.ext.debugtoolbar import DebugToolbarExtension
    
        toolbar = DebugToolbarExtension(app)


    import application.urls


and insert the monkey-patch, like so:


::

    from __future__ import absolute_import

    from flask import Flask

    app = Flask('application')
    app.config.from_object('application.settings')

    if app.config['DEBUG']:
        from werkzeug.debug import DebuggedApplication
    
        app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)


        # We can't use LineProfiler in production because it requires a C-extension,
        # but we can monkey-patch it in here for use on the dev server:
        try:
            import os, sys, re

            if 'SERVER_SOFTWARE' in os.environ and os.environ['SERVER_SOFTWARE'].startswith('Dev'):
                # white-list the line_profiler C extension
                sys.meta_path[3]._enabled_regexes.append(re.compile(r'.*line_profiler.*'))

                from flask_debugtoolbar_lineprofilerpanel.profile import line_profile


                ## import the methods you want to profile here, and whitelist them with line_profile:
                #from application.views import YourViewClass
                #
                #line_profile(YourViewClass.the_method_you_want_to_profile)
                #line_profile(YourViewClass.another_method_you_want_to_profile)
        except:
            pass
    

        # Make sure the monkey-patch is applied before you instantiate the DebugToolbarExtension.
        from flask.ext.debugtoolbar import DebugToolbarExtension
    
        toolbar = DebugToolbarExtension(app)


    import application.urls
