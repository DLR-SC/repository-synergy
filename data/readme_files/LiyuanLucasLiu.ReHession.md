# Heterogeneous Supervision for Relation Extraction: A Representation Learning Approach

Source code and data for [Heterogeneous Supervision for Relation Extraction: A Representation Learning Approach](https://arxiv.org/abs/1707.00166)

<p align="center"><img width="100%" src="docs/frameWork.png"/></p>

--------------------------------------------------------------------------------

ReHession conducts Relation Extraction with Heterogeneous Supervision, e.g., the labeling functions at left corner.

ReHession conducts Relation Extraction, featuring:
- employ heterogeneous supervision, e.g., knowledge base and heuristic patterns, to train the model (as picked in left corner)
- infers true label from noisy labels in a context-aware manner
- true label discovery and relation extraction can mutually enhance each other

# Quick Start
A demo is provided and can be execurated by:
```
bash demo_KBP.sh
```

# Details

This Project are in an early-release beta. Expect some adventures...

- [Overview](#pipeline-overview)
- [Data](#data)
	- [Corpus](#corpus)
	- [Patterns](#patterns)
	- [Knowledge base](#knowledge-base)
- [Labeling Functions](#labeling-functions)
	- [KB based labeling functions](#kb-based)
	- [Pattern based labeling functions](#pattern-based)
	- [Inverse labeling functions](#inverse)
	- [Processing KBP Dataset](#kbp-dataset)
- [Feature Extraction](#feature-extraction)
- [Model Learning and Evaluation](#model-learning-and-evaluation)
	- [encoding](#encoding)
	- [compile](#compile)
	- [execute](#execute)
- [Reference](#reference)

## Pipeline Overview

And the pipeline of ReHession is:
- recognize entities for labeling functions
- apply labeling functions to get heterogeneous supervision
- generate pos-tagging and brown clustering
- encoding training / testing corpus
- training and evaluation

## Data

We include corpus, labeling functions and knowledge base in the Data folder.

### Corpus
We stored KBP[1] corpus under the path `Data/source/KBP/corpus.txt.zip`, and  NYT[2] corpus under the folder `Data/source/NYT/corpus.txt.zip`. Pos-tagging and entity detection has been conducted by Stanford NER tools.

### Patterns
We stored the pattern-based labeling functions in the folder of the corpus, named `nlf.json`. These files stored one pattern-based labeling function at one line in the json format.

### Knowledge base
We stored the annotations generated by KB-based labeling functions in the folder of the corpus, named `train.json`. It's also used as the training file adopted by [CoType](https://github.com/shanzhenren/CoType)

## Labeling Functions
We adopted three kinds of labeling functions in ReHession: KB-based, pattern-based and inversed. And the annotations generated by those labeling functions are save in the path `Data/intermediate/`.

### KB based
KB based labeling functions are adopted to encode information of KB. Accordingly, we adopted the training file generated by distant supervision, by treating annotations of the same relation type are generated by the same labeling function (in the form of `if r(e1, e2) in KB: return r`).

### Pattern based 
Pattern-based labeling functions would annotate entity pairs with matched entity type and texture pattern with preset relation types. And each pattern-based labeling functions (as stored in `nlf.json`) has the following fields:
- reserved: whether entity 1 is before entity 2
- PID: pattern id
- rule: the rule of matching multiple entities
- Texture: texture pattern
- relationType: the detected type of this labeling function
- Type1: the type of entity 1 
- Type2: the type of entity 2

The rule field has value in the format of `[a,b]`, while a and b can be any number or `n`. It indicates how many entities would the labeling function try to match (`n` indicates matching all entities). For example, `{"reserved": "1", "PID": 0, "rule": ["1", "1"], "Texture": "founder of", "relationType": "/business/company/founders", "Type1": "ORGANIZATION", "Type2": "PERSON"}` requires the entity before texture pattern (indicated by `reserved`) to be Person (indicated by `Type2`), and entity after texture pattern to be ORGANIZATION (indicated by `Type1`). Also this labeling function would only annotate the entity pair most close to the texture pattern (indicated by `["1", "1"]`)

### Inverse 
In order to annotate `None` type, we designed another type of labeling function, i.e., if a set of labeling functions not annotate a instance, it would annotate it as `None`.

Specifically, for KBP dataset, we adopted a reverse labeling function who reserved all pattern-based labeling functions; for NYT dataset, a reverse labeling function reserving all kb-based labeling functions is adopted. 

### KBP Dataset
We now proceed to use KBP dataset as an example (also save as labelGeneration.sh) to demonstrate the pipeline of generating heterogeneous supervision.
```
python LabelGeneration/UIDExtractKB.py
python LabelGeneration/post_process_chunked_corpus.py
python LabelGeneration/applying_labelling_func.py --save_all
python LabelGeneration/applying_KB.py
python LabelGeneration/reCodeFuncs.py
python LabelGeneration/MergeLFS.py
python LabelGeneration/cal_Mention_Distance.py
python LabelGeneration/applyingInverse.py
```
These commands requires original data to be stored in `Data/source/KBP/`, while the specific requirements are stored in the default setting. 

## Feature Extraction
We provided the training files used in our experiments, which is saved in the path `Data/intermediate/`. Also we wrote a demo scripts for the whole feature extraction, model learning and evaluation pipeline. You can simply execute it by
```
bash demo_KBP.sh
```

With dataset with annotation and brown clustering file stored in the path `Data/intermediate/KBP/`, the feature extraction can be performed by
```
python DataProcessor/relation_feature_generation.py
```

## Model Learning and Evaluation

### Encoding

The model is designed to run on encoded training / evaluation / testing corpus. Each line in the encoded file is an instance, which is in the format of 
```
InsID	FeatureNum	AnnotationNum	FeatureList	AnnotationList
```
InsID, FeatureNum and AnnotationNum are integers; FeatureList is in the format of `featureId,featureId`; AnnotationList is in the format of `lfId typeId`. For example, an instance in KBP dataset is like:
```
10      78      2       457984,153472,646018,120323,1119382,739279,152889,199945,1146378,1077643,1138574,501136,1091345,55555,65558,1125465,131097,947866,1128477,869918,485663,289,201307,1066993,359723,681233,767278,1053381,1019443,742453,324534,570977,244,1059642,434747,267324,99135,376075,815283,84805,382022,1119585,1107934,43594,43595,809036,676557,749903,485662,78163,297812,43278,95417,1092708,673498,538331,218205,977502,189791,991328,380641,354658,1030244,1173222,492263,209340,520684,379757,335215,409201,786164,835966,21497,16250,872059,562651,137214,498815        6,10,6,9
```

### Compile

Run `make` under the folder of `Model` would compile the model

### Execute

The Execute commands for KBP dataset and NYT dataset are:
```
./Model/ReHession -train ./Data/intermediate/KBP/train.data -test ./Data/intermediate/KBP/test.data -none_idx 6 -instances 225977 -test_instances 2111
./Model/ReHession -train ./Data/intermediate/NYT/train.data -test ./Data/intermediate/NYT/test.data -none_idx 0 -instances 530767 -test_instances 3803
```

## Reference

Please cite the following paper if you find the codes and datasets useful:
```
@inproceedings{Liu2017rehession,
 title={Heterogeneous Supervision for Relation Extraction: A Representation Learning Approach},
 author={Liu, Liyuan and Ren, Xiang and Zhu, Qi and Zhi, Shi and Gui, Huan and Ji, Heng and Han, Jiawei},
 booktitle={Proc. EMNLP},
 year={2017}
}
```