Network Configuration Generator
===============================

This Web application is a simple configuration generator for network equipment like Routers and Switches.

It is based on python3 and the [Flask microframework](http://flask.pocoo.org). If you like to know more about the Use Case and development of this Web service, take a look on the associated blog series "[How to build your own configuration generator](https://codingnetworker.com/2015/12/network-configuration-generator/)".

The following images shows an example configuration template and the associated variable definition.

![example template](/app/static/images/example_template.png)

## Install the application

**Please Note: All setup scripts assume that this Web service and the associated services like TFTP are the only service running on the server.**

There are multiple ways to run this Web service:

  * on a Linux server (recommended is Ubuntu 16.04)
  * as a Vagrant VM (see Vagrantfile)
  * on Raspberry PI (tested with raspbian/jessie)

The configuration of the Web service depends on the `APP_SETTINGS` environment variable. The following values are possible.

| Configuration value           | used for                                                 |
| ----------------------------- | -------------------------------------------------------- |
| `config.DefaultConfig`        | default configuration                                    |
| `config.ProductionConfig`     | configuration for a production environment (recommended) |
| `config.TestConfig`           | configuration for unit-tests                             |
| `config.LiveServerTestConfig` | configuration for selenium-tests                         |

If the `APP_SETTINGS` variable is not set, the `DefaultConfig` is used. Furthermore, the `SECRET_KEY` variable is used to define a key value for the CSRF protection. Within a production environment, this key is dynamically created within the setup script.

### on Ubuntu Linux (16.04)

To setup the Web service on a Ubuntu machine, use the following commands:

```Shell
$ git clone https://github.com/hoelsner/network-config-generator.git network_config_generator
$ cd network_config_generator
$ ./setup_ubuntu.sh
```

Follow the instructions from the setup script.

Within the repository, you'll also find a Vagrantfile. To setup the Web service using [Vagrant](vagrantup.com), use the following commands:

```Shell
$ git clone https://github.com/hoelsner/network-config-generator.git network_config_generator
$ cd network_config_generator
$ vagrant up ncg
```

The setup script that is used in this case works totally unattended and will create a VM based on Ubuntu 16.04. It will also setup the FTP and TFTP service on the server.

### on a Raspberry PI

During the development, I wrote a post about the [use of a Raspberry PI as a Provisioning Appliance](https://codingnetworker.com/2016/02/using-a-raspberry-pi-as-a-configuration-generator/). At this point, I include a FTP and TFTP server to provide the configurations to the outside world. Furthermore, I add the Shell in a Box service and the Appliance Status view.

![Appliance Status view](/app/static/images/how_to/appliance_status.png)

### on your local machine

To run an instance on your local machine (for demo or testing), you need to execute the following steps:

#### 1. clone the repository

```Shell
$ git clone https://github.com/hoelsner/network-config-generator.git network_config_generator
$ cd network_config_generator
```

#### 2. create a virtualenv and install python dependencies

```Shell
$ virtualenv -p /usr/bin/python3 venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
```

#### 3. run the local server

```Shell
(venv) $ python3 run_local.py
Initialize database...
Start the Network Configuration Generator on port 5000...
```

After this step, the Network Configuration Generator is running without any external service (no TFTP, no integration options).

If you like to use the "export to TFTP/FTP directory" (or any asynchronous action), you need to run a redis-server and celery worker thread on your local system. After installing the redis-server, execute the following command in another terminal window to start the celery worker thread:

```Shell
(venv) $ export APP_SETTINGS=config.DefaultConfig
(venv) $ celery worker -A app.celery --loglevel=info
```

## license

See the [license](LICENSE.md) file for license rights and limitations (MIT).

## development and testing

To enable the debug mode of the Web service, set the `DEBUG_MODE` environment variable to `1`. This will also enable the logging to the console.

The `tests` directory contains all unit and functional test-cases for the Web service. Use the following command to run all test cases bundled with this application (assuming you already created a virtualenv and installed the dependencies from the `requirements.txt` and `requirements_text.txt`):

```Shell
(venv) $ python3 -m unittest tests.run_tests_all
```

Prior testing, you need to install and start the redis-server. Furthermore, you need to start a celery worker thread using the following commands:

```Shell
export APP_SETTINGS=config.TestConfig
celery worker -A app.celery --loglevel=debug --autoreload
```
