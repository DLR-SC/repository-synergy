<h1 align="center"> Shellab </h1> 
<h3 align="center"> Linux and Windows shellcode development/enrichment utility </h3> 
<p align="center">
  <a>
    <img alt="Shellab" title="Shellab" src="flask.png" width="380" height="450">
  </a>
</p>


## Table of Contents
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Features](#features)
- [TODO](#todo)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Contribution](#contribution)
- [License](#license)


## Introduction
Shellab is a tool that can be used to improve existing shellcodes and adapt them for personal needs. Developed to provide an alternative to msfvenom with new functionalities. Suitable for both Windows and Linux shellcode (32 and 64 bit). 

## Requirements
Shellab requires Radare2, you should install it running this command:
`$ sudo apt-get install radare2`

## Features

* Encode shellcode with custom encoder 
* Generate stagers and egghunters (including [sandwich](https://www.securitysift.com/eggsandwich-egghunter-integrity/) and [omelette](http://www.thegreycorner.com/2013/10/omlette-egghunter-shellcode.html) egghunter)
* Inject shellcode into PE files
* Run shellcode on Linux
* Remove bad characters and null-bytes
* Perform experimental size reduction (by instructions replacement)
* Export shellcode in different executable formats (C, C#, Python, Powershell, hex, raw etc.)
* Add custom instructions, NOP slides and specific system calls

## TODO
- [ ] Create more encoders
- [ ] Implement generation of fully alphanumeric shellcode
- [ ] Add shellcode comparison mechanism


## Usage
This example will encode the input shellcode with "rot_xor" encoder, insert "xor eax, eax" instruction and 100 non-canonical NOP instructions in front of it, generate a bind stager (that will listen for the incoming shellcode on port 4444) and prepend the shellcode with exit() syscall.

### Show help message:
<img src="screenshots/help_screenshot.png" width="600"/>

### List available components:

<img src="screenshots/list_screenshot.png" width="600"/>

### Generate the shellcode:

<img src="screenshots/example.png" width="600"/>




## Contribution
If you have an idea for a new encoder, egghunter or stager, or just want to improve this tool, simply create a pull request :)

## License
This software is under [MIT License](https://en.wikipedia.org/wiki/MIT_License)