# FourEyes
FourEyes uses the facial geometry of users to help them choose the most flattering glasses. 
First, it uses the ratios between six key points on the user’s face to calculate the user’s primary face shape.
Then, it uses that information to recommend a flattering glasses style.
Next, FourEyes allows users to try on several frames in that style with face tracking.
Finally, it  presents the user with a gallery of commercially available frames in that style.

All calculations and recommendations are based on extensive research, sources included in sources.txt

## INSTALLATION
FourEyes is a python file. Before running FourEyes, you will additionally need to install:
* OpenCV
* PIL
* NumPy

### MAC

[How to install OpenCV](https://jjyap.wordpress.com/2014/05/24/installing-opencv-2-4-9-on-mac-osx-with-python-support/)


How to install PIL:

1. open terminal

2. type “sudo easy_install pip”

3. type “sudo pip install pil”


How to install NumPy:

1. [install MacPorts](http://www.macports.org/install.php)

2. open terminal

3. type “sudo port install py27-numpy”


### WINDOWS
[How to install OpenCV](http://docs.opencv.org/doc/tutorials/introduction/windows_install/windows_install.html)

[How to install PIL](http://www.pythonware.com/products/pil/)

[How to install NumPy](http://docs.scipy.org/doc/numpy/user/install.html)
