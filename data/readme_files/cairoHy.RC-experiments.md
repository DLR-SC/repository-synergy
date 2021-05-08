# Reading Comprehension Experiments

## About

This is the tensorflow version implementation/reproduce of some reading comprehension models in some reading comprehension datasets including the following:

Models:

- Attention Sum Reader model as presented in "Text Comprehension with the Attention Sum Reader Network" (ACL2016) available at [http://arxiv.org/abs/1603.01547](http://arxiv.org/abs/1603.01547). 

![](http://7xpqrs.com1.z0.glb.clouddn.com/FjmgZjrmBJ5w8WdDU2v9BMRj21r8)

- Attention over Attention Reader model as presented in "Attention-over-Attention Neural Networks for Reading Comprehension" (arXiv2016.7) available at https://arxiv.org/abs/1607.04423.

![](http://7xpqrs.com1.z0.glb.clouddn.com/FupB-rvxCvGvPTwa8UC4u3QUgqKI)

Datasets:

- CBT, Children’s Book Test.http://lanl.arxiv.org/pdf/1506.03340.pdf

## Start To Use

#### 1.Clone the code

```shell
git clone https://github.com/zhanghaoyu1993/RC-experiments.git
```



#### 2.Get needed data

- Download and extract the dataset used in this repo.

```shell
cd data
./prepare-all.sh
```



#### 3.Environment Preparation

- Python-64bit >= v3.5.
- Install require libraries using the following command.

```shell
pip install -r requirements.txt
```

- Install tensorflow >= 1.1.0.

```shell
pip install tensorflow-gpu --upgrade
```

- Install nltk punkt for tokenizer.

```shell
python -m nltk.downloader punkt
```



#### 4.Set model, dataset and other command parameters

- What is the entrance of the program?

The main.py file in root directory.

- How can I specify a model in command line?

Type a command like above, the *model_class* is the class name of model, usually named in cambak-style:

```shell
python main.py [model_class]
```

For example, if you want to use AttentionSumReader:

```shell
python main.py AttentionSumReader
```

- How can I specify the dataset?

Type a command like above, the *dataset_class* is the class name of dataset:

```shell
python main.py [model_class] --dataset [dataset_class]
```

For example, if you want to use CBT:

```shell
python main.py [model_class] --dataset CBT
```

You don't need to specify the data_root and train valid test file name in most cases, just specify the dataset.

- How can I know all the parameters?

The program use [argparse](https://docs.python.org/3/library/argparse.html) to deal with parameters, you can type the following command to get help:

```shell
python main.py --help
```

or:

```shell
python main.py -h
```

- The command parameters is so long!

The parameters will be stored into a file named args.json when executed, so next time you can type the following simplified command:

```shell
python main.py [model_class] --args_file [args.json]
```



#### 5.Train and test the model

First, modify the parameters in the args.json.

You can now train and test the model by entering the following commands. The params in [] should be determined by the real situation.

- Train:

```shell
python main.py [model_class] --args_file [args.json] --train 1 --test 0 
```

After train, the parameters are stored in `weight_path/args.json`  and the model checkpoints are stored in `weight_path`.

- Test:

```shell
python main.py [model_class] --args_file [args.json] --train 0 --test 1 
```

After test, the performance of model are stored in `weight_path/result.json`.



#### 6.model performance

All the trained results and corresponding config params are saved in sub directories of weight_path(by default the `weight` folder) named `args.json` and `result.json`.

You should know that the implementation of some models are **slightly different** from the original, but the basic ideas are same, so the results are for reference only.

The best results of implemented models are listed below:

- best result **we achieve**(with little hyper-parameter tune in single model) 
- best result listed in original paper(in the brackets)

|            | CBT-NE      | CBT-CN      |
| ---------- | ----------- | ----------- |
| AS-Reader  | 69.88(68.6) | 65.0(63.4)  |
| AoA-Reader | 71.0(72.0)  | 68.12(69.4) |



#### 7.FAQ

- How do I use args_file argument in the shell?

Once you enter a command in the shell(maybe a long one), the config will be stored in weight_path/args.json where weight_path is defined by another argument, after the command execute you can use --args.json to simplify the following command:
```shell
python main.py [model_class] --args_file [args.json]
```
And the priorities of arguments typed in the command line is higher than those stored in args.json, so you can change some arguments.