### Indicator Workspaces: Elementary OS Workspace Indicator

Configure workspaces and interact with them in the panel.

----

If you are just wanting to install and use Indicator Workspaces, go to the [website](http://dysonsimmons.com/indicator-workspaces/) and download the latest version.

#### Developing

It is recommended that you first install the latest version before development as the icons need to be installed for them to load. You can then modify the indicator-workspaces file directly and run it directly from the command line during development. If you want to build and install your changes, they need to be commited in the git repository. Create your own branch, commit your changes and then build from your branch.

##### Requirements to Build/Run

```bash
$ sudo apt-get install devscripts debhelper python3
```

##### Building

```bash
$ debuild -us -uc
```

##### Installing

```bash
$ sudo debpkg -i indicator-workspaces_0.3_all.deb
```

#### License

The MIT License (MIT)

Copyright 2014 Dyson Simmons

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
