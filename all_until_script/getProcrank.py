# coding=utf-8
import os,subprocess,re
def _getDevice():
    # 获取所有设备devices,获得一个tuple
    deviceRsp = subprocess.Popen("adb devices",stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True).communicate()[0]
    # 正则提取一下设备device，return一个list
    device = re.findall('(.*)\tdevice',deviceRsp.decode('utf8'))
    print(device)
    return device
def _getFileName(to_file,device):
    # 打开文件，根据设备名称决定
    __device_list = []
    for each in device:
        # str(each).replace(':','_').replace('.','') # 模拟器的坑
        if ":" in each:
            each = "62001"
        # 根据传入的路径判断
        if to_file is None:
             __device_list.append('{0}/{1}.txt'.format(os.getcwd(),each))
             # 删除已有文件
             if os.path.exists(__device_list):
                 os.remove(__device_list)
        else:
            # 传入路径没有加后缀，给补上
            if os.path.splitext(to_file)[1] == '':
                __device_list.append(os.path.join(to_file,'{0}.txt'.format(each)))
            else:
                __device_list.append(to_file)
                break
    return __device_list




def Procrank(to_file=None,package=None,device='',e_num=1000):
    '''
    :param to_file:写入文件路径
    :param pakage: 包名
    :param e_num: 结束循环的次数
    :return:
    '''
    # 检查设备id，如果没有id则获取
    try:
        if device =='':
            device = _getDevice()
        elif not isinstance(device,str):
            raise TypeError('设备device不正确，请给字串类型')
    except:
        raise Exception('获取设备错误_getDevice，或输入设备id错误')

    # 打开文件,,,##留个坑，后面用线程开
    d = _getFileName(to_file,device)
    try:
        f = open(d[0],'a+',encoding='utf8')
    except Exception as e:
        raise Exception('错误：%s\t文件打开失败，请确认文件路径，以及文件类型，建议txt文件'%e)
    if package is None:
        cmd = 'adb shell Procrank'
    else:
        cmd = 'adb shell Procrank |findstr {0}'.format(package)
    # 循环获取procrank
    for n in range(e_num):
        d = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True).stdout.read().decode('utf8')    #windows解码变成了空的，愁。。decode有坑
        print(str(d))
        f.write(str(d))
    f.close()

if __name__ == '__main__':
    to_file = r'C:\Users\dangfuli\Desktop\111\pro.txt'
    # print(os.path.splitext(to_file))
    ## com.yfax.android.zznovel
    ## com.xxzhkyly.tyz
    Procrank(to_file,package='com.yfax.android.zznovel',device='127.0.0.1:62001',e_num=240000)
    # print(_getFileName(to_file,_getDevice()))
    # _getFileName(to_file,device='127.0.0.1:62001')
    # _getDevice()
    # d = subprocess.Popen("adb shell Procrank |findstr com.yfax.android.zznovel", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).stdout.read()
    # print(d)