# Skater

Skater is a unified framework to enable Model Interpretation for all forms of model to help one build an Interpretable
machine learning system often needed for real world use-cases(** we are actively working towards to enabling faithful interpretability for all forms models). It is an open source python library designed to
demystify the learned structures of a black box model both globally(inference on the basis of a complete data set)
and locally(inference about an individual prediction).

The project was started as a research idea to find ways to enable better interpretability(preferably human interpretability) to predictive "black boxes" both for researchers and practioners. The project is still in beta phase.

## Install Skater

pip
~~~~
    Option 1: without rule lists and without deepinterpreter
    pip install -U skater

    Option 2: without rule lists and with deep-interpreter:
    1. Ubuntu: pip3 install --upgrade tensorflow (follow instructions at https://www.tensorflow.org/install/ for details and best practices)
    2. sudo pip install keras
    3. pip install -U skater==1.1.2

    Option 3: For everything included
    1. conda install gxx_linux-64
    2. Ubuntu: pip3 install --upgrade tensorflow (follow instructions https://www.tensorflow.org/install/ for
       details and best practices)
    3. sudo pip install keras
    4. sudo pip install -U --no-deps --force-reinstall --install-option="--rl=True" skater==1.1.2

~~~~

To get the latest changes try cloning the repo and use the below mentioned commands to get started,

~~~~

    1. conda install gxx_linux-64
    2. Ubuntu: pip3 install --upgrade tensorflow (follow instructions https://www.tensorflow.org/install/ for
       details and best practices)
    3. sudo pip install keras
    4. git clone the repo
    5. sudo python setup.py install --ostype=linux-ubuntu --rl=True

~~~~

## Testing

1. If repo is cloned:
    `python skater/tests/all_tests.py`
2. If pip installed:
    `python -c "from skater.tests.all_tests import run_tests; run_tests()"`


## Usage and Examples

See `examples` folder for usage examples.
