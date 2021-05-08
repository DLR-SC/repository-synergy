##WaterMarker v.01

#####Project Status
![Project Status](http://img.shields.io/badge/Project%20Stage-Experimental-yellow.svg)
[![Build Status](https://travis-ci.org/jasimmk/watermarker.svg?branch=master)](https://travis-ci.org/jasimmk/watermarker) [![Coverage Status](https://coveralls.io/repos/jasimmk/watermarker/badge.svg)](https://coveralls.io/r/jasimmk/watermarker)
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fjasimmk%2Fwatermarker.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Fjasimmk%2Fwatermarker?ref=badge_shield)

A CLI tool for watermarking, converting and resizing images in bulk.  Created for mass watermarking  photos of KochiPython meetup group.  Whether you are a photographer, blogger, professional  this tool might be highly helpful for you to automate batch processing of images

##Installation

Make sure you have `Python 2.7` installed, This is tested only on `OSX 10.10.2`

a.  Clone git repository

```
git clone git@github.com:jasimmk/watermarker.git
```
b. Install requirements

You might need to install external libraries for image processing to work. For more details, have a look at http://pillow.readthedocs.org/en/latest/installation.html#external-libraries

Note: To be on the safe side, you should install the above-said libraries before you run the below command.

```
pip install -r requirements.txt
```

###Usage


```

$ ./watermarker -h
usage: watermarker [-h] [--wm-image WM_IMAGE] [--wm-position]
                   [--wm-text WM_TEXT] [--wm-text-color WM_TEXT_COLOR]
                   [--wm-text-font WM_TEXT_FONT] [--output-size OUTPUT_SIZE]
                   [--output-format] [--workers WORKERS] [--logging-level]
                   input_dir output_dir

A CLI tool for watermarking, converting and resizing images in bulk

positional arguments:
  input_dir             A single image file/ Directory of images to watermark
  output_dir            Output images directory

optional arguments:
  -h, --help            show this help message and exit
  --wm-image WM_IMAGE   Image used for watermarking. Supported types:
                        png,jpg,jpeg,gif,bmp,eps,webp,psd
  --wm-position         Position of watermark on image. Default:
                        'BOTTOM_RIGHT'. Allowed Values: {['BOTTOM_RIGHT',
                        'TOP_LEFT', 'CENTER_RIGHT', 'TOP_RIGHT',
                        'BOTTOM_CENTER', 'TOP_CENTER', 'CENTER_CENTER',
                        'BOTTOM_LEFT', 'CENTER_LEFT']}
  --wm-text WM_TEXT     Text to watermark eg: (c) SomeCompany
  --wm-text-color WM_TEXT_COLOR
                        Watermark text color. Default: white. Eg: black,
                        '#f0f0f0' etc
  --wm-text-font WM_TEXT_FONT
                        Watermark text font Eg: 'arial' or 'Comic Sans MS' or 'Ubuntu-M'
  --output-size OUTPUT_SIZE
                        Output Width & Height: Eg: 800x600 or 50%
  --output-format       Output format. Allowed types: png,jpg,gif
  --workers WORKERS     Number of worker processes Default: 4
  --logging-level       Logging level. Default: 'INFO'. Allowed: ['DEBUG',
                        'INFO', 'WARNING', 'ERROR', 'CRITICAL']
```

## Example

####Image watermarking
- Bulk watermark images inside a directory with another image

```
./watermarker ~/Desktop/InputImages/ ~/Desktop/OutputImages/ --wm-image ~/Desktop/watermark.png
```

- Single image, Watermark at CENTER_LEFT

```
./watermarker ~/Desktop/InputImages/input.jpg ~/Desktop/OutputImages/ --wm-image ~/Desktop/watermark.png --wm-position 'CENTER_LEFT'
```

- Single image, Watermark, reduce image size to `800x600` and convert to `PNG`

```
./watermarker ~/Desktop/InputImages/input.jpg ~/Desktop/OutputImages/ --wm-image ~/Desktop/watermark.png --output-size 800x600 --output-format png
```

#### Text Watermarking
- Bulk watermark images with text

```
./watermarker ~/Desktop/InputImages/ ~/Desktop/OutputImages/ --wm-text 'WaterMark'
```

- Single Image with Watermark at CENTER

```
./watermarker ~/Desktop/InputImages/input.jpg ~/Desktop/OutputImages/ --wm-text 'WaterMark' --wm-position 'CENTER_CENTER'
```

- Single Image with Watermark at TOP_RIGHT and font  'Microsoft Sans Serif' and Font color Black. Please note that only  `TTF` fonts are supported and size is automatically determined.

```
./watermarker ~/Desktop/InputImages/input.jpg ~/Desktop/OutputImages/ --wm-text 'WaterMark' --wm-position 'TOP_RIGHT' --wm-text-font 'Microsoft Sans Serif' --wm-text-color 'black'
```


##LICENCE
Provided under MIT Licence


[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fjasimmk%2Fwatermarker.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fjasimmk%2Fwatermarker?ref=badge_large)