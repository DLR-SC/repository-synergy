---

Provided as-is, currently not actively maintained.

[OctoPrint](http://octoprint.org) is eating up too much of my time and I don't find myself at liberty to actively maintain this project for the foreseeable future. If it works for you, great. If it doesn't, sorry, I can't look into it.

---

# netconnectd

netconnectd is a small daemon that ensures connectivity for single-PCB devices such as the Raspberry Pi where you don't 
always have the means to setup your network interfaces by hand.

It monitors your current link status by checking if there are any other systems reachable and if not fires up an access 
point (via [hostapd] and [dnsmasq]). Additionally it allows control and configuration via a unix domain socket and a command 
line client/JSON based command protocol that allows listing available wifi cells and configuring a wifi network to use 
instead of the AP in the future.

It is intended to be used as part of a connectivity solution, acting as the backend to a frontend e.g. in a web 
application running on the device.

netconnectd has been written to work with [Debian] based Linux distributions such as [Raspbian] or [Ubuntu] and is provided
under terms of the [AGPLv3] license.

[hostapd]: http://w1.fi/hostapd/
[dnsmasq]: http://www.thekelleys.org.uk/dnsmasq/doc.html
[Debian]: http://www.debian.org/
[Raspbian]: http://www.raspbian.org/
[Ubuntu]: http://www.ubuntu.com/
[AGPLv3]: https://www.gnu.org/licenses/agpl-3.0.en.html

## Motivation

The reason for writing a dedicated service to do that instead of just integrating that kind of functionality directly
in the client software is simply that I did want a solution which allowed configuration of wifi networks and
starting/stoping of access point mode through a piece of client software without the need for the client software
to need to run with superuser privileges (or a myriad of sudo rights having to be built up all around it).

Of course, there already exist such solutions, e.g. [NetworkManager] and [wicd], which allow configuration of network
connectivity via inter process communication. There are four problems with the existing solutions
though: They use DBUS for the inter process communication (which is rather targeted at desktop applications, not
at headless environments, and also brings a certain overhead to the table), they focus on the desktop environment,
they are tightly integrated with the existing system and do not offer much flexibility regarding specific needs of 
client applications in regards to special configuration options and - the biggest of the issues - don't support 
configuration of access point mode (at least not out of the box and without jumping through big hoops).

Therefore netconnectd was designed based on the following requirements:

  * Offer a very lightweight means of inter process communication (JSON messages via a Unix Domain Socket in that case)
  * Focus on headless environments (no UI)
  * Be as configurable in regards to used tooling as possible (by extensive configuration options via both a config
    file as well as during startup via command line arguments overriding anything else)
  * Be able to fire up an access point mode (via a combination of hostapd, dnsmasq as DHCP server and optionally also
    a bunch of iptable entries)

[NetworkManager]: https://wiki.gnome.org/Projects/NetworkManager
[wicd]: http://wicd.sourceforge.net/

## Setup

### Prepare the system

Install the hostapd, dnsmasq, logrotate and rfkill packages:

    sudo apt-get install hostapd dnsmasq logrotate rfkill

----

**Note for people updating**: Netconnectd now depends on the ``rfkill`` tool to be installed on the target system as
well, the above package installation instructions have since been updated to reflect this.

----

We don't want neither `hostapd` nor `dnsmasq` to automatically startup, so make sure their automatic start on boot is 
disabled:

    sudo update-rc.d -f hostapd remove
    sudo update-rc.d -f dnsmasq remove

You can verify that this worked by checking that there are no files left in `/etc/rc*.d` referencing those two services,
so the following to commands should return `0`:

    ls /etc/rc*.d | grep hostapd | wc -l
    ls /etc/rc*.d | grep dnsmasq | wc -l

If you are running NetworkManager (default for Ubuntu or other desktop linux distributions, usually not the case for 
Raspbian), make sure to disable its own `dnsmasq` by editing `/etc/NetworkManager/NetworkManager.conf` and commenting
out the line that says `dns=dnsmasq`, it should look something like this afterwards (note the `#` in front of the
`dns` line):

    [main]
    plugins=ifupdown,keyfile,ofono
    #dns=dnsmasq
    
    no-auto-default=00:22:68:1F:83:AF,
    
    [ifupdown]
    managed=false

You'll also need to modify `/etc/dhcp/dhclient.conf` to include a timeout setting, e.g.

    timeout 60;

Otherwise -- due to a limitation of how Debian/Ubuntu currently parses Wifi configurations in `/etc/network/interfaces` 
-- netconnectd won't be able to detect when it couldn't connect to your configured local wifi and will never start the 
access point mode. The value above will mean that it will take a maximum of 60sec before netconnectd will be notified 
by the system that the connection was unsuccessful -- you might want to lower that value even more but keep in mind that 
your wifi's DHCP server has to respond within that timeout for the connection to be considered successful.

### Check that your wifi card supports AP mode

Before you continue **make absolutely sure** that hostapd works with your wifi card/dongle! To test, create a file 
`/tmp/hostapd.conf` with the following contents:

    interface=wlan0
    driver=nl80211
    ssid=TestAP
    channel=3
    wpa=3
    wpa_passphrase=MySuperSecretPassphrase
    wpa_key_mgmt=WPA-PSK
    wpa_pairwise=TKIP CCMP
    rsn_pairwise=CCMP

Then run 

    sudo hostapd -dd /tmp/hostapd.conf

This should not show any errors but start up a new access point named "TestAP" and with passphrase 
"MySuperSecretPassphrase", verify that with a different wifi enabled device (e.g. mobile phone).

If you run into errors in this step, solve them first, e.g. by googling your wifi dongle plus "hostapd". You might need 
a custom version of hostapd (e.g. for the [Edimax EW-7811Un or other RTL8188 based cards](http://jenssegers.be/blog/43/Realtek-RTL8188-based-access-point-on-Raspberry-Pi)) 
or a custom driver. If you change anything related to `hostapd` during getting this to work, verify again afterwards
that the automatic startup of `hostapd` is still disabled and if not, disable it again (see above for infos on how
to do that).

### Install netconnectd

It's finally time to install `netconnectd`:

    cd
    git clone https://github.com/foosel/netconnectd
    cd netconnectd
    sudo python setup.py install
    sudo python setup.py install_extras
    sudo update-rc.d netconnectd defaults 98

Modify `/etc/netconnectd.yaml` as necessary:
 
  * Change the passphrase/psk for your access point
  * If necessary change the interface names of your wifi and wired network interfaces
  * If your machine is **not** running NetworkManager, set `wifi > free` to `false`
  * if you **don't** want to reset the wifi interface in case of any detected errors on the driver level, set
    `wifi > kill` to `false`
 
Last, start netconnectd:

    sudo service netconnectd start

Verify that the logfile looks ok-ish:

    less /var/log/netconnectd.log

and that it's indeed running (error handling of the start up script still needs to be improved):

    netconnectcli status

Congratulations, `netconnectd` is now running and should detect when you don't have any connection available, starting the AP mode to change that.

You can control the daemon via `netconnectcli`:

  * `netconnectcli status` displays the current status (which interfaces are connected, is the AP running, etc)
  * `netconnectcli start_ap` manually starts the AP
  * `netconnectcli stop_ap` manually stops the AP
  * `netconnectcli list_wifi` shows the wifi cells currently in range
  * `netconnectcli configure_wifi <ssid> <psk>` configures the wifi connection (`<ssid>` = the wifi's SSID, `<psk>` = the wifi's passphrase)
  * `netconnectcli select_wifi` manually brings up the wifi configuration

You can always get help with `netconnectcli --help` or `netconnectcli <command> --help` for specific commands.
