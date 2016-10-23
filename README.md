# PureWeiboSDK
史上最简单的微博SDK

[![CocoaPods](https://img.shields.io/cocoapods/l/AFNetworking.svg?style=flat-square)](#)

---
###用法
1.在[微博开放平台](http://open.weibo.com/)新建应用，获取App Key 和 App Secret

2.依据[微博API](http://open.weibo.com/wiki/%E5%BE%AE%E5%8D%9AAPI)

3.调用sdk
```python
from weibo_base import WeiboBase
weibo = WeiboBase(username='', password='', API_KEY=API_KEY, API_SECRET=None)
```

###栗子
1.发送微博
```python
from weibo_base import WeiboBase

weibo = WeiboBase(username='', password='', API_KEY=API_KEY, API_SECRET=None)
print weibo.weibo_action(uri='statuses/update', method=weibo.METHOD_POST, status='Hello World')
```

2.根据用户ID获取用户信息
```python
from weibo_base import WeiboBase

weibo = WeiboBase(username='', password='', API_KEY=API_KEY, API_SECRET=None)
print weibo.weibo_action(uri='users/show', method=weibo.METHOD_GET, screen_name='Helixcs')
```