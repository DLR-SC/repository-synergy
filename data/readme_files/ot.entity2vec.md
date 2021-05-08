entity2vec
==========

This library generates semantic embeddings of entities from text that describes
them. It can also quantize and compress the obtained models.

The training code is written in Python and it requires Numpy, Scipy, Numexpr,
Theano, and it also relies on gensim, which is included as a git submodule. The
code for model compression and entity scoring is instead written in Java.

This code was used in the experiments of the paper:

Roi Blanco, Giuseppe Ottaviano, Edgar Meij, _Fast and Space-efficient Entity
Linking in Queries_, ACM WSDM 2015.

Building the code
-----------------

The Python code does not require building but it is necessary to download the
git submodules. If you have cloned the repository without `--recursive`, you
will need to perform the following commands:

    $ git submodule init
    $ git submodule update

The Java code can be instead built with:

    $ mvn package


Generating the entity vectors
-----------------------------

To generate entity vectors it is necessary to generate word embeddings on a
large enough corpus. Both word2vec or gensim can be used for the task. The
training code assumes that the words in the corpus have been lower-cased. In the
following we assume that word2vec was used and the result is in
`data/word_model.bin`. Entities and descriptions should be in a TSV file
organized as follows (say `data/descriptions.tsv`).

    entity1\tdescription text 1\n
    entity2\tdescription text 2\n
    ...

For example, the description can be the first paragraph of the entity's
Wikipedia page.

The LR entity vectors can be generated as follows:

    $ ./entity_vectors.py train lr data/word_model.bin data/descriptions.tsv \
        data/entity.lr.model

The Centroid entity vectors can be computed likewise by passing `centroid`
instead of `lr`.

To evaluate the generated entity vectors it is possible to score a set of
entities matching given substrings against a given context with the following
command:

    $ ./entity_vectors eval data/word_model.bin data/entity.lr.model \
        data/entity.centroid.model

For example, by entering the string `+brad +pitt matches`, all the entities
containing the substrings `brad` and `pitt` will be found, and scored against
the context `brad pitt matches`. A few examples:

    > +brad +pitt matches
    Brad_Pitt_%28boxer%29                                 -1.103 | Brad_Pitt_filmography                                  0.516
    University_of_Pittsburgh_at_Bradford                  -1.627 | Brad_Pitt_%28boxer%29                                  0.482
    Brad_Pitt                                             -1.645 | List_of_awards_and_nominations_received_by_Brad_Pitt   0.370

    > +hollywood lyrics
    Hollywood_%28Madonna_song%29                          -0.014 | Broadway_to_Hollywood                                  0.594
    The_Hollywood_Palace                                  -0.016 | Hollywood_Pacific_Theatre                              0.584
    Hollywood_Hotel_%28film%29                            -0.019 | Hollywood_Speaks                                       0.573

Left column is scored with the LR model, right column with the Centroid
model. It is easy to see that in these examples LR gives significantly better
scores.


Compressing word and entity vectors
-----------------------------------

The word and entity models can be quantized and compressed. Quantization is done
through the script `model_quantization.py`. An example Java implementation is
included that uses Golomb coding for compression, and implements the scoring
algorithms using the compressed models.

To quantize the word vectors run

    $ ./model_quantization.py quant data/word_model.bin data/word

This will generate both a `.txt` file with the quantized coefficients and a
gensim file with the dequantized model. The latter is supposed to be used to
train the entity vectors as before: since a transformation is applied to the
word vectors before quantizing them, an entity model trained on `word_model.bin`
cannot be used with the quantized model.

When the new entity model is generated, it is possible to quantize it as well:

    $ ./model_quantization.py quant_entities data/entity.lr.model data/entity.lr

The `.txt` files can then be passed to the `Word2VecCompress` program that
generates the compressed binary models:

    $ mvn exec:java -Dexec.mainClass="it.cnr.isti.hpc.Word2VecCompress" -Dexec.args="data/word.e0.100.txt data/word.e0.100.bin"
    $ mvn exec:java -Dexec.mainClass="it.cnr.isti.hpc.Word2VecCompress" -Dexec.args="data/entity.lr.e0.100.txt data/entity.lr.e0.100.bin"

The resulting files can then be used with the `EntityScorer` class.


Authors
-------

* Giuseppe Ottaviano <giuott@gmail.com>
