
# REBEL-FRAMEWORK
![version](https://img.shields.io/badge/version-v0.1.0-green.svg)
![Supported OS](https://img.shields.io/badge/Supported%20OS-Linux-yellow.svg) 
![License](https://img.shields.io/badge/license-GPLv3-blue.svg)
![Modules](https://img.shields.io/badge/modules-43-green.svg)
<br>
automate the automation
<br>
## START
``` 
git clone https://github.com/rebellionil/rebel-framework.git
cd rebel-framework
bash setup.sh
bash rebel.sh
```
## MODULES
![screenshot at 2018-06-15 13-51-44](https://user-images.githubusercontent.com/22657154/41466679-488a6e48-7071-11e8-8ca4-763892f0759c.png)

## SCREENSHOTS
![screen2](https://user-images.githubusercontent.com/22657154/41472454-781c73e6-7084-11e8-8057-be1a11bfd718.png)

![screen3](https://user-images.githubusercontent.com/22657154/41472456-7972673c-7084-11e8-879b-d4ab3d4a8e0c.png)

## DEMOS
[![asciicast](https://asciinema.org/a/hCkHKyb57TrnY0v85xRw53NGJ.png)](https://asciinema.org/a/hCkHKyb57TrnY0v85xRw53NGJ)

[![asciicast](https://asciinema.org/a/OiKfx95E17Pjc389PZuTBitsa.png)](https://asciinema.org/a/OiKfx95E17Pjc389PZuTBitsa)

[![asciicast](https://asciinema.org/a/9Kt0jMXR9gBLV3eCUMqZsbWzb.png)](https://asciinema.org/a/9Kt0jMXR9gBLV3eCUMqZsbWzb)

## SUPPORTED DISTRIBUTIONS
|Distribution | Version Check | supported | dependencies already installed |status |
----------|-------|------|------|-------|
|Kali Linux|4.4.0 | yes| yes | working   |
|Parrot OS|4.14.0 |yes|yes|working   |

## PORT YOUR OWN TOOLS TO REBEL !
- scan.py
```shell
┌─[root@parrot]─[~]
└──╼ #python scan.py -h


     -h --help    print usage
     usage ./scan.py <target>

```

- controller.sh sample
```bash
#!/bin/bash

normal='\e[0m'
arr[0]='\e[1;94m' ; blue=${arr[0]}
arr[1]='\e[1;31m' ; red=${arr[1]}
arr[2]='\e[1;33m' ; yellow=${arr[2]}
arr[3]='\e[1;35m' ; purp=${arr[3]}
arr[4]='\e[1;32m' ; green=${arr[4]}
arr[5]='\e[97m'   ; white=${arr[5]}
grayterm='\e[1;40m'

module=$(echo $1 | cut -d '/' -f 2 )

if [[ $module != "scan" ]] ; then
   echo -e "${red}[x] Wrong module name"
   exit
fi   

misc(){
    if [[ $1 == "back" ]] || [[ $1 == "exit" ]] || [[ $1 == "quit" ]] ; then
        exit
    elif [[ $1 == '!' ]] ; then
        $2
    elif [[ $1 == "clear" ]] || [[ $1 == "reset" ]] ; then
        clear   
    elif [[ $1 == "help" ]] || [[ $1 == "?" ]] ; then
        bash print_help_modules.sh help 
    elif [[ $1 == "banner" ]] ; then
        rand="$[ $RANDOM % 6 ]"
        color="${arr[$rand]}" # select random color
        echo -e $color
        python print_banner.py  
    elif [[ $1 == "" ]] ; then
        :               
    else
       echo -e "${purp}[-] Invalid parameter use show 'help' for more information"         
    fi    
}

target="site.com"

while IFS= read -e -p "$( echo -e $white ; echo -e ${grayterm}{REBEL}➤[${white}$1]~#${normal} ) " cmd1 ; do
    history -s "$cmd1"
    if [[ ${1} =~ 're/' ]] ; then
      if [[ $( echo $cmd1 | cut -d " " -f 1 ) == "show" ]] ; then
        if [[ $( echo $cmd1 | cut -d " " -f 2 ) == "options" ]] ; then
          {
            echo -e "  Option\t\t\t\t|Value"
            echo -e "  ======\t\t\t\t|====="
            echo -e "  target\t\t\t\t|$target"
          } | column -t -s "|"
        elif [[ $( echo $cmd1 | cut -d " " -f 2 ) == "modules" ]] ; then
          bash print_help_modules.sh modules
        elif [[ $( echo $cmd1 | cut -d " " -f 2 ) == "help" ]] ; then
          bash print_help_modules.sh help
        fi 
      elif [[ $( echo $cmd1 | cut -d " " -f 1 ) == 'set' ]] ; then
          if [[ $( echo $cmd1 | cut -d " " -f 2 ) == 'target' ]] ; then
             target=$( echo $cmd1 | cut -d " " -f 3- | sed "s/'//g")
          fi
      elif [[ $( echo $cmd1 | cut -d " " -f 1 ) == 'run' ]] ; then
          python scan.py $target
      else 
         misc $cmd1  
      fi
   fi
done    
```
## BUG ? 
### OPEN NEW ISSUE   
https://github.com/rebellionil/rebel-framework/issues

## TODO
- [ ] Add wireless modules
- [ ] Add memory forensics modules
- [ ] Add java and pyc decompilers
- [ ] Make rebel scriptable and add command line arguments 
- [ ] Add bruteforce modules

## DONATE
| COIN | ADDRESS |
------|----------|
| ETH | 0x46409ba4e86313d99a5e13DD1Ca5f82d95529553 |
| BTC | 11wqnCon1V3NmYGbkLtZtAWaqbH3Nc3VS          |
## EXTERNAL PROJECTS USED INSIDE THE FRAMEWORK 
https://github.com/rebe11ion/tornado
<br>
https://github.com/rebe11ion/CryptNote
<br>
https://github.com/1N3/BlackWidow
<br>
https://github.com/Dionach/CMSmap
<br>
https://github.com/vincepare/DirScan
<br>
https://github.com/s0md3v/Decodify
<br>
https://github.com/UndeadSec/SocialFish
<br>
https://github.com/evait-security/weeman
<br>
https://github.com/m4ll0k/Infoga
<br>
https://github.com/Moham3dRiahi/Th3inspector
<br>
https://github.com/sdushantha/qr-filetransfer
<br>

- special thanks for Mahmoud Mohamed for helping improve the project quality by testing it in several environments.

© 2018
