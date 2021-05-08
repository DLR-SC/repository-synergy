iOS-Python-Project
==================

An example of developing iOS apps in Python.

In progress. It seems to be quite a lot of work, please help develop this project.

Develop
-------

- `/app` is the root of Python source code.
- `/app/uikit` is a wrapper of UIKit in Python, aiming to provide a flexible app framework
- `/app/myapp` is an example of an iOS app that builds on top of `uikit`, including examples to
[show a UITableView](https://github.com/clowwindy/iOS-Python-Project/blob/master/app/myapp/ui.py)
and [run a web server with tornado](https://github.com/clowwindy/iOS-Python-Project/blob/master/app/myapp/web.py)
- This project is based on [Python-iOS-template](https://github.com/pybee/Python-iOS-template) and [rubicon-objc](https://github.com/pybee/rubicon-objc)

Todo
----

- Make proper wrapper for classes in uikit
- Provide a helper to run code in the main thread from other threads
