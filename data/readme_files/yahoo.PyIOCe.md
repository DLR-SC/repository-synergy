Python IOC Editor v0.9.8


Description: 
PyIOCe is an OpenIOC editor built using Python 2.7 and wxPython 3.0.0.0.  

There are many systems for storing complete threat intelligence, but OpenIOC excels at manipulating that data into a reduced and 
operationalized search method.  This can be used to build IOCs that describe broad threat behavior such as persistence mechanisms 
or important forensic sources or it can be used to search for more narrowly identified threats during incident response to rapidly 
scope a compromise across large enterprise networks. 

This project is meant to expand ongoing efforts to broaden the use of OpenIOC with other systems such as Snort, GRR, Splunk, and Yara

Standalone binaries are available under /dist

Required Python Modules:
wxPython
lxml

Features:
- Almost entirely keyboard driven
- Support for opening and editing OpenIOC 1.0 and 1.1 IOCs simultaneously (OpenIOC 1.0 support is MIR only using legacy MIR terms)
- Indicator Term management
- Parameter management
- Preferences for default IOC version, default IOC context, and default IOC author
- IOC Cloning
- Revert IOC Changes to last saved
- Cut/Copy/Paste & drag and drop for Indicator tree
- Indicator Terms and Paramters defined for MIR, Yara, Splunk, and Volatility

Roadmap:
- Term Conversion Map to associate related terms across context types
- Term Conversions to quickly change context types of IndicatorTerms based on the Conversion Map
- Import Indicator Terms from Intel sources such as CybOX, STIX, or CRITS
- IOC Validation/Testing
- More well defined Indicator Terms and parameters for GRR, Snort, and other systems
- Output relevant formats for use, Splunk searches from Splunk terms, Yara signature outputs from Yara terms, XPATH from MIR terms, etc


Bug reports, questions, comments, requests:
seagill at yahoo-inc dot com
