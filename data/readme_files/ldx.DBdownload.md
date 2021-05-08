### DBdownload

**DBdownload** is a simple [Dropbox](http://www.dropbox.com) client written in
Python. It does one-way synchronization from a directory in your Dropbox
account to a local directory. The local folder will be kept in sync with your
Dropbox folder, so if anything is updated, removed or added on Dropbox, it will
be downloaded and kept updated in your local folder. Local changes will be
overwritten - it's one-way only.

### Why?

I just tried to install and use the official Dropbox client on a low-end VPS,
and the OOM kept killing it because it was such a memory hog.  Frustrated by
not being able no simply sync a folder to my box, I checked out whether I
could hack together a simple client which only did one-way synchronization.
DBdownload is the result.

### Install

- Fetch **DBdownload**, e.g., with

        $ git clone https://github.com/ldx/DBdownload.git

- Install (this will also install all necessary dependencies, if missing):

        $ python setup.py install

### Uninstall

Once installed, **DBdownload** can be removed from the system with:

    $ pip uninstall dbdownload

### Use

Just launch **DBdownload** and specify the source Dropbox directory you would
like to sync to your local computer, and the target folder it should be synced
into. If the local folder does not exist **DBdownload** will create it, if it
is used, it will be cleared first.

    $ dbdownload -s test -t /tmp/test
    1. Go to: https://www.dropbox.com/oauth2/authorize?response_type=code&client_id=6m8gx7bmf2yawbm
    2. Click "Allow" (you might have to log in first).
    3. Copy the authorization code.
    Enter the authorization code here:

If this is the first time **DBdownload** is started, it will request access to
your Dropbox data. Just open the link in your browser:

![Dropbox authentication](http://nilvec.com/static/images/db_oauth.png)

and allow access to your Dropbox:

![Dropbox authentication](http://nilvec.com/static/images/db_oauth_success.png)

Get back to the console, paste the authorization code you were given, and if you
have allowed access, **DBdownload** should start synchronizing your Dropbox source 
folder to the target directory.

**DBdownload** has quite some flags and optional parameters, check them out:

    $ dbdownload --help
