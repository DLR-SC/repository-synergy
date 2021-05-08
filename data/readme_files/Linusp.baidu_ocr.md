* BaiduOcr

  百度 OCR 客户端，对百度公开的 API 提供更易用的 Python 封装。

** 百度 OCR API 说明

   目前百度已经在其[[http://apistore.baidu.com/][ APIStore]] 上提供了个人免费版和企业版两个版本的 OCR API，除 URL 不同外，API 是一样的。

   + 个人免费版

     +API 详情地址: http://apistore.baidu.com/apiworks/servicedetail/146.html+

     +限制: 5000次/天，每秒查询次数(Query Per Second, QPS)有限制+

     <2015-12-18 五>: 个人免费版服务已下线

   + 企业版

     API 详情地址: http://apistore.baidu.com/apiworks/servicedetail/969.html

     限制: 免费使用 10 次，超出需付费


   下面是对 API 本身的说明。

   + 接口地址:

     +免费版: http://apis.baidu.com/apistore/idlocr/ocr+

     企业版: http://apis.baidu.com/idl_baidu/baiduocrpay/idlocrpaid

   + 请求方法: POST

   + 参数说明:

     | 参数名       | 类型   | 必填 | 参数位置  | 描述                         | 可用值                                                  |
     |--------------+--------+------+-----------+------------------------------+---------------------------------------------------------|
     | fromdevice   | string | yes  | bodyParam | 来源设备                     | android, iPhone, pc                                     |
     |--------------+--------+------+-----------+------------------------------+---------------------------------------------------------|
     | clientip     | string | yes  | bodyParam | 客户端出口ip                 | 略                                                      |
     |--------------+--------+------+-----------+------------------------------+---------------------------------------------------------|
     | detecttype   | string | yes  | bodyParam | OCR服务类型                  | LocateRecognize, +Recognize+, Locate, +SingleCharRecognize+ |
     |--------------+--------+------+-----------+------------------------------+---------------------------------------------------------|
     | languagetype | string | yes  | bodyParam | 待检测的文字类型             | CHN_ENG, ENG, JAP, KOR                                  |
     |--------------+--------+------+-----------+------------------------------+---------------------------------------------------------|
     | imagetype    | string | yes  | bodyParam | 图片资源类型                 | 1: 经过BASE64处理的字符串; 2: 图片源文件                |
     |--------------+--------+------+-----------+------------------------------+---------------------------------------------------------|
     | image        | string | yes  | bodyParam | 图片资源,300K以下，JPEG 格式 | 略                                                      |
     |--------------+--------+------+-----------+------------------------------+---------------------------------------------------------|
     | apikey       | string | yes  | header    | API 授权代码                 | 略                                                      |
     |--------------+--------+------+-----------+------------------------------+---------------------------------------------------------|

     <2017-07-16 日>: detecttype 现在只支持 LocateRecognize 和 Locate

   + 返回值

     返回结果为 json 格式，对其中各字段的说明如下:

     | 字段      | 值类型         | 值的含义                                                             |
     |-----------+----------------+----------------------------------------------------------------------|
     | errNum    | unicode string | 结果状态，为 '0' 时表示有结果且正常；否则出错(错误码见 API 详情页面) |
     | errMsg    | unicode string | 错误消息，当 errNum 不为 '0' 时用于分析出错原因                      |
     | querySign | unicode string | 本次请求的唯一性标识(暂时无用)                                       |
     | retData   | list           | 实际结果                                                             |

     其中 retData 的至根据参数中的 detecttype 的不同而不同，下面对其进行具体说明
     - detecttype 为 LocateRecognize 时，retData 的内容为:

       #+BEGIN_SRC python
       [
           {
               u'word': u'xxxxx',    # 识别出的文字
               u'rect': {            # 识别出的文字区域信息
                   u'left': u'91',
                   u'width': u'782',
                   u'top': u'32',
                   u'height': u'24',
               }
           }
       ]
       #+END_SRC

     - detecttype 为 Locate 时，retData 的内容为图像上 *从上到下* 每一行文字的区域信息，如下所示

       #+BEGIN_SRC python
       [
           {u'rect': {
               u'left': u'91'
               u'width': u'782',
               u'top': u'32',
               u'height': u'24',
           }},
           ...
       ]
       #+END_SRC

** 安装

   项目当前只在 Github 上托管，可通过以下方法进行安装
   #+BEGIN_SRC sh
   pip install git+https://github.com/Linusp/baidu_ocr.git
   #+END_SRC

** 使用

   命令行工具 bocr 使用:
   #+BEGIN_SRC sh
   usage: bocr [-h] -i INPUT [-s SERVICE] [-l LANG]

   Recognize text from picuture.

   optional arguments:
     -h, --help            show this help message and exit
     -i INPUT, --input INPUT
                           specify picture want to recognize
     -s SERVICE, --service SERVICE
                           choose service from: locate_recog(default), locate
     -l LANG, --lang LANG  language of text to be detected, chn_eng(default),
                           eng, jap or kor
   #+END_SRC
   命令行使用需要将 API Key(从前文提到的两个版本的 API 页面获取)写入到 HOME 目录下的 .bocr_key 文件中。

   Python 库调用示例:
   #+BEGIN_SRC python
   from baiduocr import BaiduOcr

   API_URL = 'http://apis.baidu.com/idl_baidu/baiduocrpay/idlocrpaid'
   API_KEY = 'your api key'
   client = BaiduOcr(url=API_URL, key=API_KEY)

   # client.ping()
   res = client.recog('http://lyj.fj61.net/upload/2011-11/11110912327265.jpg',
                      service='LocateRecognize', lang='CHN_ENG')
   #+END_SRC
