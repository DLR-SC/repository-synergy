### Description

Right Whale Recognition

- [Competition page at Kaggle](https://kaggle.com/c/noaa-right-whale-recognition)
- [Video recording of presentation](https://youtu.be/WfuDrJA6JBE)

### Usage

These steps take about 6 hours on a system with 8 processors and an NVIDIA
Titan X GPU. **Tested only on Ubuntu**.

1. Download and install neon 1.1.4

    ```
    git clone https://github.com/NervanaSystems/neon.git
    cd neon
    git checkout e09fc11
    make
    source .venv/bin/activate
    ```
2. Install prerequisites

    ```
    pip install scipy scikit-image
    ```
3. Download the following files from [Kaggle](https://kaggle.com/c/noaa-right-whale-recognition/data):

    ```
    imgs.zip
    train.csv
    w_7489.jpg
    sample_submission.csv
    ```
    Save these to a directory that we will refer to as /path/to/data.
4. Clone this repository

    ```
    git clone https://github.com/anlthms/whale-2015.git
    cd whale-2015
    ```
5. Train models and generate predictions

    ```
    ./run.sh /path/to/data
    ```
6. Evaluate predictions

    Submit subm.csv.gz to [Kaggle](https://kaggle.com/c/noaa-right-whale-recognition/submissions/attach)

### Notes

- To run on a system that does not have a GPU:
```
    ./run.sh /path/to/data -bcpu
```
- For quicker results, decrease `imwidth` in run.sh.
- The script run.sh first prepares the data for training. If you want to repeat
the preparation step, delete the file /path/to/data/prepdone before invoking
run.sh again.
- If using a GPU, the results are non-deterministic regardless of how the
random number generator is seeded.
- The localizer uses a heuristic to determine when to stop training. If a good
optimum is not detected, a message that says "WARNING: model may not be
optimal" is displayed.
