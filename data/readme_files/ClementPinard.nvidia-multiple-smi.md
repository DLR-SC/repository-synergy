# Multiple smi

### Look up GPU/CPU/RAM usage on multiple machines at the same time !
intended to work with python 3+

Based on [pyNVML](https://pypi.python.org/pypi/nvidia-ml-py3), and `psutil`.

### Features
- Allows you to get `nvidia-smi` output and `pustil`information for multiple connected computers at once, and display it on a a selected GUI.
  - Availables frontends :
      - Ubuntu Appindicator
          - works best on Unity, partially supported on Gnome-shell
      - [Argos](https://github.com/p-e-w/argos)
          - works on Gnome shell, but also on MacOS thanks to [BitBar](https://getbitbar.com/) compatibility


![status](https://github.com/ClementPinard/nvidia-multiple-smi/blob/master/images/status%20bar.png)

- Allows you to get a notification every time a new process is launched or finished. A default minimum of 1GB memory use is needed for the notification to appear.
  - Available notification backends :
      - [gnome libnotify](https://developer.gnome.org/libnotify/)
      - [ntfy](https://ntfy.readthedocs.io/en/latest/)

![notif](https://github.com/ClementPinard/nvidia-multiple-smi/blob/master/images/Sans%20titre.png)

- This tool is aimed at small research teams, with multiple GPU-equipped computers, which you can manually ssh to. At a glance you can see every usage of your computer stock, and where you can launch your computation. It also provides some basis if you want to develop a tool to automatically launch your computation on the least busy computer of your network.


### installation:

```[sudo] python3 setup.py install```
```[sudo] pip3 install multiple-smi```

Needed libraries, you need to install them with your package manager (e.g. `apt` for ubuntu or `brew` for MacOS) :
 * `nmap`
 * `libcairo2-dev` (if you need to install `pycairo manually`)
 * `pyzmq`

If using `appindicator` frontend or `gnome` notifier, it is advised to install it with system python, with which the `gi` package can be imported.

For `server_smi` it is also advised to install it with system python because then it will be available in `sudo` mode, needed to install the systemctl service.

#### Optional note for Ubuntu 18+ users

If you want to use the appindicator fronted, as unity is replaced by Gnome-shell, you need to enable appindicators on gnome-shell with `gnome-tweak-tool`, and you need to install python bindings for Appindicator3 :

```bash
sudo apt install gir1.2-appindicator3-0.1
```

#### Server side services installation

To allow clients to access your computer's smi stats, simply run
`server_smi`

But you can also enable it as a service that will be launched at boot.

---------------------------

- **Ubuntu 16+** :  A script is provided to automatically create the service file, whih will allow the server_smi to run automatically during boot (some options are available)
```
sudo install_server_service
```
to uninstall: 
```
sudo install_server_service -u
```
(make the `systemd` folder specified is the same as during installation)

- **Ubuntu 14** : you have to daemonize the script and put it in init.d, you can do it with the provided script `server_smi_daemon.sh`
```
sudo cp server_smi_daemon.sh /etc/init.d/.
sudo chmod 0755 /etc/init.d/server_smi_daemon.sh
sudo update-rc.d server_smi_daemon.sh defaults
```
to uninstall:
```
sudo update-rc.d -f service_smi_daemon.sh remove
```

### to run the appindicator

`client_smi --frontend {argos,appindicator} --notify-backend {gnome,ntfy}`

### to run the client_smi as only a CLI tool with no gui or notificaion:

`client_smi`


### Configuration:

To know which servers have a running `server_smi` in your local network, you can use the `discover_hosts` script, it will automatically populate a json file in `~/.client_smi/hosts_to_smi.json` with found machines.

```
discover_hosts
```

To add your own hosts manually, simply run a `client_smi` or `discover_hosts` once and add your entries in the json file that should be created here:
`~/.client_smi/hosts_to_smi.json`

### Tunnel Connexion

Thanks to `pyzmq` backend for netork, a tunnel connexion is available, when you are outside your usual local network and have to go through a bastion.

Simply launch `client_smi` with `--tunnel` option set to your bastion address

```
client_smi --tunnel user@bastion_ip
```

### Gpu usage stats:

Server-side, gpu usage history is stored in `~/.server_smi/{date}.csv` if launched from CLI, `/etc/server_smi/{date}.csv` if launched from systemctl/init.d.  Usage is written on it every ~60 sec, feel free to make some data science with it.

To enable it, you can use option `-s` in `install_server_service` or add it in `server_smi_daemon.sh` (line 6) before installing