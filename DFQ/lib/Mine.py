# coding=utf-8
from DFQ.lib.utils.getConfig import *
elements = getElement(r"D:\auto\DFQ\elements\login.json")
print(elements)
def login(driver,phone="",verify=""):
    driver.find_element_by_id(elements["wode"]).click()
    driver.find_element_by_id(elements["weidenglu"]).click()
    driver.find_element_by_id(elements["shoujihao"]).send_keys(phone)
def clear_phone(driver):
    driver.find_element_by_id(elements["shoujihao"]).clear()

