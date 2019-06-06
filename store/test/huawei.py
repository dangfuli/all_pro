from appium import webdriver
import time
desired_caps = {
	'platformName': 'Android',
    'platformVersion': '6.0',
    'deviceName': 'RDT0215B03000935',
    'appPackage': 'com.huawei.appmarket',
    'appActivity': 'com.huawei.appmarket.MainActivity',
    'newCommandTimeout': 300,
    'UnicodeKeyboard': True,
    'resetKeyboard': True,
    'automationName':'Uiautomator 2'
}
driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub',desired_capabilities=desired_caps)
driver.find_element_by_id('android:id/button1').click()
driver.implicitly_wait(20)
driver.find_element_by_id("com.huawei.appmarket:id/openWlanUpdateBtn").click()
driver.find_element_by_id('com.huawei.appmarket:id/enter_button').click()
time.sleep(3)
driver.find_element_by_id('android:id/button2').click()
driver.find_element_by_id('com.huawei.appmarket:id/search_edit_text').click()
driver.find_element_by_id('com.huawei.appmarket:id/searchText').send_keys('悦小说')
driver.find_element_by_id('com.huawei.appmarket:id/search_title_icon').click()


