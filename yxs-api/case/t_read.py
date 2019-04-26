# coding=utf-8
# 读取配置
from lib.flow import *
log = Log.Log()
reqData = Excel.ExcelUntil(reqPath).read_row(skip=1,sheetName='read')
##  {'row3': ['test_tagshudan', '', '{"tagCode":"20","page":"0"}', '']}

url = URI + 'readServer/read'

class Read(unittest.TestCase):

    def test_jinrushujia(self):
        # 进入书架
        # 更新header时间与type
        headers['time'] = str(time.time()).split('.')[0]
        headers['type'] = "00"
        to_requests(url=url,method='post',reqData=reqData,headers=headers,reqPath=reqPath,sheetindex=3,func=self.test_jinrushujia)

    def test_huoquliulanjilu(self):
        # 获取浏览记录
        # 更新header时间与type
        headers['time'] = str(time.time()).split('.')[0]
        headers['type'] = "03"
        to_requests(url=url,method='post',reqData=reqData,headers=headers,reqPath=reqPath,sheetindex=3,func=self.test_huoquliulanjilu)

    def test_jiarushujia(self):
        # 书籍加入书架
        # 更新header时间与type
        headers['time'] = str(time.time()).split('.')[0]
        headers['type'] = "02"
        to_requests(url=url,method='post',reqData=reqData,reqPath=reqPath,headers=headers,sheetindex=3,func=self.test_jiarushujia)

    def test_shujizhiding(self):
        #### 这个接口貌似有点问题
        # 书籍置顶，取消置顶
        # 更新headers
        headers['time'] = str(time.time()).split('.')[0]
        headers['type'] = "06"
        to_requests(url=url,method='post',reqData=reqData,reqPath=reqPath,headers=headers,sheetindex=3,func=self.test_shujizhiding)

    def test_renqibangshudan(self):
        # 人气榜书单
        # 更新headers
        headers['time'] = str(time.time()).split('.')[0]
        headers['type'] = "07"
        to_requests(url=url,method='post',reqData=reqData,reqPath=reqPath,headers=headers,sheetindex=3,func=self.test_renqibangshudan)

if __name__ == '__main__':
    unittest.main()
