
## 大话爬虫的基本套路   
---

![图片](http://blog.thankbabe.com/imgs/spider.jpg?v=1)

### 什么是爬虫？

`网络爬虫`也叫`网络蜘蛛`，如果把互联网比喻成一个蜘蛛网，那么蜘蛛就是在网上爬来爬去的蜘蛛，爬虫程序通过请求url地址，根据响应的内容进行解析采集数据，
比如：如果响应内容是html，分析dom结构，进行dom解析、或者正则匹配，如果响应内容是xml/json数据，就可以转数据对象，然后对数据进行解析。

---

### 有什么作用？ 

通过有效的爬虫手段批量采集数据，可以降低人工成本，提高有效数据量，给予运营/销售的数据支撑，加快产品发展。 

---

### 业界的情况

目前互联网产品竞争激烈，业界大部分都会使用爬虫技术对竞品产品的数据进行挖掘、采集、大数据分析，这是必备手段，并且很多公司都设立了`爬虫工程师`的岗位

---

### 合法性   

爬虫是利用程序进行批量爬取网页上的公开信息，也就是前端显示的数据信息。因为信息是完全公开的，所以是合法的。其实就像浏览器一样，浏览器解析响应内容并渲染为页面，而爬虫解析响应内容采集想要的数据进行存储。

---    

### 反爬虫

爬虫很难完全的制止，道高一尺魔高一丈，这是一场没有硝烟的战争，码农VS码农   
反爬虫一些手段：
* 合法检测：请求校验(useragent，referer，接口加签名，等)
* 小黑屋：IP/用户限制请求频率，或者直接拦截
* 投毒：反爬虫高境界可以不用拦截，拦截是一时的，投毒返回虚假数据，可以误导竞品决策
* ... ...

---   

### 爬虫基本套路

* 基本流程
    * 目标数据
    * 来源地址
    * 结构分析
    * 实现构思
    * 操刀编码
* 基本手段
    * 破解请求限制
        * 请求头设置，如：useragant为有效客户端
        * 控制请求频率(根据实际情景)
        * IP代理
        * 签名/加密参数从html/cookie/js分析
    * 破解登录授权
        * 请求带上用户cookie信息
    * 破解验证码
        * 简单的验证码可以使用识图读验证码第三方库
* 解析数据
    * HTML Dom解析
        * 正则匹配，通过的正则表达式来匹配想要爬取的数据，如：有些数据不是在html 标签里，而是在html的script 标签的js变量中
        * 使用第三方库解析html dom，比较喜欢类jquery的库
    * 数据字符串
        * 正则匹配(根据情景使用) 
        * 转 JSON/XML 对象进行解析



---   

### python爬虫

* python写爬虫的优势
    * python语法易学，容易上手
    * 社区活跃，实现方案多可参考
    * 各种功能包丰富
    * 少量代码即可完成强大功能
* 涉及模块包
    * 请求
        * `urllib`
        * `urllib2`
        * `cookielib`
    * 多线程
        * `threading`
    * 正则
        * `re`
    * json解析
        * `json`
    * html dom解析
        * `pyquery`
        * `beautiful soup`
    * 操作浏览器
        * `selenium`
        
---

### 实例解析   

**斗鱼主播排行**

* 目标数据
    * 获取排行榜主播信息
* 来源地址
    * **[排行榜地址]**
        * https://www.douyu.com/directory/rank_list/game
    * **[主播房间地址]**
        * https://www.douyu.com/xxx
            * xxx=房间号  
* 结构分析
    * 通过抓包 **[排行榜地址]**，**[主播房间地址]**   （谷歌调试network/charles/fiddler）
        * 获得排行数据接口：https://www.douyu.com/directory/rank_list/game
            * 参数确认(去掉不必要参数)
            * cookie确认(去掉不必要cookie)
            * 模拟请求(charles/fiddler/postman)
        * 获得主播房间信息数据
            * 发现$ROOM是主播房间信息，在页面的script标签的js变量中，可使用正则工具写表达式去匹配
* 实现构思
    * 通过请求 **[主播排行接口]** 获取 **[排行榜数据]** 
    * **[排行榜数据]** 中有主播房间号，可以通过拼接获得 **[主播房间地址]**
    * 请求 **[主播房间地址]** 可以获得 **[$ROOM信息]** ，解析可以获得主播房间信息
* 操刀编码

> 申明：此例子仅作为爬虫学习DEMO，并无其他利用

---

基于python实现爬虫学习基础demo

```python
def douyu_rank(rankName, statType):
    '''
        斗鱼主播排行数据抓取
        [数据地址](https://www.douyu.com/directory/rank_list/game)

        * `rankName` anchor(巨星主播榜),fans(主播粉丝榜),haoyou(土豪实力榜),user(主播壕友榜)
        * `statType` day(日),week(周),month(月)
    '''
    if not isinstance(rankName, ERankName):
        raise Exception("rankName 类型错误，必须是ERankName枚举")
    if not isinstance(statType, EStatType):
        raise Exception("statType 类型错误，必须是EStatType枚举")

    rankName = '%sListData' % rankName.name
    statType = '%sListData' % statType.name
    # 请求获取html源码 
    rs = rq.get(
        "https://www.douyu.com/directory/rank_list/game",
        headers={'User-Agent': 'Mozilla/5.0'})
    # 正则解析出数据
    mt = re.search(r'rankListData\s+?=(.*?);', rs, re.S)
    if (not mt):
        print u"无法解析rankListData数据"
        return
    grps = mt.groups()
    # 数据转json
    rankListDataStr = grps[0]
    rankListData = json.loads(rankListDataStr)
    dayList = rankListData[rankName][statType]
    # 修改排序
    dayList.sort(key=lambda k: (k.get('id', 0)), reverse=False)
    return dayList


def douyu_room(romm_id):
    '''
        主播房间信息解析
        [数据地址](https://www.douyu.com/xxx)
        'romm_id' 主播房号
    '''
    rs = rq.get(
        ("https://www.douyu.com/%s" % romm_id),
        headers={'User-Agent': 'Mozilla/5.0'})
    mt = re.search(r'\$ROOM\s+?=\s+?({.*?});', rs, re.S)
    if (not mt):
        print u"无法解析ROOM数据"
        return
    grps = mt.groups()
    roomDataStr = grps[0]
    roomData = json.loads(roomDataStr)
    return roomData
    
def run():
    '''
        测试爬虫
    '''
    datas = douyu_rank(ERankName.anchor, EStatType.month)
    print '\r\n主播排行榜：'
    for item in datas:
        room_id = item['room_id']
        roomData = douyu_room(room_id)
        rommName = None
        if roomData is not None:
            rommName = roomData['room_name']
        roomInfo = (u'房间(%s):%s' % (item['room_id'], rommName))
        print item['id'], item[
            'nickname'], roomInfo, '[' + item['catagory'] + ']'


run()

```
---

```
运行结果：

主播排行榜：

无法解析ROOM数据
1 冯提莫 房间(71017):None [英雄联盟]
2 阿冷aleng丶 房间(2371789):又是我最喜欢的阿冷ktv时间～ [英雄联盟]
3 胜哥002 房间(414818):胜哥：南通的雨下的我好心累。 [DNF]
4 White55开解说 房间(138286):卢本伟五五开 每天都要很强 [英雄联盟]
5 东北大鹌鹑 房间(96291):东北大鹌鹑 宇宙第一寒冰 相声艺术家！ [英雄联盟]
6 老实敦厚的笑笑 房间(154537):德云色 给兄弟们赔个不是 [英雄联盟]
7 刘飞儿faye 房间(265438):刘飞儿  月底吃鸡 大吉大利 [绝地求生]
8 pigff 房间(24422):【PIGFF】借基地直播，没OW [守望先锋]
9 云彩上的翅膀 房间(28101):翅：还是抽天空套刺激！ [DNF]
10 yyfyyf 房间(58428):无尽的9月，杀 [DOTA2]

# 冯提莫 房间做周年主题，解析会有问题

```

[Demo源码地址](https://github.com/SFLAQiu/SpiderDemo)


---





## 大话爬虫的实践技巧
---

![爬虫与反爬虫间的对决](http://blog.thankbabe.com/imgs/spider-2.jpg?v=1)
> 图1-意淫爬虫与反爬虫间的对决


#### **数据的重要性**
如今已然是大数据时代，数据正在驱动着业务开发，驱动着运营手段，有了数据的支撑可以对用户进行用户画像，个性化定制，数据可以指明方案设计和决策优化方向，所以互联网产品的开发都是离不开对数据的收集和分析，数据收集的一种是方式是通过上报API进行自身平台用户交互情况的捕获，还有一种手段是通过开发爬虫程序，爬取竞品平台的数据，后面就重点说下爬虫的应用场景和实践中会遇到的问题和反反爬虫的一些套路与技巧。


---

#### **应用场景**
* 互联网平台，偏向销售公司，客户信息的爬取
    * 客户信息的爬取可以释放销售人员寻找客户资源的时间，提高销售对市场开发的效率
    * 爬取相关平台上的客户信息，上报到CRM管理系统，提供给销售人员进行开发
* 资讯爬取并应用到平台业务中
    * 经常浏览资讯的时候会发现其实很多平台的热门资讯内容都很相似，尊重版权的平台，会标明来源出处
    * 爬取资讯信息，应用到资讯业务中，可以减轻资讯内容编辑人员的压力，如果不需要创造自己的内容，也可全部托管给程序AI运营
* 竞品公司重要数据挖掘分析与应用
    * 竞品平台重要业务数据，如：汽车X家的车型信息，X哪儿的酒店信息，返X网的商品信息，... ...
    * 爬取竞品重要数据，对数据进行筛选和处理，然后投入业务中展示，增加这块业务数据量，减轻这块资源的运营编辑的压力
* ... ...

---

#### **爬虫开发**
* python开发爬虫(推荐)
    * 入门也比较简单，代码短小精干，各种便于爬虫开发的模块和框架
* 其他语言
    * 很多语言也都可以开发爬虫，但是均都不是很全面，根据实际技术栈和开发场景去使用，语言只是工具，思路才是通用的 

---

#### **爬虫必备技巧**   
> 做爬虫开发，需要对WEB这块有相对全面深入的理解，这样后面遇到反爬虫才能得心应手，见招拆招

* 了解HTML
    * 会使用HTML标签构造页面，知道如何解析出DOM里标签，提取想要的数据内容
* 了解CSS
    * 了解CSS，会解析出样式里的数据内容
* 了解JS
    * 基本JS语法，能写能读懂，并了解JS库：Jquery，Vue 等，可以对使用开发者工具调试JS
* 了解JSON
    * 了解JSON数据，会序列化和反序列化数据，通过解析JSON对象获取数据内容
* 了解HTTP/HTTPS
    * 能够分析请求信息和响应信息，可以通过代码构造请求
* 会正则解析
    * 通过正则匹配出符合规则的字符串，提取想要的数据内容 
* 会数据库操作
    * 通过数据库操作对爬取数据进行存储，如：MYSQL语法
* 会使用抓包工具
    * 浏览器F12开发者调试工具(推荐：谷歌),Network(网络)栏目可以获取抓包信息
    * 工具：Charles，Fiddler (可抓包HTTPS，抓包APP)
    * 通过抓包工具可以过滤出数据接口或者地址，并且分析请求信息和响应信息，定位数据所在的字段或者HTML标签
* 会使用开发者工具
    * 浏览器F12开启开发者工具
    * 需要会使用开发者工具调试HTML，CSS，JS
* 会模拟请求
    * 工具：Charles，Fiddler，Postman
    * 通过模拟请求，分析出请求需要那些必要的信息，如：参数，COOKIE，请求头，懂得怎么模拟请求就知道编码的时候如何去构造
* 能定位数据
    *  数据在API中：前端/原生APP请求数据API，API返回数据大部分是JSON格式，然后渲染展示
    *  数据在HTML中：查看页面HTML源代码，如果源代码里有想要获取的数据，就说明在服务端已经绑定好数据在HTML里
    *  数据在JS代码中：查看页面HTML源代码，如果获取数据不在HTML里，又没有请求数据API，可以看下数据是不是绑定到JS变量里
* 会部署
    * 可以部署到Windows或者Linux服务器，使用工具进行爬虫进程监控，然后进行定时轮训爬取

---

#### **反爬虫对抗技巧**
> 反爬虫可以分为``服务端限制``和``前端限制``   
>``服务端限制``：服务器端行请求限制，防止爬虫进行数据请求   
>``前端限制``：前端通过CSS和HTML标签进行干扰混淆关键数据，防止爬虫轻易获取数据   

**设置请求头（``服务端限制``）**
* Referer
* User-Agent
* ... ...

**签名规则（``服务端限制``）**    
* 如果是JS发起的请求，签名规则可以在JS函数中找到，然后再根据规则去构造签名
* 如果是APP发起的请求，可能是前端调用原生封装的方法，或者原生发起的，这个就比较无解，需要反编译APP包，也不一定能成功

**延迟，或者随机延迟（``服务端限制``）**   
* 如果请求被限制，建议可以试试请求延迟，具体延迟xxx毫秒/x秒，根据实际情况设定合适的时间 

**代理IP（``服务端限制``）**   
* 如果延迟请求还是被限制，或者需要延迟很长时间才不会被限制，那就可以考虑使用代理IP，根据实际场景与限制的规律去运用，一般只要被限制的时候就切换请求的代理IP，这样就基本可以绕过限制
* 目前有很多收费的代理IP服务平台，有各种服务方式，具体可以搜索了解下，费用一般都在可以接受的范围

**登录限制（``服务端限制``）**   
* 请求带上登录用户的COOKIE信息
* 如果登录用户COOKIE信息会在固定周期内失效，那就要找到登录接口，模拟登录，存储COOKIE，然后再发起数据请求，COOKIE失效后重新这个步骤

**验证码限制（``服务端限制``）**   
* 简单验证码，对图片里的字母或者数字进行识别读取，使用识图的模块包可以实现
* 复杂验证码，无法通过识图识别，可以考虑使用第三方收费服务     

**CSS/HTML混淆干扰限制（``前端限制``）**    
> 前端通过CSS或者HTML标签进行干扰混淆关键数据，破解需要抽样分析，找到规则，然后替换成正确的数据    

**1 .**  font-face，自定义字体干扰   

如列子：[汽车X家论帖子](https://club.autohome.com.cn/bbs/thread/f79816f3918a7577/52582709-1.html)，[猫X电影电影评分](http://maoyan.com/films/1182552)


```html
<!--css-->
<!--找到：//k3.autoimg.cn/g13/M05/D3/23/wKjByloAOg6AXB-hAADOwImCtp047..ttf--> 
<style>
    @font-face {font-family: 'myfont';src: url('//k2.autoimg.cn/g13/M08/D5/DD/wKgH41oAOg6AMyIvAADPhhJcHCg43..eot');src: url('//k3.autoimg.cn/g13/M08/D5/DD/wKgH41oAOg6AMyIvAADPhhJcHCg43..eot?#iefix') format('embedded-opentype'),url('//k3.autoimg.cn/g13/M05/D3/23/wKjByloAOg6AXB-hAADOwImCtp047..ttf') format('woff');}
</style>

<!--html-->
<!--会员招募中-->
<div>&nbsp;Mercedes&nbsp;C+&nbsp;会员招募<span style='font-family: myfont;'>&#xf159;</span></div>

<!--
    从html中获取【html中文编码】=&#xf159
    然后解析ttf文件得到【ttf中文编码】列表
    匹配发现【ttf中文编码】=uniF159可以与【html中文编码】=&#xf159匹配，在第7个，第7个中文就是"中"
    （抽样分析会发现ttf中中文位置是固定的，中文编码是动态变化的，所以只要映射出【ttf中文编码】索引就可以知道中文字符了）
-->

```
破解思路：      
找到ttf字体文件地址，然后下载下来，使用font解析模块包对ttf文件进行解析，可以解析出一个字体编码的集合，与dom里的文字编码进行映射，然后根据编码在ttf里的序号进行映射出中文   

> 可以使用FontForge/FontCreator工具打开ttf文件进行分析

---

**2 .**  伪元素隐藏式   

通过伪元素来显示重要数据内容   
如例子：[汽车X家](https://car.autohome.com.cn/config/series/3170.html)  

```html
<!--css-->
<style>
.hs_kw60_configod::before {
    content: "一汽";
}
.hs_kw23_configod::before {
    content: "大众";
}
.hs_kw26_configod::before {
    content: "奥迪";
}
</style>

<!--html-->
<div>
    <span class="hs_kw60_configod"></span>
    -
    <span class="hs_kw23_configod"></span>
    <span class="hs_kw26_configod"></span>
</div> 

```
破解思路：      
找到样式文件，然后根据HTML标签里class名称，匹配出CSS里对应class中content的内容进行替换   

---   

**3 .**  backgroud-image  

通过背景图片的position位置偏移量，显示数字/符号，如：价格，评分等    
根据backgroud-postion值和图片数字进行映射   

---

**4 .**  html标签干扰     

通过在重要数据的标签里加入一些有的没的隐藏内容的标签，干扰数据的获取   
如例子：[xxIP代理平台](http://www.goubanjia.com)   

```html
<!--html-->
<td class="ip">
    <p style="display:none;">2</p>
    <span>2</span>
    <span style="display:inline-block;"></span>
    <div style="display: inline-block;">02</div>
    <p style="display:none;">.1</p>
    <span>.1</span>
    <div style="display:inline-block;"></div>
    <span style="display:inline-block;"></span>
    <div style="display:inline-block;">09</div>
    <span style="display: inline-block;">.</span>
    <span style="display:inline-block;">23</span>
    <p style="display:none;">7</p>
    <span>7</span>
    <p style="display:none;"></p>
    <span></span>
    <span style="display: inline-block;">.</span>
    <div style="display: inline-block;"></div>
    <p style="display:none;">3</p>
    <span>3</span>
    <div style="display: inline-block;">5</div>:
    <span class="port GEA">80</span>
</td>
<!--js-->
<script>
    $(".ip:eq(0)>*:hidden").remove()
    $(".ip:eq(0)").text()
</script>
<!--
    输出：202.109.237.35:80
    通过移除干扰标签里有display:none隐藏标签，然后再获取text就不会有干扰的内容了
-->
```
破解思路：      
过滤掉干扰混淆的HTML标签，或者只读取有效数据的HTML标签的内容

![看穿一切](http://blog.thankbabe.com/imgs/kcyq.jpg?v=1)
> ... ... (反爬虫脑洞有多大，反反爬虫拆招思路就有多淫荡)

---

**防止投毒**    

* 有些平台发现爬虫后并不会进行限制封杀，而是给爬虫提供误导的数据，影响竞品公司进行错误的决策，这就是投毒
* 为了防止被投毒，需要对数据进行抽样校验


---

#### **总结**    

1. 目前大部分中小平台对防御爬虫的意识还比较薄弱，促使了爬虫的盛行，通过爬虫可以用比较小的代价，获取更大的利益
2. 竞品数据的挖掘分析与应用对于业务增长有着举足轻重的作用，爬虫开发对于互联网产品公司的来说是个必不可少的技术
3. 当前并没有一种可以完全避免爬虫的技术，所以添加反爬虫策略只是增加了一定的难度门槛，只要拆招技术够硬还是可以被突破翻越
4. 反爬虫和反反爬虫是技术之间的较量，这场没有硝烟的战争永不停息。（程序员何必为难程序员）



---

#### **供参考代码**


> font解析 C#和Python实现

* C#

```csharp
/// 需要引入PresentationCore.dll
private void Test() {
            string path = @"F:\font.ttf";
            //读取字体文件             
            PrivateFontCollection pfc = new PrivateFontCollection();
            pfc.AddFontFile(path);
            //实例化字体
            Font f = new Font(pfc.Families[0], 16);
            //设置字体
            txt_mw.Font = f;

            //遍历输出
            var families = Fonts.GetFontFamilies(path);
            foreach (System.Windows.Media.FontFamily family in families) {
                var typefaces = family.GetTypefaces();
                foreach (Typeface typeface in typefaces) {
                    GlyphTypeface glyph;
                    typeface.TryGetGlyphTypeface(out glyph);
                    IDictionary<int, ushort> characterMap = glyph.CharacterToGlyphMap;
                    var datas = characterMap.OrderBy(d => d.Value).ToList();
                    foreach (KeyValuePair<int, ushort> kvp in datas) {
                        var str = $"[{kvp.Value}][{kvp.Key}][{(char)kvp.Key}]\r\n";
                        txt_mw.AppendText(str);
                    }
                }
            }

        }
```
* python

```python
# pip install TTFont
from fontTools.ttLib import TTFont
from fontTools.merge import *
me = Merger()
font = TTFont('./font.ttf')
cmaps = font.getBestCmap()
orders = font.getGlyphOrder()
# font.saveXML('F:/1.xml')
print cmaps
print orders


```


---

#### **自我推荐**

* 爬虫入门可以参考我的另一篇文章：[（大话爬虫的基本套路）](http://blog.thankbabe.com/2017/09/25/spider/)
* 爬虫入门代码可以参考我的Gtihub项目[（SpiderDemo）](https://github.com/SFLAQiu/SpiderDemo)

 
---

#### **供参考资料**

* [反击爬虫，前端工程师的脑洞可以有多大？](http://imweb.io/topic/595b7161d6ca6b4f0ac71f05)
* [有哪些有趣的反爬虫手段？](https://www.zhihu.com/question/58342241)


