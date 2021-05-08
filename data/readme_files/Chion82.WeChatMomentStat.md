#WeChat Moment Stat

一个简单的Python脚本，用于分析由[WeChatMomentExport](https://github.com/Chion82/WeChatMomentExport.git)导出的朋友圈json文件```moments_output.json``` （目录下多个json文件为作者测试用样例）

注意：由于WeChatMomentExport只能抓取你的朋友圈数据，部分不可见评论及点赞等信息无法收集（非共同好友），故统计有局限性，仅供参考。

脚本对每个朋友圈好友统计以下数据：

* 发朋友圈数量排名  
* 朋友圈点赞数排名  
* 被点赞数排名  
* 发评论数量排名  
* 朋友圈收到评论数量排名  
* 被无视概率排名（评论被回复数／写评论数，条件为 写评论数>=15）  
* 发投票／问卷调查类广告数排名  

##Usage

拷贝WeChatMomentExport生成的```moments_output.json```到本项目的所在目录下，运行：  
```
$ python wechat_moment_stat.py
```
