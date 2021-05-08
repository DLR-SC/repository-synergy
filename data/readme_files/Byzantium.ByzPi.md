ByzPi
=====

This repository is for the RaspberryPi port of Byzantium Linux, the first
milestone of the ISC development grant.

Byzantium:

::Byzantium provides true mesh networking, through the use of OLSRd, and avahi.  It uses many of the same configs from Commotion Wireless, providing seemless integration.

::The Byzantium repo is legacy, the project is in the process of being migrated to the buildtree, and it's linked repos.

Setup:

::The auto config script requires no user interaction, it's copied from autoconfigd-0.2.py, to /usr/bin/byzantium-autoconfigd.0.2.py.

::After running the config, you should see your wireless interface in "ad-hoc" mode, connected to the "Byzantium" network.  

::If you ran the curl command from the wiki, you don't need to run the script, just reboot, and you should be connected.


Please see the ByzPi Wiki for more information https://github.com/Byzantium/ByzPi/wiki/_pages
