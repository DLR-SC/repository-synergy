# bustime
提供实时的公交车信息查询以及api接口 支持微信公共号查询
>  因为调用了一些接口，长久以后可能会存在一些无法调用的风险。so 项目仅作为学习和交流使用。

- [![repo](http://ohmyrepo.ml/static/ohmyrepo.png)](http://ohmyrepo.ml/show?u=no13bus&r=bustime)

## 开始使用
- `redis-server` 开启redis服务, 程序默认使用的是redis作为一些固定查询结果的缓存(如线路信息，城市列表)
- `pip install -r requirement.txt`
- 配置好config.py内关于微信公共平台的设置
- `python app.py` 即可开启微信公共平台应用
- `python query.py` 命令行查询实时公交信息

## 关于缓存的使用。
- 使用的是[cachecore](https://github.com/core/cachecore)这个缓存库，支持redis, 文件缓存，memcache缓存等。开发者可以使用cachecore其他的缓存策略或者别的缓存库来替换api文件夹内的cache文件内的装饰器代码即可。

## 接口 (see api folder)
- 根据城市区号, 公交路线的号码, 正逆向, 站点序号或者名字来查询当前距离你最近的公交车的实时跟踪情况 (get_bus_realtime)
- 提供支持实时查询的城市列表 (get_cities)
- 单个路线的详细信息查询(起点 终点 首发时间和终点时间) (get_line_infos and get_real_line_infos)
- 单个路线的各个站点的名称查询 (get_line_orders)
- 具体使用方法见 test.py里面的例子

## 提供一个简单命令行查询接口。
- 直接执行 `python query.py` 如下:
```shell
$ python query.py
请输入线路id。格式为 "城市区号-线路号-0" 或者 "城市区号-线路号-1".
1正向行使，0逆向行驶
: 022-633-0
请输入需要查询的站点的名称或者在线路上的序号: 十字街
最近一辆车6秒前报告位置, 距离本站1站

$ python query.py
请输入线路id。格式为 "城市区号-线路号-0" 或者 "城市区号-线路号-1".
1正向行使，0逆向行驶
: 022-633-1
请输入需要查询的站点的名称或者在线路上的序号: 20
最近一辆车1秒前报告位置, 距离本站5站

```
