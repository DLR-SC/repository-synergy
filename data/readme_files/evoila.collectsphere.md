# collectsphere
This is a Collectd Plugin for VMware vSphere. It fetches performance data via the vSphere API at very good performance
which makes it suitable for medium to large environments.

## Installation
Run
> python setup.py install

This would install the collectsphere module. Add the `collectsphere.conf ` in the including collect configuration folder (usually `/etc/collectd.d` )
or add this to the collectd configuration file:
```
TypesDB "./vmware-types.db"


<LoadPlugin "python">
    Globals true
</LoadPlugin>

<Plugin "python">
    Import "collectsphere"
    <Module "collectsphere">
        Name "SOME_NAME"
        Host "FQDN"
        Port "443"
        Verbose true
        VerifyCertificate true
        UseFriendlyName false
        Username "USERNAME"
        Password "PASSWORD"
        Host_Counters "cpu.usage,mem.usage,disk.usage"
        VM_Counters "cpu.usage,mem.usage"
    </Module>
</Plugin>
```
Please note there is a special TypesDB for collectsphere. Change the path in the first line to the `vmware.types.db` file on your system.



## Configuration
Key | Description
 --- | ---
**Name** | The `Name` is a name for the environment. At the moment this is only used for internal usage.
**Host** | The `Host` is a FQDN or an IP of a vSphere Server or ESX system, e.g. *vsphere.local* or *10.0.0.10*. 
**Port** | The `Port` is the same port as the vSphere web client access port (usually 443 or 9443).
**VerifyCertificate** | When using self-signed certificates set this option to false
**UseFriendlyName** | Instead of the internal VMware Managed Object ID, you can use friendly names, which are the names of the entity for mnonitoring. <br> *Be careful, when instances have the same name, they could not divided anymore*
**Username** | A ESX/Vsphere user with `System.View` and `Performance.ModifyIntervals` privileges.
**Password** | Password for the above user
**Counters** | ;TBD

### Graphite
If you use the [write_graphite](https://collectd.org/documentation/manpages/collectd.conf.5.shtml#plugin_write_graphite)-plugin of collectd, it is helpful to use the following configuration with it:
```
EscapeCharacter "."
SeparateInstances true
```
## Naming schema
We are using the following naming schema for the type in collectsphere:
`< collectsphere_host >/collectsphere/< VMware-Type in vmware.types.db >-< Cluster >.< Host|VM >.< metric-instance >`
All non alphamerically chars would be replaced with underscore.
For more information see [collectd Naming schema](https://collectd.org/wiki/index.php/Naming_schema)

## Features
- Fetch ESXi host metrics
- Fetch VM metrics
- Awareness of VMware HA/DRS clusters
- Very good performance
- Automatic inventory discovery

## Testing
Development and testing was conducted with ...
- vSphere version: 5.5
- vCenter type: linux appliance 

## Why Collectd?
A Collectd plugin allows to use existing infrastructure in collectd to start/stop/execute the plugin and forward values
to existing backends. Like this you can easily send the information gathered to for example Graphite and create nice
looking dashboards with e.g. Grafana. (This was the primary goal of this project.)

# Screenshot from Grafana
![](https://raw.githubusercontent.com/evoila/collectsphere/master/screenshots/vms-view.png)

