from lib.flow import *
# 加载配置
log = Log.Log()
reqData = Excel.ExcelUntil(reqPath).read_row(skip=1)

url = URI + 'bserver/record'
class Record(unittest.TestCase):

    def test_rihuo(self):
        # 日活接口
        # 更新header时间与type
        headers['time'] = str(time.time()).split('.')[0]
        headers['type'] = "00"
        for key,value in reqData.items():
            if value[0] != 'rihuo':
                break
            time.sleep(1)
            try:
                resp = requests.post(url=url,headers=headers,data=value[1])
                if resp.json()['code'] == 0:
                    Excel.ExcelUntil(reqPath).update_cell(int(key[3:]) - 1, 3, 'ok')
                else:
                    raise Exception
            except:
                Excel.ExcelUntil(reqPath).update_cell(int(key[3:])-1,3,'fail')
                log.error("接口为：'bserver/record'，方法为：{0}\n参数为：{1}".format(self.test_rihuo.__name__,value))
            Excel.ExcelUntil(reqPath).update_cell(int(key[3:])-1,3,'ok')


    def test_yuedujilu(self):
        # 阅读记录接口
        # 更新header时间，添加type
        headers['time'] = str(time.time()).split('.')[0]
        headers['type'] = "10"

        # 所有的yuedujilu的接口
        for key,value in reqData.items():
            if value[0] == 'test_shudanbaoguang':
                break
            if value[0] != 'test_yuedujilu':
                continue
            time.sleep(1)
            value = json.loads(value[1])
            value['startTime'] = '{0}'.format(time.strftime('%Y%m%d%H%M%S',time.localtime()))
            try:
                resp = requests.post(url=url,headers=headers,json=value)
                if resp.json()['code'] == 0:
                    Excel.ExcelUntil(reqPath).update_cell(int(key[3:]) - 1, 3, 'ok')
                else:
                    raise Exception
            except:
                Excel.ExcelUntil(reqPath).update_cell(int(key[3:]) - 1, 3, 'fail')
                log.error("接口为：'bserver/record'，方法为：{1}\n请求参数为：{0}".format(value,self.test_yuedujilu.__name__))

            Excel.ExcelUntil(reqPath).update_cell(int(key[3:]) - 1, 3, 'ok')

    def test_shudanbaoguang(self):
        # 书单曝光记录接口
        headers['time'] = str(time.time()).split('.')[0]
        headers['type'] = '11'

        # 所有请求循环
        for key,value in reqData.items():
            if value[0] == 'test_shujixiangqingye':
                break
            if value[0] != 'test_shudanbaoguang':
                continue
            time.sleep(1)
            value = json.loads(value[1])
            value['startTime'] = '{0}'.format(time.strftime('%Y%m%d%H%M%S',time.localtime()))

            try:
                resp = requests.post(url=url,headers=headers,json=value)
                if resp.json()['code'] == 0:
                    Excel.ExcelUntil(reqPath).update_cell(int(key[3:]) - 1, 3, 'ok')
                else:
                    raise Exception
            except:
                Excel.ExcelUntil(reqPath).update_cell(int(key[3:])-1,3,'fail')
                log.error("接口为：'bserver/record'，方法为：{1}\n请求参数为：{0}".format(value,self.test_shudanbaoguang.__name__))

            Excel.ExcelUntil(reqPath).update_cell(int(key[3:])-1,3,'ok')

    def test_shujixiangqingye(self):
        # 书籍详情页曝光记录接口
        headers['time'] = str(time.time()).split('.')[0]
        headers['type'] = '12'

        # 所有请求循环
        for key,value in reqData.items():
            if value[0] == 'test_shudanhuanyihuan':
                break
            if value[0] != 'test_shujixiangqingye':
                continue
            time.sleep(1)
            value = json.loads(value[1])
            value['startTime'] = '{0}'.format(time.strftime('%Y%m%d%H%M%S',time.localtime()))

            try:
                resp = requests.post(url=url,headers=headers,json=value)
                if resp.json()['code'] == 0:
                    Excel.ExcelUntil(reqPath).update_cell(int(key[3:]) - 1, 3, 'ok')
                else:
                    raise Exception
            except:
                Excel.ExcelUntil(reqPath).update_cell(int(key[3:])-1,3,'fail')
                log.error("接口为：'bserver/record'，方法为：{1}\n请求参数为：{0}".format(value,self.test_shujixiangqingye.__name__))
            Excel.ExcelUntil(reqPath).update_cell(int(key[3:])-1,3,'ok')

    def test_shudanhuanyihuan(self):
        # 书籍详情页曝光记录接口
        headers['time'] = str(time.time()).split('.')[0]
        headers['type'] = '13'

        # 所有请求循环
        for key, value in reqData.items():
            if value[0] == 'test_jiarushujiaxinxi':
                break
            if value[0] != 'test_shudanhuanyihuan':
                continue
            time.sleep(1)
            value = json.loads(value[1])
            value['startTime'] = '{0}'.format(time.strftime('%Y%m%d%H%M%S', time.localtime()))

            try:
                resp = requests.post(url=url, headers=headers, json=value)
                if resp.json()['code'] == 0:
                    Excel.ExcelUntil(reqPath).update_cell(int(key[3:]) - 1, 3, 'ok')
                else:
                    raise Exception

            except:
                Excel.ExcelUntil(reqPath).update_cell(int(key[3:]) - 1, 3, 'fail')
                log.error("接口为：'bserver/record'，方法为：{1}\n请求参数为：{0}".format(value, self.test_shudanhuanyihuan.__name__))
            Excel.ExcelUntil(reqPath).update_cell(int(key[3:]) - 1, 3, 'ok')

    def test_jiarushujiaxinxi(self):
        # 加入书架信息
        headers['time'] = str(time.time()).split('.')[0]
        headers['type'] = '14'

        # 所有请求循环
        for key, value in reqData.items():
            if value[0] == 'test_appfenxiang':
                break
            if value[0] != 'test_jiarushujiaxinxi':
                continue
            time.sleep(1)
            value = json.loads(value[1])
            value['startTime'] = '{0}'.format(time.strftime('%Y%m%d%H%M%S', time.localtime()))

            try:
                resp = requests.post(url=url, headers=headers, json=value)
                if resp.json()['code'] == 0:
                    Excel.ExcelUntil(reqPath).update_cell(int(key[3:]) - 1, 3, 'ok')
                else:
                    raise Exception

            except:
                Excel.ExcelUntil(reqPath).update_cell(int(key[3:]) - 1, 3, 'fail')
                log.error("接口为：'bserver/record'，方法为：{1}\n请求参数为：{0}".format(value, self.test_jiarushujiaxinxi.__name__))
            Excel.ExcelUntil(reqPath).update_cell(int(key[3:]) - 1, 3, 'ok')

    def test_appfenxiang(self):
        # 加入书架信息
        headers['time'] = str(time.time()).split('.')[0]
        headers['type'] = '02'

        # 所有请求循环
        for key, value in reqData.items():
            if value[0] != 'test_appfenxiang':
                continue
            time.sleep(1)
            value = json.loads(value[1])
            value['startTime'] = '{0}'.format(time.strftime('%Y%m%d%H%M%S', time.localtime()))
            value['code'] = '{0}'.format(time.time())

            try:
                resp = requests.post(url=url, headers=headers, json=value)
                if resp.json()['code'] == 0:
                    Excel.ExcelUntil(reqPath).update_cell(int(key[3:]) - 1, 3, 'ok')
                else:
                    raise Exception
            except:
                Excel.ExcelUntil(reqPath).update_cell(int(key[3:]) - 1, 3, 'fail')
                log.error("接口为：'bserver/record'，方法为：{1}\n请求参数为：{0}".format(value, self.test_appfenxiang.__name__))


if __name__ == '__main__':
    unittest.main()