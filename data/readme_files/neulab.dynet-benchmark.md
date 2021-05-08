DyNet Benchmarks
----------------
by Graham Neubig, Yoav Goldberg, Chaitanya Malaviya, Austin Matthews, Yusuke Oda, and Pengcheng Yin

These are benchmarks to compare [DyNet](http://github.com/clab/dynet) against several other neural network toolkits: TensorFlow, Theano, and Chainer. It covers four different natural language processing tasks, some of which are only implemented in a subset of the toolkits as they wouldn't be straightforward to implement in the others:

* rnnlm-batch: A recurrent neural network language model with mini-batched training.
* bilstm-tagger: A tagger that runs a bi-directional LSTM and selects a tag for each word.
* bilstm-tagger-withchar: Similar to bilstm-tagger, but uses characer-based embeddings for unknown words.
* treelstm: A text tagger based on tree-structured LSTMs.

The benchmarks can be run by first compiling the `dynet-cpp` examples, then running run-tests.sh.

**Note:** `dynet-cpp` needs the sequence-ops branch of DyNet to compile.
