# DEPRECATION WARNING

This repository and the `qiskit-api-py` package are deprecated, and no longer supported.

For the latest version, please refer to the [qiskit-ibmq-provider](https://github.com/Qiskit/qiskit-ibmq-provider).

The newest version behaves as a formal pluggable [provider](https://qiskit.org/documentation/the_ibmq_provider.html) for Qiskit.


# Python API Client IBM Quantum Experience [![Build Status](https://travis-ci.org/QISKit/qiskit-api-py.svg?branch=master)](https://travis-ci.org/QISKit/qiskit-api-py)

The official API Client to use [IBM Quantum Experience](https://quantumexperience.ng.bluemix.net/) in Python.

This package can be used in [Jupyter Notebook](https://jupyter.org/).

* [Installation](#installation)
* [Getting Started](#getting-started)
* [Methods](#methods)
* [GIST Jupyter](#jupyter)
* [Reference](#reference)

## Installation

You can install me using `pip` or `easy_install`. For example, from the command line:

    $ pip install IBMQuantumExperience

To install the package in Jupyter, you have to run in a Notebook:

```python
import pip
def install(package):
   pip.main(['install', package])
install('IBMQuantumExperience')
```

or, if you want the standard output, one could even use the exclamation point:

```python
! pip install IBMQuantumExperience
```

### Getting Started

Now it's time to begin doing real work with Python and IBM Quantum Experience.

First, import our API Client:

```python
from IBMQuantumExperience import IBMQuantumExperience
```

Then, initialize your IBM Quantum Experience connection by supplying your *token*. You can obtain the token from *[My Account](https://quantumexperience.ng.bluemix.net/qx/account)* area of *Quantum Experience Platform* in *Personal Access Token* section.

```python
api = IBMQuantumExperience("543...9df")
```

The constructor takes also other optional arguments. The dictionary *config* allows with extra options to customize the connection (like the url of the API).
The boolean *verify* checks for SSL certificate errors:

```python
api = IBMQuantumExperience("543...9df", config = {"url":"https://..."}, verify=False)
```

By default, the config parameter is defined like:

```
config = {
   "url": 'https://quantumexperience.ng.bluemix.net/api'
}
```

But the config parameter can be store the *access_token* and the *user_id* to avoid login with API Token if you know this values.
Also all methods can be receives the *access_token* and the *user_id*. Also you can set the *client_application* to know what client is using the QX Platform. By Default the client is set to the this general api python.

If *verify* is set to `False`, ignore SSL certificate errors:

```
verify = True
```

### Methods

### User Info

To get the information about the credits of the user, you only need call to:

```python
api.get_my_credits()
```

#### Codes

To get the information of a Code, including the last executions about this Code, you only need the codeId:

```python
api.get_code("id_code")
```

To get the information about the last Codes, including the last executions about these Codes, you only need call:

```python
api.get_last_codes()
```

#### Execution

To get all information (including the Code information) about a specific Execution of a Code, you only need the executionId:

```python
api.get_execution("id_execution")
```

To get only the Result about a specific Execution of a Code, you only need the executionId:

```python
api.get_result_from_execution("id_execution")
```

#### Running [QASM 2.0](https://github.com/QISKit/qiskit-openqasm)

To execute a [QASM 2.0](https://github.com/QISKit/qiskit-openqasm) experiment:

```python
api.run_experiment(qasm, device, shots, name=None, timeout=60)
```

- **qasm**: The QASM 2.0 code to run. Eg: 
```qasm = 'OPENQASM 2.0;\n\ninclude "qelib1.inc";\nqreg q[5];\ncreg c[5];\nh q[0];\ncx q[0],q[2];\nmeasure q[0] -> c[0];\nmeasure q[2] -> c[1];\n'```
- **backend**: Type of backend to run the experiment. Options: *simulator*, or real backends (You can use the available_backends() method to get the availables backends), those are the real chips of 5 qubits. Eg:
```device = 'simulator' ```
- **shots**: Number of shots of the experiments. Maximum 8192 shots. Eg:
```shots = 1024 ```
- **name**: Name of the experiment. This paramater is optional, by default the name will be 'Experiment \#YmdHMS'. Eg:
```name = 'bell state experiment'``
- **timeout**: Time to wait for the result. The maximum timeout is 300. If the timeout is reached, you obtain the executionId to get the result with the getResultFromExecution method in the future. Eg:
```timeout = 120```

#### Running Jobs [QASM 2.0](https://github.com/QISKit/qiskit-openqasm)

To execute jobs about [QASM 2.0](https://github.com/QISKit/qiskit-openqasm) experiments:

```python
api.run_job(qasms, backend, shots, max_credits)
```

- **qasms**: A list of objects with the QASM 2.0 information. Eg: 
```
[
   { 'qasm': 'OPENQASM 2.0;\n\ninclude "qelib1.inc";\nqreg q[5];\ncreg c[5];\nh q[0];\ncx q[0],q[2];\nmeasure q[0] -> c[0];\nmeasure q[2] -> c[1];\n'},
   { 'qasm': 'OPENQASM 2.0;\n\ninclude "qelib1.inc";\nqreg q[5];\ncreg c[5];\nx q[0];\nmeasure q[0] -> c[0];\n'}
]
```
- **backend**: Type of backend to run the experiment. Options: *simulator*, or real backends (You can use the available_backends() method to get the availables backends). Eg:
```device = 'simulator' ```
- **shots**: Number of shots of the experiments. Maximum 8192 shots. Eg:
```shots = 1024 ```
- **max_credits**: Maximum number of the credits to spend in the executions. If the executions are more expensives, the job is aborted. Eg:
```max_credits = 3```

To get job information:

```python
api.get_job(id_job)
```

- **id_job**: The identifier of the Job. Eg: 
``` 
    id_job = '9de64f58316db3eb6db6da53bf9135ff'
```

To get all jobs information:

- **limit**: Number of jobs returned. Eg:
```limit=5 ```

```python
api.get_jobs(limit)
```

#### Get information about a Device

To know the status (if it is running or in maintenance) of a device (real chip 5Q by default) you can run:

```python
api.backend_status(backend)
```

- **backend**: The backend to get its availability. By default is the 5 Qubits Real Chip. Eg:
```backend='ibmqx4' ```

#### Get Calibration of a Backend

To know the last calibration of a backend (real chip 5Q by default) you can run:

```python
api.backend_calibration(backend)
```

- **backend**: The backend to get its last calibration. By default is the 5 Qubits Real Chip. Eg:
```device='ibmqx4' ```

#### Get Parameters Calibration of a Backend

To know the last parameters of calibration of a backend (real chip 5Q by default) you can run:

```python
api.backend_parameters(backend)
```

- **backend**: The backend to get its last calibration. By default is the 5 Qubits Real Chip. Eg:
```device='ibmqx4' ```

#### Get Available Devices

To know the devices where you can run (by name):

```python
api.available_backends()
```

#### Get QX API Version

To know the version of the QX API:

```python
api.api_version()
```


## Deploy and Test

If you want participate in the project, you can clone the repository and install the dependencies to run it.

You can do a pull request to improve or add any functionality.

You can run the tests under ```test``` folder. See the test/README file to more information.

## Reference

[IBM Quantum Experience Tutorial](https://quantumexperience.ng.bluemix.net/qstage/#/tutorial?sectionId=c59b3710b928891a1420190148a72cce&pageIndex=0)

[IBM Quantun Experience Community](https://quantumexperience.ng.bluemix.net/qstage/#/community)

[OPENQASM](https://github.com/QISKit/qiskit-openqasm)
