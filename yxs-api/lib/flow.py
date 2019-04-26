from lib import getConfig
import unittest
import requests,time,json,os
from lib import Excel
from doc.constant import *
from lib import Log
# 加载配置
log = Log.Log()
headers = getConfig.getConfig(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'config/commonParam.json'))
reqPath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'doc/1.xls')

def to_requests(url,method,reqData,headers,reqPath,sheetindex,func):

    for key, value in reqData.items():
        if value[0] != func.__name__:
            continue
        try:
            time.sleep(1.5)
            if method == 'get':

                if value[2] != '':
                    value_r = json.loads(value[2])
                    resp = requests.get(url=url, headers=headers, params=value_r)
                else:
                    resp = requests.get(url=url, headers=headers)
            elif method == 'post':
                # 转成字典
                value_r = json.loads(value[1])

                if value_r.setdefault('startTime') is None:
                    value_r.pop('startTime')
                else:
                    value_r['startTime'] = '{0}'.format(time.strftime('%Y%m%d%H%M%S', time.localtime()))

                if value_r.setdefault('code') is None:
                    value_r.pop('code')
                else:
                    value_r['code'] = '{0}'.format(time.strftime('%Y%m%d%H%M%S', time.localtime()))
                resp = requests.post(url=url,headers=headers,json=value_r)

            if resp.json()['code'] == 0:
                Excel.ExcelUntil(reqPath).update_cell(int(key[3:]) - 1, 3, 'ok', sheetIndex=sheetindex)
            else:
                raise Exception
        except Exception as e:
            Excel.ExcelUntil(reqPath).update_cell(int(key[3:]) - 1, 3, 'fail', sheetIndex=sheetindex)
            log.error("接口为：'bserver/record'，方法为：{0}\n参数为：body:{1}\nparams:{2}\n错误信息为:{3}".format(func.__name__, value[0],value[1],e))

