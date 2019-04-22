import datetime
import time
import os,sys
import requests

url = "http://test.gaokaoceshi.cc/jobserver/job"

payload = {"type":"01"}
headers = {
    'code': "59",
    'platform': "android",
    'time': "1555566869767",
    'channelNum': "invite",
    'usercode': "43ed6d71b6657032f29e319652f3ff9d",
    'token': "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJjZWIzNzI5M2FmYWI3NGNkOTMwYzZmODA4ZDM4OTJlNSIsImlhdCI6MTU1NTU1MTUyNiwiZXhwIjoxNTU5NDM5NTI2fQ.pyz79B7cfoE_31uaCXuURDgD00jwqVesso13zvwe5Jw",
    'info': "8e652b3a034919850700fbbc6d1ef2f3",
    'type': "00",
    'cache-control': "no-cache",
    'Postman-Token': "edb588e9-cfce-440a-ab72-43d093200100"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)