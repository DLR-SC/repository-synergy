# Videotop

## Description
A free console browser for online videos, written in python with vim-like keybindings.

## Usage
If you are already familiar with vim the controls should be pretty intuitive.  
There are two modes: command mode and browse mode.

In command mode you can search for videos by typing **:s** *VIDEOSEARCH* and hitting **ENTER**.  
This will generate a list of videos and switch to browse mode.

In browse mode you can download the videos by hitting **ENTER** and play them with **p**.
To abort the download of a video select it and hit **a**. Note that this won't delete the partially downloaded file,
in fact you can resume the download if you hit **ENTER** again.  
You can also open the YouTube page by hitting **o** or directly stream the video with MPlayer by hitting **s**.  
**CTRL n** lists the next videos of your previous search and **CTRL r** clears the screen.

To search for the string *SOMETHING* in the current video list type **/***SOMETHING* and
hit **n** to get to the next or **N** to get to the previous item.  
With the command **:videos** or just **:v** all downloaded videos will be listed. A pattern can also be specified, so
**:v monty** will list all videos containing the substring *monty*.
Since local searches are case-insensitive, the commands **:v monty** and **:v Monty** (or **/monty** and **/MONTY**) are
equivalent.  
Downloaded videos can be deleted with the command **:delete**. (*WARNING*: no undo)

All downloaded videos are stored in *~/.videotop/videos*.

## Configuration
For streaming you might want to add something like this in your MPlayer config (~/.mplayer/config), 
the values depend on your internet connection:

    [default]
    cache = 8192 # 8 mb cache
    cache-min = 5 # play if 5% of the cache is loaded in memory

## Command Table
<table border='1'>
<tr><th>Command Mode</th><th>Browse Mode</th><th>Description</th></tr>
<tr><td>:search, :s</td><td></td><td>Search for videos</td></tr>
<tr><td>:videos, :v</td><td></td><td>Show all downloaded videos</td></tr>
<tr><td>:13</td><td></td><td>Select video 13</td></tr>
<tr><td>:delete</td><td></td><td>Remove the selected video</td></tr>
<tr><td>:clear</td><td>CTRL r</td><td>Clear the video list</td></tr>
<tr><td></td><td>CTRL n</td><td>List the next videos of the previous search</td></tr>
<tr><td></td><td>ENTER</td><td>Download the selected video</td></tr>
<tr><td></td><td>a</td><td>Abort downloading the selected video</td></tr>
<tr><td></td><td>o</td><td>Open the YouTube page of the selected video in your default web browser</td></tr>
<tr><td></td><td>p</td><td>Play the selected video with MPlayer</td></tr>
<tr><td></td><td>s</td><td>Stream the selected video with MPlayer</td></tr>
<tr><td></td><td>j</td><td>Move down</td></tr>
<tr><td></td><td>k</td><td>Move up</td></tr>
<tr><td></td><td>CTRL d</td><td>Move down</td></tr>
<tr><td></td><td>CTRL u</td><td>Move up</td></tr>
<tr><td></td><td>g</td><td>Move to the first video</td></tr>
<tr><td></td><td>G</td><td>Move to the last video</td></tr>
</table>

## Dependencies
* [urwid][1] to provide an ncurses frontend.
* [gdata][2] and [youtube-dl][3] to search for and download youtube videos.
* (optional) [mplayer][4] to play the downloaded videos.

[1]: http://excess.org/urwid/
[2]: http://code.google.com/apis/youtube/1.0/developers_guide_python.html
[3]: http://rg3.github.com/youtube-dl/
[4]: http://www.mplayerhq.hu/

## Links
* [archlinux forums][5]

[5]: https://bbs.archlinux.org/viewtopic.php?id=123234/
