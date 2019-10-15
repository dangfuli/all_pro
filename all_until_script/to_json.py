#coding=utf-8
import urllib.parse
import json
'''转化从charles复制下来的字串，转为json格式'''
def to_str(body_str):
    '''检查需要转化的str是否符合标准'''
    if not body_str == '':
        par = body_str.split("&")
        # print(par)
        _temp = []
        try:
            for each in par:
                if "=" not in each:
                    print("参数不合规，请检查")
                    return ''
                if len(each.split("=")) != 2:
                    print("参数不合规，请检查")
                    return ''
                if each.split("=")[1] != '':
                    _temp.append(each.split('=')[1])
        except:
            print("参数不合规，请检查")
            return ''
    else:
        print("传入为空：%s"%body_str)
        return ''
    return urllib.parse.unquote(body_str)

def to_json(body_str):
    '''转化格式'''
    try:
        body_str = to_str(body_str)
    except:
        return False
    body_dict = {}
    # print(body_str)
    for each in body_str.split("&"):
        body_dict[str(each.split("=")[0])] = str(each.split("=")[1])
    print(body_dict)
    with open("demo.json","w") as demo:
        demo.write(json.dumps(body_dict,indent=4))
if __name__ == '__main__':
    bstr = '123'
    to_json(bstr)