# codinig=utf-8
import os,easygui
import json
from request_case import PostJira
class ManageTxt:
    def __init__(self,filepath):
        self.filepath = filepath

    def txt(self):
        txt_path = self.filepath + r'\temp'
        all_file = os.listdir(txt_path)
        os.chdir(txt_path)
        txt_list = []
        run_list = []
        for j in all_file:
            ext = os.path.splitext(j)
            if ext[1] == '.txt':
                txt_list.append(j)
        count = 1
        for i in txt_list:
            d = ManageTxt(txt_path).HandleTxt(i)
            jira = PostJira.RequestJira().serch(plate=d[0])

            if jira != []:
                os.remove(i)

                continue

            if '续保失败' in str(d[1]):
                os.remove(i)
                continue

            # e = easygui.textbox(msg='(%s/%s)车牌[%s]\n\n类型为：%s\n\n%s秒' % (count,len(txt_list),d[0],d[1],d[2]),text=d[3])
            sum = '第（%s）个车牌：%s' %  (count,d[0])
            e = easygui.textbox(msg = sum + '\n\n' + str(d[1]) + '\n\n' + '耗时%s' % d[2], title = '车辆结果', text = d[3])
            count += 1
            run_list.append(i)
            if e == None:
                break

        d_txt = easygui.boolbox(msg='是否删除所有数据？',choices=['删除','取消'])
        if d_txt == True:
            ManageTxt(txt_path).del_txt(txt_path,run_list)
        else:
            pass
    def HandleTxt(self,file):
        fp = open(file)
        plate = fp.readline()
        content = fp.readline()
        xb_time = fp.readline()
        json = fp.read()
        fp.close()
        return plate,content,xb_time,json

    def del_txt(self,dfile,run):
        try:
            os.chdir(dfile)
            for i in run:
                print(i)
                os.remove(i)
            if len(run) == 0:
                # 数据清除完毕
                pass
        except Exception as err:
            print('报错啦......报错内容为：%s' % err)

if __name__=='__main__':
    filepath = r'C:\Users\Administrator\Desktop'
    ManageTxt(filepath).txt()