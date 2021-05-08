# 記者快抄

## About DataBase

因為一些隱私權問題，我沒有釋出使用的資料庫並註解掉了 code 中有用到 database 的部分。

<strike>現在資料庫是從所有 PTT 八卦版的文章建出來的，並用其搜尋和文章相關的圖片使每個產生的新聞都有相對應的圖片。因為我還在改良其他部分的演算法，所以現在這部分是直接用文章的關鍵字 query 資料庫找到類似的文章標題後回傳結果。如果你對資料庫與搜尋演算法的設計與改進有興趣，歡迎聯絡我們或是直接送 pull request，謝謝。</strike>

現在我使用 ["Reading Wikipedia to Answer Open-Domain Questions", ACL 2017](https://github.com/facebookresearch/DrQA) 提供的 search engine 演算法來找適合的圖片。想使用的人需要

1. [clone 我寫的 interface](https://github.com/exe1023/DrQA)
2. 把自己爬的 ptt 文章丟進去

## About Auto Generated Articles

現在我是使用 TextRank 抓出內文重點與重要回文後將其填進一些常見記者抄 PTT 文章的格式來產生新聞。不依賴 template 自動產生新聞的部分我們有嘗試過兩個 model， training data 為從蘋果, 自由時報等新聞網站爬下來約 10 萬篇新聞。

- [“Abstractive Sentence Summarization with Attentive Recurrent Neural Networks”, NAACL 2016](https://github.com/facebookarchive/NAMAS): 容易 overfitting 且無法處理中文因斷詞所以 vocabulary size 太大的問題
- ["Get To The Point: Summarization with Pointer-Generator Networks", ACL 2017](https://github.com/exe1023/pointer-generator): 現在正在嘗試的 model，處理 OOV 的能力很不錯，但是產生出來的摘要在文法上略嫌不通順，可能是 training data 的問題。

同樣因為一些著作權問題不太方便公開 training data。如果你對自動產生文章有心得或是想要提供中文文章與摘要的 data，歡迎和我們聯絡。

Update: 現在我使用一份叫做 [CIRB010](kslab.km.nccu.edu.tw/xms/read_attach.php?id=150) 的 data，實際測試在 pointer-generator networks 上後結果還算能接受，但是文法不通順的問題仍待解決。

## Setup Environment

請更改 `setup.sh` 裡面的路徑並 source 它。

- `PYTHONPATH`: 這個 repository 的路徑
- `JIEBA_DATA`: jieba 資料中 extra_dict 的路徑，用於斷詞。
- `DATA`: 你想把爬下來的 PTT 資料放哪，舉例來說從八卦版爬下來的資料會放在 `$DATA/raw/Gossiping/`
- `TEMPLATE`: 你把新聞的 template 放在哪裡。
- `POSTS`: 你想把產生的新聞放在哪裡。


## To Run

`python3 journalist`

<strike>會每個小時自動執行一次爬 PTT 並產生新聞。</strike>

後來想想還是請大家自己加 crobtab 跑比較穩定

## Issues

- 更好看的前端
- Code 很多部分因為當初設計不良而做了不必要的運算，需要重新整理。
- <strike>DataBase 與搜尋圖片演算法的改良</strike>
- 自動產生內文而不依賴 template

## Related projects

- [PTT-Chat-Generator](https://github.com/zake7749/PTT-Chat-Generator): `util/ptt_filter.py` 的原型
- [ptt-web-crawler](https://github.com/jwlin/ptt-web-crawler): `util/crawler` 的原型
- [TextRank4ZH](https://github.com/letiantian/TextRank4ZH): 中文 TextRank 的實作
