# coding=utf-8
import unittest

from appium import webdriver

from lib.Mine import *

## 读取配置文件
desired_caps = getElement(r"D:\auto\DFQ\configs\desired_caps.conf")
class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        cls.driver.wait_activity(".base,ui.MainActivity",10)
    def test01(self):
        ## 只输入电话号码为123，验证码为空
        login(self.driver,phone='123',verify="")
        clear_phone(self.driver)
    def test02(self):
        ## 输入电话号码为空，验证码为空
        login(self.driver,phone="",verify="")
        clear_phone(self.driver)


if __name__ == '__main__':
    unittest.main()