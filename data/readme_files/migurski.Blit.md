Blit
====

Simple pixel-composition library for Python.

Blit can combine images and colors using different image blend modes, inspired
by the layers palette in GIMP or Adobe Photoshop. You can create a layer from
an image or color, and add new layers on top of it with a combination of opacity
(0 - 1), mask image, and blend mode.

    >>> from Blit import Bitmap, adjustments
    >>> photo = Bitmap('photo.jpg')
    >>> sepia = adjustments.curves2([(0, 64), (128, 158), (255, 255)], [(0, 23), (128, 140), (255, 255)], [(0, 0), (128, 98), (255, 194)])
    >>> oldphoto = photo.adjust(sepia)
    
    >>> from Blit import Color
    >>> purple = Color(50, 0, 100)
    >>> orange = Color(255, 220, 180)
    >>> duotone = purple.blend(orange, mask=photo)

API
---

__Layer__

* `Layer.size()` returns (width, height) tuple.

* `Layer.rgba(width, height)` returns list of four numpy arrays, for red,
  green, blue and alpha channels. The dimensions of channel arrays will
  be extended or clipped to match the requested width and height.

* `Layer.image()` returns a new PIL image instance for the layer.

* `Layer.blend(otherlayer, mask=None, opacity=1, blendfunc=None)`
  blends two layers and returns a new Layer that combines the two.
  
  Optional arguments:
  * `mask` is a Layer instance interpreted as a greyscale mask.
  * `opacity` is a float from zero to one.
  * `blendfunc` is a blend mode such as screen or multiply. See "blends" below.

* `Layer.adjust(adjustfunc)` returns a new layer instance adjusted by
  the adjustment function. See "adjustments" below.

__Bitmap__

A kind of Layer that represents a raster image file. Instantiate a Bitmap
with a file name:

    bicycle = Bitmap('bicycle.jpg')

__Color__

A kind of Layer that represents a single color. Instantiate a Color with
the numeric values of its channels, from zero to 255:

    orange = Color(255, 153, 0)
    translucent_black = Color(0, 0, 0, 102)

* `Color.size()` returns None so it's clear that a color has no intrinsic size.
* `Color.image()` returns a 1x1 pixel PIL image.

__photoshop.PSD__

Represents a Photoshop document that can be combined with other layers.
Behaves identically to `Layer` with three exceptions:

* `photoshop.PSD.save(outfile)` saves Photoshop-compatible file to a named file or file-like object.
* Additional boolean `clipped` keyword argument to `blend()` method creates clipping masks.
* No `adjust()` method.

__blends__

A blend is a function that accepts two identically-sized
input single-channel arrays and returns a single output array.

* `blends.screen(bottom, top)` implements
  [screen blend](http://illusions.hu/effectwiki/doku.php?id=screen_blending).

* `blends.add(bottom, top)` implements
  [additive blending](http://illusions.hu/effectwiki/doku.php?id=additive_blending).

* `blends.multiply(bottom, top)` implements
  [multiply blend](http://illusions.hu/effectwiki/doku.php?id=multiply_blending).

* `blends.subtract(bottom, top)` implements
  [subtractive blending](http://illusions.hu/effectwiki/doku.php?id=subtractive_blending).

* `blends.linear_light(bottom, top)` implements
  [linear light blend](http://illusions.hu/effectwiki/doku.php?id=linear_light_blending).

* `blends.hard_light(bottom, top)` implements
  [hard light blend](http://illusions.hu/effectwiki/doku.php?id=hard_light_blending).

__adjustments__

An adjustment is a function that takes a list of four identically-sized channel
arrays (red, green, blue, and alpha) and returns a new list of four channels.
The factory functions in this module return functions that perform adjustments.

* `adjustments.threshold(red, green, blue)` returns an adjustment function
  that applies a threshold to each channel, converting greyscale channels
  to plain black & white cut at the value given (0-255). If omitted, the green
  and blue arguments are identical to red.

* `adjustments.curves(black, grey, white)` returns an adjustment function
  that applies a curve to each channel. Arguments are three integers that
  are intended to be mapped to black, grey, and white outputs. For example,
  `curves(0, 204, 255)` will darken a layer while `curves(0, 53, 255)`
  will lighten it.

* `adjustments.curves2(red_map, green_map, blue_map)` returns an adjustment
  function that applies a curve to each channel.
  
  Arguments are given in the form of three value mappings, typically
  mapping black, grey and white input and output values. One argument
  indicates an effect applicable to all channels, three arguments apply
  effects to each channel separately.
    
  Simple monochrome inversion:

      `map_red=[(0, 255), (128, 128), (255, 0)]`
  
  Darken a light image by pushing light grey down by 50%, 0x99 to 0x66:
      
      `map_red=[(0, 255), (153, 102), (255, 0)]`
  
  Shaded hills, with Imhof-style purple-blue shadows and warm highlights:
      
      `map_red=[(0, 22), (128, 128), (255, 255)],
      map_green=[(0, 29), (128, 128), (255, 255)],
      map_blue=[(0, 65), (128, 128), (255, 228)]`

__utils__

`Blit.utils` includes several image and array utility functions:

 * `arr2img()` converts Numeric array to PIL Image.

 * `img2arr()` converts PIL Image to Numeric array.

 * `chan2img()` converts single floating point Numeric array object to one-channel PIL Image.

 * `img2chan()` converts one-channel PIL Image to single floating point Numeric array object.

 * `rgba2img()` converts four floating point Numeric array objects to PIL Image.

 * `img2rgba()` converts PIL Image to four floating point Numeric array objects.

 * `rgba2lum()` converts four Numeric array objects to single floating point luminance array.
