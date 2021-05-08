# Black Nurse DOS POC

Blacknurse is a low bandwidth ICMP attack that is capable of doing denial of service to well known firewalls. Most ICMP attacks that we see are based on ICMP Type 8 Code 0 also called a ping flood attack. BlackNurse is based on ICMP with Type 3 Code 3 packets. We know that when a user has allowed ICMP Type 3 Code 3 to outside interfaces, the BlackNurse attack becomes highly effective even at low bandwidth. Low bandwidth is in this case around 15-18 Mbit/s. This is to achieve the volume of packets needed which is around 40 to 50K packets per second. It does not matter if you have a 1 Gbit/s Internet connection. The impact we see on different firewalls is typically high CPU loads. When an attack is ongoing, users from the LAN side will no longer be able to send/receive traffic to/from the Internet. All firewalls we have seen recover when the attack stops.

### Vulnerable systems


 * Cisco ASA 5505, 5506, 5515, 5525 , 5540 (default settings)
 * Cisco 6500 routers with SUP2T and Netflow v9 on the inbound interface - 100% CPU load
 * Cisco ASA 5550 (Legacy) and 5515-X (latest generation)
 * Cisco Router 897 - Can be mitigated - The current code from https://www.cymru.com/Documents/secure-ios-template.html will make evil worse.
 * SonicWall - Misconfiguration can be changed and mitigated (Enable Anti-DDOS)
 * Palo Alto 5050 Firewalls with firmware 7.1.4-h2 
 * Zyxel NWA3560-N (Wireless attack from LAN Side)
 * Zyxel Zywall USG50
 * Fortinet v5.4.1 - One CPU consumed
 * Fortigate units 60c and 100D (even with drop ICMP on)

### Tested not vulnerable

 * Iptables (Netfilter even with 480 Mbit/sec)
 * mikrotik CCR1036-12G-4S firmware: 3.27 (250 Mbit/sec) and no problem && RouterOS 5.4 on Mikrotik RB750
 * OpenBSD 6.0 and current
 * Windows Firewalls
 * pfSense
 * GigaVUE HC-Serie (Gigamon)
 * AVM Fritz!Box 7360 (common ADSl router in Germany)
 * Ubiquiti Networks - EdgeRouter Lite CPU 60-70% load but still going
 * Cisco ISR4321 Router IOS XE - Version 15.5(3)S2, RELEASE SOFTWARE (fc2)
 * Check Point Security Gateways
 * Juniper SRX

## Mitigation

### Cisco ASA 5550 (Legacy) and 5515-X (latest generation) 

To mitigate this attack on Cisco routers the following commands can help

    icmp deny any unreachable outside
    icmp deny any time outside

## C compilation

    gcc exploit.c -o blacknurse
    ./blacknurse <target ip>

## Python Dependencies

 * Python 2.6 or 2.7
 * Scapy
 * argparse (included with Python >= 2.7 and >= 3.2)

### Scapy installation on Debian 

    apt-get install python-scapy

### Scapy installation with pip

    pip install scapy

### Original author

This code was based on a Perl implementation of this attack by Todor Donev and this flaw was discovered by Kenneth B. Jørgensen and Lenny Hansson, thanks guys !

### Disclaimer

This or previous program is for Educational purpose ONLY. Do not use it without permission. The usual disclaimer applies, especially the fact that me (opsxcq) is not liable for any damages caused by direct or indirect use of the information or functionality provided by these programs. The author or any Internet provider bears NO responsibility for content or misuse of these programs or any derivatives thereof. By using these programs you accept the fact that any damage (dataloss, system crash, system compromise, etc.) caused by the use of these programs is not opsxcq's responsibility.
