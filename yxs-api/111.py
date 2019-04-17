import datetime
import time
import os,sys
def a():
    print('run')
    print(sys._getframe().f_back.f_code.co_name)
def b():
    a()
print(b())