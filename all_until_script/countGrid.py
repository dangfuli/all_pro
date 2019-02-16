#coding=utf-8
import os,re
def Main():
    start = input('请将文件夹拖入命令框内：')
    print('开始获取......')
    print('正在处理文件......\n\n')
    TextCount = get_file(start)
    #print(wav)
    #print(TextGrid)
    # 计数处理文件
    # print(wav)
    # print(TextGrid)
    print('所有有效wav文件数量为：%s\n\n' % TextCount[0])
    print('所有有效的标注次数为：%s\n\n' % TextCount[1])
    quit = input('输入任意字符退出脚本：')
# def dealText(textList):
#     '''处理textgrid文件，计算有效数量
#        传入list
#        return 次数
#     '''
#     # for 循环打开文件，处理文件
#     count = 0
#     for i in textList:
#         with open(i,'r',encoding='utf-16') as f :
#             textLine = f.read()
#             textLine.replace(' ','')
#             if len(textLine) > 7:
#                 count += 1
#     print(count)
#     return count

def get_file(DirPath):
    '''收集需要查询文件的数量
        return count
        '''
    dirList = []
    fileList = []
    countTg = 0
    countWav = 0
    for root, dirs, files in os.walk(DirPath):
        for dir in dirs:
            # print(os.path.join(root,dir))
            dirList.append(os.path.join(root, dir))
        for file in files:
            # print(os.path.join(root, file))
            fileList.append(os.path.join(root, file))
    print(fileList)
    for w in fileList:
        ext = os.path.splitext(w)
        print(ext)
        if ext[1] == '.wav':
            if '打不开' in ext[0]:
                pass
            else:
                countWav += 1
        else:
            try:
                d = open(w,'r',encoding='utf-16')
                data = d.read()
                data.replace(' ','').replace('\n','')
                res = re.findall('text = "(.+?)"',data)
                countTg += len(res)
                # print(res)
                d.close()
            except:
                d = open(w,'r',encoding='utf-8')
                data = d.read()
                data.replace(' ','').replace('\n','')
                res = re.findall('text = "(.+?)"',data)
                countTg += len(res)
                # print(res)
                d.close()
    print(countWav,countTg)
    return countWav,countTg
if __name__ == '__main__':
    Main()
