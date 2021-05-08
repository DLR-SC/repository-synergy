# Desert

Desert consists of two parts.

The main library is simply called `Desert`. It is a CUDA accelerated library
for sandpainting: https://inconvergent.net/grains-of-sand/

The second part is called `Erosion`. A Redis-based client and worker that can
accept and draw `Desert` primitives and commands encoded as JSON objects. That
means that you can use the `Erosion` worker from any platform as long as you
can construct JSON and send it to a Redis queue. Eg. if you want to program in
a different language, while still having a fast drawing engine that benefits
from CUDA.

I've written a little more about the library here:
https://inconvergent.net/lost-in-the-desert/

![img](img/img.png?raw=true "img")



## Install

Use the install script:

    ./install.sh

This will use `setuptools` to install python libraries `desert` and `erosion`.
As well as a terminal util called `erosion`. It will be available as
`~/.local/bin/erosion` if you installed with the `install.sh` script.


## Examples

There are some examples in `./examples`.

To use `Desert` via Python as a local library, see:

    main.py

To see how `Erosion` works, you can run this command (from `./examples`):

    ./erosion-send.py && ~/.local/bin/erosion worker --path ./ --show --vv

This will first send some `Desert` primitives to the `Erosion` (Redis) queue.
Then it will run the `Erosion` worker, which draws those primitives. Finally it
will save the resulting image.

To see how the `Erosion` terminal util works:

    ~/.local/bin/erosion -h


## Dependencies

This code is developed on Ubuntu 16.04 LTS. I imagine you will be able to get
it running on Mac as well.

The library depends on the CUDA toolkit (8.0), Redis (if you are using
`Erosion`), and a few Python (3) packages. If you install using the install
script, the python packages will be installed automatically.


## On Use and Contributions

This code is a tool that I have written for my own use. I release it publicly
in case people find it useful. It is not however intended as a
collaboration/Open Source project. As such I am unlikely to accept PRs, reply
to issues, or take requests.


## Todo

Desert:

- [ ] Circle: varying rad
- [ ] Box: varying size


## Notes

If cuda is not working try `sudo ldconfig`. and check $LD_LIBRARY_PATH

https://documen.tician.de/pycuda/tutorial.html#executing-a-kernel

http://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#kernels

