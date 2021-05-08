Jubatus Examples
================

1. shogun
   - classifier
   - Python/Ruby/Java
   - 分類器を利用した最も簡単なサンプルです。徳川家、足利家、北条家の各将軍の特徴を学習します。未知の将軍の名前を与えて、どの将軍とおもわれるか推定します。
2. gender
   - classifier
   - C++/Python/Ruby/Java
   - 分類器を利用した最も簡単なサンプルです。服装や髪形などの特徴を学習して、性別を推定します。
3. twitter\_streaming\_lang
   - classifier
   - Python
   - 分類器を利用した応用です。Wikipediaのデータを学習し、Twitterのストリームから受け取った、各つぶやきデータの言語を推定します。
4. twitter\_streaming\_location
   - classifier
   - Python/Java
   - 分類器を利用した応用です。Twitterのストリームから位置情報付きのツイートを学習し、文章がどの地域から発信されたものかを推定します。
5. malware\_classification
   - classifier
   - C++
   - 分類器を利用した応用です。バイナリの実行を受け取って、マルウェアかどうかを推定します。
6. movielens
   - recommender
   - C++/Python/Ruby/Java
   - レコメンダーを利用した最も簡単なサンプルです。MovieLens という映画の評価情報公開データを利用して、あるユーザーに対して似ているユーザーを表示します。
7. npb\_similar\_player
   - recommender
   - C++/Python/Ruby
   - レコメンダーを利用した最も簡単なサンプルです。野球選手のプロフィール情報を学習して、未知のそれぞれの選手と最も類似した特徴の選手を探します。
8. rent
   - regression
   - Python/Ruby/Java
   - 回帰を利用した最も簡単なサンプルです。物件情報から、その物件の家賃を予測します。
9. train\_route
   - graph
   - Python
   - グラフ解析の特に最短路探索を利用した最も簡単なサンプルです。都内の路線の経路情報を学習して、駅間の最短経路を探索します。
10. language\_detection
   - classifier
   - Python/Ruby
   - 分類器を用いた言語推定のデモです。欧米の言語に含まれる単語から言語を推定します。
11. trivial\_stat
   - stat
   - Python/Java
   - 統計分析機能を利用した最も簡単なサンプルです。果物の直径・重さ・価格を学習し、フルーツごとにパラメータの合計値や標準偏差などの統計分析を行います。
12. trivial\_burst
   - burst
   - Python
   - バースト検知機能を利用した最も簡単なサンプルです。仮想の時系列データを生成してバースト検知を行います。
13. winequality
   - regression
   - Ruby
   - 回帰を利用した最も簡単なサンプルです。Wine Quality データセットを利用して、ワインの情報から品質を推測します。
14. slot
   - bandit
   - python/Java
   - 多腕バンディットを利用したサンプルです。報酬の期待値が異なる複数のスロットマシンから、一定回数のプレイで得られる報酬を多腕バンディットで最大化します。
15. iris
   - classifier
   - python
   - 分類器を用いた簡単なサンプルです。iris データセットを利用して、花びらの幅、長さ、がくの幅、長さから、アヤメの種類を推定します。
16. network\_intrusion\_detection
    - anomaly
    - Python/Ruby/Java
    - アノマリーを用いた簡単なサンプルです。KDDCup 1999 データセットを利用して、ネットワーク侵入検出を行います。
17. mnist
	- classifier
	- Python
	- 画像特徴抽出プラグインを用いた簡単なサンプルです。mnistデータセットを利用して、画像から数字を推定します。
18. clustering
	- clustering
	- Python
	- 2次元データを使ってクラスタリングを行います
19. AAAI
    - nearest neighbor
    - Python
    - 近傍探索を用いた簡単なサンプルです。AAAIのaccepted paperから類似した論文を探します。

|                                     | classifer | clustering | recommender | regression | stat | graph | anomaly | burst | bandit | nearest neighbor |Language     |
|-------------------------------------|-----------|------------|-------------|------------|------|-------|---------|-------|--------|------------------|-------------|
| 1. shogun                           | :+1:      |            |             |            |      |       |         |       |        |                  |Py/Ru/Ja     |
| 2. gender                           | :+1:      |            |             |            |      |       |         |       |        |                  |C++/Py/Ru/Ja |
| 3. twitter\_streaming\_lang         | :+1:      |            |             |            |      |       |         |       |        |                  |Py           |
| 4. twitter\_streaming\_location     | :+1:      |            |             |            |      |       |         |       |        |                  |Py/Ja        |
| 5. malware\_classification          | :+1:      |            |             |            |      |       |         |       |        |                  |C++          |
| 6. movielens                        |           |            | :+1:        |            |      |       |         |       |        |                  |C++/Py/Ru/Ja |
| 7. npb\_similar\_player             |           |            | :+1:        |            |      |       |         |       |        |                  |C++/Py/Ru    |
| 8. rent                             |           |            |             | :+1:       |      |       |         |       |        |                  |Py/Ru/Ja     |
| 9. train\_route                     |           |            |             |            |      | :+1:  |         |       |        |                  |Py           |
|10. language\_detection              | :+1:      |            |             |            |      |       |         |       |        |                  |Py/Ru        |
|11. trivial\_stat                    |           |            |             |            | :+1: |       |         |       |        |                  |Py/Ja        |
|12. trivial\_burst                   |           |            |             |            |      |       |         | :+1:  |        |                  |Py           |
|13. winequality                      |           |            |             | :+1:       |      |       |         |       |        |                  |Ru           |
|14. slot                             |           |            |             |            |      |       |         |       |  :+1:  |                  |Py/Ja        |   
|15. iris                             | :+1:      |            |             |            |      |       |         |       |        |                  |Py           |   
|16. network\_intrusion\_detection    |           |            |             |            |      |       | :+1:    |       |        |                  |Py/Ru/Ja     |
|17. mnist                            | :+1:      |            |             |            |      |       |         |       |        |                  |Py           |
|18. clustering                       |           | :+1:       |             |            |      |       |         |       |        |                  |Py           |
|19. AAAI                             |           |            |             |            |      |       |         |       |        |  :+1:            |Py           |