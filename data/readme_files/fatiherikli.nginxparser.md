### Nginx Configuration Parser

An nginx configuration parser that uses Pyparsing.

You can parse a nginx configuration file with `load` or `loads` method:

```python
>>> from nginxparser import load
>>> load(open("/etc/nginx/sites-enabled/foo.conf"))

 [['server'], [
    ['listen', '80'],
    ['server_name', 'foo.com'],
    ['root', '/home/ubuntu/sites/foo/']]]]
```

Same as other serialization modules also you can export configuration with `dump` and `dumps` methods.

```python
>>> from nginxparser import dumps
>>> dumps([['server'], [
            ['listen', '80'],
            ['server_name', 'foo.com'],
            ['root', '/home/ubuntu/sites/foo/']]])

'server {
    listen   80;
    server_name foo.com;
    root /home/ubuntu/sites/foo/;
 }'
```
