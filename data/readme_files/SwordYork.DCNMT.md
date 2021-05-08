Deep Character-Level  Neural Machine Translation
============
We implement a [**Deep Character-Level Neural Machine Translation**](https://arxiv.org/abs/1608.04738) based on [Theano](https://github.com/Theano/Theano) and [Blocks](https://github.com/mila-udem/blocks). Please intall relative packages according to [Blocks](http://blocks.readthedocs.io/en/latest/setup.html) before testing our program. Note that, please use Python 3 instead of Python 2. There will be some problems with Python 2. 

The architecture of DCNMT is shown in the following figure which is a single, large neural network.
![DCNMT](/dcnmt.png?raw=true "The architecture of DCNMT")




Training
-----------------------
If you want to train your own model, please prepare a parallel linguistics corpus, like corpus in [WMT](http://www.statmt.org/wmt15/translation-task.html). A GPU with 12GB memory will be helpful. You could run `bash train.sh` or follow these steps.
 1. Download the relative scripts (tokenizer.perl, multi-bleu.perl) and nonbreaking_prefix from [mose_git](https://raw.githubusercontent.com/moses-smt/mosesdecoder/master/scripts).
 2. Download the datasets, then tokenize and shuffle the cropus.
 3. Create the character list for both language using `create_vocab.py` in `preprocess` folder. Don't forget to pass the language setting, vocabulary size and file name to this script.
 4. Create a `data` folder, and put the `vocab.*.*.pkl` and `*.shuf` in the `data` folder.
 5. Prepare the tokenized validation and test set, and put them in `data` folder.
 6. Edit the `configurations.py`, and run `python training.py`. It will take 1 to 2 weeks to train a good model.


Testing
-----------------------
We have trained several models which listed in the following table. However, because of the limitation of available GPU and long training time (two weeks or more), we don't have enough time and resource to train on more language pairs. Would you like to help us to train on more language pairs? If you run into any trouble, please open an issue or email me directly at `echo c3dvcmQueW9ya0BnbWFpbC5jb20K | base64 -d`. Thanks!


| language pair | dataset | encoder_layers | transition_layers | BLEU |
|:--------:|:--------:|:--------:|:--------:|:--------:|
| en-fr | same as [RNNsearch](https://arxiv.org/abs/1409.0473) | 1 | 1 | 30.46 |
| en-fr | same as [RNNsearch](https://arxiv.org/abs/1409.0473) | 2 | 1 | 31.98 |
| en-fr | same as [RNNsearch](https://arxiv.org/abs/1409.0473) | 2 | 2 | 32.12 |
| en-cs | [wmt15](http://www.statmt.org/wmt15/translation-task.html) | 1 | 1 | 16.43 |


These models are all trained for about 5 epochs, and evaluate on `newstest2014` using the best validation model on `newstest2013`. You can download these models from [dropbox](https://www.dropbox.com/sh/eiaexn8q2sf277s/AADQ4RKWEsCIGkeKUUyMHh2aa?dl=0), then put them (dcnmt_\*, data, configurations.py) in this directory. To perform testing, just run `python testing.py`.  It takes about an hour to do translation on 3000 sentences if you have a moderate GPU.


Embedding
-----------------------
Please prepare a wordlist to calculate embedding, then just run `python embedding.py` to view the results.

Spelling Correction
-----------------------
It is the special feature of DCNMT model. For example,

> *Source:* Unlike in Canada, the American States are **responisble** for the **orgainisation** of federal elections in the United States.

> *Ref:* Contrairement au Canada, les États américains sont **responsables** de **l’organisation** des élections fédérales aux États-Unis.

> *Google:*  Contrairement au Canada, les États américains sont **responisble** pour le **orgainisation** des élections fédérales aux États-Unis.

> *DCNMT:* Contrairement au Canada, les États américains sont **responsables** de **l’organisation** des élections fédérales aux États-Unis.

The performance of misspelling correction would be analyzed later.



This program have been tested under the latest Theano and Blocks, it may fail to run because of different version. If you failed to run these scripts, please make sure that you can run the examples of [Blocks](https://github.com/mila-udem/blocks-examples).


References:
----------------------
1. [An Efficient Character-Level Neural Machine Translation](https://arxiv.org/abs/1608.04738)
2. [Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/abs/1409.0473)
