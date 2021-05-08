Subhd.py: subhd.com 字幕下載器
============================

這個工具除了能幫你自動從Subhd.com下載字幕以外，它還能夠：

  - 自動解壓縮並找出最可能的檔案
  - 將編碼轉換成UTF-8 without DOM
  - 自動轉換為Unix style的行尾字元
  - 自動繁體 / 簡體轉換

預計往後會加入對Python 3的支持以及Windows操作系統的完整測試。

安裝
----

直接使用`pip`套件管理程式安裝:

:code:`$ pip install subhd.py`


抑或手動使用setup.py安裝:

:code:`$ python setup.py install`

為了要能解壓縮rar格式的檔案，`unrar`命令列程序必須被安裝。

使用方法
-------

.. code-block:: shell

    $ subhd.py -h
    usage: subhd.py [-h] [-r] [-a] [-t TYPE] [-o OUTPUT] keyword [keyword ...]

    Download subtitle from subhd.com, with support for Traditional Chinese /
     Simplified Chinese, encoding conversion

    positional arguments:
      keyword               Specify source filename or keyword string

    optional arguments:
      -h, --help            show this help message and exit
      -r, --raw             Treat keyword as raw string instead of filename
      -a, --auto            Download subtitle without prompting (best guess)
      -t TYPE, --type TYPE  Type of operation, either 'zhs' or 'zht'
      -o OUTPUT, --output OUTPUT  Specify destination filename, default's prefix
                            is the same as filename

    Copyright (C) 2015 Wei-Shao Tang (Frank Tang)

    Web: https://github.com/pa4373/subhd.py

    This is free software; see the source for copying conditions.
    There is no warranty, not even for merchantability or fitness
    for a particular purpose.

舉例來說，你能夠直接使用檔名搜索字幕：

.. code-block:: shell

   $ subhd.py Blade.Runner.1982.The.Final.Cut.BluRay.720p.DTS.2Audio.x264-CHD.mkv
   1) Blade Runner (final Cut)(1982) | 銀翼殺手 (None)
   2) Blade.Runner.1982.Final.Cut.BDRip.X264.iNT-TLF | 银翼杀手 导演最终剪辑版 (None)
   3) Blade Runner | 银翼杀手 | 公元2020/叛狱追杀令 (None)
   4) Blade Runner | 銀翼殺手 | 2020 (None)
   5) Blade Runner | 银翼杀手 | （好沉闷，看不懂！） (None)
   6) Dangerous Days: Making Blade Runner | 危险的日子：制作《银翼杀手》 (None)
   7) Blade Runner | 銀翼殺手 | 2020 (None)
   8) Blade Runner | 2020 | 银翼杀手 (None)
   9) Blade Runner | 银翼杀手 (None)
   10) Blade Runner | 银翼杀手 (None)
   11) Blade Runner | 银翼杀手 (None)
   12) Blade Runner | 银翼杀手 (None)
   13) Blade Runner | 银翼杀手 (None)
   14) Blade Runner | 銀翼殺手(國際院線版) (None)
   15) 银翼杀手 | Blade Runner | 导演剪辑版 修复版 | 銀翼殺手 (None)
   16) 银翼杀手 | Blade Runner (None)
   17) 银翼杀手 | Blade Runner (None)
   18) Blade.Runner | Blade.Runner.1982.Final.Cut.DVDRip.XviD-EPiC | 银翼杀手 (None)
   19) [银翼杀手].Blade.Runner.1982.HD-DVDRip.x264.a720.AC3-C@SiLU | Blade Runner | 银翼杀手 (None)
   20) 银翼杀手 | Blade Runner (None)
   Select one subtitle to download: 2

此時，你的字幕以備自動轉換為UTF-8編碼，並且翻譯成繁體中文。若字幕為srt格式，也會重新整理字幕索引，這樣對於類似Plex的服務器應用非常方便。

若要讓程式自動選擇字幕下載，打開`-a`的旗標：

.. code-block:: shell

   $ subhd.py -a Blade.Runner.1982.The.Final.Cut.BluRay.720p.DTS.2Audio.x264-CHD.mkv

字幕也可以翻譯成簡體中文：

.. code-block:: shell

   $ subhd.py -t zhs Blade.Runner.1982.The.Final.Cut.BluRay.720p.DTS.2Audio.x264-CHD.mkv

亦可使用字串直接查詢：

.. code-block:: shell

   $ subhd.py -r Blade\ Runner

貢獻
====
1. 複製這個版本庫
2. 建立你自己的功能分支 (git checkout -b my-new-feature)
3. 在你的分支上提交改變 (git commit -am 'Add some feature')
4. 推回你的遠端版本褲 (git push origin my-new-feature)
5. 在這個專案發布Pull Request

授權
====
本程式以GNU GPL v3方式授權，若專案內未包含授權內容，可至https://www.gnu.org/licenses/gpl.txt取得授權拷貝
