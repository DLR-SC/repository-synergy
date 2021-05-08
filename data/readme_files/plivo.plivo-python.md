# plivo-python

[![Build Status](https://travis-ci.org/plivo/plivo-python.svg?branch=master)](https://travis-ci.org/plivo/plivo-python)
[![PyPI](https://img.shields.io/pypi/v/plivo.svg)](https://pypi.python.org/pypi/plivo)
[![PyPI](https://img.shields.io/pypi/pyversions/plivo.svg)](https://pypi.python.org/pypi/plivo)
[![PyPI](https://img.shields.io/pypi/l/plivo.svg)](https://pypi.python.org/pypi/plivo)


The Plivo Python SDK makes it simpler to integrate communications into your Python applications using the Plivo REST API. Using the SDK, you will be able to make voice calls, send SMS and generate Plivo XML to control your call flows.

## Installation
Install the SDK using [pip](http://www.pip-installer.org/en/latest/)

    pip install plivo

If you have the `0.11.3` version (a.k.a legacy) already installed, you will have to first uninstall it before installing the new version. `pip install --upgrade plivo` might not work depending on your system status.

Alternatively, you can download the source code from this repo(master branch) and run

    python setup.py install

For features in beta, use the beta branch:

    pip install plivo==4.2.0b1
    
Alternatively, you can download the source code from this repo(beta branch) and run

    python setup.py install

We recommend that you use [virtualenv](https://virtualenv.pypa.io/en/stable/) to manage and segregate your Python environments, instead of using `sudo` with your commands and overwriting dependencies.

## Getting started

### Authentication
To make the API requests, you need to create a `RestClient` and provide it with authentication credentials (which can be found at [https://manage.plivo.com/dashboard/](https://manage.plivo.com/dashboard/)).

We recommend that you store your credentials in the `PLIVO_AUTH_ID` and the `PLIVO_AUTH_TOKEN` environment variables, so as to avoid the possibility of accidentally committing them to source control. If you do this, you can initialise the client with no arguments and it will automatically fetch them from the environment variables:

```python
import plivo

client = plivo.RestClient()
```
Alternatively, you can specifiy the authentication credentials while initializing the `RestClient`.

```python
import plivo

client = plivo.RestClient(auth_id='your_auth_id', auth_token='your_auth_token')
```

If you expect to make a large number of API requests, re-use the same client instance, but if you expect to create a client on an on-demand basis, you can use a context manager to automatically frees all resources used by the client

```python
import plivo

with plivo.RestClient() as client:
  pass # Do something with the client
```

### The basics
The SDK uses consistent interfaces to create, retrieve, update, delete and list resources. The pattern followed is as follows:

```python
client.resources.create(*args, **kwargs) # Create
client.resources.get(id=resource_identifier) # Get
client.resources.update(id=resource_identifier, *args, **kwargs) # Update
client.resources.delete(id=resource_identifier) # Delete
client.resources.list() # List all resources, max 20 at a time
```

You can also use the `resource` directly to update and delete it. For example,

```python
resource = client.resources.get(id=resource_identifier)
resource.update(*args, **kwargs) # update the resource
resource.delete() # Delete the resource
```

Also, using `client.resources.list()` would list the first 20 resources by default (which is the first page, with `limit` as 20, and `offset` as 0). To get more, you will have to use `limit` and `offset` to get the second page of resources.

To list all resources, you can simply use the following pattern that will handle the pagination for you automatically, so you won't have to worry about passing the right `limit` and `offset` values.

```python
for resource in client.resources:
    print(resource.id)
```

## Examples

### Send a message

```python
import plivo

client = plivo.RestClient()
message_created = client.messages.create(
    src='the_source_number',
    dst='the_destination_number',
    text='Hello, world!'
)

```

### Make a call

```python
import plivo

client = plivo.RestClient()
call_made = client.calls.create(
    from_='the_from_number',
    to_='the_to_number',
    answer_url='https://answer.url'
)

```

### Generate Plivo XML

```python
from plivo import plivoxml

xml_response = plivoxml.ResponseElement()
xml_response.add_speak('Hello, world!') # or add(plivoxml.SpeakElement(text))

print(xml_response.to_string())
```

This generates the following XML:

```xml
<Response>
  <Speak>Hello, world!</Speak>
</Response>
```

### Run a PHLO

```python
import plivo

auth_id = 'Your AUTH ID'
auth_token = 'Your AUTH Token'
phlo_id = 'Your PHLO ID' # https://console.plivo.com/phlo/list/
phlo_client = plivo.phlo.RestClient(auth_id=auth_id, auth_token=auth_token)
phlo = phlo_client.phlo.get(phlo_id)
response = phlo.run()
print str(response)

```

### More examples
Refer to the [Plivo API Reference](https://api-reference.plivo.com/latest/python/introduction/overview) for more examples. Also refer to the [guide to setting up dev environment](https://developers.plivo.com/getting-started/setting-up-dev-environment/) on [Plivo Developers Portal](https://developers.plivo.com) to setup a Flask server & use it to test out your integration in under 5 minutes. to get started with Plivo.

## Reporting issues
Report any feedback or problems with this version by [opening an issue on Github](https://github.com/plivo/plivo-python/issues).
