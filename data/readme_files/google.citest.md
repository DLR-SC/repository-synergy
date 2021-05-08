# Summary
Cloud Integration Testing Framework (citest) is a python package to facilitate
writing integration tests against the REST style APIs typically used by
cloud services.

The gist is to allow tests to be written using a literary programming style
where the core framework accommodates for asynchronous calls and even retries
if appropriate.


# Setup
```
pip install -r requirements.txt
```

# Example
A test case might look something like this:

```python
  def create_google_load_balancer(self):
    bindings = self._bindings
    load_balancer_name = bindings['TEST_APP_COMPONENT_NAME']

    spec = {
        'checkIntervalSec': 9,
        'healthyThreshold': 3,
        'unhealthyThreshold': 5,
        'timeoutSec': 2,
        'port': 80
    }

    target_pool_name = '{0}/targetPools/{1}-tp'.format(
        bindings['TEST_REGION'], load_balancer_name)

        job=[{
            'cloudProvider': 'gce',
            'provider': 'gce',
            'stack': bindings['TEST_STACK'],
            'detail': bindings['TEST_COMPONENT_DETAIL'],
            'credentials': bindings['GCE_CREDENTIALS'],
            'region': bindings['TEST_GCE_REGION'],
            'ipProtocol': 'TCP',
            'portRange': spec['port'],
            'loadBalancerName': load_balancer_name,
            'healthCheck': {
                'port': spec['port'],
                'timeoutSec': spec['timeoutSec'],
                'checkIntervalSec': spec['checkIntervalSec'],
                'healthyThreshold': spec['healthyThreshold'],
                'unhealthyThreshold': spec['unhealthyThreshold'],
            },
            'type': 'upsertLoadBalancer',
            'availabilityZones': {bindings['TEST_GCE_REGION']: []},
            'user': '[anonymous]'
        }],
        description='Create Load Balancer: ' + load_balancer_name,
        application=bindings['TEST_APP'])

    builder = gcp_testing.GceContractBuilder(self.gce_observer)
    (builder.new_clause_builder('Health Check Added',
                                retryable_for_secs=30)
     .list_resources('http-health-checks')
     .contains_pred_list(
         [json_predicate.PathContainsPredicate(
              'name', '%s-hc' % load_balancer_name),
          json_predicate.DICT_SUBSET(spec)]))
    (builder.new_clause_builder('Target Pool Added',
                                retryable_for_secs=30)
     .list_resources('target-pools')
     .contains_path_value('name', '%s-tp' % load_balancer_name))
    (builder.new_clause_builder('Forwarding Rules Added',
                                retryable_for_secs=30)
     .list_resources('forwarding-rules')
     .contains_pred_list([
          json_predicate.PathContainsPredicate('name', load_balancer_name),
          json_predicate.PathContainsPredicate('target', target_pool_name)]))

    return service_testing.OperationContract(
        self.new_post_operation(
            title='upsert_load_balancer', data=payload, path='tasks'),
        contract=builder.build())

```


Where the test can be executed like this:

```python
  self.run_test_case(test_case)
```


# Overview

## Abstract Model

Integration tests are written against services by sending an operation to
the service then observing the effects of that operation and verifying them
against expectations.

`citest` introduces a `BaseAgent` class for adapting external services
to the framework where the agent is responsible for understanding the
transport and protocol for exchanging messages with the service. It introduces
some basic concrete types such as `HttpAgent` and `CliAgent` where the primary
means is HTTP messaging or running a command-line program. Specific systems
may need to further specialize these to understand any additional application
protocols added, such as status responses for asynchronous HTTP messaging.

`BaseAgent` also acts as an `AgentOperation` factory where the operations
provide a means to wrap these service calls as first-class objects understood
by the core `citest` framework. This allows `citest` to invoke (or reinvoke)
the operation when it is appropriate to do so, rather than when the static code
is specifying what the test will be. When executed, the `AgentOperation` will
create an `OperationStatus` allowing `citest` to track its progress and
eventual result.

In order to verify the operation, `citest` uses `Contract` objects. A contract
is a collection of `ContractClause` where each clause can look for different
effects. A `ContractClause` is typically composed of an observation on the
effects and an assertion about what is expected to be observed. The observation
is made by an `Observer` that collects data in an `Observation` by working with
a `BaseAgent` to collect the data (e.g. an HTTP GET on some
JSON resource). The assertion is made by looking for expected values and
patterns in the collected resources. Each clause can collect different
resources.

The assertions are written using specialized `ValuePredicate` objects, which
are python callable classes that take the object value to be validate and return
a `PredicateResult` containing the conclusion and justification for it.

When a test is run, it will provide a trace of the operations performed,
data collected and justifications as to why it thinks the collected data
meets or does not meet expectations, ultimately passing or failing the test.



## Physical Organization

SubPackage | Purpose
-------|--------
base | Introduces some classes and utilities that support other packages.
json_contract | Introduces a means to specify observers to collect JSON documents, and to define contracts specifying expectations of the collected JSON content.
json_predicate | Introduces a means to locate and attributes within JSON objects, and compare their values. These are used as the basis of json_contract.
service_testing | Introduces the core framework, base classes, and generic utilities.
aws_testing | Specializations and extensions to support testing on Amazon Web Services (AWS)
gcp_testing | Specializations and extensions to support testing on Google Cloud Platform (GCP)
openstack_testing | Specializations and extensions to support testing on OpenStack
azure_testing | Specializations and extensions to support testing on Microsoft Azure (AZ)
tests | Tests for this package


# More Examples

For more examples, see:

* The [examples](https://github.com/google/citest/blob/master/examples) subdirectory.
* [Spinnaker Citests](https://github.com/spinnaker/spinnaker/blob/master/testing/citest/README.md).


# Documentation

The [Usage Overview Document](overview.md) provides some instructions and
examples to guide basic usage.


# Contributing

See the CONTRIBUTING file for more information.


# License

See the LICENSE file for more information.

The package is composed of several subpackages of individual modules.


# Contact Info

For more information, problems, or interest, contact ewiseblatt@google.com.
