Windows Executable Shims
========================

This project allows the creation of Windows "executable shims" - exe files
that when run, execute a defined command, passing the command line arguments
on to the subcommand.

They are similar to the shims used by the Python launcher for Windows, the
"pyzzer" Python wrapper project, and the "chocolatey" project.

Usage
-----

Create a shim as follows:

    mkshim.py -f filename.exe -c "a command"

This will generate an executable, `filename.exe`, which when run, will execute
`a command`. So, for example:

    filename a b c

runs

    a command a b c

Note that there is no requirement for the command to be just an executable
name. A common usage might be to run `py C:\Some\Python\Script.py`.

It is possible to have the supplied arguments inserted somewhere other than
at the end of the line, by including `%s` in the command string. The arguments
will be inserted in place of the `%s`.

Technical Details
-----------------

The command is executed using the Windows `CreateProcess` API, so file
associations will not be considered when running the subcommand.

The stub executable is built from the `stub.c` source. The compile command is
simply `cl /Festub.exe stub.c`. The script is built from `template.py` and the
stub exe using `build.py`.

If you want to use a different stub when building a shim (for example, when
testing a change to the stub code) you can use the `--stub` argument to
specify the name of the sub exe directly.

Current WIP changes (undocumented)
----------------------------------

The stub now works by taking an appended UTF8 text file. There's a sample
in the file "footer". There's a wait element to determine whether to wait
for the subcommand, but it defaults to true for a console shim and false
for a gui one, so it should never need setting manually.

The command element supports %% (%) %a (the arg list) and %d (the directory
of the shim) substitutions.

The "subsystem.py" script is the beginnings of a subsystem editing utility.
Comments in the source include the relevant bits of the Windows headers.

With the new system, I'm less sure how useful mkshim/template is. You can
create a shim just by writing the footer and doing ```copy /b stub.exe+footer
shim.exe```.

Future Possibilities
--------------------

1. Enhance the command template syntax, for example a %-directive to mean the
   directory of the stub (to allow running programs relative to the stub).
2. Additional control over the subprocess - altered environment, run in a
   specific directory, ...?
