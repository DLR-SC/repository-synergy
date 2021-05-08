# Coincheck: Coincheck Api Library

coincheck は [coincheck](https://coincheck.com) の python 製 api ライブラリです.

```
> from coincheck import market
> m1 = market.Market()
> m1.ticker()
'{"last":30930,"bid":30810,"ask":30930,"high":31500,"low":30220,"volume":"560.51814602","timestamp":1428338044}'
```

## Documentation

Documentation for Coincheck API is  available at https://coincheck.com/documents/exchange/api

### Order

 注文が決済されたら、キャンセルできないので注意してください.

```
 # 20000 jpy で 0.1 の bitcoin を購入する注文をする.
 > from coincheck import order, market, account
 > o1 = order.Order(secret_key=settings.secret_key, access_key=settings.access_key)
 > print(o1.buy_btc_jpy(rate=20000, amount=0.1))
 {"success":true,"id":1355414,"amount":"0.1","rate":"20000.0","order_type":"buy","pair":"btc_jpy","created_at":"2015-04-06T16:56:19.821Z"}
 
 # 40000 jpy で 0.1 の bitcoin を売却する注文をする.
 > from coincheck import order, market, account
 > o1 = order.Order(secret_key=settings.secret_key, access_key=settings.access_key)
 > print(o1.sell_btc_jpy(rate=40000,amount=0.1))
 {"success":true,"id":1355421,"amount":"0.1","rate":"40000.0","order_type":"sell","pair":"btc_jpy","created_at":"2015-04-06T16:57:26.487Z"}
 
 # 自分の注文の一覧を表示する.
 > from coincheck import order, market, account
 > o1 = order.Order(secret_key=settings.secret_key, access_key=settings.access_key)
 > print(o1.list())
 {"success":true,"orders":[{"id":676197,"order_type":"buy","rate":20000,"pair":"btc_jpy","pending_amount":"0.1","created_at":"2015-04-06T16:56:19.000Z"},{"id":676201,"order_type":"sell","rate":40000,"pair":"btc_jpy","pending_amount":"0.1","created_at":"2015-04-06T16:57:26.000Z"}]}
 
 # 注文番号 676197 の注文をキャンセルする. (注文番号は coincheck.order.list() のid)
 > from coincheck import order, market, account
 > o1 = order.Order(secret_key=settings.secret_key, access_key=settings.access_key)
 > print(o1.cancel('676197'))
 {"success":true,"id":676197}
 
 # 自分の取引履歴を表示する.
 > from coincheck import order, market, account
 > o1 = order.Order(secret_key=settings.secret_key, access_key=settings.access_key)
 > print(o1.history())
 {"success":true,"transactions":[{"id":21118,"created_at":"2015-04-06T16:39:10.000Z","funds":{"btc":"-0.02","jpy":"624.6"}}]}
```
 
### Market
 
coincheck の市場情報を取得します.
 
```
 # coincheck の最新市場情報を取得する.
 > from coincheck import order, market, account
 > m1 = market.Market()
 > print(m1.ticker())
 {"last":30820,"bid":30810,"ask":30820,"high":31500,"low":30220,"volume":"559.78124602","timestamp":1428340013}
 
 # coincheck の最新取引履歴を取得する.
 > from coincheck import order, market, account
 > m1 = market.Market()
 > print(m1.trades())
 [{"id":16143,"amount":"0.25","rate":30820,"order_type":"sell","created_at":"2015-04-06T17:02:04.000Z"},{"id":16142,"amount":"0.249","rate":30930,"order_type":"buy","created_
at":"2015-04-06T16:33:12.000Z"},{"id":16141,"amount":"0.4174","rate":30810,"order_type": ...

 # coincheck の最新板情報を取得する.
 > from coincheck import order, market, account
 > m1 = market.Market()
 > print(m1.orderbooks())
 {"asks":[[31740,"2.25731223"],[31750,"0.35"],...],"bids":[[30810,"0.16228497"],[30700,"3.404"],...]}
```

### Account

ユーザのアカウント情報を取得します.

```
 # アカウントの情報を表示します.
 > from coincheck import order, market, account
 > a1 = account.Account(secret_key=settings.secret_key, access_key=settings.access_key)
 > print(a1.get_info())
 {"success":true,"id":0000,"email":"kamonshohei@gmail.com","identity_status":"identity_verified","bitcoin_address":"..."}
 
 # アカウントの残高を確認できます.
 > from coincheck import order, market, account
 > a1 = account.Account(secret_key=settings.secret_key, access_key=settings.access_key)
 > print(a1.get_balance())
 {"success":true,"jpy":"...","btc":"...","jpy_reserved":"...","btc_reserved":"...","jpy_lend_in_use":"...","btc_lend_in_use":"...","jpy_lent":"...","btc_lent":"...","jpy_debt":"...","btc_debt":"..."}
```


## Environment

- support Python 3.x,2.7)

## Installation


### git

```
git clone git@github.com:kmn/coincheck.git
```

### pip 

```
pip install coincheck
```
## Initialization

 set your api access-key and secret-key to "coincheck/settings.py"
 to get your api keys , see [API key](https://coincheck.com/api_settings).

## TODO

- add test case
- add offset to market.trade()
