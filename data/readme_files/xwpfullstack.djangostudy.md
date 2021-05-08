---
layout: post
title: Django web
---

[TOC]

# 一个项目入门Django

## 学习目标

+ 建立一个Django项目,创立一个基本的Django应用.
+ 为Django项目设立静态文件和其他文件
+ 使用Django的Model-View-Template(MVT)设计模式
+ 创建数据库模型,用Django提供的对象关系绑定功能
+ 利用数据库模型生成的数据来创建动态生成页面
+ 使用Django提供的用户认证服务
+ 整合应用的外部服务
+ 一个web应用所包括的CSS和JavaScript
+ 设计和应用CSS来增加web应用的界面交互
+ 使用Django的cookies和sessions
+ 在应用中使用像AJAX这样的高级功能
+ 用PythonAnywhere部署你的应用到web服务器


## 初始设计和规划

我们先前提到过,这本书的要点是开发一个叫做rango的应用.为了开发这个应用,它将会覆盖我们制作web应用大部分核心内容.

## 设计概要

+ 你的客户端需要建立一个叫做rango的网站,它可以让用户浏览它们自己订制的网页.

+ 在网站的主页上,让浏览者看到:
    + 5个查看最多的页面
    + 5个质量最高的目录
    + 访客浏览或者查找目录的方法
    + 当一个用户查看一个目录页,将会展现:目录名称,访问数量,喜欢数量;
    + 与目录相近的页面(展示页面标题和它的url);
    + 一个特殊的目录,客户端希望目录的名字,每个目录页面被访问的次数和多少个用户点击'like'按钮被记录.
    + 每个目录都可以通过一个可读的URL访问，比如. /rango/books-about-django/.
    + 只有注册的用户才能为目录增加页面.同时,访问者可以注册一个账户.
第一眼看上去,这个应用看起来很奇怪.事实上,它就是一个目录列表,他们可以链接到页面,对吗?然而,这里还有许多复杂的东西需要处理.首先,让我们试着画一张图来展示我们要开发什么东西.

见效果图

## 环境准备

升级python包管理工具pip

    pip install --upgrade pip

python虚拟环境安装

    sudo apt-get install python-virtualenv
    sudo easy_install virtualenvwrapper
    mkvirtualenv [虚拟环境名称]
    workon [虚拟环境名称]
    离开   deactivate
    rmvirtualenv [虚拟环境名称]

上述工具装好后找不到mkvirtualenv命令，需要执行以下环境变量设置。

    1.创建目录用来存放虚拟环境
        mkdir $HOME/.virtualenvs
    2.在~/.bashrc中添加行：
        export WORKON_HOME=$HOME/.virtualenvs
    3.在~/.bashrc中添加行：
        source /usr/local/bin/virtualenvwrapper.sh
    4.运行:
        source ~/.bashrc

使用python2.7环境，你应该安装如下环境：

    (rango)itcast@itcast:~/workspace/itcast_project$ pip freeze list
    pip==7.1.2
    Django==1.7.8
    ipdb==0.8.1
    ipython==3.2.0
    Pillow==2.8.2
    wheel==0.24.0

把以上包名存储到package.txt，在你的python虚拟环境中，运行:

    pip install -r package.txt


## helloworld项目

1.创建项目工程

    django-admin startproject itcast_project

2.目录解释

    (rango)itcast@itcast:~/workspace$ tree itcast_project
    itcast_project/
    ├── itcast_project     -项目设置目录
    │ ├── __init__.py      -空的脚本,告诉Python编译器这个目录是一个Python包
    │ ├── settings.py      -用来存储Django项目设置的文件
    │ ├── urls.py          -用来存储项目里的URL模式
    │ └── wsgi.py          -帮助你运行开发服务,同时可以帮助部署你的生产环境
    └── manage.py          -提供了一系列的Django命令，开发时常用

3.生成相关数据表

    cd itcast_project
    python manage.py migrate

4.运行项目，默认使用端口8000

    python manage.py runserver

5.浏览器输入以下地址
    
    http://127.0.0.1:8000/

![helloworld.png](../figures/helloworld.png)


6.创建Django应用

    python manage.py startapp rango

    (rango)itcast@itcast:~/workspace/itcast_project$ python manage.py startapp rango
    (rango)itcast@itcast:~/workspace/itcast_project$ tree
    .
    ├── db.sqlite3            -默认使用的sqlite3数据库，migrate那步生成的
    ├── itcast_project
    │ ├── __init__.py
    │ ├── settings.py
    │ ├── urls.py
    │ └── wsgi.py
    ├── manage.py
    └── rango                 -app应用目录，相当于整个项目的一个子模块
        ├── admin.py          -向Django注册你的模型,它会为你创建Django的管理界面
        ├── __init__.py
        ├── migrations
        │ └── __init__.py
        ├── models.py         -存储此应用中数据模型的地方，在这里描述数据的实体和关系
        ├── tests.py          -存储应用的测试代码
        └── views.py          -处理用户请求和响应

views.py和models.py在每个app应用中都要用到,他们俩是Django设计模式的组成部分,例如Model-View-Template模式.

7.把rango app应用关联到itcast_project项目中

在你创建模型和视图之前,你必须要告诉Django你的新应用的存在.所以你必须修改你配置目录里的settings.py文件.打开文件找到INSTALLED_APPS元组.在元祖的最后面增加rango.

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'rango',
    )

8.创建视图

让我们在rango中创建一个简单的视图.作为我们的第一个视图,简单的把文本传送给客户端。

打开rango目录里的views.py文件.删除注释# Create your views here.现在你得到一个空文件.输入以下代码

    from django.shortcuts import render
    from django.http import HttpResponse
    def index(request):
        return HttpResponse("Rango says hey there world!")

+ 我们第一行首先从django.http模块导入HttpResponse对象.
+ 在views.py文件里每个视图对应一个单独的函数.在这个例子中我们只创建了一个index视图.
+ 每个视图至少带一个参数，一个在django.http模块的HttpRequest对象.
+ 每个视图都要返回一个HttpResponse对象.这个HttpResponse对象把一个字符串当做参数传递给客户端.

8.URL映射

在rango目录里,创建一个叫做urls.py的文件.文件里是可以设置你的应用映射到URL.

    from django.conf.urls import patterns, url
    from rango import views
    urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
    )

这段代码导入Django自带的映射URL机制.导入rango的view模块引入我们先前建立的视图.

为了建立映射,我们用到了tuple.在Django里必须用urlpatterns来命名这个元组.

这个urlpatterns元组包含一些django.conf.urls.url()函数的调用,而每个函数里都有一个唯一的映射.在上面的代码里,我们只用了url()一次,所以我们只映射了一个URL.django.conf.urls.url()函数的第一个参数是正则表达式^$,指的是匹配一个空字符串.所有匹配这个模式的URL都会映射到views.index()这个视图.用户的请求信息会包含在HttpRequest对象里作为参数传递给视图.我们给url()函数可选参数name赋值为index.

    url(regex, view, kwargs=None, name=None, prefix='')
    regex:正则匹配
    view:对应视图函数
    kwargs:url传参，传递给视图函数
    name:标识url，区别不同的映射，可用于模板标签中索引
    prefix:在视图函数前加前缀

9.项目中url和app应用中url关联

项目目录里已经存在了一个urls.py文件.为什么在app中创建另一个呢?事实上,你可以吧所有的项目应用的URL都放在这个文件里.但是这是一个坏的习惯,这回增加你的应用的耦合.各自应用的urls.py文件存放各自应用的URL.为了最小耦合,你可以稍后把它们加入到项目目录的urls.py文件里.

这就意味着我们需要设置itcast_project里的urls.py文件,把我们的rango应用和itcast_project连接.

打开itcast_project目录里的urls.py文件.

    from django.conf.urls import patterns, include, url
    from django.contrib import admin

    urlpatterns = patterns('',
        # Examples:
        # url(r'^$', 'itcast_project.views.home', name='home'),
        # url(r'^blog/', include('blog.urls')),

        url(r'^admin/', include(admin.site.urls)),
        url(r'^rango/', include('rango.urls')), # 添加到app的映射，注意','
    )

新增的映射将会寻找匹配^rango/的url字符串.如果匹配成功的话将会传递给rango.urls(我们已经设置过了).include()函数是从django.conf.urls导入的.整个URL字符串处理过程如下图所示.在这个过程中,域名首先被提取出来然后留下其他的url字符串(rango/)传递给我们的itcast_project,在这里它会匹配并去掉rango/然后把空字符串传递给rango应用.rango现在匹配一个空字符串,它会返回我们创造的index()视图.

10.阶段胜利

+ 运行django服务器,python manage.py runserver
+ 浏览器浏览,http://127.0.0.1:8000/rango/

![helloworldok.png](../figures/helloworldok.png)


11.总结回顾

1.python manage.py startapp <appname>来创建新的应用,这里<appname>是你的应用名.

2.把新应用名加入到settings.py文件的INSTALLED_APPS里，使项目关加入新的应用.

3.在项目的urls.py文件映射应用.

4.在应用目录里创建urls.py文件使URL字符串指向视图函数.

5.在应用的view.py里,创建的视图要确保返回一个HttpResponse对象.


12.练习

恭喜你!你已经创建并运行rango了.这是里程碑意义的事件.创建视图和映射是迈向开发更复杂可用的web应用的第一步.现在试着练习一下巩固所学.

+ 修改程序,确保你知道如何把URL映射到视图.
+ 创立一个about视图,返回Rango says here is the about page.
+ 把这个视图映射到/rango/about/.在这一步里,你只需要编辑rango应用里的urls.py
+ 修改index视图的HttpResponse,使它返回包含about页面的链接.
+ 在about视图里使它包含一个回到主页的链接.

13.练习提示

如果感觉练习有困难的话,下面将能帮助你完成练习.

+ index视图里需要包含about视图的链接.

  Rango says: Hello world! `<br/> <a href='/rango/about'>About</a>`

+ 匹配about/的正则表达式是r^about/.

+ 返回主页的链接是`<a href="/rango/">Index</a>` 这个结构和上面的about页面里的一样.

## 模板和静态媒体

1.创建存放模板的目录

在itcast_project项目根目录下，创建templates目录，里面再创建rango目录
    
        mkdir -p templates/rango

2.项目中设置模板查找路径，设置itcast_project项目管理目录里settings.py

绝对路径，硬编码，不建议，项目迁移到别的服务器时会出问题

    TEMPLATE_DIRS = ['<workspace>/itcast_project/']

动态获取路径

    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')
    TEMPLATE_DIRS = [
        TEMPLATE_PATH,
    ]

3.添加模板

在我们创建模板目录和设置好路径以后,我们需要在template/rango/目录里建立一个叫做index.html的文件,在新文件里加入下面代码:

    <!DOCTYPE html>
    <html>

    <head>
        <title>Rango</title>
    </head>

    <body>
        <h1>Rango says...</h1>
        hello world! <strong>{{ boldmessage }}</strong><br />
        <a href="/rango/about/">About</a><br />
    </body>

    </html>


这个HTML代码创建一个问候用户的简单HTML页面.你可能注意到了在上面有一段非HTML代码{{boldmessage}}.这是Django模板的变量,他可以在输出时为这个变量赋值.一会我们就会用它.

为了使用这个模板,我们需要重新修改一下我们先前创建的index()视图.这次我们不让他传递简单的信息,而是让他返回我们的模板.

在rango/views.py里,确定文件头部有如下代码.

    from django.shortcuts import render

修改index()视图函数如下.

    def index(request):
        context_dict = {'boldmessage': "I am bold font from the context"}
        return render(request, 'rango/index.html', context_dict)

首先我们建立一个在模板中使用的字典,然后我们调取render()函数.这个函数接受用户的request,模板名称和内容字典作为参数.这个render()函数将会把这些参数聚合到一起生成一个完整的HTML页面.然后返回给用户的浏览器.

当模板文件被加载到Django模板系统里时,它模板内容也会被创建.在简单的例子里模板的内容是字典里的模板变量对应的Python变量.在我们早先创建的模板文件,我们创建了一个叫做boldmessage的模板变量.在index(request)视图例子中,字符串I am bold font from the context映射到模板变量boldmessage.所以字符串I am bold font from the context将会替换模板里所有的{{ boldmessage }}.

现在你已经更新了视图,运行Django服务并访问 http://127.0.0.1:8000/rango/ .你将会看到

![template1.png](../figures/template1.png)

## 静态媒体

1.设置静态媒体目录

为了设置静态媒体,你需要设立存储它们的目录.在你的项目目录(例如<workspace>/itcast_project/),创建叫做static的目录.在static里再创建一个images目录.

    mkdir -p static/images

现在在static/images目录里放置一个图片.如果你和我一样也喜欢篮球，那么让我们项目以jordan为第一张图片吧.

![jordan.jpg](../figures/jordan.jpg)


2.设置项目中静态文件目录

在settings.py文件,我们需要更新两个变量STATIC_URL和STATICFILES_DIRS元组,像下面一样创建一个储存静态目录(STATIC_PATH)的变量.

    STATIC_PATH = os.path.join(BASE_DIR,'static')
    STATIC_URL = '/static/' #项目中已定义好此变量
    STATICFILES_DIRS = (
        STATIC_PATH,
    )


第一个变量STATIC_URL定义了当Django运行时Django应用寻找静态媒体的地址.例如,像我们上面的代码一样吧STATIC_URL设置成/static/,我们就可以通过http://127.0.0.1:8000/static/来访问它了. 

`注意：我们要注意斜杠的书写.如果不这么设置将会引起一大堆麻烦.`

STATIC_URL定义了web服务链接媒体的URL地址,STATICFILES_DIRS允许你定义新的static目录.像TEMPLATE_DIRS元组一样.STATICFILES_DIRS需要static目录的绝对路径.这里,我们还是用BASE_DIR变量来创建STATIC_PATH.

完成了这两个设置后,再一次运行你的Django服务.如果我们想要查看我们的jordan图片,访问http://127.0.0.1:8000/static/images/jordan.jpg.如果没有出现请查看setings.py文件是否设置正确,并重启服务.如果出现了,试着加入其他类型的文件到static目录并在浏览器上访问他们.

![template2.png](../figures/template2.png)

3.静态媒体和模板

现在你已经为你的itcast_project项目设置了静态媒体,你可以在你的模板里加入这些媒体.

下面将展示如何加入静态媒体,打开位于<workspace>/itcast_project/templates/rango目录的index.html文件.像下面一样修改HTML源代码.新加入两行用注释标示.

    <!DOCTYPE html>

    {% load staticfiles %} <!-- 模板标签加载静态文件路径 -->

    <html>

    <head>
        <title>Rango</title>
    </head>

    <body>
        <h1>Rango says...</h1>
        hello world! <strong>{{ boldmessage }}</strong><br />
        <a href="/rango/about/">About</a><br />
        <img src="{% static "images/jordan.jpg" %}" alt="Picture of jordan" /> 
    </body>

    </html>

首先,我们需要使用{% load static %}标签来使用静态媒体.所以我们才可以用{% static "jordan.jpg" %} 在模板里调用static文件.Django模板标签用{ }来表示.在这个例子里我们用static标签,它将会把STATIC_URL和jordan.jpg连接起来,如下所示.

    <img src="/static/images/jordan.jpg" alt="Picture of Jordan" /> 

如果因为什么原因图片不能加载我们可以用一些文本来代替.这就是alt属性的作用，如果图片加载失败就显示alt属性中的文本.

好了,让我们再次运行Django服务访问http://127.0.0.1:8000/rango.幸运的话可以看到下图.

![template3.png](../figures/template3.png)


4.阶段小结

学完这章,你应当学会如何设置和创建模板,在你的视图里使用模板,设置和使用Django来发送静态媒体文件,我们已经学了很多了，加油!

创建模板并在视图里使用是这章的关键.它需要一些步骤,但是当你尝试几次后就非常容易掌握了.

+ 创建你希望使用的模板并把它保存在templates目录里,这个目录需要你写入settings.py文件.你可以在模板里使用Django模板变量(例如{{ bariable_name }}).你可以在视图里更换这些变量.
+ 在应用的views.py文件里查找或者创建一个新的视图.
+ 在视图里,创建一个字典对象可以把模板内容传递给模板引擎.
+ 使用render()函数来生成返回.确保引用request,然后是模板文件,最后是内容字典!
+ 如果你还没有修改urls.py文件或者应用中的urls.py中的映射,你需要修改一下.
+ 在你的页面上获取一个静态媒体文件也是一个你需要掌握的很重要的步骤.
+ 把你要添加的静态文件放入static目录.这个目录是你在settings.py中设置的STATICFILES_DIRS元组.
+ 在模板中添加静态媒体引用.例如一个HTML网页的图片用<img />标签.
+ 记得用{% load staticfiles %}和{% static "filename" %}命令在模板中设置静态文件.

5.练习

+ 把about页面也用一个about.html模板来设置.
+ 在about.html模板里,在你的静态媒体里增加图片.


## 模型和数据库

通常来说处理数据库需要我们掌握许多复杂的SQL语句.但是在Django里,对象关系映射(ORM)帮我们处理这一切,包括通过模型创建数据库表.事实上,模型是描述你的数据模型/图表的一个Python对象.与以往通过SQL操作数据库不同,你只用使用Python对象就能操作数据库.我们将会学习如何设立数据库并为rango建立模型.

1.rango的需求，首先,让我们看看rango的需求.下面列出了rango数据关键的几个需求.

+ rango实际上是一个网页目录 - 一个包含其他我站链接的网站
+ 有许多不同网站的目录,每个目录中包含许多链接.
+ 一个目录要有名字,访问数和链接.
+ 一个页面要有目录,标题,URL和一些视图.


2.告诉Django你的数据库，Django会自动在settings.py里添加一个叫做DATABASES的字典.它包含如下.

    DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


能看到默认用SQLite3作为后端数据库.SQLite是个轻量级的数据库对我们开发很有用.我们仅仅需要设置DATABASE_PATH里的NAME键值对.其他引擎需要USER,PASSWORD,HOST和PORT等关键字.

    注意:对于教程来说使用SQLite引擎还好,但是对于部署你的应用来说可能不是最好的选择,或许应当使用其他更健壮和更大型的数据库引擎.Django同样支持像PostgreSQL和MySQL这样的流行数据库引擎.

3.创建模型

让我们为Rango创建两个数据模型.在rango/models.py里,我们定义两个继承自djnago.db.models.Model的类.这两个类分别定义目录和页面.定义Category和Page如下.

    class Category(models.Model):
        name = models.CharField(max_length=128, unique=True)

        def __unicode__(self):  
            return self.name

    class Page(models.Model):
        category = models.ForeignKey(Category)
        title = models.CharField(max_length=128)
        url = models.URLField()
        views = models.IntegerField(default=0)

        def __unicode__(self):      #Python2, use __str__ on Python3
            return self.title

当你定义了一个模型,你需要制定可选参数的属性以及相关的类型列表.Django提供了许多内建字段.一些常用的如下.

    CharField－存储字符数据的字段(例如字符串).max_length提供了最大长度.
    URLField－和CharField一样,但是它存储资源的URL.你也可以使用max_length参数.
    IntegerField－存储整数.
    DateField－存储Python的datetime.date.

查看Django documentation on model fields获取完整列表.

每个字段都有一个unique属性.如果设置为True,那么在整个数据库模型里它的字段里的值必须是唯一的.例如,我们上面定义的Category模型.name字段被设置为unique - 所以每一个目录的名字都必须是唯一的.

如果你想把这个字段作为数据库的关键字会非常有用.你可以为每个字段设置一个默认值(default='value'),也可以设置成NULL(null=True).

Django也提供了连接模型/表的简单机制.这个机制封装在3个字段里,如下.

    ForeignKey－创建1对多关系的字段类型.
    OneToOneField－定义一个严格的1对1关系字段类型.
    ManyToManyFeild－当以多对多关系字段类型.

从上面我们的例子,Page中category字段是ForeignKey类型.所以我们可以创建一个1对多关系的Category模型/表,这个Category会作为构造函数的一个参数.Django会自动的为每个模型表中创建ID字段.所以你不同为每个模型创建主键，它已经为你做好了!

注意:当创建模板的时候,最好创建`__unicode__()`方法 - 等价于`__strr__()`方法.如果你不熟悉这两个方法,它们俩的作用和Java中toString()方法相似.`__unicode__()`方法为模型实例提供unicode表达式.例如我们的Category模型通过`__unicode__()`方法返回目录的名字，当你开始用Django的管理界面后这将会非常便利. 在你的类里加入`__unicode__()`方法对debug也非常有用.如果在Category模型中没有`__unicode__`方法将会返回`<Category: Category object>`.我们只知道是一个目录,但是是哪一个呢?如果我们有`__unicode__()`方法我们将会返回`<Category: python>`,这里的python是目录的名字.

4.创建和迁移数据库

+ 创建数据库表
    python manage.py migrate
+ 记录数据模型前后变化
    python manage.py makemigrations <app_name>
+ 根据makemigrations记录的数据模型变化文件再次更新数据表
    python manage.py migrate

5.Django Shell

通过Django shell创建Django模型，它对我们debug非常有用.下面我们将展示如何用这种方式来创建Category实例.

为了得到shell我们需要再一次调用Django项目根目录里的manage.py.

    python manage.py shell

这个实例将会创建一个Python解析器并且载入你的项目的设置.你可以和模型进行交互.下面的命令展示了这一功能.注释里可以看到每个命令的功能.

    # Import the Category model from the rango application
    >>> from rango.models import Category

    # Show all the current categories
    >>> print Category.objects.all()
    [] # Returns an empty list (no categories have been defined!)

    # Create a new category object, and save it to the database.
    >>> c = Category(name="Test")
    >>> c.save()

    # Now list all the category objects stored once more.
    >>> print Category.objects.all()
    [<Category: test>] # We now have a category called 'test' saved in the database!

    # Quit the Django shell.
    >>> quit()

在例子中我们首先导入我们需要操作的模型.然后打印出存在的目录,在这里因为我们的图表是空所以输出也是空.然后创建并储存一个目录,打印.

6.设置管理界面

Django最突出的一个特性就是它提供内建的网页管理界面,用来浏览和编辑存储在模型的数据,也可以与数据库图表交互.在settings.py文件里,注意到有一个默认安装的django.contib.adminapp,而且你的urls.py里也默认增加了admin匹配.


访问http://127.0.0.1:8000/admin/.可以用先前设置管理员账户的用户名和密码来登录Django管理界面.管理界面只包含Groups和Users图表以我们需要让Django包含rango模块.所以打开rango/admin.py输入如下代码:

    from django.contrib import admin
    from rango.models import Category, Page

    admin.site.register(Category)
    admin.site.register(Page)

上面代码会为我们在管理界面注册模型.如果我们想要其他模型,可以在admin.stie.register()函数里传递模型作为参数.

现在你可以创建一个管理员来管理数据库.

    python manage.py createsuperuser

管理员账户将会在Django管理界面登陆时使用.按照提示输入用户名,邮箱地址和密码.注意要记住用户名和密码.

![admin1.png](../figures/admin1.png)

开启Django服务:

    python manage.py runserver

完成之后重新访问http://127.0.0.1:8000/admin/,你想回看到如下图案.

![admin2.png](../figures/admin2.png)

![admin.png](../figures/admin.png)

7.创建生成测试数据脚本

往数据库里输入数据会非常麻烦.许多开发者会随机的往数据库里输入测试数据.如果你在一个小的开发团队里,每个人都得传点数据.最好是写一个脚本而不是每个人单独的上传数据,这样就可以避免垃圾数据的产生.所以我们需要为你的数据库创建 population script.这个脚本自动的为你的数据库生成测试数据.

我们需要在Django项目的根目录里创建population script(例如<workspace>/itcast_project/).创建populate_rango.py文件代码如下.

    import os
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'itcast_project.settings')

    import django
    django.setup()

    from rango.models import Category, Page


    def populate():
        python_cat = add_cat('Python')  #创建python目录类
        add_page(cat=python_cat,         
            title="Official Python Tutorial",
            url="http://docs.python.org/2/tutorial/")
        add_page(cat=python_cat,
            title="How to Think like a Computer Scientist",
            url="http://www.greenteapress.com/thinkpython/")
        add_page(cat=python_cat,
            title="Learn Python in 10 Minutes",
            url="http://www.korokithakis.net/tutorials/python/")

        django_cat = add_cat("Django")  #创建Django目录类
        add_page(cat=django_cat,
            title="Official Django Tutorial",
            url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/")
        add_page(cat=django_cat,
            title="Django Rocks",
            url="http://www.djangorocks.com/")
        add_page(cat=django_cat,
            title="How to Tango with Django",
            url="http://www.tangowithdjango.com/")

        frame_cat = add_cat("Other Frameworks")
        add_page(cat=frame_cat,
            title="Bottle",
            url="http://bottlepy.org/docs/dev/")
        add_page(cat=frame_cat,
            title="Flask",
            url="http://flask.pocoo.org")
        # Print out what we have added to the user.
        for c in Category.objects.all():
            for p in Page.objects.filter(category=c):
                print "- {0} - {1}".format(str(c), str(p))

    #函数定义
    def add_page(cat, title, url, views=0):
        p = Page.objects.get_or_create(category=cat, title=title, url=url, views=views)[0]
        return p

    def add_cat(name):
        c = Category.objects.get_or_create(name=name)[0]
        return c

    # Start execution here!
    if __name__ == '__main__':
        print "Starting Rango population script..."
        populate()


虽然看起来有许多代码,但是非常简单.在文件开头我们定义了许多函数,代码会在底部开始执行 寻找`if __name__ == '__main__'`这一行开始.我们调用了populate()函数.

警告:当导入Django模块时确保已经导入了Django设置,并把环境变量DJANGO_SETTINGS_MODULE设置为项目设置文件.然后调用django.setup()来导入django设置.如果不这么做就会引发一场.这就是为什么我们需要在导入设置之后才能导入Category和Page.
populate()函数负责调用add_cat()和add_page()函数,而这两个函数将会创建新的目录和页面.populate()创建页面和目录并存到数据库.最后我们在终端里输出页面和目录.

注意:我们使用get_or_create()函数创建模型实例.我们可以用get_or_creat()函数来检查在数据库里是否存在.如果不存在就创建它.这将减少我们的代码而不是让我们自己检查. get_or_create()方法返回(object,created)元组.如果没有在数据库找到,那么这个object参数就是get_or_create()方法创造的实例.如果这个实体不存在,那么这个方法就返回和这个实体相符的实例.created是一个布尔值;如果get_or_create()创建模型实体的话它会返回true. [0]会返回object元组的第一个位置,这个其他编程语言一样,Python使用zero-based numbering. official Django documentation 可以查看get_or_vreate()方法的详细资料.
当保存退出以后,我们可以在DJango项目根目录执行命令.

    python populate_rango.py

    Starting Rango population script...
    - Python - Official Python Tutorial
    - Python - How to Think like a Computer Scientist
    - Python - Learn Python in 10 Minutes
    - Django - Official Django Tutorial
    - Django - Django Rocks
    - Django - How to Tango with Django
    - Other Frameworks - Bottle
    - Other Frameworks - Flask

现在我们检查一下是否改变了数据库.重启Django服务,进入管理界面,查看新的目录和页面.如果点击Pages会看到下面.

![admin4.png](../figures/admin4.png)

虽然需要花费一些时间来写population script,但是在团队协作中可以分享给每个人.而且在单元测试中会有用处.


8.阶段小结，加入模型，分5步进行.

+ 在你的应用里的models.py文件里创建新的模型.
+ 修改admin.py注册你新加的模块
+ 使用python manage.py makemigrations 记录数据库更改
+ 使用python manage.py migrate应用更改.这将会为你的模型在数据库里建立必要的结构
+ 为你的新模型创建/修改population script.

总会有一些时候你不得不删除数据库.在这种情况下你需要运行migrate命令,然后是createsuperuser命令,为每个app执行sqlmigrate命令就可.

9.练习,试着做下面的练习来巩固所学.

+ 增加目录模型views和likes属性并设置为0.
+ 更新 population script ,把Python目录设置成浏览128次和喜欢64次,Django目录浏览64次和喜欢32次,the Other Framenwork目录浏览32次,喜欢16次.
+ 查看part two of official Django tutorial .它将会巩固你所学同时学习更多关于如何定制管理界面.

10.提示,如果你需要一些帮助的话,下面的提示会帮助你.

+ 修改Category模型,增加views和likes,它们的字段为IntegerFields.
+ 修改populate.py脚本里的add_cat函数,加入views和likes参数.一旦你可以获取目录c,你就可以通过c.views来修改浏览次数,likes也一样.
+ 为了定制管理界面,你需要修改rango/admin.py文件,创建PageAdmin类,这个类继承自admin.ModelAdmin.
+ 在PageAdmin类里,加入list_display = ('title', 'category', 'url').
+ 最后注册PageAdmin类到Django管理界面.需要修改admin.site.register(Page).在Rango的admin.py文件里修改成admin.site.register(Page, PageAdmin).


## 模型,模板和视图

现在我们已经建立了模型并且导入了一些数据,现在我们要把这些连一起.我们将会弄清楚如何在视图中访问数据以及如何通过模板展示数据.

### 基本流程:数据驱动页面

在Django中创建数据驱动页面必须执行以下5步.

    1.首先,在你应用的views.py文件中导入你要添加的模型.
    2.在视图里访问模型,导入你需要的数据.
    3.把模型的数据传递给模板.
    4.设置模板给用户呈现数据.
    5.如果还没有映射URL,映射一下吧.

上面的步骤告诉你如何使用Django里的模型,视图和模板.

### 展示rango主页上的目录

我们需要在rango的主页显示5个最多的目录.

1.导入需要的模型

为了达到目的,我们需要完成上面的步骤.首先,打开rango/view.py并导入rango的models.py文件的Category模块(Category应该已经在上章练习中增加了likes，views等字段)

    # Import the Category model
    from rango.models import Category

2.修改index视图

有了第一步,我们需要修改index()函数.让我们回想一下,这个index()函数负责管理主页的视图.修改如下.

    from rango.models import Category
    def index(request):
        category_list = Category.objects.order_by('-likes')[:5]
        context_dict = {'categories': category_list}
        return render(request, 'rango/index.html', context_dict)

这里我们做了第2步和第3步.首先,我们访问Category模型得到5个最多的目录.这里用order_by()方法对喜欢的数量进行降序排序,注意带着'-'.最后我们取前5个目录保存到category_list

当访问数据库结束,我们把这个列表(category_list)传给了字典context_dict.这个字典同时会作为render()的参数返回给模板.

    警告:注意Category模型包含likes字段.增添它的操作在前面章节的练习里,你需要完成它们.

3.修改index模板

修改完视图后,最后剩下的就是更改rango/index.html模板了.代码如下.

    <!DOCTYPE html>
    <html>
    <head>
        <title>Rango</title>
    </head>

    <body>
        <h1>Rango says...hello world!</h1>

        {% if categories %}
            <ul>
                {% for category in categories %}
                <li>{{ category.name }}</li>
                {% endfor %}
            </ul>
        {% else %}
            <strong>There are no categories present.</strong>
        {% endif %}

        <a href="/rango/about/">About</a>
    </body>
    </html>

这里我们用了Django模板语言里的if和for控制语句.在页面的<body>里我们检查categories是否为空(例如,{% if categories %}).

如果不为空,会建立一个无序HTML列表(在`<ul>`标签里).for循环({% for category in categories %})会依次在`<li>`标签里打印出每个目录的名字({{ category.name }}).

如果不存在categories,将会输出There are no categories present..

作为模板语言,所有的命令都包含在{%和%}标签里,所有的变量都在{{和}}里.

如果访问 http://127.0.0.1:8000/rango/ ,如下图所示.

![rango1.png](../figures/rango1.png)

### 创建详细页面

通过rango的详细描述,我们需要列出目录的每个页面.现在我们需要克服许多困难.我们需要创建一个新的视图作为参数.我们同时需要创建URL模式和URL字符串来对应每个目录的名字.

1.URL设计与映射

让我们着手解决URL问题.有一种方法是为我们的目录在URL中设立唯一的ID,我们可以创建像/rango/category/1/或者/rango/category/2/,这里的数字1和2就是它们的ID.但是这样做对我们来说不太好理解.尽管我们知道数字关联着目录,但我们怎么知道1和2代表哪个目录呢?用户不试一下就不会知道.

另一种方法就是用目录名作为URL./rango/category/Python/将会返回给我们关于Python的目录.这是一个简单的,可读的URL.

注意:对于网页来说,设计一个简洁的URL是至关重要的.

2.为Category表增加Slug字段

为了建立简洁的url我们需要在Category模型里增加slug字段.首先我们需要从django导入slugify函数,这个函数的作用是把空格用连字符代替,例如"how do i create a slug in django"将会转换成"how-do-i-create-a-slug-in-djang".

    警告:虽然你能在URL中用空格,但是它们并不安全.

接下来我们将会重写Category模型的save方法,我们将会调用slugify方法并更新slug字段.注意任何时候目录名称更改都会更改slug.像下面一样修改模型.

    from django.template.defaultfilters import slugify

    class Category(models.Model):
        name = models.CharField(max_length=128, unique=True)
        views = models.IntegerField(default=0)
        likes = models.IntegerField(default=0)
        slug = models.SlugField(unique=True)

        def save(self, *args, **kwargs):
                self.slug = slugify(self.name)
                super(Category, self).save(*args, **kwargs)

        def __unicode__(self):
                return self.name

先删除db.sqlite3数据库文件，现在需要运行下面的命令更新模型和数据库.

    rm db.sqlite3
    python manage.py migrate
    python manage.py makemigrations rango
    python manage.py migrate

因为我们slug没有设置默认值,而且模型中已经加入进数据,所以migrate命令将会给你两个选项.选择提供默认值选项并输入默认值''.它会马上进行修改.现在重新运行population脚本.因为每个目录都会执行save方法,所以重写的save方法将会被执行修改slug字段.运行Django服务,你讲会在管理界面看到修改的数据.

在管理界面你或许希望在填写目录名的时候自动填充slug字段.按照下面的方法修改rango/admin.py.

    from django.contrib import admin
    from rango.models import Category, Page

    class CategoryAdmin(admin.ModelAdmin):
        prepopulated_fields = {'slug':('name',)}

    admin.site.register(Category, CategoryAdmin)    #注册类装饰
    admin.site.register(Page)

在管理界面尝试增加新的目录.看到了吧!现在我们可以加入slug字段用作我们的url.


3.目录视图函数

在rango/views.py中,我们需要导入Page模型.然后加入我们的category()视图:如下.

    from rango.models import Page
    def category(request, category_name_slug):
        context_dict = {}
        try:
            category = Category.objects.get(slug=category_name_slug)
            context_dict['category_name'] = category.name
            pages = Page.objects.filter(category=category)
            context_dict['pages'] = pages
            context_dict['category'] = category
        except Category.DoesNotExist:
            pass
        return render(request, 'rango/category.html', context_dict)

和index()视图一样我们的新视图也要执行同样的基本步骤.我们需要定义一个字典,然后尝试从模型中导出数据,并把数据添加到字典里.我们通过参数category_name_slug的值来决定是哪个目录.如果在Category模型中找到目录,我们就会把context_dict字典传递给相关页面.

4.目录模板

现在为我们的新视图创建模板.在<workspace>/itcast_project/templates/rango/目录创建category.html.

    <!DOCTYPE html>
    <html>
    <head>
        <title>Rango</title>
    </head>

    <body>
        <h1>{{ category_name }}</h1>
        {% if category %}
            {% if pages %}
            <ul>
                {% for page in pages %}
                <li><a href="{{ page.url }}">{{ page.title }}</a></li>
                {% endfor %}
            </ul>
            {% else %}
                <strong>No pages currently in category.</strong>
            {% endif %}
        {% else %}
            The specified category {{ category_name }} does not exist!
        {% endif %}
    </body>
    </html>

上面的HTML代码同样给我们展示了如何把数据通过字典传递给模板.我们用到了category_name变量和category和pages对象.如果category在模板上下文并没有定义,或者在数据库并没有发现这个目录,那么就会提示一个友好的错误信息.相反的话如果存在,我们将会检查pages.如果pages没有被定义或者不存在元素,我们同样也会呈现友好的错误提示.否则的话目录里包含的页面就会写入HTML里面.对于在pages列表的每个页面我们都会展示它的title和url.

注意:Django模板包含{% if %}标签，是检测对象是否在模板上下文的好方法.尝试在你的代码里使用以减少错误的发生.


5.参数化的URL映射

现在让我们来看看如何把category_name_url参数值传递给category().我们需要修改rango的urls.py文件和urlpatterns元组.

    urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category,name='category'),)  # New!


你能看到当正则表达式r'^(?P<category_name_slug>\\w+)/$匹配时会调用view.category()函数.我们的正则表达式会匹配URL斜杠前所有的字母数字(例如 a-z, A-Z, 或者 0-9)和连字符(-).然后把这个值作为category_name_slug参数传递给views.category(),这个参数必须在强制的request参数之后.

注意:当你希望参数化URL时,一定要确保你的URL模式会正确匹配参数.为了更进一步的了解,让我们看一看上面的例子. url(r'^category/(?P<category_name_slug>[\\w\-]+)/$', views.category, name='category') 我们可以从这里找到在category/和后面的/之间的字符串,并把它作为参数category_name_slug传递给views.category()参数.例如,URLcategory/python-books/将会返回的category_name_slug参数是python-books. 需要知道的是所有的视图函数必须带至少一个参数.这个参数是`request`它会提供HTTP请求用户的相关信息。当参数化URL时,可以给视图添加已经命名的参数.使用上面的例子,我们的category视图是这样的. def category(request, category_name_slug): 附加参数的位置不重要,重要的是在URL模式中定义的参数名称.注意如何为我们的视图在URL模式匹配中定义category_name_slug参数.

6.修改index模板

虽然我们的视图已经建立了,但是还要做许多工作.我们的index模板需要修改并提供给用户category列表.我们可以通过slug为index.htnl模板中添加目录页面.

    <!DOCTYPE html>
    <html>
    <head>
        <title>Rango</title>
    </head>

    <body>
        <h1>Rango says..hello world!</h1>

        {% if categories %}
            <ul>
                {% for category in categories %}
                <!-- Following line changed to add an HTML hyperlink -->
                <li>
                <a href="/rango/category/{{ category.slug }}">{{ category.name }}</a>
                </li>
                {% endfor %}
            </ul>
       {% else %}
            <strong>There are no categories present.</strong>
       {% endif %}

    </body>
    </html>

这里为每个列表元素(`<li>`)增加一个HTML超链接(`<a>`).超链接有一个href属性,我们用{{ category.slug}}来定义目标URL.


7.Demo

让我们访问rango主页.你将会看到列出所有的目录.这些目录都是可以点击的链接.点击Python将会带你王文Python目录视图,如下图所示.如果你看到了像Official Python Tutorial列表,说明你已经成功了建立视图.试着访问不存在的目录,比如/rango/category/computers,你将会看到页面不存在的信息.

![rango2.png](../figures/rango2.png)

8.练习

+ 修改index页面也包含5个最多访问的页面.

9.提示

+ 修改population脚本,为每个页面增加浏览次数.

## 有趣的表单

Django自带表单系统使在web上收集用户信息变得简单.通过Django’s documentation on forms我们知道表单处理功能包含以下:

+ 显示一个HTML表单自动生成的窗体部件(比如一个文本字段或者日期选择器).
+ 用一系列规则检查提交数据.
+ 验证错误的情况下将会重新显示表单.
+ 把提交的表单数据转化成相关的Python数据类型.

使用Django表单功能最大的好处就是它可以节省你的大量时间和HTML方面的麻烦.这部分我们将会注重如何通过表单让用户增加目录和页面.

1.基本流程

基本步骤包括创建表单和允许用户通过表单输入数据.

+ 在Django应用目录创建forms.py来存储和表单相关的类.
+ 为每个使用表单的模块创建ModelForm类.
+ 定制你的表单.
+ 创建或修改表单的视图,包括展示表单,存储表单数据,当用户输入错误数据(或者根本没有输入)时显示错误标志.
+ 创建或修改你表单的模板.

为新视图增加urlpattern映射(如果你创建了一个新的).
这个流程将会比先前的都复杂些,我们创建的视图也会非常复杂.但是孰能生巧,如果多练几次就非常好掌握了.

2.页面和目录表单

首先,我们需要在rango应用目录里创建叫做forms.py文件.尽管这步我们并不需要,我们可以把表单放在models.py里,但是这将会使我们的代码简单易懂.

在rango的forms.py模块里我们将会创建一些继承自ModelForm的类.实际上,ModelForm是一个帮助函数,它允许你在一个已经存在的模型里创建Django表单.因为我们定义了两个模型(Category和Page),我们将会分别为它们创建ModelForms.

在rango/forms.py添加下面代码:

    #coding:utf-8
    from django import forms
    from rango.models import Page, Category

    class CategoryForm(forms.ModelForm):
        name = forms.CharField(max_length=128, help_text="Please enter the category name.")
        views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
        likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
        slug = forms.CharField(widget=forms.HiddenInput(), required=False)

        # 内部类
        class Meta:
            # model建立表单和模型类的关联，fields里包含表单显示出来的字段
            model = Category
            fields = ('name',)

    class PageForm(forms.ModelForm):
        title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
        url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
        views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

        class Meta:
            # model建立表单和模型类的关联，排除exclude里包含的字段，其它字段显示
            model = Page
            exclude = ('category',)
            #fields = ('title', 'url', 'views')


值得注意的是Django1.7+需要通过fields指定包含的字段,或者通过exclude指定排除的字段.

Django为我们提供了许多定制表单的方法.在上面的例子中,我们指定了我们想要展示字段的窗口部件.例如在我们的PageForm类中,我们为title字段定义forms.CharField,为url字段定义forms.URLField.两个字段都为用户提供文本输入.注意字段里包含max_length参数,它定义字段最大长度.

可以看到在每个表单都包含浏览和喜欢的IntegerField字段.我们可以在参数里设置widget=forms.Hiddeninput()来隐藏窗口组件,设置initial=0来设置默认值为0.这是不用用户去自己设置字段为0的一种方法.然而可以在PageForm看到,尽管我们隐藏了字段,但是我们还是得在表单里包含字段.如果fields排除了views,那么表单将不包含字段(尽管已经定义了)而且将不会返回给模型0值.由于模型建立的不同有可能会引起一个错误.如果在模型里我们把这些字段定义为default=0那么我们可以自动的返回默认值,从而避免not null错误.在这种情况下就不需要隐藏字段了.在表单里我们也包含了slug字段并设置为widget=forms.HiddenInput()值,这里我们并没给他设置初始值或者默认值,而是设置为不需要(required=False).这是因为我们的模型将会负责填充字段.实际上,当你定义模型和表单时一定要注意表单一定要包含和传递所有的数据.

除了CharField和IntegerField组件还有许多.例如,Django提供了EmailField(e-mail地址入口),ChoiceField(输入按钮)和DateField(日期/时间入口).有许多其他不同种类字段可以使用,他们可以为你检查执行错误(例如是否提供了一个有效的整数?).强烈建议你看一下official Django documentation on widgets来定制自己的组件.

或许继承ModelForm最大的作用就是需要定义我们要给哪个模型提供表单.我们通过Meta类来实现.在Meta类设置model属性为我们需要使用的模型.例如CategoryForm类引用Category模型.这对Django创建我们想要的模型表单至关重要.它还可以帮助我们在存储和展示表单数据时获取错误.

我们也可以用Meat类来定义我们希望包括的表单字段.用fields元组来定义所需包含的字段.

        `注意:强烈建议查看 official Django documentation on forms来获取更多.`

3.创建增加目录视图

创建CategoryForm类以后,我们需要创建一个新的视图来展示表单并传递数据.在rango/views.py中增加如下代码.

    from rango.forms import CategoryForm

    def add_category(request): 
        if request.method == 'POST':
            form = CategoryForm(request.POST)
            if form.is_valid():
                form.save(commit=True)
                return index(request)
            else:
                print form.errors
        else:
            form = CategoryForm()
        return render(request, 'rango/add_category.html', {'form': form})


新的add_category()视图增加几个表单的关键功能.首先,检查HTTP请求方法是GET还是POST.我们根据不同的方法来进行处理,例如展示一个表单(如果是GET)或者处理表单数据(如果是POST) ,所有表单都是相同URL.add_category()视图处理以下三种不同情况:

+ 为添加目录提供一个新的空白表单;
+ 保存用户提交的数据给模型,并转向到Rango主页;
+ 如果发生错误,在表单里展示错误信息.


Django表单处理数据是用户浏览器的HTTPPOST请求实现.它不仅可以存储表单数据,而且还能对每个表单字段自动生成错误信息.这就意味着Django将不会存储表单的错误信息以保护数据库的数据完整性.例如如果目录名为空的话将会返回不能为空的错误.

注意到render()中将会调用add_category.html模板,这个模板包含表单和页面.


4.创建增加目录模板

创建templates/rango/add_category.html文件.

    <!DOCTYPE html>
    <html>
    <head>
        <title>Rango</title>
    </head>
    <body>
        <h1>Add a Category</h1>

        <form id="category_form" method="post" action="/rango/add_category/">

            {% csrf_token %}
            {% for hidden in form.hidden_fields %}
                {{ hidden }}
            {% endfor %}

            {% for field in form.visible_fields %}
                {{ field.errors }}
                {{ field.help_text }}
                {{ field }}
            {% endfor %}

            <input type="submit" name="submit" value="Create Category" />
        </form>
    </body>
    </html>


注意:使用隐藏和可见表单字段是因为HTTP是无状态协议.你不可以在两个不同的HTTP请求之间保持状态,因为实现起来相当复杂.为了摆脱这个限制,创建隐藏的HTML表单字段可以使web应用传递给用户HTML表单重要的数据,只有用户提交的时候才会返回数据.
可能你也注意到了代码{% csrf_token %},这是跨站请求伪造令牌,有助于保护我们提交表单的HTTPPOST方法的安全.Django框架要求使用CSRFtoken.如果忘记在你的表单里包含CSRF令牌,有可能会在提交表单时遇到错误.查看 official Django documentation on CSRF tokens 以获取更多信息.

            
            from django.views.decorators.csrf import csrf_exempt
            @csrf_exempt


5.映射增加目录视图

现在我们需要映射add_category()视图.在模板里我们使用/rango/add_category/URL来提交.所以我们需要修改rango/urls.py的urlpattterns.

    urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^add_category/$', views.add_category, name='add_category'), # NEW MAPPING!
        url(r'^category/(?P<category_name_slug>[\\w\-]+)/$', views.category,    name='category'),
    )

6.修改主页内容

作为最后一步,让我们在首页里加入链接.修改rango/index.html文件,在`</body>`前添加如下代码.

`<a href="/rango/add_category/">Add a New Category</a><br />`

7.Demo

现在试一试!启动Django服务,进入http://127.0.0.1:8000/rango/.用新加的链接跳转到增加目录页面,然后增加页面.下图是增加目录和首页截图.

![rango3.png](../figures/rango3.png)


8.创建增加页面视图

下一步是要求用户对于给出的目录增加页面.我们需要重复上面相同的流程，创建一个新的视图(add_page()),一个新的模板(rango/add_page.html),URL映射和在目录页面增加一个链接.

    from rango.forms import PageForm

    def add_page(request, category_name_slug):
        try:
            cat = Category.objects.get(slug=category_name_slug)
        except Category.DoesNotExist:
            cat = None

        if request.method == 'POST':
            form = PageForm(request.POST)
            if form.is_valid():
                if cat:
                    page = form.save(commit=False)
                    page.category = cat
                    page.views = 0
                    page.save()
                    # probably better to use a redirect here.
                    return category(request, category_name_slug)
                else:
                    print form.errors
        else:
            form = PageForm()

        context_dict = {'form':form, 'category': cat}
        return render(request, 'rango/add_page.html', context_dict)

9.创建添加页面模板

创建rango/add_page.html文件

    <!DOCTYPE html>
    <html>
    <head>
	<title>Rango</title>
    </head>
    <body>
	<h1>Add a page</h1>
	<form id="page_form" method="post" >
	{% csrf_token %}
	{% for hidden in form.hidden_fields %}
		{{hidden}}
	{% endfor %}

	{% for field in form.visible_fields %}
		{{ field.errors }}
		{{ field.help_text }}
		{{ field }}
	{% endfor %}
		<input type="submit" name="submit" value="Create Page" />
		<input type="reset" value="reset" id="reset" name="reset" />
	</form>
    </body>
    </html>

10.添加页面URL映射

    urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^add_category/$', views.add_category, name='add_category'), # NEW MAPPING!
        url(r'^category/(?P<category_name_slug>[\\w\-]+)/$', views.category,    name='category'),
        url(r'^category/(?P<category_name_slug>[\\w\-]+)/add_page/$', views.add_page, name='add_page'),
    )

11.修改category视图

    def category(request, category_name_slug):
        context_dict = {} 
        try:
            category = Category.objects.get(slug=category_name_slug)
            context_dict['category_name'] = category.name
            pages = Page.objects.filter(category=category)
            context_dict['pages'] = pages
            context_dict['category'] = category
	        context_dict['category_name_slug']=category_name_slug #新加
        except Category.DoesNotExist:
            pass
        return render(request, 'rango/category.html', context_dict)

12.修改category.html

    <!DOCTYPE html>
    <html>
    <head>
    <title>Rango</title>
    </head>

    <body>
    <h1>{{ category_name }}</h1>

    {% if category %}
        {% if pages %}
        <ul>
            {% for page in pages %}
            <li><a href="{{ page.url }}">{{ page.title }}</a></li>
            {% endfor %}
        </ul>
        {% else %}
            <strong>No pages currently in category.</strong>
        {% endif %}
    {% else %}
        The specified category {{ category_name }} does not exist!
    {% endif %}
    <a href="/rango/category/{{category_name_slug}}/add_page/">Add a New page</a><br />
    </body>
    </html>

13.二次处理表单（选作）

我们Page模型有一个url属性设置为URLField类型.在相应的HTML表单,Django希望任何文本输入的URL字段是一个完整的URL.然而,用户能发现输入像http://www.url.com这种形式有些繁琐。

设想有时候用户输入并不是一定正确,我们可以重写ModelForm模块里clean()方法.这个方法会在表单数据存储到模型实例之前被调用,所以它可以让我们验证甚至修改用户输入的数据.在我们上面的例子中,我们可以检查url字段的值是否以http://开头，如果不是，我们可以在用户前面添加上http://.

    class PageForm(forms.ModelForm):
        ...
        #url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
        url = forms.CharField(max_length=200, help_text="Please enter the URL of the page.")

 以下实验只能把class PageForm中，URLField字段换成CharField字段。


    class PageForm(forms.ModelForm):

    ...

        def clean(self):
            cleaned_data = self.cleaned_data
            url = cleaned_data.get('url')
            if url and not url.startswith('http://'):
                url = 'http://' + url
                cleaned_data['url'] = url

            return cleaned_data

在clean()方法里.

表单数据的字典从ModelForm的cleaned_data属性获取.
你希望检查的表单字段可以在cleaned_data字典中获取.使用.get()字典方法获取表单值.如果用户没有表单字段,那么cleaned_data字典就没有这项.在这种情况下.get()会返回None而不是引发异常.这将会是你的代码更加简洁!
处理你希望处理的表单字段.如果输入了一个值,检查这个值.如果不是你希望的值,你可以在存储到cleaned_data字典之前增加一些逻辑来修改这个值.
必须每次都是以返回cleaned_data字典来结束clean()方法.如果没有将会得到错误提示.
这个小例子说明如何在表单数据存储之前进行修改.这是非常方便的,尤其是有一些字段需要设定默认值时，或者表单中的数据发生了丢失.

注意:重写方法是Django框架提供给我们增加应用额外功能的一种优雅的方法.就像ModelForm模块中clean()方法一样,Django提供了许多安全的方法可以供你重写.


14.提示

+ 修改category()视图,把category_name_slug加入进视图的context_dict字典.
+ 修改category.html添加/rango/category/\<category_name_url\>/add_page/链接.
+ 确保只有请求的目录存在时才会出现链接，页面存在或不存在皆可.例如,在模板用{% if category %} .... {% else %} A category by this name does not exist {% endif %}.
+ 在rangp/urls.py修改URL映射.


## 用户验证

接下来将教会你Django的用户验证机制.我们将会使用Django标准包django.contrib.auth的auth应用.

+ 用户.
+ 权限:一系列的二进制标志(例如 yes/no)决定用户可以做或不可以做什么.
+ 群组:为不止一个用户提供权限的方法.
+ 用户登录的表单和视图工具,还有限制内容.

在用户验证方面Django可以做很多.我们将从基础开始学习.这将非常有利于建立使用它们的信心和它们运行的理念.

### 设置验证

在你使用Django的验证之前,你需要确定在你的rango项目的settings.py文件里已经设置了相关内容.在settings.py文件里找到INSTALLED_APPS元组,检查django.contrib.auth和django.contrib.contenttypes是否在元组里.

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'rango',
    )


django.contrib.auth为Django提供访问认证系统,django.contrib.contenttypes可以通过认证的应用程序来跟踪安装的数据库模型.

注意:如果你需要在INSTALLED_APPS元组里添加auth应用,你需要用命令python manage.py migrate来进行更新数据库.

密码默认将会用 PBKDF2 algorithm进行储存,它可以安全的保存你用户的数据.Django还提供了使用不同的哈希算法来提高安全等级.

如果你希望控制使用哪种哈希算法,你需要在settings.py里加入PASSWORD_HASHERS元组:

    PASSWORD_HASHERS = (
        'django.contrib.auth.hashers.PBKDF2PasswordHasher',
        'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    )

Django将会使用PASSWORD_HASERS里的第一个哈希算法(例如 settings.PASSWORD_HASHERS[0]).

然而在默认情况下你不需要修改PASSWORD_HASHERS,Django默认添加django.contrib.auth.hashers.PBKDF2PasswordHasher.

### 用户模型

Django认证系统最重要的部分就是User对象,它位于django.contrib.auth.models.User.一个User对象代表了和Django应用交互的用户.

User模型主要有5个属性.它们是:

+ 账户的用户名
+ 账户密码
+ 用户邮箱地址
+ 用户名
+ 用户姓

模型也有其他一些属性像is_active(决定账户是活动还是非活动状态).查看official Django documentation on the user model,这里有完整的User模型属性列表.


### 增加用户属性

如果你希望在User模型里加入其他属性,你需要创建一个和User模型相关的模型.对于我们的rango应用,我们希望为我们的用户增加两个属性.我们希望包含:

+ URLField - 允许用户写明自己的网站
+ ImageField - 允许用户在它们的档案里添加图片

可以再rango的models.py文件里增加模型.让我们加入UserProfile模型:

    from django.contrib.auth.models import User

    class UserProfile(models.Model):
        user = models.OneToOneField(User)
        website = models.URLField(blank=True)
        picture = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username

注意我们在User模型里使用一对一关系.因为我们使用了默认User模型,我们需要在models.py文件中导入.

在这里我们还可以直接继承User模型来增加这些字段.但是因为其他应用也可能需要存取User模型,所以这里不建议使用继承,而是使用一对一关系来代替.

对于rango我们已经增加了两个字段来完善用户档案,还提供了一个`__unicode__()`方法返回实例名称.

对于website和picture两个字段,我们都设置了blank=True.它会使所有的字段都为空,意味着用户不必为每一个都设置字段值.

注意ImageField字段有一个upload_to属性.这个属性值连接着MEDIA_ROOT设置用来提供上传文档图片的路径.例如,MEDIA_ROOT设置为<workspace>/itcast_project/media/,那么upload_to=profile_imges将会使图片保存在<workspace>/itcast_project/media/profile_images/目录.

`警告:DjangoImageField使用python图片库(pillow).我们在安装Django时已经讲过如何安装pillow.如果还没有安装现在就可以安装了.如果你没有安装pillow,那么将会遇到pillow模块不能找到的错误!
定义完UserProfile模型,我们需要修改rango的admin.py文件使管理界面包含UserPrifile模型.在admin.py文件里添加如下.`

    from rango.models import UserProfile

    admin.site.register(UserProfile)

注意:我们在修改模型后需要更新数据库.

    python manage.py makemigrations rango
    python manage.py migrate.

### 创建用户注册表单，视图和模板

注意:这里有许多现成的用户注册包可以使用,它们大大的减少创建注册和表单的繁琐程度.
为用户提供注册服务我们需要以下几步:

+ 创建UserForm和UserProfileForm.
+ 增加创建新用户视图.
+ 增加展示UserForm和UserProfileForm的模板.
+ 映射URL.
+ 在主页放置注册页链接

### 注册表单

在rango/forms.py中,我们需要创建两个继承自forms.ModelForm的类.一个是为User模型创建的,一个是为UserProfile创建的.这两个继承自ModelForm的类给我们提供展示HTML表单所需要的表单字段.

在rango/forms.py文件,让我们创建这两个类.

    from django import forms
    from django.contrib.auth.models import User
    from rango.models import Category, Page, UserProfile

    class UserForm(forms.ModelForm):
        password = forms.CharField(widget=forms.PasswordInput())
        class Meta:
            model = User
            fields = ('username', 'email', 'password')

    class UserProfileForm(forms.ModelForm):
        class Meta:
            model = UserProfile
            fields = ('website', 'picture')

注意到在两个类中我们都加入了Meta类.在Meta类中所有定义都会被当做它的附加属性.每个Meta至少包含一个model字段,它可以和模型之间关联.例如在我们的UserForm类中就关联了User模型.在Django1.7+中你可以用fields或者exclude来定义你需要展示的字段.

这里我们仅仅需要展示User模型的username,email和password字段,和UserProfile模型的website和picture字段.当用户注册的时候我们需要连接UserPrifile模型的user字段.

看到了吧UserForm包含一个定义password属性.当User模型实例默认包含password属性时,HTML表单元素将不会隐藏密码.如果用户输入密码,那么这个密码就会可见.所以我们修改password属性作为CharField实例并使用PasswordInput()组建,这时用户输入就会被隐藏.


### 创建register视图

下面我们处理表单和表单输入的数据.在rango的views.py文件,加入下面视图函数:

    from rango.forms import UserForm, UserProfileForm

    def register(request):
        registered = False
        if request.method == 'POST':
            user_form = UserForm(data=request.POST)
            profile_form = UserProfileForm(data=request.POST)
            if user_form.is_valid() and profile_form.is_valid():
                user = user_form.save()
                user.set_password(user.password)
                user.save()
                profile = profile_form.save(commit=False)
                profile.user = user

                if 'picture' in request.FILES:
                    profile.picture = request.FILES['picture']

                profile.save()
                registered = True
            else:
                print user_form.errors, profile_form.errors
        else:
            user_form = UserForm()
            profile_form = UserProfileForm()
        return render(request,'rango/register.html',
                        {'user_form': user_form, 
                        'profile_form': profile_form, 
                        'registered': registered} )


和我们前面add_category()视图差不多,仅仅添加了两个不同的ModelForm实例,一个是User模型的,另一个是UserProfile模型的.如果用户上传图像我们还得需要处理它们.

我们还需要创建两个模型实例之间的连接.创建新的User模型实例后,我们需要用profile.user = user把它关联到UserProfile实例.

### 创建注册模板

现在我们创建rang/register.html加入如下代码:

    <!DOCTYPE html>
    <html>
    <head>
        <title>Rango</title>
    </head>

    <body>
        <h1>Register with Rango</h1>

        {% if registered %}
        Rango says: <strong>thank you for registering!</strong>
        <a href="/rango/">Return to the homepage.</a><br />
        {% else %}
        Rango says: <strong>register here!</strong><br />

        <form id="user_form" method="post" action="/rango/register/"
                enctype="multipart/form-data">

            {% csrf_token %}

            <!-- Display each form. The as_p method wraps each element in a paragraph
                 (<p>) element. This ensures each element appears on a new line,
                 making everything look neater. -->
            {{ user_form.as_p }}
            {{ profile_form.as_p }}

            <!-- Provide a button to click to submit the form. -->
            <input type="submit" name="submit" value="Register" />
        </form>
        {% endif %}
    </body>
    </html>

这个HTML模板使用registered变量来检测注册是否成功.当registered为False时模板会展示注册表单,否则,除了标题外它只会展示一条成功信息.
    
`警告:你可能注意到在<form>元素里的enctype属性.当你希望用户通过表单上传文件时,必须把enctype设置成multipart/form-data.这个属性会让你的浏览器以特定的方式把表单数据返回给服务器.实际上,你的文件会被分成一块块的传输.想了解更多查看 this great Stack Overflow answer.你也应当记得加入CSRF令牌.确保在你的<form>属性里包含{% csrf_token %}.`


### 视图register的URL映射

现在为我们的新视图加入URL映射.在rango/urls.py文件里修改urlpatterns元组如下:


    urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^category/(?P<category_name_slug>[\\w\-]+)/$', views.category,name='category'), 
        url(r'^add_category/$', views.add_category, name='add_category'), 
        url(r'^category/(?P<category_name_slug>[\\w\-]+)/add_page/$', views.add_page, name='add_page'),
        url(r'^register/$', views.register, name='register'),  # New!
    )
 
新加入的模式的URL,rango/register/指向register()视图.

### 主页建立索引

最后,我们需要在主页index.html模板里加入链接.在添加目录链接后加入下面链接.

    <a href="/rango/register/">Register Here</a>

### Demo

![Rango](../figures/rango5.png)

![Register](../figures/rango6.png)

现在你可以点击Register Here超链接进入到注册页面.现在试试看!启动你的Django服务试着注册一个账户.如果你愿意可以上传一个个人图片.你的注册表单看起来像下面一样.

### 增加登录功能

完成了注册功能,我们需要添加登录的功能.我们需要做以下几步:

+ 创建登录视图处理用户验证
+ 创建登录模板展示登录表单
+ 映射url
+ 在首页提供登录表单链接

1>创建login()视图

在rango/views.py创建user_login()函数,代码如下:

    def user_login(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/rango/')
                else:
                    return HttpResponse("Your Rango account is disabled.")
            else:
                print "Invalid login details: {0}, {1}".format(username, password)
                return HttpResponse("Invalid login details supplied.")
        else:
            return render(request, 'rango/login.html', {})

这个视图可能看起来相当的复杂.和前面的例子一样,user_login()视图负责处理和传递表单.

首先,如果访问视图的方式是HTTP GET,那么就会展示登录表单.如果是通过HTTP POST,那么它将对表单进行处理.

如果表单被发送,那么用户名和密码将会从表单中抽离出来.它们将会被用作验证用户(使用Django的authenticate()函数).如果用户名/密码在数据库中存在authenticate()就会返回一个User对象 - 反之则会返回None.

如果我们查找一个User对象,我们可以检查账户是处于激活或非激活状态 - 然后会返回浏览器相应的状态.

然而如果发送了无效的表单,是因为没有添加用户名和密码导致返回错误信息(例如用户名/密码丢失).

上面代码最有意思的是用Django内建的机制来实现验证过程.authenticate()函数用来检查用户名和密码是否和账户匹配,而login()函数用来标记用户登录.

你也可能注意到我们使用了HttpResponseRedirect类.看到名字就猜到了,最后代码返回的是一个HttpResponseRedirect类实例,它的参数是一个跳转地址,用来使用户的浏览器跳转到该地址.注意它返回的状态码不是正常状态下的200而是302,它表示一个重定向.参看official Django documentation on Redirection以获取更多信息.

所有的这些函数和类都在Django之中,所以你需要导入它们,在rango/views.py中加入下面.

    from django.contrib.auth import authenticate, login
    from django.http import HttpResponseRedirect, HttpResponse

2>创建登录模板

我们已经创建完视图,所以接下来我们需要创建登录模板了.我们知道模板存储在templates/rango/目录,所以我们在这里创建login.html文件,代码如下:

    <!DOCTYPE html>
    <html>
        <head>
            <!-- Is anyone getting tired of repeatedly entering the header over and over?? -->
            <title>Rango</title>
        </head>

        <body>
            <h1>Login to Rango</h1>

            <form id="login_form" method="post" action="/rango/login/">
                {% csrf_token %}
                Username: <input type="text" name="username" value="" size="50" />
                <br />
                Password: <input type="password" name="password" value="" size="50" />
                <br />

                <input type="submit" value="submit" />
            </form>

        </body>
    </html>

确保在inputname属性要和user_login()视图里的名字相同 - 例如,username作为用户名,password作为密码.同时不要忘记{% csrf_token %}!

3>添加登录视图URL映射

接下来我们需要对user_login()视图映射URL.修改urls.py文件里的urlpatterns元组如下.

    urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^category/(?P<category_name_slug>\w+)$', views.category, name='category'),
        url(r'^add_category/$', views.add_category, name='add_category'),
        url(r'^category/(?P<category_name_slug>\w+)/add_page/$', views.add_page, name='add_page'),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        )

4>添加链接

最后一步是为我们的登录页提供链接.所以我们需要修改在tmplates/rango目录里的index.html文件.找到先前创建的增加目录链接和注册链接,在后面添加.如果你希望进行分割以下可以在链接前面包含(<br />).

    <a href="/rango/login/">Login</a>

在头部替换下面的代码.注意到我们使用了user对象,它是通过上下文传递给Django的模板的.通过它我们可以知道用户是否登录(验证).如果用户登录了我们可以提供给详细信息.

    {% if user.is_authenticated %}
    <h1>Rango says... hello {{ user.username }}!</h1>
    {% else %}
    <h1>Rango says... hello world!</h1>
    {% endif %}

正如你看到的我们用Django模板语言{% if user.is_authenticated %}来检查用户是否通过验证.如果用户成功登录那么我们传递给模板的上下文变量会包含一个用户变量 - 所以我们可以检查用户是否登录.如果登录用户会得到一个欢迎用户的信息,比如Rango says... hello itcast!.否则的话只会返回Rango says... hello world!通用的欢迎信息.

5>Demo

看看是否和下面图片一样.


### 限制访问

现在用户可以登录Rango,现在我们需要对一些特殊的部分限制访问,例如只有注册用户才能增加目录和页面.在Django里我们有两种方法实现这个功能:

通过检查request对象和检查用户是否登录.
用一个方便的装饰器来检查用户是否登录.
第一个是通过user.is_authenticated()方法查看用户是否登录.user对象是通过request对象传递给视图的.下面是简单的例子.

    def some_view(request):
        if request.user.is_authenticated():
            return HttpResponse("You are logged in.")
        else:
            return HttpResponse("You are not logged in.")

第二个是使用了python装饰器.装饰器是由一种软件设计模式命名的.它们可以动态的修改一个函数,方法或者类而不用去直接修改它们的源代码.

Django提供了叫做login_required()的装饰器,它可以在视图里要求用户进行登录.如果一个用户没有登录并且尝试访问一个视图,那么这个用户将会重定向到你设定的页面,通常是一个登录页面.

#### 使用装饰器进行限制访问

我们尝试在views.py文件里调用retricted(),代码如下:

    @login_required
    def restricted(request):
        return HttpResponse("Since you're logged in, you can see this text!")

这里我们用了一个装饰器,它位于函数定义前,并且用@符号开头.Python会在执行函数/方法前执行装饰器.在使用装饰器前同样需要导入,像下面一样导入:

    from django.contrib.auth.decorators import login_required

同样的还是要在urls.py文件的urlpatterns元组进行修改.我们的元组看起来和下面的例子一样.

    urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^add_category/$', views.add_category, name='add_category'),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^(?P<category_name_slug>\w+)', views.category, name='category'),
        url(r'^restricted/', views.restricted, name='restricted'),
        )

我们同样需要处理用户未登录时的restricted()视图.我们怎么做呢?最简单的就是重定向用户的浏览器.Django允许我们自定义项目里的settings.py文件.在settings.py文件里设置LOGIN_URL变量为我们希望跳转的URL,例如登录页位于/rango/login/:

    LOGIN_URL = '/rango/login/'

这就确保用户在没有登录的情况下直接跳转至/rango/login/.

### 注销

确保用户能够优雅的注销需要给用户提供注销的选项.Django的logout()函数将会确保用户注销,以及终止它们的会话,如果用户随后继续访问视图,将会拒绝它们的请求.

在rango/views.py中加入user_logout()函数:

    from django.contrib.auth import logout

    @login_required
    def user_logout(request):
        # Since we know the user is logged in, we can now just log them out.
        logout(request)

        # Take the user back to the homepage.
        return HttpResponseRedirect('/rango/')

同样我们需要给user_logout()添加URL映射,打开urls.py文件修改urlpaatterns元组:

    urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^category/(?P<category_name_slug>\w+)$', views.category, name='category'),
        url(r'^add_category/$', views.add_category, name='add_category'),
        url(r'^category/(?P<category_name_slug>\w+)/add_page/$', views.add_page, name='add_page'),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^restricted/$', views.restricted, name='restricted'),
        url(r'^logout/$', views.user_logout, name='logout'),
        )

现在我们已经完成了用户注销的功能,我们需要在主页上创建一个链接,当用户点击即可进行注销.但是对于没有登录的用户来说这个链接就毫无意义了.最好是这样当用户没有登录时我们可以提供一个注册的链接.

和前面的章节一样,我们需要修改index.html模板,使用模板上下文中的user对象来决定我们需要现实什么链接.在页面底部找到链接列表用下面的HTML代替它.注意别忘了加入注册页面的链接/rango/restricted/.

    {% if user.is_authenticated %}
    <a href="/rango/restricted/">Restricted Page</a><br />
    <a href="/rango/logout/">Logout</a><br />
    {% else %}
    <a href="/rango/register/">Register Here</a><br />
    <a href="/rango/login/">Login</a><br />
    {% endif %}

    <a href="/rango/about/">About</a><br/>
    <a href="/rango/add_category/">Add a New Category</a><br />

当用户验证登录后,就能看到Restricted Page和Logout链接.如果用户没有登录,就会显示Register Here和Login.About和Add a New Category并不在模板的条件代码里,这两个链接在用户匿名或登录时都可以看见.


## 使用模板

到目前为止我们已经为我们应用里许多的不用页面创建了Django HTML模板.可能你已经注意到了在模板里有许多重复的HTML代码.

大多数网站将会有大量重复的结构(例如顶部,则边栏,底部等等),在每个模板中重复这些HTML可不是一个好的方法.在Django模板语言中使用它提供的继承功能可以减少代码大量的冗余,而不是做大量的重复复制和粘贴.

基本的模板继承步骤如下:

+ 定义应用里每个页面重复出现的部分(例如标题栏,侧边栏,底部,内容窗格)

+ 在基础模板里提供页面基本的框架和通用内容(例如在页底的版权声明,以及页面中的标识和标题),然后定义一些代码段,用户可以定义需要的代码段.

+ 创建具体的模板 - 它们都继承自基础模板 - 并且制定每个块的内容.

### 1.重复的HTML和基础模板

很明显我们创建的几个模板都有很多重复的HTML代码.下面我们抽离出每个模板中都重复的部分.

    <!DOCTYPE html>

    <html>
        <head>
            <title>Rango</title>
        </head>

        <body>
            <!-- Page specific content goes here -->
        </body>
    </html>

从现在开始让它做我们的基础模板,并且包存在templates目录的base.html文件(例如 templates/base.html)

    注意:应当尽可能多的抽离出重复的内容.虽然在开始的时候会有一些困难,但是一旦做完以后会省下大量的时间.想想吧:你希望看到许多同样代码的拷贝吗?
    警告:<!DOCTYPE html>必须放在页面的第一行!不这样做将意味着你的标记不符合W3C HTML5准则。

### 2.模板块

现在我们已经定义了我们的基础模板,我们可以把它变为我们需要继承的模板.我们需要在模板中加入一个模板标签以便于我们能在基础模板里重写 - 这需要用到blocks.

在基础模板里增加body_block如下.

    <!DOCTYPE html> 
    <html>
        <head lang="en">
            <meta charset="UTF-8">
            <title>Rango</title>
        </head>

        <body>
            {% block body_block %}{% endblock %}
        </body>
    </html>

用{%和%}标签调用标准的Django模板命令.为了开启一个块,模板命令是block <NAME>,这里<NAME>是你希望创建块的名字.最后需要保证用endblock命令关闭块.

你也可以再块中设置'默认内容',例如:

    {% block body_block %}This is body_block's default content.{% endblock %}

当我们创建模板时我们会继承base.html和重写body_block里的内容.你也可以在模板中放置更多的块,例如,你可以分别为页面标题,底部,侧边栏设置块.Django模板系统中的块十分的有用, official Django documentation on templates查看更多内容.

#### 更多的抽象

既然已经理解了Django块,让我们抽象出更多的基础模板.重新打开base.html模板修改如下.

    <!DOCTYPE html>
    <html>
        <head>
            <title>Rango - {% block title %}hello itcast!{% endblock %}</title>
        </head>
        <body>
            <div>
                {% block body_block %}{% endblock %}
            </div>
            <hr />
            <div>
                <ul>
                {% if user.is_authenticated %}
                    <li><a href="/rango/restricted/">Restricted Page</a></li>
                    <li><a href="/rango/logout/">Logout</a></li>
                    <li><a href="/rango/add_category/">Add a New Category</a></li>
                {% else %}
                    <li><a href="/rango/register/">Register Here</a></li>
                    <li><a href="/rango/login/">Login</a></li>
                {% endif %}
                    <li><a href="/rango/about/">About</a></li>
                </ul>
            </div>
        </body>
    </html>

我们在模板中引入两个新的特性.

第一个是加入新的Django模板块title.所以我们可以为继承自基础模板的页面定制标题.如果页面没有使用这个块,那么这个标题会默认为Rango - hello itcast!.

我们也可以把index.html模板中的链接列表加入到body_block块的后部.这将会为所有继承基础模板的页面展示这些链接.可以在body_block内容和链接之间加入一个水平线,以便我们区分这两部分.

注意我们的body_block包含在HTML<div>标签里 - <div>意义相当于一个区块.我们的链接同样使用<ul>和<li>标签包含在HTML无序列表里.

### 3.模板继承

我们已经创建了带块的基础模板,现在我们需要修改那些继承基础模板的模板.例如,让我们重构rango/category.html模板.

首先我们需要移除所有重复的HTML代码和模板标签/命令.然后加入代码:

    {% extends 'base.html' %}

extends命令携带一个参数,这个参数是要继承的模板(例如 rango/base.html).然后修改category.html模板如下.

注意:提供给extends命令的参数的默认路径是项目的templates目录.例如,Rango所有模板应当是从rango/base.html扩展而不是base.html.

    {% extends 'base.html' %}

    {% load staticfiles %}

    {% block title %}{{ category_name }}{% endblock %}

    {% block body_block %}
        <h1>{{ category_name }}</h1>
        {% if category %}
            {% if pages %}
            <ul>
                    {% for page in pages %}
                    <li><a href="{{ page.url }}">{{ page.title }}</a></li>
                    {% endfor %}
                    </ul>
            {% else %}
                    <strong>No pages currently in category.</strong>
                    {% endif %}

            {% if user.is_authenticated %}
                    <a href="/rango/category/{{category.slug}}/add_page/">Add a Page</a>
                    {% endif %}
            {% else %}
                     The specified category {{ category_name }} does not exist!
        {% endif %}

    {% endblock %}

在category.html模板里使用extends命令来继承base.html.在这里你不需要写一个完整的HTML文档,因为base.html已经提供了一个完整的框架.你只要把增添的内容写到基础模板里,它就会创建一个完整的HTML文档发送给用户浏览器.

    注意:模板非常强大,你甚至可以创建你自己的模板标签.在这里我们将演示如何减小模板里重复的HTML结构. 然而,模板可以减小应用视图里的代码.例如,如果你想在你的应用增加一些相同的数据库驱动的内容,你需要调用特定的视图来处理网页中重复的部分.这样在每个视图里就不用重复调用Django ORM函数来收集数据了. 查看更多内容请查看 Django documentation on templates.

### 4.模板里加入URL

到目前为止我们可以直接的在模板里键入页面/视图的URL,例如<a href="./rango/about/"> About </a>.然而最好的方式是使用url模板标签来查找在urls.py文件中的url.我们需要改写一下.

    <li><a href="{% url 'about' %}">About</a></li>

在这里我们要指定应用和about视图.

现在可以修改基础模板的url模板标签:

    <div>
        <ul>
        {% if user.is_authenticated %}
            <li><a href="{% url 'restricted' %}">Restricted Page</a></li>
            <li><a href="{% url 'logout' %}">Logout</a></li>
            <li><a href="{% url 'add_category' %}">Add a New Category</a></li>
        {% else %}
            <li><a href="{% url 'register' %}">Register Here</a></li>
            <li><a href="{% url 'login' %}">Login</a></li>
        {% endif %}

        <li><a href="{% url 'about' %}">About</a></li>
        </ul>
    </div>

在我们的index.html模板里有一个带参数的url模式,例如category会带一个category.slug参数.在这里你可以使用模板标签来传递这个category.slug参数,例如在模板里写入{% url ‘category’ category.slug %}:

    {% for category in categories %}
        <li><a href="{% url 'category'  category.slug %}">{{ category.name }}</a></li>
    {% endfor %}

备注：官方提供的如何使用模板标签,http://django.readthedocs.org/en/latest/intro/tutorial03.html 这个stackoverflow也很有帮助 http://stackoverflow.com/questions/4599423/using-url-in-django-templates


### 5.练习

完成下面的练习你将会成为Django模板专家.

1.更改所有模板使他们都继承base.html模板.步骤和上面的例子一样.就和下图一样,所有的模板都会继承base.html.当完成后记得删除index.html模板里的链接.我们不再需要它们了!你也可以移除在about.html模板里的链接.

2.在限制页面使用模板.模板取名为restricted.html,并且保证它也继承base.html模板.

3使用url模板标签代替所有的url.

4添加一个地址使用户不论在网站的哪个位置都能返回到主页.

警告:记得在每个模板头部加入{% load static %}以使用静态媒体.如果没有这样做,将会产生一个错误!Django模板模块需要分别单独导入 - 你不可以调用在你扩展的模板里的模块.

![模版继承关系](../figures/rango-template.png)

注意:完成上面的练习后,所有Rango的模板都会继承bashe.html.让我们回过头看看base.html的内容,user对象 - 在Django请求的上下文中 - 将会用来检查当前的Rnago用户是否已经登录(通过使用user.is_authenticated).因为所有的Rango模板都会继承基础模板,所以所有的Rango模板的访问都要依赖于所发送请求的上下文. 因为这个新的依赖,你必须检查每个Rango的Django视图.对于每个视图,确保每个请求对于Django模板引擎都是可用的.通过这个教程,我们通过render()传递请求作为参数来达到这个目的.有时会发生这样的情况,如果你的请求被错误的传送可能出现用户没有登录,但是Django认为已经登录. 这里我们以about视图作为例子来进行检查.开始用硬编码的方式进行,代码如下.注意我们只发送字符串 - 我们没有使用request参数.

    def about(request):
        return HttpResponse('Rango says: Here is the about page. <a href="/rango/">Index</a>')

为了使用模板我们需要调用render函数传递request对象.这将会使我们的模板引擎可以获取像user这样的对象,它可以允许模板引擎查看用户是否登录.(例如进行验证).

    def about(request):
        return render(request, 'rango/about.html', {})

记住,render()最后一个参数是一个字典,它可以添加额外的数据传递给Django模板引擎.因为我们没有什么额外的数据传递给模板所以这里为空.

# AJAX

AJAX即“Asynchronous Javascript And xML”（异步JavaScript和XML），是指一种创建交互式网页应用的网页开发技术。


通过在后台与服务器进行少量数据交换，AJAX可以使网页实现异步更新。这意味着可以在不重新加载整个网页的情况下，对网页的某部分进行更新。

传统的网页（不使用 AJAX）如果需要更新内容，必须重载整个网页页面。

两种在客户端和服务器端进行请求-响应的常用方法是：GET 和 POST。

    GET - 从指定的资源请求数据
    POST - 向指定的资源提交要处理的数据

## jQuery

jQuery 库可以通过一行简单的标记被添加到网页中,jQuery 库的特性:

    jQuery 是一个 JavaScript 函数库。
    HTML 元素选取
    HTML 元素操作
    CSS 操作
    HTML 事件函数
    JavaScript 特效和动画
    HTML DOM 遍历和修改
    AJAX

### 向您的页面添加 jQuery 库

jQuery 库位于一个 JavaScript 文件中，其中包含了所有的 jQuery 函数。

可以通过下面的标记把 jQuery 添加到网页中：
```html

    <head>
    <script type="text/javascript" src="jquery.js"></script>
    </head>

```

    请注意，<script> 标签应该位于页面的 <head> 部分。

### 下载 jQuery

共有两个版本的 jQuery 可供下载：一份是精简过的，另一份是未压缩的（供调试或阅读）。

这两个版本都可从 jQuery.com 下载。

1 和 2 就是1版本支持 ie 6 7 8， 2不支持 的。小版本的差异，会改写新版本浏览器的兼容，加些api等。

库的替代
百度 和 Microsoft 对 jQuery 的支持都很好。
如果您不愿意在自己的计算机上存放 jQuery 库，那么可以从 百度或 Microsoft 加载 CDN jQuery 核心文件。

使用百度的 CDN

```html

    <head>
    <script type="text/javascript" src="http://libs.baidu.com/jquery/1.11.1/jquery.min.js"></script>
    </head>
``` 

使用 Microsoft 的 CDN

```html

    <head>
    <script type="text/javascript" src="http://ajax.microsoft.com/ajax/jquery/jquery-1.4.min.js"></script>
    </head>
```

基础 jQuery 实例,下面的例子演示了 jQuery 的 hide() 函数，隐藏了 HTML 文档中所有的 <p> 元素。

```html

    <html>
    <head>
        <script type="text/javascript" src="http://libs.baidu.com/jquery/1.11.1/jquery.min.js"></script>
        <script type="text/javascript">
            $(document).ready(function(){
                $("button").click(function(){
                    $("p").hide();
                });
            });
        </script>
    </head>

    <body>
        <h2>This is a heading</h2>
        <p>This is a paragraph.</p>
        <p>This is another paragraph.</p>
        <button type="button">Click me</button>
    </body>
    </html>
```


jQuery $.get() 方法

    $.get() 方法通过 HTTP GET 请求从服务器上请求数据。
    语法：
    $.get(URL,callback);
        必需的 URL 参数规定您希望请求的 URL。
        可选的 callback 参数是请求成功后所执行的函数名。


jQuery $.post() 方法

    $.post() 方法通过 HTTP POST 请求从服务器上请求数据。
    语法：
    $.post(URL,data,callback);
        必需的 URL 参数规定您希望请求的 URL。
        可选的 data 参数规定连同请求发送的数据。
        可选的 callback 参数是请求成功后所执行的函数名。
## JSON

JSON的全称是”JavaScript Object Notation”，意思是JavaScript对象表示法，它是一种基于文本，独立于语言的轻量级数据交换格式。XML也是一种数据交换格式，为什么没有选择XML呢？因为XML虽然可以作为跨平台的数据交换格式，但是在JS(JavaScript的简写)中处理XML非常不方便，同时XML标记比数据多，增加了交换产生的流量，而JSON没有附加的任何标记，在JS中可作为对象处理，所以我们更倾向于选择JSON来交换数据。

### JSON 语法规则

JSON 语法是 JavaScript 对象表示法语法的子集。

+ 数据在名称/值对中
+ 数据由逗号分隔
+ 花括号保存对象
+ 方括号保存数组

JSON 名称/值对

+ JSON 数据的书写格式是：名称/值对。
+ 名称/值对包括字段名称（在双引号中），后面写一个冒号，然后是值：
        "firstName" : "John"
        这很容易理解，等价于这条 JavaScript 语句：
        firstName = "John"

JSON 值

+ 数字（整数或浮点数）
+ 字符串（在双引号中）
+ 逻辑值（true 或 false）
+ 数组（在方括号中）
+ 对象（在花括号中）
+ null

JSON 对象

    { "firstName":"John" , "lastName":"Doe" }
    这一点也容易理解，与这条 JavaScript 语句等价：
    firstName = "John"
    lastName = "Doe"

JSON 数组

    {
        "employees": [
            { "firstName":"John" , "lastName":"Doe" },
            { "firstName":"Anna" , "lastName":"Smith" },
            { "firstName":"Peter" , "lastName":"Jones" }
        ]
    }

JSON 使用 JavaScript 语法

因为 JSON 使用 JavaScript 语法，所以无需额外的软件就能处理 JavaScript 中的 JSON。
通过 JavaScript，您可以创建一个对象数组，并像这样进行赋值：
例子

```javascript

    var employees = [
        { "firstName":"Bill" , "lastName":"Gates" },
        { "firstName":"George" , "lastName":"Bush" },
        { "firstName":"Thomas" , "lastName": "Carter" }
    ];
```
可以像这样访问 JavaScript 对象数组中的第一项：

    employees[0].lastName;

返回的内容是：

    Gates

可以像这样修改数据：

    employees[0].lastName = "Jobs";

JSON 文件的文件类型是 ".json"

## 实例1:数据请求

视图文件views.py

```python
    #views.py
    from django.shortcuts import render
    from django.http import HttpResponse


    def index(request):
        return render(request, 'index.html')


    def add(request):
        print request.GET['a']
        print request.GET['b']
        if request.is_ajax():
            a = request.GET['a']
            b = request.GET['b']
            c = int(a) + int(b)
            r = HttpResponse(str(c))
        return r
```

模版文件index.html

```html
    <!DOCTYPE html>
    <html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <title>do ajax</title>
        <script type="text/javascript" src="http://ajax.aspnetcdn.com/ajax/jQuery/jquery-1.8.0.js"></script>

        <script>
        $(document).ready(function(){
          $("#sum").click(function(){
            var a = $("#a").val();
            var b = $("#b").val();
     
            $.get("/ajax/add/",{'a':a,'b':b}, function(ret){
                $('#result').html(ret)
            })
          });
        });
        </script>

    </head>
    <body>

        <p>请输入两个数字</p>
        <form action="/ajax/add/" method="get">
            a:
            <input type="text" id="a" name="a">
            <br>
            b:
            <input type="text" id="b" name="b">
            <br>
            <p>
                result:
                <span id='result'></span>
            </p>
            <button type="button" id='sum'>提交</button>
        </form>

    </body>
    </html>
```

url路由文件

```python

    from django.conf.urls import patterns, include, url
    from django.contrib import admin


    urlpatterns = patterns('',
                           url(r'^admin/', include(admin.site.urls)),
                           url(r'^ajax/', include('ajax.urls')),
                           )
```

## 实例2:字典和列表

视图文件views

```python

    from django.http import HttpResponse
    from django.shortcuts import render
    import json


    def index(request):
        return render(request, 'index.html')


    def add(request):
        a = request.GET['a']
        b = request.GET['b']
        a = int(a)
        b = int(b)
        return HttpResponse(str(a + b))


    def ajax_list(request):
        a = range(100)
        return HttpResponse(json.dumps(a), content_type='application/json')


    def ajax_dict(request):
        name_dict = {'saywhat': 'I love python and Django', 'school': 'Itcastcpp'}
        return HttpResponse(json.dumps(name_dict), content_type='application/json')
```

模版文件index

```html

    <!DOCTYPE html>
    <html>
    <body>
    <p>请输入两个数字</p>
    <form action="/add/" method="get">
        a: <input type="text" id="a" name="a"> <br>
        b: <input type="text" id="b" name="b"> <br>
        <p>result: <span id='result'></span></p>
        <button type="button" id='sum'>提交</button>
    </form>


    <div id="dict">Ajax 加载字典</div>
    <p id="dict_result"></p>

    <div id="list">Ajax 加载列表</div>
    <p id="list_result"></p>


    <script src="http://ajax.aspnetcdn.com/ajax/jQuery/jquery-1.8.0.js"></script>
    <script>
        $(document).ready(function(){
          // 求和 a + b
          $("#sum").click(function(){
            var a = $("#a").val();
            var b = $("#b").val();

            $.get("/add/",{'a':a,'b':b}, function(ret){
                $('#result').html(ret);
            })
          });

          // 列表 list
          $('#list').click(function(){
              $.getJSON('/ajax_list/',function(ret){
                //返回值 ret 在这里是一个列表
                for (var i = ret.length - 1; i >= 0; i--) {
                  // 把 ret 的每一项显示在网页上
                  $('#list_result').append(' ' + ret[i])
                };
              })
          })

          // 字典 dict
          $('#dict').click(function(){
              $.getJSON('/ajax_dict/',function(ret){
                  //返回值 ret 在这里是一个字典
                  $('#dict_result').append(ret.saywhat + ' ' + ret.school + '<br>');
                  // 也可以用 ret['saywhat']
              })
          })
        });
    </script>
    </body>
    </html>
```

url路由文件

```python 

    from django.conf.urls import patterns, include, url
    from django.contrib import admin

    urlpatterns = patterns('',
                           url(r'^admin/', include(admin.site.urls)),

                           url(r'^$', 'ajax.views.index', name='home'),
                           url(r'^add/$', 'ajax.views.add', name='add'),
                           url(r'^ajax_list/$', 'ajax.views.ajax_list',
                               name='ajax-list'),
                           url(r'^ajax_dict/$', 'ajax.views.ajax_dict',
                               name='ajax-dict'),

                           )
``` 


## 实例3:超市管理系统

关闭csrf验证

```python

    #csrf_exempt关闭csrf验证
    from django.views.decorators.csrf import csrf_exempt
    @csrf_exempt
    def fun():
        pass

```

代码见github： [超市管理][1]:https://github.com/xwpfullstack/djangostudy/tree/master/itproject4/mydeb_3
[1]:https://github.com/xwpfullstack/djangostudy/tree/master/itproject4/mydeb_3 "https://github.com/xwpfullstack/djangostudy/tree/master/itproject4/mydeb_3"

下载项目后执行
    
    python manage.py migrate 
    python manage.py createsuperuser
    python populate_fruit.py
    python manage.py runserver

浏览器输入```127.0.0.1:8000/fruit/```

# Bootstrap

# Django部署

![部署速查图](../figures/uwsgi.jpg)


## python虚拟环境 

构造python开发虚拟环境:

    sudo apt-get install python-virtualenv 
    sudo easy_install virtualenvwrapper 
    mkvirtualenv [虚拟环境名称] 
    workon [虚拟环境名称] 
    离开 deactivate 
    rmvirtualenv [虚拟环境名称] 

## 项目开发环境迁移 

    客户端 pip freeze > list 
    在服务器创建python虚拟环境 
    服务器 pip install -r list 

## django项目关闭调试模式 

修改settings.py 

    DEBUG = False 

静态文件需收集出来，由nginx代理去寻找 

    ALLOWED_HOSTS = ['*',] 
    指定可以访问项目的ip，*表示所有 

## uwsgi配置

在虚拟环境里安装（切记）
    pip install uwsgi 

uWSGI.ini文件里设置

socket标识被代理转发(注意，曾经哥遇到过的坑)

http标识自己作为web服务器 

    [uwsgi]
    socket = 127.0.0.1:8000
    #http = 127.0.0.1:8000
    chdir = /home/itcast/workspace/vmaig_blog #项目根目录
    wsgi-file = vmaig_blog/wsgi.py #项目管理目录
    processes = 4
    threads = 2
    master = True
    pidfile = uwsgi.pid
    daemonize = uwsgi.log 

启动uwsgi 

    uwsgi --ini uWSGI.ini 

## nginx配置 

    location / {
        include uwsgi_params;
        uwsgi_pass 127.0.0.1:8000;
    }
    location /static/ {
        alias /var/static/;
    }

nginx重启 

    /usr/local/nginx/sbin/nginx -s reload 

## 收集项目静态资源 

1.在项目的settings.py中设置

    STATIC_ROOT='/var/static' 

2.服务器端创建'/var/static'目录 

    python manage.py collectstatic 


## mysql数据库

pip install MYSQL-python

修改setting.py里面的DATABASES元组为

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'books',    #你的数据库名称
        'USER': 'root',   #你的数据库用户名
        'PASSWORD': '', #你的数据库密码
        'HOST': '', #你的数据库主机，留空默认为localhost
        'PORT': '3306', #你的数据库端口
    }
}

## git管理本地代码和服务器代码同步 

### 架设服务器端Git仓库 

    apt-get install git
    mkdir repo
    cd repo
    git --bare init 

### 创建本地Git并完成第一次推送 

本地

    mkdir source
    cd source
    git init
    touch Readme
    git add Readme
    git commit -m 'init'
    git remote add origin username@servername:/path/to/repo
    git push -u origin master 

回到服务器,添加Hook 

    cd /repo/hooks vim post-receive 

在post-receive文件里加入，路径改为你想存放项目代码的位置 

    #!/bin/sh
    GIT_WORK_TREE=/path/to/www
    git checkout -f 

增加执行权限

    chmod +x post-receive 

接下来把你的代码上传到服务器吧 

    注意 :Hook执行的权限是由你用来往repo push的帐号决定的，如果部署不成功请检查该帐号是否对web目录具有写权限。另外post-receive必须有可执行权限，不然什么都不会发生 

## 附录

![django模版变量](../figures/django-val.jpg)

![http协议](../figures/http.jpg)

![全栈待学习任务](../figures/fullstack.jpg)


### mode对应的类型

1. 见 : https://docs.djangoproject.com/en/1.8/ref/models/fields/
2. 命令行ipython查看
        
        from django.db import models 
        model.  tab补齐


        V=models.CharField(max_length=None[, **options])　　　　#varchar
        V=models.EmailField([max_length=75, **options])　　　　#varchar
        V=models.URLField([verify_exists=True, max_length=200, **options])　　　　#varchar
        V=models.FileField(upload_to=None[, max_length=100, **options])　　　　#varchar
        #upload_to指定保存目录可带格式，
        V=models.ImageField(upload_to=None[, height_field=None, width_field=None, max_length=100, **options])
        V=models.IPAddressField([**options])　　　　#varchar
        V=models.FilePathField(path=None[, match=None, recursive=False, max_length=100, **options])　#varchar
        V=models.SlugField([max_length=50, **options])　　　　#varchar，标签，内含索引
        V=models.CommaSeparatedIntegerField(max_length=None[, **options])　　　　#varchar

        V=models.IntegerField([**options])　　　　#int
        V=models.PositiveIntegerField([**options])　　　　#int 正整数
        V=models.SmallIntegerField([**options])　　　　#smallint
        V=models.PositiveSmallIntegerField([**options])　　　　#smallint 正整数
        V=models.AutoField(**options)　　　　#int；在Django代码内是自增
        V=models.DecimalField(max_digits=None, decimal_places=None[, **options])　　　　#decimal
        V=models.FloatField([**options])　　　　#real
        V=models.BooleanField(**options)　　　　#boolean或bit
        V=models.NullBooleanField([**options])　　　　#bit字段上可以设置上null值
        V=models.DateField([auto_now=False, auto_now_add=False, **options])　　　　#date
        #auto_now最后修改记录的日期；auto_now_add添加记录的日期
        V=models.DateTimeField([auto_now=False, auto_now_add=False, **options])　　　　#datetime
        V=models.TimeField([auto_now=False, auto_now_add=False, **options])　　　　#time
        V=models.TextField([**options])　　　　#text
        V=models.XMLField(schema_path=None[, **options])　　　　#text

        ——————————————————————————–

        V=models.ForeignKey(othermodel[, **options])　　　　#外键，关联其它模型，创建关联索引
        V=models.ManyToManyField(othermodel[, **options])　　　　#多对多，关联其它模型，创建关联表
        V=models.OneToOneField(othermodel[, parent_link=False, **options])　　　　#一对一，字段关联表属性

### forms类型

见: /home/itcast/.virtualenvs/itcast/lib/python2.7/site-packages/django/forms/fields.py

        1.启动ipython
        2.from django import forms
        3.forms.fields 然后tab补齐显示所有forms类
        4.help(forms.fields)　查看帮助文档

## 阿里云项目环境变量

    Django==1.7.8
    djangorestframework==3.1.3
    httplib2==0.9.1
    ipdb==0.8.1
    ipython==3.2.0
    lxml==3.4.4
    MySQL-python==1.2.5
    Pillow==2.8.2
    requests==2.7.0
    uWSGI==2.0.11.1
    wechat-sdk==0.5.8
    wheel==0.24.0


    