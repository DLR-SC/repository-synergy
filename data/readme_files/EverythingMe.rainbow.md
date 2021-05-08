[![Build Status](https://travis-ci.org/EverythingMe/rainbow.svg?branch=master)](https://travis-ci.org/EverythingMe/rainbow)

# Rainbow - AWS Cloudformation on steroids

Working with Cloudformation inhouse, we discovered the following needs:
* Break a big stack into several smaller ones
* Reference resources *between* stacks and regions
* Add dynamic template preprocessing logic
* Compose a stack from reusable 'building blocks'
* Improve readability by coding templates and parameters in YAML (and have comments!)

# Installation
`pip install rainbow-cfn`

Usage
=====
* [Configure boto](http://boto.readthedocs.org/en/latest/boto_config_tut.html)
* Run `rainbow`

Datasources
===========

What is a datasource
--------------------
Datasource is a key-value mapping which Rainbow uses to fill [Cloudformation templates parameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/concept-parameters.html)  
Datasources can be YAML files, other Cloudformation stacks (resources, outputs and even parameters), files, etc.  
The system is fully extensible for you to add any other datasources you might want.  

Every parameter the template requires is being looked up on the list of datasources given to the rainbow CLI tool. A parameter can exist on multiple datasources, having the first match returned.  
For example, say you run rainbow with `--data-source yaml:a.yaml --data-source yaml:b.yaml --data-source:c.yaml`, the files are:
```yaml
# a.yaml
InstanceType: m1.small
KeyName: omrib-laptop
AvailabilityZones:
  - us-east-1a

# b.yaml
AutoScalingGroupMinSize: 0
AutoScalingGroupMaxSize: 1
Image: PreciseAmd64PvInstanceStore

# c.yaml
InstanceType: m1.large
```

Lets say your template requires the following parameters:  
```yaml
Parameters:
  AvailabilityZones: {Type: CommaDelimitedList}
  KeyName: {Type: String}
  AutoScalingGroupMinSize: {Type: String}
  AutoScalingGroupMaxSize: {Type: String}
  Image: {Type: String}
  InstanceType: {Type: String}
```

The lookup order is `a.yaml`, `b.yaml` and `c.yaml`. Rainbow will fill all the parameters as follows:
```
AvailabilityZones: us-east-1a (from a.yaml)
KeyName: omrib-laptop (from a.yaml)
AutoScalingGroupMinSize: 0 (from b.yaml)
AutoScalingGroupMaxSize: 1 (from b.yaml)
Image: PreciseAmd64PvInstanceStore (from b.yaml)
InstanceType: m1.small (from a.yaml. Even though the value exists in c.yaml as well, because the yaml:a.yaml datasource appears before yaml:c.yaml, the value will be m1.small and not m1.large)
```

Another cool feature of the YAML datasource is pointers. You can make the lookup begin all over again when a key has a value that begins with `$`. For example, when running rainbow with `--data-source yaml:a.yaml --data-source yaml:b.yaml`:
```yaml
# a.yaml
AdminKeyName: omrib-laptop

# b.yaml
KeyName: $AdminKeyName
AdminKeyName: oren-laptop
```

The value of `KeyName` (`b.yaml`) points to `AdminKeyName`, which exists both on `a.yaml` and `b.yaml`, but the `a.yaml` value will be used, meaning `KeyName` equals `omrib-laptop`.  
Pointers can be used to reference a key from a different type of datasource.


## Available datasources

### YAML
`yaml[:rootkey]:path/to/file` - stores all keys (starting from rootkey, if given) with their values

### cfn_resources
`cfn_resources[:region]:stackname` - stores a logical resource to physical resource mapping. [Read more about Cloudformation resources](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/concept-resources.html)

### cfn_outputs
`cfn_outputs[:region]:stackname` - stores a output to value mapping. [Read more about Cloudformation outputs](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/concept-outputs.html)

### cfn_parameters
`cfn_parameters[:region]:stackname` - input parameters to value mapping. You can use this as the only datasource when you only want to modify the template without touching the parameters.

### file
`file:name:path/to/file` - stores a single key `name` with the value of the file content

### file64
`file64:name:path/to/file` - same as `file`, but returns a BASE64 string instead of plaintext

# Rainbow functions

## Rb::InstanceChooser

From a given list of possible instance types, choose the first one that exists on that region.  
Suppose you have a CFN stack that should be using a `c3.large` instance, but in a particular region that instance family is not yet supported. In that case, you want it to fallback to `c1.medium`.  
A code of `{'Rb::InstanceChooser': ['c3.large', 'c1.medium']}` will evaluate to `c3.large` on regions that supports it and `c1.medium` on regions that don't.
