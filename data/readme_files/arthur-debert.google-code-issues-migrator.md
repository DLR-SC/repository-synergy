This is a simple script to migrate issues from Google Code to Github.

For a full history of changes, please
consult the [change log](https://github.com/arthur-debert/google-code-issues-migrator/blob/master/CHANGES.md).

## THIS SCRIPT WILL SEND A LOT OF EMAILS TO ALL WATCHERS

Github's API does not support creating issues or adding comments without
notifying everyone watching the repository. As a result, running this script
targetting an existing repository with watchers who do not want to recieve a
very large number of emails is probably not a good idea.

I do not know of any way around this other than deleting and recreating the
repository immediately before running the import.

### How it works ###

The script iterates over the issues and comments in a Google Code repository,
creating matching issues and comments in Github. This has some limitations:

 - All migrated issues and comments are authored by the user running the
   script, and lose their original creation date. We try to mitigate this by
   adding a non-obtrusive header to each issue and comment stating the original
   author and creation date.

 - Github doesn't support attachments for issues, so any attachments are simply
   listed as links to the attachment on Google Code.

 - Support for Merged-into links for duplicate issues are not implemented.

Otherwise almost everything is preserved, including labels, issue state
(open/closed), and issue status (invalid, wontfix, duplicate).

The script can be run repeatedly to migrate new issues and comments, without
mucking up what's already on Github.

### Required Python libraries ###

Run `pip install -r requirements.txt` to install all required libraries.

If you have problems, try `sudo pip install -r requirements.txt --upgrade`.

### Usage ###

    migrateissues.py [options] <google project name> <github username> <github project>

      google_project_name       The project name (from the URL) from google code
      github_user_name          The Github username
      github_project            The Github project name, e.g. username/project
                                For Organizations, use orgname/project

    Options:
      -h, --help                Show this help message and exit
      -a, --assign-owner        Assign owned issues to the Github user
      -d, --dry-run             Don't modify anything on Github
      -p, --omit-priority       Don't migrate priority labels
      -s, --synchronize-ids     Ensure that migrated issues keep the same ID
      -c, --google-code-cookie  Supply cookies to use for scraping Google Code
      --skip-closed             Skip all closed bugs
      --start-at                Start at the given Google Code issue number
      --migrate-stars           Migrate binned star counts as labels
      -v, --verbose             Print more detailed information during migration

    You will be prompted for your github password.

`--assign-owner` automatically assigns any issues that currently have an owner
to your Github user (the one running the script), even if you weren't the
original owner. This is used to save a little time in cases where you do in
fact own most issues.

`--dry-run` does as much as possible without actually adding anything to
Github. It's useful as a test, to turn up any errors or unexpected behaviors
before you run the script, irreversibly, on your real repository.

`--omit-priorities` skips migration of Google Code Priority labels, since many
projects don't actually use them, and would just remove them from Github
anyway.

`--synchronize-ids` attempts to ensure that every Github issue gets the same ID
as its original Google Code issue. Normally this happens anyway, but in some
cases Google Code skips issue numbers; this option fills the gaps with dummy
issues to ensure that the next real issue keeps the same numbering. This only
works, of course, if the migration starts with a fresh Github repistory.

`--google-code-cookie` takes a HTTP header encoded cookie to use when fetching
pages from Google Code. Google Code normally mangles names for spam prevention,
and getting the raw names requires being logged in and having filled out a
CAPTCHA.

`--skip-closed` will skip migrating issues that were closed.

`--start-at` will skip migrating issues with Google Code issue numbers less than
the provided value.

`--migrate-stars` will migrate the 'Stars' count on each Google Code issue to
Github labels. The following mapping is used:
* `Stars == 1`: Label '1 star'
* `Stars <= 5`: Label '2-5 stars'
* `Stars <= 10`: Label '6-10 stars'
* `Stars <= 20`: Label '11-20 stars'
* `Stars >= 21`: Label '21+ stars'
