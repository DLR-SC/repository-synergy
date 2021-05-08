# dizzy

dizzy is a fuzzing framework, written in python and capable of state-full and state-less fuzzing with a lot of output options.

## usage

```
$dizzy_cmd version 2.0 running on Linux
usage: dizzy_cmd [-h] [-s START_AT] [-d SEC] [-l] [-o OPTIONS] [jobfile]

positional arguments:
  jobfile

optional arguments:
  -h, --help   show this help message and exit
  -s START_AT  Start at the given step
  -d SEC       Output status every SEC seconds
  -l           List all loaded modules and their contents.
  -o OPTIONS   Overwrite a config option
```

A [jobfile](jobfile) is all that is needed. The `-s START_AT` option can be used to start the fuzzing process at a given step and skip all previous steps. The `-d SEC` option configures the output interval of progress messages and using the `-o OPTIONS` parameter, config values from the jobfile can be overwritten.


## jobfile

The Job Configfile contains all information necessary to start a fuzzing job

The `[job]` section defines which interaction file (state-full fuzzing) or which dizz file (state-less fuzzing) to use, the fuzzing mode and other parameters, like verbosity or the delay between mutations. 

The `[output]` section defines were to send the generated data. The only common parameter is the `type` parameter, defining which session module to use. All other parameters in this section are session module dependent.

In the optional `[probe]` section a target probe can be defined. The probe runs after each complete fuzzing step and checks if the target is still available.

In the optional `[value]` section, generic values can be defined. Those values will be available to .dizz and .act files via the `config_value` function.

```
[job]
file = smb2/act/smb2_tree_connect.act
mode = none
delay = 0
verbose = 4

[output]
type = session.tcp
server = False
auto_reopen = False
session_reopen = True
timeout = 5
target_host = 127.0.0.1
target_port = 445

#[probe]
#type = icmp
#timeout = 1
#pkg_size = 64
#target_host = 192.168.2.1

[values]
creds_file = ./creds
share_path = \\127.0.0.1\test
```

## module structure

Modules are created from the _modules\_src_ folder. A Makefile is provided that generates the \_\_init\_\_.py index files and packs the module zip files. To update the modules run _make_ in the modules\_src folder:
```
~/dizzy/modules_src# make
```
to the generated index files, run _make clean_ in the modules\_src folder:
```
~/dizzy/modules_src# make clean
```

In the _modules\_src_ folder, every module has an own folder, named the same as the module. Each module folder has the following structure:

- config.py -- in here, values such as the modules name, the modules external dependecies and the version number are defined.
- a folder named like the module (smb2 in this example).
   - a folder named _dizz_, containing the module's .dizz files. (See [DizzFile](dizzfile))
   - a folder named _act_, containing the module's .act files. (See [ActFile](actfile))
   - a folder named _job_, containing the module's job files. (See [JobFile](jobfile))
   - a folder named _probe_, containing the module's probes. (See [Probe](interface-of-probe))
   - a folder named _session_, containing the module's sessions. (See [Session](interface-of-session))
   - a folder named _deps_, containing the module's internal dependencies. The folder will be added to pythons include path and its contents can be _import_ ed in .dizz and .act files.

As a example the structure of the smb2 module is shown:

```
~/dizzy/modules_src# tree smb2
smb2
├── config.py
├── __init__.py
└── smb2
    ├── act
    │   ├── smb2_file_access_read.act
    │   ├── smb2_file_access_write.act
    │   ├── smb2_neg_setup_auth.act
    │   └── smb2_tree_connect.act
    ├── deps
    │   ├── nmb
    │   │   ├── ...
    │   ├── pyasn1
    │   │   └── ...
    │   └── smb
    │       ├── ...
    ├── dizz
    │   ├── smb2_close_request.dizz
    │   ├── smb2_create_request_read.dizz
    │   ├── smb2_create_request_write.dizz
    │   ├── smb2_negotiate_req.dizz
    │   ├── smb2_read_request.dizz
    │   ├── smb2_session_setup_req.dizz
    │   ├── smb2_tree_connect_req.dizz
    │   ├── smb2_write_request.dizz
    │   └── smb_com_negotiate_req.dizz
    ├── job
    │   ├── smb2_file_access_read.conf
    │   ├── smb2_file_access_write.conf
    │   └── smb2_tree_connect.conf
    └── probe
        └── smb2.py
```

## wireshark plugin

In the wireshark folder, there is a lua plugin to export parsed packet in `.dizz` files.

Note, that it requires a lua version of 5.2.0 or newer.

To use it, run 

```
$ cwd
~/dizzy/wireshark
$ wireshark -X lua_script:dizzy.lua
```
 


## dizz file

So, now a short introduction to the dizzy packet and protocol specifications:

A single packet is described by a so called dizz file.
Some example files can be found in the demo module folder that comes with dizzy.
These files are python code so you need to write them in python syntax and format rules.
They consist of 2 variables which need to be defined.

The first var is called `objects` and describes the fields of the packet.
Its a python array of objects with a specific [interface](Interface-of-dizz-object):
```python
objects = [
    ...
    ]
```

The following list show the pre-defined classes which is has implemented the [interface](Interface-of-dizz-object) 
already and are imported in a dizz file:
- `Field()` is the standard class to defined a field.
  The class takes 6 arguments, which are:
  * `name` (**REQUIRED**) have to be a `str()`, which is the name of the field (it to be unique in the packet).
  * `default` (**`=b''`**) have to be a `bytes`, `int` or `str()`, which is the default value of the field.
  * `size` (**`=None`**) have to be a `int()` or `slice()` (in bits).  
    If it is `None` than the field has the same size as the default value.
    With `slice()` a variable size can be defined.
  * `fuzz` (**`="none"`**) have to be a `str()`, which is defined the fuzzing mode for the field.  
    The fuzzing mode for that field can be `"none"` for not fuzzing that field at all, `"std"` for fuzzing some values 
    on the upper and lower value border, and `"full"` for fuzzing all possible values.
  * `endian` (**="!"**) have to be a `str()`, which is defined the endianness of the field when the default value is a 
    `int()`  
    The endianss for that argument can be `"!"` for network (=big-endian), `"<"` for little-endian or `">"` for 
    big-endian.
  * `encoding` (**`=CONFIG["GLOBALS"]["CODEC"]`**) have to be a `str`, which defined the encoding schema of the default 
    value if it is a `str()`  
  
  Example:
  ```python
  ...
  objects = [
      Field("length_field", b"\x00" * 8), # 8 byte length filed
      Field("variable_sized_field", b"\x00" * 8, slice(2, 20, 2))
      ...
      ]
  ...
  ```
- `List()` is a field, which have a list of value from a file.
  The class takes 4 arguments, which are:
  * `name` (**REQUIRED**) have to be a `str()`, which is the name of the field (it to be unique in the packet).
  * `path` (**`=CONFIG["GLOBALS"]["DEFAULT_STR_LIB"]`**) have to be a `str()`, which defined the path to the file (one value per line, all values will be inserted 
     while fuzzing)
  * `encoding` (**`=CONFIG["GLOBALS"]["CODEC"]`**) have to be a `str`, which defined the encoding list.
  * `default` (**`=None`**) have to be `bytes()`, which defined the first value of the list. 
  
  Example:   
    ```python
    ...
    objects = [
        Field("length_field", b"\x00" * 8), # 8 byte length filed
        List("list_of_values", "/lists/test.txt", default=b"First value"), # new line separated list
    ...
    ]
   ```

The second var is called `functions` and is for execute some code to change the value of the fields.
Its a python array of functions with a specific [interface](Interface-of-dizz-function):
```python
functions = [
    ...
    ]
```

The following list show the pre-defined functions which is has the [interface](Interface-of-dizz-object) already and are
 imported in a dizz file:
- `link` is a function to copy the value of a field into another field per mutation.
  So that target field has the same value as the source field during the fuzzing.
  The function takes 2 arguments, which are:
  * `source` (**REQUIRED**) have to be a `str()`, which defined the name of the source field.
  * `target` (**REQUIRED**) have to be a `str()`, which defined the name of the target field.
  
  Example:
  ```python
  ...
  objects = [
      Field("source_field", b"\xaa", fuzz="full"),
      Field("target_field", b"\x00", fuzz="none"), # this field has always the same value as source_field
      ...
    ]
  
  functions = [
      link("source_field", "target_field"),
      ...
  ]
  ```
- `length` is a function to save the current size(in bits) of fields in a dedicated length field.
  This function is useful for example when the packet has a Type Length Value structure.
  The function takes 3s arguments, which are:
  * `target` (**REQUIRED**) have to be a `str()`, which defined the name of the field to save the length.
  * `start` (**`=START`**) have to be a `str()`, which defined where the function should start to count the length.
    The default parameter of this argument(`=START`) means to start at the beginning of the packet.
  * `stop` (**`=STOP`**) have to be a `str()`, which defined where the function should stop(inclusive) to count the 
    length.
    The default parameter of this argument(`=STOP`) means to start at the end of the packet.
  
  Example:
  ```python
  objects = [
      Field("field0", b"\xaa" * 2, fuzz="full"),
      Field("field1", b"\xaa" * 2, slice(4, 9), fuzz="full"),
      # calculate the current size of the field0 und field1 in bits and saves the size in length_field
      Field("length_field", b"\x00\x00", endian="<", fuzz="none"), 
      ...
    ]

  functions = [
      length("length_field", "field0", "field1"),
      ...
  ]
  ```
- `length_bytes` is a function same as `length` but the length is saved in bytes.
  The function takes 3 arguments, which are:
  * `target` (**REQUIRED**) have to be a `str()`, which defined the name of the field to save the length.
  * `start` (**`=START`**) have to be a `str()`, which defined where the function should start to count the length.
    The default parameter of this argument(`=START`) means to start at the beginning of the packet.
  * `stop` (**`=STOP`**) have to be a `str()`, which defined where the function should stop(inclusive) to count the 
    length.
    The default parameter of this argument(`=STOP`) means to start at the end of the packet.
    
  Example:
  ```python
  objects = [
      Field("field0", b"\xaa" * 2, fuzz="full"),
      Field("field1", b"\xaa" * 2, slice(4, 9), fuzz="full"),
      # calculate the current size of the field0 und field1 in bytes and saves the size in length_field
      Field("length_field", b"\x00\x00", endian="<", fuzz="none"), 
      ...
    ]

  functions = [
      length_bytes("length_field", "field0", "field1"),
      ...
  ]
  ```
    
- `length_string_bytes` is a function same as `length_bytes` but the length is saved in bytes and as `str()`.
  The function takes 4 arguments, which are:
  * `target` (**REQUIRED**) have to be a `str()`, which defined the name of the field to save the length.
  * `start` (**`=START`**) have to be a `str()`, which defined where the function should start to count the length.
    The default parameter of this argument(`=START`) means to start at the beginning of the packet.
  * `stop` (**`=STOP`**) have to be a `str()`, which defined where the function should stop(inclusive) to count the 
    length.
    The default parameter of this argument(`=STOP`) means to start at the end of the packet.
  * `encoding` (**`=CONFIG["GLOBALS"]["CODEC"]`**) have to be a `str`, which defined the encoding of string.
  
  Example:
  ```python
  objects = [
      Field("field0", b"\xaa" * 2, fuzz="full"),
      Field("field1", b"\xaa" * 2, slice(4, 9), fuzz="full"),
      # calculate the current size of the field0 und field1 in bytes as and saves the size as string in length_field
      Field("length_field", b"\x00\x00", endian="<", fuzz="none"), 
      ...
    ]

  functions = [
      length_string_bytes("length_field", "field0", "field1"),
      ...
  ]
  ```
- `length_lambda` is a function same as `length` but the length is pass to a function and the return value of the function
  is saved in a dedicated length field.
  The function takes 4 arguments, which are:
  * `lam` (**REQUIRED**) have to be a function(mostly a lambda function), to pass the size(so the function has 1 
     argument).
  * `target` (**REQUIRED**) have to be a `str()`, which defined the name of the field to save the length.
  * `start` (**`=START`**) have to be a `str()`, which defined where the function should start to count the length.
    The default parameter of this argument(`=START`) means to start at the beginning of the packet.
  * `stop` (**`=STOP`**) have to be a `str()`, which defined where the function should stop(inclusive) to count the 
    length.
    The default parameter of this argument(`=STOP`) means to start at the end of the packet.
  * `encoding` (**`=CONFIG["GLOBALS"]["CODEC"]`**) have to be a `str`, which defined the encoding of string.
  
  Example:
  ```python
  objects = [
      Field("field0", b"\xaa" * 2, fuzz="full"),
      Field("field1", b"\xaa" * 2, slice(4, 9), fuzz="full"),
      # calculate the current size of the field0 und field1 in bits and pass it to the lambda function and saves the 
      # return value into the length_field
      Field("length_field", b"\x00\x00", endian="<", fuzz="none"), 
      ...
    ]

  functions = [
      length_lambda(lambda x: x + 1, "length_field", "field0", "field1"),
      ...
  ]
  ```
- `chechsum` is a function that calculate a checksum over fields and save the value to a dedicate field.
  The function takes 4 arguments, which are:
  * `target` (**REQUIRED**) have to be a `str()`, which defined where to save the checksum.
  * `start` (**REQUIRED**) have to be a `str()`, which defined where the function should start to calculate the 
    checksum.
  * `stop` (**REQUIRED**) have to be a `str()`, which defined where the function should stop(inclusive) to calculate the 
    checksum.
  * `algorithm` (**REQUIRED**) have to be a `str()`, which defined the algorithm to use for the checksum.
    The possible value for this argument are:
      - `"md5"` for Message-Digest Algorithm 5
      - `"sha1"` for Secure Hash Algorithm 1
      - `"sha224"` for Secure Hash Algorithm 2 with a hash length of 224 bits
      - `"sha256"` for Secure Hash Algorithm 2 with a hash length of 256 bits
      - `"sha384"` for Secure Hash Algorithm 2 with a hash length of 384 bits
      - `"sha512"` for Secure Hash Algorithm 2 with a hash length of 512 bits
    
    Example:
    ```python
    objects = [
        Field("field0", b"\xaa" * 2, fuzz="full"),
        Field("field1", b"\xaa" * 2, slice(4, 9), fuzz="full"),
        # calculate the checksum of field0 and field1 and save it to checksum_field (the size of checksum_field is the
        # same, if the checksum value is bigger than the size of the field then it would be truncate)
        Field("checksum_field", b"\x00\x00\x00\x00"), 
        ...
    ]
    functions = [
        chechsum("checksum_field", "field0", "field1", "md5"),
        ...
    ]
    ```
- `checksum_inet` is a function that calculate a checksum over field by using the algorithm 'inet' (rfc1071) and save 
  the to a dedicate field.
  The function take 3 arhuments, which are:
  * `target` (**REQUIRED**) have to be a `str()`, which defined where to save the checksum.
  * `start` (**REQUIRED**) have to be a `str()`, which defined where the function should start to calculate the 
    checksum.
  * `stop` (**REQUIRED**) have to be a `str()`, which defined where the function should stop(inclusive) to calculate the 
    checksum.
    
    Example:
    ```python
    objects = [
        Field("field0", b"\xaa" * 2, fuzz="full"),
        Field("field1", b"\xaa" * 2, slice(4, 9), fuzz="full"),
        # calculate the checksum of field0 and field1 and save it to checksum_field
        Field("checksum_field", b"\x00\x00\x00\x00"), 
        ...
    ]
    functions = [
        checksum_inet("checksum_field", "field0", "field1", "md5"),
        ...
    ]
    ```

## act file

Ok, that are the packet descriptions so far.
Ones you want to get state full, you need to write interaction in act files. 
Some prepared can be found in the interactions folder that comes with dizzy. 
These file are python code as well.
They consist of 2 variables which need to be defined.

The first var is called `objects` which is a python list of `Dizz()`.   
`Dict()` is a class, which have 6 arguments:
- `name` (**REQUIRED**) have to be a `str()`, which is the name of the packet (it to be unique in the interaction).
- `filename` (**REQUIRED**) have to be a `str()`, which is the path of the dizz file.
- `readback` (**`=0`**) have to be a `int()`, which defined how many bytes at least to read after the packet was send.
- `fuzz` (**`="std"`**) have to be a `str()`, which define the fuzzing mode for this packet.
   The fuzzing mode for that packet can be `"none"` for not fuzzing that packet at all, `"std"` for fuzzing each field 
   at once, and `"full"` for fuzzing all fields by using the cross product.
- `start_at` (**`=0`**) have to be a `int()`, which defined at which iteration the packet should start.
- `config_values` (**`={}`**) have to be a `dict()`, which defined the configuration values for the packet.

```python
objects = [
    # define the first packet of the interaction and after the packet is send it have read at least 100 bytes from the 
    # session 
    Dizz("first_packet", "module_name/dizzes/first_packet.dizz", 100, fuzz="full"),
    Dizz("second_packet", "module_name/dizzes/second_packet.dizz"),
    ...
    ]
```
 
The second var is called `functions`, which is this case a python `dict()`.
For more information about act `functions` see [Interface](interface-of-act-function).
The following example takes the value of the `field0` dizz object of the dizz packet `Dizz0` and assigned it to the 
`field0` of the dizz packet `Dizz3`:
```python
def test(interaction_iterator, dizzy_iterator, response):
    buf0 = response[0:10]
    dizzy_iterator["field4"] = buf0
    buf1 = interaction_iterator["Dizz0"]["field0"]
    interaction_iterator["Dizz3"]["field0"] = buf1
```

## Interface of Probe
This section describes the interface of the probe objects.
A field object have mandatory attributes.

### Mandatory
- `__init__(self, section_proxy)`
- `open(self)` have to be a `function`, which open the probe.
- `close(self)` have to be a `function`, which close the probe.
- `probe(self)` have to be a `function`, which runs the probe check and returns `True` or `False`.  
  
### Example
A probe always succeeding:
```python
class DizzyProbe(object):
    def __init__(self, section_proxy):
        pass

    def open(self):
        pass

    def probe(self):
        return True

    def close(self):
        pass
```

## Interface of Session
This section describes the interface of the session objects.
A field object have mandatory attributes.

### Mandatory
- `__init__(self, section_proxy)`
- `open(self)` have to be a `function`, which open the session.
- `close(self)` have to be a `function`, which close the session.
- `send(self, data)` have to be a `function`, which send data through the session.  
  * `data` have to be a bytes.
- `recv(self)` have to be a `function`, which receive data from the session.

### Example
The following example takes the creates a session as `stdin` for input and `stdout` for output:
```python
class DizzySession(object):
    def __init__(self, section_proxy):
        pass

    def open(self):
        pass

    def send(self, data):
        self.f.write(data + b"\n")

    def recv(self):
        return stdin.readline()

    def close(self):
        pass
```