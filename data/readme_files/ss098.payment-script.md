支付宝免签约收款工具，这是一个 Docker 的应用，当然也可以运行在普通 Python 环境下，默认与 https://github.com/ss098/payment 配合使用，你也可以自行改造通知到自定义的接口。

安装步骤：

 1. Python 2 运行环境，安装 requests，beautifulsoup4，html5lib 依赖库
 2. 定义环境变量 `PAYMENT_APPLICATION_ID` `PAYMENT_APIKEY`，这是在上文提到的 payment 的 `application` 表中自行添加的
 3. 环境变量 `PAYMENT_SECERT` 如果使用了 payment 则是在 payment 中配置的
 4. 环境变量 `PAYMENT_COOKIE` 需要在支付宝网站 https://consumeprod.alipay.com/record/advanced.htm 获取 document.cookie。需要注意的是这里是高级版的账单，通常直接访问会跳转到普通版，需要在网页中手工切换
 5. 执行 python alipay.py，可以与 supervisor 等配合使用

如果在 Docker 中使用，只需要配置环境变量并使用 Dockerfile 生成镜像即可自动部署。
