# Word2Vec

有一對情侶正為晚餐不知道要吃什麼而煩惱...
- 男：寶貝，晚餐想吃什麼？
- 女：都可以呀！
- 男：我們去吃久久神鍋好不好？
- 女：很熱欸～
- 男：那去轉角吃涼麵怎麼樣？
- 女：那又沒有冷氣吹～
- 男：找一家有帥哥店員的好不好？
- 女：好！讓我們去有帥哥氣氛又好的餐廳吧～
- 男：:joy::joy::joy:

男友不禁想問，為什麼找一家餐廳會這麼困難呢？氣氛要好又要有帥哥店員的餐廳到底在哪裡？換個角度想，炎炎夏日，為什麼找不到一家主打充滿陽光、沙灘、比基尼這種夏日風情的餐廳？我們常常在餐廳享受的不只是食物，而是享受餐廳營造的氣氛，餐廳營造的可以是一個人與食物的寧靜對話，可以是三五好友歡聚的燒烤派對，當然也可以是家人一同聚餐的溫馨。

##### 這是一篇關於如何透過情境搜尋餐廳的文章，可以直接往下看結果。

# 專案緣起
不知道大家最近有沒有看到一篇 PTT 上的文章？作者對約 X 信進行語義分析，內容專業到讓人無法直視，看的當下就覺得：哇！原來語意分析還有這種應用的方式！程式語言是用來幫忙解決問題的好工具，能把它應用到生活大小事上真的很棒！這篇文章燃起了我心中對文字探勘的熱情，剛好最近有個比賽會需要這方面的技術~~（才不是因為 PIXNET HACKTHON 的比賽入選機率極低而抱著不服輸的心態呢！）~~

由於本身對資料分析很有興趣，尤其是圖像分析和語意分析，因為他們能夠應用的範疇很廣，而且已經不知不覺地影響著這個世界的運行，例如無人車駕駛、Alphago、SkyRec、IBM Waston 等等。這個領域的知識又深又廣，既然要朝這個方向持續邁進，平常就要有所累積。公司正在朝著將情境與餐廳建立連結轉型，正好和我有興趣的領域有所重疊，所以對於這個專案我也有比平常玩玩還認真的使命感，於是便花了星期六和星期日的上午把做了一些有趣的東西。

# 工具介紹
大多數的公司使用 Solr, Elasticsearch 建置搜尋引擎，有些還會直接嵌入 Google 搜尋列，前者運用的方法是 TF-IDF，後者就是借助 Google 強大的搜尋演算法。但是沒有一種方法是完美的，如果今天下的關鍵字比較多，想要透過「酒館」和「義式」搜尋餐廳，就會發現沒有我要的結果，但是這兩個關鍵字如果分開來就都能得到結果，事實上，這兩個關鍵應該是有著相關性的，但是透過 TF-IDF 卻無法知道。如果可以將這兩個關鍵字的特性相加之後得到一個新的特性，再用新的特性去尋找最相近的餐廳就太棒了！

這就是本篇文章會運用到的概念，這個概念的基礎是 Word2Vec，它很適合用來對文字、圖像、聲音進行模糊搜尋，由於運作原理一言難盡~~（死線要到啦）~~，我就直接說重點：透過訓練將詞會投影到高維度的向量空間，相近的詞彙有相近的詞向量。

而詞向量有個特性是可以透過相加減獲得有趣的結果，例如：`國王 - 男人 + 女人 ~= 皇后`。

# 操作流程
**1. 收集連結**：收集公司合作餐廳的食記連結，並且把餐廳資訊與餐廳食記連結輸出成文字檔，檔案內沒有提供連結。

執行`python getUrl.py`

**2. 爬網站 & 擷取資訊**：過濾非 Pixnet 連結透過 requests 結合 multiprocessing 爬網站的 Html。使用 PyQuery 擷取網站標題與內容，並且存到 Sqlite。

執行`python getBlog.py`

**3. 斷詞**：使用 Jieba 對文字進行預處理，轉換成 Word2Vec 能夠訓練的格式。

執行`python cut.py`

**4. 訓練**：透過在 gensim 中實作的 Word2Vec，設定參數對資料進行訓練，產生詞向量與模型。（直接使用 52nlp 提供的檔案）

執行`python train_word2vec_model.py training_sentence.txt model_name.model vector_name.vector`

# 注意事項

在專案中主要遇到兩個困難：
- 處理中文字遇到的編碼問題：Unicode、UTF-8 與 ASCII 之間錯綜複雜的關係，不同套件的輸入的接口要求的編碼可能不一樣。
- 使用 multiprocess 要小心：原因還沒有弄清楚，只要在 `the_function` 裡面加入了 pyquery 或是 sqlite 的 function 就會 crash，但是放 requests 就沒事。

```python
from multiprocessing import Pool
p = Pool(5)
results = p.map(the_fucntion, inputs)
```
# 專案成果
本次訓練的文章共有 5899 篇食記，訓練結果為 35962 個 500 維的詞向量。由於訓練數量蠻小的，所以訓練速度很快。

1. 先載入 gensim 套件與剛剛訓練好的 model
```python
import gensim
# print result
def ps(result):
  if result:
  for e in result:
    print e[0], e[1]
# load fresh model
model = gensim.models.Word2Vec.load("articles_rname.model")
```
接下來就可以開始玩啦！我很愛吃水餃，但是昨天才剛吃過，有沒有什麼類似的料理可以推薦給我呢？
```python
>>> result = model.most_similar(u"水餃",topn=5)
>>> ps(result)
'叉燒包' 0.732798755169
'蔥油餅' 0.717539072037
'三鮮' 0.706256866455
'餃子' 0.703786492348
'包子' 0.694874405861
```
如果我們想要知道泰式之於瓦城，就像是義式之於什麼餐廳，就可以這樣計算：  瓦城 - 泰式 + 義式 =  ?
```python
>>> result = model.most_similar(positive=u"義式 瓦城".split(" "), negative=[u"泰式"],topn=5)
>>> ps(result)
'義大利餐廳' 0.754565596581
'NINI' 0.750810861588
'帕莎' 0.707847952843
'廚子市場' 0.703588843346
'蒂娜' 0.700719475746
```
得出來的結果是在義式餐廳中，風格與瓦城最像的前五名餐廳。但是，在這裡我們發現了一個問題，「義大利餐廳」是哪一家？答案是義大皇家酒店的義大利餐廳，NINI 呢？原來是 Le NINI 樂尼尼義式餐廳，帕莎和蒂娜應該要合起來叫做帕蒂娜莎，產生問題的原因是之前在處理餐廳名稱的時候不夠謹慎。目前會先用 mapping 的方式找回原本的餐廳名稱。

接下來我們要進入重頭戲，情境搜尋了！
```python
>>> result = model.most_similar(u"夏天 海灘 餐廳".split(" "), topn=5)
>>> ps(result)
'皮椅' 0.694285988808
'LOUNGE' 0.688326239586
'HALEAKALA' 0.68235886097
'仿舊' 0.674678146839
'小徑' 0.662850260735
```
我們想要的結果是根據情境找到符合的餐廳，但是得出的結果只有2家餐廳，2個名詞，1個形容詞。因此我們必須建立涵蓋訓練集餐廳的 list，把這個 list 的詞向量拿出來與我們想要搜尋的情境詞向量進行相似度的計算。特別感謝 jimgoo 提供的 `most_similar_in_list` function，讓我可以直接使用。
```python
>>> print(rname_list[:5])
[u'Follow', u'Bellini', u'TABLE', u'Taverna', u'90']
>>> print(mapping(rname_list[:5]))
[u'Follow Lady 法蕾蒂', u'Bellini Pasta Pasta', u'TABLE JOE 喬桌子廚房', u'Taverna De  Medici 梅帝騎小酒館', u'90 a la sante 酒食歐風朝']

>>> result = model.most_similar_in_list(u"夏天 海灘".split(" "), topn=5, restrict_vocab=rname_list)
>>> ps([[mapping(rname[0]), rname[1]] for rname in result])
'VG Cafe & Bistro' 0.650945961475
'HALEAKALA 夏威夷酒吧餐廳' 0.615895032883
'Eslite Tea Room' 0.599678635597
'URBAN331-台北慕軒飯店' 0.579266548157
'Destino 妳是我的命運' 0.57857131958

>>> result = model.most_similar_in_list(u"消暑 下午 茶".split(" "), topn=3, restrict_vocab=rname_list)
>>> ps([[mapping(rname[0]), rname[1]] for rname in result])
'Caldo Cafe咖朵咖啡' 0.47723197937
'Eslite Tea Room' 0.468698769808
'H-Bar' 0.460396289825

>>> result = model.most_similar_in_list(u"正妹 店員".split(" "), topn=3, restrict_vocab=rname_list)
>>> ps([[mapping(rname[0]), rname[1]] for rname in result])
'etage15-高雄Hotel dua' 0.468320250511
'Sunny Cafe' 0.447554886341
'Kevin Coffee' 0.418976008892

>>> result = model.most_similar_in_list(u"音樂 悠閒".split(" "), topn=3, restrict_vocab=rname_list)
>>> ps([[mapping(rname[0]), rname[1]] for rname in result])
'Mammoth lounge' 0.670462846756
'HALEAKALA 夏威夷酒吧餐廳' 0.626639544964
'RUBY CAFE' 0.6229159832

>>> result = model.most_similar_in_list(u"工程師".split(" "), topn=3, restrict_vocab=rname_list)
>>> ps([[mapping(rname[0]), rname[1]] for rname in result])
'American Steakhouse' 0.802481234074
'i sweet' 0.785791814327
'Silk Road Feast 絲路宴餐廳' 0.776082456112

>>> result = model.most_similar_in_list(u"求婚 紀念".split(" "), topn=3, restrict_vocab=rname_list)
>>> ps([[mapping(rname[0]), rname[1]] for rname in result])
'Ton Up Cafe' 0.62010884285
'TABLE JOE 喬桌子廚房' 0.608335494995
'URBAN331-台北慕軒飯店' 0.606325864792

>>> result = model.most_similar_in_list(u"酒 餐廳 美式 跨年".split(" "), topn=3, restrict_vocab=rname_list)
>>> ps([[mapping(rname[0]), rname[1]] for rname in result])
'bar & restaurant a³ 新義式餐廳' 0.665651142597
'MW 時尚義法料理&酒品' 0.665459275246
'Le Bar 吧 戶外餐廳' 0.644170224667
```
這些結果很有趣，有空再來分析～

# 未來方向
- 餐廳食記收集的數量要夠多夠平均，不然會影響到訓練結果
- 換成訓練餐廳評論結果可能會更精準
- 將多維向量降維，可以拿來做 clustering，另外可以畫個 2D 的圖
- 文字處理不容易但是很重要，還有許多可以優化的地方
- 多國語言搜尋也能配合 Word2Vec

# 參考資源
Python 有很多好用的套件，像是中文斷詞有 jieba，word2vec 有 gensim，用起來上手很快，而且還有熱心的大大們不吝分享與教學。
- 謝謝 Google 大神
- 謝謝 Mark -> 提供的 API
- 謝謝 亮亮 [中文搜尋經驗分享](https://blog.liang2.tw/2015Talk-Chinese-Search/) -> 非常精彩，讓我對 NLP 產生了莫大的興趣 
- 謝謝 Shaform [用中文資料測試 word2vec](http://city.shaform.com/blog/2014/11/04/word2vec.html) -> 簡潔易懂 
- 謝謝 52nlp [中英文维基百科语料上的Word2Vec实验](http://www.52nlp.cn/%E4%B8%AD%E8%8B%B1%E6%96%87%E7%BB%B4%E5%9F%BA%E7%99%BE%E7%A7%91%E8%AF%AD%E6%96%99%E4%B8%8A%E7%9A%84word2vec%E5%AE%9E%E9%AA%8C) -> gensim word2vec 教學完整，logger 好帥 
- 謝謝 jimgoo 在 gensim 實作的 [most_similar_in_list](https://github.com/RaRe-Technologies/gensim/pull/481) -> 節省很多時間
- 謝謝 mrvege [處理標點符號的方法](https://gist.github.com/mrvege/2ba6a437f0a4c4812f21)
- 謝謝 Hokusai [[討論] 有男生收過騷擾/約砲信嗎](https://www.ptt.cc/bbs/sex/M.1467099969.A.1D1.html) -> 激起了我對 NLP 的無限想像 

---
有什麼建議或是需要其他資訊都歡迎與我聯繫！
> **Paris Tsai**  [paristsaiswing@gmail.com](mailto:paristsaiswing@gmail.com)
