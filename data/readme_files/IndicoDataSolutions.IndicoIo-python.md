# indico: machine learning for human use
### A python client library for the [indico API](https://indico.io/).

![API Demo](http://i.imgur.com/47Fipms.gif)


Installation
--------------
From PyPI:
```bash
pip install indicoio
```

From source:
```bash
git clone https://github.com/IndicoDataSolutions/IndicoIo-python.git
python setup.py install
```

Running in a Docker container:
```
git clone https://github.com/IndicoDataSolutions/IndicoIo-python.git
docker build --build-arg INDICO_API_KEY=<Your Indico API key here> \
  -f Dockerfile.indicoio \
  -t indicoio
docker run -it indicoio bash
```

After building the Docker container, you can use only the last command to run the library unless you need to update the code.

Having trouble with installation? Missing system dependencies? Check out our [complete installation guide](https://indico.io/blog/getting-started-indico-tutorial-for-beginning-programmers/).


API Keys + Setup
----------------
Are you a student or researcher?  [Register here](https://indico.io/non-commercial) for free API credit.  
Interested in using indico for a commercial business?  [Sign up here](https://indico.io/enterprise).

Once you have an API key, setup is simple:

```python
import indicoio
indicoio.config.api_key = "YOUR_API_KEY_HERE"
```

![Setting your API key](http://i.imgur.com/Qcv8its.gif)


Full Documentation
------------
Detailed documentation and further code examples are available at [indico.io/docs](https://indico.io/docs).

![Happy hacking](http://i.imgur.com/W9ZcOe0.gif)
