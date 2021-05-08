# RACE Reading Comprehension Task

Code for the paper: [RACE: Large-scale ReAding Comprehension Dataset From Examination](https://arxiv.org/pdf/1704.04683.pdf). Guokun Lai*, Qizhe Xie*, Hanxiao Liu, Yiming Yang and Eduard Hovy. EMNLP 2017

[Leaderboard of RACE](http://www.qizhexie.com//data/RACE_leaderboard)

## Dependencies
* Python 2.7
* Theano >= 0.7
* Lasagne 0.2.dev1

## Datasets
* RACE:
    Please submit a data request [here](http://www.cs.cmu.edu/~glai1/data/race/). The data will be automatically sent to you. Create a "data" directory alongside "src" directory and download the data.

* Word embeddings:
    * glove.6B.zip: [http://nlp.stanford.edu/data/glove.6B.zip](http://nlp.stanford.edu/data/glove.6B.zip)

## Usage
### Preprocessing
    * python preprocess.py

### Stanford AR
    * test pre-trained model: bash test_SAR.sh
    * train: bash train_SAR.sh (The pre-trained model will be replaced)

### GA
    * test pre-trained model: bash test_GA.sh
    * train: bash train_GA.sh (The pre-trained model will be replaced)

## Reference
```
@inproceedings{lai2017large,
  title={RACE: Large-scale ReAding Comprehension Dataset From Examinations},
  author={Lai, Guokun and Xie, Qizhe and Liu, Hanxiao and Yang, Yiming and Hovy, Eduard},
  booktitle={EMNLP},
  year={2017}
}
```

## Acknowledgement
* The code is adapted from Stanford AR https://github.com/danqi/rc-cnn-dailymail and GA https://github.com/bdhingra/ga-reader

## Contact
* Please contact Qizhe Xie (qzxie AT cs DOT cmu DOT edu) if you find bugs or missing info

## License
MIT
