# coding=utf-8
# 读取配置
from lib.flow import *
log = Log.Log()
reqData = Excel.ExcelUntil(reqPath).read_row(skip=1,sheetName='mine')
##  {'row3': ['test_tagshudan', '', '{"tagCode":"20","page":"0"}', '']}

url = URI + "mineserver/mine"

class Mine(unittest.TestCase):

    def test_jinruwode(self):
        # 进入我的
        # 更新header时间与type
        headers['time'] = str(time.time()).split('.')[0]
        headers['type'] = "00"
        headers['Content-Type'] = 'application/json'
        to_requests(url=url,method='post',reqData=reqData,headers=headers,reqPath=reqPath,sheetindex=5,func=self.test_jinruwode)

    def test_jinruxiaoxizhongxin(self):
        # 进入消息中心
        # 更新header时间与type
        headers['time'] = str(time.time()).split('.')[0]
        headers['type'] = "07"
        headers['Content-Type'] = 'application/json'
        to_requests(url=url,method='post',reqData=reqData,headers=headers,reqPath=reqPath,sheetindex=5,func=self.test_jinruxiaoxizhongxin)

    def test_tuichuxiaoxizhongxin(self):
        # 退出消息中心,这个貌似有点问题
        # 更新header时间与type
        headers['time'] = str(time.time()).split('.')[0]
        headers['type'] = "07"
        headers['Content-Type'] = 'application/json'
        to_requests(url=url,method='post',reqData=reqData,headers=headers,reqPath=reqPath,sheetindex=5,func=self.test_tuichuxiaoxizhongxin)

    def test_huoqujinbiliushui(self):
        # 获取金币流水
        # 更新header时间与type
        headers['time'] = str(time.time()).split('.')[0]
        headers['type'] = "07"
        headers['Content-Type'] = 'application/json'
        to_requests(url=url,method='post',reqData=reqData,headers=headers,reqPath=reqPath,sheetindex=5,func=self.test_huoqujinbiliushui)

    def test_huoqutudiyuedu(self):
        # 获取徒弟阅读
        # 更新header时间与type
        headers['time'] = str(time.time()).split('.')[0]
        headers['type'] = "01"
        headers['Content-Type'] = 'application/json'
        to_requests(url=url,method='post',reqData=reqData,headers=headers,reqPath=reqPath,sheetindex=5,func=self.test_huoqutudiyuedu)

    def test_jinrutixian(self):
        # 进入提现页面
        # 更新header时间与type
        headers['time'] = str(time.time()).split('.')[0]
        headers['type'] = "02"
        headers['Content-Type'] = 'application/json'
        to_requests(url=url,method='post',reqData=reqData,headers=headers,reqPath=reqPath,sheetindex=5,func=self.test_jinrutixian)

    def test_tixianxiadan(self):
        # 提现下单
        # 更新header时间与type
        headers['time'] = str(time.time()).split('.')[0]
        headers['type'] = "02"
        headers['Content-Type'] = 'application/json'
        to_requests(url=url,method='post',reqData=reqData,headers=headers,reqPath=reqPath,sheetindex=5,func=self.test_tixianxiadan)

    def test_chakantixianlishi(self):
        # 查看提现历史
        # 更新header时间与type
        headers['time'] = str(time.time()).split('.')[0]
        headers['type'] = "02"
        headers['Content-Type'] = 'application/json'
        to_requests(url=url,method='post',reqData=reqData,headers=headers,reqPath=reqPath,sheetindex=5,func=self.test_chakantixianlishi)

    def test_jinruyaoqingye(self):
        # 进入邀请页
        # 更新header时间与type
        headers['time'] = str(time.time()).split('.')[0]
        headers['type'] = "06"
        headers['Content-Type'] = 'application/json'
        to_requests(url=url,method='post',reqData=reqData,headers=headers,reqPath=reqPath,sheetindex=5,func=self.test_jinruyaoqingye)

    def test_huoquhaoyou(self):
        # 获取好友信息
        # 更新header时间与type
        headers['time'] = str(time.time()).split('.')[0]
        headers['type'] = "06"
        headers['Content-Type'] = 'application/json'
        to_requests(url=url,method='post',reqData=reqData,headers=headers,reqPath=reqPath,sheetindex=5,func=self.test_huoquhaoyou)

    def test_lianxikefu(self):
        # 联系客服
        # 更新header时间与type
        headers['time'] = str(time.time()).split('.')[0]
        headers['type'] = "07"
        headers['Content-Type'] = 'application/json'
        to_requests(url=url,method='post',reqData=reqData,headers=headers,reqPath=reqPath,sheetindex=5,func=self.test_lianxikefu)

    def test_jinrushezhi(self):
        # 进入设置页面
        # 更新header时间与type
        headers['time'] = str(time.time()).split('.')[0]
        headers['type'] = "07"
        headers['Content-Type'] = 'application/json'
        to_requests(url=url,method='post',reqData=reqData,headers=headers,reqPath=reqPath,sheetindex=5,func=self.test_jinrushezhi)

    def test_bangdingzhifubao(self):
        # 绑定支付宝
        # 更新header时间与type
        headers['time'] = str(time.time()).split('.')[0]
        headers['type'] = "03"
        headers['Content-Type'] = 'application/json'
        to_requests(url=url,method='post',reqData=reqData,headers=headers,reqPath=reqPath,sheetindex=5,func=self.test_bangdingzhifubao)


if __name__ == '__main__':
    unittest.main()
