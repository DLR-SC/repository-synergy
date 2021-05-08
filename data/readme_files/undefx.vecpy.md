VecPy
=====

VecPy builds native libraries from arbitrary kernel functions written in Python. Native libraries leverage multi-threading and SIMD instructions on modern x86 processors to execute the kernel as efficiently as possible. Multiple language bindings allow the vectorized kernel to be called from Python, C++, and Java - all from a single, shared library.


Hello, world!
=====
One of the primary design goals of VecPy is *simplicity*. In just a few lines of code, VecPy translates and compiles a Python function into an efficient, data-parallel native library. The generated library can then be loaded as a Python module, allowing the optimized function to be used as a drop-in replacement for the original Python function. The following program illustrates how simple it can be to use VecPy to significantly improve Python program performance.
```python
#Import VecPy
from vecpy.runtime import *
from vecpy.compiler_constants import *

#Define the kernel
def volume(radius, volume):
  volume = (4/3 * math.pi) * (radius ** 3)

#Generate some data
def data():
  array = get_array('f', 10)
  for i in range(len(array)): array[i] = (.1 + i/10)
  return array
radii, volumes = data(), data()

#Call VecPy to generate the native module
vectorize(volume, Options(Architecture.avx2, DataType.float))

#Import the newly-minted module and execute kernel
from vecpy_volume import volume
volume(radii, volumes)

#Print the results!
print('Radius:', ', '.join('%.3f'%(r) for r in radii))
print('Volume:', ', '.join('%.3f'%(v) for v in volumes))
```

Features and Functionality
=====
Other design goals of VecPy include *utility*, *flexibility*, and *efficiency*.

VecPy aims to implement a sufficiently large feature set to be useful for meaningful, real-world applications. Conditional operations within `if-elif-else` blocks and `while` loops are fully implemented, and the following Python operators, functions, and constants are currently available:

  - **Operators**
    - Arithmetic: +, -, \*, /, //, %, \*\*
    - Comparison: ==, !=, >, >=, <, <=
    - Boolean: and, or, not
    - Bitwise: &, |, ^, ~, <<, >> (integer only)
  - **Functions**
    - global: abs, max, min, pow, round
    - math: acos, acosh, asin, asinh, atan, atan2, atanh, ceil, copysign, cos, cosh, erf, erfc, exp, expm1, fabs, floor, fmod, gamma, hypot, lgamma, log, log10, log1p, log2, pow, sin, sinh, sqrt, tan, tanh, trunc
  - **Constants**
    - math: e, pi

VecPy provides many options to allow for extensive customization. The following data types and language bindings are currently supported:

  - **Data Types**
    - 32-bit floats
    - 32-bit unsigned integers
  - **Language Bindings**
    - C++
    - Python
    - Java

VecPy relies on multi-threading and SIMD execution to achieve the fastest possible performance. The following x86 architectures and operating systems are currently supported:

  - **Architectures**
    - Generic (no SIMD)
    - SSE4.2
    - AVX2
  - **Operating Systems**
    - Linux

Requirements
=====
  - Python 3.x (to run VecPy)
  - g++ (to compile the native library)
  - Optional: Python 3.x headers if compiling as a Python module
  - Optional: JDK if compiling for use with Java via JNI
