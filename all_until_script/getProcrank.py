import os,subprocess,re
def _getDevice():
    # 获取所有设备devices,获得一个tuple
    deviceRsp = subprocess.Popen("adb devices",stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True).communicate()[0]
    # 正则提取一下设备device，return一个list
    device = re.findall('(.*)\tdevice',deviceRsp.decode('utf8'))
    print(device)
    return device
def _getFileName(to_file,device):
    # 打开文件，根据设备名称决定，默认用夜神模拟器，端口62001
    __device_list = []
    for each in device:
        str(each).replace(':','_').replace('.','') # 模拟器的坑
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

def procrank(to_file=None,package=None,device='',e_num=1000):
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

    # 打开文件
    d = _getFileName(to_file,device)
    try:
        f = open(d[0],'a+',encoding='utf8')
    except Exception as e:
        raise Exception('错误：%s\t文件打开失败，请确认文件路径，以及文件类型，建议txt文件'%e)
    if package is None:
        cmd = 'adb shell procrank'
    elif os.name == 'posix':
        cmd = 'adb shell procrank |grep {0}'.format(package)
    elif os.name == 'nt':
        cmd = 'adb shell procrank |findstr {0}'.format(package)

    # 循环获取procrank
    for n in range(e_num):
        # windows解码byte类型变成了空,mac解码变成了str，统一用byte
        d = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True).stdout.read()
        print(str(d))
        f.write(str(d))
    f.close()

if __name__ == '__main__':
    to_file = '1.txt'
    procrank(to_file,package='com.android.gallery3d',device='127.0.0.1:62001',e_num=240000)