```
                        __                             __ __   
.----.-----.---.-.-----|  |_.-----.----.--------.-----|  |  |_ 
|  __|  _  |  _  |__ --|   _|  -__|   _|        |  -__|  |   _|
|____|_____|___._|_____|____|_____|__| |__|__|__|_____|__|____|
--A fun way to break your Blu-Ray burner-----------------------
```

The **coastermelt** project is an effort to make open source firmware for creatively repurposing BD-R drives.

Follow the video channel:  https://vimeo.com/channels/coastermelt

The new firmware is still not real yet, this project is still in the early stages of reverse engineering.


What it has
-----------

For the Samsung SE-506CB external Blu-Ray burner, it provides a way to install 'backdoored' firmware to support a set of programmatic and interactive reverse engineering tools.

Mac OS X only for now. Requires an ARM cross compiler (arm-none-eabi-gcc and friends) as well as a local compiler (XCode).

NOTE that there are NO copyrighted firmware images included here in this open source project! To be on the safe side, we don't include large disassemblies or reverse engineering databases either. The installation process requires patching a specific version of firmware, which we download from the official firmware update site during the build process.

The documentation here is an original effort created without access to any data sheets or official documentation for the MT1939 chip. I started with a marketing blurb about the chip, the "ARM" logo lasered on top, and some firmware updates. Everything else here is based on extensive guesswork and experimentation. If anything sounds authoritative, that is completely by accident. I have no idea what I'm doing here.


Parts
-----

* doc - Reverse engineering notes, sketchy DIY hardware doumentation
* flasher - Command line tool to flash firmware
    - The official tool is annoying and the Mac version is broken. So this.
    - Also it has some weird debug features, naturally
    - And there's a Python tool to patch the firmware checksum and bypass its cryptographic signatures.
* backdoor - Debugging tools based on binary patching official firmware
    - The assembly code in patch.s gets planted in a SCSI callback
    - A bunch of weird Python stuff uses that as a debug stub


Getting Started
---------------

* Get XCode, right?
* Also this compiler. Put it in your path or something: [arm-none-eabi-gcc](https://launchpad.net/gcc-arm-embedded/+download)
* Yet another weird compiler. With [homebrew](http://brew.sh), do `brew install sdcc`
* You probably want to have [IPython](http://ipython.org/install.html) too. It's great, and the cool debug shell needs it.
* You usually want to have **no disc** in the drive or have the tray ejected when you start working with it. Otherwise, the OS can keep us from claiming the device.
* Run **make** in the `backdoor` directory to build the patched firmware and the Python extensions
* If you're paranoid like me, **make disassemble** will show you the damage
* If you're ready to toast your drive, run **make flash**

If the update worked, you'll see my backdoor signature show up when you run mtflash. This is how you can tell your drive has the patch! Otherwise it should mostly work, though of course it's totally untrustworthy at this point. I mean, we just turned off all the bootloader integrity checks.

```
cylindroid:flasher micah$ ./mtflash 
Inquiry:
       0: 05 80 00 32 1f 00 00 00 54 53 53 54 63 6f 72 70  ...2....TSSTcorp
      10: 42 44 44 56 44 57 20 53 45 2d 35 30 36 43 42 20  BDDVDW SE-506CB 
      20: 54 53 30 31 20 20 30 35 32 38 20 20 20 20 20 20  TS01  0528      
      30: 20 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ...............
      40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
      50: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
Firmware version:
       0: 00 06 01 01 54 53 20 00                          ....TS .
Backdoor signature:
       0: 7e 4d 65 53 60 31 34 20 76 2e 30 33              ~MeS`14 v.03
```

But hooray! Now if you have IPython, you can start the interactive shell. For more about what you can do with it, take a look at the [shell recipe book](https://github.com/scanlime/coastermelt/blob/master/doc/cmshell-recipes.txt).

```
cylindroid:backdoor micah$ ./cmshell.py 

                        __                             __ __   
.----.-----.---.-.-----|  |_.-----.----.--------.-----|  |  |_ 
|  __|  _  |  _  |__ --|   _|  -__|   _|        |  -__|  |   _|
|____|_____|___._|_____|____|_____|__| |__|__|__|_____|__|____|
--IPython Shell for Interactive Exploration--------------------

Read, write, or fill ARM memory. Numbers are hex. Trailing _ is
short for 0000, leading _ adds 'pad' scratchpad RAM offset.
Internal _ are ignored so you can use them as separators.

    rd 1ff_ 100
    wr _ 1febb
    ALSO: rdw, orr, bic, fill, watch, find
          peek, poke, read_block

Disassemble, assemble, and invoke ARM assembly:

    dis 3100
    asm _4 mov r3, #0x14
    dis _4 10
    ea mrs r0, cpsr; ldr r1, =0xaa000000; orr r0, r1
    ALSO: tea, blx, assemble, disassemble, evalasm

Or compile and invoke C++ code with console output:

    ec 0x42
    ec ((uint16_t*)pad)[40]++
    ecc println("Hello World!")
    ALSO: console, compile, evalc

Live code patching and tracing:

    hook -Rrcm "Eject button" 18eb4
    ALSO: ovl, wrf, asmf

You can use integer globals in C++ and ASM snippets,
or define/replace a named C++ function:

    fc uint32_t* words = (uint32_t*) buffer
    buffer = pad + 0x100
    ec words[0] += 0x50
    asm _ ldr r0, =buffer; bx lr

You can script the device's SCSI interface too:

    sc c ac              # Backdoor signature
    sc 8 ff 00 ff        # Undocumented firmware version
    ALSO: reset, eject, sc_sense, sc_read, scsi_in, scsi_out

Happy hacking!    -- Type 'thing?' for help on 'thing' or
~MeS`14              '?' for IPython, '%h' for this again.

In [1]: 
```
