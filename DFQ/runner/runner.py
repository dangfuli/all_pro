# coding=utf-8
import time
import unittest

from lib.utils.HTMLTestRunner import HTMLTestRunner
from runner.install_app import *


def get_test():
    '''
    加载用例
    :return:
    '''
    case_path = os.path.join(os.path.abspath(".."),"case")
    print(case_path)
    discover = unittest.defaultTestLoader.discover(case_path,pattern="*.py")
    testcase = unittest.TestSuite()   # 创建单元套件，添加用例到套件
    for test_suit in discover:
        for i in test_suit:
            testcase.addTest(i)
    return testcase

def html_report(report_path=os.path.join(os.path.abspath(".."),"report")):
    ## 拼接输出报告的路径
    report = time.strftime("%m-%d-%H-%M",time.localtime())
    path = report_path + "\\" + report + ".html"
    ## 打开报告
    f = open(path,"wb")
    runner = HTMLTestRunner(stream=f,title="test-report",description="run of description")
    runner.run(get_test())
    f.close()
if __name__ == '__main__':
    installApp()
    html_report()