# PyPylon
An experimental python wrapper around the Basler Pylon 5 library. 
Its initial ideas were inspired by the [python-pylon](https://github.com/srgblnch/python-pylon) which is also a cython based wrapper around the Basler pylon library.

However, in contrast to `python-pylon` this code directly instanciates the Pylon C++ classes inside the cython code instead of adding another C++ abstraction layer. In addition it tries to automagically configure your build environment and to provide you with a PEP8 conform pythonic access to your camera.

While the basic code seems to work, I'd like to point out, that it still in early alpha stage. You will probably stumble over bugs.

## Current TODO list and development targets
 - [ ] Test with color cameras
 - [x] Handle different image packing other than Mono8
 - [ ] Make cython code more modular
 - [ ] Support commands
 - [ ] Try triggered images and such
 - [ ] Add some callbacks on events
 - [x] Test code under Windows
 
## Simple usage example
```python
>>> import pypylon
>>> pypylon.pylon_version.version
'5.0.1.build_6388'
>>> available_cameras = pypylon.factory.find_devices()
>>> available_cameras
[<DeviceInfo Basler acA2040-90um (xxxxxxx)>]
>>> cam = pypylon.factory.create_device(available_cameras[0])
>>> cam.opened
False
>>> cam.open()

>>> cam.properties['ExposureTime']
10000.0
>>> cam.properties['ExposureTime'] = 1000
>>> # Go to full available speed
... cam.properties['DeviceLinkThroughputLimitMode'] = 'Off'
>>> 

>>> import matplotlib.pyplot as plt
>>> for image in cam.grab_images(1):
...     plt.imshow(image)
...     plt.show()
```
