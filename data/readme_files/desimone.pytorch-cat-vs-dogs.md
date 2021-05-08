

Example of network fine-tuning in pytorch for the kaggle competition [Dogs vs. Cats Redux: Kernels Edition](https://www.kaggle.com/c/dogs-vs-cats-redux-kernels-edition/)

Currently #27 (`0.05074`) on the [leaderboard](https://www.kaggle.com/c/dogs-vs-cats-redux-kernels-edition/leaderboard). 

## Data prep work

```bash
    # unzip!
    unzip train.zip
    unzip test.zip
    # prep train directory and split train/trainval
    mv train/ catdog
    cd catdog
    # sanity check
    find . -type f -name 'cat*' | wc -l # 12500
    find . -type f -name 'dog*' | wc -l # 12500
    mkdir -p train/dog
    mkdir -p train/cat
    mkdir -p val/dog
    mkdir -p val/cat
    # Randomly move 90% into train and val, 
    # if reproducability is important you can pass in a source to shuf
    find . -name "cat*" -type f | shuf -n11250 | xargs -I file mv file train/cat/
    find . -maxdepth 1 -type f -name 'cat*'| xargs -I file mv file val/cat/
    # now dogs
    find . -name "dog*" -type f | shuf -n11250 | xargs -I file mv file train/dog/
    find . -maxdepth 1 -type f -name 'dog*'| xargs -I file mv file val/dog/

    # requires gnu utils (brew install coreutils)
    # use gmv instead of mv on osx
    echo cat*.jpg | xargs mv -t cat
    echo dog*.jpg | xargs mv -t dog
```


[See also](https://github.com/pytorch/examples)
