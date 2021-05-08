Flask Debug API
===============

Flask-Debug-API is an API Browser for Flask-DebugToolbar.

Injects a form to POST, PUT, PATCH or DELETE to API endpoints and allows debugging SQLAlchemy queries, Werkzeug stack traces, and everything else that Flask-DebugToolbar supports.

.. image:: http://simplectic.com/static/resources/flask-debug-api/flask-debug-todo.gif

Installation
------------

Install with pip

.. code-block:: sh

    $ pip install Flask-Debug-API


Usage
-----

.. code-block:: python

    # Create your app and enable debugging
    from flask_todomvc.factory import create_app
    from flask_debugtoolbar import DebugToolbarExtension
    from flask_debug_api import DebugAPIExtension

    app = create_app()
    app.debug = True

    # Register Flask-DebugToolbar and Flask-Debug-API
    DebugToolbarExtension(app)
    DebugAPIExtension(app)

    # Append Browse API Panel to Flask-DebugToolbar defaults
    # (or add explicitly)
    config = app.config
    panels = list(config['DEBUG_TB_PANELS'])
    panels.append('flask_debug_api.BrowseAPIPanel')
    config['DEBUG_TB_PANELS'] = panels

    # Optional: Change API prefix to custom prefix
    # to filter routes in Browse API Panel
    # Can leave '' to browse all routes
    # (Default is /api)
    config['DEBUG_API_PREFIX'] = '/todos'

    app.run(port=8000)
