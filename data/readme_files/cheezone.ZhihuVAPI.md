# ZhihuVAPI:优雅地玩知乎

## 简介

### ZhihuVAPI是什么?

ZhihuVAPI 是一个可以让你以一种优雅的形式调用知乎数据的 Python 包.

### 怎么安装或者更新 ZhihuVAPI?

`pip install -U ZhihuVAPI`

## 使用

### 引用 ZhihuVAPI

`import ZhihuVAPI as zhihu`

后面的`as zhihu`是别称的意思,便于输入.

### 配置用户

配置脚本使用的 `cookies`,一共有两种方法.

1. 什么都不管,脚本会默认读取 Chrome 或者 Cent 的 cookies.如果你是其他类 Chrome 的浏览器,你可以在`config.py`的`cookiepath`自定义cookies文件的路径.
2. 在`config.py`禁用`is_use_chrome_cookies`后,你可以在里面自定义`headers`.


**Mac 用户需要设置自定义的 cookie 和 hash**

登录之后 Zhihu 后，访问 [这个接口](https://api.zhihu.com/people/self)，拿到 json 对象第一层的 id 值。
配置 `ZhihuVAPI/config.py` 文件，`is_use_chrome_cookies = False` ，并且添加你的 hash 属性到文件中，同时使用自定义的 headers，注意将自己知乎页面的 cookie 值填入（仅补全 `Cookie': '_xsrf=...;   z_c0=...'` 省略号代表的值即可）。

```
// 示例
// 接口的返回值
{
    id: "a8bXXXXXXXXXXXXXXXX475", // 这个就是 hash
    favorite_count: xxx,
    voteup_count: xxx,
    live_count: xxx,
    ...// 其他属性
}

// config.py
hash = 'a8bXXXXXXXXXXXXXXXX475'
is_use_chrome_cookies = False
```

使用 `pip install -U --no-dependencies ZhihuVAPI` 来下载依赖可以略过 pywin32 的依赖下载。


### 读取自己

```Python
import ZhihuVAPI as zhihu
self=zhihu.self
print(f'我的名字叫{self.name},目前获得了{self.voteup_count}个赞同,{self.favorited_count}个收藏,有{self.followers_count}个粉丝.提出了{self.question_count}个问题,撰写了{self.answer_count}个答案,{self.articles_count}篇文章,拥有{self.columns_count}个专栏.')

```
输出:
```
我的名字叫以茄之名,目前获得了14480个赞同,7654个收藏,有876个粉丝.提出了24个问题,撰写了49个答案,7篇文章,拥有2个专栏.
```

### 基本操作

ZhihuVAPI 支持以下三种初始化:
1. **URL 初始化**:`zhihu.People('https://www.zhihu.com/people/iCheez/activities')`
2. **ID 初始化**:`zhihu.People('e4f87c3476a926c1e2ef51b4fcd18fa3')`
3. **URL_Token 初始化(仅对用户对象有效)**:`zhihu.People('iCheez')`

对于点赞列表,粉丝列表等数据,ZhihuVAPI支持以下方式调用:

#### 获取列表的所有项
```Python
import ZhihuVAPI as zhihu
self=zhihu.People('iCheez')
for a in self.answers():
    a:zhihu.Answer # 让 IDE 智能提示
    print(a.excerpt)
```

#### 获取列表的指定数量的项
```Python
import ZhihuVAPI as zhihu
self=zhihu.People('iCheez')
for a in self.answers(5):
    a:zhihu.Answer # 让 IDE 智能提示
    print(a.excerpt)
```


#### 获取列表的从某处开始的指定数量的项
```Python
import ZhihuVAPI as zhihu
self=zhihu.People('iCheez')
for a in self.answers(count=5,start=50):
    a:zhihu.Answer # 让 IDE 智能提示
    print(a.excerpt)
```

#### 获取列表的从某页开始的指定数量的项
```Python
import ZhihuVAPI as zhihu
self=zhihu.People('iCheez')
for a in self.answers(count=5,page=2):
    a:zhihu.Answer # 让 IDE 智能提示
    print(a.excerpt)
```

### 获取答案

```Python
import ZhihuVAPI as zhihu
a=zhihu.Answer('https://www.zhihu.com/question/31343133/answer/58763430')
for p in a.voters(count=5):
    p:zhihu.People # 让 IDE 智能提示
    print(p.name)
    if p.is_waterman():
        print(f'{p.name} 是水军')
print(f'这个在 "{a.question.title}" 下的回答得到了{a.voteup_count}个赞同,我{"已经赞同了"if a.is_voting else "还没有赞同" }')

for c in a.comments():
    c:zhihu.Comment
    print(c.content)
a.down() #反对
a.undown() #取消反对(以此类推)
a.vote() # 赞同
a.thank() # 感谢
# a.collect([zhihu.Collection('你自己的收藏夹 ID'),])

```
输出:
```
日志：获取以茄之名的点赞列表
午夜
斗战胜佛
Chern
万铆工
言知
这个答案在 "以下这篇文章关于「四大发明」的观点是否客观、准确？" 下的回答得到了201个赞同,我还没有赞同
```


### 获取用户
```Python
import ZhihuVAPI as zhihu
person = zhihu.People('zhihuadmin')

for p in person.followers(count=5): # 粉丝
    p: zhihu.People  # 让 IDE 智能提示
    print(p.name)

for a in person.answers(count=5): # 答案
    a: zhihu.Answer  # 让 IDE 智能提示
    print(a.voteup_count)

for ar in person.articles(count=5): #文章
    ar: zhihu.Article  # 让 IDE 智能提示
    print(ar.voteup_count)

for m in person.msgs(count=5): #私信
    print(m)

for pin in person.pins(count=5): #想法
    pin: zhihu.Pin  # 让 IDE 智能提示
    print(pin.voteup_count)


person.block() # 屏蔽
person.unblock() # 取消屏蔽(以此类推)
person.send('你好,我是{zhihu.self.name}') # 发送私信
```

### 获取专栏
```Python
import ZhihuVAPI as zhihu
column = zhihu.Column('cheezpython')
print(column.title)
for ar in column.articles():
    ar: zhihu.Article  # 让 IDE 智能提示
    print(f'{ar.title} 一共有 {ar.voteup_count} 个赞')


for p in column.coauthors():
    p: zhihu.People  # 让 IDE 智能提示
    print(f'{p.name} 他有 {p.voteup_count} 个赞')

column.follow() #关注

```


### 获取文章
```Python
import ZhihuVAPI as zhihu
ar=zhihu.Article('https://zhuanlan.zhihu.com/p/39747259')
for p in ar.voters(count=5):
    p:zhihu.People # 让 IDE 智能提示
    print(p.name)
    if p.is_waterman():
        print(f'{p.name} 是水军')
print(f'这篇文章 "{ar.title}" 得到了{ar.voteup_count}个赞同,我{"已经赞同了"if ar.is_voting else "还没有赞同" }')

ar.down() #反对
ar.undown() #取消反对(以此类推)
ar.vote() # 赞同
ar.thank() # 感谢
# ar.collect([zhihu.Collection('你自己的收藏夹 ID'),])

```

### 获取收藏夹
```Python
import ZhihuVAPI as zhihu 
co = zhihu.Collection('https://www.zhihu.com/collection/62217998')
print(f'这个收藏夹的名字是{co.title}')
for ct in co.contents(count=10):
    if ct.type == 'answer':
        print(f'{ct.content.excerpt}\n') 
```


### 获取问题
```Python
import ZhihuVAPI as zhihu 
```
