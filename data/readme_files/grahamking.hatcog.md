
*Upgrading from 0.9 to 0.10*: The config file format has changed slightly. Please take a look at .hatcogrc in this repo, and adapt your local. Thanks!

----

**Hatcog is the perfect IRC client if you live on the command line, and are addicted to tmux**. It allows you to connect to different channels from different tmux windows, using the same IRC connection. It offers (probably) most things you'd expect your IRC client to have, such as colors, nick notification, private messages, etc.

Hatcog targets 32-bit and 64-bit Linux. I don't know if it will work anywhere else.

## Screenshots

Single channel in Gnome Terminal: [View basic hatcog screenshot](https://github.com/grahamking/hatcog/raw/master/screenshots/hatcog-single.png)

Three channels in two Gnome Terminals, one with `screen` split: [View hatcog with screen screenshot](https://github.com/grahamking/hatcog/raw/master/screenshots/hatcog-screen.png)

Three channels in `tmux` panes - now we're talking! [View hatcog with tmux screenshot](https://github.com/grahamking/hatcog/raw/master/screenshots/hatcog-tmux.png)

## Install

**1. Clone and install:**

    git clone https://github.com/grahamking/hatcog.git
    cd hatcog
    sudo python3 setup.py install   # Yes, python3!

**2. Copy example config and edit it:**

    cd ~
    cp hatcog/.hatcogrc .   # Now edit it

## Run

Run `hjoin <network.channel>` e.g. hjoin freenode.test. There is no hash in front of the channel name. If your channel starts with two hashes, use one and backslash escape it.

To start a private conversation: `hjoin -private=<network.nick>` e.g. hjoin -private=freenode.bob.

Log files are in `~/.hatcog/`.

The first time (after reboot) you run `hjoin`, it starts the `hatcogd` daemon. When you `/quit` hjoin, the daemon stays running. If you want to kill the daemon, use `hjoin --stop`.

## Details

hatcog is a text-based IRC client which plays well with [tmux](http://www.google.ca/search?q=tmux), or any other window manager. It lets you manage your chat windows. The client is in Python3 / curses, the server in Go.

hatcog is made up of two programs: `hatcogd`, which connects to your irc server, and `hjoin`, which manages input/output for a single channel. `hatcogd` is started for you in the background, so usually you only interact with the curses client, `hjoin`.

The `hjoin` curses interface will display the following information, if available:

 - Top: Server name, time of last ping from server
 - Bottom: Your nick, channel name, channel url, number of active users in channel (spoke in last 10 minutes), number of users in channel.

## Alerts

When someone says your name in a channel or sends you a private message, we notify you. You'll need to customise the command in .hatcogrc.

A common way to display a notification in Ubuntu is using `notify-send`. I prefer to send myself an IM message, that way Pidgin handles displaying it on my desktop and making a sound. It works even if I am using hatcog on a remote machine over ssh. I use `sendxmpp` wrapped in a small bash script.

## Supported commands

See hjoin/hfilter.py for a list. Anything you prefix with / is sent direct to the server. DCC is not supported.

**Standard commands**

 - /me : Display something differently. Try it: `/me eats lunch`.
 - /names : List users in channel.
 - /nick <new_nick> : Change your nickname.
 - /quit : Quit the client. You will part the channel. Server stays running (to stop server `hjoin --stop`).

**Extra commands**

Non-standard IRC commands:

 - /url : Open the most recent url (urls get underlined when displayed) in a browser. Command to open the browser is in .hatcogrc.
 - /notify : Alert me on all messages. Uses the same method of alerting you when someone says your nick, to alert you of every message. Useful for quiet channels, to notice when something happens. Do /notify again to switch it off.
 - /pw : Send your password to identify with NickServ. The client does this for you on startup (password is in .hatcogrc), so you should never need this.
 - /connect : Hatcog subverts the CONNECT command, so it's probably not the best client for a network operator.

## But I don't have Linux (or not an AMD / Intel processor)

The python client part (hjoin) will run anywhere you have Python 2.7+.

The server part (written in Go), `hatcogd` has binaries included for i686 32-bit Linux (`bin/hatcogd-32`) and x86\_64 64-bit Linux (`bin/hatcogd-64`). Anything else you'll need to compile it yourself.

Get [Go](http://golang.org) v1+. Make sure the hatcogd checkout is on your GOPATH, then type `go build hatcogd`. That will put a `hatcogd` executable in your current directory.

Copy or symlink it from `/usr/local/bin`. Finally you'll need to modify hjoin/hjoin.py so it can find your binary.

## But I only have Python 2

Most likely you already have python3, and if not it's easy to install it and run both versions of python side by side. That's what I do. They don't conflict.

## Development

For development I use a local install of [ircd-hybrid](https://help.ubuntu.com/community/IrcServer), and the 'test' channel on freenode.

Happy IRC-ing!

