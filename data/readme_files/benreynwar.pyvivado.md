pyvivado
========

WARNING
-------

It is unlikely this project will be maintained for long.
[fusesoc](https://github.com/olofk/fusesoc) has very similar functionality, but also supports many more FPGA vendors.
I'm trying to migrate my own work to use fusesoc instead of pyvivado.  Future effort will go into
improving fusesoc's support for vivado rather than improving this project.


SUMMARY
-------

A python toolbox for automating vivado projects.

 - Automate generation of Vivado projects.
 - Communicate easily with FPGA-deployed modules from python.

REMOVED FUNCTIONALITY
---------------------

Previously pyvivado contained functionality for generating HDL files
and utilities for testing HDL code with python.  This has now been split
out into separate projects, or abandoned since other open-source tools
were doing it better.

 - Dependency management is best handled using [fusesoc](https://github.com/olofk/fusesoc).
 - Code generation is split off into [fusesoc_generators](https://github.com/benreynwar/fusesoc_generators).
 - Testbench generation, and python-based HDL testsing is split off into [slvcodec](https://github.com/benreynwar/slvcodec).
 - Python tools for Axi4Lite interfaces are split off into [axilent](https://github.com/benreynwar/axilent).
 - Unit testing of HDL is best handled using [VUnit](https://github.com/vunit/vunit).
