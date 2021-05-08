# SubtitleFixer

## Important

This is a simple nautilus script for fixing Persian subtitles.
If you don't want to watch videos with Persian subtitles this script won't be usefull for you..

## User Guide

There is a user document in persian [here](http://aliva.ir/projects/subtitlefixer)

## AUTHORS

Ali Vakilzade

## Quick Guide

### Install

#### deb package

Download the latest deb package from [download page](https://github.com/aliva/SubtitleFixer/downloads) then install with dpkg

    dpkg -i subtitlefixer_xx.yy.deb

#### Other

Copy these lines in a terminal and press enter for auto install.

    su -c 'wget https://github.com/aliva/SubtitleFixer/raw/master/install.sh \
    -O subtitlefixer-install.sh \
    && chmod +x+u subtitlefixer-install.sh \
    && ./subtitlefixer-install.sh'

### Usage

#### Terminal

    subtitlefixer file.srt

#### Nautilus

Right click on srt files in nautilus and select "اصلاح زیرنویس پارسی"

(This Options is only available for 'srt' files)

## COPYING

SubtitleFixer is distributed under the GPL Version 3.
