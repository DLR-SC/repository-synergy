**Deprecated in favor of mem_util**
https://github.com/yaroslavvb/chain_constant_memory/blob/master/mem_util_test.py

# memory_util

This utility parses LOG_MEMORY messages out of TensorFlow vlog output and builds timeline of memory allocations

## Example usage:

(only works for GPU for later versions of TF)

```
# install memory util
import urllib.request
response = urllib.request.urlopen("https://raw.githubusercontent.com/yaroslavvb/memory_util/master/memory_util.py")
open("memory_util.py", "wb").write(response.read())

import memory_util
memory_util.vlog(1)
import tensorflow as tf

sess = tf.Session()
a = tf.random_uniform((1000,))
b = tf.random_uniform((1000,))
c = a + b
with memory_util.capture_stderr() as stderr:
    sess.run(c.op)
memory_util.print_memory_timeline(stderr, ignore_less_than_bytes=1000)
```

And you'll see

```
       67       random_uniform/RandomUniform(32-cpu)        4000        4000 cpu
       69                 random_uniform/mul(33-cpu)        4000        8000 cpu
       71       random_uniform/RandomUniform(32-cpu)       -4000        4000 cpu
       72                     random_uniform(34-cpu)        4000        8000 cpu
       74                 random_uniform/mul(33-cpu)       -4000        4000 cpu
       75     random_uniform_1/RandomUniform(35-cpu)        4000        8000 cpu
       77               random_uniform_1/mul(36-cpu)        4000       12000 cpu
       79     random_uniform_1/RandomUniform(35-cpu)       -4000        8000 cpu
       80                   random_uniform_1(37-cpu)        4000       12000 cpu
       82               random_uniform_1/mul(36-cpu)       -4000        8000 cpu
       83                                add(38-cpu)        4000       12000 cpu
       85                     random_uniform(34-cpu)       -4000        8000 cpu
       86                   random_uniform_1(37-cpu)       -4000        4000 cpu
       87                                add(38-cpu)       -4000           0 cpu
```
