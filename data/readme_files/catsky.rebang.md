rebang
======
![](https://github.com/catsky/rebang/blob/master/screenshot.png)
A tiny and beautiful blog system using Flask, SQLAlchemy,

- a blog system to manage your articles, with beautiful thumbnail overview
- using **Flask** web framework
- using **SQLAlchemy** for ORM layer
- deployed on China Cloud Computing platform: **Sinaapp**
- using **MySQL** to store the data of article
- using Sinaapp **Storage** Module to store the picture, and the thumbnail as well
- leverage the python crawler to download the articles. The crawler is also availible on GIT [https://github.com/catsky/auCrawler](https://github.com/catsky/auCrawler)


## Is there a live Demo?
Yes. Here is the link: [http://australian.sinaapp.com](http://australian.sinaapp.com)

## Vision

1. to be a simple and beautiful blog system
2. interact with Weixin (a.k.a WeChat)
3. automate the article publishing via scrapy (or sinaapp fetching service)
## How to deploy on Sinaapp?
1. create a python app **you_app_name** on http://sae.sina.com.cn
2. update the attribute value of "name" to **you_app_name** in the file of australian\1\config.yaml
3. update BASE_URL in the file of australian\1\chartnet\setting.py
4. enable **MySQL** on your sinaapp
5. enable **Storage** on your sinaapp, and create a new domain with name of **attachment**, remember set the anti-stealing-link to false
6. upload the folder of '1' to your sinaapp via SVN
7. access the homepage of your app, db schema will be created automatically. 
8. Done and enjoy:)

## Having Problems getting set up?
Any issues, please contact me via zhdhui at gmail.com

## Copyright / License
- MIT License
