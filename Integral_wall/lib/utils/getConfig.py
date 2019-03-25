# coding=utf-8
import os,subprocess
def getElement(file):
    '''
    元素以json数据格式存储，此方法读取文件
    :param file: 数据文件，json格式
    :return: dict
    '''
    if os.path.exists(file):
        try:
            f = open(file,"r")
        except:
            print("打开文件{0}错误".format(file))
            return {}
        try:
            elements = eval(f.read())
            # print(type(elements))
            return elements
        except:
            print("解析文件{0}错误".format(file))
            return {}

    else:
        print("can not find .json file")
        return {}

def getDevices(EM_host=[]):
    '''
    获取设备devices
    :param EM_host:如果有模拟器，将模拟器host加到这个list里面
    :return:
    '''
    ## 优先检查虚拟设备连接状态
    if EM_host != []:
        for host in EM_host:
            res = subprocess.Popen("adb connect %s"%host,stderr=subprocess.PIPE,stdout=subprocess.PIPE).communicate()
            if res[1] != b'':
                print('输入模拟机host有错误，清检查！！！%s'% res[1])
                return []
            if b'unable to connect' in res[0]:
                print('设备连接失败，名称为；%s'%host)


if __name__ == '__main__':
    getElement(r"D:\auto\DFQ\elements\login.json")
