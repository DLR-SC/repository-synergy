# App Crawler

[中文介绍及讨论](http://www.jianshu.com/p/411b20a5ce55)

Collect app infomation from Baidu / Google Play app market using python Scrapy and Mongodb

for Scrapy 1.0+，change ｀app/settings.py｀ 's ITEM_PIPELINE to

```
ITEM_PIPELINES = {
  'scrapy_mongodb.MongoDBPipeline': 100
}
```
