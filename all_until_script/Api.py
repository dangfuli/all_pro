# coding=utf-8
import time,requests
def get_request_post(url,**kwargs):
    '''
    post请求
    :param url: 请求的地址
    :param kwargs: 请求的参数，dict格式
    :return: json or None
    '''
    data = {kwargs}
    try:
        print('开始请求post，地址：%s'% url)
        start = time.time()
        r = requests.post(url,data)
        end = time.time()
        print('请求结束。花费%.2f秒'%(end-start))
        print(r.json())
        return r.json()
    except Exception as e:
        print('请求失败，错误：%s'%e)
        return None

def get_request_get(url,**kwargs):
    '''
    get请求
    :param url:被请求的url
    :param kwargs:param变量参数,dict格式
    :return:json or None
    '''
    param = {kwargs}
    print('开始请求get，地址：%s'%url)
    if param == {}:
        try:
            start = time.time()
            r = requests.get(url)
            end = time.time()
            print('请求结束，花费%.2f秒'%(end-start))
            return r.json()
        except Exception as e:
            print('错误信息：%s'%e)
            return None
    else:
        paramstr = ''
        for key,values in param:
            paramstr += '%s=%s&'%(key,values)
        print(paramstr)
        try:
            print('开始请求get，地址：%s'%url)
            start = time.time()
            r = requests.get(url + '?' + paramstr)
            end = time.time()
            print('请求结束，花费%.2f秒'%(end-start))
            return r.json()
        except Exception as e:
            print('错误信息为：%s'%e)
            return None
