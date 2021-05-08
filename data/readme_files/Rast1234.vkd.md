vkd (en)
===
WARNING: it is dead, not supported and does not work. See https://github.com/Rast1234/VOffline instead.
===

VK dumper - save stuff from your vk.com to local drive
---

**Features:**

* Download almost anything from your wall:
    * Posts
    * Multimedia attachments
    * Comments
    * Comment attachments
    * Some extra raw info for your history
* Download audio tracks
    * Correct fime naming
    * Text stored also (if available)
    * Sort by playlists (as subfolders)
* Download docs
    * Auto-change filename if exists
    * Write correct extension
* **TODO:** Downloading video 
* **TODO** Downloading notes

**Known limitations, bugs and other considerations:**

* Unable to download videos (Anyone need this?)
* Unable to download note comments (Maybe an unneeded feature?)
* Tested on a particular user, audio tested on a group
* Can't grant access by itself, so you need to enter auth token manually (see below)
* If wall, documents or audio list has been modified during work, it **will** cause unpredictable things.
* Sometimes you need to solve CAPTCHA (interactively)

Usage and requirements
---
You need **Python 2.7** only for this to work. Should work under different OSes, not tested.  
For all available list of arguments see `--help` output.
Essential options described below:
* `-i / --id`    User ID or group ID to dump. Group ID should be prefixed with `-`, e.x. `-123456`
* `-a / --app_id`	Application ID, see below.
* `-m / --mode` Working mode. Supported modes are `wall`, `docs` and `audio`, you may specify all at the same time. Script will download your wall, docs or audio tracks, respectively.

How-to
---
1. Clone this repo
2. Register your own [vk app here](https://vk.com/editapp?act=create) to get Application ID. Be sure to select **standalone** application type.
3. Write down your Application ID (ex. **1234567**).
4. Find your [profile ID here](https://vk.com/settings) near the bottom of the page. For example, **1**.
5. What do you want to dump? `audio`, `wall` or `docs`?
6. Now specify everything to the script:

        main.py --app_id 1234567 --id 1 --mode wall audio docs

7. Script will ask you to go to a given URL, so, do it :)
8. Give access for this application to your profile.
9. You will be redirected to a white page with text about security.
10. Copy URL of this page. Yeah, I know, VK tells you not to do that for security reasons. But this application is your just registered app, and this script is open-source, so go and read sources if you don't trust me..
11. Paste URL int script, it is waiting for you!
12. Enjoy downloading process. This will take a lot of time, though.

You may set limits of posts and audio tracks to download, change directory to store data, etc. See `--help` output.

Results
---
According to working mode and wall posts' contents, corresponding dirs and files will be created.
Everything will be stored in specified directory, say, `some_dir`:
   
      some_dir                                     (base directory)
      +---- 9876543                                (user id)
            +---- docs                             (documents stored here)
            |     +---- cat.gif
            |     +---- my_archive.zip
            |     +---- ...
            +---- audio                            (audio tracks ant dexts)
            |     +---- Artist1 - Track.mp3
            |     +---- Artist2 - Track.mp3
            |     +---- Artist2 - Track.mp3.txt    (text for that song)
			|     +---- Album1                     (audio album name)
            |     |     +---- Artist - track.mp3   (tracks in that album)
            |     +---- ...
            +---- post_1234                        (wall post id)
            |     +---- text.html                  (post text)
            |     +---- image.jpg                  (any multimedia attachments)
            |     +---- music.mp3                  
            |     +---- ...
            |     +---- media_urls.txt             (list of attachments' urls)
            |     +---- comments.json              (raw comments, reply from vk server)
            |     +---- raw.json                   (raw post, reply from vk server)
            |     +---- note_1234                  (note, if attached to post)
            |     |     +---- text.html            (note text)
            |     |     +---- raw.json             (raw note, reply from vk server)
            |     +---- comments                   (comments dir)
            |           +---- text.html            (all comments' text)
            |           +---- raw.json             (raw comments, reply from vk server)
            |           +---- image.jpg            (any multimedia attachments)
            |           +---- music.mp3                  
            |           +---- ...
            |           +---- media_urls.txt       (list of attachments' urls)
            +---- post_1235
            |     +---- ...
            +---- ...
                        


Bugs
---
Any bug reports, pul requests appreciated. Open an issue [here](https://github.com/Rast1234/vkd/issues) or [PM me](https://vk.com/rast1234)

Credits:
---

Me :)  
http://habrahabr.ru/post/143972/ (call_api function)  
http://stackoverflow.com/questions/22676/how-do-i-download-a-file-over-http-using-python (fancy progressbar)  
Pavel Durov for great social network and its buggy API :)  
    
