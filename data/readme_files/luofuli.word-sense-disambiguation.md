# Incorporating Dictionary Knowledge into Neural Word Sense Disambiguation

This repo contains the code and data of the following paper:

<i> "Incorporating Glosses into Neural Word Sense Disambiguation". Fuli Luo, Tianyu Liu, Qiaolin Xia, Baobao Chang, Zhifang Sui. ACL 2018. [Link](http://aclweb.org/anthology/P18-1230)</i>

In this paper, we integrate the context and glosses of the target word into a unified framework in order to make full use of both labeled data and lexical knowledge of WSD.
Therefore, we propose ``GAS``: a gloss-augmented WSD neural network which jointly encodes the context and glosses of the target word in an improved memory network.
We further extend the original gloss of word sense via its semantic relations in WordNet to enrich the gloss information (``GAS_ext``).

<p align="center"><img src="image/model.png"></p>

<br>

## Quick Start
Steps to train and test a model:
- modify `self.GLOVE_VECTOR` in `path.py`: pre-trained word embeddings path (download from: [https://nlp.stanford.edu/projects/glove/](https://nlp.stanford.edu/projects/glove/)).
- modify `self.WORDNET_PATH` in `path.py`: wordnet 3.0 database.
- go to the <code>GAS/</code> folder and run the following command:

```bash
python train.py
```

- or go to the `GAS_ext/` folder and run the following command:
```bash
python train_plus.py
```

- All outputs will be stored in  `tmp/` folder. More specifically, the summary of the model path is `tmp/tf.log`), and test result path is `tmp/result.txt`.


## Dependencies
```
python2.7
lxml==4.2.1
tensorflow_gpu==1.6.0
numpy==1.14.2
nltk==3.2.5
beautifulsoup4==4.6.0
```

## Cite

If you use this code, please cite the following paper:
```
@InProceedings{P18-1230,
  author = 	"Luo, Fuli
		and Liu, Tianyu
		and Xia, Qiaolin
		and Chang, Baobao
		and Sui, Zhifang",
  title = 	"Incorporating Glosses into Neural Word Sense Disambiguation",
  booktitle = 	"Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (ACL)",
  year = 	"2018",
  publisher = 	"Association for Computational Linguistics",
  pages = 	"2473--2482",
  url = 	"http://aclweb.org/anthology/P18-1230"
}
```
