# STTinyPNG-Python

TinyPNG 批量压缩图片脚本

待解决的问题 ： 请保持文件路径中没有中文 （文件名可以是中文）

## 一、环境配置

别被这四个字吓到了，只需要一行命令。

首先，电脑需要有 Python 环境，正好 Mac 自带 Python 环境。然后，安装 TinyPNG 的库：

``` ruby
sudo pip install --upgrade tinify
```

ok，环境配置到此结束。

## 二、申请 AppKey

到[ TinyPNG 网站](https://tinypng.com/developers)上去申请 AppKey，唯一不是很爽的就是一个月只能压缩 500 张（但这不是没限制你可以注册多少个吗…）。填写名字和邮箱，验证以后就可以获得 AppKey 了，很方便。

## 三、下载并运行脚本

打开 `STTinyPNG-Python.py` ，填写你的 AppKey、图片文件夹路径、图片输出文件夹路径（输出文件夹空的就行，如果图片里的文件夹目录不存在，会自动创建）。

``` python
tinify.key = "your AppKey" # AppKey
fromFilePath = "/Users/tangjr/Desktop/test1" # 源路径
toFilePath = "/Users/tangjr/Desktop/test2"   # 输出路径
```

ok，运行脚本。打开终端：

``` ruby
python /Users/tangjr/Documents/STTinyPNG-Python/STTinyPNG-Python.py
```

Done ！

## 四、简单说一下思路

使用 Python 的 `os` 库，遍历源文件夹，找到 `.png` 或 `.jpg` 文件，则进行压缩（ TinyPNG 只支持这两种图片类型）。

恩，就这么简单，没了...

