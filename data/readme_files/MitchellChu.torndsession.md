Torndsession Session
====================


`Torndsession <https://github.com/MitchellChu/torndsession>`_ is a session extension for `Tornado <https://github.com/tornadoweb/tornado>`__ web framework.
Torndsession support application memory, file, redis or memcached to save session data for request, and it's easy to extend for developer.

Quick links
===========
    
* `Documentation <http://blog.useasp.net/category/30.aspx>`_
  
* `Source (github) <https://github.com/MitchellChu/torndsession>`_
  
* `Torndsession License <https://raw.githubusercontent.com/MitchellChu/torndsession/master/LICENSE>`_
  
* `Examples <https://github.com/MitchellChu/torndsession/tree/master/demos>`_


Hello, Session
==============

Here is a simple "Hello, Session" example web app for Tornado with Torndsession.::


    import tornado.web
    import tornado.httpserver
    import tornado.ioloop
    import torndsession


    class Application(tornado.web.Application):
        def __init__(self):
            handlers = [
                (r"/", MainHandler),
            ]
            settings = dict(
                debug=True,
            )
            # sid_name, lifetime added in 1.1.5.0
            # sid_name: the name of session id in cookies.
            # lifetime: session default expires seconds.
            session_settings = dict(
                driver='memory',
                driver_settings={'host': self},
                force_persistence=True,
                sid_name='torndsessionID',
                session_lifetime=1800
            ),
            settings.update(session=session_settings)
            tornado.web.Application.__init__(self, handlers, **settings)


    class MainHandler(torndsession.sessionhandler.SessionBaseHandler):
        def get(self):
            self.write("Hello, Session.<br/>")
            if 'data' in self.session:
                data = self.session['data']
            else:
                data = 0
            self.write('data=%s' % data)
            self.session["data"] = data + 1


    def main():
        http_server = tornado.httpserver.HTTPServer(Application())
        http_server.listen(8000)
        tornado.ioloop.IOLoop.instance().start()


    if __name__ == "__main__":
        main()


In this example, Request handler obtain memory session feature, it just inherit from SessionBaseHandler. more session example see `torndsession demos <https://github.com/MitchellChu/torndsession/tree/master/demos>`_.


Installation
============

**Automatic installation**:

::

    pip install torndsession

Torndsession is listed in `PyPI <https://pypi.python.org/pypi/torndsession>`__ and can be installed with `pip` or `easy_install`. Note that this installation can not install demos applicatinos which be included in source code.

The another way is use `git+` install torndsession from github.

::

    pip install git+https://github.com/mitchellchu/torndsession



**Manual installation**:

In this way, you need download the source from `PyPI <https://pypi.python.org/pypi/torndsession>`__.::

    tar xvzf torndsession.tar.gz
    cd torndsession
    python setup.py build
    sudo python setup.py install


The Torndsession source code is hosted on `GitHub <https://github.com/MitchellChu/torndsession>`_.


Updated
=======

Torndsession 1.1.5:

- fixed bug in 1.1.4
- default session id value generator changed. see `#ISSUE 12# <https://github.com/MitchellChu/torndsession/issues/12>`_.
- added two custom key in settings.

  - sid_name: session's cookie name.
  - session_lifetime: default expired seconds for session.

Torndsession 1.1.4:

- fixed bug

Torndsession 1.1.3 fixed some bug and supported python 3.x.


Requires
========


+ `Tornado <https://github.com/tornadoweb/tornado>`__
+ `Redis (Optional) <http://redis.io/>`_
+ `Memcached (Optional) <http://memcached.org/>`_



LICENSE
=======
Torndsession is licensed under MIT.


