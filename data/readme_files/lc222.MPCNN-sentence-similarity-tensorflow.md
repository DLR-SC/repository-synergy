# MPCNN-sentence-similarity-tensorflow
this is the tensorflow code of the paper:"Multi-Perspective Sentence Similarity Modeling with Convolution Neural Networks." &&
“UMD-TTIC-UW at SemEval-2016 Task 1: Attention-Based Multi-Perspective Convolutional Neural Networks for Textual Similarity 
Measurement”

to run, you should have python2.7 and tensorflow 1.0
what's more, you should download the glove word2vec file:
http://nlp.stanford.edu/data/glove.6B.zip

also you can watch my blog of this, there are test result in the third blog. but the acc is not good, about 70%, it need to be improved: 
http://blog.csdn.net/liuchonge/article/details/62424805
http://blog.csdn.net/liuchonge/article/details/64128870
http://blog.csdn.net/liuchonge/article/details/64440110


This code has NAN while training, So you can see the new version code in https://github.com/Fengfeng1024/MPCNN. This is repaired by Fengfeng1024.

为了方便大家了解整个bug的修复过程，可以参考下面的沟通邮件过程：


https://github.com/Fengfeng1024/MPCNN   感谢博主的分享


------------------ 原始邮件 ------------------
发件人: "254557889"<254557889@qq.com>;
发送时间: 2018年5月8日(星期二) 晚上9:04
收件人: "输过,败过,不曾怕过"<chenfeng_scut@qq.com>;
主题: 回复：关于您的MPCNN模型复现代码遗留问题

恭喜恭喜，因为我看这个代码还有文章下面一直有人在咨询NAN的问题，所以如果可以的话你能把终版代码pull到我github的项目上吗，或者说你上传到你自己的GitHub上面，然后我在文章和代码里面给出你实现的连接，好让更多的人能够看到，有所帮助~~


------------------ 原始邮件 ------------------
发件人: "输过,败过,不曾怕过"<chenfeng_scut@qq.com>;
发送时间: 2018年5月8日(星期二) 下午4:26
收件人: "刘冲"<254557889@qq.com>;
主题: 回复：关于您的MPCNN模型复现代码遗留问题

今天我用tensorboard可视化了每个层的权重和一些输出，发现计算欧氏距离的时候有些输出是0，我觉得可能因为这个导致最后softmax的输入有些为0，所以loss变为NAN了，既然如此，我于是计算欧式距离最后加了1e-4，没想到loss还是NAN。还有一个想法就是用标准化欧氏距离，不知道可不可行。现在跑模型没用欧式距离，同时对您的代码有一些改进，权重都初始化为mean=0，stddev=1.0，在每一层卷积后加BN层，所有可训练的参数加到L2正则化。附件有acc和loss曲线，增加了epoch，终于收敛了。


------------------ 原始邮件 ------------------
发件人: "254557889"<254557889@qq.com>;
发送时间: 2018年5月7日(星期一) 中午12:13
收件人: "输过,败过,不曾怕过"<chenfeng_scut@qq.com>;
主题: 回复：关于您的MPCNN模型复现代码遗留问题

你好，看了你的邮件也给了我一些提示，首先我认为NAN出现的原因可能是，相似度计算处，对每个向量的每个维度的平方差求和，而每个向量都是卷积之后的输出，正如你所说relu激活函数的输出值可能会很大，导致欧氏距离计算平方和时出现NAN的现象，而余弦相似度分母会进行归一化操作，自然没有NAN的问题。上面是我分析的原因，但我不明白的是为什么去掉了sqrt就可以解决NAN？？我的想法是把relu改成tanh，或者说不使用欧氏距离。然后至于说训练效果很差这个问题，首先来讲数据集是公共数据集应该不会有问题，肉眼可见的训练上的规律很可疑，因为训练过程中加入了shuffle，不应该能找到像你说的那种规律。这里可以尝试的方案是，将代码改变一下，可以每100个step eval一次，而不是每个epoch eval一次，然后再tensorboard上面查看train和eval两条曲线，看看原因究竟是什么，另外把训练过程中的W和b权重也都可视化一下，往往问题会出现在某个权重的异常上面。再有就是我看训练的acc还算可以，但是eval的acc只有0.3，另外一个就是loss下降的很缓慢，一般使用了tf.reduce_mean之后loss应该降到很低才对，现在维持在40+肯定是有问题的。


------------------ 原始邮件 ------------------
发件人: "输过,败过,不曾怕过"<chenfeng_scut@qq.com>;
发送时间: 2018年5月7日(星期一) 中午11:43
收件人: "刘冲"<254557889@qq.com>;
主题: 回复：关于您的MPCNN模型复现代码遗留问题

非常感谢您的回复。根据您提供的思路，首先我采用了梯度截断的方法，将梯度控制在某一范围内，但是这样跑出来的效果并不好；然后我用了tfdbg定位到计算欧式距离的时候出现了NAN，我把tf.sqrt去掉之后就可以了，不过我还是不明白为什么会出现NAN，因为计算余弦相似度的时候也是用了tf.sqrt函数。还有一个原因也会导致NAN，就是relu激活函数，paper中的激活函数都是tanh。训练过程中，我发现到某些数据集的时候训练效果非常不好，而且loss和acc波动有点大，难以收敛。附件有训练日志，lr=1e-3、epoch=10、batch_size=64.


------------------ 原始邮件 ------------------
发件人: "254557889"<254557889@qq.com>;
发送时间: 2018年5月5日(星期六) 下午3:08
收件人: "输过,败过,不曾怕过"<chenfeng_scut@qq.com>;
主题: 回复：关于您的MPCNN模型复现代码遗留问题

你好，这个代码是我刚开始使用tf仿真论文的时候做的，当时确实遇到了很多问题，包括代码本身应该也存在很多问题。当时的效果其实也很差，一直想着回头再看看修改一下，但是最近一直比较忙没时间搞，所以希望你在跑程序的同时自己看看程序本身是否存在问题，而不是单纯的跑代码。另外关于你说的W1全部变为NAN这个问题，可以尝试使用RNN训练过程中常用的梯度截断的方法，把梯度限制在10以内，这样应该可以防止NAN现象的出现，另外就是看看代码里面究竟哪一行引起了NAN的出现，这里可以看一下官网上面tfdbg的介绍，里面说了如何找到NAN出现的位置以及简单地分析方法。很哟可能是分母部分为0之类的情况导致的。最后，希望你能把这个代码跳出来改正确吧~~


------------------ 原始邮件 ------------------
发件人: "输过,败过,不曾怕过"<chenfeng_scut@qq.com>;
发送时间: 2018年5月5日(星期六) 中午12:45
收件人: "刘冲"<254557889@qq.com>;
主题: 关于您的MPCNN模型复现代码遗留问题

博主，您好，首先非常感谢您对MPCNN模型的思路与代码分享，我在运行您的代码过程中，碰到了loss为nan的情况，网上查了很多方法，调整lr、batch_size，tf.clip_by_value函数调整最后一层输出，同时仔细对比了论文与您的复现代码，没发现任何问题，然后我打印出每一个权重参数，发现第一个batch_size训练过后，权重参数W1[0]全部变为NAN，我还是不知道怎么解决这个问题，无奈之下联系博主，希望博主能解决我的疑问，万分感谢。
