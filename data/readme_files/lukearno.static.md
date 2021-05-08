# static

Serve static or templated content via WSGI or stand-alone.

Install Static

    $ pip install static

Serve up some content:

    $ static localhost 9999 static-content/

Or in the context of a WSGI application:

```python
import static
wsgi_app = static.Cling('/var/www')
```

You can also use Python template strings, Moustache templates or 
easily roll your own templating plugin. See the tests and source
code for examples.

Pull requests welcome. Happy hacking.

