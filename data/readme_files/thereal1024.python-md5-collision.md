# Python MD5 Collision Library
for CS 460 SP15

I don't currently have a creative name for this library. I was hoping to use MD5SuperCollider, but that's [taken](https://github.com/culmor30/MD5-SuperCollider).

## Installation
First, this library currently only runs on Linux because it uses some unix commands (tested with Ubuntu). It may work on Mac, but that is untested. The library is designed for Python 3 and it requires the boost library headers as a dependency. Obviously standard C compilation packages including gcc are also required. One of the demos outputs Python 2 scripts (not feasible to do in v3), so also have Python 2 to make that work.

```sh
$ sudo apt-get install libboost-all-dev
$ sudo apt-get install python # python 2
$ sudo apt-get install python3
```

## Description
This library is contained within `coll.py` (which depends on `md5.py`) and can be used to generate a collection of different files that all have the same MD5 hash. To accomplish this task, I used the [chosen prefix attack](https://en.wikipedia.org/wiki/Collision_attack#Chosen-prefix_collision_attack) from [Marc Stevens'](https://marc-stevens.nl/p/hashclash/) hashcoll program. His program allows one to supply the intermediate hash value (IHV) of the MD5 function and get two pairs of 2 blocks (128 bytes each) that are different yet, after the next 2 block iterations the IHVs will be the same.

The effect of this attack is that given some prefix (starting) data, we can come up with a pair of possible suffix data that are different yet result in the same hash overall when concatentated onto the starting data. `MD5(prefix + collision1a) = MD5(prefix + collision1b)`. We can even extend the above by the inherent linear progression property of MD5. We can use the suffix pair above to generate more complex files: `MD5(prefix + collision1a + moreData)  = MD5(prefix + collision1b + moreData)`. 

Or in the general form: `MD5(prefix + collision1{a,b} + moreData1 + collision2{a,b} + moreData2 + ... + collisionN{a,b} + moreDataN)`, where for each `{a,b}` you have a choice of `a` or `b`. That means given some N collisions, 2^N files with the same MD5 can be generated. Or from the other perspective, if you are looking to generate N files, you need log(N) collisions.

Unfortunately, it is very cumbersome to do interesting things directly with fastcoll and the command line. My library provides a Collider class and other utility functions so you can easily write a script to generate files with the same MD5. 

### My work
- Automatic download and compilation of fastcoll
- Wrote a Python 3 compatible MD5 library that exposes internals including the current IHV (Python's hashlib does NOT)
- Utility functions
    - Pad data to MD5 block size
    - A filter generator that will not allow collision blocks if they contain certain binary substrings
    - Direct access to a wrapper around fastcoll that takes in an IHV and outputs a tuple of the 2 collision parts.
- Collider class
    - Pass in data chunks to build the file
    - Call `diverge()` to place a collision after all the currently supplied data
    - Use `get_collisions()` to get an iterable over each possible colliding total file (as data)
        - Only one file is generated in memory at a time
    - Sanity check functions to help adhere to MD5 block boundaries
- 3 demos, see below

## Demos
Each demo is a Python 3 script that begins with `gen_`.
```sh
$ python3 gen_<scriptname>.py # or
$ ./gen_<scriptname>.py
```

All output files of the demos start with `out_`. This is useful to delete them or check that the MD5 sums are equal. clean.sh removes all output files.
```sh
$ ./clean.sh
$ md5sum out_* # check if related files have the same MD5
$ sha256sum out_* # related files with the same MD5 sum should have DIFFERENT SHA256
```
All demos have comments, so you can read more about how they work in the code. 

**Note that each collision needed will take abou 3s-15s to generate! It's not that fast.**

### Large Amount of Collisions Demo
This demo is in `gen_coll_test.py`. It generates 213 files that have a mix of text and binary data (the binary data is from the collision blocks). Since we need 8 collisions for that, it may take a minute or three to run, but progress is printed. It showcases the simplicity of using the library by completing the task in 25 lines (some blank).

### Python Script Collision Demo
This demo is in `gen_coll_python.py`. It generates two python files `out_py_good.py` and `out_py_evil.py`. The good one prints `good` to the console, while the evil one prints `evil`. It's not hard to imagine this being used for much more nefarious purposes. Caveat: the behaviour of both good and evil is contained in both files and easily visible upon reading them. This is because the only degree of freedom we get between the two files is choosing the collision blocks.

### Binary Collision Demo
This demo is in `gen_coll_c.py`. It first compiles a special C program in `c_demo.c`. Then it generates two executables `out_c_good` and `out_c_evil`. The good one prints `good` to the console (via the `good()` function), while the evil one prints `evil` (via the `evil()` function). These programs are of course harder to open up and examine, but still their behaviour can be determined by working through the disassembly. Obsfucation and anti-debugger techniques could provide more help.

## Future Work
I have taken a look at Marc Stevens' more recent HashClash project, which includes a more sophisticated attack on MD5 that can converge two unrelated pieces of data by adding specially chosen blocks to each. Unfortunately, I was not able to sort out configuration and execution issues with the software. It is much more complex than fastcoll and requires dozens of configuration parameters and the passing through of data between 5 different programs that do steps of the attack in parallel. Still, I am not completely deterred at this point, and will likely make support for it an addition to this project after the semester.
