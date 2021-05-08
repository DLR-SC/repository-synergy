# YaYaNLP: Chinese Language Processing
YaYaNLP是一个纯python编写的中文自然语言处理包，取名于“牙牙学语”。
YaYaNLP提供以下功能：
- 中文分词
- 词性标注
- 命名实体识别
 * 人名识别
 * 地名识别
 * 组织机构识别
- 简繁转换

## 项目

项目主页：[https://github.com/Tony-Wang/YaYaNLP](https://github.com/Tony-Wang/YaYaNLP)

我的主页：[www.huangyong.me](http://www.huangyong.me)

## 安装

### 直接下载源码包，解压后运行

``` bash
python setup.py install
```

### 下载字典与模型文件

YaYaNLP使用了与HanLP兼容的字典数据，而编译后的字典数据保存的扩展名为.ya
可以直接从hanLP项目下载，[data-for-1.2.4.zip](http://pan.baidu.com/s/1gd1vo8j)

### 配置数据文件路径

在**yaya/config.py**修改自己的数据文件路径
``` python
DATA_ROOT = "/your/data/path"
```

## 特性

### 人名识别

``` 
    # 识别人名
    text = u"签约仪式前，秦光荣、李纪恒、仇和等一同会见了参加签约的企业家。"
    terms = segment.seg(text)
    print_terms(terms)
```

```
签约/vi
仪式/n
前/f
，/w
秦光荣/nr
、/w
李纪恒/nr
、/w
仇和/nr
等/udeng
一同/d
会见/v
了/ule
参加/v
签约/vi
的/ude1
企业家/nnt
。/w
```


### 歧意词识别

```
    # 识别歧意词
    text = u"龚学平等领导说,邓颖超生前杜绝超生"
    terms = segment.seg(text)
    print_terms(terms)
```

```
龚学平/nr
等/udeng
领导/n
说/v
,/w
邓颖超/nr
生前/t
杜绝/v
超生/vi
```

### 地名识别

``` 
    # 识别地名
    text = u"蓝翔给宁夏固原市彭阳县红河镇黑牛沟村捐赠了挖掘机"
    terms = segment.seg(text)
    print_terms(terms)
```

```
蓝翔/nt
给/p
宁夏/ns
固原市/ns
彭阳县/ns
红河镇/ns
黑牛沟村/ns
捐赠/v
了/ule
挖掘机/n
```

### 组织名识别

```
    # 组织名识别
    text = u"济南杨铭宇餐饮管理有限公司是由杨先生创办的餐饮企业"
    terms = segment.seg(text)
    print_terms(terms)
```

```
济南杨铭宇餐饮管理有限公司/nt
是/vshi
由/p
杨先生/nr
创办/v
的/ude1
餐饮企业/nz
```

### 简繁转换

```
    # 简繁转换
    text = u"以后等你当上皇后，就能买草莓庆祝了"
    print segment.simplified_to_traditional(text)
```

```
以後等妳當上皇后，就能買士多啤梨慶祝了
```

```
    # 繁简转换
    text = u"用筆記簿型電腦寫程式HelloWorld"
    print segment.traditional_to_simplified(text)
```

```
用笔记本电脑写程序HelloWorld
```

## 感谢
本项目参考了[hanck/HanLP](https://github.com/hankcs/HanLP/)项目实现原理并使用了该项目的字典和模型文件。


## 版权
* Apache License Version 2.0
* 任何使用了YaYaNLP的全部或部分功能、词典、模型的项目、产品或文章等形式的成果必须显式注明YaYaNLP及此项目主页。
