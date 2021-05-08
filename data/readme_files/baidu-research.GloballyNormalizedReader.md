# Globally Normalized Reader

This repository contains the code used in the following paper:

[Jonathan Raiman and John Miller. Globally Normalized Reader. Empirical Methods in Natural Language Processing (EMNLP), 2017.](https://www.aclweb.org/anthology/D17-1112)

If you use the dataset/code in your research, please cite the above paper:

    @inproceedings{raiman2015gnr,
        author={Raiman, Jonathan and Miller, John},
        booktitle={Empirical Methods in Natural Language Processing (EMNLP)},
        title={Globally Normalized Reader},
        year={2017},
    }

Note: This repository is a reimplementation of the original used for the above paper. The original used a batch size of 32 and synchronous-SGD across multiple GPUs. However, this code currently only runs on a single GPU and will split a batch that runs out of memory into several smaller batches. For this reason, the code does not exactly reproduce the results in that paper (but it should be <2% off). Work is underway to rectify this issue.

## Usage (TensorFlow)

### Prerequisites
You must have installed and available the following libraries:

- CUDA 8.0.61 or higher, with appropriate drivers installed for the available GPUs.
- CuDNN v6.0 or higher.

Make sure you know where the aforementioned libraries are located on your system; you will need to adjust the paths you use to point to them.

### Set-Up

1. Set up your environment variables
    ```bash
    # Copy this into ~/.zshrc or ~/.bashrc for regular use.
    source env.sh
    ```
    If you are not running on the SVAIL cluster, you will need to change these variables.

2. Create your virtual environment:

    ```bash
    python3.6 -m venv env
    ```
    Python 3.6 must be on your command-line `PATH`, which is set up automatically by `env.sh` above.

3. Activate your virtual environment:

    ```bash
    # You will need to do this every time you use the GNR
    source env/bin/activate
    ```

4. Install `numpy`, separately from the other packages
    ```bash
    pip install numpy
    ```

5. Install all dependencies from `requirements.txt`
    ```bash
    pip install -r requirements.txt
    ```

### Data
Before training the Globally Normalized Reader, you need to download and featurize the dataset.

1. Download all the necessary data:
    ```bash
    cd data && ./download.sh && cd ..
    GLOVE_PATH=data/glove.txt
    wget http://nlp.stanford.edu/data/glove.840B.300d.zip -O $GLOVE_PATH
    ```

2. Featurize all of the data:
    ```bash
    python featurize.py --datadir data --outdir featurized  --glove-path $GLOVE_PATH
    ```

### Training

1. Create a new model:
    ```bash
    python main.py create --name default --vocab-path featurized/
    ```

2. Train the model:
    ```bash
    python main.py train --name default --data featurized/
    ```

### Evaluation

1. Evaluate the model:
    ```bash
    python main.py predict --name default --data data/dev.json --vocab-path featurized/ --output predictions.txt
    ```

## Usage (PaddlePaddle)

1. Install the latest GPU-compatible PaddlePaddle Docker image, as directed on [the PaddlePaddle website](http://www.paddlepaddle.org/).
2. To print the model configuration as text, use `paddle_model.py`.
3. To train the model, use `paddle_train.py`.
4. To run inference the model, use `paddle_infer.py`.
