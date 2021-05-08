#Drench

Drench is a lightweight BitTorrent client written in Python. There are a couple of nice features, like the ability to download a subset of all the files in the torrent and exiting cleanly once the download is complete. 

The client works with [vis](https://github.com/jefflovejapan/vis), a Twisted web server and D3.js visualization, to show what's going on in the user's file system while the download is taking place.


##Install

The preferred way to install Drench is with [`pip`](http://www.pip-installer.org/en/latest/installing.html), which will let you run the following command from the terminal:

`pip install drench`

Alternatively, you can clone the source and run the following:

`python setup.py install`


##Use

From the command line enter the following:

`python -m drench ./mytorrent.torrent --port 8000 --visualizer 127.0.0.1:8002 --directory ~/Downloads/`

`./mytorrent.torrent`: The path to your torrent file (required)

`--port 8000`: The port to use for BitTorrent traffic (optional)

`--directory ~/Downloads`: Where to save your download (optional)

`--visualizer 127.0.0.1:8002`: The address of your [vis](https://github.com/jefflovejapan/vis) server (optional)

Drench isn't capable of downloading multiple torrents at once; just start up a second instance in another terminal instead.


##Status

You can use Drench to download torrent files from the small handful of sites I've tested on. 

What doesn't work:
- Seeding
- Magnet links
- UDP-based handshake with tracker (which knocks out several of the biggest trackers)



