# Obstacle-Detection-and-Path-Planning


#Overview

This is the code for [this](https://youtu.be/2cQK_brSVvo) video on youtube by @sirajology .Path planning is a technique used for find the shortest path between a source and destination. Path planning ensures that navigation is done in least time and in most optimized way, saving energy and providing a optimized way of the doing task.

We have a set of test images, each containing

1. 10x10 grid, making 100 squares
2. Obstacles marked as black square
3. Objects defined by three features, viz. Shape, Size and Color 

<img src="https://raw.githubusercontent.com/Aniruddha-Tapas/Obstacle-Detection-and-Path-Planning/master/test_images/test_image4.jpg" width="400" height= "400" />

The squares are identified by the coordinate (x,y) where x is the column and y is the row to which the square belongs. Each square
can be empty or have an Obstacle or have an Object.

The program returns 2 major findings:

<img src="https://raw.githubusercontent.com/Aniruddha-Tapas/Obstacle-Detection-and-Path-Planning/master/screenshot.png" />


1. <b><u>The coordinates of occupied grid</u></b>:

	The code returns a python list having ‘n’ python tuples, where ‘n’ denotes number of occupied grid in test image. Grid is to be considered occupied if either grid has an Obstacle or an Object. Each tuple has two elements, first element is the x-coordinate of an Obstacle/Object and second element is the y-coordinate of the Obstacle.

2. <b><u/>The minimum path<u/></b>:

	For each object in the test images, a matching object which is nearest to it is found using `compare_ssim` function from `scikit-image`. Object is said to be nearest to another Object, if length of path traversed between two objects is smallest. Traversal is done by moving either horizontally or vertically. The length of the path is determined by the number of moves made during traversal. [A* search](https://en.wikipedia.org/wiki/A*_search_algorithm) is used to find this shortest path.


The code return a python dictionary. Format for creating dictionary is as follows:
* Key for dictionary is a tuple - (x,y) coordinate of an Object
* first element of dictionary is a tuple - (x,y) coordinate of an object nearest to it
* second element is a list of tuples having (x,y) coordinate of all grids traversed i.e all route path
* third element of dictionary should be number of moves taken for traversal

##Dependencies

[Use pip to install.](https://pypi.python.org/pypi/pip)

1.  Install OpenCV for Python

	[`For Windows`](http://docs.opencv.org/3.1.0/d5/de5/tutorial_py_setup_in_windows.html)

	[`For Ubuntu`](http://www.pyimagesearch.com/2015/06/22/install-opencv-3-0-and-python-2-7-on-ubuntu/)

2. 
Install skimage (or scikit-image)
Open command prompt and type in:
```pip install scikit-image```

3. 
Install numpy 
Open command prompt and type in:
```pip install numpy```


#Usage

Run `main.py` to check the results.
You can edit the test image from main.py to see different results.

The `process_image.py` contains the major code.
Check that script to see the main functionality.
Follow the comments to undertand the code better.

`astarsearch.py` contains the implemenatation of A* search algo. 
`traversal.py` contains the script to traverse through the image to find objects/min path. 

#Credits

The credits for this code go to [Annirudha](https://github.com/Aniruddha-Tapas) i've merely created a wrapper to get people started.
