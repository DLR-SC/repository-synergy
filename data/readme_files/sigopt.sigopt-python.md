[![Build Status](https://circleci.com/gh/sigopt/sigopt-python.svg?style=svg)](https://circleci.com/gh/sigopt/sigopt-python)

# SigOpt Python API

This is the [SigOpt](https://sigopt.com) Python API client.
Use this to natively call SigOpt API endpoints to create experiments and report data.

For more help getting started with SigOpt and Python, check out the [docs](https://sigopt.com/docs/overview/python).

Take a look in `examples` for example usage.

## Getting Started

Install the sigopt python modules with `pip install sigopt`.

Sign up for an account at [https://sigopt.com](https://sigopt.com).
In order to use the API, you'll need your API token from the [API tokens page](https://sigopt.com/tokens).

To call the API, instantiate a connection with your token.

### Authentication
Authenticate each connection with your API token directly (will override any token set via environment variable):
```python
from sigopt import Connection
conn = Connection(client_token=api_token)
```

### Authentication with Environment Variable
Insert your API token into the environment variable `SIGOPT_API_TOKEN`, and instantiate a connection:

```python
from sigopt import Connection
conn = Connection()
```


## Issuing Requests
Then, you can use the connection to issue API requests. An example creating an experiment and running the
optimization loop:

```python
from sigopt import Connection
from sigopt.examples import franke_function
conn = Connection(client_token=SIGOPT_API_TOKEN)

experiment = conn.experiments().create(
  name='Franke Optimization',
  parameters=[
    dict(name='x', type='double', bounds=dict(min=0.0, max=1.0)),
    dict(name='y', type='double', bounds=dict(min=0.0, max=1.0)),
  ],
)
print("Created experiment: https://sigopt.com/experiment/" + experiment.id);

# Evaluate your model with the suggested parameter assignments
# Franke function - http://www.sfu.ca/~ssurjano/franke2d.html
def evaluate_model(assignments):
  return franke_function(assignments['x'], assignments['y'])

# Run the Optimization Loop between 10x - 20x the number of parameters
for _ in range(20):
  suggestion = conn.experiments(experiment.id).suggestions().create()
  value = evaluate_model(suggestion.assignments)
  conn.experiments(experiment.id).observations().create(
    suggestion=suggestion.id,
    value=value,
  )
```

## API Token

Your API token does not have permission to view or modify information about individual user accounts,
so it is safe to include when running SigOpt in production.

## Endpoints

Endpoints are grouped by objects on the `Connection`.
For example, endpoints that interact with experiments are under `conn.experiments`.
`ENDPOINT_GROUP(ID)` operates on a single object, while `ENDPOINT_GROUP()` will operate on multiple objects.

`POST`, `GET`, `PUT` and `DELETE` translate to the method calls `create`, `fetch`, `update` and `delete`.
To retrieve an experiment, call `conn.experiments(ID).fetch()`. To create an experiment call
`conn.experiments(ID).create()`. Parameters are passed to the API as named arguments.

Just like in the resource urls, `suggestions` and `observations` are under `experiments`.
Access these objects with `conn.experiments(ID).suggestions` and `conn.experiments(ID).observations`.
The REST endpoint `POST /v1/experiments/1/suggestions` then translates to `conn.experiments(ID).suggestions().create()`.

## Testing

To run the included tests, just run

```bash
pip install -r requirements-dev.txt
make test
```

To lint, install requirements (included in the previous step) and run
```bash
make lint
```
