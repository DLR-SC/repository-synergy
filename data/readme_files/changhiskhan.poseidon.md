poseidon
========

Python library for managing your Digital Ocean account via API v2

[![PyPi version](https://pypip.in/v/poseidon/badge.png)](https://crate.io/packages/poseidon/)
[![PyPi downloads](https://pypip.in/d/poseidon/badge.png)](https://crate.io/packages/poseidon/)

The DigitalOcean API allows you to manage Droplets and resources within the
DigitalOcean cloud in a simple, programmatic way using conventional HTTP
requests. The endpoints are intuitive and powerful, allowing you to easily make
calls to retrieve information or to execute actions.

All of the functionality that you are familiar with in the DigitalOcean control
panel is also available through the API, allowing you to script the complex
actions that your situation requires.

This library starts with a python wrapper for the API and aims to build tools to
make it easier to manage, provision, and deploy to Digital Ocean.

Highlights
----------
*Full featured* : API wrapper covering the published DigitalOcean API v2
*Tested* : integration test coverage against most of the API
*SSH integration*: integrates `paramiko` library so you can SSH in and issue commands
*Deployment conveniences*: methods like `apt`, `pip`, and `git` for easier deployment


Setup
-----

`pip install -U poseidon`

To run the unit tests make sure you have the `pytest` module.
If not, run `pip install -U pytest`


Examples
--------

Setup authentication by generating an API key and exporting it as the value of the
`DIGITALOCEAN_API_KEY` environment variable.


### Connect to API
```
import poseidon
client = poseidon.connect() # or poseidon.connect(api_key=<KEY>) for custom api key
```

### Create a droplet
```
image_id = 135123 # replace with your own
key_id = 175235 # e.g., client.keys.list()[0]['id']
droplet = client.droplets.create(name='test', region='sfo1', size='512mb',
                                 image=image_id, ssh_keys=[key_id])
```

### Programmatically create a snapshot
```
droplet.power_off() # snapshots are only allowed while powered off
droplet.take_snapshot('test-snapshot')
```

### Check that it worked
```
snapshots = droplet.snapshots() # one of these should be named 'test-snapshot'
```

### Issuing commands to the droplet via SSH
poseidon connects to your droplet via SSH using the `paramiko` library

#### Create a connection

```
ssh = droplet.connect()
```

#### Install system packages

```
ssh.apt('git python-pip')
```

#### Clone a github repo

```
# requires GITHUB_TOKEN envvar
ssh.git(username='changhiskhan', repo='hello_world')
```

#### Change directory

```
ssh.chdir('hello_world')
```

#### pip install -r
`ssh.pip_r('requirements.txt')`

#### Launch application
```
ssh.nohup('python app.py')
```

#### Check processes
```
print ssh.ps()
```



Other API Features
------------------

### Other simple droplet commands
```
droplet.reboot()
droplet.shutdown()
droplet.power_on()
droplet.power_cycle()
droplet.password_reset()
droplet.enable_ipv6()
droplet.disable_backups()
droplet.enable_private_networking()
```

### Droplet commands that take a parameter
```
droplet.resize('1024mb')
droplet.restore(image_id) # integer
droplet.rebuild(image_id)
droplet.rename('new-name')
droplet.change_kernel(12534)
```

### Delete droplet
`droplet.delete()`

### Keys
```
# list keys
client.keys.list() # it works

# create a new key
public_key = ("ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAQQDWF7SdoK0JvdjGR/8MHjj"
              "b7qtKVSdqoVZ2bCX0SXdn2pxZitnFjUx+lQ4osMGjOOTE/Hi86qQnFGE8Ym"
              "Sur/LT example")
key = client.keys.create('test-key', public_key)
print rs['public_key']
print rs['name']

# rename the key
client.keys.update(key['id'], 'test-key2')

# delete the key
client.keys.delete(new_id)
```

### Domains
```
# list domains
client.domains.list() # it works

# create new domain
ip_address = '127.0.0.1'
test = 'b7qtKVSdqoVZ2bCX0SXdn2pxZitnFjUx.com' # must be unique
domain = client.domains.create(test, ip_address)
print domain['name']

# retrieve a domain by name
new_domain = client.domains.get(domain['name'])

# delete a domain by name
client.domains.delete(new_domain['name'])
```

### Regions
`client.regions.list()`
### Sizes
`client.sizes.list()`


Testing
-------
```
pip install -U pytest
py.test
```

Because the test for droplets goes through the exercise of creating a new droplet,
modifying it, then finally destroying it, the test takes a long time to run.
To only run the other tests, use the `not slow` marker from `pytest`:

```
py.test -v -m "not slow"
```
