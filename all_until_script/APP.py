# coding=utf-8
import os,time

class AppUntil:
    @staticmethod
    def swipUp(driver,time=500,n=1):
        '''上滑屏幕'''
        location = driver.get_window_size()
        x1 = location['width'] * 0.5  #起始X坐标
        y1 = location['height'] * 0.75  #起始Y坐标
        y2 = location['height'] * 0.25  #终点Y坐标
        for i in range(n):
            driver.swipe(x1,y1,x1,y2,time)

    @staticmethod
    def swipLeft(driver,time=500,n=1):
        '''左滑屏幕'''
        location = driver.get_window_size()
        x1 = location['width'] * 0.75
        y1 = location['height'] * 0.5
        x2 = location['width'] * 0.05
        for i in range(n):
            driver.swipe(x1,y1,x2,y1,time)

    @staticmethod
    def swipeRight(driver,time=500,n=1):
        '''右滑屏幕'''
        location = driver.get_window_size()
        x1 = location['width'] * 0.05
        y1 = location['height'] * 0.5
        x2 = location['width'] * 0.75
        for i in range(n):
            driver.swipe(x1,y1,x2,y1,time)

    @staticmethod
    def swipDown(driver,time=500,n=1):
        '''下滑屏幕'''
        location = driver.get_window_size()
        x1 = location['width'] * 0.5
        y1 = location['height'] * 0.25
        y2 = location['height'] *0.75
        for i in range(n):
            driver.swipe(x1,y1,x1,y2,time)
    @staticmethod
    def getCodeFromSms(timeout=20):
        os.system("adb logcat -c")
        cmd = 'adb logcat -d |findstr D/Mms/Txn'
        n = 0
        while n < timeout:
            smscode = os.popen(cmd).read()
            print(smscode)
            if smscode != " ":
                smscode = smscode.split("验证码:")[1].split(",")[0]
                print("code is {}:".format(smscode))
                return smscode

            else:
                time.sleep(1)
                n += 1
                print('已等待:{}秒'.format(n))
                continue
        print('短信接收失败！')

