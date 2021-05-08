# sketch
Project https://github.com/udibr/sketch

Use RNN to model handwriting using Theano blocks.
I am trying to reproduce handwriting model given by
[Alex Graves](http://arxiv.org/abs/1308.0850),
see also his [demo](http://www.cs.toronto.edu/~graves/handwriting.html)

Dependencies
------------
* [Blocks](https://github.com/bartvm/blocks) follow
  the [install instructions](http://blocks.readthedocs.org/en/latest/setup.html).
  This will install all the other dependencies for you (Theano, Fuel, etc.).
  See [this note if using python 3.4](https://github.com/Theano/Theano/issues/2317)
* Download handwriting dataset using [this notebook](./handwriting-to-hdf5.ipynb)
 
Running code
------------

Run parameteres are used to build a unique name which is used to 
create a directory where the model is saved and also a sample image
`sketch.png`

For example:

```bash
python sketch.py --dim 900 --depth 1 --bs 56 --lr 1e-3 -G 10
   Running experiment handwriting-1X900m20d5r13b56e15G10
   ...
   Epoch 1, step 105
   test_sequence_log_likelihood: -631.519287109
python sketch.py --dim 900 --depth 1 --bs 56 --lr 3e-4 -G 10 --model handwriting-1X900m20d5r13b56e15G10
   Running experiment handwriting-1X900m20d5r34b56e15G10
   ...
   Epoch 5, step 25
   test_sequence_log_likelihood: -950.866210938
python sketch.py --dim 900 --depth 1 --bs 56 --lr 1e-4 -G 10 --model handwriting-1X900m20d5r34b56e15G10
   Running experiment handwriting-1X900m20d5r14b56e15G10
   ...
   Epoch 153, step 165
   test_sequence_log_likelihood: -1482.28918457
python sketch.py --dim 900 --depth 1 --bs 56 --lr 1e-5  -G 10 --model handwriting-1X900m20d5r14b56e15G10
   Epoch 11, step 84
   test_sequence_log_likelihood: -1607.07531738
```
The result directory can be downloaded
[here](https://s3.amazonaws.com/udisketch/handwriting-1X900m20d5r15b56e15G10.tgz)
and after opening it you can generate samples with:

```bash
python sketch.py --dim 900 --depth 1 --model handwriting-1X900m20d5r15b56e15G10 --sample
```

 ![samples](sketch.png)
