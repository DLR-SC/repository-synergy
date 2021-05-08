# Cortex

Homepage: <http://cortex.glacicle.org/>

## About

[Cortex](http://cortex.glacicle.org/) is a simple application to keep track
and browse through reddit article lists where one would usually need to open
a web browser and possibly use a mouse to navigate.

Since rss readers can get cluttered and are not the same as the actual reddit
homepage, cortex will allow you to stop refreshing the reddit page all the
time while sticking to the same paradigm as the usual reddit frontpage would.

Configuring cortex to display your personal frontpage and monitor your unread
messages is easy, just create a file called ~/.cortex/config, retrieve your
personal reddit json links (Located in Preferences -> RSS feeds) and put
them in the config. It will look something like this:

    [config]
    frontpage=http://www.reddit.com/.json?feed=my-long-personal-hash&user=my-username
    inbox=http://www.reddit.com/message/unread/.json?feed=my-long-personal-hash&user=my-username

Of course you can also just keep cortex as it is and browse the global reddit
frontpage as usual. See the cortex(1) manpage for more information about the
syntax and keybindings.

## License

Cortex is licensed as free software under the MIT/X11 license.
See LICENSE for the full license text.

## Screenshots

![Screenshot #1](http://cortex.glacicle.org/screen_1.png)
![Screenshot #2](http://cortex.glacicle.org/screen_2.png)
![Screenshot #3](http://cortex.glacicle.org/screen_3.png)
