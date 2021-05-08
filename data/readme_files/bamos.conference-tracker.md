**[Subscribe for Weekly Emails](https://groups.google.com/forum/#!forum/cs-conference-tracker)**

Crafted by [Brandon Amos](http://bamos.github.io).

---

[![Build Status](https://travis-ci.org/bamos/conference-tracker.svg)](https://travis-ci.org/bamos/conference-tracker)

This repository contains my minimal-maintenance conference tracker
and an opinionated list of CS conferences.
I find this slightly easier than keeping the dates on Google Calendar
because I can glance at the entire list, keep track of URLs,
and add reminders when I need to add next year's conference.

![](screenshot.png)

# Project Structure
The Python source in [report.py](report.py) generates a plaintext
report from the [YAML data](./data).
I have a [Cron](https://en.wikipedia.org/wiki/Cron) job send
weekly emails with [email-report.sh](email-report.sh)
and [mutt](http://www.mutt.org/).

# Adding and Updating Data
As conferences pass and the data becomes outdated,
I'm happy to accept pull requests with updated data.
If you want to track yours by adding/removing conferences,
please fork this repo.

# Conference Lists
+ [Wikipedia](https://en.wikipedia.org/wiki/List_of_computer_science_conferences)
+ [RichardLitt/awesome-conferences](https://github.com/RichardLitt/awesome-conferences)
+ [WikiCFP: CS](http://www.wikicfp.com/cfp/call?conference=computer%20science)
