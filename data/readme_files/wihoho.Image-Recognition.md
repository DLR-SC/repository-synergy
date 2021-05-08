### Introduction [![HitCount](http://hits.dwyl.io/wihoho/wihoho/Image-Recognition.svg)](http://hits.dwyl.io/wihoho/wihoho/Image-Recognition)
This python package implements Spatial Pyramid Matching [1] to recognize images under different categories. Furthermore, Earth Mover's distance [2] is also incorporated to better align parts of images when calculating image-to-image distance. 

For better explanation, please refer to [my report](https://dl.dropboxusercontent.com/u/37572555/Github/Image%20Recognition/ImageRec.pdf).


### Dependencies
1. python 2.7.x
2. sklearn
3. vlfeat (extract SIFT features)
4. numpy
5. scipy

In terms of vlfeat, do the following steps to ensure SIFT extractions succeed.

1. Download vlfeat and remember the path of vlfeat of your environment
2. Update the following path at line 84 in `/recognition/utils.py` with your own path of vlfeat

```python
os.environ['PATH'] += os.pathsep +'/Users/GongLi/Dropbox/FYP/PythonProject/vlfeat/bin/maci64'
os.system(cmmd)
```

### Usage 
Below are two examples of two approaches to recognise images.
	
	python SpatialPyramidExample.py
	python EarthMoverDistanceExample.py

### Data Set

The image data set, in which there are six classes (shooting, playing guitar, running, phoning, riding bike and riding horse) as shown in Figure 13, comes from [[3]](https://github.com/lipiji/PG_BOW_DEMO). For each class, there are 60 images with different backgrounds, different persons and different viewpoints.

![dataSet](https://dl.dropboxusercontent.com/u/37572555/Github/Image%20Recognition/imageSet.png)

### Performances
Recognition accuracies (percent) of different pyramids using SVMs with different kernels
![result](https://dl.dropboxusercontent.com/u/37572555/Github/Image%20Recognition/result1.png)

Comparison of recognition accuracy (percent) between aligned distance and unaligned distance

![result](https://dl.dropboxusercontent.com/u/37572555/Github/Image%20Recognition/result2.png)

### References
[1] S. Lazebnik, C. Schmid, and J. Ponce, “Beyond bags of features: Spatial pyramid matching for recognizing natural scene categories,” in Computer Vision and Pattern Recognition, 2006 IEEE Computer Society Conference on, vol. 2. IEEE, 2006, pp. 2169–2178.

[2] Y. Rubner, C. Tomasi, and L. J. Guibas, “The earth mover’s distance as a metric for image retrieval,” International Journal of Computer Vision, vol. 40, no. 2, pp. 99–121, 2000.

[3] P. Li, J. Ma, and S. Gao, “Actions in still web images: Visualization, detec- tion and retrieval,” in Web-Age Information Management. Springer, 2011, pp. 302–313.


### License
MIT License

Copyright © 2015 wihoho <wihoho@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
