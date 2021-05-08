#Parenthetic

Parenthetic is a programming language that uses only ```(``` and ```)``` as code. All other characters are considered comments.

##Hello World

The following Parenthetic program prints 'hello world':

    ((()()())(()(()()))((()(()))((())()()()()()()())((()()(()))((())()()()()()()()()())
    ((())()()()()()()()()()()))))((()()())(()(()()()))((()(())(())())((())()()()()()()(
    )()()()()()()()()()()()()()()()()()()()()()()()()())))((()(()))((()(())(())())((()(
    ()))(()(()()))((())()()()()()()())))((()(())(())())((()(()))(()(()()))((())()()()()
    )))((()(())(())())((()(()))(()(()()))((())()()()()()()()()()()())))((()(())(())())(
    (()(()))(()(()()))((())()()()()()()()()()()())))((()(())(())())((()(()))(()(()()))(
    (())()()()()()()()()()()()()()())))(()(()()()))((()(())(())())((()(()))(()(()()))((
    ())()()()()()()()()()()()()()()()()()()()()()())))((()(())(())())((()(()))(()(()())
    )((())()()()()()()()()()()()()()())))((()(())(())())((()(()))(()(()()))((())()()()(
    )()()()()()()()()()()()()())))((()(())(())())((()(()))(()(()()))((())()()()()()()()
    ()()()())))((()(())(())())((()(()))(()(()()))((())()()()))))

##Installation

1. Clone the repo, which includes an interpreter written in Python 2.7:

   ```git clone git@github.com:cammckinnon/Parenthetic.git```

2. Navigate to the Parenthetic directory and run the interpreter by typing:

   ```python parenthetic.py```

   It accepts code as input from standard input. Input is read until EOF is found, after which the output is written to the console.

3. Or you can read input from a file like this:

   ```cat program.p | python parenthetic.py```

##Syntax

Parenthetic uses Lisp-style expressions, where parentheses enclose expressions:

    (foo arg1 arg2)

Note that parenthetic programs with unmatched parentheses are invalid

###Integers

A sequence of *n* parenthesis sets can be used to represent the integer *n*. For example the following sequence could represent the number 3:

    () () ()

In order to tell the interpreter that you want the sequence to represent an integer, you must pass it as an argument to the built-in ```(())``` macro. The macro acts like a function that accepts parenthesis sequences and returns integers. For example, the following program prints 3.0 to the console:

    (
        integer macro
        (())
        3 sets of parentheses
        () () ()
    )

*Output*: ```3.0```

Or equivalently:

    ((()) ()()())

*Output*: ```3.0```

Note that it doesn't matter how the parentheses in the sequence are nested within each other. For instance the following Parenthetic program prints 5.0 to the console:

    ((()) ((())) () () )

*Output*: ```5.0```

###Symbols

A symbol is a sequence of parentheses that corresponds to some data or a function. For example, the symbol for the built-in multiplication function is ```()(())```. Like with integers, there is a macro for interpreting parenthesis sequences as symbols. It is ```()```.

For example, the following Parenthetic program prints 10 by using the multiplication function ```()(())``` to multiply 5 times 2:

    (
        multiply [note the use of the [] macro]
        (() ()(()))

        2
        ((()) ()())

        5
        ((()) ()()()()())
    )

*Output*: ```10.0```

Equivalent Lisp code:

    (* 2 5)

It is also possible to define your own symbols, using the built-in 'define' function, whose symbol is ```()()```. For example, the following code defines ```(())(())``` as 6, then adds multiplies by 2 to get 12. Remember that all characters other than ```(``` and ```)``` characters are comments (including ```[``` and ```]```).:

    define [[]][[]] as 6
    (
        define
        (() ()())

        [[]][[]]
        (() (())(()))
        
        6
        ((()) ()()()()()())
    )

    [[]][[]] * 2
    (
        multiply
        (() ()(()))

        [[]][[]]
        (() (())(()))

        2
        ((()) ()())
    )

*Output*: ```12.0```

Equivalent Lisp code:

    (define x 6)
    (* x 2)

##Standard Library

Parenthetic has a built-in standard library that is available by default (no includes/library imports necessary):

###define
Symbol: ```()()```

For details on **define** and its usage, see the Syntax->Symbols section above.

###multiply, divide, subtract, add
These math operations can be performed on one or more numbers. Here are their symbols:

 - **subtract**: ```(()())```
 - **multiply**: ```()(())```
 - **divide**: ```(())()```
 - **add**: ```(())```. Note: You can also use **add** for concatenating characters/strings together (see the **string** section below).

Example:

    (
        plus
        (() (()))
        
        3
        ((()) ()()())

        6
        ((()) ()()()()()())
    )

*Output*: ```9.0```

Equivalent Lisp code:

    (+ 3 6)


###lambda
Symbol: ```()```

Facilitates anonymous functions. Here's an example where we use **define** and **lambda** to create a function that takes in a number and adds 1 to it:

    define a [][][] as a function that
    takes in a number n and returns n + 1
    (
        define
        (() ()())

        [][][]
        (() ()()())

        (
            lambda
            (() ())

            (
                n [[]][]
                (() (())())
            )

            n + 1
            (
                plus
                (() (()))
                
                n [[]][]
                (() (())())

                1
                ((()) ())
            )
        )
    )

    7 + 1
    (
        plus
        (() ()()())
        7
        ((()) ()()()()()()())
    )


*Output*: 8.0

Equivalent Lisp code:

    (define f
      (lambda (n)
        (+ n 1)))

    (f 7)


###equal

Symbol: ```(())(())```

Takes in two arguments. If they are equal, the True primitive is returned. Otherwise the False primitive is returned.

Example:

    [equal 2 2]
    (
        equal
        (() (())(()))
        2
        ((()) ()())
        2
        ((()) (()))
    )

*Output*: ```True```

Equivalent Lisp code:

    (equal? 2 2)

###<=

Symbol: ()(())()

Takes in two numeric arguments *a* and *b*. If *a* <= *b*, the True primitive is returned. Otherwise the False primitive is returned.

Example:

    [<= 3 4]
    (
        <=
        (() ()(())())
        3
        ((()) ()()())
        4
        ((()) (())(()))
    )

*Output*: ```True```

Equivalent Lisp code:

    (<= 3 4)

###if

Symbol: ```()()()```

Takes in three arguments: *condition*, *then*, and *else*. If *condition* is not false and not 0, the *then* argument is evaluated and returned. Otherwise, the *else* argument is evaluated and returned.

Example:

    if 3 = 4, return 1, otherwise return 2
    (
        if
        (() ()()())

        [equal 3 4]
        (
            equal
            (() (())(()))
            3
            ((()) ()()())
            4
            ((()) ((()))())
        )

        1
        ((()) ())
        2
        ((()) ()())
    )

*Output*: ```2.0```

Equivalent Lisp code:

    (if (equal? 3 4) 1 2)

###not

Symbol: ```()(()())```

If the argument is neither 0.0 nor False, True is returned. Otherwise, False is returned.

Example:

    [not [equal 1 1]]
    (
        not
        (() ()(()()))

        [equal 1 1]
        (
            equal
            (() ()(())())
            1
            ((()) ())
            1
            ((()) ())
        )
    )

*Output*: ```False```

Equivalent Lisp code:

    (not (equal? 1 1))

###cons

Symbol: ```((()))()```

Takes in two arguments *a* and *b* and returns a pair ```(a, b)```.

Example:

    (
        cons
        (() ((()))())

        1
        ((()) ())

        2
        ((()) ()())
    )

*Output*: ```(1.0, 2.0)```

Equivalent Lisp code:

    (cons 1 2)

###car

Symbol: ```((()))(())```

Given a pair ```(a, b)```, returns `a`.

Example:

    (
        car
        (() ((()))(()))

        (
            cons
            (() ((()))())

            1
            ((()) ())

            2
            ((()) ()())
        )
    )

*Output*: ```1.0```

Equivalent Lisp code:

    (car (cons 1 2))

###cdr

Symbol: ```((()))()()```

    (
        cdr
        (() ((()))()())

        (
            cons
            (() ((()))())

            1
            ((()) ())

            2
            ((()) ()())
        )
    )

*Output*: ```2.0```

Equivalent Lisp code:

    (cdr (cons 1 2))

###empty

Symbol: ```((()))```

**empty** exists to facilitate lists. We define a list as a pair such that applying **cdr** one or more times to the list will return **empty**. Note - empty is not a function; it can be accessed directly. When printed to the console, **empty** appears as ```()```.

Example:

    (() ((())))

*Output*: `()`

Equivalent Lisp code:

    (list)

###char

Symbol: ```(())(())()```

Accepts one integer argument, and returns the corresponding ascii character.

Example:

    (
        char
        (() (())(())())

        33 [ascii value for '!']
        ((()) ()()()()()()()()()()
              ()()()()()()()()()()
              ()()()()()()()()()()
              ()()())
    )

*Output*: ```!```

###string

Symbol: ```(())()(())```

Accepts a list of characters, and returns a string. **string** is useful for displaying messages.

Example:

    define 97 for easy access to a and b
    (   define
        (() ()())
        97
        (() (()()))
        [+ 7 [* 9 10]]
        (
            (() (()))
            ((()) ()()()()()()())
            (
                (() ()(()))
                ((()) ()()()()()()()()())
                ((()) ()()()()()()()()()())
            )
        )
    )

    [string ['a', ['b', []]]]
    (
        string
        (() (())()(()))
        (   
            cons
            (() ((()))())
            a
            (
                (() (())(())())
                (   
                    (() (()))
                    ((()) )
                    (() (()()))
                )
            )

            (   
                cons
                (() ((()))())
                b
                (
                    (() (())(())())
                    (   
                        (() (()))
                        ((()) ())
                        (() (()()))
                    )
                )
                empty
                (() ((())))
                
            )
        )   
    )

*Output*: ```ab```

Tip: You can also pass any combination of characters and strings into the **add** function (see above) to create strings.


##Error handling

If your program has a runtime error or a compiletime error the interpreter will print "Parenthesis Mismatch" to standard output and then exit.

##Test Suite

In the `./tests` folder there is a series of tests that check the interpreter for correctness.

        python tests.py

You may find this useful if you wish to modify the interpreter's source code.

##Inspiration

This language was inspired by a conversation with [Lucas](http://www.lucaswoj.com), who said that scheme looks like this: ())()()()))))(). Well, it does now!

Also the esoteric language [Parenthesis Hell](http://esolangs.org/wiki/Parenthesis_Hell) was a great inspiration.