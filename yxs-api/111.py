import datetime
import time
import os,sys
import requests
from unittest import mock
def need_mock():
    a = 1
    b = 2
    return a+b
def use_func():
    print(need_mock())

need_mock = mock.Mock(return_value={"key":"123","value":"321"})

