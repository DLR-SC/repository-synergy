# Neural Networks for Audio Processing

Created by Stephen Welch, February 2015

Artificial Neural Networks offer a powerful tool for signal processing. This repository represents a collection of tools and a place to explore applications of neural networks and other adaptive signal processing approaches for audio processing. This work is biased towards music signals, and specifically toward processing signals from acoustic musical instruments, although other applications are quite feasible.

## Acoustic Pickups

One application explored here is modeling microphone signals of acoustic instruments from pickup signals. In the past, efforts have been made to model acoustic instruments as Linear Time Invariant (LTI) sytems. This approach works reasonably well for sustain portions of playing, but does a poor job when modeling transients, a key part of the tonality of an acoustic instrument. 

A strong modeling solution will then respond adaptively to various modes of operation of an acoustic instrument (plucking, strumming, bowing, sustain). 

## Objective and Direction
While this repository is focused on processing audio using neural networks, other models and adaptive filtering approaches will be investigated. We begin with an OLS (ordinary least squares) method and will slowly expand to explore more sophisticated approaches, while documenting the functionality, application, advantages, and disadvantages of other approaches. 

### Viewing iPython Notebooks
A significant portion of the work done here is developed and presented using iPython notebooks. These can be viewed using the nbviewer: http://nbviewer.ipython.org/github/stephencwelch/Neural-Networks-For-Audio-Processing/tree/master/


