# pyZZUF

Python implementation of bit-flip [zzuf](http://caca.zoy.org/wiki/zzuf) mutator.

No more `os.system`, `subprocess.check_output` and `subprocess.Popen` :thumbsup:

## Basic usage

### Inline

```python
from pyZZUF import *

print (pyZZUF(b'good').mutate().tostring().decode())
```

#### Options

```python
from pyZZUF import *

zzuf = pyZZUF(b'good')

# Random seed (default 0)
zzuf.set_seed(9)
# Bit fuzzing ratio (default 0.004)
zzuf.set_ratio(0.91)

# Offsets and ranges
zzuf.set_offset(6)
# Only fuzz bytes at offsets within <ranges>
zzuf.set_fuzz_bytes([[0, 3], [6, EOF]])

# Protect bytes and characters in <list>
zzuf.set_protected([0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39])
# Append more bytes
zzuf.set_protected("0123456789", True)

# Refuse bytes and characters in <list>
zzuf.set_refused("abcd")
# Append more bytes
zzuf.set_refused([0x00, 0xFF], True)

# Permit bytes and characters in <list>
zzuf.set_permitted('bad')
# Append more bytes
zzuf.set_permitted('!', True)

# Fuzzing mode <mode> ([xor] set unset)
zzuf.set_fuzz_mode(FUZZ_MODE_XOR)

print (zzuf.mutate().tostring().decode())
```

### Mutagen

```python
import binascii
from pyZZUF import *

zzuf = pyZZUF(b'good')

for data in zzuf.mutagen(start=0.0, stop=1, step=0.1):
	if __debug__:
		seed, ratio, index = data.get_state()
		print (binascii.hexlify(data.tostring()), seed, ratio, index)
	if data == 'bad!':
		break
```

#### Inheritance of the previous state (meat)

```python
import binascii
from pyZZUF import *

zzuf = pyZZUF(b'good')

for data in zzuf.mutagen(start=0.0, stop=1, step=0.1, inheritance=True):
	if __debug__:
		seed, ratio, index = data.get_state()
		print (binascii.hexlify(data.tostring()), seed, ratio, index)
	if data == 'bad!':
		break
```

### Stream-generator with restoring state of mutator

```python
import binascii
from pyZZUF import *

obj = pyZZUF(b'good')
gen = obj.mutagen(start=0.0, stop=1, step=0.01)

while True:
	try:
		data = next(gen)
		seed, ratio, index = data.get_state()
		
		if __debug__:
			print (binascii.hexlify(data.tostring()), seed, ratio, index)

		if seed == 20:
			# Set next state of generator (<seed>, <ratio>).
			# In this example, it makes an infinite loop!
			gen.send((0, 0.0))

		if data == 'bad!':
			break
	except StopIteration:
		break
```

## Check of identity

```bash
$ echo -n "The quick brown fox jumps over the lazy dog" | zzuf -r0.04 | hd

00000000  54 68 65 20 71 75 69 63  6b 20 62 72 6f 57 6c 20  |The quick broWl |
00000010  66 4f 58 20 6a 75 6f 70  73 24 6f 76 75 72 20 74  |fOX juops$ovur t|
00000020  68 65 21 6c 61 7a 78 20  66 6f 67                 |he!lazx fog|
0000002b

$ python -c "import pyZZUF, sys; sys.stdout.write(pyZZUF.pyZZUF(b'The quick brown fox jumps over the lazy dog', ratio=0.04).mutate().tostring().decode())" | hd

00000000  54 68 65 20 71 75 69 63  6b 20 62 72 6f 57 6c 20  |The quick broWl |
00000010  66 4f 58 20 6a 75 6f 70  73 24 6f 76 75 72 20 74  |fOX juops$ovur t|
00000020  68 65 21 6c 61 7a 78 20  66 6f 67                 |he!lazx fog|
0000002b
```

## Installation

```
pip install pyZZUF
```

## Notes*

> *Use [PyPy](http://pypy.org/) for speedup*
