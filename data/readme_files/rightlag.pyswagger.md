# pyswagger [![Build Status](https://img.shields.io/travis/rightlag/pyswagger/master.svg?style=flat-square)](https://travis-ci.org/rightlag/pyswagger) [![Gitter](https://img.shields.io/gitter/room/nwjs/nw.js.svg?style=flat-square)](https://gitter.im/rightlag/pyswagger)

pyswagger 0.2.0

Released: 7-Jan-2016

# Release Notes

  - **Release 0.2.0**
    - Support for both token-based and HTTP basic authentication (e.g. `apiKey`, `basic`)
    - Support for Swagger schema specifications to be read from hosted sites instead of reading them from local device
    - Scheme is automatically assigned if not passed as an argument when issuing requests (e.g. `http`, `https`, `ws`, `wss`)
    - Minor bug fixes

  - **Release 0.1.0**
    - Reads Swagger schema specifications
    - Creates a `client` object used to instantiate requests to paths defined in the schema
    - Supports `apiKey` authentication
    - Supports common request methods (e.g. `GET`, `POST`, `PUT`, and `DELETE`)

  - **Roadmap**
    - `$ref` support
    - Automatically determine MIME type for content-negotiation if not specified when issuing requests
    - ~~Support for OAuth~~

# Introduction

pyswagger is a Python toolkit that reads any JSON formatted [Swagger](http://swagger.io/) (Open API) schema and generates methods for the [operations](http://swagger.io/specification/#operationObject) defined in the schema.

# Quickstart

To use the pyswagger client, import the `Swagger` class from the `swagger` module. The following example uses the [Swagger Petstore](http://petstore.swagger.io/) API.

```python
>>> from swagger import Swagger
>>> client = Swagger.load('http://petstore.swagger.io/v2/swagger.json')
>>> res = client.get('/pet/findByStatus', status='sold')
>>> print res.json()
[{u'category': {u'id': 1, u'name': u'Dogs'}, u'status': u'sold', u'name': u'Dog 2', u'tags': [{u'id': 1, u'name': u'tag2'}, {u'id': 2, u'name': u'tag3'}], u'photoUrls': [u'url1', u'url2'], u'id': 5}]
```

This returns a list of `Pet` objects whose `status` attribute is assigned `sold`.

The `load()` method requires a URL to where the schema exists. The schema **must** be JSON formatted. In this example, the petstore schema is being loaded via a HTTP GET request and is then deserialized.

The `status` keyword argument is located within the list of parameters of the `/pet/findByStatus` path in the `petstore.json` schema.

# Query parameters

Endpoints that accept optional or required query parameters can be passed as keyword arguments to the method call.

# Endpoints containing IDs

For endpoints that contain IDs (e.g. `/pet/2`), pyswagger uses string interpolation to match the ID with the respective keyword argument. The following example simulates a `GET` request that will return a pet with ID `2`:

```python
from swagger import Swagger
>>> client = Swagger.load('http://petstore.swagger.io/v2/swagger.json')
>>> res = client.get('/pet/{petId}', petId=2)
>>> print res.json()
{u'category': {u'id': 2, u'name': u'Cats'}, u'status': u'available', u'name': u'Cat 2', u'tags': [{u'id': 1, u'name': u'tag2'}, {u'id': 2, u'name': u'tag3'}], u'photoUrls': [u'url1', u'url2'], u'id': 2}
```

The `{petId}` placeholder is matched in the endpoint string and is replaced with the value of the `petId` keyword argument.

# Requests containing a payload

For requests that require a request payload, the `body` keyword argument can be passed as an argument to the method. The value of the `body` argument *should* be [serialized](https://en.wikipedia.org/wiki/Serialization). The following example simulates a `POST` request that will create a new pet:

```python
>>> import json
>>> from swagger import Swagger
>>> data = {
...     'id': 0,
...     'category': {
...         'id': 0,
...         'name': 'string',
...     },
...     'name': 'doggie',
...     'photoUrls': [
...         'string',
...     ],
...     'tags': [
...         {
...             'id': 0,
...             'name': 'string',
...         }
...     ],
...     'status': 'available',
... }
>>> data = json.dumps(data)
>>> client = Swagger.load('http://petstore.swagger.io/v2/swagger.json')
>>> res = client.post('/pet', body=data, auth='special-key')
>>> print res.status_code, res.reason
200 OK
```

**Note:** Some endpoints do not return a response body. Therefore, invoking the `.json()` method on the response object will raise an exception.

The example above  also includes the `auth` keyword argument which is explained in further detail in the next section.

# Authenticated endpoints

Authentication is sometimes required to access some or all endpoints of a web API. Since pyswagger is a client-side toolkit, it does not support authentication schemes such as [OAuth](https://en.wikipedia.org/wiki/OAuth). However, if the endpoint requires an access token to make a request, then the `auth` keyword argument can be supplied.

## Using the `auth` keyword argument

Swagger uses [Security Definitions](http://swagger.io/specification/#securityDefinitionsObject) to define security schemes available to be used in the specification. For [token-based authentication](https://scotch.io/tutorials/the-ins-and-outs-of-token-based-authentication), The `in` field states the location of the API key which is either the `query` or the `header`. For [HTTP Basic Authentication](https://en.wikipedia.org/wiki/Basic_access_authentication), the `in` keyword is *not* defined.

If a token-based authentication security definition exists in the schema, pyswagger inspects the value of the `in` field and automatically assigns it as a request header or a query parameter. Therefore, when using the `auth` keyword, it is not required to specify the location of the API key.

**Token authentication**

To use token authentication, the `auth` keyword argument *should* be of type `str`.

```python
>>> from swagger import Swagger
>>> client = Swagger.load('http://petstore.swagger.io/v2/swagger.json')
>>> res = client.get('/pet/{petId}', petId=2, auth='special-token')
```

**HTTP basic authentication**

To use HTTP basic authentication, the `auth` keyword argument *should* be of type `tuple`.

```python
>>> from swagger import Swagger
>>> client = Swagger.load('http://petstore.swagger.io/v2/swagger.json')
>>> res = client.get('/pet/{petId}', petId=2, auth=('username', 'password'))
```
