### Introduction

Minion, which achieves an approach to maximize utilization of
broadband traffic like BT, implemented by python and based on HTTP
protocol

Minion can be easily used to dispatch data, similar to curl/wget. It
also provides python API libs.

### Installtion

minion cli need python 2.7, requests

minion tracker need python 2.7, django mysql

```
git clone git://github.com/alibaba/minion
cd minion
pip install -r requirements.txt
python setup.py install
```

### Usage

deploy your tracker server

tracker need django mysql

```
python tracker/manage.py syncdb
python tracker/manage.py runserver # or use wsgi/nginx
```

try your minion cli

```
minion get http://foo.bar/testfile \
     --tracker some.tracker.server \
     --dest-path=/tmp/tops1 \
     --upload-rate 10M \
     --download-rate 100M \
     --callback delete \
     --upload-time 5 \
     --fallback
```

* --tracker specify tracker
* --dest-path specify the path data will be wrote to, default to current dir
* --upload-time specify time for upload after download complete, default
  to 60s
* --download-rate --upload-rate specify rate for upload/download
    can used with unit, like 10M
* --fallback option, if no resource exists in tracker download directly
    from origin url
* --callback
* --verbose for more log

### Framework

Minion work as picture below

![image](/docs/p2p_flow.png)


PEER:    The host ready to download SOURCE
TRACKER: The host manage PEERs and SOURCEs
SOURCE:  URL of some data


STEP

1. PEER0 access TRACKER to get peers that was uploading  SOURCE, TRACKER
   return null
2. PEER0 get SOURCE from origin url directly
3. PEER0 upload SOURCE, telling that to TRACKER
4. PEER1 do like step 1，return a list contain PEER0
5. PEER1 get SOURCE from PEER0
6. PEER1 do like step 3

## License

Minion as a whole is released under the GNU General Public License
version 2.

[中文](/README.cn.md)
