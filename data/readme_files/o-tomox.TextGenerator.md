# Text Generator
マルコフ連鎖を使った文章自動生成プログラム

## バージョン
ver 0.1

## 使い方
文章の自動生成の方法

### 事前準備
まずは、事前準備として、3つ組のデータを揃える
```
from PrepareChain import PrepareChain
text = u"適当な長い文章。長い文章。"
chain = PrepareChain(text)
triplet_freqs = chain.make_triplet_freqs()
chain.save(triplet_freqs, True)
```

### 文章の生成
事前準備がされていることが前提
```
from GenerateText import GenerateText
generator = GenerateText()
print generator.generate()
```


## 各ファイル
### README.md
このファイル

### PrepareChain.py
適当なテキストを与えて、そこから3つ組のチェーンを作成し、DBに保存するファイル

### schema.sql
DB作成のためのスキーマファイル

### GenerateText.py
実際にランダムで文章を生成するファイル

### chain.db
gitで管理はされていないが、3つ組チェーンの情報が保存されているDBファイル