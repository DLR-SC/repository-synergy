TvplexendChannel.bundle 
=======================

This is a **channel plugin** for the [Plex Media Server](https://plex.tv).
It makes [Tvheadend](https://tvheadend.org)'s channel list available as live streams in Plex Media Server.

Instructions
------------

1. Follow the Plex' [instructions](https://support.plex.tv/hc/en-us/articles/201187656-How-do-I-manually-install-a-channel-) on *how to manually install a channel [plugin]*.
2. A new channel (i.e., *Tvheadend*) will be displayed in Plex' Web Interface (e.g., [http://plex.local:32400/web/index.html](http://plex.local:32400/web/index.html)).
3. Configure the Tvheadend channel by clicking the ![settings](http://cdn-img.easyicon.net/png/10734/1073494.png) icon. Note that you *must* specify the URL (e.g., _http://localhost:9981/_) of the Tvheadend Web-Interface!
4. Enjoy live TV!

Troubleshooting
---------------

- If something goes wrong, make sure that Tvheadend's HTTP-API can be reached. You can easily check this by opening, e.g., _http://localhost:9981/api/serverinfo_ in your favorite Web browser. If Tvheadend is configured correctly, it should immediately return a JSON document (e.g, `{"sw_version": "3.9...`).

See Also
--------

You might also want to check out the corresponding **metadata agent plugin**: [TvplexendAgent.bundle](https://github.com/pgaubatz/TvplexendAgent.bundle).
