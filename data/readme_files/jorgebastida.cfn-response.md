cfn-response
==============

[![Build Status](https://travis-ci.org/jorgebastida/cfn-response.svg?branch=master)](https://travis-ci.org/jorgebastida/cfn-response)

cfn-response is a micro package which exposes some helpers to talk with CloudFormation from within python Lambda functions. This package is intentionally small in order to be embedded lambda functions.

If you are looking to create aws-lambda backed custom CloudFormation resources using python, you are going to need this.

The source is pretty much a literal translation of the javascript version of this module developed by AWS and available here: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-code.html

Usage
------
Let's say we want to implement a dummy cfn-lambda which waits 5 seconds and then it succeed.

```python
import time
import json

from cfnresponse import send, SUCCESS

def handler(event, context):
    if event['RequestType'] == 'Delete':
        send(event, context, SUCCESS)
        return
    print("Received event: " + json.dumps(event, indent=2))
    time.sleep(5)
    send(event, context, SUCCESS)

```

References
-----------
* http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-custom-resources-lambda.html
* http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-code.html


Javascript
-----------
If you are looking for this library but for javascript, the aws-lambda javascript runtime already have a cfn-response module available. You can read more about here: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-code.html

Java
-----
If you are looking for this library but for Java, check out
https://github.com/SunRun/cfn-response-java
