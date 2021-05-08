# LINE-ChatBot
LINE Messaging Chat Bot.
# Requirements & Dependencies
Libraries Needed: <br>
- Python 2.7.x <br>
- pip install line <br>
- pip install pafy <br>
- pip install goslate <br>

# Screenshot
![IMAGE ALT TEXT HERE](https://cloud.githubusercontent.com/assets/12862541/8268114/279263a2-17ab-11e5-9d08-6ec75ddfe23f.png)

# Features

- !botreply <pesan> -> Auto Reply Feature. <br>
- !botbioskop -> Giving you an information about now playing cinemas/films.<br>
- !botkatamutiara -> Giving you a beautiful words.<br>
- !bottranslate <pesan> ( ID - EN / EN - ID) -> Translating from Indonesia to English, English to Indonesia.<br>
- !botmeme -> Giving you a funny meme image from 1cak site.<br>
- !botyoutubemp3 <url youtube> -> Giving you a link which has converted from Youtube's video to mp3.<br>
- !botyoutubedl <url youtube> -> Giving you a link to download *.mp4 file video with the best quality.<br>

# Command Examples
See the <b>command_examples.txt</b> file

# Tips
- If you need to run your bot everytime , run the bot via cronjob/crontab in your server. <br>
- To Maximize the bot reply response, i suggest you to use this settings in your cron.

```
* * * * * sleep 15; python /home/user/public_html/linebot.py --mode your_mode --target your_target --execute
* * * * * sleep 30; python /home/user/public_html/linebot.py --mode your_mode --target your_target --execute
* * * * * sleep 45; python /home/user/public_html/linebot.py --mode your_mode --target your_target --execute
```

# FAQ ( Frequently Asked Questions ) 
<b>Q</b>: How can i get the authentication token ( authtoken ) ? <br>
<b>A</b>: Just Google or check the source code of LINE's python library.
   Please, try to find it by yourself dude! <br>

<b>Q</b>: Whoa, i got the authentication token! So, where i can put this ? <br>
<b>A</b>: Check "settings.py" inside "src" directory. Put it into AUTH_TOKEN variable. <br>

<b>Q</b>: I got an error , how do i fix it ? <br>
<b>A</b>: 
    If you are not familiar with Python just wait for the official update source code by the author ( budanthara's github ).
    If you are a core pythonic programmer, try to fix it by yourself.

<b>Q</b>: I tried to chat with "!botreply" mode, but i didn't get any responses. <br>
<b>A</b>: The first thing you should know. The bot will replying the messages when your LINE Account already added the others contact in the same group/room. <br>

<b>Q</b>: How do i can add the others contact when the members of the group have so many members ? <br>
<b>A</b>: Mass add group members under development, so try to add it manually for a while. Sorry btw :p <br>


