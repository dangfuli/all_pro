from lib.flow import *

# 读取配置
log = Log.Log()
reqData = Excel.ExcelUntil(reqPath).read_row(skip=1,sheetName='store')

url = URI + 'bserver/store'

class Store(unittest.TestCase):

    def test_huoqushuchengye(self):
        # 获取书城页
        # 更新header时间与type
        headers['time'] = str(time.time()).split('.')[0]
        headers['type'] = "00"
        for key,value in reqData.items():
            if value[0] != 'test_huoqushuchengye':
                break
            time.sleep(1)
            try:
                resp = requests.get(url=url,headers=headers,params=value[2])
                if resp.json()['code'] == 0:
                    Excel.ExcelUntil(reqPath).update_cell(int(key[3:]) - 1, 3, 'ok')
                else:
                    raise Exception
            except:
                Excel.ExcelUntil(reqPath).update_cell(int(key[3:])-1,3,'fail',sheetIndex=1)
                log.error("接口为：'bserver/record'，方法为：{0}\n参数为：{1}".format(self.test_rihuo.__name__,value))
            Excel.ExcelUntil(reqPath).update_cell(int(key[3:])-1,3,'ok',sheetIndex=1)

    def test_tagshudan(self):
        # 书城页内tag书单
        headers['time'] = str(time.time()).split('.')[0]
        headers['type'] = "01"
        for key,value in reqData.items():
            if value[0] != 'test_tagshudan':
                break
            time.sleep(1)
            try:
                resp = requests.get(url=url,headers=headers,params=value[2])
                if resp.json()['code'] == 0:
                    Excel.ExcelUntil(reqPath).update_cell(int(key[3:]) - 1, 3, 'ok')
                else:
                    raise Exception
            except:
                Excel.ExcelUntil(reqPath).update_cell(int(key[3:])-1,3,'fail',sheetIndex=1)
                log.error("接口为：'bserver/record'，方法为：{0}\n参数为：{1}".format(self.test_rihuo.__name__,value))
            Excel.ExcelUntil(reqPath).update_cell(int(key[3:])-1,3,'ok',sheetIndex=1)



if __name__ == '__main__':
    unittest.main()