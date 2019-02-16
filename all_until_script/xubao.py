# coding=utf-8
import os,time

# 检验如果没有找到requests包，pip下载
try:
    import requests
except ImportError:
    os.system('pip install requests')
    time.sleep(5)
    import requests

# 检验如果没有找到eastgui的包，pip下载
try:
    import easygui
except ImportError:
    os.system('pip install easygui')
    time.sleep(5)
    import easygui
import datetime
from  common import get_excel_data   # 获取桌面Excel 第一个sheet中的第一列中数据
from common import manage_txt
import random
class TestGetLicensePlate:
    # def __init__(self,Agent,CityCode):
    #    self.Agent = Agent
    #    self.CityCode = CityCode
    def result(self):
        msg = '使用方法：\n1、新建一个Excel(不用改名字，放在桌面) \n2、打开平时写车牌的网站，复制车牌（可以筛选一下成功率高的。）\n3、将车牌复制到新建的excel表里（第一个sheet页，车牌排列在第一列中）\n4、输入经纪人id以及城市id'
        title = '车牌信息'
        fieldNames = ["Agent","城市id"]
        enterlist = easygui.multenterbox(msg=msg,title=title,fields=fieldNames)   # 收集输入的agent和citycode
        work_path = r'C:\Users\Administrator\Desktop'
        assert_car_type_list = []   # 车辆类型判断列表
        count = 1  # 后面记录执行几个车牌
        now = datetime.datetime.now()  # 获取本机时间，datetime类型
        now.strftime('%Y-%m-%d %H:%M:%S')
        d = get_excel_data.ExcelUntil().get_excel()     # 调用获取桌面的Excel数据
        for i in d:         # for循环，遍历所有的车牌
            num = random.choice(['a','b','c''d','e','f','g','h','i','j','k','l','m'])
            url = 'http://qa.interfaces.com/api/CarInsurance/getreinfo?LicenseNo=%s&CityCode=%s&Agent=%s&CustKey=testtestt%s&SecCode=e9779d2c054d69306fc9fc0b93bfa8a9&CanShowNo=1&Group=1&TimeFormat=1' % (str(i),str(enterlist[1]),str(enterlist[0]),num)
            # print(url)
            start_time = time.time()   #计算续保耗时
            # 发出GET请求
            req = requests.get(url)
            end_time = time.time()
            result_time = '%.2f' %(end_time - start_time)
            j = req.json()
            # j = json.loads(req.json())
            # 解析json格式,判断车类型


 # 以下为判断-----------------------------------------------------------------------------------------------------------

            if j['StatusMessage'] == '续保成功':   # 续保成功，继续判断类型
                # 将json参数赋值
                CarUsedType = j['UserInfo']['CarUsedType']
                CredentislasNum = j['UserInfo']['CredentislasNum']
                InsuredIdCard = j['UserInfo']['InsuredIdCard']
                HolderIdCard = j['UserInfo']['HolderIdCard']
                ForceExpireDate = j['UserInfo']['ForceExpireDate']
                BusinessExpireDate = j['UserInfo']['BusinessExpireDate']
                Source = j['SaveQuote']['Source']
                # 判断交强险与商业险是否都为空，如为空则判断下一车辆
                if ForceExpireDate == '' and BusinessExpireDate == '':
                    assert_car_type_list = []
                    continue
                # 判断险种
                if Source == 1:
                    assert_car_type_list.append('太平洋')
                if Source == 2:
                    assert_car_type_list.append('平安')
                if Source == 4:
                    assert_car_type_list.append('人保')
                if Source == 8:
                    assert_car_type_list.append('国寿财')
                if Source == 16:
                    assert_car_type_list.append('中华联合')
                if Source == 32:
                    assert_car_type_list.append('大地')
                if Source == 64:
                    assert_car_type_list.append('阳光')
                if Source == 128:
                    assert_car_type_list.append('太平保险')
                if Source == 256:
                    assert_car_type_list.append('华安')
                if Source == 512:
                    assert_car_type_list.append('天安')
                if Source == 1024:
                    assert_car_type_list.append('英大')
                if Source == 2048:
                    assert_car_type_list.append('安盛天平')
                # 地区由传入citycode决定，不予判断

                # 判断公私车
                if len(j['UserInfo']['LicenseOwner']) >= 5 and len(j['UserInfo']['InsuredName']) >= 5 and len(j['UserInfo']['PostedName']) >= 5:
                    assert_car_type_list.append('公车')
                else:
                    assert_car_type_list.append('私车')
                    # 判断身份证信息
                    if str(CredentislasNum).replace(' ', '').isalnum() or str(InsuredIdCard).replace(' ','').isalnum() or str(HolderIdCard).replace(' ', '').isalnum() and len(str(HolderIdCard).replace(' ', '')) == 18 and len(str(InsuredIdCard).replace(' ', '')) == 18 and len(str(CredentislasNum).replace(' ', '')) == 18:
                        pass
                    else:
                        assert_car_type_list.append('身份证为空或格式不正确')
                # 判断车主与被保险人是否一致
                if j['UserInfo']['LicenseOwner'] == j['UserInfo']['InsuredName'] == j['UserInfo']['PostedName']:
                    pass
                else:
                    assert_car_type_list.append('车主与被保险人不一致')

                # 判断货车
                if CarUsedType == 6 or CarUsedType == 7 :
                    assert_car_type_list.append('货车')
                # 判断车价超过150万
                if  j['UserInfo']['PurchasePrice'] >= 1500000:
                    assert_car_type_list.append('车价超过150万')
                # 判断三证合一
                if j['UserInfo']['IdType'] == 9:
                    assert_car_type_list.append('三证合一')
                # 判断单商业
                if ForceExpireDate == '' and BusinessExpireDate != '':
                    assert_car_type_list.append('单商业')
                # 判断单交强
                if ForceExpireDate != '' and BusinessExpireDate == '':
                    assert_car_type_list.append('单交强')

                # 判断司机乘客险是否一致
                if j["SaveQuote"]['SiJi'] != j["SaveQuote"]['ChengKe']:
                    assert_car_type_list.append('司机乘客险不一致')
                # 判断新能源车
                if '电动' in j['UserInfo']['ModleName']:
                    assert_car_type_list.append('新能源车')
                # 判断车辆超过8年
                RegisterDate_str = str(j['UserInfo']['RegisterDate']) + ' ' + '23:59:59'  # 获取车辆购买时间
                # 将str格式时间转化成datetime
                registerdate_date = datetime.datetime.strptime(RegisterDate_str, '%Y-%m-%d %H:%M:%S')
                assert_time = now - registerdate_date  # 将本机时间减去购买时间，时间大于2920天，即超过8年
                if assert_time >= datetime.timedelta(days=2920):
                    assert_car_type_list.append('车辆超过8年')
                if ForceExpireDate != '' and BusinessExpireDate != '':     # 判断交强险与商业险其中任意一项为空不判断是否在同一天
                     # 判断交强险商业险不在同一天
                    f_time = datetime.datetime.strptime(str(ForceExpireDate),'%Y-%m-%d %H:%M:%S')   # 将交强与商业险的时间转化为datetime格式，作减法，等于0
                    b_time = datetime.datetime.strptime(str(BusinessExpireDate),'%Y-%m-%d %H:%M:%S')
                    if f_time - b_time == datetime.timedelta(days=0):
                        pass

                    elif f_time - b_time <= datetime.timedelta(hours=23) and f_time - b_time >= datetime.timedelta(hours=-23):
                        pass
                    else:
                        assert_car_type_list.append('交强险与商业险不在同一天')
                # 判断次新车
                if now - registerdate_date >= datetime.timedelta(days=365):
                    pass
                else:
                    assert_car_type_list.append('次新车')
                # 判断脱保车
                if ForceExpireDate != '' and BusinessExpireDate != '':
                    if b_time - now <= datetime.timedelta(days=0) or f_time - now <= datetime.timedelta(days=0):
                        assert_car_type_list.append('脱保车')
                elif ForceExpireDate == '' and BusinessExpireDate != '':
                    b_time = datetime.datetime.strptime(str(BusinessExpireDate), '%Y-%m-%d %H:%M:%S')
                    if b_time - now <= datetime.timedelta(days=0):
                        assert_car_type_list.append('脱保车')
                elif ForceExpireDate != '' and BusinessExpireDate == '':
                    f_time = datetime.datetime.strptime(str(ForceExpireDate), '%Y-%m-%d %H:%M:%S')
                    if f_time - now <= datetime.timedelta(days=0):
                        assert_car_type_list.append('脱保车')
                # 判断普通车
                if len(assert_car_type_list) == 2:
                    assert_car_type_list.append('普通车')

            else:
                assert_car_type_list = [i,'续保失败']
            copy_data = str(j)
            if '司机乘客险不一致' in str(assert_car_type_list):
                copy_data = copy_data.split("'BoLi'")[0]
            elif '续保失败' in str(assert_car_type_list):
                copy_data = str(j)
            else:
                copy_data = copy_data.split("'FuelType'")[0]
 #  以上为判断---------------------------------------------------------------------------------------------------------

            try:
                os.mkdir(work_path + r'\temp')    # 桌面位置创建文件夹’temp
            except:
                pass
            filename = os.path.join(work_path,'temp',i + '.txt' )

            count += 1      # 计数用

            # 调用写入txt文件方法
            if assert_car_type_list[1] == '续保失败':
                pass
            else:
                TestGetLicensePlate().write_txt(plate=i,type=assert_car_type_list,time=result_time,content=copy_data,filename=filename)
            assert_car_type_list = []  # 清空判断列表
        bool = easygui.boolbox(msg='已经读取完毕，是否继续？',choices=['继续','取消'])
        if bool == True:
            manage_txt.ManageTxt(work_path).txt()

    def write_txt(self,plate,type,time,content,filename):
        try:
            f = open(filename,'w')
            f.write(plate+'\n'+str(type) + '\n' + time + '\n'+content)
            f.close()
        except Exception as err:
            print('报错啦......报错内容为：%s' % err)

if __name__=='__main__':
    TestGetLicensePlate().result()