cfn\_resource.py
----------------

This project is a decorator and validation system that takes the
drudgery out of writing custom resources. You still have access to the
context and event as normal, but the decorator handles serializing your
response and communicating results to CloudFormation.

See `cfn-lambda <https://github.com/andrew-templeton/cfn-lambda>`__ from
Andrew Templeton if you're looking to write your custom resources in
Node.js.

Usage
-----

1. Copy ``cfn_resource.py`` into the directory of your lambda function
   handler.py
2. Use the ``cfn_resource.Resource`` event decorators to decorate your
   handler like in ``example.py``
3. Zip up the contents and upload to Lambda

Once the function is up, copy its ARN and use it as the ServiceToken for
your `custom
resource <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cfn-customresource.html>`__.
For more on the requests you may receive, see `this
document <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/crpg-ref-requests.html>`__

.. code-block:: json

    {
        "AWSTemplateFormatVersion": "2010-09-09",
        "Resources": {
            "FakeThing": {
                "Type": "Custom::MyResource",
                "Properties": {
                    "ServiceToken": "arn:aws:lambda:SOME-REGION:ACCOUNT:function:FunctionName",
                    "OtherThing": "foobar",
                    "AnotherThing": 2
                }
            }
        }
    }

For more on how custom resources work, see the `AWS
docs <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-custom-resources.html>`__

Code Sample
-----------

For this example, you need to have your handler in Lambda set as
``filename.handler`` where filename has the below contents.

.. code-block:: python

    import cfn_resource

    # set `handler` as the entry point for Lambda
    handler = cfn_resource.Resource()

    @handler.create
    def create_thing(event, context):
        # do some stuff
        return {"PhysicalResourceId": "arn:aws:fake:myID"}

    @handler.update
    def update_thing(event, context):
        # do some stuff
        return {"PhysicalResourceId": "arn:aws:fake:myID"}

Running Tests
-------------

To run the tests locally, you need Python 2.7 and ``pip``. Ideally, you
should use a virtualenv.

.. code-block:: sh

    $ pip install -r test-requirements.txt
    $ py.test

The tests use ``mock`` and ``py.test`` and will give you a terminal
coverage report. Currently the tests cover ~90% of the (very small)
codebase.

License
-------

This code is released under the MIT software license, see LICENSE.txt
for details. No warranty of any kind is included, and the copyright
notice must be included in redistributions.
