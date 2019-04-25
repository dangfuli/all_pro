# coding=utf-8
# 读取配置
from lib.flow import *
log = Log.Log()
reqData = Excel.ExcelUntil(reqPath).read_row(skip=1,sheetName='books')
##  {'row3': ['test_tagshudan', '', '{"tagCode":"20","page":"0"}', '']}

url = URI + 'bserver/books'
class Books(unittest.TestCase):

    def test_jrshujixiangqingye(self):
        # 进入书籍详情页
        # 更新header时间与type
        headers['time'] = str(time.time()).split('.')[0]
        headers['type'] = "00"
        to_requests(url=url,method='get',reqData=reqData,headers=headers,reqPath=reqPath,sheetindex=2,func=self.test_jrshujixiangqingye)

    def test_shujimulu(self):
        # 书籍目录
        # 更新header时间与type
        headers['time'] = str(time.time()).split('.')[0]
        headers['type'] = "02"
        to_requests(url=url,method='get',reqData=reqData,headers=headers,reqPath=reqPath,sheetindex=2,func=self.test_shujimulu)

    def test_shujineirong(self):
        # 书籍内容
        # 更新header时间与type
        headers['time'] = str(time.time()).split('.')[0]
        headers['type'] = "01"
        to_requests(url=url,method='get',reqData=reqData,headers=headers,reqPath=reqPath,sheetindex=2,func=self.test_shujineirong)

    def test_xiangtongshujitj(self):
        # 相同书籍推荐
        # 更新header时间与type
        headers['time'] = str(time.time()).split('.')[0]
        headers['type'] = "03"
        to_requests(url=url,method='get',reqData=reqData,headers=headers,reqPath=reqPath,sheetindex=2,func=self.test_xiangtongshujitj)

if __name__ == '__main__':
    unittest.main()