Compiler
========

## Description
A single-pass, recursive decent `LL(1)` compiler written by hand for a made-up.
language. This compiler is written entirely in Python 3 and uses the `gcc`
compiler to finish compilation of the generated intermediate C representation.

## Author
Created by [Evan Sneath](http://github.com/evansneath).

## License
This software licensed under the
[Open Software License v3.0](http://www.opensource.org/licenses/OSL-3.0).

## Dependencies
In order to run, this software requires the following dependencies:

* [Python 3](http://python.org/download/releases/3.3.2/)

## Progress

<table>
<tr><td><b>Component</b></td><td><b>Status</b></td></tr>
<tr><td>Scanning</td><td>Completed</td></tr>
<tr><td>Parsing</td><td>Completed</td></tr>
<tr><td>Type Checking</td><td>Completed</td></tr>
<tr><td>Code Generation</td><td>Completed</td></tr>
<tr><td>Runtime</td><td>Completed</td></tr>
</table>

## Usage
```
usage: compiler.py [-h] [-d] [-o OUT] source

positional arguments:
  source             source file to compile

optional arguments:
  -h, --help         show this help message and exit
  -d, --debug        print comments in generated code
  -o OUT, --out OUT  target path for the compiled code
```

The compiler will scan the source file for all valid tokens and 
parse the language grammar. All scanner, parser, and type errors will be 
outputted as they are encountered. Generated code is then outputted to `ir.c`
where it is then run through the `gcc` compiler. The default output file
generated by the compiler is `a.out` in the working directory. The `-o`
argument may be used to modify the output file name.

The `tests/` directory contains test source files which have several examples 
of token scanning with error/warning handling, grammar parsing, code
generation, and runtime libraries.

## Implementation Details

### Software

In determining the implementation language, robustness was chosen over speed as
the deciding factor for the compiler. Python 3 was selected because ease of
use, access to simple dictionary and table libraries, and my own familiarity
with the language.

As I progressed through the parser stage of the compiler, it became clear that
the simple exception raising and handling would be useful for displaying
compiler errors and trapping at resync points to continue syntax parsing.

### Structure

For the sake of modularity and ease of debugging, the program is structured in
a hierarchical fashion.

`compiler.py` acts as the engine responsible for parsing of
command-line arguments, calling the code parser, and completing the build using
the `gcc` compiler with the appropriate arguments once the intermediate C code
is generated.

`parser.py` and the `Parser` class is the entry-point for the action of
compiling the valid input file. In order to do this, `Parser` inherits the
`Scanner` class (in `scanner.py`) and the `CodeGenerator` class
(in `codegenerator.py`) to allow for simple access to their class methods and
objects. The `datatypes.py` and `errors.py` source files containing several
data types and exception classes respectively which are used in the various
components of the compiler.

### Scanning

The implementation of the language scanner first tackles the problem of source
code parsing by splitting the source code into a list of distinct lines. Not
only does this allow for easier ways to determine end of line and end of file,
but also makes the operation of retrieving line numbers simple for purposes of
warning and error messages.

At the start of each non-whitespace character, the first character is used to
determine the type of the token to expect. The token is returned if the type is
matched without issue. Otherwise, a scanner warning is thrown.

The scanner warnings are never fatal, though syntactically the tokens returned
may cause a parser error. My methodology behind the scanner was to try to
correct as many lexical errors as possible. For instance, if a string literal
has no end quote a warning will be thrown and a quote will be assumed at the
end of the line.

### Parsing

In order to eliminate loops caused by recursive grammar, any left-recursion in
the language grammar was rewritten.

Type-checking is performed in expressions by returning the types from the
expression tree functions and evaluating types for compatibility if an
operation is performed. There are many other locations were type-checking is
performed in the compiler other than expressions.

Parser resync points are used throughout the compiler to continue parsing if
an error is encountered without propagating spurious error messages. Exception
handling in Python is used to elegantly handle resyncing. Once a parser error
is encountered in a statement or declaration, an exception is raised. This
exception is then handled at the starting point of statement or declaration
parsing and the parsing will continue to the next statement or declaration.

Note that once a fatal error or any kind is encountered, code will no longer
be generated.

### Code Generation

Memory and registers for the operation of the program are defined and used as
32-bit integer arrays. This allows for simple addressing of memory and register
space. All non-integer types present in the program are cast as integers for
storage in the memory spaces. In the case of string storage, memory spaces hold
a 32-bit pointer to the start of the string in either the heap (this will be
covered later) or a literal value. To ensure that pointers are 32-bit and may
be cast to integer without issue, the `gcc` compiler flag `-m32` is used.

A fixed number of available register locations are allocated for use. These are
used incrementally and are not reused or reallocated. For this reason, a large
number of registers are required so that register space is always available.
Future improvements could be made to "push back" register allocation to the
first register (`R[0]`) at the end of each scope. At the end of a scope, it can
be assumed that the same register will not be referenced again.

The main memory structure of the program is divided into the stack and heap.
The stack begins are the high memory address and is maintained using both a
stack and frame pointer. The frame pointer (pointing to the scope's return
address) provides a way to easily smash local stack variables when leaving the
scope. All global variables may only be declared in the program scope and are
referenced using the offset from the top of main memory.

The heap in main memory is used only to allocate space for strings during
runtime. This is accomplished using a heap pointer pointing to the next unused
memory location in the heap. As the `getString()` procedure is called, the
string retrieved from `stdin` is moved to the heap and the variable
referencing that string is modified to point to the newly allocated heap
location.

Memory is arranged in the following manner:

```
         MAIN MEMORY
--  .-------------------.
P   | RETURN ADDR       | <== MM_END (MM_SIZE - 1)
R   | ----------------- |
O   | LOCAL/GLOBAL VARS |
G   |         .         |
R   |         .         |
A   |         .         |
M   |         .         |
--  | ----------------- |
P   | PARAMS            | 
R   |         .         |
O   |         .         |
C   |         .         |
E   | ----------------- |
D   | CALLER FP         |
U   | ----------------- |
R   | RETURN ADDR ..    | <== FP
E   | ----------------- |
    | LOCAL VARS        |
    |         .         |
    |         .         |
    |         .         | <== SP
    `---v--v--v--v--v---`
              .
              .
              .
    .---^--^--^--^--^---.
    |         .         |
    |         .         |
    |         .         |
    | HEAP              | <== MM_START (0)
    `-------------------`
```

When entering a scope, the caller pushes all params onto the stack in reverse
order. This allows for easy addressing by their indexes. The caller then stores
its current FP onto the stack and the return address. At this point the called
scope is responsible for maintaining the stack and adding its local variables.

When leaving a scope, the SP is moved to the FP location and the return address
is called. The caller scope then is responsible for restoring the caller FP and
ensuring that all outbound params are written back to their appropriate
locations.

All procedure calls are made using C labels and the `goto` statement. This
ensures that the program code remains in the `main` function and no outside
function calls are required. The technique of using
[labels as values](http://gcc.gnu.org/onlinedocs/gcc/Labels-as-Values.html)
was used to store the location of the return labels on the stack.

Loop and conditional statements also make use of the `goto` statement to
determine program flow. After the conditional expression is resolved to a
boolean form, the register used for the expression is tested. If the expression
resolved to `false`, then the code portion is skipped.

For example:

```
R[0] = <expression_outcome>;
if (!R[0]) goto else_label;
    <do_if>
    goto end_if_label;
else_label:
    <do_else>
end_if_label:
```

### Runtime Environment
Initially, I had created a separate C library to implement the runtime
functions necessary. I determined that these functions were simple enough to be
handwritten directly inline with the generated code as I progressed though
development. The runtime functions use the same principles of stack memory
referencing as other procedures and are populated in the identifiers table
manually at the start of parsing.

## Language Specifications

### Syntax
```
<program> ::=
    <program_header> <program_body>

<program_header> ::=
    'program' <identifier> 'is'

<program_body> ::=
        ( <declaration> ';' )*
    'begin'
        ( <statement> ';' )*
    'end' 'program'

<declaration> ::=
    [ 'global' ] <procedure_declaration>
    [ 'global' ] <variable_declaration>

<variable_declaration> ::=
    <type_mark> <identifier> [ '[' <array_size> ']' ]

<type_mark> ::=
    'integer' |
    'float' |
    'bool' |
    'string'

<procedure_declaration> ::=
    <procedure_header> <procedure_body>

<procedure_header> ::=
    'procedure' <identifier> '(' [ <parameter_list> ] ')'

<procedure_body> ::=
        ( <declaration> ';' )*
    'begin'
        ( <statement ';' )*
    'end' 'procedure'

<parameter_list> ::=
    <parameter> ',' <parameter_list> |
    <parameter>

<parameter> ::=
    <variable_declaration> ( 'in' | 'out' )

<statement> ::=
    <assignment_statement> |
    <if_statement> |
    <loop_statement> |
    <return_statement> |
    <procedure_call>

<assignment_statement> ::=
    <destination> ':=' <expression>

<if_statement> ::=
    'if' '(' <expression> ')' 'then' ( <statement> ';' )+
    [ 'else' ( <statement> ';' )+ ]
    'end' 'if'

<loop_statement> ::=
    'for' '(' <assignment_statement> ';' <expression> ')'
        ( <statement> ';' )*
    'end' 'for'

<procedure_call> ::=
    <identifier> '(' [ <argument_list> ] ')'

<argument_list> ::=
    <expression> ',' <argument_list> |
    <expression>

<destination> ::=
    <identifier> [ '[' <expression> ']' ]

<expression> ::=
    <expression> '&' <arith_op> |
    <expression> '|' <arith_op> |
    [ 'not' ] <arith_op>

<arith_op> ::=
    <arith_op> '+' <relation> |
    <arith_op> '-' <relation> |
    <relation>

<relation> ::=
    <relation> '<' <term> |
    <relation> '>' <term> |
    <relation> '>=' <term> |
    <relation> '<=' <term> |
    <relation> '==' <term> |
    <relation> '!=' <term> |
    <term>

<term> ::=
    <term> '*' <factor> |
    <term> '/' <factor> |
    <factor>

<factor> ::=
    '(' <expression> ')' |
    [ '-' ] <name> |
    [ '-' ] <number> |
    <string> |
    'true' |
    'false' |

<name> ::=
    <identifier> [ '[' <expression> ']' ]

<identifier> ::=
    [a-zA-Z][a-zA-Z0-9_]*

<number> ::=
    [0-9][0-9_]*[.[0-9_]*]?

<string> ::=
    "[a-zA-Z0-9 _,;:.']*"
```

### Semantics
* Procedure parameters are transmitted by value. Recursion is supported.
* Non-local variables and functions are not visible except for those variables
   and functions in the outermost scope prefixed with the global reserved word.
   Functions currently being defined are visible in the statement set of the
   function itself (so that recursive calls are possible).
* No forward references are permitted or supported.
* Expressions are strongly typed and types must match. However, there is
   automatic conversion in the arithmetic operators to allow any mixing between
   integers and floats. Furthermore, the relational operators can compare
   boolean with integer tokens (boolean tokens are converted to integers as
    `false = 0`, `true = 1`).
* The type signatures of a procedure's arguments must match exactly their
   parameter declaration.
* Arithmetic operations (`+`, `-`, `*`, `/` `&` `|`) are defined for integers
   and floats only. The bitwise AND (`&`), bitwise OR (`|`) and bitwise NOT
   (`not`) operators are valid only on variables of type integer.
* Relational operations are defined for integer and boolean tokens. Only
   comparisons between the compatible types is possible. Relational operations
   return a boolean result.