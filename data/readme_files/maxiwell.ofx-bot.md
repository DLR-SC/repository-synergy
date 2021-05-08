OFX-BOT
=============

These bots will help you to automate the bank reconciliation with Brazilian banks: Banco do Brasil,
Caixa Economica, Itau, Santander and NuBank. You can use financial software that supports OFX format, like 
GNUCash, HomeBank.free.fr and Microsoft Money. 

#### ofx-bb:
* Downloading 'ofx' from checking account
* Downloading 'ofx' from saving account
* Downloading 'ofx' from Petrobras credit card

#### ofx-caixa:
* Downloading 'ofx' from checking account

#### ofx-itau:
* Downloading 'ofx' from checking account
* Downloading 'csv' from checking account
* Downloading 'csv' from credit card

Run ``ofx-itau --help`` for more options.

#### ofx-santander:
* Downloading 'ofx' from checking account

#### ofx-nubank:
* Downloading 'ofx' from credit card

Run ``ofx-nubank --help`` for more options.

Requirements:
--------------

#### ofx-bb, ofx-caixa and ofx-santander
* Python2 Selenium package

```bash
pip2 install selenium
```

#### ofx-itau and ofx-nubank

* Haskell Stack package:

```bash
wget -q -O- https://s3.amazonaws.com/download.fpcomplete.com/ubuntu/fpco.key | sudo apt-key add -
echo "deb http://download.fpcomplete.com/ubuntu/$(lsb_release -sc) stable main"|sudo tee /etc/apt/sources.list.d/fpco.list
sudo apt-get update
sudo apt-get install stack
```

* Compiling:

```bash
cd itau
./build.sh
```
or

```bash
cd nubank
./build.sh
```

* The first ``build.sh`` execution will download all packages in ``~/.stack``.

Using:
-------------

```bash
./ofx-bb.py
./ofx-caixa.py
./ofx-itau
./ofx-santander.py
./ofx-nubank
```

Using files:

```bash
./ofx-bb.py < input.cfg
./ofx-caixa.py < input.cfg
./ofx-itau < input.cfg
./ofx-santander.py < input.cfg
./ofx-nubank < input.cfg
```

Hiding the browser window:

```bash
xvfb-run --server-args="-screen 0, 1440x900x24" ./ofx-bb.py < input.cfg
```

More Instructions:
-----------------------

More details in the [PT-BR Readme](README-ptbr.md)

