# Features modified

* Ported to python3
* Added `to_dict` method on YouTrack objects

# YouTrack REST API Client Library for Python
This is a Python client library that you can use to access the REST API for JetBrains YouTrack. Previously, this repository also included command-line tools for importing issues from other issue trackers. We have created a [separate repository](https://github.com/JetBrains/youtrack-python-scripts) to store scripts that use this library.

The primary purpose of this library is to support migration to YouTrack, but you are welcome to build integrations with it as well. If you choose to work with this library, please be mindful of the following limitations:
- We don't provide any documentation for this library. You can either learn through trial and error or by dissecting the import scripts in the linked repository. 
- This library references an older version of the YouTrack REST API. Many of the newer features in YouTrack are not supported.

We will continue to support this library with updates that are required to support issue import. Other issues that are not import related may be closed.
Our intention is to eventually publish a fully-documented library that uses the latest version of the YouTrack REST API and is also compatible with Python 3.

## Compatibility
This client library and the import scripts that use the library are compatible with Python 2.7+. Python 3 releases are not supported.

This library supports YouTrack Standalone versions 5.x and higher as well as the current version of YouTrack InCloud. The REST API is enabled by default in all YouTrack installations.

## Getting Started
This package has been published to PyPI and can be installed with pip.
`pip install youtrack`

## Authentication
To communicate with YouTrack, you need a connection. 
- The preferred method is to use a permanent token for authentication requests. You can generate your own permanent tokens in your user profile. For instructions, refer to the [YouTrack documentation](https://www.jetbrains.com/help/youtrack/standalone/Manage-Permanent-Token.html#obtain-permanent-token).
- You can also authenticate using a login and password, however, these values are printed in plain text and expose your credentials in your client application.
```python
from youtrack.connection import Connection as YouTrack

# authentication request with permanent token
yt = YouTrack('https://instance_name.myjetbrains.com/youtrack/', token='perm:abcdefghijklmn')

# versus authentication with username and password
yt = YouTrack('https://instance_name.myjetbrains.com/youtrack/', login='username', password='password')
```
This request requires that you specify the base URL of the target YouTrack server. For YouTrack InCloud instances, your base URL includes the trailing `/youtrack`, as shown in the previous example.

Once you have established a connection, your credentials are cached for subsequent requests.

## Supported Operations
Most of the operations that are supported by the YouTrack REST API are mapped to methods for the `Connection` object. The Python client library, however, supports a simplified set of parameters. In some cases, like `createIssue`, the Python method supports a custom set of request parameters.

To learn more about the YouTrack REST API, refer to the [YouTrack documentation](https://www.jetbrains.com/help/youtrack/standalone/rest-api-reference.html).

## YouTrack Support
Your feedback is always appreciated.
- To report bugs and request updates, please [create an issue](http://youtrack.jetbrains.com/issues/JT#newissue=yes).
- If you experience problems with an import script, please [submit a support request](https://youtrack-support.jetbrains.com/hc/en-us).
