PlexTools.bundle
================

A Plex plugin that provides the following:
* Downloads subtitles for any videos in your library from http://www.opensubtitles.org/ and modifies them so that work correctly with the Roku client
* Converts any video in your Plex library to MP4 which can be Direct Played on most/all Plex clients

Installation Instructions
-------------------------
1.  Install FFMPEG and FFPROBE from http://www.ffmpeg.org/
2.  Copy PlexTools.bundle to your plugin directory
    * Mac: ~/Library/Application Support/Plex Media Server/Plug-ins
    * Windows: C:\Users\\[user]\AppData\Local\Plex Media Server\Plug-ins
    * Linux: /var/lib/plexmediaserver/Library/Application Support/Plex Media Server/Plug-ins
3.  Make sure to update the plugins settings
    * `OpenSubtitles Username`: OpenSubtitles account name (required)
    * `OpenSubtitles Password`: Password for OpenSubtitles account (required)
    * `OpenSubtitle Language`: Language preference for subtitles (defaults to English)
    * `FFMPEG_PATH`: Path to FFMPEG (including binary) (required)
    * `FFPROBE_PATH`: Path to FFProbe (including binary) (required)
    * `Audio Bitrate`: The audio bitrate for the converted video (in kbs)
    * `Video Bitrate`: The video bitrate for the converted video (in kbs)
    * `Audio Codec`: The audio codec used for the converted video
    * `Delete Original File`: Delete original video (defaults to false)
    * `Enable Folder Renaming`: Enables file renaming
    * `Add additional 2ch audio stream`: Adds an additional 2ch AAC streaam to converted video
    * `Max Audio Channels`: Sets the number of channels for the main audio stream
    * `Embed Subtitles`: Embeds subtitles into video stream (subtitle must already be downloaded)
    * `Download subtitles in the background`: Enables the Auto Download feature
    * `Frequency to check for new subtitles`: The frequency in hours to check for new subtitles

Credits
-------------------------
* https://github.com/mdhiggins/sickbeard_mp4_automator
* https://github.com/agonzalezro/python-opensubtitles
