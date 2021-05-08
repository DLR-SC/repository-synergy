## GPS

Real-time 3D renderings of GPS satellite locations.

http://www.michaelfogleman.com/gps/

![Screenshot](http://www.michaelfogleman.com/static/img/project/gps/gps.png)

### Hardware

[GlobalSat BU-353-S4 USB GPS Receiver](http://www.amazon.com/GlobalSat-BU-353-S4-USB-Receiver-Black/dp/B008200LHW/)

### Dependencies

    pip install ephem pg pyserial

`pg` requires a glfw3 binary. On Mac, it's easy with Homebrew:

    brew tap homebrew/versions
    brew install glfw3
