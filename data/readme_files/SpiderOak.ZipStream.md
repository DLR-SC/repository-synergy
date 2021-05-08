
# ZipStream

zipstream.py is a zip archive generator based on zipfile.py. It was created to
generate a zip file on-the-fly for download in a web.py (http://webpy.org/)
application. This is beneficial for when you want to provide a downloadable
archive of a large collection of regular files, which would be infeasible to
generate the archive prior to downloading.

The archive is generated as an iterator of strings, which, when joined, form
the zip archive. For example, the following code snippet would write a zip
archive containing files from 'path' to a normal file:

```python
zf = open('zipfile.zip', 'wb')
for data in ZipStream(path):
    zf.write(data)
zf.close()
```

Since recent versions of web.py support returning iterators of strings to be
sent to the browser, to download a dynamically generated archive, you could
use something like this snippet:

```python
def GET(self):
    path = '/path/to/dir/of/files'
    zip_filename = 'files.zip'
    web.header('Content-type' , 'application/zip')
    web.header('Content-Disposition', 'attachment; filename="%s"' % (
        zip_filename,))
    return ZipStream(path)
```

If the zlib module is available, ZipStream can generate compressed zip
archives.

## Requirements

  * Python >=2.6

## License

This library was created by SpiderOak, Inc. and is released under the GPLv3.
Copyright 2008-2013 SpiderOak Inc.

