# -*- coding:utf-8 -*-


"""
 Verion: 1.0
 Author: zhangjian
 Site: http://iliangqunru.com
 File: weibo_base.py
 Time: 2016/10/19 21:31
"""
import logging
import time

try:
    import requests
except:
    raise ImportError

level = logging.DEBUG
format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
datefmt = '%Y-%m-%d %H:%M'
logging.basicConfig(level=level, format=format, datefmt=datefmt)
logger = logging.getLogger(__name__)

MAIN_API = 'https://api.weibo.com/2/CUSTOMER_ACTION.json'


class WeiboException(BaseException):
    """Weibo Exception"""

    def __init__(self, *args, **kwargs):
        pass

    def __new__(cls, *args, **kwargs):
        pass


def function_decrator(func):
    """
    装饰器记录请求
    :param func:
    :return:
    """

    def invoke_time(*args, **kwargs):
        startTime = time.time()
        print '[decrator] Function:%s ,params is :[%s]' % (func.__name__, kwargs)
        result = func(*args, **kwargs)
        endTime = time.time()
        print '[decrator] Function:%s, response is %s,invoke time:%ss' % \
              (func.__name__, result, (endTime - startTime))
        return result

    return invoke_time


class WeiboBase:
    """
    微博基础类
    """
    METHOD_GET = 'GET'
    METHOD_POST = 'POST'

    def __init__(self, username, password, API_KEY, API_SECRET=None):
        """
        :param username:微博用户名
        :param password: 用户密码
        :param API_KEY: 申请API_KEY
        :param API_SECRET: (暂时不用)
        """
        self.API_KEY = API_KEY
        self.session = requests.session()
        self.session.auth = username, password

    @function_decrator
    def weibo_action(self, uri, method, *args, **kwargs):
        """
        核心处理
        :param uri:api
        :param method:方法
        :param args:
        :param kwargs:参数
        :return:
        """
        kwargs['source'] = self.API_KEY
        if not method:
            raise Exception('[X] Weibo Method Not Found!')
        if not uri:
            raise Exception("[X] Weibo %s Api Not Found!" % method)
        url = MAIN_API.replace('CUSTOMER_ACTION', uri)
        res = None
        if str(method).upper() == 'GET':
            res = self.session.get(url=url, params=kwargs, timeout=5).json()
        if str(method).upper() == 'POST':
            res = self.session.post(url=url, data=kwargs, timeout=5).json()
        return res

    def _assert_error(self, res):
        pass


if __name__ == '__main__':
    pass
