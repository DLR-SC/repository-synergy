This Is My Jam Image Filters
============================

A set of image filters crafted and curated by This Is My Jam. These are currently live on www.thisismyjam.com/jam/style, where they are used to automatically generate backgrounds from jam images.

There's also a [blog post](http://thisismyjam.tumblr.com/post/44061678763/how-we-built-music-looks-awesome-how-you-can-join) we wrote about how and why we created these filters.

Installation
------------

To install the Python filters:

    cd jam_image_filter
    sudo pip install -r requirements.txt

To install *glitch*:

    cd src/glitch
    make
    sudo make install

Usage
-----

The Python filters all reside in the `jam_image_filter` folder. To invoke:

    python FILTER.py INPUT_PATH OUTPUT_PATH

Contribute
----------

Have an algorithm? Send us a pull request and we'll see if we can get it up on Jam. You can write your script in pretty much any language (as long as we can figure out how to run it, and it doesn't open massive security holes).

Some constraints:

 * It should take the same argument list as the existing ones, i.e. the first argument should be an input file and the second an output file
 * Your script should work with .jpg, .png, and .gif input files (also, grayscale, semi-transparency, etc.)
 * Ideally, it should either tile or have 1700x540px dimensions
 * It should run under 2 seconds and not use crazy amounts of memory

There are some useful functions in util.py, but you don't have to use them.

Examples
--------

![Halftone](https://raw.github.com/thisismyjam/jam-image-filter/master/examples/halftone.jpg)

![PXL](https://raw.github.com/thisismyjam/jam-image-filter/master/examples/pxl.jpg)

![Glitch](https://raw.github.com/thisismyjam/jam-image-filter/master/examples/glitch.jpg)

For more examples look inside the `examples` folder.
