## Shell-Pipe Command

This gdb extension allows the piping of internal gdb commands to external
commands, as described in [this Stackoverflow
question](https://stackoverflow.com/q/7120673/391161).

Suppose one wanted to find all the `mov` instructions in the current function.

    (gdb) disas
    Dump of assembler code for function foo:
    0x0000000000400526 <+0>:     push   %rbp
    0x0000000000400527 <+1>:     mov    %rsp,%rbp
    0x000000000040052a <+4>:     sub    $0x10,%rsp
    0x000000000040052e <+8>:     movq   $0x4005e4,-0x8(%rbp)
    => 0x0000000000400536 <+16>:    mov    -0x8(%rbp),%rax
    0x000000000040053a <+20>:    mov    %rax,%rdi
    0x000000000040053d <+23>:    callq  0x400400 <puts@plt>
    0x0000000000400542 <+28>:    nop
    0x0000000000400543 <+29>:    leaveq
    0x0000000000400544 <+30>:    retq


One can source the file `ShellPipeCommand.py` in their `$HOME/.gdb_init` file,
and then invoke the following command.

        (gdb) shell-pipe disas | grep mov
        0x0000000000400527 <+1>:     mov    %rsp,%rbp
        0x000000000040052e <+8>:     movq   $0x4005e4,-0x8(%rbp)
     => 0x0000000000400536 <+16>:    mov    -0x8(%rbp),%rax
        0x000000000040053a <+20>:    mov    %rax,%rdi

Note that the native gdb `shell` command already handles shell pipelines which
do not involve internal gdb commands.  This extension is intended for the case
where the **first** command in the pipeline is a gdb internal command. If the
first command in the pipeline is a valid gdb command as well as a valid
external command, it will be interpreted as the former rather than the latter.
