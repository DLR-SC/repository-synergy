![Clarifai logo](docs/logo.png)

# Clarifai API Python Client

This is the official Python client for interacting with our powerful recognition [API](https://docs.clarifai.com).
The Clarifai API offers image and video recognition as a service. Whether you have one image or billions,
you are only steps away from using artificial intelligence to recognize your visual content.

* Try the Clarifai demo at: https://clarifai.com/demo
* Sign up for a free account at: https://clarifai.com/developer/account/signup/
* Read the developer guide at: https://clarifai.com/developer/guide/


[![PyPi version](https://pypip.in/v/clarifai/badge.png)](https://pypi.python.org/pypi/clarifai)
[![Build Status](https://travis-ci.org/Clarifai/clarifai-python.svg?branch=master)](https://travis-ci.org/Clarifai/clarifai-python)


## Installation
Install the API client:
```
pip install clarifai --upgrade
```

> Note: If you cannot use `pip`, you can download the latest
[release](https://github.com/Clarifai/clarifai-python/releases) manually or using git.

## Setup
Firstly, generate your Clarifai API key [on the API keys page](https://clarifai.com/developer/account/keys). The client
uses it for authentication.

Then, to authenticate, either:
- initialize the `ClarifaiApp` with your API key
    ```python
    from clarifai.rest import ClarifaiApp
    app = ClarifaiApp(api_key='YOUR_API_KEY')
    ```
- or set the environment variable named `CLARIFAI_API_KEY`
- or run the script `./scripts/clarifai config` which will, after you input the API key, create a
file `~/.clarifai/config` with your key


> Note: If you have both the environmental variable CLARIFAI_API_KEY and a file `~/.clarifai/config`, the environmental
  variable will be used.

For AWS or Windows users, please refer to
[the documentation](https://clarifai-python.readthedocs.io/en/latest/install/#aws-lambda-users) for more instructions.


## Getting Started
The following example will setup the client and predict concepts on an image from a URL, using the general model
```python
from clarifai.rest import ClarifaiApp

app = ClarifaiApp()
model = app.public_models.general_model
response = model.predict_by_url(url='https://samples.clarifai.com/metro-north.jpg')
```

Use `model.predict_by_filename` to predict concepts on a local file.

The response is a JSON structure. Here's how to print all the predicted concepts associated with the image, together
with their confidence values.

```python
concepts = response['outputs'][0]['data']['concepts']
for concept in concepts:
    print(concept['name'], concept['value'])
```

## Documentation
See many more code examples [in the developer guide](https://clarifai.com/developer/guide/) and in the
[Python client tutorial](https://clarifai-python.readthedocs.io/en/latest/).

Also see [the Python client reference](https://clarifai-python.readthedocs.io/en/latest/clarifai.rest/).
