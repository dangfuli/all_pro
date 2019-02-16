#coding=utf-8
import urllib.parse
import json
import re
'''转化从charles复制下来的字串，转为json格式'''
def check_body_str(body_str):
    '''检查需要转化的str是否符合标准'''
    if not body_str == '':
        par = body_str.split("&")
        # print(par)
        _temp = []
        try:
            for each in par:
                if "=" not in each:
                    print("参数不合规，请检查")
                    break
                if len(each.split("=")) != 2:
                    print("参数不合规，请检查")
                    break
                if each.split("=")[1] != '':
                    _temp.append(each.split('=')[1])
        except:
            print("参数不合规，请检查")
    else:
        print("传入为空：%s"%body_str)
    return urllib.parse.unquote(body_str)
def to_json(body_str):
    '''转化格式'''
    body_str = check_body_str(body_str)
    body_dict = {}
    # print(body_str)
    for each in body_str.split("&"):
        body_dict[str(each.split("=")[0])] = str(each.split("=")[1])
    print(body_dict)
    with open("demo.json","w") as demo:
        demo.write(json.dumps(body_dict,indent=4))
if __name__ == '__main__':
    bstr = 'appVersion=0.6.0&bizId=392&cart=%7B%0A%20%20%22settleShops%22%20%3A%20%5B%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22eta%22%20%3A%200%2C%0A%20%20%20%20%20%20%22deliveryType%22%20%3A%200%2C%0A%20%20%20%20%20%20%22tradAble%22%20%3A%20false%2C%0A%20%20%20%20%20%20%22deliveryTime%22%20%3A%200%2C%0A%20%20%20%20%20%20%22realPrice%22%20%3A%200%2C%0A%20%20%20%20%20%20%22saveMoney%22%20%3A%200%2C%0A%20%20%20%20%20%20%22orderPrice%22%20%3A%200%2C%0A%20%20%20%20%20%20%22realPayPrice%22%20%3A%200%2C%0A%20%20%20%20%20%20%22deliveryPrice%22%20%3A%200%2C%0A%20%20%20%20%20%20%22itemIsExpended%22%20%3A%20false%2C%0A%20%20%20%20%20%20%22afterFavPrice%22%20%3A%200%2C%0A%20%20%20%20%20%20%22payType%22%20%3A%200%2C%0A%20%20%20%20%20%20%22items%22%20%3A%20%5B%0A%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%22status%22%20%3A%200%2C%0A%20%20%20%20%20%20%20%20%20%20%22itemId%22%20%3A%20%223458764696029692713%22%2C%0A%20%20%20%20%20%20%20%20%20%20%22mdu%22%20%3A%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%22itemId%22%20%3A%20%223458764696029692713%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22amount%22%20%3A%201%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22status%22%20%3A%200%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22price%22%20%3A%20100%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22specialPrice%22%20%3A%200%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22mduId%22%20%3A%20%22044D1A776F039925E4AF1131A220BEA8%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22subItems%22%20%3A%20%5B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22itemId%22%20%3A%20%223458764696105190185%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22contentId%22%20%3A%20%223458764599715889959%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22shopId%22%20%3A%20%221152921673201876998%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22shortDesc%22%20%3A%20%22%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22itemName%22%20%3A%20%22subitem1%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22stock%22%20%3A%200%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22price%22%20%3A%20100%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22status%22%20%3A%201%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22currency%22%20%3A%20%22MXN%22%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22currency%22%20%3A%20%22MXN%22%0A%20%20%20%20%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%20%20%20%20%22stock%22%20%3A%200%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%5D%2C%0A%20%20%20%20%20%20%22shopId%22%20%3A%20%221152921673201876998%22%2C%0A%20%20%20%20%20%20%22cShopStatus%22%20%3A%200%0A%20%20%20%20%7D%0A%20%20%5D%0A%7D&channel=AppStore&cityId=52140500&clientType=6&dataType=9&deviceId=2db6d71a4e919355b733305f848c26a7&deviceType=iPhone&imei=2db6d71a4e919355b733305f848c26a7&ip=&lat=20.627399&lng=-103.323752&local=en-US&locationType=1&mapType=wgs84&networkType=WIFI&operatorName=%E4%B8%AD%E5%9B%BD%E8%81%94%E9%80%9A&osType=1&osVersion=11.2.1&poiCityId=52140500&poiId=Ek9Eci4gUi4gTWljaGVsIDMwMDAsIEFsYW1vIEluZHVzdHJpYWwsIDQ1NTkzIFNhbiBQZWRybyBUbGFxdWVwYXF1ZSwgSmFsLiwgTWV4aWNvIhsSGQoUChIJlRBxqVCyKIQRMgiJmdnGGgwQuBc&poiLat=20.627399&poiLng=-103.323752&poiName=Avenida%20Doctor%20Roberto%20Michel%2C%203000&requestId=067CFFFC00A44297E1DF8F5C73191660&suuid=2db6d71a4e919355b733305f848c26a7&terminalId=300103&timestamp=1546510383&token=wBETlCI7hXFQBGQ0Kv2hxtWubNf0rqqGM96CQG4jHBcUyDlOwDAQhtG7fC2j6B-Pl3juQE_LEpbGSCCqKHdHqZ70TpZIYtMmjOWkG6uQTfJqrCB9tBk-enj4fl8lZaxG8viE8UyC8UKWOdV3b6GYw7vxRrqmcZAnv99_P68HGZL7ZbyT3mqve4kxjA-Sh1YkeZfqGI7xSXL7Rer6DwAA__8%3D&versionCode=0.6.0&wifiMac=Didi-wireless&wifiName=Didi-wireless'
    to_json(bstr)