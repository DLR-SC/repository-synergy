# malicious_file_maker
Malicious file maker/sender to create and send malicious attachments to test your email filter/alerting.

* Created to work on OS X using Keka to do most of the archiving functions. Easy enough to change for your distro.


# Creating the applescript app
Open the calc_applescript.scpt file with script editor and export as application, zip file should also contain a working version.

ref: http://apple.stackexchange.com/questions/8299/how-do-i-make-an-applescript-file-into-a-mac-app

![alt text](https://cloud.githubusercontent.com/assets/735360/18999317/fc31bea8-870a-11e6-9051-faed2f9a5393.png "Applesecript compile")


# Example run:
```
$ python python_filemaker.py

7-Zip [64] 9.20  Copyright (c) 1999-2010 Igor Pavlov  2010-11-18
p7zip Version 9.20 (locale=utf8,Utf16=on,HugeFiles=on,8 CPUs)
Scanning

Creating archive eicar_encrypt.zip

Compressing  eicar.com

Everything is Ok
..........
created: /Users/nyob/Documents//filemaker/2016-09-30T11:56:14.654053/eicardmg.dmg

7-Zip [64] 9.20  Copyright (c) 1999-2010 Igor Pavlov  2010-11-18
p7zip Version 9.20 (locale=utf8,Utf16=on,HugeFiles=on,8 CPUs)
Scanning

Creating archive eicar.7z

Compressing  eicar.com

Everything is Ok

7-Zip [64] 9.20  Copyright (c) 1999-2010 Igor Pavlov  2010-11-18
p7zip Version 9.20 (locale=utf8,Utf16=on,HugeFiles=on,8 CPUs)
Scanning

Creating archive eicar.tar

Compressing  eicar.com

Everything is Ok
a eicar.com
a eicar.com

7-Zip [64] 9.20  Copyright (c) 1999-2010 Igor Pavlov  2010-11-18
p7zip Version 9.20 (locale=utf8,Utf16=on,HugeFiles=on,8 CPUs)
Scanning

Creating archive eicar.gzip

Compressing  eicar.com

Everything is Ok

7-Zip [64] 9.20  Copyright (c) 1999-2010 Igor Pavlov  2010-11-18
p7zip Version 9.20 (locale=utf8,Utf16=on,HugeFiles=on,8 CPUs)
Scanning

Creating archive eicar.bzip

Compressing  eicar.com

Everything is Ok

7-Zip [64] 9.20  Copyright (c) 1999-2010 Igor Pavlov  2010-11-18
p7zip Version 9.20 (locale=utf8,Utf16=on,HugeFiles=on,8 CPUs)
Scanning

Creating archive eicar.xz

Compressing  eicar.com

Everything is Ok

7-Zip [64] 9.20  Copyright (c) 1999-2010 Igor Pavlov  2010-11-18
p7zip Version 9.20 (locale=utf8,Utf16=on,HugeFiles=on,8 CPUs)
Scanning

Creating archive calcjs_encrypt.zip

Compressing  calc.js

Everything is Ok

7-Zip [64] 9.20  Copyright (c) 1999-2010 Igor Pavlov  2010-11-18
p7zip Version 9.20 (locale=utf8,Utf16=on,HugeFiles=on,8 CPUs)
Scanning

Creating archive calcjs.7z

Compressing  calc.js

Everything is Ok

7-Zip [64] 9.20  Copyright (c) 1999-2010 Igor Pavlov  2010-11-18
p7zip Version 9.20 (locale=utf8,Utf16=on,HugeFiles=on,8 CPUs)
Scanning

Creating archive calcjs.tar

Compressing  calc.js

Everything is Ok
a calc.js
a calc.js

7-Zip [64] 9.20  Copyright (c) 1999-2010 Igor Pavlov  2010-11-18
p7zip Version 9.20 (locale=utf8,Utf16=on,HugeFiles=on,8 CPUs)
Scanning

Creating archive calcjs.gzip

Compressing  calc.js

Everything is Ok

7-Zip [64] 9.20  Copyright (c) 1999-2010 Igor Pavlov  2010-11-18
p7zip Version 9.20 (locale=utf8,Utf16=on,HugeFiles=on,8 CPUs)
Scanning

Creating archive calcjs.bzip

Compressing  calc.js

Everything is Ok

7-Zip [64] 9.20  Copyright (c) 1999-2010 Igor Pavlov  2010-11-18
p7zip Version 9.20 (locale=utf8,Utf16=on,HugeFiles=on,8 CPUs)
Scanning

Creating archive calcjs.xz

Compressing  calc.js

Everything is Ok

7-Zip [64] 9.20  Copyright (c) 1999-2010 Igor Pavlov  2010-11-18
p7zip Version 9.20 (locale=utf8,Utf16=on,HugeFiles=on,8 CPUs)
Scanning

Creating archive calc_hta.bzip

Compressing  calc_hta.hta

Everything is Ok

7-Zip [64] 9.20  Copyright (c) 1999-2010 Igor Pavlov  2010-11-18
p7zip Version 9.20 (locale=utf8,Utf16=on,HugeFiles=on,8 CPUs)
Scanning

Creating archive calc_lnk.bzip

Compressing  calc.lnk

Everything is Ok

7-Zip [64] 9.20  Copyright (c) 1999-2010 Igor Pavlov  2010-11-18
p7zip Version 9.20 (locale=utf8,Utf16=on,HugeFiles=on,8 CPUs)
Scanning

Creating archive calc_enc_jse.bzip

Compressing  calc_enc.jse

Everything is Ok

7-Zip [64] 9.20  Copyright (c) 1999-2010 Igor Pavlov  2010-11-18
p7zip Version 9.20 (locale=utf8,Utf16=on,HugeFiles=on,8 CPUs)
Scanning

Creating archive calc_enc_vbe.bzip

Compressing  calc_enc.vbe

Everything is Ok

7-Zip [64] 9.20  Copyright (c) 1999-2010 Igor Pavlov  2010-11-18
p7zip Version 9.20 (locale=utf8,Utf16=on,HugeFiles=on,8 CPUs)
Scanning

Creating archive calc_bat.bzip

Compressing  calc.bat

Everything is Ok

7-Zip [64] 9.20  Copyright (c) 1999-2010 Igor Pavlov  2010-11-18
p7zip Version 9.20 (locale=utf8,Utf16=on,HugeFiles=on,8 CPUs)
Scanning

Creating archive calc_cmd.bzip

Compressing  calc.cmd

Everything is Ok

7-Zip [64] 9.20  Copyright (c) 1999-2010 Igor Pavlov  2010-11-18
p7zip Version 9.20 (locale=utf8,Utf16=on,HugeFiles=on,8 CPUs)
Scanning

Creating archive calc_vbs.bzip

Compressing  calc.vbs

Everything is Ok

7-Zip [64] 9.20  Copyright (c) 1999-2010 Igor Pavlov  2010-11-18
p7zip Version 9.20 (locale=utf8,Utf16=on,HugeFiles=on,8 CPUs)
Scanning

Creating archive calc_wsf.bzip

Compressing  calc.wsf

Everything is Ok

7-Zip [64] 9.20  Copyright (c) 1999-2010 Igor Pavlov  2010-11-18
p7zip Version 9.20 (locale=utf8,Utf16=on,HugeFiles=on,8 CPUs)
Scanning

Creating archive calcvbs_encrypt.zip

Compressing  calc.vbs

Everything is Ok

7-Zip [64] 9.20  Copyright (c) 1999-2010 Igor Pavlov  2010-11-18
p7zip Version 9.20 (locale=utf8,Utf16=on,HugeFiles=on,8 CPUs)
Scanning

Creating archive calcvbs.7z

Compressing  calc.vbs

Everything is Ok

7-Zip [64] 9.20  Copyright (c) 1999-2010 Igor Pavlov  2010-11-18
p7zip Version 9.20 (locale=utf8,Utf16=on,HugeFiles=on,8 CPUs)
Scanning

Creating archive calcvbs.tar

Compressing  calc.vbs

Everything is Ok
a calc.vbs
a calc.vbs

7-Zip [64] 9.20  Copyright (c) 1999-2010 Igor Pavlov  2010-11-18
p7zip Version 9.20 (locale=utf8,Utf16=on,HugeFiles=on,8 CPUs)
Scanning

Creating archive calcvbs.gzip

Compressing  calc.vbs

Everything is Ok

7-Zip [64] 9.20  Copyright (c) 1999-2010 Igor Pavlov  2010-11-18
p7zip Version 9.20 (locale=utf8,Utf16=on,HugeFiles=on,8 CPUs)
Scanning

Creating archive calcvbs.xz

Compressing  calc.vbs

Everything is Ok
sending:asciiart.command
sending:calc.bat
sending:calc.cmd
sending:calc.exe
sending:calc.js
sending:calc.lnk
sending:calc.ps1
sending:calc.vbs
sending:calc.wsf
sending:calc_applescript.zip
sending:calc_bat.bzip
sending:calc_bat.zip
sending:calc_cmd.bzip
sending:calc_cmd.zip
sending:calc_enc.jse
sending:calc_enc.vbe
sending:calc_enc_jse.bzip
sending:calc_enc_jse.zip
sending:calc_enc_vbe.bzip
sending:calc_enc_vbe.zip
sending:calc_hta.bzip
sending:calc_hta.hta
sending:calc_hta.zip
sending:calc_lnk.bzip
sending:calc_lnk.zip
sending:calc_vbs.bzip
sending:calc_vbs.zip
sending:calc_wsf.bzip
sending:calc_wsf.zip
sending:calcjs.7z
sending:calcjs.bzip
sending:calcjs.gzip
sending:calcjs.tar
sending:calcjs.tar.bz2
sending:calcjs.tar.gz
sending:calcjs.xz
sending:calcjs.zip
sending:calcjs_encrypt.zip
sending:calcvbs.7z
sending:calcvbs.gzip
sending:calcvbs.tar
sending:calcvbs.tar.bz2
sending:calcvbs.tar.gz
sending:calcvbs.xz
sending:calcvbs_encrypt.zip
sending:eicar.7z
sending:eicar.bzip
sending:eicar.com
sending:eicar.gzip
sending:eicar.tar
sending:eicar.tar.bz2
sending:eicar.tar.gz
sending:eicar.xz
sending:eicar.zip
sending:eicar_encrypt.zip
sending:eicardmg.dmg
sending:SimpleJavaCalculator.jar
```

Inbox:
![alt text](https://cloud.githubusercontent.com/assets/735360/18999303/e1386048-870a-11e6-9b41-a8730311939e.png "inbox")

