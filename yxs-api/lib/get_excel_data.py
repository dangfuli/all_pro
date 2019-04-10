# coding=utf-8
# 检验如果没有找到xlrd包，pip下载
import os
import time
try:
    import xlrd
except ImportError:
    os.system('pip install xlrd')
    time.sleep(5)
    import xlrd
xlrd.Book.encoding = "gbk"
class ExcelUntil:
    def __init__(self,excel_path = r'C:\Users\Administrator\Desktop\新建 Microsoft Excel 工作表.xlsx'):
        try:
            epath = input('请输入excel路径(可以将文件拖入控制台中，注意文件名字中不要有空格\n输入回车默认桌面位置默认文件名）：')
            if epath == '':
                self.data = xlrd.open_workbook(excel_path)
            else:
                self.data = xlrd.open_workbook(epath)
        except Exception as e:
            # log.debug('打开excel失败')
            print('打开excel失败：%s' % e)

        else:
            # log.debug('excel打开成功'.center(40).replace(' ','-'))
            print('excel打开成功'.center(40).replace(' ','-'))
        try:

            self.table = self.data.sheet_by_index(0)
            # 获取总行数
            self.ncols = self.table.ncols
            # 获取总列数
            self.ncows = self.table.nrows
        except Exception as e:
            # log.debug('读取excel数据失败')
            print('读取excel数据失败%s' % e)

    def get_excel(self):
        excel_data = self.table.col_values(0)
        # print(excel_data)
        # 去空
        while '' in excel_data:
            excel_data.remove('')
        # print(excel_data)

        # 删车牌空格
        count_list = 0
        for q in excel_data:
            if ' ' in q:
                result = q.replace(' ','').replace('\n','')
                excel_data[count_list] = result
            # 判断两个车牌是否重复
            if count_list >= 1:
                if excel_data[count_list] == excel_data[count_list-1]:
                    excel_data.remove(q)
            count_list += 1

        print(excel_data)

        # 删除长度大于8的车牌
        for w in excel_data:
            if len(w) >= 8:
                excel_data.remove(w)

        # print(excel_data)
        # log.info('excel数据收集成功')
        return excel_data
if __name__=='__main__':
    # excel_path = r'C:\Users\Administrator\Desktop\新建 Microsoft Excel 工作表.xlsx'
    ExcelUntil().get_excel()


