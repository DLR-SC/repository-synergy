Python wrapper for Digital Ocean API v2
=======================================

Simple and easy to use package that provides access to Digital Ocean API v2.


How To Install
==============

With **pip**

	pip install digitalocean-api

Or with **setuptools**

	python setup.py install


Examples
========

```python
>>> from digitalocean import ClientV2
>>> client = ClientV2(token='your_token_here')
>>> client.droplets.all()
{u'droplets': [{u'status': u'active', u'kernel': {u'version': u'2.6.32-431.1.2.0.1.el6.i686', u'id': 379, u'name': u'CentOS 6.x x32 vmlinuz-2.6.32-431.1.2.0.1.el6.i686'}, u'locked': False, u'name': u'dropletname.com', u'backup_ids': [], u'region': {u'available': True, u'sizes': [u'512mb', u'2gb', u'4gb', u'8gb', u'32gb', u'48gb', u'16gb', u'64gb', u'1gb'], u'features': [u'virtio', u'private_networking', u'backups'], u'slug': u'ams2', u'name': u'Amsterdam 2'}, u'snapshot_ids': [], u'networks': {u'v4': [{u'type': u'public', u'netmask': u'255.255.255.0', u'ip_address': u'188.xxx.xxx.xxx', u'gateway': u'188.xxx.xxx.1'}], u'v6': []}, u'vcpus': 1, u'features': [u'virtio'], u'image': {u'slug': u'centos-6-5-x32', u'name': u'CentOS 6.5 x32', u'created_at': u'2014-05-02T20:16:38Z', u'id': 3448674, u'regions': [u'nyc1', u'ams1', u'sfo1', u'nyc2', u'ams2', u'sgp1', u'lon1', u'nyc3', u'ams3'], u'distribution': u'CentOS', u'public': True}, u'memory': 1024, u'created_at': u'2014-08-13T12:15:58Z', u'disk': 30, u'id': 2323856, u'size': {u'price_monthly': 10.0, u'transfer': 2, u'slug': u'1gb', u'price_hourly': 0.01488}}], u'meta': {u'total': 1}}
>>> 
>>> client.droplets.get(droplet_id=2323856)
{u'droplet': {u'status': u'active', u'kernel': {u'version': u'2.6.32-431.1.2.0.1.el6.i686', u'id': 379, u'name': u'CentOS 6.x x32 vmlinuz-2.6.32-431.1.2.0.1.el6.i686'}, u'locked': False, u'name': u'dropletname.com', u'backup_ids': [], u'region': {u'available': True, u'sizes': [u'512mb', u'2gb', u'4gb', u'8gb', u'32gb', u'48gb', u'16gb', u'64gb', u'1gb'], u'features': [u'virtio', u'private_networking', u'backups'], u'slug': u'ams2', u'name': u'Amsterdam 2'}, u'snapshot_ids': [], u'networks': {u'v4': [{u'type': u'public', u'netmask': u'255.255.255.0', u'ip_address': u'188.xxx.xxx.xxx', u'gateway': u'188.xxx.xxx.1'}], u'v6': []}, u'vcpus': 1, u'features': [u'virtio'], u'image': {u'slug': u'centos-6-5-x32', u'name': u'CentOS 6.5 x32', u'created_at': u'2014-05-02T20:16:38Z', u'id': 3448674, u'regions': [u'nyc1', u'ams1', u'sfo1', u'nyc2', u'ams2', u'sgp1', u'lon1', u'nyc3', u'ams3'], u'distribution': u'CentOS', u'public': True}, u'memory': 1024, u'created_at': u'2014-08-13T12:15:58Z', u'disk': 30, u'id': 2323856, u'size': {u'price_monthly': 10.0, u'transfer': 2, u'slug': u'1gb', u'price_hourly': 0.01488}}}
>>> 
>>> client.droplets.shutdown(droplet_id=2323856)
{u'action': {u'status': u'in-progress', u'resource_id': 2323856, u'region': u'ams2', u'completed_at': None, u'started_at': u'2014-09-15T11:04:36Z', u'type': u'shutdown', u'id': 32469004, u'resource_type': u'droplet'}}
>>> 
>>> client.droplets.get_droplet_action(droplet_id=2323856, action_id=32469004)
{u'action': {u'status': u'completed', u'resource_id': 2323856, u'region': u'ams2', u'completed_at': u'2014-09-15T11:05:13Z', u'started_at': u'2014-09-15T11:04:36Z', u'type': u'shutdown', u'id': 32469004, u'resource_type': u'droplet'}}
```


TODO
====

1. Documentation
2. Dealing with pagination
3. Better API with manager and models
