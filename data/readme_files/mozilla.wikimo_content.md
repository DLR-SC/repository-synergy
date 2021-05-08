# Wikimo Git documentation

This repository stores  documentation for https://wiki.mozilla.org/ and in particular the
https://wiki.mozilla.org/Security pages. It is possible to both pull existing pages, or changes made to pages
directly back to Git as well as commit changes to Git first then push them to the wiki. In any case, the Git repository
 has authority and, for pages tracked here, it is highly recommended to ensure that your changes are sent via a
pull-request.

Please do not change the main repository directly (i.e always fork and send a pull-request, get at least one
peer-review and merge).

All documentation is licensed under the MPL (see LICENSE).

# Notes on infosec.mozilla.org (no longer hosted on wikimo)

Certain pages used to be hosted on wiki.mozilla.org are now hosted on https://infosec.mozilla.org.
The wiki.mozilla.org pages redirect there automatically. Please use https://github.com/mozilla/infosec.mozilla.org if
you wish to improve these pages.

# Drafting new documentation, or changes to documents

Sometimes, it's a little hard to edit documents directly from Git in your own text editor.
When or if that is the case, the currently recommended practice is:

1. Create a draft in your Wikimo space, such as: https://wiki.mozilla.org/User:Gdestuynder/mydraft
  a. Optionally: Create an issue in https://github.com/mozilla/wikimo_content/issues to indicate you're working on this.
     This may be particularly useful if you're going to work on this for a long time to avoid work duplication.
2. Edit, preview, etc. to your heart's content.
3. Copy paste the result to Git and push to your local/personal GitHub fork of this very repository
4. Create a PR (Pull-request) with the new contents and also refer to your Wikimo space for a rendered version.

# Usage of the sync.py tool

This tool synchronizes Git to Mediawiki automatically (both ways!) and should be run after you merged commits to GitHub
for changes to appear on Mediawiki (or to pull changes from Mediawiki into GitHub!).

**Recommended:** Install/use virtual envs for Python. See the example below if you've never done that before.

```
# Place these in your $HOME/.bashrc or favorite shell RC file
# then call 'pyvenv2' or 'pyvenv' when entering the directory with the virtual
# python environment.

# Python 2.x - 3.5
function pyvenv2() {
[ -d venv2 ] || virtualenv2 --no-site-packages venv2
source venv2/bin/activate
}
# Python 3.6+
function pyvenv() {
	[ -d venv ] || python3 -m venv venv
	source venv/bin/activate
}
```

## Install & configure sync.py

```
$ git clone https://github.com/mozilla/wikimo_content && cd wikimo_content
# <activate your venv>
$ pip install -r requirements.txt
$ cp sync.json.inc sync.json
# <edit sync.json>
```

## Using sync.py

Checking for differences/changes between your local Git copy and Wikimo. Nothing will be written to Wikimo.

```
$ ./sync.py
# This also shows the unified diff for the pages
$ ./sync.py -d
```


Push changes - this **will** write to Wikimo.

```
$ ./sync.py --push
```

To sync the wiki back to git (for example when someone forgot to use git... ;-).

```
$ ./sync.py --get
# To send back to GitHub as well:
$ git commit -a -m "your commit msg here"
$ git push origin master:myfix
# Create a pull-request after this to get your changes integrated upstream
```
