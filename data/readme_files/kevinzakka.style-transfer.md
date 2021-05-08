# Artistic Style Transfer in Keras

This is a Keras implementation of [A Neural Algorithm of Artistic Style](https://arxiv.org/abs/1508.06576) by Leon A. Gatys, Alexander S. Ecker and Matthias Bethge.

<div align='center'>
<img src = './examples/bases/chicago.jpg' height="200px">
</div>

<div align = 'center'>
<img src = './examples/thumbnail/the_scream.jpg' height = '200px'>
<img src = './examples/results/my_result_at_iteration_0.png' height = '200px'>
<img src = './examples/results/my_result_at_iteration_499.png' height = '200px'>
</div>

<br>

Neural Styler lets you create artistic images by combining a base picture with the style of another. For example, the images above show multiple iterations of the [Chicago skyline](http://www.nursing.uic.edu/sites/default/files/chicagoskyline_2.jpg) combined with Edvard Munch's [The Scream](https://en.wikipedia.org/wiki/The_Scream).

## API

Styling an image is done through `generate.py` as follows:

```python
python generate.py examples/bases/chicago.jpg examples/styles/umbrella_girl.jpg examples/results/my_result
```

For a more detailed documentation along with the default parameters click [here](https://github.com/kevinzakka/style_transfer/blob/master/docs.md).

## Requirements

- keras (and associated dependencies)
  - numpy, scipy
  - pyyaml
  - HDF5 and h5py
- pillow 
- Python 2 and 3

## Attribution

- This implementation uses some code from Francois Chollet's [Neural Style Transfer](https://github.com/fchollet/keras/blob/master/examples/neural_style_transfer.py).
- The hierarchy also borrows from Giuseppe's gist which you can view [here](https://gist.github.com/giuseppebonaccorso/ef09a03424c9a49ae9b087bd364a5813).
- Documentation has also borrowed from Logan Engstrom's [Fast Style Transfer](https://github.com/lengstrom/fast-style-transfer)
