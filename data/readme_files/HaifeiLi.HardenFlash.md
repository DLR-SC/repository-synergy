#HardenFlash - Patching Flash binary to stop Flash exploits and zero-days

Introduction
============
You probably know how bad it is for Flash security. Five years ago we often heard of Flash-based zero-day attacks, 5 years later we are still facing the same situation (or even worse since we are in the "APT" era now). In Feb 2013, the author revealed the a.k.a. ["Vector Spray" exploitation technique](https://sites.google.com/site/zerodayresearch/smashing_the_heap_with_vector_Li.pdf), which was later used again and again in almost every single Flash or IE zero-day attack. Unfortunately, Adobe - as the vendor - hasn't took any action yet to harden the weakness in their custom heap management, the weakness is so obvious and has been abused for more than 2 years.

The HardenFlash was developed from the thought that we must do something to protect Flash users around the world, specially for IE users because IE doesn't have a strong Sandbox. We hook (through PE patching) the Flash binary at certain functions/addresses so we know when the SWF is doing something malicious.

Currently, it's focused only on detecting the previously-mentioned Vector Spray, which is a "must" for all the Flash exploits as I have seen.


Why we need tools like HardenFlash?
==================================
Some readers may argue that there are already some endpoint exploitation protection tools/products out there, regardless of they are free or commercial. Typical example is the Microsoft's [EMET](https://support.microsoft.com/en-us/kb/2458544). However, such an EMET-like tool is usually protecting at the generic exploitation or shellcode level. The Vector Spray technique enables the attacker to read and write at any bytes in the memory space of the process, with such an "ultimate" ability, the attacker is able to defeat any EMET-like protection easily. In fact, at [this year's PWN2OWN competition](http://h30499.www3.hp.com/t5/HP-Security-Research-Blog/A-look-back-at-Pwn2Own-2015/ba-p/6724115), researchers have already demonstrated this - with successfully bypassing EMET couple times. All these suggest that a hardening or detecting approach from the "Flash level" is critical to protect users from Flash-based attacks.


How to Deploy
=============
Currently, I've only released the patched binary for the following Flash Player binary.

**Flash Player 17.0.0.169 for Internet Explorer running on Windows 7 (32bit)**<br>
(it's the latest Flash Player version as of April 30, 2015)

It works on both the 32bit and 64bit version of Windows 7, because on the default configuration of Windows 7 64bit the IE just uses the 32bit Flash Player to render Flash contents. For Windows 8+, because Flash is part of the OS, I've not figured out how to block the Flash auto-update from Windows Update but not block any other security updates. For older OS like Windows XP, the patched binary may work also but I didn't do any test - one reason is that there are many other ways to compromise your system if you are still using XP, which make the HardenFlash not quite necessary.

The patched binary sits in the "patched_binary" directory, the SHA256 hash is as following, use it to identify it's a good (not malicious!) version from me.
**158D5AE45A0A2FC8FF49713645B910192440244DDE7ADBBA905AD6F9D2EACCC0**

So, if you are a professional, you may just download the binary and use it to replace the official one from Adobe. If you are not a professional, I've wrote a Python script (HardenFlash-deploy.py) to do that automatically.

Note you need to run this script with "administrator" privilege on Windows. And, you need to have the Flash Player for IE installed on your system first.

There are up to 2 yes-or-no options you need to decide.

1. You will always to be asked to choose to disable the Flash Player's auto-update feature or not, this is because that the patched binary will be replaced if you install any future Flash Player. If you choose not to disable the auto-update feature, at a future time point, you may find that you are actually not running the HardenFlash because it's replaced by a new Flash binary from Adobe.

	Of course, disabling the auto-update will block you from accepting any update from Adobe, which may fix security vulnerabilities. There is no way for the author to keep updating the patched binary as this is a "free-time" project only and Adobe often updates Flash Player. So, talking about the balance, in the author's opinion, since the HardenFlash blocks at the exploitation level, it's "okay" to continue to use the "outdated" HardenFlash if it's not "so-outdated" because even if the attacker uses a known vulnerability he/she will fail at the exploitation step, as long as there is no significant bypass disclosed for HardenFlash. On the other hand, protecting against Flash threats through fixing vulnerabilities has been proven to be a failed strategy as we have seen so many Flash zero-days in these years. After all, this is just the author's personal opinion, final decision will be left to the user.

2. If the script finds that the HardenFlash version is not exactly the same as in the official Flash Player you installed from Adobe, you will be gave a chance to decide. The author's suggestion is that if the Adobe version is older than the HardenFlash, you should install the HardenFlash. Otherwise, it's the same situation as we discussed in above, if you continue, you will be installed an "outdated" but "hardened" Flash, you need to decide for your best interests.


Here is a sample usage of the "HardenFlash-deploy.py"
    
    [*] This Flash Player binary on your OS will be replaced: C:\Windows\system32\Macromed\Flash\Flash32_17_0_0_169.ocx
    [*] HardenFlash binary (158D5AE45A0A2FC8FF49713645B910192440244DDE7ADBBA905AD6F9D2EACCC0) will be downloaded from: https://g
    ithub.com/HaifeiLi/HardenFlash/raw/master/patched_binary/Flash32_17_0_0_169.ocx
    [*] We suggest to disable Flash Player's auto-update feature since in future installing a new Flash Player will uninstall Ha
    rdenFlash.
    [*] However, we'd like to ask you to decide: 'y' to disable Flash auto-update, 'n' to keep [y/n]
    y
    [*] Downloading patched binary from https://github.com/HaifeiLi/HardenFlash/raw/master/patched_binary/Flash32_17_0_0_169.ocx
    
       16955056  [100.00%]
    
    [*] Checking the downloaded binary is legal
    [*] The binary is ready to deploy
    [*] Removing deny-write security permission
    processed file: C:\Windows\system32\Macromed\Flash\Flash32_17_0_0_169.ocx
    Successfully processed 1 files; Failed processing 0 files
    [*] Replacing C:\Windows\system32\Macromed\Flash\Flash32_17_0_0_169.ocx with C:\HardenFlash\Flash32_17_0_0_169.
    ocx
    [*] All done!
    [*] In future, installing the official Flash Player from Adobe (https://get.adobe.com/flashplayer) will uninstall the Harden
    Flash automatically


When it Works
=============
After the installation, you are free to use IE as normal and it's expected to not bring any impact for normal uses. However, when the patched Flash binary detects a potential Flash exploit or zero-day attack, you will be give a warning dialog like the following:<br>
![](https://github.com/HaifeiLi/HardenFlash/blob/master/image/HardenFlash.png)

Then, after the user confirms the message, the process will be terminated and the malicious exploit will be stopped.

How to Uninstall
================
You can always uninstall the HardenFlash any time. To uninstall it, you just need to install the Flash Player from Adobe, this will replace the HardenFlash binary automatically. You may go https://get.adobe.com/flashplayer.


How It Works
============
The idea is simple in fact. In short, it tries to hook the function that instantiates a Vector object (constructor), and then we count how many Vector objects have been instantiated in a short time period. If, the total number is bigger than the threshold value we set, we say this is a Vector Spray, since usually a normal SWF doesn't need to instantiate a lot of Vector objects in short time.

This is the function that instantiates a Vector object, at the L64 from https://github.com/adobe-flash/avmplus/blob/master/core/VectorClass-impl.h.

    template<class OBJ>
    OBJ* TypedVectorClass<OBJ>::newVector(uint32_t length, bool fixed)
    {
        OBJ* v = (OBJ*)OBJ::create(gc(), ivtable(), prototypePtr());
        v->m_vecClass = this;
        if (length > 0)
            v->set_length(length);
        v->m_fixed = fixed;
        return v;
    }

In the released binary, the above function is compiled into 4 different addresses, since Flash implements 4 types of Vector objects, they are `Vector.<int>`, `Vector.<uint>`, `Vector.<Number>` and `Vector.<Object>`.



What've been Modified
=====================
1. A new PE section named ".hard" is added.

2. The entry point of the Flash binary is hooked, and jumped to our added code in ".hard" section to prepare addresses of some APIs for later use.

3. As discussed in previous section, 4 functions are hooked, and they will be all led to the following code in our added PE section.

>
.hard:11123600 call$+5<br>
.hard:11123605 pop edx<br>
.hard:11123606 and edx, 0FFFFF000h<br>
.hard:1112360C sub edx, 0E7000h<br>
.hard:11123612 sub edx, 40h<br>
.hard:11123615 push edx<br>
.hard:11123616 nop <br>
.hard:11123617 mov eax, edx<br>
.hard:11123619 add eax, 24h<br>
.hard:1112361C call dword ptr [eax] ; GetTickCount<br>
.hard:1112361E pop edx<br>
.hard:1112361F mov ebx, eax<br>
.hard:11123621 sub ebx, [edx]<br>
.hard:11123623 cmp ebx, 0EA60h ; if the current time is not less than 1min to the previous one,<br> calculation starts over.<br>
.hard:11123629 jb  short loc_11123640<br>
.hard:1112362B nop <br>
.hard:1112362C mov [edx], eax<br>
.hard:1112362E add edx, 4<br>
.hard:11123631 mov dword ptr [edx], 0<br>
.hard:11123637 jmp loc_11123500; safely exit<br>
.hard:11123637 ; <br>---------------------------------------------------------------------------<br>
.hard:1112363C align 10h<br>
.hard:11123640<br>
.hard:11123640 loc_11123640:   ; CODE XREF: .hard:11123629<br>
.hard:11123640 mov [edx], eax<br>
.hard:11123642 add edx, 4<br>
.hard:11123645 mov ebx, [edx]<br>
.hard:11123647 inc ebx<br>
.hard:11123648 cmp ebx, 0FEh   ; allowing ~255 instantiations of Vector<br>
.hard:1112364E jnb short loc_11123660 ; give user a warning, then exit the process<br>
.hard:11123650 nop<br>
.hard:11123651 mov [edx], ebx<br>
.hard:11123653 jmp loc_11123500; safely exit<br>
.hard:11123653 ; <br>---------------------------------------------------------------------------<br>
.hard:11123658 align 10h<br>
.hard:11123660<br>
.hard:11123660 loc_11123660:   ; CODE XREF: .hard:1112364E<br>
.hard:11123660 call $+5 ; give user a warning, then exit the process<br>
.hard:11123665 pop ebx<br>
.hard:11123666 push edx<br>
.hard:11123667 and ebx, 0FFFFF000h<br>
.hard:1112366D push 10h<br>
.hard:1112366F mov eax, ebx<br>
.hard:11123671 add eax, 0B0h<br>
.hard:11123676 push eax<br>
.hard:11123677 push ebx<br>
.hard:11123678 push 0<br>
.hard:1112367A call dword ptr [edx+1Ch] ; MessageBoxA<br>
.hard:1112367D pop edx<br>
.hard:1112367E push 0FFFFFFFFh<br>
.hard:11123680 call dword ptr [edx+24h] ; ExitProcess<br>



Effectiveness
=============
As of June 22, 2015, HardenFlash receieves a %100 success detection rate since its release on April 30, 2015 - a strong proof of its effectiveness. Specifically, it stops the following Flash exploits seen in the wild.

1. CVE-2015-0336
2. CVE-2015-3090
3. CVE-2015-3105
4. CVE-2015-3104

sample credit: [@kafeine](http://malware.dontneedcoffee.com).					



Known Issues
============
@binjo has reported that the gaming website (http://s6.hxjy.iwan4399.com/game.php) will cause False Positive. Currently there are no known False Negatives.


Feedback and Contribute!
========================
Any feedback/suggestion/discussion/etc are always very welcome. Please reach to haifei.van ## hotmail or @HaifeiLi on Twitter.


License
=======
HardenFlash is released under the GNU General Public License V2 (https://github.com/HaifeiLi/HardenFlash/blob/master/LICENSE.md), WITHOUT ANY WARRANTY - USE IT AT YOUR OWN RISK. All rights reserved.

This project is released as free, open-source and you are free to integrate it into your tool/product as long as your tool/product is free or open-source for good purpose (with acknowledging the project and the author). For commercial use, you need to contact the author first.






