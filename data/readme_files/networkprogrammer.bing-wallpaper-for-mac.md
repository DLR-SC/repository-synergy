# bing-wallpaper-for-mac
Bing wallpaper for mac

This program is written in python specifically for OSX and tested on Yosemite 10.10.2 running python 2.7.9 and 3.4.3

###Notes

-  The app calls the python scripts on execution.
-  In order to save space, the script assumes that *only 1 image* is kept in the ~/Pictures/bing-wallpaper folder.
-  Place all the files into a single folder. Here it is in the Applications folder within the user's home directory - `~/Applications/Bing Wallpaper`
-  Open the plist file with your favorite editor and change the username to your username

![Image](http://i.imgur.com/Zr9qkQs.jpg)

###The App
- The application is split in the following ways:
	- The checker app checks to ensure there is internet connectivity, then checks to see if an image file already exists in the ~/Pictures/bing-wallpaper folder.
		- If there are files, it will check to see if the file was created today.
			- If the file was created today, stop and don't do anything
			- Else, run the app to download the wallpaper.
		- If there are no files, run the app to download the wallpaper
	- The wallpaper downloader app ensures that you only have the latest wallpaper in your folder. It makes sure to delete all files from that folder before downloading the new wallpaper.

###Plist File
- Copy the plist file to `~/Library/LaunchAgents`
```
cp bing.wallpaper.mac.plist ~/Library/LaunchAgents
```
- Edit the plist file to reflect your username
- Save and close
- Run the following terminal command
```
launchctl load ~/Library/LaunchAgents/bing.wallpaper.mac.plist
```

###Uninstall
- To uninstall run this command
```
launchctl unload ~/Library/LaunchAgents/bing.wallpaper.mac.plist
```
- Delete the `~/Applications/Bing Wallpaper` folder and its contents
- Delete the `~/Pictures/bing-wallpaper` folder and its contents

###Thanks
Feel free to share your comments and thoughts. I am new to github.
