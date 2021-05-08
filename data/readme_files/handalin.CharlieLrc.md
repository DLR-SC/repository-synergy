CharlieLrc
==========
<br>
<h3>查理歌词, 一个微信公众帐号, 1.0版本. 暂时可以实现快速查找歌词.<br>
微信号  chaligeci (查理歌词的拼音)<br></h3>
<br>
<h3>操作指南:</h3>
输入 '歌曲名 歌手名' 发送即可(注意中间有一个空格)
<br>
<br>
<h3>本应用计划以音乐,歌词为核心内容,服务音乐发烧友.</h3><br>
计划如下:<br>
1.0版本: 实现歌词查找功能.<br>
2.0版本: 实现猜歌小游戏功能.<br>
3.0版本: 实现"心情推荐"功能.<br>

<br>
<h3>灵感来源:</h3><br>
我们经常有种情况,突然忘了某句歌词,或者干脆是忘了一段.这种情况下,打开浏览器(或者手机浏览器)来搜索都是一件"划不来"的事情,且不说交互过程麻烦,而且为了读取歌词文本,竟然要下载整个html到手机上,怎么想都不划算.为了解决这个问题,顺便把作业做了.所以查理面世了.查理歌词是一个小巧的歌词助手,可以快速搜索到歌词并返回给用户.

<br>
<h3>后续功能模块开发:</h3><br>
2.0版本会加入猜歌的游戏功能,敬请期待.<br>
  你说你会唱五月天的所有歌曲? "经过了漫长的等候,梦想是梦想,我还是一个我" 出自哪首歌?<br>
  哈哈,看歌词猜歌名, 你ok吗?<br>
<br>
3.0版本,计划实现一个微型推荐系统,基于item之间的关系,为用户推荐精品.<br>
<br>
4.0版本(如果有的话), 计划实现"魔盒"功能, 鼓励用户之间的"音乐交换", 实现一种基于对等交换的社交. 伯牙遇子期, wechat我和你.<br>
<br>
<h3>技术架构：</h3><br>
1. 后端代码托管于 Sina App Engine，用的是Python-Flask<br>
2. 平台发来的用户消息拆成关键词封到一个http包里，发给 xiami.com ，从返回的歌单里用reg挑出第一个链接，取得歌曲内容页<br>
3. 用reg抓取歌词并返回给用户<br>