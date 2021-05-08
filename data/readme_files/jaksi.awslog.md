# awslog

Show the history and changes between configuration versions of AWS resources

Uses AWS Config to fetch the configuration history of resources, only works on [resources supported by AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html).

![Screenshot](https://raw.githubusercontent.com/jaksi/awslog/master/screenshot.png)

# Installation

`pip install awslog`

# Usage

Make sure your [AWS credentials are properly configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html).
You can test it using the AWS CLI by issuing `aws sts get-caller-identity`. It should report information about your current CLI session and not raise any errors.

Make sure [AWS Config](https://aws.amazon.com/config/) is set up to record configuration changes of your resources.

## CLI

```
usage: awslog [-h] [--type TYPE] [--number NUMBER] [--before BEFORE]
              [--after AFTER] [--deleted] [--context CONTEXT] [--no-color]
              name

positional arguments:
  name                  name or ID of the resource to query

optional arguments:
  -h, --help            show this help message and exit
  --type TYPE, -t TYPE  the type of the resource to query list of supported
                        resource types: https://docs.aws.amazon.com/config/lat
                        est/developerguide/resource-config-reference.html
  --number NUMBER, -n NUMBER
                        number of history items to show
  --before BEFORE, -b BEFORE
                        show changes more recent than the specified date and
                        time
  --after AFTER, -a AFTER
                        show changes older than the specified date and time
  --deleted, -d         include deleted resources
  --context CONTEXT, -c CONTEXT
                        number of context lines in the diffs
  --no-color, -o        disable colored output
```

Examples:
```shellsession
$ awslog sg-7235f203
--- arn:aws:ec2:us-east-1:281519598877:security-group/sg-7235f203/configuration	2018-09-12 23:44:36
+++ arn:aws:ec2:us-east-1:281519598877:security-group/sg-7235f203/configuration	2018-09-12 23:53:44
@@ -1,24 +1,24 @@
 {
   "description": "default VPC security group",
   "groupId": "sg-7235f203",
   "groupName": "default",
   "ipPermissions": [
     {
       "fromPort": 80,
       "ipProtocol": "tcp",
       "ipRanges": [
-        "1.1.1.1/32"
+        "0.0.0.0/0"
       ],
       "ipv4Ranges": [
         {
-          "cidrIp": "1.1.1.1/32"
+          "cidrIp": "0.0.0.0/0"
         }
       ],
       "ipv6Ranges": [],
       "prefixListIds": [],
       "toPort": 80,
       "userIdGroupPairs": []
     }
   ],
   "ipPermissionsEgress": [
     {
```

```shellsession
$ awslog --type AWS::IAM::User \
>        --number 2 \
>        --before '10 minutes ago' \
>        --after '2018-01-01' \
>        --deleted \
>        --context 3 \
>        --no-color \
>        ReadOnly
--- arn:aws:iam::281519598877:user/ReadOnly/configuration	2018-09-13 11:28:16
+++ arn:aws:iam::281519598877:user/ReadOnly/configuration	2018-09-13 11:53:02
@@ -1,10 +1,6 @@
 {
   "arn": "arn:aws:iam::281519598877:user/ReadOnly",
   "attachedManagedPolicies": [
-    {
-      "policyArn": "arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess",
-      "policyName": "AmazonEC2ReadOnlyAccess"
-    },
     {
       "policyArn": "arn:aws:iam::aws:policy/AdministratorAccess",
       "policyName": "AdministratorAccess"

--- arn:aws:iam::281519598877:user/ReadOnly/configuration	2018-09-13 10:58:19
+++ arn:aws:iam::281519598877:user/ReadOnly/configuration	2018-09-13 11:28:16
@@ -4,6 +4,10 @@
     {
       "policyArn": "arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess",
       "policyName": "AmazonEC2ReadOnlyAccess"
+    },
+    {
+      "policyArn": "arn:aws:iam::aws:policy/AdministratorAccess",
+      "policyName": "AdministratorAccess"
     },
     {
       "policyArn": "arn:aws:iam::aws:policy/IAMUserChangePassword",
```

## Python module

```python console
>>> import boto3
>>> import awslog
>>> config = boto3.client('config')
>>> after, before = list(awslog.get_config_history(config, 'AWS::EC2::SecurityGroup', 'sg-7235f203'))
>>> print('\n'.join(awslog.create_diff(after, before)))
```

```
--- arn:aws:ec2:us-east-1:281519598877:security-group/sg-7235f203/configuration	2018-09-12 23:44:36
+++ arn:aws:ec2:us-east-1:281519598877:security-group/sg-7235f203/configuration	2018-09-12 23:53:44
@@ -1,24 +1,24 @@
 {
   "description": "default VPC security group",
   "groupId": "sg-7235f203",
   "groupName": "default",
   "ipPermissions": [
     {
       "fromPort": 80,
       "ipProtocol": "tcp",
       "ipRanges": [
-        "1.1.1.1/32"
+        "0.0.0.0/0"
       ],
       "ipv4Ranges": [
         {
-          "cidrIp": "1.1.1.1/32"
+          "cidrIp": "0.0.0.0/0"
         }
       ],
       "ipv6Ranges": [],
       "prefixListIds": [],
       "toPort": 80,
       "userIdGroupPairs": []
     }
   ],
   "ipPermissionsEgress": [
     {
```
