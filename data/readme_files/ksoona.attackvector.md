![Dragon](https://raw.githubusercontent.com/ksoona/attackvector/master/gfx/green_dragon.png)

Дtta¢k Vεcтøя Linux a.k.a. 'AVL'
================================
©#!zǝяø88∴» ✪[TØѪμ](http://github.com/thomhastings)™ ✪[5тiиgεя](http://ksoona.github.io)® —[didym0us](http://ejje.weblio.jp/content/65803+Didymos)☻ #!∆∴»~ skip to: [Downloads](https://github.com/ksoona/attackvector/blob/master/README.md#download)
![Propaganda](http://media.arstechnica.com/news.media/linux-desktop-i-want-to-believe.jpg)
「**AttackVector Linux**」 is a new distribution for anonymized* penetration testing & security auditing.  
If you will, the "[dargon](http://www.n1tr0g3n.com/wp-content/uploads/2011/12/Green_dragon_by_archstroke.png)" {[龍](http://dragonkahn.deviantart.com/art/Sleek-and-Sporty-528791)} now has "[tails](http://tails.boum.org)" —get [it](http://5tinger.deviantart.com/art/Sleek-and-Sporty-2-60881670)? Follow the extended [meta](https://www.spaceglasses.com)phor? **AVL** is organized around a [custom](http://sf.net/p/customwheezy7)ized [Kali](http://kali.org) build, using design patterns from [Tails](https://tails.boum.org), as well as aethetic ideas from [Parrot](http://parrotsec.org).  All of the above are based on [Debian](http://debian.org). Дtta¢k Vεcтøя also comes with additional tools not found in these prior art sub-distributions.

-------------------------------------------------------------------

Design Philosophy
=================
**Yin** and _Yang_

_AttackVector Linux_ (A.V.L.) is a [Kali](http://kali.org) [live-build](http://docs.kali.org/live-build/live-build-a-custom-kali-iso) "recipe", which can be thought of as add-ons for Kali live-build.  
The biggest add-on is [Tor](http://torproject.org) _installed_ by default. It is taken from [Tails](http://tails.boum.org)' [design patterns](https://tails.boum.org/contribute/design/).  

**Kali** vs. _Tails_

While Kali requires a modified kernel for network drivers to use injection and so forth,  
TAILS is designed from the bottom up for encryption, and anonymity. These can dovetail.  
**The intention of AttackVector Linux is to provide the capability to anonymize attacks  
_while warning the user when he or she takes actions that may compromise anonymity._**  
The two projects have different design philosophies that can directly conflict with one another.  
In spite of this, the goal of **AttackVector Linux** is to integrate them complimentary into one.

##### Features
* apt/iceweasel/wget all run through tor (using polipo)
* Iceweasel includes cookie monster, [HTTPS Everywhere](https://www.eff.org/https-everywhere), TORbutton, and other great extensions
* Incredible password recovery tools: [hashkill](http://www.gat3way.eu/hashkill) OCLHashcat, many more!
* Great Ruby tools like [Ronin](https://github.com/ronin-ruby/) ...and [Bro](https://www.bro.org)[nin](http://rwnin.blogspot.com)?
* ![Pwnin](http://turing.slu.edu/~hastint/images/ronin2a.jpg)
* Every penetration testing security tool from [Kali](http://kali.org). (Yes, [really](https://gist.github.com/ksoona/5691841).)
* Additional tools for pen-testing, password cracking, and more!
* Dedicated install with FDE and [wordlists](http://turing.slu.edu/~hastint/avl/3804453f6297/) [galore](https://github.com/thomhastings/bt5-scripts#get-wordlistssh).
* Other tools like [PwnSTAR](https://github.com/SilverFoxx/PwnSTAR), FakeAP, sdmem, [mimikatz-en](https://github.com/thomhastings/mimikatz-en), [cortana](https://github.com/rsmudge/cortana-scripts)

Download
========
* Recall you can always just follow the [build instructions](https://github.com/ksoona/attackvector/blob/master/README.md#build-instructions).
* Otherwise, Download Away! » [attack_vector_alpha_0.1.1b.iso](http://bit.do/avlinuxdl)
* ![QR](http://chart.apis.google.com/chart?cht=qr&chs=500x500&choe=UTF-8&chld=H%7C0&chl=http://bit.do/avlinuxdl)
* md5 = 99243d5f4132116e2e9606d6b0c98e6f
* Mirrors: [GDrive](https://docs.google.com/a/attackvector.org/file/d/0B4pmR5w1r5JkWXA4VlJwN19yVEk)
* If you can host a mirror, please do. Also put up torrents. Yes. I'm asking for help. Plz ppl.
* [attackVector.org](https://webcache.googleusercontent.com/search?q=cache:http%3A//turing.slu.edu/~hastint/AttackVector.htm)?

F.A.Q.
======
**Q: Why are you doing this/whom are you doing this for?**  
_A: My design goals were inspired by security professionals who have little time and/or money to put towards finding new tools/frameworks/configurations that would benefit them. That isn't to say this is the only group of people who will find this distro beneficial, but it is the group that I was hoping would find use in the extended tools/toolsets/configurations._

**Q: What's so different about this distro, as opposed to Kali?**  
_A: One of the design goals is anonymity, which security professionals require on various job sites, especially for black-box testing. To accomplish this I took much of the TOR/TSOCKS configuration from TAILS and put it in the Kali build, including starting Vidalia with the GNOME3 window manager. I added many things at the behest of friends, including [Ronin](https://github.com/ronin-ruby/), [FakeAP](https://web.archive.org/web/20131119203514/http://www.blackalchemy.to/project/fakeap/), and more. I also added a bunch of packages from the regular old Debian repos that I like to see. For a full list (more of less) of changes is listed below_

**Q: Can Tor be turned off?**  
_A: Yes, to disable Tor globally simple exit Vidalia, then run the command "/etc/init.d/polipo stop", and finally comment out the config in "/etc/apt/apt.conf.d/0000runtime-proxy" and "/etc/wgetrc". FYI, TOR does not affect anything that is not intentionally proxied through Polipo, meaning that it will not interfere with NMAP, etc._

**Q: Is this only GNOME 3, or can I switch to MATE/KDE/alternate?**  
_Kaneda: Right now I'm building for GNOME 3 specifically, but I will come out with a KDE version due to popular demand. Feel free to give your input regarding alternate window managers and I'll see what I can do._  
_Thom_: I like compiz, screen, tiling windows, drop-down terminal emulators from hotkeys (like Tilda, Guake, or Yakuake) and the Buuf icon theme.
Here's a quick UI brainstorm...
[razor-qt](http://razor-qt.org)
[compiz](http://compiz.org)
[qtile](http://qtile.org)
[openbox](http://openbox.org)
[fluxbox](http://fluxbox.org)
[ion](http://tuomov.iki.fi/software)
I _love_ the Buuf icon theme:
[buuf](http://buuficontheme.free.fr)
Also obviously we could use MATE, XFCE, or LXDE, etc.
  
**Q: One of your design goals is a Windows XP theme? (camouflage)**  
_Kaneda: This is one that's up for debate, but given @thomhastings' insistence that we include it I will get around to it at some point in the near future._
_Thom_: Here's the link from Tails' design: [Windows XP Camouflage](https://tails.boum.org/doc/first_steps/startup_options/windows_camouflage/index.en.html), also: [phillips321 did it on BT5](http://www.phillips321.co.uk/2012/08/28/making-backtrack5-look-like-xp/). I think it's totally useful to avoid suspicion from shoulder-surfers and nosy nancies.
  
**Q: Aren't kiddies going to use this tool to... Chaos?!**  
_A: Probably. I'm not a lawyer._ Here is an official-ish blurb: Customarily, I ([@kensoona](http://twitter.com/kensoona)) am not responsible for any malicious use of this tool, and I hope that releasing it and its source code engenders better information security for the community at large.


Build Instructions
==================
## Install prerequisites for Kali build. This can be done in Debian Squeeze, but we recommend starting from a Kali install:  
```
#!/bin/sh
apt-get install git live-build cdebootstrap kali-archive-keyring
cd /tmp
git clone git clone https://attackvector@bitbucket.org/attackvector/attackvector-linux.git
apt-get remove libdebian-installer4   # /* We reinstall libdebian-installer4 */
apt-get install libdebian-installer4  # /* due to a weird bug */
cd attackvector-linux/live-build-config
```
## Live build:  
```
#!/bin/sh
lb clean --purge
dpkg --add-architecture amd64
apt-get update
lb config --architecture amd64 --mirror-binary http://http.kali.org/kali --mirror-binary-security http://security.kali.org/kali-security --apt-options "--force-yes --yes"
lb build
```

#### Issue Tracker:
Please submit all requests for bugfixes and features for our next release cycle to [GitHub Issues](https://github.com/ksoona/attackvector/issues).  
We release under an "early, occasional" philosophy. That whole "early, often" thing didn't work out.  

##### Target use case(s):
* Research labs targeting malware servers such as command and control servers.
* Legitimate penetration testing consulting companies needing to do black-box testing.
* `"Hacktivists"` living within oppressive governmental regiemes bent on censorship.
* Academics and students working on experimental or other educational research projects.
* Anyone at all seeking plausible deniability, personal privacy, freedom or anonymity.

When I was asking my mentor, a computer security professor who had interned briefly at the CIA, about the ethically gray implications of the project, she replied, `"You can always just call it an academic exercise."`

Further Q&A ([/r/netsec](http://redd.it/1fcrjh))
========================
Q: How is this different from BackBox/[ADHD](http://sf.net/p/adhd)/ArchAssault/myFavDistr.iso?

* 0.) All this FOSS was available elsewhere (different packages and repositories). However, I (@kensoona) would say:
* 1.) No one had stiched the pieces together in this particular way. I'd argue that Tails features and [design goals like these](https://tails.boum.org/doc/about/features/index.en.html#index3h2) are noble ones for a Kali tandem project.
* 2.) Kali's [live-build](http://docs.kali.org/live-build/live-build-a-custom-kali-iso) is designed for uses like this. Think of it as a post-install script that runs as you generate the ISO instead, so it's sorta like a pre-install as opposed to something like [remastersys](http://www.remastersys.com)&[system-imager](http://system-imaging.blogspot.com).

via ex-developer [@kaneda](https://github.com/kaneda):  
* 1) Tor is not configured "globally". It does not break UDP scans. It is set up such that things like wget and Iceweasel use it out of the box but can easily be switched off (in the case of Iceweasel, just hit the TOR button!)
* 2) The additional tools you will find are not ones that many people know about, hence why they were not included in Kali to begin with. Further, I have received permission to distribute any and all of this software (if it did not come with a clear, legal license)
* 3) You can go and look at the build scripts: this is how the ISOs are built, feel free to build it yourself and compare the resultant contents
* 4) As stated in the FAQ, my design goals are to reach pen-testers and security professionals who do not have the time, money, and/or patience to build such a thing, and use them to get feedback regarding further innovations to this product. The immediate intent is not to aid "hacktivists working within oppressive governmental regiemes," but if it does in fact help them, then that's OK too  
* 5) Necessary plug for Kaneda's competitor build, called "Knife" https://github.com/kaneda/knife
* ∆) This is still in **ΛLPHΛ STΛGE**, for bugfixes and feature requests please hassle [AAG](https://github.com/AAG-SATIEDN/attackvector), not @kensoona or @kaneda.

Quotes
======
```
<muts> so basically, your project can be represented as a "live-build" recipe.
<`butane> AttackVector merges the tools of Kali and the anonymity of Tails into the scariest Linux security distribution on the internet
"the Kahn Noonien Singh of Linux distros" ~ stl2600.org
"hardcore penguin on penguin action" - ibid.
```

Add-ons List
============
##### Additional Debian Packages:

###### Packages for service wrapper, supports i2p
* libservice-wrapper-java
* libservice-wrapper-jni
* service-wrapper

###### Package for hashkill
* libssl-dev
* libjson0-dev
* amd-opencl-dev
* nvidia-opencl-dev

###### Packages we want in general
* adduser
* armitage
* binutils
* bsdutils
* chkconfig
* coreutils
* curl
* diffutils
* dnsutils
* dsniff
* findutils
* florence
* fuse-utils
* gnupg
* gnupg-agent
* gnupg-curl
* gnutls-bin
* gzip
* haveged
* i2p
* i2p-router
* ipheth-utils
* iproute
* iptstate
* iputils-ping
* iputils-tracepath
* john
* john-data
* keepassx
* laptop-mode-tools
* libsqlite3-dev
* libsqlite3-ruby1.9.1
* liferea
* liferea-data
* lockfile-progs
* lua5.1
* lzma
* metasploit
* moreutils
* mtools
* ncurses-base
* ncurses-bin
* net-tools
* netcat-traditional
* nmap
* openssl
* pidgin
* pidgin-data
* pidgin-otr
* polipo
* poppler-utils
* pwgen
* rfkill
* ruby1.9.1
* ruby1.9.1-dev
* rubygems
* seahorse
* seahorse-nautilus
* secure-delete
* sqlite3
* sshfs
* ssss
* thc-hydra
* tor
* tor-arm
* tor-geoipdb
* torsocks
* tsocks
* unar
* unzip
* vim-nox
* vim-runtime
* vim-tiny
* wget
* whois
* xul-ext-adblock-plus
* xul-ext-cookie-monster
* xul-ext-foxyproxy-standard
* xul-ext-https-everywhere
* xul-ext-noscript
* xul-ext-torbutton

###### Other Source Packages/Binaries:
* hashkill
* fakeap
* quicksnap

###### Ruby Gems:
* gem install ronin
* gem install ronin-asm
* gem install ronin-dorks
* gem install ronin-exploits
* gem install ronin-gen
* gem install ronin-grid
* gem install ronin-php
* gem install ronin-scanners
* gem install ronin-sql
* gem install ronin-support
* gem install ronin-web

###### Configuration:
* polipo -> tor
* wget -> polipo
* apt -> polipo
* sdmem (wipes memory at shutdown/reboot)

------------------
###### Social ಠ_ರೃ
> Internet Relay Chat (IRC) -> **#attackVector** on Freenode  
> [![Follow Me](http://i267.photobucket.com/albums/ii311/Vap0r_InThe_Wind/Animated%20Pictures/twitter.png)](https://twitter.com/intent/tweet?text=%40attackvector)[![Facebook](http://richardxthripp.thripp.com/files/plugins/tweet-this/icons/tt-facebook-micro4.png)](http://facebook.com/attackVector)[![Linkedin](http://www.hollybrady.com/bradyholly/wp-content/plugins/tweet-this/icons/en/linkedin/tt-linkedin-micro4.png)](http://linkedin.com/in/attackVector)  
> ![Web Mockup](https://sourceforge.net/p/attackvector/screenshot/attackvector_header.jpg)  
> (Web Mockup)

##### RTFM
* [Live Build Manual](http://live.debian.net/manual/3.x/html/live-manual/index.en.html)
* [TAILS git branches](https://tails.boum.org/contribute/git/#index4h3)
* How to [build TAILS](https://tails.boum.org/contribute/build/#index1h1)
* How to [customize TAILS](https://tails.boum.org/contribute/customize/#index1h1)
* [Rebuilding a Kali Package](http://docs.kali.org/development/rebuilding-a-package-from-source)
* [Rebuilding the Kali Kernel](http://docs.kali.org/development/recompiling-the-kali-linux-kernel)
* [Live Build a Custom Kali ISO](http://docs.kali.org/live-build/live-build-a-custom-kali-iso)
* How to [customize Debian live](http://live.debian.net/manual/current/html/live-manual/customizing-contents.en.html)

Project Status
==============
* Build => Success
* Download => UP
* Domain/Hosting
![UML Diagram](https://sourceforge.net/p/attackvector/screenshot/attackvector-uml-diagram2.png)
It seems our best structural approach is customizing the [Kali Live Build scripts](http://docs.kali.org/live-build/live-build-a-custom-kali-iso).  
Eventually this Kali derivative should meet the [TAILS design specifications](https://tails.boum.org/contribute/design/#index13h2).

##### Git Repos (Operation Dovetail)
* [Kali git repositories](http://git.kali.org/gitweb/)
* [TAILS git repositories](https://tails.boum.org/contribute/git/#index3h1)
* Todo: Configure build system to generate & test ISOs ([GitLab](https://gitlab.org)-CI)
* [GitLab.org](http://gitlab.org) for hosting repos cron pull'd from the above (see **base-git-subtree.sh**)
* [GitLab-CI](https://github.com/gitlabhq/gitlab-ci#gitlab-ci-is-an-open-source-continuous-integration-server) Continuous Intergration system uses [Vagrant](http://vagrantup.com), just like [TAILS build](https://tails.boum.org/contribute/build/#index1h1) scripts
* Configure build system to generate & test ISOs (CI)

##### Tasks // To-Do // Unassigned
* [Help port TAILS to Wheezy](https://tails.boum.org/todo/Wheezy/)
* Evaluate features of each distro & unify them into a single kernel
* Provide two layers of functionality: [desktop](http://www.dorkfolio.net/kernel-repository) install and [live](http://www.irongeek.com/i.php?page=videos/portable-boot-devices-usb-cd-dvd)
* Evaluate features of each distro & unify them into a single kernel
* **Add warning messages for anonymity risks**
* Full Disk Encryption (FDE) w/ [LUKS](https://code.google.com/p/cryptsetup/): Thank you [Kali](http://www.kali.org/tag/luks/)!
+ Live version on flash storage jump drive for Live Linux on-the-go
+ Full version on dedicated install with [wordlists galore](https://github.com/thomhastings/bt5-scripts#get-wordlistssh)
* Host on [AttackVector.org](http://parrotsec.org) (?)
* Provide documentation!
* Continue to integrate high [quality](http://www.fuzzysecurity.com/coding.html) [tools](https://github.com/thomhastings/bt5-scripts#get-scriptssh)
* cron Clone the Kali&Tails git repos so that AttackVector can stand-alone
+ Change live build to run off this/these new mirror(s)
+ Torrent tracker? just for downloads...
* Debian repositories! via git-pkg
* Add [more](https://www.trustedsec.com/downloads) [tools](https://github.com/trustedsec)!
* Automate!

--------------
###### license
> [![PRISM-break.org](https://f.cloud.github.com/assets/490579/1184157/1a8794f0-2240-11e3-9809-3db8577d9594.png)](http://prism-break.org)[![Creative Commons License](http://i.creativecommons.org/l/by/3.0/80x15.png)](http://creativecommons.org/licenses/by/3.0/)[![Open Source](http://www.ipol.im/static/badges/open-source.png)](http://www.gnu.org/licenses/gpl.html)[![Hacker Emblem](http://catb.org/hacker-emblem/hacker.png)](http://www.catb.org/hacker-emblem/)  
> Text under [Creative Commons License](http://creativecommons.org/licenses/by-nc-sa/3.0/).  
> Code under [GNU Public License](http://www.gnu.org/licenses/gpl.html).  
> ✮☠卍☤✡☥♔卐☠✮  

яøʇɔǝΛʞɔɐʇʇ∀AttackVectØR
========================
via [ÜNiCØD∄SP♠DE](http://unicodespade.wordpress.com)  

*not affiliated with "Anonymous" "4chan" "LulzSec" etc.
