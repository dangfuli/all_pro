# coding=utf-8
import time,os,sys,unittest
sys.path.append('../')
from lib.HTMLTestRunner import HTMLTestRunner
# from apscheduler.schedulers.background import BackgroundScheduler
from lib.sendMail import *
def get_test():
    '''
    加载用例
    :return:
    '''
    case_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "case")
    print(case_path)
    discover = unittest.defaultTestLoader.discover(case_path,pattern="t_*.py")
    # testcase = unittest.TestSuite()   # 创建单元套件，添加用例到套件
    # for test_suit in discover:
    #     for i in test_suit:
    #         testcase.addTest(i)
    #
    # return testcase
    testcase = unittest.TestSuite()
    testcase.addTests(discover)
    return testcase

def html_report(report_path=os.path.join(os.path.dirname(os.path.dirname(__file__)),'report')):
    ## 拼接输出报告的路径
    path = report_path + "/" + time.strftime("%m-%d-%H-%M", time.localtime()) + ".html"
    ## 打开报告
    f = open(path,"wb")
    runner = HTMLTestRunner(stream=f,title="test-report",description="run of description")
    runner.run(get_test())
    f.close()
report_file = '../report/{0}.html'.format(time.strftime("%m-%d-%H-%M", time.localtime()))
# html_report()
# send_mail(report_file)

# if __name__ == '__main__':
#     aps = BackgroundScheduler()
#     aps.add_job(html_report,'interval',seconds=60)
#     aps.start()

#     while 1:
#         try:
#             print(time.strftime('%H:%M:%S',time.localtime()))
#             time.sleep(60)
#         except:
#             aps.shutdown()
#             print('end')

