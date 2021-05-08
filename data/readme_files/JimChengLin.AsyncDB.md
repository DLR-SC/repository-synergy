# AsyncDB
When traditional databases encounter concurrency problems, multiple threads and SyncIO is a reasonable solution and is
widely used. However, the DB tries to solve the problem by Python Coroutine and AsyncIO.

The DB can get some optimizations that cannot be done with traditional databases, by modifying B-Tree algorithm.

## Attention
* Python 3.5.1 or later is required and no other dependency.
* Only compatible with coroutine environment.
* All keys must be "bisectable" i.e. can be sorted by bisect.insort.
* There is cache inside. The result can be a reference of the previous result.
* The DB guarantees ACID properties with software failure but hardware.
* If the DB gets closed unexpectedly, it will repair itself next time, which takes time.
* The source code is shared under MIT license.

## Usage
Copy "AsyncDB" folder to the root of your program.

```Python
from AsyncDB import AsyncDB

# open/create
db = AsyncDB('Test.db')

# get
val = await db['key']

# set
db['any_key_bisectable_picklable'] = 'any_value_picklable'

# pop/del
val = db.pop('key')

# iter
items = await db.items(item_from='begin', item_to='end', max_len=1024, reverse=False)

# safely close before exit
await db.close()
```

### 中文
传统数据库面对高并发，采用多线程和同步IO。本作采用协程和异步IO，基于Python开发。

通过对B-Tree进行调整，能做到许多传统数据库做不到的优化。

## 注意事项
* Python 3.5.1以上版本，没有其余依赖。
* 只能在协程环境下使用。
* 所有key必须可以使用bisect排序，建议使用bisect.insort测试。
* 内置缓存，得到的结果有可能是之前结果的引用。
* ACID，软件可以在任意时刻崩溃，数据都是安全的，但对硬件断电之类的情况不做保证。
* 非正常关闭，下一次启动，程序会自动修复数据库，这会相当费时。
* MIT协议发布。
