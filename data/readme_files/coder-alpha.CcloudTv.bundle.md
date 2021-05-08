CcloudTv.bundle
===================

Plex Media Server plug-in designed for cCloud TV | A Community based Social IPTV Service for Live TV, Movies, TV Shows & Radio

- [Plex Forum Support Thread](http://forums.plex.tv/discussion/166602/)

System Requirements
===================

- **Plex Media Server:**
	- Tested Working:
		- Windows
		- Linux (Ubuntu) - cd to Plex Plugin's dir & use 'sudo chown -R plex:plex CcloudTv.bundle'
- **Plex Clients:**
	- Tested Working:
		- Plex Home Theater
		- Plex/Web
		- Samsung Plex App
		- Android Kit-Kat (Samsung Galaxy S3)
		- iOS (Apple iPhone6)

How To Install
==============

- Download the latest version of the plugin.
- Unzip and rename folder to "CcloudTv.bundle"
- Delete any previous versions of this bundle
- Copy CcloudTv.bundle into the PMS plugins directory under your user account:
	- Windows 7, Vista, or Server 2008: 
		C:\Users\\[Your Username]\AppData\Local\Plex Media Server\Plug-ins
	- Windows XP, Server 2003, or Home Server: 
		C:\Documents and Settings\\[Your Username]\Local Settings\Application Data\Plex Media Server\Plug-ins
	- Mac/Linux: 
        ~/Library/Application Support/Plex Media Server/Plug-ins
- Restart PMS

How To Use
==============

- No configuration required, however, one can set a private web url or local file under Preferences (examples included). Refer [Plex forums support thread](http://forums.plex.tv/discussion/166602/).
- EPG data is available as xml files graciously provided by others located [here] (https://github.com/coder-alpha-prog-guide). Refer [Plex forums support thread](http://forums.plex.tv/discussion/166602/) on how to set them under options.

Known Issues
==============

- Some channels will not play, if so check in web-browser before reporting with an issue.
- To Fix 'Cannot load M3U8: crossdomain access denied' on PlexWeb - disabling direct play gets around this issue, but it may have issues playing other streams that previously worked fine.
- Other useful information is listed on the [Plex Forum Support Thread](http://forums.plex.tv/discussion/166602/)

Acknowledgements
==============

- Credits to [cCloud TV | Popcorntime for LIVE TV an open source project] (https://github.com/imbane/imbane.github.io)
- Credits to [Cigaras, Valdas Vaitiekaitis] (https://forums.plex.tv/discussion/83083/rel-iptv-bundle-plugin-that-plays-iptv-streams-from-a-m3u-playlist/p1): IPTV (This plugins uses some parts)
- Credits to [SharkOne] (http://forums.plex.tv/discussion/102253/rel-bittorrent-channel/p1): (Some parts of Channel updater)
- Credits to [zombian] (http://forums.plex.tv/profile/zombian) for plugin icons
- Credits to [walktheway] (http://forums.plex.tv/discussion/96270/vlc-channel) (VLC Transcoder based on VLC Plex Channel)
- Credits to [b_caudill21] (http://forums.plex.tv/discussion/193042/rel-expat-tv) (Online guide code based on Expat plugin)
- Credits to [coryo123] (https://forums.plex.tv/discussion/194503) (DumbTools-for-Plex)
- Credits to [Filippo Valsorda] (https://github.com/FiloSottile) (Redirect Follower)
- Credits to [IMDbPY] (http://imdbpy.sourceforge.net/index.html) (IMDb scrapper)
- Credits to [Livestreamer] (http://docs.livestreamer.io/) & [Streamlink] (https://streamlink.github.io/) a fork of the former.
- Thanks to [Twoure] (https://github.com/Twoure), [Shopgirl284] (https://github.com/shopgirl284), [coryo123] (https://forums.plex.tv/discussion/194503) and many others I have had discussions, read their posts and borrowed code.