* IMESupport for Sublime Text
  English: https://github.com/chikatoike/IMESupport/blob/master/README_en.org

* 概要
  IMESupportは、Windows の Sublime Text で IME を利用した文字入力をサポートするパッケージです。
  IME でインライン変換の入力文字が正しい位置に表示されない問題をある程度解決できます。

* 動作環境
  Windows OS のみ対応しています。 以下のバージョンで動作します。
  - Sublime Text 2 32bit
  - Sublime Text 2 64bit
  - Sublime Text 3 32bit
  - Sublime Text 3 64bit

  以下の環境で動作確認しました。
  - Sublime Text 2 32bit + Windows Vista 32bit + Microsoft Office IME 2007
  - Sublime Text 2 32bit + Windows Vista 32bit + Google日本語入力
  - Sublime Text 2 32bit + Windows Vista 32bit + SKK日本語入力FEP
  - Sublime Text 2 32bit + Windows 7 32bit + Microsoft Office IME 2010
  - Sublime Text 2 32bit + Windows 7 32bit + Google日本語入力
  - Sublime Text 2 32bit + Windows 7 32bit + SKK日本語入力FEP
  - Sublime Text 2 64bit + Windows 8 64bit + Microsoft IME 2012
  - Sublime Text 3 32bit + Windows 8 64bit + Microsoft IME 2012
  - Sublime Text 3 64bit + Windows 8 64bit + Microsoft IME 2012
  ATOK等、上に書かれていないIMEでも動作するはずですが、確認していません。

* インストール方法
  Package Controlを使ってインストールしてください。
  Package Controlをインストールした状態で、以下の手順でインストールできます。

  1. コマンドパレットで「Package Control: Install Package」を絞り込んでEnter
  2. パッケージ一覧から「IMESupport」を絞り込んでEnter
  3. ステータスバーにインストール完了のメッセージが表示されたら Sublime Text 2 を再起動

  手動でインストールする場合:

  コマンドプロンプト等で C:\Users\(ユーザー名)\AppData\Roaming\Sublime Text 2\Packages に移動して、
  git clone してください。

* 機能
  以下の機能が利用できます。
  - インライン変換の表示位置補正

* インライン変換の表示位置補正について
  この機能はインストールするだけで有効になります。ユーザー側での設定は必要ありません。

  現行バージョンの Sublime Text 2 では、IMEをONにして日本語入力しようとすると、以下のようにカーソル位置とは別の場所に入力中のテキストが表示されます。

  [[https://raw.github.com/chikatoike/IMESupport/master/img/inline1.png]]

  これを、カーソル位置に表示されるように補正します。

  [[https://raw.github.com/chikatoike/IMESupport/master/img/inline2.png]]

** 既知の不具合
   - IME ON で連続で入力するときに、変換確定後の次の1文字が、前の入力開始位置と同じ場所に表示されてしまいます。 これは2文字以上入力すれば、正しい位置に移動します。
   - File→New View into File で現在開いているファイルを新しいViewに表示した場合、最初のView以外では正しく動作しない可能性があります。
   これは Sublime Text 自体の不具合が原因です。適当な対策を実装していますが、パッケージ側で完全に対策するのは困難です。もし正しく動作していない場合はご報告下さい。

** 制限事項
   - ファイル編集以外の入力は対応していません。例えば、検索文字列の入力、Goto Anything などです。これらに入力フォーカスがある場合、強制的に画面左上に表示します。
   - 垂直分割時に、左側に1つもタブ(View)が表示されていない場合、右側のViewでは正しい位置に表示されません。これは、Viewがないとウィンドウ左端からの距離が計算出来ないためです。同様に、水平分割時に上側にViewがない場合は下側で正しい位置に表示されません。

* 参考
  - http://d.hatena.ne.jp/chikatoike/20121030/1351552567
  - http://sublimetext.userecho.com/topic/98697-handling-ime-message-on-windows-for-koreanjapanese-and-chinese-user/

* CHANGELOG
  2013-02-26
  - File→New View into File で開いたビューでの不具合対策(ST2/ST3)

  2013-02-09
  - Sublime text 3 でside barが表示されているときに、IMEの表示位置がずれていた問題を修正 (shirosakiさん、ありがとうごさいます)

  2013-01-30
  - Sublime Text 3 に対応
  - ver.0.2 開発開始

  2013-01-29
  - ver.0.1 リリース

  2013-01-22
  - Package Controlを使ったインストール方法を追加

  2013-01-21
  - line_padding_top, line_padding_bottom が設定されているときのフォントの大きさを修正 (shspageさん、ありがとうごさいます)

  2012-11-19
  - x64版に対応
  - メニューからのプロジェクト選択でクラッシュする問題を修正

  2012-11-11
  - 対応するIMEについて追記

  2012-11-07
  - IME起動時のフォントの大きさを修正 (tkmusic1976さん、ありがとうございます)

  2012-10-30
  - 64bit版のWindowsのサポートについて記載

  2012-10-29
  - 分割の比率が 1:1 ではない場合の表示位置がおかしい問題を修正
  - 最初のリリース
