# JTB Investigator

### A tool born out of laziness
------

###### This tool was born out of the unhappy marriage of terrible telemetry and tooling built into BitSight and my general laziness when it comes to doing a lot of look ups on Domain Names and IP addresses.

------

JTB (Just the basics) Investigator is a simple framework to ease the monotonous looks up many of us do every day. When you get an alert and need to track down an IP or Domain Name or just in general investigation, we often do the same basic look ups (NSLookup, Nmap, whois, etc.) over and over. Trying to manage the different terminals and out puts became annoying and cumbersome to me so I wanted to make it easier.

Author: [@Th3J0kr](https://twitter.com/Th3J0kr)
More information: [My Blog](https://www.purpleteamsec.com/)

Version: 2.1

------

## Installation

The setup is very simple:

##### Ensure you have nmap, whois, and python 3 installed on the system
###### *Only tested on linux systems with python 3.7 (but should work with all python3)*

### Install python requirements with pip
`pip3 install -r requirements.txt`

Make sure you have `nmap` and `dnsutils` installed

### Clone the repo
`git clone https://github.com/Th3J0kr/jtb_investigator.git`

And you're good to go!

### Post Installation
In order to do ASN Lookups the pyasn module requires a local ASN Database file located in `asn_db/` by default.

If you want to update this file, which you should every so often, just run the `update.sh` script in the `asn_db/` directory.

This database file is included in the repo but a new one can be downloaded by going into the `asn_db/` directory and running `pyasn_util_download.py --latest` then `pyasn_util_convert.py --single <Downloaded RIB File> ipasn_db_main.dat` (IMPORTANT: backup the old file first `mv ipasn_db_main.dat ipasn_db_main.dat.bak` and name the new one `ipasn_db_main.dat`). For best results this should be down fairly regularly.

## Usage

Using is very simple, that's the whole point. Not just to help us that do this manually everyday but also to make it easier for newbs to do these looks more quickly!

### Command line usage

```
usage: jtb.py [-h] [-i IP] [-n HOSTNAME] [-r REPORT] [-d] [-f FORMAT] [-p]
              [-t TIME] [-m MASS] [-c COMBINE] [-v]

Investigate from the command line

optional arguments:
  -h, --help            show this help message and exit
  -i IP, --ip IP        IP to investigate
  -n HOSTNAME, --hostname HOSTNAME
                        Hostname to investigate
  -r REPORT, --report REPORT
                        Report to import
  -d, --disable         Disable auto investigate when starting with option
  -f FORMAT, --format FORMAT
                        Format to export to. Avoids prompt for CLI auto
                        investigate.
  -p, --passive         Passive recon only. Doesn't run nmap or any scans that
                        interact with the target itself.
  -t TIME, --time TIME  Convert time from UTC to Local Time and quit. (format:
                        2018-10-16 21:22:23)
  -m MASS, --mass MASS  Filename of hostnames or ips to investigate. Must
                        start with "hostnames_" "ips_", supports txt and csv 
                        import files
  -c COMBINE, --combine COMBINE
                        Name to give file after combine
                        (<filename>_combined.<format>
  -v, --version         Print JTB version currently installed
```

There is various mixing and matching that is supported. While I'm too lazy to document all possible combinations, check out the examples at the bottom for more help.

#### Auto Investigate via CLI

Using the command line makes the lookups even faster. After I added this feature I realized there isn't much point of the menu driven part but ASCII art is fun so...

Anyway it's easy to automate it all with: `./jtb.py -i <ip to investigate>` or `python3 jtb.py -n <hostname to investigate>`

This will spit the report(s) into the `reports/` directory in `<hostname or ip>_report.txt`.

Or if you have a file of hostnames or ips. Supports `.txt` (each on new line) and `.csv` host lists. (Filename must start with "ips_" or "hostnames_"): `./jtb.py -m <filename>`

This will spit the report(s) into the `reports/` directory in `<hostname or ip>_report.csv`. Or you can specify the format with `-f <format>` at the end. 

#### Start an investigation with IP and/or hostname from CLI

If you add the `-d` option along with `-i` or `-n` then JTB will start a new investigation with the information provided. Adds control from the CLI.

#### Import via CLI

Run `./jtb.py -r <filepath to report>` to import a report and drop back into the investigation session

#### Convert Time via CLI

Run `./jtb.py -t <YYYY-mm-dd HH:MM:SS>` to convert UTC Time to Local Time. Use if your logs are in local time but you get alerts from a different tool in UTC

#### Combine exisitng reports into 1 file via cli

Run `./jtb.py -c <name>` where name will be the beginning of the new combined file `<name>_combined.<format>`

### Menu Driven

#### Main Menu

Just `cd` into the `jtb_investigator` directory and run `jtb.py` with `./jtb.py` or `python3 jtb.py`

You will be greeted with:

```
Choose an option: 
1: Open a new investigation
2: Import a previous investigation
3: Mass Investigator of file (file must start with "hostnames_" or "ip_"
4: Combine current reports into 1 file for each format
99: Quit
> 
```

This just gives a menu driven UI to the command line options. Choose an option to get started.

#### Investigation Menu

Once you have started your investigation of an IP or Domain Name you will be presented with a menu of options:

```
Choose an option: 
0: Display help
1: Print working host info
2: Print Investigation report
3: Lookup missing info
4: Nmap it
5: Get whois info
6: ASN Lookup
7: Blacklist check
8: Auto Investigate
95: Convert time from UTC to Local Time
96: Export Investigation
97: Change IP
98: Change Domain Name
99: Back to main menu (destroys current investigation)
> 
```

#### Menu Options

`0`: Display help information

`1`: Print info about the host (IP and Domain)

`2`: Print all the information gathered so far.

`3`: Get either the IP or the Domain Name depending which you have already provided

`4`: Get open ports on target host (Only scans 21-100,443-445,3389,8080,8081 right now)

`5`: Do a whois lookup and store import information to investigation report

`6`:  Get ASN information on the target host.

`7`: Check if hostname is in SPAMHAUS DBL, SPAMHAUS ZEN or SURBL

`8`: Let the Investigator collect as much information for you as possible (Runs all modules against what it has)

`95`: Convert time from UTC to Local Time (Useful for splunk searches if alert is in UTC)

`96`: Export the report to a file. Currently support CSV, JSON, and txt. Saved to `reports/<csv/txt>/<hostname/ip>_report.<file type>`

`97`: Change IP of target

`98`: Change Domain Name of target

`99`: Go back to main menu. Destroys current investigation

## To Do:

This framework is still in the very early stages of development. There will likely be lots of bugs and errors so don't hesitate to contribute or open an issue on github.

It is written to be easily extended. All the options are classes in the `modules.py` file. To add a new module just add an option to the menu and write a new class in `modules.py`. Pull requests to extend features are welcome

## Examples:

Convert time: `./jtb.py -t '2018-10-16 21:22:23'`

Start investigation with a hostname: `./jtb.py -n scanme.nmap.org -d`

Start investigation with an IP: `./jtb.py -i 8.8.8.8 -d`

Get all information you can about hostname: `./jtb.py -n scanme.nmap.org`

Get all information you can about hostname using only passive techniques: `./jtb.py -n scanme.nmap.org -p`

Get all information you can about hostname and send to csv report (avoids the prompt after the investigation): `./jtb.py -n scanme.nmap.org -f csv`

Combine all reports currently in reports (exluding already combined files) into `new_combined.<format>`: `./jtb.py -c new`

Run batch investigation of hostnames in hostnames_test.txt in passive mode (without nmap) and export report in json (csv is default): `./jtb.py -m hostnames_test.txt -p -f json`

Run batch investigation of hostnames in hostnames_test.txt in passive mode (without nmap) and export report in json (csv is default) then combine files into `test1_combine.json` (warning also combines other reports): `./jtb.py -m hostnames_test.txt -p -f json -c test1`
