# coding=utf-8
import re
#@classmethod
hostPath = 'C:/Windows/System32/drivers/etc/hosts'
hostData = ['test1','test2','test3']
hostName = 'crm.91bihu.com'
def readHost(hostPath):
    '''
    读取host文件
    :param hostPath: 传入hosts路径地址
    :return: data_str，读取的data
    '''
    try:
        host = open(hostPath,'r',encoding='utf-8')
    except:
        host = open(hostPath,'r',encoding='utf-16')
    finally:
        data_str = host.read()
        host.close()
        print(data_str)
        return data_str

def writeHost(hostPath,hostData,hostName):
    '''
    写入host
    :param hostPath: host路径地址
    :param hostData: 需要传入修改的host，list格式
    :param hostName: 需要修改的http地址，字符串格式，例如：crm.91bihu.com
    :return: True or False
    '''
    loc = readHost(hostPath)
    oldHost = re.findall('(.+?) %s'%hostName,loc)
    print(oldHost)
    for each in oldHost:
        if '#' in each:
            oldHost.remove(each)
    print(oldHost)
    if oldHost[0] in hostData:
        #判断是否在host数据列表中
        try:
            index = hostData.index(oldHost[0])
            if len(hostData)-1 == index:
                newHost = hostData[0]
            else:
                newHost = hostData[index+1]
            rewriteHost = loc.replace(oldHost[0]+' '+hostName,newHost+' '+hostName)
            with open(hostPath,'w',encoding='utf-8') as f:
                f.write(rewriteHost)
                # print(f.read())
            return True
        except Exception as e:
            print('报错了：%s'% e)
            return False
    elif len(oldHost) >= 1:
        rewriteHost = loc.replace(oldHost[0]+' '+hostName,hostData[0] + ' ' + hostName)
        with open(hostPath,'w',encoding='utf-8') as f:
            f.write(rewriteHost)
            #print(f.read())
            return True
    else:
        #没有配置此网址host，配置host，默认配置hostData第一个
        print('没有配置host，正在配置......')
        with open(hostPath,'w',encoding='utf-8') as f1:
            f1.write(loc+'\n'+hostData[0]+' '+hostName)
        return True

if __name__ == '__main__':
    # readHost(hostPath)
    writeHost(hostPath,hostData,hostName)
