
# NER-LSTM-CNNs-CRF  #
- LSTM-CNNs-CRF impolment in pytorch, and test in conll2003 dataset, reference [End-to-end Sequence Labeling via Bi-directional LSTM-CNNs-CRF](http://www.aclweb.org/anthology/P/P16/P16-1101.pdf).

- PyTorch0.3.1 Code release on here. [[PyTorch0.3.1](https://github.com/bamtercelboo/pytorch_NER_BiLSTM_CNN_CRF/releases/tag/PyTorch0.3.1)]  

## Requirement ##

	PyTorch: 1.0.1
	Python: 3.6
	Cuda: 8.0 or 9.0(support cuda speed up, can chose)



## Usage ##
	modify the config file, detail see the Config directory
	Train:
		The best nn model will be saved during training.
		---> sh run_train_p.sh
	Test:
		Train finished. Decoding test data, and write decode result to file.
		---> sh run_test.sh
	Eval:
		For the decode result file, use conlleval script in Tools directory to calculate F-score.
		---> sh run_eval.sh  

## Config ##
	[Embed]
		pretrained_embed = True（default: False）
		nnembed = True
		pretrained_embed_file = embed file path
	[Data]
		max_count = -1  ## Number of sentences loaded(-1 represents all)
	[Save]
		save_pkl = True(save pkl file for test, default True)
		save_best_model = True(save best performance result for test, default True)
	[Model]
		use_crf = True  ## CRF 
		use_char = True  ## CNN
		model_bilstm = True  ##BiLSTM
		embed_dim = 100, lstm_hiddens = 200
		dropout_emb = 0.5, dropout = 0.5
		max_char_len = 20, char_dim = 30, conv_filter_sizes = 3, conv_filter_nums = 30
	[Optimizer]
		sgd = True
		learning_rate = 0.015 , weight_decay = 1.0e-8
		use_lr_decay = True, lr_rate_decay = 0.05, min_lrate = 0.000005, max_patience = 1
	[Train]
		batch_size = 10
		early_max_patience = 10(early stop max patience)

This is a major configuration file description, for more detailed reference to config.cfg file and [config readme](https://github.com/bamtercelboo/pytorch_NER_BiLSTM_CNN_CRF/tree/master/Config).

## Model ##

- `BiLSTM`  
	- `CNN`
	-  `CRF`

## Data ##

- The number of sentences:  

| Data | Train | Dev | Test |  
| ------------ | ------------ | ------------ | ------------ |  
| conll2003 | 14987 | 3466 | 3684 |


- The Data format is `BIES` label, data sample in Data directory.

- Tag convert scripr in Here [[tagSchemeConverter.py](https://github.com/bamtercelboo/pytorch_NER_BiLSTM_CNN_CRF/blob/master/DataUtils/tagSchemeConverter.py)]  

- Conll2003 dataset can be downloaded from [Conll2003](https://www.clips.uantwerpen.be/conll2003/ner/)

- Pre-Trained Embedding can be downloaded from [glove.6B.zip](nlp.stanford.edu/data/glove.6B.zip)  

## Performance ##

- Performance on the `Conll2003`,  eval on the script `conlleval` in [Tools](https://github.com/bamtercelboo/pytorch_NER_BiLSTM_CNN_CRF/tree/master/Tools)  

- log in [final_log](https://github.com/bamtercelboo/pytorch_NER_BiLSTM_CNN_CRF/tree/master/final_log)  

| Model | % P | % R | % F1 |  
| ------------ | ------------ | ------------ | ------------ |  
| BLSTM | 88.61 | 88.50 | 88.56 |  
| BLSTM-CRF | 90.33 | 88.81 | 89.56 |  
| BLSTM-CNN | 89.23 | 90.97 | 90.09 |  
| BLSTM-CNN-CRF | 91.42 | 91.24 | 91.33 |  


## Reference ##
- [Ma X, and Hovy E. End-to-end Sequence Labeling via Bi-directional LSTM-CNNs-CRF. ACL, 2016](http://www.aclweb.org/anthology/P/P16/P16-1101.pdf)  
- https://github.com/jiesutd/NCRFpp  
- https://github.com/liu-nlper/SLTK  


## Question ##

- if you have any question, you can open a issue or email **bamtercelboo@{gmail.com, 163.com}**.

- if you have any good suggestions, you can PR or email me.
