## Keras-rest-server: A simple rest implementation for loading and serving keras models
------------------
## About:
This repository contains a very simple server implemented in flask which loads a
a simple neural network model trained using Keras from its saved-weights and
model.

In this example a very simple case of XOR is considered.
## Getting started:
---
1. Install Anaconda:
```
https://docs.continuum.io/anaconda/install
```

2. Clone this repository
```
git clone https://github.com/ansrivas/keras-rest-server.git
cd keras-rest-server
```

3. Create a new environment ( Change python=2 or python=3) and activate it:
```
conda create --name keras-server -y python=2
source activate keras-server
```

4. Install all the dependencies:
```
conda env update -n keras-server  --file requirements.txt
```

5. To remove the environment run:
```
conda remove -n keras-server --all -y
```

### Usage
------------------

### Run to generate pickle files:
```
python createpickles.py
```

### Run the server (defaults to http://localhost:7171)
```
python server.py
```

### Send a post request to this server to test your model
```
python client.py
```
