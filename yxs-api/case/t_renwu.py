# coding=utf-8
# 读取配置
from lib.flow import *
from lib.Mysql1 import *
mysql = Mysql(sql_config)
log = Log.Log()
reqData = Excel.ExcelUntil(reqPath).read_row(skip=1,sheetName='job')
##  {'row3': ['test_tagshudan', '', '{"tagCode":"20","page":"0"}', '']}

url = URI + 'jobserver/job'
'''以下接口需要校验user信息，签名加密暂时不清楚，此接口后续完善,验签的先避免，可以先实现修改数据库的'''

class Renwu(unittest.TestCase):

    def test_huoqurenwu(self):
        # 获取任务，这个应该是校验了user相关的信息了
        # 更新header时间与type
        # headers['time'] = str(time.time()).split('.')[0]
        # headers['type'] = "00"
        # headers['Content-Type'] = 'application/json'
        # to_requests(url=url,method='post',reqData=reqData,headers=headers,reqPath=reqPath,sheetindex=4,func=self.test_huoqurenwu)
        pass

    def test_huoquqiandaoxinxi(self):
        # 获取签到信息
        # # 更新header时间与type
        # headers['time'] = str(time.time()).split('.')[0]
        # headers['type'] = "00"
        # headers['Content-Type'] = 'application/json'

        # to_requests(url=url,method='post',reqData=reqData,reqPath=reqPath,headers=headers,sheetindex=4,func=self.test_huoquqiandaoxinxi)

        pass

    def test_lingqujinbi(self):
        # 领取金币
        ## 更新header时间与type
        # headers['time'] = str(time.time()).split('.')[0]
        # headers['type'] = "01"
        # headers['Content-Type'] = 'application/json'

        # to_requests(url=url,method='post',reqData=reqData,headers=headers,reqPath=reqPath,sheetindex=4,func=self.test_lingqujinbi)
        pass

    def test_qiandao(self):
        # 签到
        ## 更新header时间与type
        # headers['time'] = str(time.time()).split('.')[0]
        # headers['type'] = "01"
        # headers['Content-Type'] = 'application/json'
        # to_requests(url=url,method='post',reqData=reqData,headers=headers,reqPath=reqPath,sheetindex=4,func=self.test_qiandao)

        pass

    def test_jilurenwujindu(self):
        # 记录任务进度
        ## 更新header时间与type
        # headers['time'] = str(time.time()).split('.')[0]
        # headers['type'] = "02"
        # headers['Content-Type'] = 'application/json'
        # to_requests(url=url,method='post',reqData=reqData,headers=headers,reqPath=reqPath,sheetindex=4,func=self.test_jilurenwujindu)
        pass

    def test_wanchengyuedurenwu(self):
        # 完成阅读任务
        ## 更新header时间与type
        # headers['time'] = str(time.time()).split('.')[0]
        # headers['type'] = "02"
        # headers['Content-Type'] = 'application/json'
        # to_requests(url=url,method='post',reqData=reqData,headers=headers,reqPath=reqPath,sheetindex=4,func=self.test_wanchengyuedurenwu)
        pass

    def test_qiandaofenxiang(self):
        # 签到分享
        ## 更新header时间与type
        # headers['time'] = str(time.time()).split('.')[0]
        # headers['type'] = "02"
        # headers['Content-Type'] = 'application/json'
        # to_requests(url=url,method='post',reqData=reqData,headers=headers,reqPath=reqPath,sheetindex=4,func=self.test_qiandaofenxiang)
        pass

    def test_baishirenwu(self):
        # 拜师任务
        ## 更新header时间与type
        # headers['time'] = str(time.time()).split('.')[0]
        # headers['type'] = "02"
        # headers['Content-Type'] = 'application/json'
        # to_requests(url=url,method='post',headers=headers,reqPath=reqPath,reqData=reqData,sheetindex=4,func=self.test_baishirenwu)
        pass

    def test_chufatuisongrenwu(self):
        # 触发推送任务，需要push token
        ## 更新header时间与type
        # headers['time'] = str(time.time()).split('.')[0]
        # headers['type'] = "03"
        # to_requests(url=url,method='post',reqData=reqData,headers=headers,reqPath=reqPath,sheetindex=4,func=self.test_chufatuisongrenwu)
        pass

    def test_lingqutuisonghongbao(self):
        # 领取推送红包,需要push token
        ## 更新header时间与type
        # headers['time'] = str(time.time()).split('.')[0]
        # headers['type'] = "04"
        # to_requests(url=url,method='post',reqData=reqData,headers=headers,reqPath=reqPath,sheetindex=4,func=self.test_lingqutuisonghongbao)
        pass


if __name__ == '__main__':
    unittest.main()

