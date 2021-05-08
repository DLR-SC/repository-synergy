## About ##
This module allows, with the use of python decorators, to transparently select a render function for an HTTP request handler's result. It uses mimeparse to parse the HTTP Accept header and select the best available representation.

## Author ##
[Nicola Iarocci](mailto:nicola@nicolaiarocci.com)

### Contributors ###
[Bruno Ripa](http://twitter.com/brunoripa)

## License ##
[MIT License](http://www.opensource.org/licenses/mit-license.php)

## Attribution ##
This is a Flask port from the excellent [mimerender](http://code.google.com/p/mimerender/) v0.2.3 by Martin Blech. *Update* Martin has moved to GitHub and added Flask support to the original mimerender project. He has plans for further developments, so you might want to fork/clone [his project](https://github.com/martinblech/mimerender) instead.

## Usage ##
The decorated function must return a dict with the objects necessary to
render the final result to the user. The selected renderer will be called
with the map contents as keyword arguments.
If override_arg_idx isn't None, the wrapped function's positional argument
at that index will be removed and used instead of the Accept header.
override_input_key works the same way, but with the specified query string 
parameter.

	from flask import Flask, request, jsonify
	from flaskmimerender import mimerender

	render_xml = lambda message: '<message>%s</message>' % message
	render_json = jsonify
	render_html = lambda message: '<html><body>%s</body></html>' % message
	render_txt = lambda message: message

	app = Flask(__name__)

	@app.route('/')
	@mimerender(
	    default = 'html',
	    html = render_html,
	    xml  = render_xml,
	    json = render_json,
	    txt  = render_txt
	)
	def index():
		if request.method == 'GET':
			return {'message': 'Hello, World!'}

	if __name__ == "__main__":
	    app.run(debug=True)

Then you can do:

	$ curl -H "Accept: application/html" localhost:5000/
	<html><body>Hello, World!</body></html>

	$ curl -H "Accept: application/xml" localhost:5000/
	<message>Hello, World!</message>

	$ curl -H "Accept: application/json" localhost:5000/
	{'message':'Hello, World!'}

	$ curl -H "Accept: text/plain" localhost:5000/
	Hello, World!

## Installation ##
Flask-MimeRender is on the official Python Package Index (PyPI). All you have to do is

	pip install flask-mimerender

and you're good to go.

