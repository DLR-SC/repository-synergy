# Home Assistant Extras for Yonsm

这是我个人的 Home Assistant 配置和扩展插件库，请酌情参考。**注意，我升级到 0.88 了，目录结构有重大调整，请注意升级调整，或自行适配目录路径**

# 一、[dash.html](www/dash.html) 操作面板

[dash.html](www/dash.html) 是为 Home Assistant 开发操作面板，使用 HA WebSocket API 作为数据通道，基于非常简单的 HTML+JS+CSS 渲染而成的高效、快速的操控面板。可完美替代 AppDaemon 的 HADashboard。

![dash preview](https://bbs.hassbian.com/data/attachment/forum/201901/03/175726uff10j90488qea94.png)

# 1. 用法

- **使用方法**非常简单，只要把 [dash.html](https://github.com/Yonsm/HAExtra/raw/master/www/dash.html) 放入 www 目录，然后使用 `http://xxx.xxx.xxx:8123/local/dash.html` 访问即可。

    - 如果曾经登录过 Home Assistant 并保存过登录会话，访问 /local/dash.html 时会自动复用 HA localStorage accessToken 用于 WebSocket 认证。如果没有会提示转到 Home Assistant 主页登录，请选择保存本次登录才会记录 accessToken。
    - **最佳姿势**：在 configuration.yaml 中加入以下配置，可以在侧栏中直接访问（在 [WallPanel](https://github.com/thanksmister/wallpanel-android) 中配合使用更佳）：
    
```yaml
panel_iframe:
  dash:
    title: 面板
    icon: mdi:microsoft
    url: /local/dash.html
```
 
- **指定地址**：你也可以把 dash.html 放在任何位置，用浏览器打开后，在使用 `dash.html?password@ws:host:8123` 指定要访问的 WS API 地址，其中 password 可以是 HA Legacy Password 或者永久有效的 accessToken（在 HA 用户管理页面中创建“长期访问令牌”）。

- **分组排序**：dash.html 后面可以用`#`指定一个 group 名称（如 `dash.html#group.dash`，依此仅显示此分组的设备，且按这个分组排序（优先依据类型排序，同类型的按分组先后排序）。如果不指定，默认情况下使用 `group.default_view` 分组；如果不想使用分组，可以使用 `dash.html#NA` 来显示所有设备（如果你的 HA 中未使用分组功能，即 group.default_view 不存在，也会 fallback 到显示所有设备）。

- **移动设备**：自适应移动设备，同时在 iOS 中支持 WPA 模式（添加到桌面后使用，看起来非常像个 APP）。

- **设备操作**：支持大多数设备的开关操作，支持空调和风扇的操作模式和温度设置。

# 2. 个性化配置

可以在 customize.yaml 中对特定的设备进行个性化定制，目前支持以下配置：

| key  | 用途 | 不配置/默认情况 | 备注 |
| ------------- | ------------- | ------------- | ------------- |
| dash_name | 名称 | 使用 attributes.friendly_name | 支持 template 模式 |
| dash_icon | 图标 | 传感器显示 state；空调显示当前温度；其它使用 attributes.icon | 支持 template 模式，支持文字（如引用一个传感器属性） |
| dash_extra | 扩展信息 | 空调和风扇显示操作模式和设定温度，其它无 | 支持 template 模式 |
| dash_extra_forced | 强制显示扩展信息 | off 状态下不显示扩展信息 |
| dash_hidden | 不显示 | | hidden 也不显示
| dash_click | 点击时的动作 | 传感器无动作，其它执行开关操作 | 支持 http 链接或 JavaScript |
| dash_relation | 驱动关联设备 | | 用于更新另外一个引用当前状态/属性的设备 |

关于 `template 模式`：支持以下几种示例：

- 直接输入文字如，如 `我的设备`
- 插入 state 宏，如 `状态 ${sate}`
- 插入 attributes 宏，如 `温度 ${temperature}℃`
- 插入其它设备的 state 宏，如 `气温 ${sensor.caiyun_temperature}℃`
- 插入其它设备的 attributes 宏，如 `气温 ${sensor.caiyun_weather.temperature}℃`
- 使用 JavaScript eval 运算，如`eval:"${status}"=="Charging" ? "充电中" : "${status}"`

更多个性化配置案例可以在我的 [customize.yaml](customize.yaml) 中搜索 `dash`，以上几种用法基本上都能找到案例。

# 二、[custom_components](custom_components) 插件

**注意：部分命名为 2.py 是因为和 HA 官方的插件命名冲突或者派生而来**

# 1. [modbus2/climate](custom_components/modbus2/climate.py)

通用 ModBus 空调插件，比 HA 官方做的更通用、更好，详情请参考 [https://yonsm.github.io/modbus](https://yonsm.github.io/modbus)

# 2. [saswell/climate](custom_components/saswell/climate.py)

SasWell 温控面板插件（地暖），详情请参考 [https://yonsm.github.io/saswell](https://yonsm.github.io/saswell)

# 3. [broadlink2/cover](custom_components/broadlink2/cover.py)

基于 broadlink 万能遥控器的窗帘插件（支持 RF），详情请参考 [https://bbs.hassbian.com/thread-1924-1-1.html](https://bbs.hassbian.com/thread-1924-1-1.html)

`这个并非我原创，我只是使用者`，我的修改点：

-   依赖库升级到 `broadlink==0.9.0`，解决 N1 armbian HA 0.8x 下面 segment fault 的问题；
-   `self._travel == 0` 改成 `self._travel <= 0` 避免相关 BUG。

# 4. [caiyun/weather](custom_components/caiyun/weather.py)

彩云天气的标准天气插件，支持15天预报。另外，[旧版 sensror](extra/sensor/caiyun.py) 已不再使用，详情请参考[https://yonsm.github.io/caiyun](https://yonsm.github.io/caiyun)

# 5. [aircat/sensor](custom_components/aircat/sensor.py)

基于 DNS 拦截实现的斐讯悟空空间检测仪 M1 插件，详情请参考网友发的帖子 [https://bbs.hassbian.com/thread-4601-1-1.html](https://bbs.hassbian.com/thread-4601-1-1.html)

另外，基于斐讯在线云数据实现的斐讯悟空空间检测仪 M1 插件 [extra/sensor/phicomm.py](extra/sensor/phicomm.py)，详情请参考 [https://yonsm.github.io/phicomm](https://yonsm.github.io/phicomm)

# 6. [mqtt2/swicth](custom_components/mqtt2/switch.py)

基于 mqtt swicth 扩展的 MQTT 开关，支持以下功能：

- 支持 icon_template 配置，可以使用 Jinja 脚本运算出不同的图标（参考我的 configuration.yaml 中的 mqtt2 Speaker）；
- 支持 original_state attribute。

# 7. [aligenie](custom_components/aligenie/__init__.py)

几乎零配置，一键接入 Home Assistant 的大部分设备到天猫精灵，可以语音控制相关设备开关。详情请参考 [https://bbs.hassbian.com/thread-2700-1-1.html](https://bbs.hassbian.com/thread-2700-1-1.html)

但上述文章是老的实现方式，不适用于此插件。此插件使用姿势更妙，无需第三方服务器，直接使用 Home Assistant 作为服务器和 OAuth，链路更高效。具体可参考网友的帖子 [https://bbs.hassbian.com/thread-4758-1-1.html](https://bbs.hassbian.com/thread-4758-1-1.html)

另外一键接入 Home Assistant 的大部分设备到小爱同学，没有维护了：[miai](https://github.com/Yonsm/HAExtra/blob/master/extra/custom_components/miai.py)。小爱同学的智能设备使用控制方式没有天猫精灵好，需要唤醒词语。详情请参考 [https://bbs.hassbian.com/thread-4680-1-1.html](https://bbs.hassbian.com/thread-4680-1-1.html)

# 8. [miai](custom_components/miai/__init__.py)

小爱同学 TTS 播报插件，可以参考 automation.yaml 中大量使用到相关功能；还可以 [在HomeAssistant中输入文本，让小爱音TTS箱朗读出来](https://bbs.hassbian.com/thread-4184-1-1.html)；我并非原创者，源自 [https://bbs.hassbian.com/thread-3669-1-1.html](https://bbs.hassbian.com/thread-3669-1-1.html)

# 9. [actuator](custom_components/actuator/__init__.py)

根据传感器数值区间来自动控制设备，详情请参考 [https://bbs.hassbian.com/thread-7876-1-1.html](https://bbs.hassbian.com/thread-7876-1-1.html)

# 三、个人配置

## 1. [configuration.yaml](configuration.yaml)

这是我的 Home Assistant 配置文件。

## 2. [automations.yaml](automations.yaml)

这是我的 Home Assistant 自动化文件，其中有些脚本可以参考，如只用 Motion Sensor 解决洗手间自动开关灯的难题。

## 3. [groups.yaml](groups.yaml)

这是我的 Home Assistant 分组文件。

## 4. [customize.yaml](customize.yaml)

这是我的 Home Assistant 个性化配置文件，主要是中文名称和部分插件的个性化扩展配置。

## 5. [scripts.yaml](scripts.yaml)

这是我的 Home Assistant 脚本文件，主要是开关投影仪的批量处理脚本。

# 四、[extra](extra) 其它

# 1. [setup.sh](extra/setup.sh)

树莓派和斐讯 N1 armbian 下安装 Home Assistant 的脚本，仅供参考，请按需逐步执行，不要整个脚本直接运行。

# 2. [其它](extra)

主要是一些过期的或者不用的文件，仅供备忘参考。

