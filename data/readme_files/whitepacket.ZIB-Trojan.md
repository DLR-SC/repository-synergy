<h3>Project</h3>
The Open Tor Botnet (ZIB) Official Release<br>
<h3>General information and instructions.</h3>
The Open Tor Botnet requires the installation and configuration of bitcoind, however I neglect to detail this here out of a lack of time.<br>
This bot-net is fully undetectable and bypasses all antivirus through running on top of Python27's pyinstaller, which is used for many non-Trojan computer programs. The only hypothetical possibility of detection comes from the script, however, the script contains randomized-looking data through using a randomized AES key and initialization vector, meaning this is a non-issue.<br>
ZIB.py is the main project file.<br>
intel.py is the chat bot for handling automatic transactions and client authentication.<br>
compileZIB.py is used by intel.py, and is started in the background using chp.exe<br>
ZIB_imports.txt contains all the Python module imports that ZIB uses. They're appended to the script during compilation.<br>
btcpurchases.txt includes all the Bitcoin payments that are pending. Pending transactions older than 24 hours are deleted.<br>
channels.txt includes all completed BTC payments.<br>
Point your webserver to C:\Python27\dist\ for hosting the bot executables.<br>
chp.exe is required in the local dir.<br>
For the IRC server, run bircd, set up an oper with the username Zlo and password RUSSIA!@#$RUSSIA!@#$RUSSIA!@#$RUSSIA!@#$. For the max users per ip set to 0 because tor users all connect from 127.0.0.1 and look the same to the IRCd. Keep all scripts in C:\Python27\Scripts.<br>
Put nircmd in the local directory for editing file dates.<br>
<h3>Credits/Attribution</h3>
WhitePacket<br>
<h3>Legal</h3>
The Open Tor Botnet is for legal, research purposes only.<br>
Please don't use this for malicious purposes. This was released out of good will for the benifit of others.<br>
This bot may contain a small amount of stolen code.<br>
<h3>Features</h3>
ZIB is an IRC-based, Bitcoin-funded bot network that runs under Tor for anonymity.<br>
ZIB is coded totally from scratch.<br>
ZIB uses the Department of Defense standard for encryption of Top Sercret files as one method of generating fully undetectable binaries every time!<br>
ZIB creates a new binary for every client with varying file sizes, creation dates, and rot13->zlib->base64->AES-256(random key+IV) encrypted strings.<br>
ZIB is fully undetectable (FUD) to Anti-Virus.<br>
ZIB has an automated system for handling payments, providing bot-net binaries, and creating bot-net IRC channels.<br>
All bot networks on a ZIB network require a password to join.<br>
ZIB uses passworded user-based authentication, handled through our Zlo intelligence bot, so you don't have to worry about channel password, main password, or bot compromise. Normal users can't create their own channels. All IRC functionalities are handled by the Zlo IRC intelligence bot. You can do authenticated, single bot commands through Zlo, or set up a user session on your bots, which is slightly less secure.<br>
Paid users (paid in terms of sending BTC to Zlo once you set up your IRC server. This bot-net is meant to accept payments to host bots for other people, not just a single bot-net.) get unlimited bot space per channel.<br>
Our bot has been tested on and is fully compatible with Windows Server 2008 R2 32-bit, Windows XP SP1 & SP3 32-bit, Windows 7, and Windows 8 64-bit.<br>
<h3>Features</h3>
Multi-threaded HTTP/s (layer7 [Methods: TorsHammer, PostIt, Hulk, ApacheKiller, Slowloris, GoldenEye]), TCP/SSL, and fine-tuned UDP flooding. Ability to flood hidden services, or attack via the clearnet. 66 randomized DDoS user-agents and referers. All methods send randomized data, bypass firewalls, filtering, and caching. ZIB also comes with FTP flood, and TeamSpeak flood.<br>
Undetectable ad-fraud smart viewer that's fully compatible with Firefox, Tor Browser Bundle, Portable Firefox, Internet Explorer, Google Chrome, Opera, Yandex, Torch, FlashPeak SlimBrowser, Epic Privacy Browser, Baidu, Maxthon, Comodo IceDragon, and QupZilla.<br>
Download & Execute w/ optional SHA256 verification.<br>
Update w/ optional SHA256 verification.<br>
Chrome password recovery.<br>
Each bot can act as a shell booter and utilize external php shells for attacks.<br>
Replace Bitcoin addresses in clipboard with yours.<br>
FileZilla password recovery.<br>
Fully routed through Tor.<br>
File, registry, startup folder, and main/daemon/tor process persistence.<br>
Installation and use is completely hidden from bots.<br>
0/60 Fully undetectable to Antivirus.<br>
File download/upload.<br>
Process status, creator, and killer.<br>
Undetectable, instant obfuscation when generating new binaries.<br>
Self spreading.<br>
All bot files are SHA256 hash verified. Broken/corrupted files get replaced.<br>
Bypasses AntiVirus Deep-Scan.<br>
Bot location varies, depending on administrative access.<br>
IRC nickname format: Country[version]windows version|CPU bits|User Privileges|CPU cores|random characters. Ex: US[v2]XP|x32|A|4c|F4L0s4kpN5. 64-bit detection may be having issues (shows up as 32-bit).<br>
Disables various windows functions WITHOUT giving the user warnings!<br>
Disables Microsoft Windows error reporting, sending additional data, and error logging - System-wide as administrator, and on a per-user basis.<br>
Disables User Access Control (UAC) - System-wide as administrator, and on a per-user basis.<br>
Disables Windows Volume Shadow Copy Backup Service (vss) - System-wide as administrator.<br>
Disables System Restore Service (srservice) - System-Wide as administrator.<br>
Disables System Restore - System-Wide as administrator.<br>
Melts on execution. Original file gets deleted. Should delete the file out of the temporary folder, if used with a binder.<br>
Multi-threaded mass SSH scanner that saves servers are on the bot's HDD encoded with base64 without duplicates, or honeypots. Four integrated password lists of increasing difficulty [A,B,C,D], or brute force with min/max characters (supports numbers, upper/lowercase letters, symbols). Cracked routers are used for UDP/TCP/HTTP/ICMP flooding. UDP flood requires having the routers download a python script, and the majority of routers won't have Python. Has the ability to be used to take down DDoS-protected servers from scanning with just one bot. The Open Tor Botnet optionally will scan under Tor, multiple ports at once, ip range/s [A/B/C] or randomized IPs, optionally block government IPs, blocks reserved IPv4 addresses aside from the user's LAN.
BotKiller with file scanning [kills .exe, .bat, .scr, .pif, .dll, .lnk, .com] in AppData, Startup, etc and has been successful against NanoCore, Andromeda, AGhost Silent Miner, Plasma HTTP/IRC/RAT, and almost every HackForums bot. The botkiller utilizes process scanning with file deletion, and registry scanning.<br>
Mutex. No duplicate IRC connections.<br>
Amazing error handling, install rate, detection ratio, and persistence.<br>
Completely native malware. No .NET framework, or Python installation required!<br>
Installs to the startup folder & AppData with a registry RUN key.<br>
Kills all popular anti-virus and prevents A/V installation. Will disable Anti-Virus which have rootkits, through deleting important A/V dlls.<br>
BotKiller, scanner, and A/V killer are optional. You could easily run the Open Tor botnet as a back-up for your bots, or install other software on them as back-up. The network control system is highly scaleable.
Duel-process and duel-file persistence. Files processes are re-created nearly instantly, after being removed.<br>
Recovers File-Zilla logins, which is great for getting SSH, and FTP logins.<br>
Automatically removes some ad-ware.<br>
Contains an Omegle spreader which spreads either a link through social engineering tactics, or a Skype account with every line of text being completely unique in order to avoid detection. Always waits for the Omegle stranger to type a message before responding with a reply. Shows stranger typing, and writes messages human-like. Multi-threaded.<br>
Deletes zone identifier on all bot files, Tor, download & executed files, and update files. This means that you don't get the "Would you like to run this program?" dialog, and it runs completely hidden.<br>
Detects all Windows operating systems from Windows 95, ME, to 8. Will show Windows 10 as just Windows, or W8.
Text-To-Speech with speaker detection.<br>
Duplicate nick-name handling, and ping-out handling.<br>
Tor is downloaded directly from the Tor Project - It only needs to be downloaded once, but still has persistence.<br>
Grabs the bot IP address on startup, has the ability to disable/enable bot command response, view status of ssh scanner/omegle spreading/ddos/botkiller and start/stop them.<br>
Functionality to kill the bot instance, uninstall ZIB, grab full OS info, check if a host on a certain port is online/offline using TCP connect and a full HTTP request whilst checking the reply for server status related information.<br>
Check if a process is running, how many are running, and list directories. Use \ instead of C:\, e.x !dir \ as some people run their main operating system on non-standard drive letters, especially on servers.<br>
Upload specific files of your choosing that exist on a bot's computer to your FTP server. Files that can be uploaded could include BTC wallets.<br>
Read files in plain-text off zombie computers. View amount of scanned SSH servers. Kill processes. The bot will tell you about missing command parameters, if a certain parameter contains the wrong data-type, etc. Errors from executing a command are outputted to the IRC channel without flooding the chat.<br>
Commands are ran mutli-threaded and con-currently. This means your bots wont freeze up each time you run a command.<br>
<h3>Notes</h3>
The default server won't accept new channels unless the client purchases one.<br>
This is filled with *some* wrong information, non-commented code, etc.<br>
<h3>Contact</h3>
Email: chris@whitepacket.com<br>
Twitter: @WhitePacket<br>
