# coding=utf-8
import os

def installApp(appName=None):
    '''
    安装app
    :param appName:app名称，不要添加后缀名
    :return:
    '''
    ## 获取app路径
    app_path = os.path.join(os.path.abspath(".."),"App")
    print(app_path)
    ## 安装替换app
    app_list = os.listdir(app_path)
    if os.path.exists(str(app_path)+"\\"+str(appName)+".apk"):
        try:
            os.system(r"adb install -d -r {0}\{1}.apk".format(app_path,appName))
        except Exception as e:
            print("install app faild :%s" % e)
    elif len(app_list) >= 1:
        print("find apps in directery,install the least version")
        os.system(r"adb install -d -r {0}\{1}".format(app_path,app_list[-1]))
    else:
        print("can not find app,please del ext")
if __name__ == '__main__':
    dict1={"name":"x","sex":"male","home":"HB","age":"18"}
    installApp()

