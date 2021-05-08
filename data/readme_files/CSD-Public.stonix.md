##License

Los Alamos National Security, LLC owns the copyright to "stonix". The license for the software is BSD with standard clauses regarding modifications and redistribution.

stonix has been assigned the Los Alamos Computer Code Number LA-CC-15-021.

Copyright (c) 2015-2018, Los Alamos National Security, LLC All rights reserved.

This software was produced under U.S. Government contract DE-AC52-06NA25396 for Los Alamos National Laboratory (LANL), which is operated by Los Alamos National Security, LLC for the U.S. Department of Energy. The U.S. Government has rights to use, reproduce, and distribute this software. NEITHER THE GOVERNMENT NOR LOS ALAMOS NATIONAL SECURITY, LLC MAKES ANY WARRANTY, EXPRESS OR IMPLIED, OR ASSUMES ANY LIABILITY FOR THE USE OF THIS SOFTWARE. If software is modified to produce derivative works, such modified software should be clearly marked, so as not to confuse it with the version available from LANL.
Additionally, redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

- Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

- Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

- Neither the name of Los Alamos National Security, LLC, Los Alamos National Laboratory, LANL, the U.S. Government, nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY LOS ALAMOS NATIONAL SECURITY, LLC AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL LOS ALAMOS NATIONAL SECURITY, LLC OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

---------------------

0. Overview
-----------

  STONIX is an operating system configuration hardening tool for Unix and Unix
  like (e.g. Linux) operating systems. This tool implements a hybrid of
  guidance from NSA, DISA STIGs, USGCB and the CIS. To as great of a degree as
  possible each guidance element for each platform is evaluated on the other
  platforms for applicability and applied if possible.

  The STONIX program is a modular codebase implemented in Python (currently
  using the 2.x dialect, a port to Python 3.0 is in future planning). Python
  was selected due to it being part of the default install on all target
  platforms. The program is primarily a command-line utility but there is a
  robust GUI built in. The GUI is implemented in PyQt. Many platform packages
  will not express a dependecy on PyQt due to the GUI's optional nature.

  At the present time (revision 0.9.34) the following platforms are used for
  development and test: Red Hat Enterprise Linux 6 and 7, Fedora Linux
  22, OpenSuSE 13.2, Debian 7 and 8 (stable), Ubuntu 14.04 LTS, CentOS 7,
  macOS Catalina 10.15.
  
  Close derivatives of these operating systems should be well supported,
  more distant cousins less so.
  
1. Documentation
----------------

  README	This file
  INSTALL	Installation instructions
  PACKAGERS	Information to packagers
  LICENSE	GNU General Public Licsense v2
  AUTHORS	The main authors of STONIX
  THANKS	An incomplete list of people who contributed to this software
  ChangeLog	Detailed list of changes
  TODO		Known bugs and to-do listing
  DEVELOPERS Detailed documentation for people who want to contribute to STONIX
  
2. Version numbering
--------------------

  STONIX uses a Major.Minor.Release versioning scheme.

  At present STONIX is in an Alpha, not feature complete stage. Every attempt
  is made to ensure that the code is production ready, but the features are not
  yet complete and there will be functionality changes in future revisions.

3. Reporting bugs
-----------------

  When reporting issues in STONIX please fully document the specific
  functionality that is causing a problem. We will likely need sample
  configuration files that cause the section of STONIX to have issues. A copy
  of the debug output is also very valuable.

  Report your issue via the STONIX github issue tracker.

4. Known Issues
---------------

   1. Developers have observed behavior on CentOS where DisableThumbnailers
   returns non-compliant after the fix is run. This appears to be due to
   issues in gconf or dbus and the rule is working as designed.
