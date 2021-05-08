#mailFilter V1.2

### 原理简介

基于贝叶斯推断的垃圾邮件过滤器。通过8000封正常邮件和8000封垃圾邮件“训练”过滤器:
解析所有邮件，提取每一个词,然后，计算每个词语在正常邮件和垃圾邮件中的出现频率。

1. 当收到一封未知邮件时，在不知道的前提下，我们假定它是垃圾邮件和正常邮件的概率各
   为50%，p(s) = p(n) = 50%

2. 解析该邮件，提取每个词，计算该词的p(s|w)，也就是受该词影响，该邮件是垃圾邮件的概率

					p(sw)             p(w|s)p(s)
		p(s|w) = -----------  =   ----------------------
					p(w)        p(s)p(w|s) + p(n)p(w|n)

3. 提取该邮件中p(s|w)最高的15个词，计算联合概率。

					p(s|w1)p(s|w2)...p(s|w15)
		p = ---------------------------------------------------------------
			p(s|w1)p(s|w2)...p(s|w15) + (1-p(s|w1))(1-p(s|w2)...(1-p(s|w15)))			

4. 设定阈值 p > 0.9 :垃圾邮件  
            p < 0.9 :正常邮件  

> 注:如果新收到的邮件中有的词在史料库中还没出现过，就假定p(s|w) = 0.4

### 使用

1. 解压data.rar到当前文件夹  
2. 启动一个终端，模拟邮件服务器

		cd mailFilter
		python server.py

   	
3. 等到出现 "Waiting for clients..."，启动另一终端，模拟邮件发送端

		cd mailFilter
		python client.py emaillocation
		
**注意使用Python 2.7版本**		

### 参考资料
[http://www.ruanyifeng.com/blog/2011/08/bayesian_inference_part_two.html](http://www.ruanyifeng.com/blog/2011/08/bayesian_inference_part_two.html)  
[http://en.wikipedia.org/wiki/Bayesian_spam_filtering](http://en.wikipedia.org/wiki/Bayesian_spam_filtering)  



