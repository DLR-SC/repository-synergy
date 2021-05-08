# Collaborative RNN

This is a TensorFlow implementation of the Collaborative RNN presented in the
paper

> **Collaborative Recurrent Neural Networks for Dynamic Recommender Systems**,
> Young-Jun Ko, Lucas Maystre, Matthias Grossglauser, ACML, 2016.

A PDF of the paper can be found
[here](https://infoscience.epfl.ch/record/222477/files/ko101.pdf).

## Requirements

The code is tested with

- Python 2.7.12 and 3.5.1
- NumPy 1.13.3
- TensorFlow 1.4.0
- CUDA 8.0
- cuDNN 6.0
- six 1.11.0

If you are interested in quickly testing out our code, you might want to **check
out our [step-by-step guide][1]** for running the collaborative RNN on an AWS
EC2 p2.xlarge instance.

## Quickstart

Reproducing the results of the paper should be as easy as following these three
steps.

1. Download the datasets.
    - The last.fm dataset is available on [Òscar Celma's page][2]. The relevant
      file is `userid-timestamp-artid-artname-traid-traname.tsv`.
    - The BrighKite dataset is available at [SNAP][3]. The relevant file is
      `loc-brightkite_totalCheckins.txt`.
2. Preprocess the data (relabel user and items, remove degenerate cases, split
   into training and validation sets). This can be done using the script
   `utils/preprocess.py`. For example, for BrightKite:

        python utils/preprocess.py brightkite path/to/raw_file.txt

   This will create two files named `brightkite-train.txt` and
   `brightkite-valid.txt`.
3. Run `crnn.py` on the preprocessed data. For example for BrightKite, you
   might want to try running

        python -u crnn.py brightkite-{train,valid}.txt --hidden-size=32 \
            --learning-rate=0.0075 --rho=0.997 \
            --chunk-size=64 --batch-size=20 --num-epochs=25

Here is a table that summarizes the settings that gave us the results published
in the paper. All the setting can be passed as command line arguments to
`crnn.py`.

| Argument             | BrightKite | last.fm |
| -------------------- | ---------- | ------- |
| `--batch-size`       | 20         | 20      |
| `--chunk-size`       | 64         | 64      |
| `--hidden-size`      | 32         | 128     |
| `--learning-rate`    | 0.0075     | 0.01    |
| `--max-train-chunks` | *(None)*   | 80      |
| `--max-valid-chunks` | *(None)*   | 8       |
| `--num-epochs`       | 25         | 10      |
| `--rho`              | 0.997      | 0.997   |

On a modern server with an Nvidia Titan X (Maxwell generation) GPU it takes
around 40 seconds per epoch for the BrightKite dataset, and around 14 minutes
per epoch on the last.fm dataset.

[1]: docs/running-on-aws.md
[2]: http://www.dtic.upf.edu/~ocelma/MusicRecommendationDataset/lastfm-1K.html
[3]: https://snap.stanford.edu/data/loc-brightkite.html
