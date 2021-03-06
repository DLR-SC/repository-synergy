# FileInsight-plugins: a decoding toolbox of McAfee FileInsight hex editor for malware analysis

FileInsight-plugins is a collection of plugins for McAfee FileInsight hex editor.
It adds many capabilities such as decryption, decompression, searching XOR-ed text strings, scanning with a YARA rule, and more!
It is useful for various kind of decoding tasks in malware analysis (e.g. extracing malware executables and decoy documents from malicious document files).

## Screenshots
![screenshot1.png](docs/screenshot1.png)

![screenshot2.png](docs/screenshot2.png)

## How to install
### Automatic installation
Please execute the following command. FileInsight-plugins and all pre-requisites will
be installed.

```
powershell -exec bypass -command "IEX((New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/nmantani/FileInsight-plugins/master/install.ps1'))"
```

If you use a HTTP proxy, please download install.ps1 and edit $PROXY_HOST and $PROXY_PORT variables in it,
then please execute the following command.

```
powershell -exec bypass .\install.ps1
```

### Manual installation
Please copy "plugins" folder into %USERPROFILE%\Documents\FileInsight .
You need Python 2.7 (x86) installed in addition to FileInsight.

![folders.png](docs/folders.png)

### **Note regarding Python**
FileInsight is incompatible with Python 3 and plugins can not be used with Python 3.
**If you would like to use Python 3 for other tools, please install Python 2.7 with
the "Install just for me" option.** If you install Python 2.7 with the "Install for
all users" option, FileInsight tries to use Python 3 rather than Python 2.7 and it
fails to execute plugins. And please execute the following command with administrator
privilege to make sure that python.exe of Python 2.7 will be executed from FileInsight.
```
mklink "C:\Program Files (x86)\FileInsight\python.exe" C:\Python27\python.exe
```

### **Note regarding FileInsight installer**
FileInsight was removed from the McAfee Free Tools website.
However, FileInsight installer is still available from the following location.
https://www.mcafee.com/enterprise/en-us/downloads/free-tools/terms-of-use.html?url=http://downloadcenter.mcafee.com/products/mcafee-avert/fileinsight.zip

## Pre-requisites
For the "aPLib compress" and "aPLib decompress" plugins, they require aplib.dll.
Please download aPLib from http://ibsensoftware.com/download.html and copy
aplib.dll (32 bits version) into "Compression operations" folder.

For the "Binwalk scan" plugin, it requires binwalk Python module.
Please get it from https://github.com/ReFirmLabs/binwalk
(pip cannot be used to install binwalk)."

For crypto-related plugins such as "AES decrypt", it requires PyCryptodome Python module.
Please get it from https://github.com/Legrandin/pycryptodome
or execute the following command.
```
C:\Python27\python.exe -m pip install pycryptodomex
```

For LZMA-related plugins such as "LZMA Compress", it requires backports.lzma Python module.
Please get it from https://github.com/peterjc/backports.lzma
or execute the following command.
```
C:\Python27\python.exe -m pip install -i https://pypi.anaconda.org/nehaljwani/simple backports.lzma
```

For the "File type" plugin, it requires python-magic Python module.
Please get it from https://github.com/ahupp/python-magic
or execute the following command.
```
C:\Python27\python.exe -m pip install python-magic-bin
```

For the "Find PE" file plugin, it requires pefile Python module.
Please get it from https://github.com/erocarrera/pefile
or execute the following command.
```
C:\Python27\python.exe -m pip install pefile
```

For the "YARA scan" plugin, it requires yara-python Python module.
Please get it from https://github.com/VirusTotal/yara-python
or execute the following command.
```
C:\Python27\python.exe -m pip install yara-python
```

You can install some of required Python modules with the following command.
```
C:\Python27\python.exe -m pip install -r requirements.txt
```

## Customization
For the "Send to" plugin, please edit "Misc operations\send_to.json" to run your
favorite programs.

## How to use
Please click a category from the "Plugins" tab then select a plugin.

![how_to_use1.png](docs/how_to_use1.png)

You can also use plugins from the right-click menu.

![how_to_use2.png](docs/how_to_use2.png)

Some plugins show an additional dialog for plugin settings at use of them.

![how_to_use3.png](docs/how_to_use3.png)

## How to update
### Semi-automatic update
If you would like to update FileInsight-plugins to the latest release version,
please execute the following command. Existing files will be overwritten.

```
powershell -exec bypass -command "& ([scriptblock]::Create((New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/nmantani/FileInsight-plugins/master/install.ps1'))) -update"
```

If you use a HTTP proxy, please download install.ps1 and edit $PROXY_HOST
and $PROXY_PORT variables in it, then please execute the following command.

```
powershell -exec bypass .\install.ps1 -update
```

### Manual update
Please download the latest release version and copy "plugins" folder into
%USERPROFILE%\Documents\FileInsight to overwrite with the new version.

## List of plugins (71 plugins)
* Basic operations
  * Copy to new file  
    Copy selected region (the whole file if not selected) to new file
  * Delete before  
    Delete all region before current cursor position
  * Delete after  
    Delete all region after current cursor position
  * Fill  
    Fill selected region with specified hex pattern
  * Invert  
    Invert bits of selected region
  * Reverse order  
    Reverse order of selected region
  * Swap nibbles  
    Swap each pair of nibbles of selected region
  * Swap two bytes  
    Swap each pair of bytes of selected region
  * To upper case  
    Convert text to upper case of selected region
  * To lower case  
    Convert text to lower case of selected region
  * Swap case  
    Swap case of selected region

* Compression operations
  * aPLib compress  
    Compress selected region with aPLib compression library
  * aPLib decompress  
    Decompress selected region with aPLib compression library
  * Bzip2 compress  
    Compress selected region with bzip2 algorithm
  * Bzip2 decompress  
    Decompress selected region with bzip2 algorithm
  * Gzip compress  
    Compress selected region with gzip format
  * Gzip decompress  
    Decompress selected gzip compressed region
  * LZMA compress  
    Compress selected region with LZMA algorithm
  * LZMA decompress  
    Decompress selected region with LZMA algorithm
  * LZNT1 compress  
    Compress selected region with LZNT1 algorithm
  * LZNT1 decompress  
    Decompress selected region with LZNT1 algorithm
  * Raw deflate  
    Compress selected region with Deflate algorithm without header and checksum (Equivalent to gzdeflate() in PHP language)
  * Raw inflate  
    Decompress selected Deflate compressed region that does not have header and checksum (Equivalent to gzinflate() in PHP language)
  * XZ compress  
    Compress selected region with XZ format
  * XZ decompress  
    Decompress selected XZ compressed region

* Crypto operations
  * AES decrypt  
    Decrypt selected region with AES
  * AES encrypt  
    Encrypt selected region with AES
  * ARC2 decrypt  
    Decrypt selected region with ARC2 (Alleged RC2)
  * ARC2 encrypt  
    Encrypt selected region with ARC2 (Alleged RC2)
  * ARC4 decrypt / encrypt  
    Decrypt / encrypt selected region with ARC4 (Alleged RC4)
  * Blowfish decrypt  
    Decrypt selected region with Blowfish
  * Blowfish encrypt  
    Encrypt selected region with Blowfish
  * ChaCha20 decrypt / encrypt  
    Decrypt / encrypt selected region with ChaCha20
  * DES decrypt  
    Decrypt selected region with DES
  * DES encrypt  
    Encrypt selected region with DES
  * Salsa20 decrypt / encrypt  
    Decrypt / encrypt selected region with Salsa20
  * Triple DES decrypt  
    Decrypt selected region with Triple DES
  * Triple DES encrypt  
    Encrypt selected region with Triple DES

* Encoding operations
  * Binary data to hex text  
    Convert binary of selected region into hex text
  * Hex text to binary data  
    Convert hex text of selected region into binary
  * Binary data to decimal text  
    Convert binary of selected region into decimal text
  * Decimal text to binary data  
    Convert decimal text of selected region into binary data
  * Binary data to octal text  
    Convert binary of selected region into octal text
  * Octal text to binary data  
    Convert octal text of selected region into binary data
  * Binary data to binary text  
    Convert binary of selected region into binary text
  * Binary text to binary data  
    Convert binary text of selected region into binary data
  * Custom base64 decode  
    Decode selected region with custom base64 table
  * Custom base64 encode  
    Encode selected region with custom base64 table
  * ROT13  
    Rotate alphabet characters in selected region by the specified amount (default: 13)
  * From quoted printable  
    Decode selected region as quoted printable text
  * To quoted printable  
    Encode selected region into quoted printable text

* Misc operations
  * Byte frequency  
    Show byte frequency of selected region (the whole file if not selected)
  * File comparison  
    Compare contents of two files
  * Hash values  
    Calculate MD5, SHA1, SHA256 hash values of selected region (the whole file if not selected)
  * Send to  
    Send selected region (the whole file if not selected) to other programs

* Parsing operations
  * Binwalk scan  
    Scan selected region (the whole file if not selected) to find embedded files
  * File type  
    Identify file type of selected region (the whole file if not selected)
  * Find PE file  
    Find PE file from selected region (the whole file if not selected)
  * Strings  
    Extract text strings from selected region (the whole file if not selected)

* Search operations
  * Regex search  
    Search with regular expression in selected region (the whole file if not selected)
  * Replace  
    Replace matched data in selected region (the whole file if not selected) with specified data
  * XOR hex search  
    Search XORed / bit-rotated data in selected region (the whole file if not selected)
  * XOR text search  
    Search XORed / bit-rotated string in selected region (the whole file if not selected)
  * YARA scan  
    Scan selected region (the whole file if not selected) with YARA.

* XOR operations
  * Decremental XOR  
    XOR selected region while decrementing XOR key
  * Incremental XOR  
    XOR selected region while incrementing XOR key
  * Null-preserving XOR  
    XOR selected region while skipping null bytes and XOR key itself
  * XOR with next byte  
    XOR selected region while using next byte as XOR key
  * Guess 256 byte XOR keys  
    Guess 256 byte XOR keys from selected region (the whole file if not selected) based on the byte frequency
  * Visual encrypt  
    Encode selected region with visual encrypt algorithm that is used by Zeus trojan
  * Visual decrypt  
    Decode selected region with visual decrypt algorithm that is used by Zeus trojan

## Author
Nobutaka Mantani (Twitter: @nmantani)

## License
The BSD 2-Clause License (http://opensource.org/licenses/bsd-license.php)
