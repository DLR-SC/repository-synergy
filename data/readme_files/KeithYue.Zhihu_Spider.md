Zhihu_Spider
============

Scrapy the Zhihu content and user social network information. Now it contains 314400 questions and 261376 users.

### File Strcture

* ./zhihu/zhihu : The related files about crawling the zhihu.com
* ./zhihu/zhihu_dat/ : The structured data for baseline experiments on zhihu dataset
    * ./zhihu/zhihu_dat/item.dat: the corpus(bag of words) of all questions, using Blei’s LDA-C format. The line number represents qid
    * ./zhihu/zhihu_dat/users.dat: the corpus of all users, the features of users is the bag representations of all the questions they have answered.
    * ./zhihu/zhihu_dat/vocab.dat: the vocabulary of zhihu dataset
    * ./zhihu/zhihu_dat/item_adj.dat: the questions and their answerer ids, the first column is the number of answers, the line number is question id
    * ./zhihu/zhihu_dat/user_adj.dat: the users and their answered question ids, the line number the user id, 
    * ./zhihu/zhihu_dat/truth.dat: the questions and their answers, each answer has a score with them

