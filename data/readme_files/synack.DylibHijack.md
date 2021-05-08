# DylibHijack
python utilities related to dylib hijacking on OS X (presented at CanSecW 2015)

1) createHijacker.py
given a generic hijacker dylib and a target dlyib, configure the hijack dylib so that it's a *compatible* hijacker

2) scan.py
scans the list of running processes or the entire file-system for applications that either
