building/hacking/...
--------------------

Checkout this repo in Android studio, wait for gradle sync to finish
(you might need to install missing android-21 target) and click "build" :)

Just click "Run" and choose a running device (requires "USB debugging" enabled)..  

Alternatively, you can use "Build/Build APK" to build an unsigned APK so you can copy and 
install this APK on your phone (requires allowed "Unknown sources").

basic usage
-----------

Start the application, click "start" and telnet to the IP address of your android device on the specified port (default 5554) and you can mock locations exactly the same as with the android emulator:

<pre>
$ <b>telnet my_phone_ip 5554</b>
Trying my_phone_ip...
Connected to my_phone_ip.
Escape character is '^]'.
MockGeoFix: type 'help' for a list of commands
OK
<b>geo fix 50 50</b>
OK
<b>geo nmea $GPRMC,081836,A,3751.65,S,14507.36,E,000.0,60.0,130998,011.3,E*51</b>
OK
</pre>


helper scripts
-------------------

### run_sim.py

`helper_scripts/run_sim.py` loads a GPX file and replays it sending "geo fix" commands. 
This script also supports optional live visualization of the simulated route in a web browser.

**examples**

1. run MockGeoFix on your phone and click "start"
2. run `./run_sim.py -i <your_phone_ip> -g your_gpx_file.gpx` on your computer

with web visualization ...

1. run MockGeoFix on your phone
2. run `./run_sim.py -i <your_phone_ip> -g your_gpx_file.gpx -I 127.0.0.1 -P 8080 -s 20`
  - NOTE: -s 20 will simulate 20km/h speed
3. open http://127.0.0.1:8080 in your web browser

`helper_scripts/run_sim.py --help` for more info

NOTE: You can use http://www.gpsvisualizer.com/convert_input to convert directions from google
maps to GPX (just copy the URL from google maps to the 'Or provide the URL of a file on the Web: '
field in gpsvisualizer converter). Alternatively, simply export GPX from http://map.project-osrm.org/ .

### run_json_proxy.py
`helper_scripts/run_json_proxy.py` provides a simple js application with a map you can use to set the mock location. run `helper_scripts/run_json_proxy.py --help` for more info

extra tricks
-------------

### where to get APKs

If you can't/don't want to install MockGeoFix from Google Play, you can download APKs directly from the [Releases](https://github.com/luv/mockgeofix/releases) page.

### forwarding geo commands sent to the emulator to a real device

`tcpflow -B -C -i lo dst port 5554 | socat - TCP4:my_phone_ip:5554`

### running MockGeoFix in the emulator

It's possible to run mockgeofix in the emulator as well (this seems a bit "wtf" but it can be useful when the "geo fix" functionality in the emulator just does not work):

`adb -e forward tcp:5556 tcp:5554`

and then simply

`telnet 127.0.0.1 5556`

this can then be combined with tcpflow and socat to forward "geo commands"

`tcpflow -B -C -i lo dst port 5554 | socat - TCP4:127.0.0.1:5556`

step-by-step guides
-------------------
* [Running MockGeoFix on Android <=5.1](https://github.com/luv/mockgeofix/blob/master/docs/android5_howto/README.md)
* [Running MockGeoFix on Android >=6.0](https://github.com/luv/mockgeofix/blob/master/docs/android6_howto/README.md)


