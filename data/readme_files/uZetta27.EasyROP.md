# EasyROP
This Python tool allows you to search gadgets, operations formed by gadgets and generate automatic ROP chains in Portable Executable (PE). EasyROP is based in Capstone Disassembly Framework to search gadgets.

### Install
EasyROP needs [Python3](https://www.python.org/downloads/), [Capstone](http://www.capstone-engine.org/download.html) and [pefile](https://pypi.python.org/pypi/pefile/) installation.

Once you solve these dependencies, EasyROP can be used as:
```
$> python EasyROP.py
```

### Use
```
usage: EasyROP.py [-h] [-v] [--binary <path> [<path> ...]] [--depth <bytes>]
                  [--all] [--nojop] [--noretf] [--op <op>] [--reg-dst <reg>]
                  [--reg-src <reg>] [--ropchain <file>]

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         display EasyROP's version
  --binary <path> [<path> ...]
                        specify a list of binary paths to analyze
  --depth <bytes>       depth for search engine (default 5 bytes)
  --all                 disables the removal of duplicate gadgets
  --nojop               disables JOP gadgets
  --noretf              disables gadgets terminated in a far return (retf)
  --op <op>             search for operation
  --reg-dst <reg>       specify a destination reg to operation
  --reg-src <reg>       specify a source reg to operation
  --ropchain <file>     plain text file with rop chains
```

### Operations
This operations are high level operations built by gadgets. The following is an example to move a value from one register to another:
```
xchg dst, src
```
```
xor dst, dst
add dst, src
```

### Specification of operations
Following the next DTD you can specify your own operations through a XML file:
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE operations [
        <!ELEMENT operations (operation)+>
        <!ELEMENT operation (set)+>
        <!ATTLIST operation
                name CDATA #REQUIRED>
        <!ELEMENT set (ins)+>
        <!ELEMENT ins (reg1|reg2)*>
        <!ATTLIST ins
                mnemonic CDATA #REQUIRED>
        <!ELEMENT reg1 (#PCDATA)>
        <!ATTLIST reg1
                value CDATA #IMPLIED>
        <!ELEMENT reg2 (#PCDATA)>
        <!ATTLIST reg2
                value CDATA #IMPLIED>
        ]>
<operations>
    <operation name="move">
        <set>
            <ins mnemonic="xor">
                <reg1>dst</reg1>
                <reg2>dst</reg2>
            </ins>
            <ins mnemonic="add">
                <reg1>dst</reg1>
                <reg2>src</reg2>
            </ins>
        </set>
    </operation>
</operations>
```

This XML structure allows you to define register value of each instruction:

* dst: destination register
* src: source register
* aux: auxiliary register (only one by set)
* [dst]: destination direction allocated in a register
* [src]: source direction allocated in a register
* {eax, ebx, ecx...}: specific register
* {[eax, ebx, ecx...]}: direction allocated in a specific register
* &lt;reg{1,2} value ="0xFFFFFFFF">: mandatory value of register

### Automatic ROP chains generation
Through the --ropchain &lt;path> option you can specify in a plaintex file a ROP attack composed by operations defined in the XML. An example:
```
lc(reg1)
lc(reg2)
sub(reg2, reg1)
clear(reg3)
move(reg3, reg2)
```

Which results in the following output (summarized for the sake of readability):
```
$> python EasyROP.py --binary C:\Windows\system32\kernel32.dll --ropchain rop.txt --nojop --noretf
[+] Analyzing kernel32.dll

lc(reg1)
	[kernel32.dll @ 0x77e1f35d]: pop ebp ; adc bh, dh ; ret 
	[kernel32.dll @ 0x77e000ad]: pop ebp ; ret 
	[kernel32.dll @ 0x77e4a3ed]: pop ecx ; pop ebp ; pop ecx ; pop ebx ; ret 4 
	[kernel32.dll @ 0x77e4a3ef]: pop ecx ; pop ebx ; ret 4 
	[kernel32.dll @ 0x77e2922d]: pop edi ; pop esi ; ret 
	[kernel32.dll @ 0x77e5238b]: pop edi ; ret 
	[kernel32.dll @ 0x77e85f37]: pop edx ; pop eax ; ret 
	[kernel32.dll @ 0x77e976d4]: pop edx ; ret 0xb 
	[kernel32.dll @ 0x77e123a0]: pop esi ; leave ; ret 
	[kernel32.dll @ 0x77e77f01]: pop esi ; ret 4 
	[kernel32.dll @ 0x77e2683c]: pop esp ; add byte ptr [eax], al ; leave ; ret 4 
	[kernel32.dll @ 0x77e735e0]: pop esp ; ret 0xfffb 
lc(reg2)
	[kernel32.dll @ 0x77e6f379]: pop eax ; leave ; ret 
	[kernel32.dll @ 0x77e78a2d]: pop eax ; ret 
	[kernel32.dll @ 0x77e2e386]: pop ebx ; ret 
	[kernel32.dll @ 0x77e4a3f0]: pop ebx ; ret 4 
	[kernel32.dll @ 0x77e93018]: pop ecx ; leave ; ret 4 
	[kernel32.dll @ 0x77e4a3ed]: pop ecx ; pop ebp ; pop ecx ; pop ebx ; ret 4 
	[kernel32.dll @ 0x77e2ef97]: pop edi ; leave ; ret 
	[kernel32.dll @ 0x77e5238b]: pop edi ; ret 
	[kernel32.dll @ 0x77e2683c]: pop esp ; add byte ptr [eax], al ; leave ; ret 4 
	[kernel32.dll @ 0x77e735e0]: pop esp ; ret 0xfffb 
sub(reg2, reg1)
	[kernel32.dll @ 0x77e1d2b1]: sub eax, ecx ; pop ebx ; pop ebp ; ret 8 
	[kernel32.dll @ 0x77e3ec10]: sub eax, esi ; pop esi ; pop ebp ; ret 8 
	[kernel32.dll @ 0x77e1f2ce]: sub ebx, edx ; add byte ptr [eax], al ; ret 4 
	[kernel32.dll @ 0x77e928ed]: sub ecx, ebp ; ja 0x77e928d9 ; ret 
	[kernel32.dll @ 0x77e306a1]: sub ecx, edx ; mov dword ptr [edi], ecx ; ret 
	[kernel32.dll @ 0x77e1fece]: sub ecx, esi ; add byte ptr [eax], al ; ret 8 
	[kernel32.dll @ 0x77e699d2]: sub edi, esp ; dec ecx ; ret 0x14 
	[kernel32.dll @ 0x77e69b50]: sub esp, edi ; dec ecx ; ret 0x14 
clear(reg3)
	[kernel32.dll @ 0x77e0b823]: xor eax, eax ; ret 
	[kernel32.dll @ 0x77e02ce5]: xor eax, eax ; ret 4 
move(reg3, reg2)
	[kernel32.dll @ 0x77e79dcd]: and eax, ecx ; pop ebp ; ret 0xc  (eax = 0xFFFFFFFF)
	[kernel32.dll @ 0x77e3e168]: and eax, ecx ; pop ebp ; ret 4  (eax = 0xFFFFFFFF)
	[kernel32.dll @ 0x77e2243b]: mov eax, eax ; ret 
	[kernel32.dll @ 0x77e913ae]: mov eax, ebx ; pop ebx ; leave ; ret 0x10 
	[kernel32.dll @ 0x77e94bf8]: mov eax, ecx ; leave ; ret 0x18 
	[kernel32.dll @ 0x77e2a43f]: mov eax, ecx ; pop ebp ; ret 8 
	[kernel32.dll @ 0x77e3e138]: mov eax, edi ; pop edi ; leave ; ret 0xc 
	[kernel32.dll @ 0x77e3da51]: mov eax, edi ; pop edi ; leave ; ret 8 
	[kernel32.dll @ 0x77e8772e]: push edi ; pop eax ; pop ebp ; ret 4 
	[kernel32.dll @ 0x77e90c9a]: push edi ; pop eax ; pop esi ; leave ; ret 8 
	[kernel32.dll @ 0x77e63143]: xchg eax, ebx ; cld ; dec ecx ; ret 4 
	[kernel32.dll @ 0x77e631c7]: xchg eax, ebx ; sti ; dec ecx ; ret 4 
	[kernel32.dll @ 0x77e34c56]: xchg eax, edi ; add al, byte ptr [eax] ; leave ; ret 
	[kernel32.dll @ 0x77e212c2]: xchg eax, esp ; ret 

Time elapsed: 0:00:05.522
 ```

### License
This tool is published under the GNU GPLv3 license.

### Thanks
Special thanks to [ricardojrdez](https://github.com/ricardojrdez) for directing this project.