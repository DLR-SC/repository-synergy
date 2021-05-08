# Pygments - Tomorrow Theme Styles

Pygments style classes for the popular [Tomorrow Theme](https://github.com/chriskempson/tomorrow-theme).


## Installation

Copy the contents of the `styles` folder to your Pygments styles folder.

    cp styles/* /path/to/your/pygments/styles/

## Generating CSS

Run the `pygmentize` command:

`pygmentize -f html -S [style] -a .class-name > output.css`

The options are:

`-f html` - html formatter.  
`-S [style]` - generate style definitions, where `[style]` is the Pygments style class.  
`-a .class-name` - prepend the defintions with a parent CSS class.


### Example 1 - Tomorrow
    
    pygmentize -f html -S tomorrow -a .highlight > tomorrow.css

Output:

    .highlight .hll { background-color: #d6d6d6 }
    .highlight  { background: #ffffff; color: #4d4d4c }
    .highlight .c { color: #8e908c } /* Comment */
    .highlight .err { color: #c82829 } /* Error */
    ...

### Example 2 - Tomorrow Night
    
    pygmentize -f html -S tomorrownight -a .parent-class > tomorrow_night.css

Output:

    .parent-class .hll { background-color: #373b41 }
    .parent-class  { background: #1d1f21; color: #c5c8c6 }
    .parent-class .c { color: #969896 } /* Comment */
    ...
