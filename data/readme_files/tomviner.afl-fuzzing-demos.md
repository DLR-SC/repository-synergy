# afl fuzzing demos
[afl](http://lcamtuf.coredump.cx/afl/) or *american fuzzy lop* has been getting a lot of buzz recently. So let's have a go at fuzzing things with afl and [python-afl](http://jwilk.net/software/python-afl)

## Installing Fuzzing Tools

- create a working directory and python virtual env
- afl
    - http://lcamtuf.coredump.cx/afl/
    - [Download](http://lcamtuf.coredump.cx/afl/releases/afl-latest.tgz) and unpack
    - follow instructions in [docs/INSTALL](https://github.com/mcarpenter/afl/blob/master/docs/INSTALL)
- python-afl
    - pip install cython
    - pip install python-afl

## Approach

Usage of afl (without python-afl) ([docs](https://github.com/mcarpenter/afl/blob/master/docs/README#L177)):

- `afl-fuzz -i testcase_dir -o findings_dir /path/to/program [...params...]`

**Note**: upon first run, you may be advised to take certain actions to ensure afl's performance is reasonable

Usage of python-afl ([docs](https://github.com/jwilk/python-afl/blob/master/doc/README.rst#readme)):

- Add this code (ideally, after all other modules are already imported) to
  the target program:

```
    import afl
    afl.start()
```
- Use `py-afl-fuzz` instead of `afl-fuzz`:

      `$ py-afl-fuzz [options] -- /path/to/fuzzed/python/script [...]`compound


## Fuzzing Python's JSON library

assuming a layout:

    python-afl/
    └── py-afl-fuzz
    afl-fuzzing-demos/
    ├── json
    │   ├── afl_findings/
    │   ├── afl_testcases/
    │   ├── demo.py
    │   └── README.md
    └── README.md

- cd `afl-fuzzing-demos`
- `../python-afl/py-afl-fuzz -i json/afl_testcases/ -o json/afl_findings/ -- python json/demo.py`

I'm using some very basic testcases to get the fuzzer started, e.g. `{"a":true}` & `{"1":2}`, this should start it off with basic json syntax and it'll mutate from there.

**Note**: afl makes constant reads & writes to the file system, so if you're running on an SSD it's a good idea to replace the output directory with an in-memory RAM disk folder. E.g. on debian based systems, the shared memory directory `/run/shm/`. But obviously remember, the results won't survive a reboot, so copying the results out like this might be best:


    mkdir -p /run/shm/json/afl_findings

    ../python-afl/py-afl-fuzz \
        -i json/afl_testcases/ \
        -o /run/shm/json/afl_findings \
        -- python json/demo.py; cp -r /run/shm/json/afl_findings json/

When you're finished, Ctrl-C and see what you come up with in `json/afl_findings`.
You'll start to see output after a few seconds, but it's usual to leave a fuzzer running for a few days or more.

### Console after all night fuzzing
![image](https://cloud.githubusercontent.com/assets/167319/7226227/b61d1e66-e73e-11e4-8b86-4a00e94e5b89.png)

# bidict

## fuzzing by script


    mkdir -p /run/shm/bidict/afl_findings

    ../python-afl/py-afl-fuzz \
        -i bidict/afl_testcases/ \
        -o /run/shm/bidict/afl_findings \
        -- python bidict/fuzz_script.py; cp -r /run/shm/bidict/afl_findings bidict/


try running outputs against script:


    for f in bidict/afl_findings/hangs/id*; do cat $f | python bidict/fuzz_script.py; done
