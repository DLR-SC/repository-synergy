Utilities
=========

Uncategorized utilities that do not need their own repository.

Simple Jack Symbol Porting tool
-------------------------------

Small dumb utility to port obvious function matches across two IDA databases.

Instruction frequency counter (arm_frequency.py)
----------------------------------------------------

The script 'arm_frequency.py' takes as input the output of objdump
on an ARM binary.
It will show the ammount of times every instruction was used, sorted
by the most used ones.

XRef printer (func_references.py)
---------------------------------

Small utility to print all the function calls to a given function.
This is generally used to look for calls to malloc like function.

DumpFunctionBytes.py
--------------------

IDA Python script that dumps the current function (you need to position
the cursor on the start of the function) as a shellcode.
It does a very limited analysis of the function in order to let you know
that you need to fix call sites to functions.

The main idea of this is being able to extract a function from a binary
and use it.

**Usage:**

Open IDA Pro and set the cursor to the begining of the function you want to dump.
Run the script, it will print the C++ code to stdout, so copy it and paste it on
a C++ file.

Now that you have the output on a file look for `TODO` makers and place the needed
manual information.

**Example output:**

```c++
#include <string>
#include <iostream>
#include <sys/mman.h>

using namespace std;

string build_blob();

void *alloc_rwx(size_t size) {
    void *mem = mmap(0, size, PROT_READ | PROT_WRITE | PROT_EXEC, MAP_ANON | MAP_PRIVATE, 0, 0);
    if (!mem) {
        cout << "Could not alloc RWX memory." << endl;
        return nullptr;
    }

    cout << "Allocated RwX memory at: " << mem << endl;
    return mem;
}

int main(int argc, char **argv) {
    string blob = build_blob();
    void *mem = alloc_rwx(blob.size());
    memcpy(mem, &blob[0], blob.size());

    // TODO: Change the signature of the function pointer.
    ((int (*)(void)) mem)();
}

string build_blob() {
    string dispatch_table;
    // TODO: Replace function_46_address with the correct implementation.
    uintptr_t function_46_address = reinterpret_cast<uintptr_t>(&printf);
    dispatch_table.append("\x48\xb8", 2);                        // 0x0000002e: movabs   rax, function_46_address
    dispatch_table.append(reinterpret_cast<const char *>(&function_46_address), sizeof(function_46_address));
    dispatch_table.append("\xff\xe0", 2);                        // 0x00000038: jmp      rax

    // Dumped [0x100000f30-0x100000f5e]
    string shellcode;
    shellcode.append("\x55", 1);                                 // 0x00000000: push     rbp
    shellcode.append("\x48\x89\xe5", 3);                         // 0x00000001: mov      rbp, rsp
    shellcode.append("\x48\x83\xec\x10", 4);                     // 0x00000004: sub      rsp, 0x10
    shellcode.append("\x48\x8d\x3d\x6b\x00\x00\x00", 7);         // 0x00000008: lea      rdi, qword ptr [rip + 0x6b]
    shellcode.append("\xc7\x45\xfc\x00\x00\x00\x00", 7);         // 0x0000000f: mov      dword ptr [rbp - 4], 0
    shellcode.append("\xb0\x00", 2);                             // 0x00000016: mov      al, 0
    shellcode.append("\xe8\x11\x00\x00\x00", 5);                 // 0x00000018: call     0x2e
    shellcode.append("\x8b\x4d\xfc", 3);                         // 0x0000001d: mov      ecx, dword ptr [rbp - 4]
    shellcode.append("\x83\xc1\x64", 3);                         // 0x00000020: add      ecx, 0x64
    shellcode.append("\x89\x45\xf8", 3);                         // 0x00000023: mov      dword ptr [rbp - 8], eax
    shellcode.append("\x89\xc8", 2);                             // 0x00000026: mov      eax, ecx
    shellcode.append("\x48\x83\xc4\x10", 4);                     // 0x00000028: add      rsp, 0x10
    shellcode.append("\x5d", 1);                                 // 0x0000002c: pop      rbp
    shellcode.append("\xc3", 1);                                 // 0x0000002d: ret

    return shellcode + dispatch_table;
}
```
