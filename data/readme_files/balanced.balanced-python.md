# Balanced

Online Marketplace Payments

[![Build Status](https://secure.travis-ci.org/balanced/balanced-python.png?branch=master)](http://travis-ci.org/balanced/balanced-python) [![Latest Version](https://pypip.in/version/balanced/badge.svg)](https://pypi.python.org/pypi/balanced/) [![Downloads](https://pypip.in/download/balanced/badge.svg)](https://pypi.python.org/pypi/balanced/) [![Supported Python versions](https://pypip.in/py_versions/balanced/badge.svg)](https://pypi.python.org/pypi/balanced/) [![License](https://pypip.in/license/balanced/badge.svg)](https://pypi.python.org/pypi/balanced/)

**v1.x requires Balanced API 1.1. Use [v0.x](https://github.com/balanced/balanced-python/tree/rev0) for Balanced API 1.0.**

## Installation

    pip install balanced

## Usage

View Balanced's online tutorial and documentation at https://www.balancedpayments.com/docs/overview?language=python

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Write your code **and unit tests**
4. Ensure all tests still pass (`nosetests`)
5. [PEP8](http://pypi.python.org/pypi/pep8) your code
6. Commit your changes (`git commit -am 'Add some feature'`)
7. Push to the branch (`git push origin my-new-feature`)
8. Create new pull request


## Documentation scenarios

Each scenario lives in the scenarios directory and is comprised of the following:

- definition.mako - Method definition
- request.mako - Scenario code
- executable.py - Processed request.mako. Can be executed directly in Python. Generated by render_scenarios.py.
- python.mako - Documentation template to be consumed by balanced-docs. Generated by - render_scenarios.py.