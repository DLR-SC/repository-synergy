linux-salted
============

I use this to quickly configure a GNU/Linux system with the software I generally use and the configuration I like.

The setup currently understands laptop (desktop) configuration and cloud VMs (Ubuntu 16.x).

main features:
--------------

- XMonad tiling window manager
- NVidia graphics drivers
- Steam client
- Dropbox
- Google Cloud SDK
- fish shell, mosh mobile shell, gyazo, synergy

cloud oriented:
---------------

If configured for cloud features, you also get:

- Docker bootstrap
- Salt master to control Windows minions on EC2
- Discourse docker image

extras:
-------

Additional formulas, my own or third parties, which can be used in your own salt setups:

- Steam developer runtime: https://github.com/TTimo/steamrt-formula
- Google Chrome: https://github.com/TTimo/google-chrome-formula

getting started:
----------------

If you can use cloud-init (EC2 and some other providers), you can upload cloud-init/user-data.payload.gz when creating the VM (Advanced Details, User data in the Launch Instance Wizard).

Otherwise run the scripts in order from cloud-init/scripts once you have a shell (as root).

You will need to customize (or skip) 30_flavor, depending what you default username is and if you want to configure the cloud or desktop version.
