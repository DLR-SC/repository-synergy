基本工具：
=============

中科院NLPIR（推荐）
-------------
http://ictclas.nlpir.org/  
原名ICTCLAS，是由中科院计算所历经数年开发的分词工具，采用C++编写。  
主要功能包括分词、词性标注、命名实体识别、用户词典功能，新词发现与关键词提取。  
可以可视化界面操作和API方式调用。

哈工大LTP（推荐）
-------------
http://www.ltp-cloud.com/  
语言技术平台（LTP）是哈工大社会计算与信息检索研究中心开发的一整套中文语言处理系统，采用C++编写。  
主要功能包括分词、词性标注、命名实体识别、依存句法分析、语义角色标注、语义依存分析等。  
语言云新版API是REST风格的WEB API调用服务，免SDK安装，支持JavaScript调用。  

jieba分词（推荐）
-------------
https://github.com/fxsjy/jieba  
基于前缀词典高效词图扫描，采用动态规划查找最大概率路径，支持三种分词模式：精确模式、全模式、搜索引擎模式。  
主要功能包括分词、添加自定义词典、关键词提取（基于TF-IDF或TextRank）、词性标注、并行分词等功能。  

FudanNLP
-------------
https://code.google.com/archive/p/fudannlp/  
FudanNLP采用Java编写，提供了API的访问调用方式，包含机器学习算法和数据集。  
主要功能包括：中文分词，词性标注，实体名识别，关键词抽取，依存句法分析，时间短语识别，文本分类，新闻聚类，精确推理等。  

Stanford Natural Language Processing
-------------
http://nlp.stanford.edu/software/
*   Stanford CoreNLP 采用Java编写的面向英文的处理工具，主要功能包括分词、词性标注、命名实体识别、语法分析等。  
*   Stanford Word Segmenter 提供基于CRF（条件随机场）算法的分词功能。  
*   Stanford Named Entity Recognizer 提供命名实体识别功能。  
*   Stanford POS Tagger 提供词性标注功能。  
*   Stanford Parser 提供语法分析功能。  



主题模型（Topic Model）
=============

主题模型在机器学习和自然语言处理等领域是用来在一系列文档中发现抽象主题的一种统计模型。直观来讲，如果一篇文章有一个中心思想，那么一些特定词语会更频繁的出现。一个主题模型试图用数学框架来体现文档的这种特点。主题模型自动分析每个文档，统计文档内的词语，根据统计的信息来断定当前文档含有哪些主题，以及每个主题所占的比例各为多少。

*   概率主题模型简介：http://www.cnblogs.com/siegfang/archive/2013/01/30/2882391.html  
*   潜在狄立克雷分配（Latent Dirichlet Allocation，LDA）算法的python实现参见code。  

词嵌入（Word Embedding）
=============

词嵌入的实现包括Word2vec，GloVe等。

Word2vec是Google在2013年开源的一款将词表征为实数值向量的高效工具，其利用深度学习的思想，通过训练把对文本内容的处理简化为K维向量空间中的向量运算，而向量空间上的相似度可以用来表示文本语义上的相似度，应用包括聚类、找同义词、词性分析等。
其核心思想是基于词频的Huffman编码，使得词频相似的词在隐藏层激活的内容基本一致，而出现频率越高的词激活的隐藏层数目越少，因此有效的降低了计算的复杂度。

*   Word2vec下载： https://code.google.com/archive/p/word2vec/  
*   Word2vec笔记：http://suanfazu.com/t/shen-du-xue-xi-word2vec-bi-ji/192  



资源（持续更新中）
=============

*   斯坦福深度学习与自然语言处理课程  
http://cs224d.stanford.edu/syllabus.html

*   TensorFlow (Open Source Library for Machine Intelligence)  
https://www.tensorflow.org/



其他机器学习相关工具
=============

*   基于python的深度学习库Theano  
http://deeplearning.net/software/theano/

