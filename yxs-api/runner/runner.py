# coding=utf-8
import time,os
import unittest
from lib.HTMLTestRunner import HTMLTestRunner
import sys,os
from apscheduler.schedulers.background import BackgroundScheduler

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
    # print(testcase)
    # return testcase
    testcase = unittest.TestSuite()
    testcase.addTests(discover)
    print(testcase)
    return testcase

def html_report(report_path=os.path.join(os.path.dirname(os.path.dirname(__file__)), "report")):
    ## 拼接输出报告的路径
    report = time.strftime("%m-%d-%H-%M", time.localtime())
    path = report_path + "/" + report + ".html"
    ## 打开报告
    f = open(path,"wb")
    f = open(path,"wb")
    runner = HTMLTestRunner(stream=f,title="test-report",description="run of description")
    runner.run(get_test())
    f.close()

if __name__ == '__main__':

    aps = BackgroundScheduler()
    aps.add_job(html_report,'interval',seconds=60)
    aps.start()

    while 1:
        try:
            print(time.strftime('%H:%M:%S',time.localtime()))
            time.sleep(60)
        except:
            aps.shutdown()
            print('end')
from selenium.webdriver.support import expected_conditions
expected_conditions.element_located_to_be_selected()

# <unittest.suite.TestSuite tests=[<unittest.suite.TestSuite tests=[<unittest.suite.TestSuite tests=[<t_books.Books testMethod=test_jrshujixiangqingye>, <t_books.Books testMethod=test_shujimulu>, <t_books.Books testMethod=test_shujineirong>, <t_books.Books testMethod=test_xiangtongshujitj>]>]>, <unittest.suite.TestSuite tests=[<unittest.suite.TestSuite tests=[<t_mine.Mine testMethod=test_bangdingzhifubao>, <t_mine.Mine testMethod=test_chakantixianlishi>, <t_mine.Mine testMethod=test_huoquhaoyou>, <t_mine.Mine testMethod=test_huoqujinbiliushui>, <t_mine.Mine testMethod=test_huoqutudiyuedu>, <t_mine.Mine testMethod=test_jinrushezhi>, <t_mine.Mine testMethod=test_jinrutixian>, <t_mine.Mine testMethod=test_jinruwode>, <t_mine.Mine testMethod=test_jinruxiaoxizhongxin>, <t_mine.Mine testMethod=test_jinruyaoqingye>, <t_mine.Mine testMethod=test_lianxikefu>, <t_mine.Mine testMethod=test_tixianxiadan>, <t_mine.Mine testMethod=test_tuichuxiaoxizhongxin>]>]>, <unittest.suite.TestSuite tests=[<unittest.suite.TestSuite tests=[<t_read.Read testMethod=test_huoquliulanjilu>, <t_read.Read testMethod=test_jiarushujia>, <t_read.Read testMethod=test_jinrushujia>, <t_read.Read testMethod=test_renqibangshudan>, <t_read.Read testMethod=test_shujizhiding>]>]>, <unittest.suite.TestSuite tests=[<unittest.suite.TestSuite tests=[<t_record.Record testMethod=test_appfenxiang>, <t_record.Record testMethod=test_jiarushujiaxinxi>, <t_record.Record testMethod=test_rihuo>, <t_record.Record testMethod=test_shudanbaoguang>, <t_record.Record testMethod=test_shudanhuanyihuan>, <t_record.Record testMethod=test_shujixiangqingye>, <t_record.Record testMethod=test_yuedujilu>]>]>, <unittest.suite.TestSuite tests=[<unittest.suite.TestSuite tests=[<t_renwu.Renwu testMethod=test_baishirenwu>, <t_renwu.Renwu testMethod=test_chufatuisongrenwu>, <t_renwu.Renwu testMethod=test_huoquqiandaoxinxi>, <t_renwu.Renwu testMethod=test_huoqurenwu>, <t_renwu.Renwu testMethod=test_jilurenwujindu>, <t_renwu.Renwu testMethod=test_lingqujinbi>, <t_renwu.Renwu testMethod=test_lingqutuisonghongbao>, <t_renwu.Renwu testMethod=test_qiandao>, <t_renwu.Renwu testMethod=test_qiandaofenxiang>, <t_renwu.Renwu testMethod=test_wanchengyuedurenwu>]>]>, <unittest.suite.TestSuite tests=[<unittest.suite.TestSuite tests=[<t_store.Store testMethod=test_bangdanxiangqing>, <t_store.Store testMethod=test_bangdanxinxi>, <t_store.Store testMethod=test_gundongtiaoxinxi>, <t_store.Store testMethod=test_huoqushuchengye>, <t_store.Store testMethod=test_pubuliushudan>, <t_store.Store testMethod=test_shuchengbanner>, <t_store.Store testMethod=test_shudanhuanyihuan>, <t_store.Store testMethod=test_shudanxiangqing>, <t_store.Store testMethod=test_shuijifenleixiangqing>, <t_store.Store testMethod=test_shujifenlei>, <t_store.Store testMethod=test_tagshudan>, <t_store.Store testMethod=test_tuijianwei>, <t_store.Store testMethod=test_tuijianweixinxi>]>]>]>
# <unittest.suite.TestSuite tests=[<unittest.suite.TestSuite tests=[<t_books.Books testMethod=test_jrshujixiangqingye>, <t_books.Books testMethod=test_shujimulu>, <t_books.Books testMethod=test_shujineirong>, <t_books.Books testMethod=test_xiangtongshujitj>]>, <unittest.suite.TestSuite tests=[<t_mine.Mine testMethod=test_bangdingzhifubao>, <t_mine.Mine testMethod=test_chakantixianlishi>, <t_mine.Mine testMethod=test_huoquhaoyou>, <t_mine.Mine testMethod=test_huoqujinbiliushui>, <t_mine.Mine testMethod=test_huoqutudiyuedu>, <t_mine.Mine testMethod=test_jinrushezhi>, <t_mine.Mine testMethod=test_jinrutixian>, <t_mine.Mine testMethod=test_jinruwode>, <t_mine.Mine testMethod=test_jinruxiaoxizhongxin>, <t_mine.Mine testMethod=test_jinruyaoqingye>, <t_mine.Mine testMethod=test_lianxikefu>, <t_mine.Mine testMethod=test_tixianxiadan>, <t_mine.Mine testMethod=test_tuichuxiaoxizhongxin>]>, <unittest.suite.TestSuite tests=[<t_read.Read testMethod=test_huoquliulanjilu>, <t_read.Read testMethod=test_jiarushujia>, <t_read.Read testMethod=test_jinrushujia>, <t_read.Read testMethod=test_renqibangshudan>, <t_read.Read testMethod=test_shujizhiding>]>, <unittest.suite.TestSuite tests=[<t_record.Record testMethod=test_appfenxiang>, <t_record.Record testMethod=test_jiarushujiaxinxi>, <t_record.Record testMethod=test_rihuo>, <t_record.Record testMethod=test_shudanbaoguang>, <t_record.Record testMethod=test_shudanhuanyihuan>, <t_record.Record testMethod=test_shujixiangqingye>, <t_record.Record testMethod=test_yuedujilu>]>, <unittest.suite.TestSuite tests=[<t_renwu.Renwu testMethod=test_baishirenwu>, <t_renwu.Renwu testMethod=test_chufatuisongrenwu>, <t_renwu.Renwu testMethod=test_huoquqiandaoxinxi>, <t_renwu.Renwu testMethod=test_huoqurenwu>, <t_renwu.Renwu testMethod=test_jilurenwujindu>, <t_renwu.Renwu testMethod=test_lingqujinbi>, <t_renwu.Renwu testMethod=test_lingqutuisonghongbao>, <t_renwu.Renwu testMethod=test_qiandao>, <t_renwu.Renwu testMethod=test_qiandaofenxiang>, <t_renwu.Renwu testMethod=test_wanchengyuedurenwu>]>, <unittest.suite.TestSuite tests=[<t_store.Store testMethod=test_bangdanxiangqing>, <t_store.Store testMethod=test_bangdanxinxi>, <t_store.Store testMethod=test_gundongtiaoxinxi>, <t_store.Store testMethod=test_huoqushuchengye>, <t_store.Store testMethod=test_pubuliushudan>, <t_store.Store testMethod=test_shuchengbanner>, <t_store.Store testMethod=test_shudanhuanyihuan>, <t_store.Store testMethod=test_shudanxiangqing>, <t_store.Store testMethod=test_shuijifenleixiangqing>, <t_store.Store testMethod=test_shujifenlei>, <t_store.Store testMethod=test_tagshudan>, <t_store.Store testMethod=test_tuijianwei>, <t_store.Store testMethod=test_tuijianweixinxi>]>]>