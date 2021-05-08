===============
Flask-API-Utils
===============

.. image:: https://travis-ci.org/marselester/flask-api-utils.png
   :target: https://travis-ci.org/marselester/flask-api-utils

Flask-API-Utils helps you to create APIs. It makes responses in appropriate
formats, for instance, JSON. All you need to do is to return dictionary
from your views. Another useful feature is an authentication.
The library supports Hawk_ HTTP authentication scheme and `Flask-Login`_
extension. To sum up, there is an `API example project`_.

"Accept" Header based Response
------------------------------

**ResponsiveFlask** tends to make responses based on **Accept**
request-header (RFC 2616). If a view function does not return a dictionary,
then response will be processed as usual. Here is an example.

.. code-block:: python

    from api_utils import ResponsiveFlask

    app = ResponsiveFlask(__name__)


    @app.route('/')
    def hello_world():
        return {'hello': 'world'}


    def dummy_xml_formatter(*args, **kwargs):
        return '<hello>world</hello>'

    xml_mimetype = 'application/vnd.company+xml'
    app.response_formatters[xml_mimetype] = dummy_xml_formatter

    if __name__ == '__main__':
        app.run()


It's assumed that file was saved as ``api.py``:

.. code-block:: console

    $ python api.py
     * Running on http://127.0.0.1:5000/

Here are curl examples with different **Accept** headers:

.. code-block:: console

    $ curl http://127.0.0.1:5000/ -i
    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 22
    Server: Werkzeug/0.9.4 Python/2.7.5
    Date: Sat, 07 Dec 2013 14:01:14 GMT

    {
      "hello": "world"
    }
    $ curl http://127.0.0.1:5000/ -H 'Accept: application/vnd.company+xml' -i
    HTTP/1.0 200 OK
    Content-Type: application/vnd.company+xml; charset=utf-8
    Content-Length: 20
    Server: Werkzeug/0.9.4 Python/2.7.5
    Date: Sat, 07 Dec 2013 14:01:50 GMT

    <hello>world</hello>
    $ curl http://127.0.0.1:5000/ -H 'Accept: blah/*' -i
    HTTP/1.0 406 NOT ACCEPTABLE
    Content-Type: application/json
    Content-Length: 83
    Server: Werkzeug/0.9.4 Python/2.7.5
    Date: Sat, 07 Dec 2013 14:02:23 GMT

    {
      "mimetypes": [
        "application/json",
        "application/vnd.company+xml"
      ]
    }

HTTP Error Handling
-------------------

You can set HTTP error handler by using **@app.default_errorhandler**
decorator. Note that it might override already defined error handlers,
so you should declare it before them.

.. code-block:: python

    from flask import request
    from api_utils import ResponsiveFlask

    app = ResponsiveFlask(__name__)


    @app.default_errorhandler
    def werkzeug_default_exceptions_handler(error):
        error_info_url = (
            'http://developer.example.com/errors.html#error-code-{}'
        ).format(error.code)

        response = {
            'code': error.code,
            'message': str(error),
            'info_url': error_info_url,
        }
        return response, error.code


    @app.errorhandler(404)
    def page_not_found(error):
        return {'error': 'This page does not exist'}, 404


    class MyException(Exception):
        pass


    @app.errorhandler(MyException)
    def special_exception_handler(error):
        return {'error': str(error)}


    @app.route('/my-exc')
    def hello_my_exception():
        raise MyException('Krivens!')


    @app.route('/yarr')
    def hello_bad_request():
        request.args['bad-key']

    if __name__ == '__main__':
        app.run()


Let's try to curl this example. First response shows that we redefined
default ``{'code': 400, 'message': '400: Bad Request'}`` error format.
Next ones show that you can handle specific errors as usual.

.. code-block:: console

    $ curl http://127.0.0.1:5000/yarr -i
    HTTP/1.0 400 BAD REQUEST
    Content-Type: application/json
    Content-Length: 125
    Server: Werkzeug/0.9.4 Python/2.7.5
    Date: Sun, 29 Dec 2013 14:26:30 GMT

    {
      "code": 400,
      "info_url": "http://developer.example.com/errors.html#error-code-400",
      "message": "400: Bad Request"
    }
    $ curl http://127.0.0.1:5000/ -i
    HTTP/1.0 404 NOT FOUND
    Content-Type: application/json
    Content-Length: 41
    Server: Werkzeug/0.9.4 Python/2.7.5
    Date: Sun, 29 Dec 2013 14:28:46 GMT

    {
      "error": "This page does not exist"
    }
    $ curl http://127.0.0.1:5000/my-exc -i
    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 25
    Server: Werkzeug/0.9.4 Python/2.7.5
    Date: Sun, 29 Dec 2013 14:27:33 GMT

    {
      "error": "Krivens!"
    }

Authentication
--------------

**Hawk** extension provides API authentication for Flask.

Hawk_ is an HTTP authentication scheme using a message authentication code
(MAC) algorithm to provide partial HTTP request cryptographic verification.

The extension is based on Mohawk_, so make sure you have installed it.

.. code-block:: console

    $ pip install mohawk

Usage example:

.. code-block:: python

    from flask import Flask
    from api_utils import Hawk

    app = Flask(__name__)
    hawk = Hawk(app)


    @hawk.client_key_loader
    def get_client_key(client_id):
        # In a real project you will likely use some storage.
        if client_id == 'Alice':
            return 'werxhqb98rpaxn39848xrunpaw3489ruxnpa98w4rxn'
        else:
            raise LookupError()


    @app.route('/')
    @hawk.auth_required
    def index():
        return 'hello world'

    if __name__ == '__main__':
        app.run()

.. code-block:: console

    $ curl http://127.0.0.1:5000/ -i
    HTTP/1.0 401 UNAUTHORIZED
    ...

Cookie based authentication is disabled by default.
Set ``HAWK_ALLOW_COOKIE_AUTH = True`` to enable it. Also **Hawk** supports
response signing, enable it ``HAWK_SIGN_RESPONSE = True`` if you need it.

Following configuration keys are used by Mohawk_ library.

.. code-block:: python

    HAWK_ALGORITHM = 'sha256'
    HAWK_ACCEPT_UNTRUSTED_CONTENT = False
    HAWK_LOCALTIME_OFFSET_IN_SECONDS = 0
    HAWK_TIMESTAMP_SKEW_IN_SECONDS = 60

Check `Mohawk documentation`_ for more information.

It can be convenient to globally turn off authentication when unit testing
by setting ``HAWK_ENABLED = False``.

Tests
-----

Tests are run by:

.. code-block:: console

    $ pip install -r requirements.txt
    $ tox

.. _API example project: https://github.com/marselester/api-example-based-on-flask
.. _Hawk: https://github.com/hueniverse/hawk
.. _Mohawk: https://github.com/kumar303/mohawk
.. _Mohawk documentation: http://mohawk.readthedocs.org
.. _Flask-Login: https://flask-login.readthedocs.org
