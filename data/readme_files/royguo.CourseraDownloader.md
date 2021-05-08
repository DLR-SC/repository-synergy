感谢各位小伙伴的关注，本项目由于时间问题不再更新了，现在Coursra的官网结构更改后，已经不可用了

## Features
---
1. 多进程下载，命令行不再显示具体文件的下载进程，统一显示为未完成的任务个数

2. 支持断点续传，第一次没有执行完成的话，第二次只需要指定相同的文件夹即可断点续传.

## Usage
---
1. 把config-sample.py重命名为config.py，把自己coursera的账号密码配置进去

2. usage : ./downloader.py download_dir class_name

**download-dir**: 你要把文件下载到哪个文件夹里，可使用绝对路径或相对路径

**class-name**: 你要下载的课程URL名称，如 https://class.coursera.org/neuralnets-2012-001/lecture/index 这门课，class_name就是neuralnets-2012-001

![revolunet logo](https://raw.github.com/royguo/CourseraDownloader/master/demo.png "revolunet logo")

## Download
---
需要注意，必须要先在coursera上enroll课程才可以下载

下载逻辑在downloader.py的main函数中，可以根据需要修改

下载过程使用curl，在linux正常运行，没测试windows。

## Issue
不知道为何，下载过程总是会时不时的僵死，重启即可，文件已经存在的话不会重新下载，此问题正在解决中，看起来像是国内的网络问题导致。
