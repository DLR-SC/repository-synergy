# xuebao
支持中文的智能音箱，能够听懂你的命令，通过语音控制一切。

原始代码复制自 http://jasperproject.github.io/ branch：jasper-dev，并做了很多修改，具体有：

* 原先的 Jasper 只支持最老版本的 raspberry pi，代码在新版 raspberry pi 上跑不通。通过 debug，修改代码，使代码能够在 raspberry pi 3 上正常跑起来。
* 修改了原先的 config 配置格式，jasper-dev 原有两种配置文件格式，现修改为一种。
* 删除了一些中国用不上连不上的 plugin。
* 语音模块保留了 pocketsphinx-stt 和 espeak-tts，如果需要其他模块，请到 jasper-dev 自行添加。
* 增加了 baidu-tts，需要网络。（有兴趣的朋友可以自己增加科大讯飞的模块）
* 增加了一个 mp3player，可以由语音控制播放，暂停等等。由这个 player，可以播放音乐，讲故事，放儿歌。
* 将命令识别口令从 Jasper 改为 雪宝。

### 怎样工作
成功运行之后，就可以和 xuebao 互动了：
```
你：雪宝
雪宝：滴
你：今天是几号啊？
雪宝：嘟
雪宝：今天是 2016 年 7 月 19 号
```

最终的成品请参考 http://jasperproject.github.io/ 的视频。xuebao 支持中文，会讲中文笑话，中文绕口令，播放音乐，等等，这部分请自行脑补。

### 更多功能
开源软件＋树莓派使我们对 xuebao 有很多想象空间，看看这个 [Mycroft 视频](https://www.indiegogo.com/projects/mycroft-open-source-artificial-intelligence)，我们完全可以用 xuebao 做到一样对功能。

没有做不到，只有想不到。^_^

### 问题讨论
如果遇到什么问题，请到 http://niutool.com 讨论。
