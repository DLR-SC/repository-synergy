# Google Deepdream + Docker

A Docker Container to run Google's [Deepdream](https://github.com/google/deepdream/). This avoids having to setup all the dependencies (including GPU drivers, Python, Caffe, etc) in your OS of choice, so you can skip right to the fun part!


## Installing

The only dependency you need is [Docker](https://www.docker.com/).


## Building locally

```
docker build -t herval/deepdream .
```


## Running

```
docker run -i -t -e INPUT=your_file.png -e ITER=20 -e SCALE=0.10 -e MODEL='inception_3b/5x5_reduce' -v /path/to/your/folder:/data herval/deepdream
```

Replace  `/path/to/your/folder` to the folder where your `INPUT` file is. That's also where the output will be written to.


*Note*: Depending on how much memory your machine has, you might run into problems with high-res images. In my case, processing failed for a 12mp image. Either stick to smaller images or buy more RAM ;-)


The output of the script will be written to the `output/` subfolder. Enjoy!