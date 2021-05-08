# Kanan's Mabinogi Mod 
Mods for Mabinogi using JavaScript

## Installation
1. Download the repository by clicking the green **Clone or Download** button, and extract it anywhere on your computer. Alternatively you can download it through the Github desktop application.
2. Download Python 3.5 x86-64 (the **64 bit** version) from
[python.org](https://www.python.org/downloads/release/python-352/) (near the bottom) or use this [direct link](https://www.python.org/ftp/python/3.5.2/python-3.5.2-amd64.exe).
3. While installing Python, make sure you check the box that says **Add Python 3.x to
PATH** or **Add Python to environment variables**, depending on the version you downloaded.
4. To make sure Python was installed correctly, open a command prompt from the start menu and type
`python --version` and you should get a response.

## Injection
There are three methods to start kanan, manually, automatically or debug.
* Manually -  Run the batch file `kanan.bat` then launch Mabinogi manually with your prefer launching method. 
* Automatically - Make sure the path in the `[AutoStart]` section of `config.toml` is correct, then run the batch file `kanan auto start.bat`.
* Debug - Same as manually, but run `kanan debug mode.bat` instead. This method contains information for testing purposes such as patched addresses which are useful for contributors.

It is possible to launch kanan while Mabinogi is already running, but for best results its best to let it inject as Mabinogi launches, and keep it running in the background. You can run `python kanan.py -h` for more usage information. 

Note: If you are running under User Account Control (UAC), be sure to run the respective batch file as an administrator.

## Features at a glance
Look in the `./scripts/` directory for a full list of mods provided with kanan.
* By default most scripts (mods) that come with kanan are enabled. To disable a
mod find the correct section in `config.toml` and set `enable = true` to `enable = false`
* You can attach kanan to different processes if you are running multiple
clients. Open an administrator command prompt where `kanan.py` is located and
run `python kanan.py -p<id>` where `id` is the process id you want to attach to.
 You can also have kanan start multiple clients by running 
`kanan auto-start.bat` or `python kanan.py -s`.
* You can use kanan to load DLL's into Mabinogi by modifying `DllLoader.js`. More
details on what to do are located at the top of that file.
* You can use kanan's data folder as if it was Mabinogi's data folder for file based
mods. Read `UseDataFolder.js` for more detail. Essentially this feature
redirects Mabinogi's data folder, to the data folder `kanan.py` is in, allowing you
to fully mod Mabinogi without touching its folder.
* Simple scripts can be automatically coalesced to cut down on memory usage.
* `PatternScanSnapshot.js` automatically disassembles the locations of patterns
used by each script for archiving and easier updating when a mod breaks.
* Keep kanan running in the background and whenever you close and relaunch Mabinogi
kanan will automatically rerun all the scripts.

Learn about configuring kanan on our [wiki](https://github.com/cursey/kanan/wiki).

## Contributing
Contributions are welcome. If you are contributing a patch that you aren't the
original author of, please give credits at the top of the file. If a patch has
been added and you are the original author of it or know who is, open an issue
so proper credits may be given (or issue a pull request).

## Original patch authors
kanan comes with more mods than are listed here. This is the list of patch 
authors who haven't directly contributed via GitHub's pull requests.
* Blade3575
    * Bitmap font
    * Elf lag
* Step29
    * NPC fast text
    * One click revive
    * Free indoor camera
    * Hide NPC curtains
    * Hide second title
    * No player zoom transparency
    * Mana tunnel lag fix
    * No skill rank up window
    * Windows appear faster
    * Uncapped auto production
    * Mini title menu (TitleOrganize)
    * Mute commerce imp (NoImp)
    * No render sky
* Rydian
    * Transformation mastery collect mode always enabled
    * No persistent fighter chain popup
    * Objects between camera and character do not become transparent
    * Hide main title
* Licat
    * No mount timeout

Many original patches/ideas came from the following projects:
* Fantasia
* MAMP
* JAP
* Gerent/GerentxNogi
* MNG
* Noginogi-Party

And to all the patchers that came before, and all that will come after.

## Thank you to all contributors!
* QewQew
* C0ZIEST
* Kyralis
* x99user
* Aahzmandius
* Poshwosh
* Warsen
* Rydian
* y3tii
* miawsama
* vurtic
* Blade3575
