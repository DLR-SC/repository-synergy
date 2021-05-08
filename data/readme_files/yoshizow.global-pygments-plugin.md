# Pygments Plug-in Parser for GNU GLOBAL

This software is a plug-in parser for GNU GLOBAL.
Uses Pygments, which is a syntax highlighter written in Python, to
extract tags.
Supports wide variety of programming languages thanks to Pygments.

This software can also use Exuberant Ctags for collecting definition tags
as well as symbol tags which are collected with Pygments.

**Note**: global-pygments-plugin is now bundled with GLOBAL-6.3.2 or later.
Please use the bundled version in normal case.

## Prerequisites

- gtags (GNU GLOBAL) 5.8.1 or later
- Python 2.6 or later (3.x is not supported)
- Pygments python package
- automake, autoconf, libtool
- Exuberant Ctags 5.5 or later (optional)

## Install

Make sure Pygments package is installed.

    $ pip install Pygments

Generate automake/autoconf stuff.

    $ ./reconf.sh

Configure, build and install.

    # ./configure
    $ make
    $ sudo make install

Notes:

- This software must be installed where gtags have been installed.
  For example, if you have installed gtags under `/opt/local`, you should
  run configure as `./confiure --prefix=/opt/local` .
- This software can work with Exuberant Ctags to extract definition
  tags.
  ctags is automatically detected by configure script.
  If you want to specify explicit location of ctags or want to
  disable ctags integration, you can pass `--with-exuberant-ctags=XXX`
  option to configure script.

## Configuration

Like other GLOBAL plug-in parsers, in order to use this plug-in parser
you need to configure `~/.globalrc`.

First, write langmap entries for this plug-in.

    pygments-parser|Pygments plug-in parser:\
        :tc=common:\
        :langmap=ABAP\:.abap:\
        :langmap=ANTLR\:.G.g:\
        :langmap=ActionScript3\:.as:\
		(snip)
        :langmap=XQuery\:.xqy.xquery.xq.xql.xqm:\
        :langmap=XSLT\:.xsl.xslt.xpl:\
        :langmap=Xtend\:.xtend:\
        :gtags_parser=ABAP\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=ANTLR\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=ActionScript3\:/usr/local/lib/gtags/pygments-parser.la:\
		(snip)
        :gtags_parser=XQuery\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=XSLT\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Xtend\:/usr/local/lib/gtags/pygments-parser.la:

(snipped. See complete example: [sample.globalrc](sample.globalrc))  
This is so long, but you can remove unnecessary entries for you.
You can also add languages not listed here but supported by Pygments.

Change path of `/usr/local/lib/gtags/pygments-parser.a` according to
the path where you installed this plug-in.

Then, edit `default:` clause of `~/.globalrc` to use pygments-parser.
(Or you can configure this by setting environment variable GTAGSLABEL.)

     default:\
    -        :tc=native:
    +        :tc=native:tc=pygments:
    +pygments:\
    +:tc=pygments-parser:tc=htags:

Complete example is available: [sample.globalrc](sample.globalrc).

## Usage

Once you have configured ~/.globalrc, you can use gtags as usual.

    $ cat hello.rb
    class Hello
      def hello
        puts message
      end

      def message; 'hello, world'; end
    end
    $ gtags
    $ global -sx message hello.rb 
    message             3 hello.rb             puts message
    message             6 hello.rb           def message; 'hello, world'; end

As you can see the identifier 'message' in line 3 and line 6 are listed.
They are originally reference tag and definition tag respectively,
but they are both listed as symbol tags as they cannot be distinguished
from Pygments's output.

When ctags is installed, this parser calls ctags to collect definition tags.
This enables distinguishing definition tags and reference tags.
Of course, this is only avaiable for programming languages which is
supported by ctags.

    $ gtags
    $ global -x message hello.rb 
    message             6 hello.rb         def message; 'hello, world'; end
    $ global -rx message hello.rb 
    message             3 hello.rb             puts message

You can see 'message' are listed as definition tag and reference tag.

### Customizing Behavior

Some programming languages allow punctuation characters within identifiers.
For example methods like `gsub!` or `empty?` in Ruby.
By default, this plug-in parser includes these kind of punctuation characters
in generated tags.
But for some GLOBAL front-ends (like gtags.el) this behavior is 
inconvenient.

In such case, you can set environment variable
`GTAGSPYGMENTSOPTS=strippunctuation` before running `gtags` to strip
punctuation characters from generated tags.

    $ cat hello.rb
    s = 'hello'
    s.gsub!(/./, '')
    s.empty?
    $ gtags
    $ gtags -d GRTAGS
    __.COMPACT   __.COMPACT
    __.COMPLINE  __.COMPLINE
    __.COMPNAME  __.COMPNAME
    __.VERSION   __.VERSION 6
    empty?  1 @n 3
    gsub!   1 @n 2
    s   1 @n 1-2
    $ export GTAGSPYGMENTSOPTS=strippunctuation
    $ gtags
    $ gtags -d GRTAGS
    __.COMPACT   __.COMPACT
    __.COMPLINE  __.COMPLINE
    __.COMPNAME  __.COMPNAME
    __.VERSION   __.VERSION 6
    empty   1 @n 3
    gsub    1 @n 2
    s   1 @n 1-2

## Limitations

This parser works for most programming languages supported by Pygments.
But for some languages it does not work well.  
For example, CoffeeScript lexer in Pygments 1.6 splits tokens in an
unusual manner. This may contribute to readability as a syntax
highlighter, but not work well with this software.

## Issues and Questions

If you have any issues or questions, please create an issue on GitHub.

https://github.com/yoshizow/global-pygments-plugin/issues

Pull requests are also welcome!

This product is depend on but does not have direct relationship to
neither GNU GLOBAL, Pygments nor Exuberant Ctags.
Please don't ask them questions about this software.

## Tested Environment

Tested with:

- Python 2.7.3
- Pygments 1.6
- autoconf 2.69
- automake 1.14.1
- libtool 2.4.2
- global 6.2.9
- Exuberant Ctags 5.8
