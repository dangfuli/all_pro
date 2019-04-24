import datetime
import time
import os,sys
import requests
# from unittest import mock
# def need_mock():
#     a = 1
#     b = 2
#     return a+b
# def use_func():
#     print(need_mock())
#
# need_mock = mock.Mock(return_value={"key":"123","value":"321"})
#
l = [2,5,1,4,3,8,6]
for i in range(len(l))[::-1]:
    for j in range(i):
        if l[j] > l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)