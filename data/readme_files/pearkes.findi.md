findi
-------

A port of a port of sosumi. Find your iPhone through Apple's API.

Source from:

[comfuture's recordmylatitude](https://github.com/comfuture/recordmylatitude/blob/master/findmyiphone/__init__.py)

That was inspired by:

[tyler hall's sosumi](https://github.com/tylerhall/sosumi)

I will attempt to keep up with Apple's changing API, as it breaks horribly when they update the app and modify version numbers. Fair warning.

Use
-------

Initialize findmyiphone with your Apple ID.

```python
from findi import FindMyIPhone
findi = FindMyIPhone('email@example.com', 'password')
```

List your devices.

```python
print findi.devices
```

Get the first devices location:

```python
iphone = findi.devices[0]
print iphone.latitude, iphone.longitude
```

Recording Your Location
-------
There is an example Heroku application called [findi-heroku-example](https://github.com/pearkes/findi-heroku-example) with instructions
for setting up a service that stores your location over a period of time.

LICENSE
-------

The MIT License

Majority of source Copyright (c) 2011 [comfuture](https://github.com/comfuture).

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

