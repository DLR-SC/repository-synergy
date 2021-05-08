#deepAutoController
When we build deep graphical models, it is difficult to gain intuition about the contributions of individual neural units or groups of neural units. This project aims to achieve two goals:

* Allow a user to gain a better understanding of the code layer of a deep autoencoder
* Create new sounds by performing sample-based synthesis using a deep autoencoder.

The code in this repository will allow one to

* Collect a corpus of Constant Q Fourier Transform features
* Train a deep autoencoder having an arbitrary number of hidden layers and units per layer
* Perform music by modifying the optimized model interactively with a midi controller

Developed by [Andy Sarroff](http://www.cs.dartmouth.edu/~sarroff) with help from Sean Manton and Phil Hermans for the 2013 Hacking Audio and Music Research ([HAMR](http://labrosa.ee.columbia.edu/hamr2013/)) hackathon hosted by [LabROSA](http://labrosa.ee.columbia.edu/) at Columbia University.


## Dependencies
Bregman Audio-Visual Information Toolbox for feature extraction:
http://bregman.dartmouth.edu/bregman/

Theano for symbolic differentiation:
http://deeplearning.net/software/theano/

pygame for mdi stuff:
http://pygame.org/news.html

Korg nanoKontrol2 (other controllers should work with some minor editing):
http://www.korg.com/nanoseries2

This code has only been tested on a Mac having OS 10.8.4 using pythnon 2.7.5

Note: I've had problems with IOError: [Errno Input overflowed] -9981
updating to the newest pyaudio version fixed the problem Unfortunately, brew does not link to the newest version. to fix, do this:
brew rm portaudio
brew edit portaudio
replace the stable section with:
  stable do
    url 'http://www.portaudio.com/archives/pa_stable_v19_20140130.tgz'
    sha1 '526a7955de59016a06680ac24209ecb6ce05527d'
  end
brew install portaudio


## Files
### autocontrol.py

Build a deep autoencoder. Acoustically monitor the influence of the middle code layer using a Kork nanoKontroller2.

Use a Korg nonoKONTROL2 to control the weights of a n autoencoder. Given a learned model. The Korg attaches to the input of the center (topmost encoding layer). The faders of the Korg may be used to multiply the incoming weights. Use the faders as a multiplier, use the knobs to change the range of the faders. Use the solo buttons to reverse the sign of the multiplier. An output screen shows in real time the scale and multipler values.

The play  button plays the original audio file (reconstructed from the inverse CQFT. The record button plays the inverse resynthesized CQFT as output by the autoencoder. The stop button quits the application.

Example running command:

	python autocontrol.py {modelFile} {audioFile} --plot

### deepAE.py
Implementation of a deep autoencoder with some helper functions for reconstruction of the code layer and output.

This code is based on the Theano stacked denoising autoencoder tutorial. The main differences between this code and the tutorial are:

* This is a deep autoencoder, the tutorial shows a stacked autoencoder
* In order to implement a deepautoencoder, the model is unfolded into its symmetrical upper half.
* A couple of helper functions are provided to rebuild a saved model and plot results
* The learned model parameters are saved, along with input variables cost curves, and an arbitrary example of an original input and its reconstruction.

Example command:

	python deepAE.py l1 l2 l3 -o ~/Desktop/ -d {dataFile}

where l1, l2, and l3 are the sizes of the hidden layers.

### dA.py
This is a modified version of the denoising autoencoder tutorial provided at http://deeplearning.net/tutorial/dA.html

The modifications are very minor. In particular, two variables are added:

* nl (bool) : if False the hidden units are linear
* mult (theano.shared) : provides a mechanism for multiplying the weights and the input of each hidden unit. No error checking is provided. mult should be a theano shared variable holding an  dimensional array of floats. The length of the array should be the same as the number of hidden units.

This module is imported by deepAE.py

### deepAEFeatures.py
Use this code as a guide for extracting a dataset of CQFT features.
