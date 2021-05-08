# pymysensors [![Build Status][build-badge]][build]

Python API for talking to a [MySensors gateway](http://www.mysensors.org/). Currently supports serial protocol v1.4, v1.5, v2.0 - v2.2. Not all features of v2.x are implemented yet.

- Supports smartsleep with serial API v2.x.
- Supports the MQTT client gateway with serial API v2.x.
- Supports OTA updates, for both [DualOptiboot](https://github.com/mysensors/DualOptiboot) and [MYSBootloader](https://github.com/mysensors/MySensorsBootloaderRF24) bootloaders.
- All gateway instances, serial, tcp (ethernet) or mqtt will run in separate threads.
- As an alternative to running the gateway in its own thread, there are experimental implementations of all gateways using asyncio.

## Requirements

pymysensors requires Python 3.5.3+.

## Installation

You can easily install it from PyPI:

```pip3 install pymysensors```

## Usage

Currently the API is best used by implementing a callback handler

```py
import mysensors.mysensors as mysensors

def event(message):
    """Callback for mysensors updates."""
    print('sensor_update ' + str(message.node_id))

GATEWAY = mysensors.SerialGateway('/dev/ttyACM0', event)
GATEWAY.start()
```

In the above example pymysensors will call "event" whenever a node in the Mysensors network has been updated. The message passed to the callback handler has the following data:

```txt
Message
    gateway - the gateway instance
    node_id - the sensor node identifier
    child_id - the child sensor id
    type - the message type, for example "set" or "presentation" (int)
    ack - True is message was an ACK, false otherwise (0 or 1)
    sub_type - the message sub_type (int)
    payload - the payload of the message (string)
```

_Note: The content of the sub_type differs according to the context. In presentation messages, the sub_type denotes S_TYPE data (such as S_INFO). In 'set' and 'req' messages the sub_type denotes V_TYPE data (such as V_TEXT)._

Symbolic names for the Message types and sub_types are defined in the protocol version-specific const_X.py files.

The data structure of a gateway and it's network is described below.

```txt
SerialGateway/TCPGateway/MQTTGateway
    sensors - a dict containing all nodes for the gateway; node is of type Sensor

Sensor - a sensor node
    children - a dict containing all child sensors for the node
    sensor_id - node id on the MySensors network
    type - 17 for node or 18 for repeater
    sketch_name
    sketch_version
    battery_level
    protocol_version - the mysensors protocol version used by the node

ChildSensor - a child sensor
    id - child id on the parent node
    type - data type, S_HUM, S_TEMP etc.
    description - the child description sent when presenting the child
    values - a dictionary of values (V_HUM, V_TEMP, etc.)
```

Getting the type and values of node 23, child sensor 4 would be performed as follows:

```py
s_type = GATEWAY.sensors[23].children[4].type
values = GATEWAY.sensors[23].children[4].values
```

Similarly, printing all the sketch names of the found nodes could look like this:

```py
for node in GATEWAY.sensors.values():
    print(node.sketch_name)
```

Getting a child object inside the event function could be:

```py
    if GATEWAY.is_sensor(message.node_id, message.child_id):
        child = GATEWAY.sensors[message.node_id].children[message.child_id]
    else:
        print("Child not available yet.")
```

To update a node child sensor value and send it to the node, use the set_child_value method in the Gateway class:

```py
# To set sensor 1 (int), child 1 (int), sub-type V_LIGHT (= 2) (int), with value 1.
GATEWAY.set_child_value(1, 1, 2, 1)
```

### Persistence

With persistence mode on, you can restart the gateway without
having to restart each individual node in your sensor network. To enable persistence mode, the keyword argument `persistence`
in the constructor should be True. A path to the config file
can be specified as the keyword argument `persistence_file`. The file type (.pickle or .json) will set which persistence protocol to use, pickle or json. JSON files can be read using a normal text editor. Saving to the persistence file will be done on a schedule every 10 seconds if an update has been done since the last save. Make sure you start the persistence saving before starting the gateway.

```py
GATEWAY.start_persistence()
```

### Protocol version

Set the keyword argument `protocol_version` to set which version of the MySensors serial API to use. The default value is `'1.4'`. Set the `protocol_version` to the version you're using.

### Serial gateway

The serial gateway also supports setting the baudrate, read timeout and reconnect timeout.

```py
import mysensors.mysensors as mysensors

def event(message):
    """Callback for mysensors updates."""
    print("sensor_update " + str(message.node_id))

GATEWAY = mysensors.SerialGateway(
  '/dev/ttyACM0', baud=115200, timeout=1.0, reconnect_timeout=10.0,
  event_callback=event, persistence=True,
  persistence_file='somefolder/mysensors.pickle', protocol_version='2.2')
GATEWAY.start_persistence() # optional, remove this line if you don't need persistence.
GATEWAY.start()
```

There are two other gateway types supported besides the serial gateway: the tcp-ethernet gateway and the MQTT gateway.

### TCP ethernet gateway

The ethernet gateway is initialized similar to the serial gateway. The ethernet gateway supports setting the tcp host port, receive timeout and reconnect timeout, besides the common settings and the host ip address.

```py
GATEWAY = mysensors.TCPGateway(
  '127.0.0.1', port=5003, timeout=1.0, reconnect_timeout=10.0,
  event_callback=event, persistence=True,
  persistence_file='somefolder/mysensors.pickle', protocol_version='1.4')
```

### MQTT gateway

The MQTT gateway requires MySensors serial API v2.0 or greater and the MQTT client gateway example sketch loaded in the gateway device. The gateway also requires an MQTT broker and a python MQTT client interface to the broker. See [mqtt.py](https://github.com/theolind/pymysensors/blob/master/mqtt.py) for an example of how to implement this and initialize the MQTT gateway.

### Over the air (OTA) firmware updates

Call `Gateway` method `update_fw` to set one or more nodes for OTA
firmware update. The method takes three positional arguments and one
keyword arguement. The first argument should be the node id of the node to
update. This can also be a list of many node ids. The next two arguments should
be integers representing the firwmare type and version. The keyword argument is
optional and should be a path to a hex file with the new firmware.

```py
GATEWAY.update_fw([1, 2], 1, 2, fw_path='/path/to/firmware.hex')
```

After the `update_fw` method has been called the node(s) will be requested
to restart when pymysensors Gateway receives the next set message. After
restart and during the MySensors `begin` method, the node will send a firmware
config request. The pymysensors library will respond to the config request. If
the node receives a proper firmware config response it will send a firmware
request for a block of firmware. The pymysensors library will handle this and
send a firmware response message. The latter request-response conversation will
continue until all blocks of firmware are sent. If the CRC of the transmitted
firmware match the CRC of the firmware config response, the node will restart
and load the new firmware.

### Gateway id

The gateway method `get_gateway_id` will try to return a unique id for the
gateway. This will be the serial number of the usb device for serial gateways,
the mac address of the connected gateway for tcp gateways or the publish topic
prefix (in_prefix) for mqtt gateways.

### Connection callbacks

It's possible to register two optional callbacks on the gateway that are called
when the connection is made and when the connection is lost to the gateway
device. Both callbacks should accept a gateway parameter, which is the gateway
instance. The connection lost callback should also accept a second parameter
for possible connection error exception argument. If connection was lost
without error, eg when disconnecting, the error argument will be `None`.

**NOTE:**
The MQTT gateway doesn't support these callbacks since the connection to the
MQTT broker is handled outside of pymysensors.

```py
def conn_made(gateway):
  """React when the connection is made to the gateway device."""
  pass

GATEWAY.on_conn_made = conn_made

def conn_lost(gateway, error):
  """React when the connection is lost to the gateway device."""
  pass

GATEWAY.on_conn_lost = conn_lost
```

### Async gateway

The serial, TCP and MQTT gateways now also have versions that support asyncio. Use the
`AsyncSerialGateway` class, `AsyncTCPGateway` class or `AsyncMQTTGateway` class to make a gateway that
uses asyncio. The following public methods are coroutines in the async gateway:

- get_gateway_id
- start_persistence
- start
- stop
- update_fw

See [async_main.py](https://github.com/theolind/pymysensors/blob/master/async_main.py) for an example of how to use this gateway.

## Development

Install the packages needed for development.

```sh
pip install -r requirements_dev.txt
```

Use the Makefile to run common development tasks.

```sh
make
```

### Code formatting

We use black code formatter to automatically format the code.
This requires Python 3.6 for development.

```sh
black ./
```

### Release

See the [release instructions](RELEASE.md).

[build-badge]: https://github.com/theolind/pymysensors/workflows/Test/badge.svg
[build]: https://github.com/theolind/pymysensors/actions
