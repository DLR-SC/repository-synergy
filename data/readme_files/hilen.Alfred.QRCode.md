![Alfred.QRCode](./icon.png)

Alfred.QRCode
======================

A QRcode generator based on [python-qrcode](https://github.com/lincolnloop/python-qrcode) for Alfred Workflows.

## Install Python library:
1. Install python packages tool [pip](https://github.com/pypa/pip) by: `sudo easy_install pip`
2. Install image library [pillow](https://pypi.python.org/pypi/Pillow) by : `sudo pip install pillow`
3. Install [python-qrcode](https://github.com/lincolnloop/python-qrcode) by : `sudo easy_install qrcode`

## Usage:
1. Type `qr text`;
2. Define a hotkey, select some text, press the hotkey;
3. Type `qrfolder` to open the QR code image folder. The image's name is created by your time and content's md5 value.

## Output:
1. The QRCode image your generate will be open with Preview application.
![demo](./demo.png)

## Todo:
- Create a txt file to collect the QR code content.
- Hotkey to open the txt file.

