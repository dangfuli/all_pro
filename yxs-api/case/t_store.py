from lib.flow import *

# 读取配置
log = Log.Log()
reqData = Excel.ExcelUntil(reqPath).read_row(skip=1,sheetName='store')
##  {'row3': ['test_tagshudan', '', '{"tagCode":"20","page":"0"}', '']}
url = URI + 'bserver/store'

class Store(unittest.TestCase):

    def test_huoqushuchengye(self):
        # 获取书城页
        # 更新header时间与type
        headers['time'] = str(time.time()).split('.')[0]
        headers['type'] = "00"
        to_requests(url=url,method='get',reqData=reqData,reqPath=reqPath,headers=headers,sheetindex=1,func=self.test_huoqushuchengye)
        # for key,value in reqData.items():
        #     if value[0] != 'test_huoqushuchengye':
        #         break
        #     time.sleep(1)
        #     try:
        #         resp = requests.get(url=url,headers=headers,params=value[2])
        #         if resp.json()['code'] == 0:
        #             Excel.ExcelUntil(reqPath).update_cell(int(key[3:]) - 1, 3, 'ok',sheetIndex=1)
        #         else:
        #             raise Exception
        #     except:
        #         Excel.ExcelUntil(reqPath).update_cell(int(key[3:])-1,3,'fail',sheetIndex=1)
        #         log.error("接口为：'bserver/record'，方法为：{0}\n参数为：{1}".format(self.test_huoqushuchengye.__name__,value))

    def test_tagshudan(self):
        # 书城页内tag书单
        # 更新headers
        headers['time'] = str(time.time()).split('.')[0]
        headers['type'] = "01"
        to_requests(url=url,method='get',reqData=reqData,reqPath=reqPath,headers=headers,sheetindex=1,func=self.test_tagshudan)
        # for key,value in reqData.items():
        #     if value[0] != 'test_tagshudan':
        #         continue
        #     time.sleep(1)
        #     value = json.loads(value[2])
        #     try:
        #         resp = requests.get(url=url,headers=headers,params=value)
        #         if resp.json()['code'] == 0:
        #             Excel.ExcelUntil(reqPath).update_cell(int(key[3:]) - 1, 3, 'ok',sheetIndex=1)
        #         else:
        #             raise Exception
        #     except:
        #         Excel.ExcelUntil(reqPath).update_cell(int(key[3:])-1,3,'fail',sheetIndex=1)
        #         log.error("接口为：'bserver/record'，方法为：{0}\n参数为：{1}".format(self.test_tagshudan.__name__,value))

    def test_shujifenlei(self):
        # 书籍分类接口
        # 更新headers
        headers['time'] = str(time.time()).split('.')[0]
        headers['type'] = "02"
        to_requests(url=url,method='get',reqData=reqData,reqPath=reqPath,headers=headers,sheetindex=1,func=self.test_shujifenlei)
        # for key, value in reqData.items():
        #     if value[0] != 'test_shujifenlei':
        #         continue
        #     time.sleep(1)
        #     value = json.loads(value[2])
        #     try:
        #         resp = requests.get(url=url, headers=headers, params=value)
        #         if resp.json()['code'] == 0:
        #             Excel.ExcelUntil(reqPath).update_cell(int(key[3:]) - 1, 3, 'ok',sheetIndex=1)
        #         else:
        #             raise Exception
        #     except:
        #         Excel.ExcelUntil(reqPath).update_cell(int(key[3:]) - 1, 3, 'fail', sheetIndex=1)
        #         log.error("接口为：'bserver/record'，方法为：{0}\n参数为：{1}".format(self.test_shujifenlei.__name__, value))

    def test_shuijifenleixiangqing(self):
        # 书籍分类详情
        # 更新headers
        headers['time'] = str(time.time()).split('.')[0]
        headers['type'] = "03"
        to_requests(url=url,method='get',reqData=reqData,reqPath=reqPath,headers=headers,sheetindex=1,func=self.test_shuijifenleixiangqing)
        # for key, value in reqData.items():
        #     if value[0] != 'test_shuijifenleixiangqing':
        #         continue
        #     time.sleep(1)
        #     value = json.loads(value[2])
        #     try:
        #         resp = requests.get(url=url, headers=headers, params=value)
        #         if resp.json()['code'] == 0:
        #             Excel.ExcelUntil(reqPath).update_cell(int(key[3:]) - 1, 3, 'ok',sheetIndex=1)
        #         else:
        #             raise Exception
        #     except:
        #         Excel.ExcelUntil(reqPath).update_cell(int(key[3:]) - 1, 3, 'fail', sheetIndex=1)
        #         log.error("接口为：'bserver/record'，方法为：{0}\n参数为：{1}".format(self.test_shuijifenleixiangqing.__name__,value))

    def test_shuchengbanner(self):
        # 书籍分类详情
        # 更新headers
        headers['time'] = str(time.time()).split('.')[0]
        headers['type'] = "05"
        to_requests(url=url,method='get',reqData=reqData,reqPath=reqPath,headers=headers,sheetindex=1,func=self.test_shuchengbanner)
        # for key, value in reqData.items():
        #     if value[0] != 'test_shuchengbanner':
        #         continue
        #     time.sleep(1)
        #     value = json.loads(value[2])
        #     try:
        #         resp = requests.get(url=url, headers=headers, params=value)
        #         if resp.json()['code'] == 0:
        #             Excel.ExcelUntil(reqPath).update_cell(int(key[3:]) - 1, 3, 'ok',sheetIndex=1)
        #         else:
        #             raise Exception
        #     except:
        #         Excel.ExcelUntil(reqPath).update_cell(int(key[3:]) - 1, 3, 'fail', sheetIndex=1)
        #         log.error("接口为：'bserver/record'，方法为：{0}\n参数为：{1}".format(self.test_shuchengbanner.__name__,value))

    def test_bangdanxinxi(self):
        # 榜单信息
        # 更新headers
        headers['time'] = str(time.time()).split('.')[0]
        headers['type'] = "10"
        to_requests(url=url,method='get',reqData=reqData,reqPath=reqPath,headers=headers,sheetindex=1,func=self.test_bangdanxinxi)
        # for key, value in reqData.items():
        #     if value[0] != 'test_bangdanxinxi':
        #         continue
        #     time.sleep(1)
        #     value = json.loads(value[2])
        #     try:
        #         resp = requests.get(url=url, headers=headers, params=value)
        #         if resp.json()['code'] == 0:
        #             Excel.ExcelUntil(reqPath).update_cell(int(key[3:]) - 1, 3, 'ok', sheetIndex=1)
        #         else:
        #             raise Exception
        #     except:
        #         Excel.ExcelUntil(reqPath).update_cell(int(key[3:]) - 1, 3, 'fail', sheetIndex=1)
        #         log.error("接口为：'bserver/record'，方法为：{0}\n参数为：{1}".format(self.test_bangdanxinxi.__name__, value))

    def test_bangdanxiangqing(self):
        # 榜单详情
        # 更新headers
        headers['time'] = str(time.time()).split('.')[0]
        headers['type'] = "11"
        to_requests(url=url,method='get',reqData=reqData,reqPath=reqPath,headers=headers,sheetindex=1,func=self.test_bangdanxiangqing)
        # for key, value in reqData.items():
        #     if value[0] != 'test_bangdanxiangqing':
        #         continue
        #     time.sleep(1)
        #     value = json.loads(value[2])
        #     try:
        #         resp = requests.get(url=url, headers=headers, params=value)
        #         if resp.json()['code'] == 0:
        #             Excel.ExcelUntil(reqPath).update_cell(int(key[3:]) - 1, 3, 'ok', sheetIndex=1)
        #         else:
        #             raise Exception
        #     except:
        #         Excel.ExcelUntil(reqPath).update_cell(int(key[3:]) - 1, 3, 'fail', sheetIndex=1)
        #         log.error("接口为：'bserver/record'，方法为：{0}\n参数为：{1}".format(self.test_bangdanxiangqing.__name__, value))

    def test_shudanhuanyihuan(self):
        # 书单换一换
        # 更新headers
        headers['time'] = str(time.time()).split('.')[0]
        headers['type'] = "07"
        to_requests(url=url,method='get',reqData=reqData,reqPath=reqPath,headers=headers,sheetindex=1,func=self.test_shudanhuanyihuan)
        # for key, value in reqData.items():
        #     if value[0] != 'test_shudanhuanyihuan':
        #         continue
        #     time.sleep(1)
        #     value = json.loads(value[2])
        #     try:
        #         resp = requests.get(url=url, headers=headers, params=value)
        #         if resp.json()['code'] == 0:
        #             Excel.ExcelUntil(reqPath).update_cell(int(key[3:]) - 1, 3, 'ok', sheetIndex=1)
        #         else:
        #             raise Exception
        #     except:
        #         Excel.ExcelUntil(reqPath).update_cell(int(key[3:]) - 1, 3, 'fail', sheetIndex=1)
        #         log.error("接口为：'bserver/record'，方法为：{0}\n参数为：{1}".format(self.test_shudanhuanyihuan.__name__, value))

    def test_tuijianwei(self):
        # 推荐位
        # 更新headers
        headers['time'] = str(time.time()).split('.')[0]
        headers['type'] = "08"
        to_requests(url=url,method='get',reqData=reqData,reqPath=reqPath,headers=headers,sheetindex=1,func=self.test_tuijianwei)
        # for key, value in reqData.items():
        #     if value[0] != 'test_tuijianwei':
        #         continue
        #     time.sleep(1)
        #     value = json.loads(value[2])
        #     try:
        #         resp = requests.get(url=url, headers=headers, params=value)
        #         if resp.json()['code'] == 0:
        #             Excel.ExcelUntil(reqPath).update_cell(int(key[3:]) - 1, 3, 'ok', sheetIndex=1)
        #         else:
        #             raise Exception
        #     except:
        #         Excel.ExcelUntil(reqPath).update_cell(int(key[3:]) - 1, 3, 'fail', sheetIndex=1)
        #         log.error("接口为：'bserver/record'，方法为：{0}\n参数为：{1}".format(self.test_tuijianwei.__name__, value))

    def test_shudanxiangqing(self):
        # 书单详情
        # 更新headers
        headers['time'] = str(time.time()).split('.')[0]
        headers['type'] = "22"
        to_requests(url=url,method='get',reqData=reqData,reqPath=reqPath,headers=headers,sheetindex=1,func=self.test_shudanxiangqing)
        # for key, value in reqData.items():
        #     if value[0] != 'test_shudanxiangqing':
        #         continue
        #     time.sleep(1)
        #     value = json.loads(value[2])
        #     try:
        #         resp = requests.get(url=url, headers=headers, params=value)
        #         if resp.json()['code'] == 0:
        #             Excel.ExcelUntil(reqPath).update_cell(int(key[3:]) - 1, 3, 'ok', sheetIndex=1)
        #         else:
        #             raise Exception
        #     except:
        #         Excel.ExcelUntil(reqPath).update_cell(int(key[3:]) - 1, 3, 'fail', sheetIndex=1)
        #         log.error("接口为：'bserver/record'，方法为：{0}\n参数为：{1}".format(self.test_shudanxiangqing.__name__, value))

    def test_tuijianweixinxi(self):
        # 推荐位信息
        # 更新headers
        headers['time'] = str(time.time()).split('.')[0]
        headers['type'] = "08"
        to_requests(url=url,method='get',reqData=reqData,reqPath=reqPath,headers=headers,sheetindex=1,func=self.test_tuijianweixinxi)
        # for key, value in reqData.items():
        #     if value[0] != 'test_tuijianweixinxi':
        #         continue
        #     time.sleep(1)
        #     value = json.loads(value[2])
        #     try:
        #         resp = requests.get(url=url, headers=headers, params=value)
        #         if resp.json()['code'] == 0:
        #             Excel.ExcelUntil(reqPath).update_cell(int(key[3:]) - 1, 3, 'ok', sheetIndex=1)
        #         else:
        #             raise Exception
        #     except:
        #         Excel.ExcelUntil(reqPath).update_cell(int(key[3:]) - 1, 3, 'fail', sheetIndex=1)
        #         log.error("接口为：'bserver/record'，方法为：{0}\n参数为：{1}".format(self.test_tuijianweixinxi.__name__, value))

    def test_shudanxiangqing(self):
        # 推荐位信息
        # 更新headers
        headers['time'] = str(time.time()).split('.')[0]
        headers['type'] = "22"
        to_requests(url=url,method='get',reqData=reqData,reqPath=reqPath,headers=headers,sheetindex=1,func=self.test_shudanxiangqing)
        # for key, value in reqData.items():
        #     if value[0] != 'test_shudanxiangqing':
        #         continue
        #     time.sleep(1)
        #     value = json.loads(value[2])
        #     try:
        #         resp = requests.get(url=url, headers=headers, params=value)
        #         if resp.json()['code'] == 0:
        #             Excel.ExcelUntil(reqPath).update_cell(int(key[3:]) - 1, 3, 'ok', sheetIndex=1)
        #         else:
        #             raise Exception
        #     except:
        #         Excel.ExcelUntil(reqPath).update_cell(int(key[3:]) - 1, 3, 'fail', sheetIndex=1)
        #         log.error("接口为：'bserver/record'，方法为：{0}\n参数为：{1}".format(self.test_shudanxiangqing.__name__, value))

    def test_pubuliushudan(self):
        # 瀑布流书单
        # 更新headers
        headers['time'] = str(time.time()).split('.')[0]
        headers['type'] = "30"
        to_requests(url=url,method='get',reqData=reqData,reqPath=reqPath,headers=headers,sheetindex=1,func=self.test_pubuliushudan)

    def test_gundongtiaoxinxi(self):
        # 滚动条信息
        # 更新headers
        headers['time'] = str(time.time()).split('.')[0]
        headers['type'] = "20"
        to_requests(url=url,method='get',reqData=reqData,reqPath=reqPath,headers=headers,sheetindex=1,func=self.test_gundongtiaoxinxi)

if __name__ == '__main__':
    unittest.main()

