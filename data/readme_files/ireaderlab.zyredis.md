=======
zyredis yet another redis client that support failover and codis, zyredis is also a redis orm that supports define redis model
=======
iReader python接入redis客户端

项目描述
--------

- 实现redis接入以及redis的failover机制
- 实现redis客户端级别的负载均衡
- 解决长连接失效后需要重启服务问题
- 提供redis的基础model层
- 支持codis

项目当前状态
---------

- 服务线上所有redis的接入，日请求量大于5亿
- failover机制可以灵活切换redis proxy，并配置不同不服务器的负载

项目依赖
--------

- [QConf](https://github.com/Qihoo360/QConf) 可以用也可以不用，非必须依赖
- QConf python client目前已经集成到本目录代码中，zyredis/utils/qconf_py.so是通过QConf项目编译的python客户端，可以用也可以不用，非必须依赖
- [redis client](https://github.com/andymccurdy/redis-py) 必须依赖
- [Codis](https://github.com/wandoulabs/codis)  如果使用codis的话可以参考，非必须依赖项

当前版本
--------

- v1.0.0 兼容redis所有原生命令和codis支持的命令，额外提供pythonic的数据结构，此外zyredis还是一个redis ORM用于规范redis的key的定义规则，数据类型的使用，zyredis还对阻塞redis后端的操作进行了统一优化避免因为开发的失误导致对后端redis的阻塞


安装
--------

```
git clone https://github.com/ireaderlab/zyredis.git
cd zyredis
python setup.py install
```

使用举例
-------

- zyredis封装了pythonic的对象有以下几个
- Client: 用于和redis进行交互的对象
- Key: 提供了统一的key的封装方式
- List: redis官方的List数据结构的封装，支持python原生的List方法
- Set: redis官方的Set数据结构的封装，支持python原生的set操作方法
- SortedSet: redis官方的SortedSet数据结构的封装
- Dict: redis官方的Dict数据结构的封装，支持python原生的dict操作方法
- ZSet: ZSet官方的zset数据结构的封装
- Plain: 对写入redis的数据的默认编解码操作，Plain是不对数据进行处理
- Pickler: 使用python的Cpickle对数据进行编解码
- JSON: 使用JSON对写入和读取的数据进行编解码
- NotSupportCommandError: 可能会触发的异常，codis客户端存在个别命令不支持，通过异常的方式进行抛出
- Model: 所有的redis相关的操作都通过一个model进行交互
- RedisManager: 管理所有redis的连接

使用zyredis的orm举例
------
- 如果使用纯粹redis的orm管理的话可以用下面举例的方式来创建BaseRedisModel
```python
# 定义完redis的基础model后其他所有的model均继承自此model即可
class BaseRedisModel(Model):

    client_name = "test_redis"
    db_num = 0
    # 说明使用本地配置项
    init_from = "local"
    # 初始化redis配置
    redis_conf = {
        0:"redis://localhost:6389/test_redis?weight=1&transaction=1&db=0",
        1:"redis://localhost:6389/test_redis2?weight=3&transaction=1&db=0",
    }
```
- 如果使用qconf提供的配置项来做配置管理的话请参考下面配置
qconf对应zookeeper配置项路径：/test_group/service/codis
该路径下节点codis0的值为：redis://localhost:6389/test_cache?weight=1
该路径下节点codis1的值为：redis://localhost:6339/test_cache?weight=3
该路径下节点codis2的值为：redis://localhost:6339/test_db?weight=1
该路径下节点codis3的值为：redis://localhost:6339/test_db?weight=2

这样的配置项目声明了两种proxy的客户端分别为用做缓存的test_cache和用做db的test_db
```python
from zyredis import Model

class BaseCacheModel(Model):

    client_name = "test_cache" # 声明使用的客户端名称
    db_num = 0
    init_from = "qconf"
    zk_path = "/test_group/service/codis" # qconf对应的zookeeper路径

class BaseDbModel(Model):

    client_name = "test_db" # 声明使用的客户端名称
    db_num = 0
    init_from = "qconf"
    zk_path = "/test_group/service/codis" # qconf对应的zookeeper路径

class TestCacheModel(BaseCacheModel):

    prefix = "wlctest"

    def set_key(self, arg1, arg2, val):
        # redis key = wlctest_{arg1}_{arg2} 默认使用下划线连接
        self.db[self.key[arg1][arg2]] = val

    def set_key1(self, arg1, val):
    	# redis key = wlctest_{arg1}
        self.db.set(self.key[arg1], val)

    def get_key(self, arg1, arg2):
        return self.db[self.key[arg1][arg2]]

    def get_key1(self, arg1):
        return self.db.get(self.key[arg1])

class TestDbModel(BaseDbModel):

    prefix = "wlctest"

    def set_key(self, arg1, arg2, val):
    	# redis key = wlctest_{arg1}_{arg2} 默认使用下划线连接
        self.db[self.key[arg1][arg2]] = val

    def set_key1(self, arg1, val):
    	# redis key = wlctest_{arg1}
        self.db.set(self.key[arg1], val)

    def get_key(self, arg1, arg2):
        return self.db[self.key[arg1][arg2]]

    def get_key1(self, arg1):
        return self.db.get(self.key[arg1])
```
- 使用zyredis做为codis的客户端举例
```python
import zyredis

db = zyredis.Client(host='localhost', port=6389, serializer=JSON(), transaction=True)  # transaction=True使用zyredis当做原生redis的client使用
codis_db = zyredis.Client(host='localhost', port=6389, serializer=JSON(), transaction=False)  # transaction=False使用zyredis 当做codis的redis client使用，最大区别是对pipeline事务支持以及codis本身部分api不支持时日志输出

db.set('key', "mydata")
codis_db.set('codis_db', 'codis_data')

db.Dict("test_dict", {'1': 1, '2': 2})  # 对应redis的map数据结构
td = Dict("test_dict")
td.get("1") # will return 1
td.get("2") # will return 2
td['3'] = 3 # 新增字段3
```

开源协议
-------
本软件使用FreeBSD协议开源

技术交流
-----
QQ群：329474804 申请备注请说明zkredis技术交流
