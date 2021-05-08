gzhihu是一个从知乎上爬取内容的爬虫 
----------



##<a name="code"/>conf.ini文件说明
```python
   #conf.ini文件通过模块ConfigParser.ConfigParser解析, 通过名字就可以知道这个文件一般是放置一些常用的配置信息。
   #比如post信息，header头信息。
 
  conf = ConfigParser()  #初始一个ConfigParser对象
  conf.read('conf.ini')  #读取当前目录下conf.ini文件
  email = conf.get('account', 'email')   #得到account段中email的value

  conf.section()   #执行结果为一个列表，包含3个段的段名信息
  ['account', 'cookies', 'header']

  print dict(conf._section['account'])  #转化为字典，但是会自动加入 '__name__': 'account'
  {'__name__': 'account', 'password': ' ', 'email': ' '}

  #未转化为dict前的执行结果：
  print conf._section['account']
  OrderedDict([('__name__', 'account'), ('email', 'sbzhg1@163.com'), ('password', '7748548w')])

  print type(conf._section['account'])
  <class 'collections.OrderedDict'>
```



##<a name="code"/>代码示例
```python
  from zhihu import mysession, MyZhihu, Question

  #创建一个会话
  session = mysession()

  #把会话对象传给MyZhihu类
  my = MyZhihu(session)
  print my.ask()  #打印我的全部问题
  print my.topic()  #打印我的话题
  print my.column()  #打印我关注的专栏

  #有些问题在question/23905111之后还有类似#12817817的后缀，请删除之
  question = Question('http://www.zhihu.com/question/23905111', session)
  print question.title()  #问题的标题
  print question.question_detail()  #问题的详情
  print question.answer_number()   #问题的回答数
  print question.follower()    #问题的关注数

  
  #会打印出问题的每个答案，返回的是一个generator
  answers = question.all_answer()  
  for each in answers:
     print each

  #如果你需要保存，第二个参数是保存文件的路径，第三个参数是文件打开的读写模式。
  #如果你要指定文件   /home/path/a.txt
  #如果你要指定路径  /home/path/dir/   会在此路径下生成以问题标题为名的txt文件
  question.save(answers, '/path', 'w')
```



