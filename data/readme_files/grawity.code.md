My giant repo o' random hacks.

Started off as your regular ~/bin dump – with two Finger implementations and a
web server written in PHP. Later got pushed over to ~/code, to make place for
the horde of overgrown aliases that have since taken over ~/bin (which I didn't
consider commit-worthy at first, but then I suddenly had 250 scripts in ~/code
and almost 200 in ~/bin and *five* different Finger implementations...)

tl;dr I write a lot of useless scripts

---

This repository is released under the MIT License, unless declared otherwise in
specific files. (Everything up to commit 93dbb8dd38eb92ddb4cc may also be used
under WTFPL v2.)

The generally useful stuff:

  desktop/
    dbus-name           – list, activate, wait for D-Bus names
    gnome-inhibit       – set & list power management inhibitors in GNOME
  media/
    gnome-mpris-inhibit – disable power management in GNOME while music is playing
    mpris               – control MPRISv2-capable players
  net/
    getpaste            – download pastebin posts as plain text (even ZeroBin)
    tapchown            – change owner of Linux tun/tap network interfaces
    testrad             – test RADIUS auth servers (wrapper for eapol_test)
  term/
    xterm-color-chooser – a color picker for ANSI & Xterm sequences
  x11/
    dbus-name           – list, activate, wait for D-Bus names
    gnome-inhibit       – set & list power management inhibitors in GNOME

The not really useful stuff:

  devel/
    git-find-blob       – find all Git commits that contain a given file
  misc/
    envcp               – borrow the environment of another process
    motd                – show a diff for /etc/motd upon login
    treeify             – translate a list of files to a fancy tree
  net/
    rdt                 – run a recursive rDNS trace
    sprunge             – post to the sprunge.us pastebin
  kerberos/
    kc                  – manage Kerberos ticket caches
    kl                  – like 'klist' except better
    pklist              – like 'klist' except machine-readable
  system/
    upower-monitor      – suspend when UPower claims it's low on battery

The "that's nice... but what's it good for?" stuff:

  lib/python/nullroute/
    authorized_keys.py  – parse ~/.ssh/authorized_keys
    sexp.py             – parse Ron Rivest's S-expressions
  misc/
    treeify             – translate a list of files to a fancy tree
    uniboxify           – convert ASCII box drawings to Unicode box drawings
  security/
    denettalk           – decrypt Nettalk "NCTCTC001"-encrypted messages
    dh                  – do a D-H key exchange over IRC or whatever
    ssh-duphosts        – clean up ~/.ssh/known_hosts
  system/
    locale-check        – half-assed attempt to verify your locale settings
    upower-monitor      – suspend when UPower claims it's low on battery

The rest:

  bin/
    – contains symlinks to all scripts, for my $PATH
  dist/
    – scripts dealing with this repository itself
  obj/
    – compiled binaries for C tools, to allow sharing `~/code` over NFS
  misc/
    – stuff that will, some day, be cleaned up and put in the right place

Moved elsewhere:

  accdb                 – plain-text account & password database
    <https://github.com/grawity/accdb>

  dzenify               – libnotify provider using dzen2
    <https://gist.github.com/grawity/d7d7e93d6c7215188592>

  NullCA                – personal X.509 CA scripts in Ruby
    <https://nullroute.eu.org/git/?p=hacks/nullca-scripts.git>

  ssh-publickeyd        – backend for SecureCRT's "public key assistant"
    <https://github.com/grawity/ssh-publickeyd>

  ~/bin                 – random junk
    <https://github.com/grawity/bin#readme>

Log:

  * 2009-11-28: initial commit of "simplehttpd"
  * 2010-01-01: initial commit of the "main" repository
  * 2014-07-29: cleaned up old branches; moved to refs/attic/* to avoid clutter
  * 2015-03-16: exported security/accdb
  * 2015-04-05: changed default license to MIT
  * 2015-07-10: forked to hacks.git
        - the original, code.git, trimmed down to a bare minimum
        - the fork, hacks.git, merged with Code Recycle Bin
  * 2017-02-01: cleaned up a lot of garbage
  * 2018-05-21: merged hacks.git and code.git again
        - it's still basically the code recycle bin

vim: ts=4:sw=4:et
