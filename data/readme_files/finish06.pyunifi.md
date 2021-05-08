[![PyPI version](https://badge.fury.io/py/pyunifi.svg)](https://badge.fury.io/py/pyunifi)
[![Build Status](https://travis-ci.org/finish06/pyunifi.svg?branch=master)](https://travis-ci.org/finish06/pyunifi)


PyUnifi
=========

---
A rewrite of https://github.com/unifi-hackers/unifi-lab in cleaner Python.
Forked from https://github.com/calmh/unifi-api due to unmaintained status and rewritten to use the Requests module.

Development & Pull Request
--------------------------
Perform all pull requests against the development branch.  Pull requests against the master branch will not be merged, but closed.

Install
-------

    sudo pip install -U pyunifi

API Example
-----------

```python
from pyunifi.controller import Controller
c = Controller('192.168.1.99', 'admin', 'p4ssw0rd')
for ap in c.get_aps():
	print 'AP named %s with MAC %s' % (ap.get('name'), ap['mac'])
```

See also the scripts `unifi-ls-clients` and `unifi-low-rssi-reconnect` for more
examples of how to use the API.

API
---

### `class Controller`

Interact with a UniFi controller.

Uses the JSON interface on port 8443 (HTTPS) to communicate with a UniFi
controller. Operations will raise unifi.controller.APIError on obvious
problems (such as login failure), but many errors (such as disconnecting a
nonexistant client) will go unreported.

### `__init__(self, host, username, password)`

Create a Controller object.

 - `host`		-- the address of the controller host; IP or name
 - `username`	-- the username to log in with
 - `password`	-- the password to log in with
 - `port`		-- the port of the controller host
 - `version`	-- the base version of the controller API [v4|v5]
 - `site_id`	-- the site ID to access
 - `ssl_verify`	-- Verify the controllers SSL certificate, default=True, can also be False or "path/to/custom_cert.pem"

### `block_client(self, mac)`

Add a client to the block list.

 - `mac` -- the MAC address of the client to block.

### `disconnect_client(self, mac)`

Disconnects a client, forcing them to reassociate. Useful when the
connection is of bad quality to force a rescan.

 - `mac` -- the MAC address of the client to disconnect.

### `get_alerts(self)`

Return a list of Alerts.

### `get_alerts_unarchived(self)`

Return a list of unarchived Alerts.

### `get_events(self)`

Return a list of Events.

### `get_aps(self)`

Return a list of all AP:s, with significant information about each.

### `get_clients(self)`

Return a list of all active clients, with significant information about each.

### `get_statistics_last_24h(self)`

Return statistical data of the last 24h

### `get_statistics_24h(self, endtime)`

Return statistical data last 24h from endtime

 - `endtime` -- the last time of statistics.

### `get_users(self)`

Return a list of all known clients, with significant information about each.

### `get_user_groups(self)`

Return a list of user groups with its rate limiting settings.

### `update_user_group(self, group_id, down_kbps=-1, up_kbps=-1)`

Update user group bandwidth settings.

- `group_id` -- Group ID to modify.
- `down_kbps` -- New bandwidth in KBPS for download.
- `up_kbps` -- New bandwidth in KBPS for upload.

### `get_healthinfo(self)`

Return high level health information on status of the setup

### `get_wlan_conf(self)`

Return a list of configured WLANs with their configuration parameters.

### `restart_ap(self, mac)`

Restart an access point (by MAC).

 - `mac` -- the MAC address of the AP to restart.

### `restart_ap_name(self, name)`

Restart an access point (by name).

 - `name` -- the name address of the AP to restart.

### `unblock_client(self, mac)`

Remove a client from the block list.

 - `mac` -- the MAC address of the client to unblock.

### `archive_all_alerts(self)`

Archive all alerts of site.

### `create_backup(self)`

Tells the controller to create a backup archive that can be downloaded with download_backup() and
then  be used to restore a controller on another machine.

Remember that this puts significant load on a controller for some time (depending on the amount of users and managed APs).

### `get_backup(self, targetfile)`

Tells the controller to create a backup archive and downloads it to a file. It should have a .unf extension for later restore.

 - `targetfile` -- the target file name, you can also use a full path. Default creates unifi-backup.unf in the current directoy.

### `authorize_guest(self, guest_mac, minutes, up_bandwidth=None, down_bandwidth=None, byte_quota=None, ap_mac=None)`

Authorize a guest based on his MAC address.

   - `guest_mac`     -- the guest MAC address : aa:bb:cc:dd:ee:ff
   - `minutes`      -- duration of the authorization in minutes
   - `up_bandwith`  -- up speed allowed in kbps (optional)
   - `down_bandwith` -- down speed allowed in kbps (optional)
   - `byte_quota`    -- quantity of bytes allowed in MB (optional)
   - `ap_mac`        -- access point MAC address (UniFi >= 3.x) (optional)

### `unauthorize_guest(self, guest_mac)`
Unauthorize a guest based on his MAC address.

  - `guest_mac` -- the guest MAC address : aa:bb:cc:dd:ee:ff

### `set_client_alias(self, mac, alias)`
Set client alias. Use "" to reset to the default.
  - mac: The target MAC: aa:bb:cc:dd:ee:ff
  - alias: The alias to set

### `create_voucher(self, number, quota, expire, up_bandwidth=None, down_bandwidth=None, byte_quota=None, note=None)`
Create voucher for guests. Return list of new vouchers.

  - `number`          -- number of vouchers
  - `quota`           -- maximal number of using; 0 = unlimited
  - `expire`          -- expiration of vouchers in minutes
  - `up_bandwidth`    -- up speed allowed in kbps (optional)
  - `down_bandwidth`  -- down speed allowed in kbps (optional)
  - `byte_quota`      -- quantity of bytes allowed in MB (optional)
  - `note`            -- description of vouchers (optional)

### `list_vouchers(self, **filter)`
Get list of vouchers.

  - `filter`  --  Voucher filter  (create_time, code, quota, used, note, status_expires, status, ...)

```
  c.list_vouchers(code='12345-67890')
```

### `delete_voucher(self, id)`
Delete / revoke voucher.

  - `id`    -- voucher id

### `get_device_stat(self, target_mac)`
Gets the current state & configuration of the given device based on its MAC Address.

  - `target_mac` -- MAC address of the device

### `get_switch_port_overrides(self, target_mac)`
Gets a list of port overrides, in dictionary format, for the given target MAC address. The dictionary contains the port_idx, portconf_id, poe_mode, & name.

  - `target_mac` -- MAC address of the device

### `switch_port_power_off(self, target_mac, port_idx)`
Powers Off the given port on the Switch identified by the given MAC Address.

  - `target_mac` -- MAC address of the device
  - `port_idx`   -- Port ID to power off

### `switch_port_power_on(self, target_mac, port_idx)`
Powers On the given port on the Switch identified by the given MAC Address.

  - `target_mac` -- MAC address of the device
  - `port_idx`   -- Port ID to power on

Utilities
---------

The following small utilities are bundled with the API:

### unifi-ls-clients

Lists the currently active clients on the networks. Takes parameters for
controller, username, password, controller version and site ID (UniFi >= 3.x)

```
jb@unifi:~ % unifi-ls-clients -c localhost -u admin -p p4ssw0rd -v v3 -s default
NAME                             MAC  AP            CHAN  RSSI   RX   TX
client-kitchen     00:24:36:9a:0d:ab  Study          100    51  300  216
jborg-mbp          28:cf:da:d6:46:20  Study          100    45  300  300
jb-iphone          48:60:bc:44:36:a4  Living Room      1    45   65   65
jb-ipad            1c:ab:a7:af:05:65  Living Room      1    22   52   65
```

### unifi-low-snr-reconnect

Periodically checks all clients for low SNR values, and disconnects those who
fall below the limit. The point being that these clients will then try to
reassociate, hopefully finding a closer AP. Take the same parameters as above,
plus settings for intervals and SNR threshold. Use `unifi-low-snr-reconnect -h`
for an option summary.

A good source of understanding for RSSI/SNR values is [this
article](http://www.wireless-nets.com/resources/tutorials/define_SNR_values.html).
According to that, an SNR of 15 dB seems like a good cutoff, and that's also
the default value in the script. You can set a higher value for testing:

```
jb@unifi:~ % unifi-low-snr-reconnect -c localhost -u admin -p p4ssw0rd -v v3 -s default --minsnr 30
2012-11-15 11:23:01 INFO unifi-low-snr-reconnect: Disconnecting jb-ipad/1c:ab:a7:af:05:65@Study (SNR 22 dB < 30 dB)
2012-11-15 11:23:01 INFO unifi-low-snr-reconnect: Disconnecting Annas-Iphone/74:e2:f5:97:da:7e@Living Room (SNR 29 dB < 30 dB)
```

For production use, launching the script into the background is recommended...

### unifi-save-statistics

Get a csv file with statistics

```
unifi-save-statistics -c localhost -u admin -p p4ssw0rd -v v3 -s default -f filename.csv
```


License
-------

MIT
