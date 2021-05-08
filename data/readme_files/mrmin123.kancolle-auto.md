# kancolle-auto

## The king is dead, long live the king!

**kancolle-auto** is officially retired as of 2017-12-09. Further automation development will continue only on [**kcauto-kai**](https://github.com/mrmin123/kcauto-kai), the successor and complete re-write of kancolle-auto featuring better performance, a robust combat engine, and a browser-based interface for setting your config. Join the [kcauto-kai Discord](https://discord.gg/smAhRKw) for kcauto-kai announcements, discussion, and help. Thank you for your past and on-going support!

## Original Readme

**kancolle-auto** is a robust Kantai Collection automation tool run from the command line. Please see the [kancolle-auto GUI APP (KAGA)](https://github.com/waicool20/KAGA), developed by waicool20, for a GUI for kancolle-auto (note: KAGA is not maintained by the developer of kancolle-auto).

***

>**WARNINGS/DISCLAIMERS**

> kancolle-auto is meant for educational purposes only. Actual and prolonged use of kancolle-auto may result in your account being banned. Remember that botting is against the rules!

> I make no guarantees that you will not be caught and penalized using kancolle-auto, so be smart about it. Don't spam expeditions and sorties nonstop 24/7. Try to mimic a human as much as possible with your use of this tool! Relevant discussion can be found [here](https://github.com/mrmin123/kancolle-auto/issues/130).

> In addition, if you let kancolle-auto sortie you might lose ships! It is highly unlikely (multiple checks occur to prevent this from happening) but I make no guarantees! If you're using a viewer with subtitles, please read the 1st question and answer of the [FAQ](#faqcommon-issues)! Also, if you let kancolle-auto use buckets, make sure you can spare them!

***

>**NOTE**

> kancolle-auto is **not** designed to be the **fastest** automation tool. It is designed to be **robust** and **highly customizable**. kancolle-auto is meant to free up your time, energy, and attention, not to net you the most resources or XP in the shortest time possible. It can automate almost every major feature in the game, including combat, and it can run for days on end with minimal to no user intervention.

***

**Please refer to the [releases page](https://github.com/mrmin123/kancolle-auto/releases) for stable releases, or the [master branch](https://github.com/mrmin123/kancolle-auto/archive/master.zip) for bleeding-edge (stable for the most part, but may potentially contain untested and/or buggy code in exchange for additional features). For Event support, please use the master branch for most up-to-date compatibility with the Event.**

Please read the [**kancolle-auto wiki**](https://github.com/mrmin123/kancolle-auto/wiki) for more details:

* The [**Changelog**](http://github.com/mrmin123/kancolle-auto/wiki/Changelog) will have information on the differences between the releases and master branch
* Please refer to the [**Setup**](https://github.com/mrmin123/kancolle-auto/wiki/Setup) page for instructions on setting up kancolle-auto
* Examples of the config can be found [**here**](https://github.com/mrmin123/kancolle-auto/wiki/Example-configs), while Event-specific config examples can be found [**here**](https://github.com/mrmin123/kancolle-auto/wiki/Event-configs)


### Features

* Expedition module &mdash; automate expeditions
* PvP module &mdash; automate PvP, including diamond and line abreast formations versus submarine-heavy fleets
* Combat module &mdash; automate sorties, node selections, repairs, and submarine switching
  * Supports sorties to Event maps, Combined Fleets, LBAS, and pre-boss/boss support expeditions
* Quests module &mdash; automate quests
* Individual toggles for each of the above modules
* Scheduled sleeping/pausing of script
* Rudimentary catbomb recovery
* Separate `config.ini` file for easier configuration and backup of configurations
* Random variations to help avoid bot detection
* Helpful timers and other messages in console (when using SikuliX in command line mode)

For a more in-depth list of features, as well as installation/usage directions, please refer to the [kancolle-auto wiki](http://github.com/mrmin123/kancolle-auto/wiki).

kancolle-auto was originally a fork of [these](https://github.com/amylase/kancolle-auto) [other](https://github.com/Yukariin/kancolle-auto) [projects/forks](https://github.com/kevin01523/kancolle-auto), but has since outgrown on them in scope and function. Some ideas were inspired by [another similiar tool](https://github.com/tantinevincent/Onegai-ooyodosan).

### Quick Start

1. Install [Java JRE 8](http://www.oracle.com/technetwork/java/javase/downloads/jre8-downloads-2133155.html)
2. Install the latest [SikuliX Nightly](http://nightly.sikuli.de/) with options 1 (Pack 1) and 3 (Tesseract OCR) selected (these are important!)
3. Install kancolle-auto
4. [Setup kancolle-auto's config file](https://github.com/mrmin123/kancolle-auto/wiki/Setup-config.ini) ([standard examples](https://github.com/mrmin123/kancolle-auto/wiki/Example-configs)/[event examples](https://github.com/mrmin123/kancolle-auto/wiki/Event-configs))
5. Run Kantai Collection
6. Run kancolle-auto using command `java -jar <path_to_sikuli>/sikulix.jar -r <path_to_kancolle_auto>/kancolle_auto.sikuli` (replacing `<path_to_sikuli>` and `<path_to_kancolle_auto>` with the correct directories for your installs)

### FAQ/Common Issues

#### Q: Can I lose my ships using kancolle-auto?

A: It's highly unlikely, but I can make no guarantees. There is a caveat to 'highly unlikely', however: if you're using a viewer with subtitles and those subtitles cover up ship portraits on the post-combat results screen (typically the last ship in a fleet if the subtitles are at the bottom of the screen), it can hinder kancolle-auto's ability to accurately detect ships in danger of being sunk. Either lower the subtitle's font size so that it does not cover up the results screen (I personally use a font size of 12px on KC3Kai), or disable them entirely.

You could also lose ships if you set the Combat module's LastNodePush to `True` and accidentally push into a comabt node. Hopefully the warnings in the config file will help you make the right decision regarding this flag.

#### Q: Can I do other stuff on the machine/play Kantai Collection while kancolle-auto is running?

A: Sometimes. kancolle-auto takes control of the mouse as it runs so it will be difficult to do anything meaningful while kancolle-auto is actively running. During scheduled pauses, however, you have full control of the machine. Just make sure that Kantai Collection is not in the middle of a PvP or Sortie when the schedule pause ends. The script will crash and you will have to restart the script.

#### Q: kancolle-auto crashes on startup (AttributeError ( 'NoneType' object has no attribute 'x' ) error)

A: Check/try the following:

* If you have multiple monitors, make sure Kantai Collection is running on the primary monitors. Sikuli can only find windows on the primary monitor.
* Make sure your Kantai Collection game window is scaled/resized to 100% (no resize). kancolle-auto only works if your game is in its original scale.
* Disable any extensions or plugins that might obstruct the Kantai Collection game window.
* The moment the script starts, manually click on the game window to switch focus to it.

#### Q: kancolle-auto periodically restarts and/or crashes!

A: kancolle-auto is fairly stable at this moment. Assuming your dependencies (Java, Sikuli, and Tesseract) and config are set up properly, crashes might be specific to your viewer, machine, internet connection, etc. To help mitigate these issues please turn to the `SleepModifier` parameter in the config. This value raises the buffer time kancolle-auto takes between steps, and can address most issues not caused by actual bugs in the code. Begin with 1 and gradually raise it to 10. If this does not eliminate or reduce the number of restarts and crashes, only then please open a detailed issue ticket.

Side note 1: If you are on Windows, also try disabling time synchronization on the OS level ([relevant information](https://answers.launchpad.net/sikuli/+question/194095)).

Side note 2: Certain VMs and VM setups have been known to cause issues with Sikuli image matching. If you are running kancolle-auto on a VM, try restarting your environment, or switching to a different VM.

#### Q: kancolle-auto does not take timers into consideration and/or I get OCR warnings (n0text warnings)

A: You're missing the tesseract OCR files. Please re-install Sikuli with the correct settings.

#### Q: I started getting catbombed frequently after I started using kancolle-auto!

A: You probably botted too much and triggered the game's bot protection. Use the ScheduledSleep functionality and let the program pause itself for a few hours every day.

#### Q: This command line stuff blows... isn't there an easier and prettier way to run kancolle-auto?

A: Please refer to the [kancolle-auto GUI APP (KAGA)](https://github.com/waicool20/KAGA) for your GUI needs.
