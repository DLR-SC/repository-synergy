EliteOCR
==============
EliteOCR is a Python script that runs optical character recognition on screenshots
from Elite: Dangerous commodities market. 

Prerequisites
--------------
EliteOCR is capable of reading the entries in Elite: Dangerous markets screenshots.
Best results are achieved with screenshots of 3840 by 2160 pixel (4K) or more.
You can make screenshots in game by pressing F10. You find them usually in
C:\Users\USERNAME\Pictures\Frontier Developments\Elite Dangerous
Screenshots made with ALT+F10 are ignored due to memory errors!


Usage
--------------
Run EliteOCR.exe
Click "+" and select your screenshots. Select multiple files by holding CTRL or add them one by one.
Select one file and click the OCR button. Check if the values have been recognised properly.
Optionally correct them or choose alternative from the drop down list. Click on "Add and Next"
to continue to next line. You can edit the values in the table by double clicking on the entry.

After processing one screenshot you can choose the next file in the list and click the ORC Button
again. Should there be a corrupted entry, you can click "Skip" to continue to next line without adding
current one to the list. Duplicate entries are by default filtered out. To change this behaviour
go to Settings.

When finished click on "Export" to save your results to a csv-file(separated by ; ). CSV can be
opened by most spreadsheet editors like Excel, LibreOffice Calc etc. or alternatively text editors.


Building/running from source
--------------

[Windows](WINDOWS.md)

[Mac](MAC.md)

[Linux](LINUX.md)
