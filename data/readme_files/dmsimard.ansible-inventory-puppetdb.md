# ansible-inventory-puppetdb
Leverage Puppet facts and PuppetDB to generate a dynamic Ansible inventory

Usage
=====

    ./puppetdb.py -h
    usage: puppetdb.py [-h] (--list | --host HOST)

    PuppetDB Inventory Module

    optional arguments:
      -h, --help   show this help message and exit
      --refresh    Refreshes cached information
      --list       List servers known by PuppetDB
      --host HOST  List details about specified host

Configuration
=============

See in-file documentation provided in [puppetdb.yml](https://github.com/dmsimard/ansible-inventory-puppetdb/blob/master/puppetdb.yml)

Notes on large(r) amount of hosts in a single PuppetDB instance
---------------------------------------------------------------
If you are dealing with a large(r) amount of hosts in a single PuppetDB instance, what becomes important for improving performance is:

1. The JSON library to encode and decode data for Ansible to use
> The script will automatically attempt to load, in order of performance: ujson > simplejson > json (stdlib). For best results, try to install ujson.

2. Latency between where you run the inventory script and the PuppetDB instance
> Try to run the inventory somewhere with as little latency as you can to your PuppetDB instance.

3. Performance of the server the inventory is run on

4. Performance of the PuppetDB server

Usage example
=============

    ./puppetdb.py --host node.domain.tld
    {
      "node.domain.tld": {
        "_timestamp": "Fri Mar 13 20:05:48 -0400 2015",
        "ansible_ssh_host": "node.domain.tld",
        "architecture": "amd64",
        "augeasversion": "0.10.0",
        "bios_release_date": "03/31/2014",
        "bios_vendor": "American Megatrends Inc.",
        "bios_version": "3.0a",
        "blockdevice_sda_model": "SMC2108",
        "blockdevice_sda_size": "955999322112",
        "blockdevice_sda_vendor": "SMC",
        "blockdevices": "sda",
        "boardmanufacturer": "Supermicro",
        "boardproductname": "X9DR3-F",
        "boardserialnumber": "VM138S020078",
        "clientcert": "node.domain.tld",
        "clientnoop": "false",
        "clientversion": "3.7.4",
        "concat_basedir": "/var/lib/puppet/concat",
        "domain": "domain.tld",
        "facterversion": "2.0.1",
        "filesystems": "ext3,ext4,vfat",
        "fqdn": "node.domain.tld",
        "hardwareisa": "x86_64",
        "hardwaremodel": "x86_64",
        "hostname": "node05",
        "id": "root",
        "interfaces": "bond0,eth0,eth1,lo",
        "ip6tables_version": "1.4.12",
        "ipaddress": "192.168.1.2",
        "ipaddress_bond0": "192.168.1.2"
        "ipaddress_lo": "127.0.0.1",
        "iptables_version": "1.4.12",
        "is_pe": "false",
        "is_virtual": "false",
        "kernel": "Linux",
        "kernel_ipv6_disable": "false",
        "kernelmajversion": "3.11",
        "kernelrelease": "3.11.0-20-generic",
        "kernelversion": "3.11.0",
        "lsbdistcodename": "precise",
        "lsbdistdescription": "Ubuntu 12.04.4 LTS",
        "lsbdistid": "Ubuntu",
        "lsbdistrelease": "12.04",
        "lsbmajdistrelease": "12",
        "macaddress": "00:25:90:ca:43:d8",
        "macaddress_bond0": "00:25:90:ca:43:d8",
        "macaddress_eth0": "00:25:90:CA:43:D8",
        "macaddress_eth1": "00:25:90:CA:43:D9",
        "manufacturer": "Supermicro",
        "memoryfree": "124.62 GB",
        "memoryfree_mb": "127615.09",
        "memorysize": "125.89 GB",
        "memorysize_mb": "128908.46",
        "mtu_bond0": "1500",
        "mtu_eth0": "1500",
        "mtu_eth1": "1500",
        "mtu_lo": "65536",
        "netmask": "255.255.255.0",
        "netmask_lo": "255.0.0.0",
        "netmask_bond0": "255.255.255.0"
        "network_lo": "127.0.0.0",
        "network_bond0": "192.168.1.0"
        "operatingsystem": "Ubuntu",
        "operatingsystemrelease": "12.04",
        "osfamily": "Debian",
        "path": "/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin",
        "physicalprocessorcount": "2",
        "processor0": "Intel(R) Xeon(R) CPU E5-2650 v2 @ 2.60GHz",
        "processor1": "Intel(R) Xeon(R) CPU E5-2650 v2 @ 2.60GHz",
        "processor10": "Intel(R) Xeon(R) CPU E5-2650 v2 @ 2.60GHz",
        "processor11": "Intel(R) Xeon(R) CPU E5-2650 v2 @ 2.60GHz",
        "processor12": "Intel(R) Xeon(R) CPU E5-2650 v2 @ 2.60GHz",
        "processor13": "Intel(R) Xeon(R) CPU E5-2650 v2 @ 2.60GHz",
        "processor14": "Intel(R) Xeon(R) CPU E5-2650 v2 @ 2.60GHz",
        "processor15": "Intel(R) Xeon(R) CPU E5-2650 v2 @ 2.60GHz",
        "processor16": "Intel(R) Xeon(R) CPU E5-2650 v2 @ 2.60GHz",
        "processor17": "Intel(R) Xeon(R) CPU E5-2650 v2 @ 2.60GHz",
        "processor18": "Intel(R) Xeon(R) CPU E5-2650 v2 @ 2.60GHz",
        "processor19": "Intel(R) Xeon(R) CPU E5-2650 v2 @ 2.60GHz",
        "processor2": "Intel(R) Xeon(R) CPU E5-2650 v2 @ 2.60GHz",
        "processor20": "Intel(R) Xeon(R) CPU E5-2650 v2 @ 2.60GHz",
        "processor21": "Intel(R) Xeon(R) CPU E5-2650 v2 @ 2.60GHz",
        "processor22": "Intel(R) Xeon(R) CPU E5-2650 v2 @ 2.60GHz",
        "processor23": "Intel(R) Xeon(R) CPU E5-2650 v2 @ 2.60GHz",
        "processor24": "Intel(R) Xeon(R) CPU E5-2650 v2 @ 2.60GHz",
        "processor25": "Intel(R) Xeon(R) CPU E5-2650 v2 @ 2.60GHz",
        "processor26": "Intel(R) Xeon(R) CPU E5-2650 v2 @ 2.60GHz",
        "processor27": "Intel(R) Xeon(R) CPU E5-2650 v2 @ 2.60GHz",
        "processor28": "Intel(R) Xeon(R) CPU E5-2650 v2 @ 2.60GHz",
        "processor29": "Intel(R) Xeon(R) CPU E5-2650 v2 @ 2.60GHz",
        "processor3": "Intel(R) Xeon(R) CPU E5-2650 v2 @ 2.60GHz",
        "processor30": "Intel(R) Xeon(R) CPU E5-2650 v2 @ 2.60GHz",
        "processor31": "Intel(R) Xeon(R) CPU E5-2650 v2 @ 2.60GHz",
        "processor4": "Intel(R) Xeon(R) CPU E5-2650 v2 @ 2.60GHz",
        "processor5": "Intel(R) Xeon(R) CPU E5-2650 v2 @ 2.60GHz",
        "processor6": "Intel(R) Xeon(R) CPU E5-2650 v2 @ 2.60GHz",
        "processor7": "Intel(R) Xeon(R) CPU E5-2650 v2 @ 2.60GHz",
        "processor8": "Intel(R) Xeon(R) CPU E5-2650 v2 @ 2.60GHz",
        "processor9": "Intel(R) Xeon(R) CPU E5-2650 v2 @ 2.60GHz",
        "processorcount": "32",
        "productname": "X9DR3-F",
        "ps": "ps -ef",
        "puppet_vardir": "/var/lib/puppet",
        "puppetversion": "3.7.4",
        "root_home": "/root",
        "rubysitedir": "/usr/local/lib/site_ruby/1.8",
        "rubyversion": "1.8.7",
        "selinux": "false",
        "serialnumber": "0123456789",
        "sshdsakey": "AAAAB3NzaC1kc3MAAACBAJp0queeP6ygTExbmJZ+oF67DqTIrYsnCzwaKNsF1FmZTGlBwk89cgQJtmaiH0llMDzfpujo//NoEtHM/rp+LW/4lBDbk1xpvXQFwRYg+Oja/Uf5PkXljvW9WpchMbhMtXdhaHYiRtICxoB+og1De4VFB6bbV/6QIiT82mGeqWKlAAAAFQCqhMaZHl8vcBsqeOcJMr6K06NQjwAAAIBv+tNfnYyPMu54U1XcSuyPnHu39LsotL+xl3Zym6pj3HIQ9UfBfOztJUW0tXbWQmEMsCaaCkcwVaYNm3ZqZfHLs7WVRWqNEpHfYBLZzuxnlrUfZfVy041GS3cRf9vlL2VWhPGBn2Es/Lvidglvl9r6GowEOzERanVLXwdxPZJNCwAAAIBYrGqEfvx7JPDhKYxrb6VIVbEqoYg/xhwIRubyrwfaNNtgWS6smhIN5OgbzxLeiYZLoSbrBUxUZg9Zn02/5IWG1bCkrKaaDQr7g8l3ofVN3vPRsVliNTfLRr3CvloFCojFM7QgvrtLcaFDVpCH6IyhIETgMOuN5lYKOSm3QtKgMQ==",
        "sshecdsakey": "AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBI1Y0kAB9QGPP3q/HJ/sh8UoKiODQDNSzGsAb5TI5CRgObpEeCmKxrXC3fT8dyDpFjs3WwR1LiGNZNzjfQ1AxvE=",
        "sshfp_dsa": "SSHFP 2 1 a3a5c027c250ad2c36f5e294042dfe7dae5b3585\nSSHFP 2 2 d06cc98ce9b0e8796bbdbde23f2042c805ef8cc7834e28e66c6bee52547f06ec",
        "sshfp_ecdsa": "SSHFP 3 1 e61278fcc8b5920c57a8fbc205d15c7aedc9f4ee\nSSHFP 3 2 132ba8f2bccd83a071d7235d91c0cf661fa693b778267d7915fe9fcab4e27244",
        "sshfp_rsa": "SSHFP 1 1 0c64e5e41832d8eef545e1fb5b59dc9db2abb368\nSSHFP 1 2 c2d603d736902e54703720a1fbfad2b6d000b87c5cb309c7ddf73aa0a89d2c7a",
        "sshrsakey": "AAAAB3NzaC1yc2EAAAADAQABAAABAQCkEukWO5BdJsvlK68d4HKi3KHu1YvCRxZLDc50TPKG1JpEk0LHdb1qgAcIYnRdBZLBvW5rfCxEzaLQ9RWsichCLcihLGCjPQC3x1jZMhYR7qhtON8UGNxppfgtYCjnN1HiccB5hbtaRxmtZgMNcf6MOCiceNg4lRP85fnb+ry9XOwrbevMIeFwhnKkg8Rm9haD007xBb5qp9Fgn0oN0fhDIReMUXIfpijv1CF+5vPIesltNFYG/pscSc86ZKKt95LbCQ5f7mGSgre4s+6EmGapzwfxgtnyse68yGBRE+e5lr3wH9CSdjCXPUB4G8H2Wb7IpR0Gl73LuQ+tqlfHWHD7",
        "swapfree": "3.73 GB",
        "swapfree_mb": "3815.00",
        "swapsize": "3.73 GB",
        "swapsize_mb": "3815.00",
        "timezone": "EDT",
        "type": "Desktop",
        "uniqueid": "007f0101",
        "uptime": "62 days",
        "uptime_days": "62",
        "uptime_hours": "1511",
        "uptime_seconds": "5441389",
        "uuid": "CA902500-D843-0000-0000-000000000000",
        "virtual": "physical",
      }
    }


List example
============

__With group_by set to 'kernelversion'__

    {
      "_meta": {
        "hostvars": {
          "node01.domain.tld": {
            "_timestamp": "Fri Mar 13 22:06:06 -0400 2015",
            ...
            "kernelversion": "3.11.0",
            "lsbdistcodename": "precise",
            "lsbdistdescription": "Ubuntu 12.04.4 LTS",
            "lsbdistid": "Ubuntu",
            "lsbdistrelease": "12.04",
            "lsbmajdistrelease": "12",
            ...
          },
          "node02.domain.tld": {
            "_timestamp": "Fri Mar 13 22:06:06 -0400 2015",
            ...
            "kernelversion": "3.11.0",
            "lsbdistcodename": "precise",
            "lsbdistdescription": "Ubuntu 12.04.4 LTS",
            "lsbdistid": "Ubuntu",
            "lsbdistrelease": "12.04",
            "lsbmajdistrelease": "12",
            ...
          },
          "node03.domain.tld": {
            "_timestamp": "Fri Mar 13 22:06:06 -0400 2015",
            ...
            "kernelversion": "3.11.0",
            "lsbdistcodename": "precise",
            "lsbdistdescription": "Ubuntu 12.04.4 LTS",
            "lsbdistid": "Ubuntu",
            "lsbdistrelease": "12.04",
            "lsbmajdistrelease": "12",
            ...
          },
          "node04.domain.tld": {
            "_timestamp": "Fri Mar 13 22:06:06 -0400 2015",
            ...
            "kernelversion": "3.13.0",
            "lsbdistcodename": "precise",
            "lsbdistdescription": "Ubuntu 12.04.4 LTS",
            "lsbdistid": "Ubuntu",
            "lsbdistrelease": "12.04",
            "lsbmajdistrelease": "12",
            ...
          },
          "node05.domain.tld": {
            "_timestamp": "Fri Mar 13 22:06:06 -0400 2015",
            ...
            "kernelversion": "3.13.0",
            "lsbdistcodename": "precise",
            "lsbdistdescription": "Ubuntu 12.04.4 LTS",
            "lsbdistid": "Ubuntu",
            "lsbdistrelease": "12.04",
            "lsbmajdistrelease": "12",
            ...
          },
          "node06.domain.tld": {
            "_timestamp": "Fri Mar 13 22:06:06 -0400 2015",
            ...
            "kernelversion": "3.13.0",
            "lsbdistcodename": "precise",
            "lsbdistdescription": "Ubuntu 12.04.4 LTS",
            "lsbdistid": "Ubuntu",
            "lsbdistrelease": "12.04",
            "lsbmajdistrelease": "12",
            ...
          },
          "node07.domain.tld": {
            "_timestamp": "Fri Mar 13 22:06:06 -0400 2015",
            ...
            "kernelversion": "3.2.0",
            "lsbdistcodename": "precise",
            "lsbdistdescription": "Ubuntu 12.04.4 LTS",
            "lsbdistid": "Ubuntu",
            "lsbdistrelease": "12.04",
            "lsbmajdistrelease": "12",
            ...
          },
        }
      },
      "3.11.0": {
        "hosts": [
          "node01.domain.tld",
          "node02.domain.tld",
          "node03.domain.tld"
        ]
      },
      "3.13.0": {
        "hosts": [
          "node05.domain.tld",
          "node06.domain.tld"
        ]
      },
      "3.2.0": {
        "hosts": [
          "node07.domain.tld"
        ]
      },
      "all": {
        "hosts": [
          "node01.domain.tld",
          "node02.domain.tld",
          "node03.domain.tld",
          "node04.domain.tld",
          "node05.domain.tld",
          "node06.domain.tld",
          "node07.domain.tld"
        ]
      }
    }

__With group_by_tag set to__

```
#Puppet code example tagging class...
class webservices_tag {

  case $fqdn {
    /\-dev/: { tag 'web-development' }
    /\-production/: { tag 'web-production' }
  }

}
```

```
group_by_tag:
  - Class: web-development
  - Class: web-production
```

Snippet of tagged group being added...
```
 "web-development": {
   hosts: [ 'node01-dev.domain.tld', 'node02-dev.domain.tld' ]
 }
 "web-production": {
   hosts: [ 'node01-production.domain.tld', 'node02-production.domain.tld' ]
 }
```
