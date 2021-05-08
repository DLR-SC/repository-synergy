# ness6rest.py - a REST interface to Nessus 6
[![Build Status](https://travis-ci.org/tenable/nessrest.svg?branch=master)](https://travis-ci.org/tenable/nessrest)
[![PyPI Version](https://badge.fury.io/py/nessrest.svg)](https://pypi.python.org/pypi/nessrest)
### Dependencies:

* Nessus 6.4.x
* Python 2.7+ or 3.3+
* requests module (install via pip)
* The dependencies can be satisfied via `pip install -r requirements.txt`

### Quick Install
```
pip install nessrest
```

### Features:

* Logins

  ```python
  scan = ness6rest.Scanner(url="https://nessusscanner:8834", login="username", password="password")

  creds = [credentials.WindowsPassword(username="administrator", password="foobar"),
           credentials.WindowsPassword(username="administrator", password="barfoo"),
           credentials.SshPassword(username="nessususer", password="foobar")]

  scan.policy_add_creds(credentials=creds)
  ```
* Build policies

  ```python
  scan.upload(upload_file="file.audit")
  scan._policy_add_audit(category="Windows", filename="file.audit")
  scan.policy_add(name="Scripted Scan", plugins="21156")
  ```

* Launch scans

  ```python
  scan.scan_add(targets="192.168.0.1")
  scan.scan_run()
  ```

* Schedule scans
  ```python
  scan.scan_add(targets="192.168.0.1", start="YYYYMMDDTHHMMSS")
  ```

* Parse scan results

  ```python
  scan.scan_results()
  ```

* Download KB for target

  ```python
  kbs = scan.download_kbs()

  for hostname in kbs.keys():
      f = open(hostname, "w")
      f.write(kbs[hostname])
      f.close()
  ```

* Output for ticketing/wiki format

### Feature Requests:

* Deleting of a schedule
* Ability to change "tag" from CLI via config/CLI arg
* Enforce supported versions of Nessus

### Notes:
* Proxies are not supported, although transparent proxies should work... transparently

# nessrest - an example client

### Suggested installation:

* Find the path to your "site-packages" with: `python -c "import sys; print(sys.path)"`
* Symlink `ness6rest.py` in the Git repo in the "site-packages" or "dist-packages" directory.
* Test by issuing `import ness6rest` inside the Python interactive
  interpreter.

### Specifying a ca\_bundle

If you are using a corporate or self-signed SSL certificate, you can specify the path to a ca\_bundle to use for verification by passing it to the Scanner initializer:
  ```python
  scan = ness6rest.Scanner(url="https://nessusscanner:8834", login="username", password="password", ca_bundle="/path/to/ca_bundle.pem")
  ```

If you are using the ness\_rest client, you can pass this path on the command line using the --ca\_bundle option.

### Self-signed certificates

If you're running Nessus with a self-signed certificate, and you wish to disable SSL certificate checking, you can pass insecure=True to the Scanner initializer:
  ```python
  scan = ness6rest.Scanner(url="https://nessusscanner:8834", login="username", password="password", insecure=True)
  ```

If you're using the nessrest example client, it has an --insecure option that will do this.

Note that this will disable invalid SSL cerficate errors and should be used with caution.

### Configuration file:

* Copy `ness_rest.conf.example` to `ness_rest.conf` and configure for your scanner.
* There are several valid paths for the location of the config file(in order):
* The path passed from the CLI with `--config`
* A permanent config file is searched for in the following locations:
    * `$HOME/.ness_rest.conf`
    * `$HOME/.ness_rest/ness_rest.conf`
    * `/etc/ness_rest.conf`
    * `/etc/ness_rest/ness_rest.conf`
    * `$PWD/ness_rest.conf`

### Building modules:

* To build a package to install via `pip` or `easy_install`, execute:
    * `python setup.py sdist`
* The resulting build will be in `$PWD/dist/nessrest-<version>.tar.gz`
