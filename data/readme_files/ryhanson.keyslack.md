# keyslack
Simple Slack API client used to encrypt/decrypt and send/receive Keybase PGP messages through a Slack private group.

## Overview
This little tool utilizes [Slacker](https://github.com/os/slacker) to interact with the [Slack Web API](https://api.slack.com/) and Websockets to interact with [the Slack Real Time Messaging API](https://api.slack.com/). It also wraps the [Keybase CLI](https://keybase.io/docs/command_line) to encrypt, decrypt, and sign messages and files.

It uses a Slack private group as a means for transferring PGP messages back and forth. You can send encrypted messages or files to the group and automatically download and decrypt and PGP messages sent to you. Utilizing websockets allows this tool to constantly watch the room for any PGP messages meant for you, then download and decrypt them.

## Installation
This tool does require that you have a [Keybase.io](https://keybase.io) account along with the command line tool installed.

### Manual install
```
git clone https://github.com/ryhanson/keyslack.git
pip install -r requirements.txt
```

### Usage
1. First thing you'll need to do is update your Slack profile. Add #keybase:[keybase_username] at the end of any of these fields: title, skype, or phone
  Example title: Software Developer #keybase:ryhanson
2. Next get a Slack API auth token at the bottom of this page: https://api.slack.com/web
3. Either create or choose a private group in Slack to use as the PGP Message delivery platform
4. Now lets run it: `python keyslack.py`

On your first run, you will be prompted to enter the auth token and group name that you setup earlier. Your keybase username will be parsed from your profile after your are authenticated.

**NOTE**: Depending on the GPG tool you are using, you may be prompted to enter your Keybase passphrase on each encryption/decryption.

### Purpose
Allow you and your team to securely transmit files and messages by utilizing Keybase for encryption, signing, and identity proofing. This tool becomes powerful when everyone on a team is using it. By running this tool and issuing the command `encrypt ryhanson -f certs.zip` it would encrypt the zip file, upload it to the private group on slack, and `ryhanson` is running this tool, it would automatically download the the PGP encrypted .zip and then decrypt it. Running `encrypt ryhanson -m "sup3rs3cr3tpassw0rd"` would encrypt and send that password to `ryhanson`.

### Note
This is obviously VERY rough. I mainly wrote it out of my own curiosity and because I wanted to get my feet wet with Python. There are no guarantees for any support for this code. It may be abandoned and left here for historical purposes.

With that said, I do plan to work on this some more. Some things I have on my TODO list are:

1. Refactoring, modularizing, and making it more "Pythonic". Any code review and pointers are welcome! I primarily develop in C#/.NET, so this realm is a little different than what I am used to.
2. Keybase recipient validation: validate that the recipient the user is sending to is in the room, and has the #keybase tag setup in their profile.
3. Bulk message delivery: send a message per keybase user to the private group. This would allow for an entire team to receive the same update password, certificate, SSH key, etc.
4. Steganography: allow for PGP messages to be hidden in images before they are sent. This would make the Slack group much more amusing if it was full of random memes and GIFs, instead of big encrypted text previews.
