# python
## cpython
This folder contains a modified version of CPython which supports running in a Windows 10 UWP application.  
Specifically, this supports running in Python in a background application on Windows 10 IoT Core and also contains some module extensions which also support Windows 10 IoT Core.  See [README_uwp.md](README_uwp.md) for differences running under Windows 10 IoT core.
* Before performing any builds, ensure to run *cpython\PCBuild\get_externals -c* from command line first
* For UWP specific builds, open *cpython\Tools\pyuwp\pyuwp.sln*.
* For all CPython projects, open *cpython\PCBuild\pcbuild.sln*.

## pywindevices.sln
This file is the solution pulling the 3 device extension modules together to build for Windows 10 IoT Core UWP
### wingpio
This folder contains a GPIO extension module to work in Windows 10 IoT Core UWP applications for communication with GPIO pins 
### wini2c
This folder contains an I2C extension module to work in Windows 10 IoT Core UWP applications for communication with I2C interfaces
### winspi
This folder contains a SPI extension module to work in Windows 10 IoT Core UWP applications for communication with SPI interfaces

===

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

