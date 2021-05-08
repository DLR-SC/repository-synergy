Sublime Text 3 slack.com integration plugin
=========================

A Sublime Text 3 plugin which integrates http://slack.com services.  

### This plugin is no longer maintained (mainly because I switched to PyCharm). If someone wants to continue work on this, i will give access rights.

### Installation
Search for "Slack" package in Sublime Package Control

### Configuration
Open "Settings - User" from Preferences -> Package Settings -> Slack

    {
        "team_tokens": {
            "Team 1": "team-1-token-goes-here",
            "Team 2": "team-2-token-goes-here",
        },
        "username": "Sublime",
        "username_subtext": "via Sublime",
        "show_plaform_and_name": true,
        "repeat_file_ext": false,
        "avatar_url": "http://simionbaws.ro/icons/sublime-48.png"
    }

* ##### `"team_tokens"` (required)
    * A list of tokens you have, keyed by the team name that the token corresponds to.
    * You can get the token(s) from https://api.slack.com/web#auth (make sure you are authenticated on slack.com with your account)

* ##### `"username"` (required)
    * **defaults to "Sublime"**
    * The "sender" username that will be attributed to each message

* ##### `"username_subtext"`(optional)
    * The parenthetical subtext to show next to your username. Defaults to "via Sublime".
    * \*Note that if set, this setting will override the `"show_platform_and_name"` setting
    * \*Slack enforces that external plugins have parenthetical subtext next to the sender's username for each message.
  So if this option is omitted AND the `"show_platform_and_name"` setting is `false`, Slack adds the default subtext "bot", e.g., "myUser (bot)"

* ##### `"show_platform_and_name"` (optional)
    * **defaults to `true`**
    * if this is `true` and no setting is given for `username_subtext`, will use your name and your platform as the subtext to the username, e.g. "myUser (simion, linux)"

* ##### `"repeat_file_ext"` (optional)
    * **defaults to `false`**
    * If this is `true`, the name of the file being uploaded with have the extension repeated., e.g. `script.py` is uploaded as `script.py.py`.
    * \*This is meant to account for the fact that Slack, by default, chops off the file extension when displaying the filename. So uploading
  a file called `script.py` shows up in most places in Slack as just having the filename `script`.
With this option set to true, it would show up as `script.py` in Slack, at the expense of having the actual uploaded filename as `script.py.py`
    * \*See [Screenshots](#user-content-screenshots-file-uploads) below for examples

* ##### `"avatar_url"` (required)
    * url to the avatar image to use
    * **defaults to** [http://simionbaws.ro/icons/sublime-48.png](http://simionbaws.ro/icons/sublime-48.png)
    * ![alt text](http://simionbaws.ro/icons/sublime-48.png)


### Features
* Send messages to
    * users
    * channels
    * private groups
* Can send message:
    * from selected code
    * from user input
* @user, #channel or .group supported (at beggining of message)
* Autofill last @user, #channel or .group used
* Multiple teams(tokens) support
* Upload files
    * current open file
    * contextual (right click) in sidebar
    * enter file path manually


###Changelog
* __1.4.6__: Fixed empty filename on uploads. Made it so that messages sent to users via `@user` are sent via IM (private message) rather than to that user's slackbot channel.
Added `"repeat_file_ext"` and `"username_subtext"` options
* __1.4.5__: Code preformatting
* __1.4.3__: http://simionbaws.ro/plugins/sublime-slack-1-4-3/
* __1.4.0__: http://simionbaws.ro/plugins/sublime-slack-1-4-0/
* __1.3.3__: http://simionbaws.ro/plugins/sublime-slack-1-3-3/
* __1.3.2__: http://simionbaws.ro/plugins/sublime-slack-1-3-2/
* __1.3.1__: http://simionbaws.ro/plugins/sublime-slack-1-3/


### Usage
* Select a text and Right click (or ctrl+shift+p) -> Slack: Send selection
* Sending a custom message:
 - press Ctrl+Alt+n (or control + command + n)
 - enter the message
 - choose a channel/group/user from the dropdown
If the message begins with @username #channel or .group the message is sent directly to the specified receiver.
When using new message input box, it will have the last receiver name autocompletet automatically
* Send a file: right click, or using quick panel

### Shortcuts
* ctrl+alt+u -> Send Selection (osx: control + option + u)
* ctrl+alt+n -> Send Custom Message (osx: control + option + n)
* ctrl+alt+j -> Send Current File (osx: control + option + k)


### Feedback
If you have any suggestions, please leave a reply here:
http://simionbaws.ro/sublime-text-3-slack-integration-plugin/

### Bug report / feature request
Please use github issues system: https://github.com/simion/sublime-slack-integration/issues

### Development
This plugin is constantly being upgraded as the slack.com API team releases new features or fixes existing bugs.
If you want to contribute, feel free to fork and make a pull request. The code must pe PEP8 compliant to be accepted (or at least close to that)

### Support
I like beer.
So if you'd like to support the continuous development of this plugin, you could buy me a beer: https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=NNPZNQULPETD4



#### Screenshots <a id="screenshots"></a>
* Grab message from user input
    * ![](http://i.imgur.com/lyv6Yd6.png "Grab message from user input")


* Receiver selection
    * ![](http://i.imgur.com/fu941bH.png "Receiver selection")


* Direct message sending, skips channel/user/group selection
    * ![](http://i.imgur.com/SXnHYZo.png "Direct message sending, skips channel/user/group selection")


* Send message directly to user
    * ![](http://i.imgur.com/SXnHYZo.png "Send message directly to user")


* Send message to channel
    * ![](http://i.imgur.com/qaXE9EN.png "Send message directly to channel")


* Example of received message
    * ![](http://i.imgur.com/7n14c5H.png "Example of received message")


* Example of uploaded file - *WITHOUT* `"repeat_file_ext"` setting <a id="screenshots-file-uploads"></a>
    * ![](http://i.imgur.com/hxsNw1t.png "Without 'repeat_file_ext' setting")


* Example of uploaded file - *WITH* `"repeat_file_ext"` setting (notice the `.py`)
    * ![](http://i.imgur.com/eZRO97k.png "With 'repeat_file_ext' setting")


* Sidebar right-click
    * ![](http://i.imgur.com/Gf6UvSn.png "Sidebar right-click")


* Quick menu
    * ![](http://i.imgur.com/GTfi88U.png "Quick menu")
