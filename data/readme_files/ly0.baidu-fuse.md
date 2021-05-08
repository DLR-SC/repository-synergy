baidu-fuse
==========

Introduction
----------

基于百度网盘的一个fuse，实验性项目

随时更新
----------

* *baidufuse2.py* 使用 *axel* 作下载器, 目前在图形界面下浏览会很糟糕 (图形界面如果尝试读取预览图的话).

需要的库
----------

1. fuse (http://fuse.sourceforge.net)
2. baidupcsapi: https://github.com/ly0/baidupcsapi
3. fusepy: https://github.com/terencehonles/fusepy

```Shell
mkdir ./mnt 
python baidufuse.py USERNAME PASSWORD mnt
```

*强烈建议在文本模式下访问挂载点，很多图形界面的文件管理器会尝试读取一部分文件生成预览图，在文件数目多的时候会造成速度慢*

