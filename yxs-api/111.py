import re
nane =  []
print(name)
html = "人保舒适  未勾选核保重:asdlkasjdak的洒家 11.11元 查看详情 报价失败:z原因：VPN无法连接"
htm3 = ";太平洋  未勾选核保重:asdlkasjdak的洒家 11.11元 查看详情 重复投保 报价失败:z原因：VPN无法连接"
htm4 = ""
htm5 = " 国寿财  报价成功未勾选核保重:asdlkasjdak的洒家 12222.11元 查看详情 :z原因：VPN无法连接"
nane.append(html)
nane.append(htm3)
nane.append(htm4)
nane.append(htm5)

print([re.findall('(^\w{2,3})',x) for x in nane])
# for i in nane:
#     result.extend(re.findall('(^\w{2,3})',i))
#     # print(re.findall('(^\w{2,3})',s))
#     # print(re.findall('^\w{2,3}',html))
#     # print(re.findall('^\w{2,3}',htm4))
#     # print(re.findall('^\w{2,3}',htm5))
# print(result)


