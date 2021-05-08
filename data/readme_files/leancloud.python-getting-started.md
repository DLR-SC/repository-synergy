# Flask-getting-started

一个简单的使用 Flask 的 Python 应用。
可以运行在 LeanEngine Python 运行时环境。

## 本地运行

首先确认本机已经安装 [Python](http://python.org/) 运行环境。然后执行下列指令：

## 一键部署
[![Deploy to LeanEngine](http://ac-32vx10b9.clouddn.com/109bd02ee9f5875a.png)](https://leancloud.cn/1.1/functions/_ops/deploy-button)

## 本地运行

首先确认本机已经安装 [Python](http://python.org/) 运行环境和 [LeanCloud 命令行工具](https://www.leancloud.cn/docs/leanengine_cli.html)，然后执行下列指令：

```
$ git clone git@github.com:leancloud/python-getting-started.git
$ cd python-getting-started
```

### 安装依赖：

```
pip install -r requirements.txt
```

### 关联应用：

```
lean switch
```

### 启动项目：

```
lean up
```

应用即可启动运行：[localhost:3000](http://localhost:3000)

## 部署到 LeanEngine

部署到预备环境（若无预备环境则直接部署到生产环境）：
```
lean deploy
```

将预备环境的代码发布到生产环境：
```
lean publish
```

## 相关文档

* [LeanEngine 指南](https://leancloud.cn/docs/leanengine_guide.html)
* [Python SDK 指南](https://leancloud.cn/docs/python_guide.html)
* [Python SDK API](https://leancloud.cn/docs/api/python/index.html)
* [命令行工具详解](https://leancloud.cn/docs/cloud_code_commandline.html)
* [LeanEngine FAQ](https://leancloud.cn/docs/cloud_code_faq.html)
