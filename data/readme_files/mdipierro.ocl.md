# ocl

ocl is a minimalist library that dynamically (at run time) converts decorated Python functions into C99, OpenCL, or JavaScript. In the C99 case, it also uses distutils to compile the functions to machine language and allow you to run the compiled ones instead of the interpreted ones. In the OpenCL case you can run the compiled ones using pyOpenCL.

It consists of a single pure-Python file containing about 600 lines of code. Some of the ocl functionalities overlap with Cython, CLyter, and Pyjamas. 

It is based on the Python ast module, and the these fantastic libraries:

- http://pypi.python.org/pypi/meta (always required)
- http://pypi.python.org/pypi/pyopencl (required only to run opencl code)

The conversion is purely syntatical and assumes all symbols used in the code are defined on the target. It only check for undefined variables used in assignments. You can only use types which are defined on the target. This means you can use a list or hash table if converting to JS not but if converting to C99 or OpenCL. Functions can only return local variables.

Examples:

## Convert Python Code into C99 Code

    from ocl import Compiler
    c99 = Compiler()
    @c99.define(a='int', b='int')
    def f(a, b):
        for k in range(n):
            while True:
                break
            if k==0 or k!=0 or k<0 or k>0 or not k==0 or \
               k>=0 or k<=0 or k is None or k is not None:
                continue
        c = new_int(a+b)
        printf("%i + %i = %i", a, b, c)

        d = new_ptr_int(CAST(prt_int,ADDR(c)))
        c = REFD(d)
        return c
    print c99.convert(headers=False, constants=dict(n=10))

Output:

    int f(int a, int b) {
        long k;
        int c;
        int* d;
        for (k=0; k<10; k+=1) {
            while (1) {
                break;
            }
            if (((k == 0) || ((k != 0) || ((k < 0) || ((k > 0) || ((! (k == 0)) ||
                ((k >= 0) || ((k <= 0) || ((k == None) || (k != None)))))))))) {
                continue;
            }
        }
        c = (a + b);
        printf("%i + %i = %i",a,b,c);
        d = (int*)((&(c)));
        c = (*(d));
        return c;
    }

Notice variables are declared via `new_int` or similar pseudo-function. Use `new_ptr_float` to define a `float*` or `new_ptr_ptr_long` for a `long**`, etc. The convert allows to pass `constants` defined in the code (`n` in the example). You must define the types of function arguments in the decorator "c99". The return type is inferred from the type of the object being returned (you must retrun a variable defined within the function or ``None`` for void). You can decorate more than one function and get the complete code.

`new_<type>`, `range`, `ADDR` (address of), `REFD` (obj referenced by), `CAST`, `True`, `False`, and `None` are keywords.

## Convert Python Code into C99 Code and replace function with compiled one

    from ocl import Compiler
    c99 = Compiler()
    @c99.define(n='int')
    def factorial(n):
        output = 1
        for k in range(1,n+1):
            output = output*k
        return output
    compiled = c99.compile()
    print compiled.factorial(10)
    assert factorial(10) == compiled.factorial(10)

The function call `compiled.factorial(10)` runs the C-compiled version of the ``factorial`` function. `.compiled()` creates and imports a python module containing all the decorated functions. It returns a module with the compiled functions, `compiled`. Compiled functions can call other compiled functions.

## Convert Python Code into OpenCL code and run it with PyOpenCL

(requires pyopencl to run)

Here is a solver for the Laplace equation "d^2 u = d in 2D"

    from ocl import Compiler
    opencl = Compiler()
    @opencl.define_kernel(
               w='global:ptr_float',
               u='global:const:ptr_float',
               q='global:const:ptr_float')
    def solve(w,u,q):
        x = new_int(get_global_id(0))
        y = new_int(get_global_id(1))
        site = new_int(x*n+y)
        if y!=0 and y!=n-1 and x!=0 and x!=n-1:
            up = new_int(site-n)
            down = new_int(site+n)
            left = new_int(site-1)
            right = new_int(site+1)
            w[site] = 1.0/4*(u[up]+u[down]+u[left]+u[right] - q[site])
    print opencl.convert(constants=dict(n=300))

Output:

    __kernel void solve(__global float* w, __global const float* u, __global const float* q) {
        int right;
        int site;
        int up;
        int down;
        int y;
        int x;
        int left;
        x = get_global_id(0);
        y = get_global_id(1);
        site = ((x * 300) + y);
        if (((y != 0) && ((y != (300 - 1)) && ((x != 0) && (x != (300 - 1)))))) {
            up = (site - 300);
            down = (site + 300);
            left = (site - 1);
            right = (site + 1);
            w[site] = ((1.0 / 4) * ((((u[up] + u[down]) + u[left]) + u[right]) - q[site]));
        }
    }


Here `__kernel`, `__global`, and `__local` are OpenCL modifiers. `get_global_id` and `get_global_size` are OpenCL specific functions. A more comlete example that puts this code into context and runs it with PyOpenCL can be found in the `example_laplace_opencl.py` file.

## Convert Python Code into Javascript Code

(works with jQuery and every other JS library)

    from ocl import Compiler, JavaScriptHandler
    js = Compiler(handler=JavaScriptHandler())
    @js.define()
    def f(a):
        a = new(array(1,2,3,4))
        v = [1, 2, 'hello']
        w = {'a': 2, 'b': 4}
        def g():
            try:
                alert('hello')
            except e:
                alert(e)
        jQuery('button').click(lambda: g())
    print js.convert(call='f')

Output:

    var f = function(a) {
        var a = new array(1,2,3,4);
        var v = [1, 2, "hello"];
        var v = [1, 2, "hello"];
        var w = {"a":2, "b":4};
        var g = function() {
            try {
                alert("hello");
            catch (e) {
                alert(e);
            }
        }
        jQuery("button").click(function () { g() });
    }
    f();

In the JS case, the call="f" option tells JS to call the newly defined function "f". Notice undefined assigned variables are automatically made local with `var`.

Supported control structures include `def`, `if..else`, `for ... range`, `while`, `try ... except`, `break`, `continue`.

## How does it work?

It uses the meta library to convert python code into an "Abstract Syntax Tree". It then calls a handler (C99Handler by default or JavaScriptHandler) which converts the AST into the target language.

In the C99 case, `c99.compile()` uses distutil to compile the source to a binary Python module and it imports the module. The module is returned. A more complex of a C implementation of Black-Scholes solver can be found in `example_black_scholes.py`.

OpenCL code is just C99 code with special types modifiers. ocl provides the `Device` class which allows interaction with GPU devices (and other OpenCL devices) using the myOpenCL library. This handles mapping of host memory into device memory, JIT compilation of OpenCL code, deploying and running on OpenCL devices. A complete example is in the `example_laplace_opencl.py` file.
