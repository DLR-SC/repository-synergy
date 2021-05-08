Markdown Render Library for Douban Code
====

[![Build Status](https://travis-ci.org/qingfeng/mikoto.png)](https://travis-ci.org/qingfeng/mikoto)
[![Code Quality](https://landscape.io/github/qingfeng/mikoto/master/landscape.png)](https://landscape.io/github/qingfeng/mikoto/master)
[![PyPI version](https://badge.fury.io/py/mikoto.svg)](http://badge.fury.io/py/mikoto)

### Mikoto 是什么
[Mikoto](https://github.com/qingfeng/mikoto) 是 CODE 的 Markdown, reStructuredText 渲染库。
基于 Misaka，CODE 使用的渲染相关的方法单独封装了一个库，支持emoji，Task List等高级特性。

### Installation

```
pip install mikoto
```

### 使用方法

#### 代码
```python
>>> from mikoto.libs.text import render
>>> render(markdown_content)
```

#### 命令行
```
mikoto -f README.md
```

#### Demo Site
https://github.com/qingfeng/mikoto_demo

### 具体效果

```
# 富士之风

扇携富士风 送礼回江户

    ```python
    >>> import this
    ```

- [x] 显示标题
- [x] 显示代码
- [x] 显示俳句
- [ ] つづき

:beer:

```

![渲染结果](http://douban-code.github.io/images/mikoto_result.png)
