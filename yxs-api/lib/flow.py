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
