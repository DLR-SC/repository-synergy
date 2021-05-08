Flask-Failsafe
==============

A failsafe for the Flask reloader.

.. image:: https://travis-ci.org/mgood/flask-failsafe.png
   :target: https://travis-ci.org/mgood/flask-failsafe

The Flask reloader works great until you make a syntax error and it fails
importing your app. This extension helps keep you working smoothly by catching
errors during the initialization of your app, and provides a failsafe fallback
app to display those startup errors instead.

To use it, run your app via a small script script with a factory function to
initialize your app::

  from flask_failsafe import failsafe

  @failsafe
  def create_app():
      # note that the import is *inside* this function so that we can catch
      # errors that happen at import time
      from myapp import app
      return app

  if __name__ == "__main__":
      create_app().run()


The ``@failsafe`` decorator catches any errors calling ``create_app()`` and
returns a fallback app that will instead display the Flask error debugger.

If you use `Flask-Script <http://flask-script.readthedocs.org>`_, you can pass
the same ``@failsafe``-decorated factory function to the ``Manager()`` class::

  from flask.ext.script import Manager, Server
  from flask_failsafe import failsafe

  @failsafe
  def create_app():
      from myapp import app
      return app

  manager = Manager(create_app)
  manager.add_command("runserver", Server())

  if __name__ == "__main__":
      manager.run()
