# オンラインジャッジ補助スクリプト OnlineJudgeHelper

## 1. はじめに
このスクリプトは各種オンラインジャッジを利用する際、
サンプル入出力データを用いたテストやソースコードの提出等を
素早く行うことを目的に作りました。
まだ未完成のスクリプトですのでパッチ等は大歓迎です。

## 2. 仕様

### 2.1. 機能
-   解答ソースコードのコンパイル
-   サンプル入出力データのダウンロード
-   サンプル入出力データとの一致確認
    -   単純diffバリデータ
    -   浮動小数バリデータ
-   解答ソースコードの提出

### 2.2. 対応オンラインジャッジ
-   PKU JudgeOnline
-   CodeForces (サンプル入出力データのダウンロードのみ)
-   MJudge
-   AOJ
-   CodeChef (サンプル入出力データのダウンロードのみ)
-   ImoJudge (サンプル入出力データのダウンロードのみ)
-   AtCoder
-   ZOJContest
-   NPCA Judge
-   KCS
-   yukicoder (サンプル入出力データのダウンロードのみ)

## 3. 使い方

``` sh
    $ ./oj.py --onlinejudgename [contest_id] problem_id [options...]
```

例:

``` sh
    $ ./oj.py --atcoder arc001 arc001_1 -i atcoder-arc001-A.cpp
    $ ./oj.py --yukicoder 9002 -i yukicoder9002.cpp -e 1e-4
```

contest\_id,problem\_idに指定する値はオンラインジャッジ毎に異なります。
大半は問題ページのURLの一部です。

オンラインジャッジ | オプション名   | contest_id,problem_idに指定する値
-------------------|----------------|--------------
PKU JudgeOnline    | `--poj`        | `http://acm.pku.edu.cn/JudgeOnline/problem?id=[ problem_id ]`
CodeForces         | `--codeforces` | `http://codeforces.com/contest/[ contest_id ]/problem/[ problem_id ]`
MJudge             | `--mjudge`     | `http://m-judge.maximum.vc/problem.cgi?pid=[ problem_id ]`
AOJ                | `--aoj`        | `http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=[ problem_id ]`
CodeChef           | `--codechef`   | `http://www.codechef.com/[ contest_id ]/problems/[ problem_id ]`
ImoJudge           | `--imojudge`   | `http://judge.imoz.jp/page.php?page=view_problem&pid=[ problem_id ]&cid=[ contest_id ]`
AtCoder            | `--atcoder`    | `http://[ contest_id ].contest.atcoder.jp/tasks/[ problem_id ]`
ZOJContest         | `--zojcontest` | `http://acm.zju.edu.cn/onlinejudge/showContestProblem.do?problemId=[ problem_id ]`
NPCA Judge         | `--npca`       | `http://judge.npca.jp/problems/view/[ problem_id ]`
KCS                | `--kcs`        | `http://kcs.miz-miz.biz/contest/[ contest_id ]/view_problem/[ problem_id ]`
yukicoder          | `--yukicoder`  | problem\_id=問題番号（No.xx 問題名 のxx部分）(`http://yukicoder.me/problems/no/[ problem_id ]`)

AtCoderのproblem\_idは`arc042_a`のようにcontest\_idを含む形になっていることが多いですが、単に`a`とだけ指定することも可能です。

### 3.1. 初めて使う場合
設定ファイルを`setting.json`という名前で作成し、
oj.pyと同じディレクトリに配置して下さい。
あるいは`.onlinejudgehelper.setting.json`という名前で、ホームディレクトリ直下に配置して下さい。
内容は各種オンラインジャッジのユーザーID、パスワード、起動するブラウザを
json形式で書いたものです。

例:

``` json
    {
      "atcoder":{"user_id":"nodchip","password":"hogehoge", "browser":"C:/Users/nodchip/AppData/Local/Google/Chrome/Application/chrome.exe"},
      "zoj":{"user_id":"nodchip","password":"fufagufa", "browser":"C:/Users/nodchip/AppData/Local/Google/Chrome/Application/chrome.exe"}
    }
```

また、`setting.json`を用いて、オプション`--testcase-directory`、オプション`--source-file-name`の既定値を指定することもできます。

例:

``` json
    {
        "testcase_directory":"test",
        "source_file_name":"a.cpp",
    }
```

### 3.2. オプション

```
  -h, --help            ヘルプを出力します
  -c, --create-solution-template-file
                        解答ソースコードのコンパイルと
                        サンプル入出力データとの一致確認を行います
  -s, --submit          解答ソースコードを提出します
  -a, --add-test-case-template
                        入出力データのひな形ファイルを追加作成します
  -i SOURCE_FILE_NAME, --source-file-name=SOURCE_FILE_NAME
                        ソースコードファイル名を指定します
  --setting-file-path=SETTING_FILE_PATH
                        設定ファイルのパスを指定します
  --testcase-directory=TESTCASE_DIRECTORY
                        テストケースを置くディレクトリを指定します
  -t, --titech-pubnet   東工大内ネットワークからプロキシを使用して接続します
  -e FLOATING_POINT     許容誤差を指定して浮動小数バリデータを使用します
  -d, --download        サンプル入出力データのダウンロードのみ行います
```

### 3.3. 色について
colormaというpyhtonのライブラリがインストールしてあれば、テストの実行の際に色が付きます。
インストールの際は2.xと3.xを間違えないように注意してください。

### 3.4. 補完について
zsh用の補完設定ファイルがあります。
completionというディレクトリをfpathに追加すれば有効になります。antigen等を用いてインストールすることも可能です。


## 4. その他
OnlineJudgeHelperは幾つかのブログで紹介されました。
この場を借りて御礼申し上げます。

-   [\[O\] PKUやCodeforcesなど5つのオンラインジャッジ対応の神スクリプト](http://diary.overlasting.net/2011-02-12-1.html)
-   [情報系の備忘録: 神スクリプトの使い方 Codeforces編](http://joho-log.blogspot.jp/2011/08/codeforces.html)
-   [こどふぉのすすめ - wisteryメモ](http://d.hatena.ne.jp/wistery_k/20111226)
