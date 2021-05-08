===============
WTForms-Tornado
===============

WTForms extensions for Tornado.

.. image:: https://travis-ci.org/puentesarrin/wtforms-tornado.png
    :target: https://travis-ci.org/puentesarrin/wtforms-tornado
    :alt: Travis CI status

.. image:: https://coveralls.io/repos/puentesarrin/wtforms-tornado/badge.png
   :target: https://coveralls.io/r/puentesarrin/wtforms-tornado
   :alt: Coveralls status

.. image:: https://pypip.in/v/wtforms-tornado/badge.png
   :target: https://pypi.python.org/pypi/wtforms-tornado
   :alt: Latest PyPI version

.. image:: https://pypip.in/d/wtforms-tornado/badge.png
   :target: https://pypi.python.org/pypi/wtforms-tornado
   :alt: Number of PyPI downloads

Usage
=====

::

   import tornado.ioloop
   import tornado.web

   from wtforms.fields import IntegerField
   from wtforms.validators import Required
   from wtforms_tornado import Form

   class SumForm(Form):

       a = IntegerField(validators=[Required()])
       b = IntegerField(validators=[Required()])

   class SumHandler(tornado.web.RequestHandler):
       def get(self):
           self.write("Hello, world")

       def post(self):
           form = SumForm(self.request.arguments)
           if form.validate():
               self.write(str(form.data['a'] + form.data['b']))
           else:
               self.set_status(400)
               self.write("" % form.errors)

   application = tornado.web.Application([
       (r"/", SumHandler),
   ])

   if __name__ == "__main__":
       application.listen(8888)
       tornado.ioloop.IOLoop.instance().start()

Installation
============

You can to use pip_ to install WTForms-Tornado::

   $ pip install wtforms-tornado

Or using last source::

   $ pip install git+git://github.com/puentesarrin/wtforms-tornado.git

Or manually, download the latest source from PyPI_::

   $ tar xvzf wtforms-tornado-$VERSION.tar.gz
   $ cd wtforms-tornado-$VERSION
   $ python setup.py build
   $ sudo python setup.py install

.. _pip: https://pypi.python.org/pypi/pip
.. _PyPI: https://pypi.python.org/pypi/wtforms-tornado
