# coding=utf-8
import os
try:
    import xlrd
except ImportError:
    os.system('pip install xlrd')
    import xlrd
try:
    import xlwt
except ImportError:
    os.system("pip install xlwt")
    import xlwt
try:
    from xlutils.copy import copy
except ImportError:
    os.system('pip install xlutils')
    from xlutils.copy import copy
class ExcelUntil:
    """
    读取支持xlsx，xls。写入更新支持xls
    """

    def __init__(self, excel_path):
        """
        传入地址规则，不输入绝对路径，默认相对路径查找
        传入文件名尽量加上后缀
        传入不存在的文件名，则新建excel
        xlwt.Workbook.Workbook,xlrd.book.Book
        :param excel_path:
        :return:
        """
        __excel_path = os.path.basename(excel_path)  ## 传入的文件名
        __excel_path_list = os.listdir(os.path.dirname(excel_path))  ## 文件所在的列表
        __has_excel = False  ## 找到传入的文件的标识参数
        for i in __excel_path_list:
            ## 如果找到，则更改标识
            if __excel_path in i:
                __has_excel = True
                self.workbook = xlrd.open_workbook(os.path.join(os.path.dirname(excel_path), i))
                self.excel_path = os.path.join(os.path.dirname(excel_path), i)
                break
        ## 没找到excel
        if not __has_excel:
            ## 分一下文件名
            ext = os.path.splitext(excel_path)
            ## 没有后缀的话，
            if ext[1] == "":
                self.excel_path = excel_path + ".xlsx"
            else:
                self.excel_path = excel_path
            self.workbook = xlwt.Workbook(excel_path)
            print("未找到文件名，认为新建excel")

    def _checkout_sheet(self, sheetIndex, sheetName):
        """默认是第一个sheet,内部方法，获取sheet用
            读取专用切换
        """
        if isinstance(self.workbook, xlrd.book.Book):
            if sheetName is not None:
                try:
                    ## sheet变量
                    self.sheet = self.workbook.sheet_by_name(sheetName)
                    print('sheet切换成功，当前在：%s' % sheetName)
                except Exception:
                    print('sheet名称不正确/不存在,\n所有sheet共计%s个，有%s\n' % (
                        len(self.workbook.sheet_names()), self.workbook.sheet_names()))
                    self.sheet = self.workbook.sheet_by_index(0)
                    print('已切换到%s' % self.workbook.sheet_names()[0])
            else:
                try:
                    self.sheet = self.workbook.sheet_by_index(sheetIndex)

                    print('sheet切换成功，当前在：第%s个。名称：%s' % (sheetIndex + 1, self.workbook.sheet_names()[sheetIndex]))
                except Exception:
                    print('sheet索引错误，请输入正确索引。\n所有sheet共计%s个，有%s' % (
                        len(self.workbook.sheet_names()), self.workbook.sheet_names()))
                    self.sheet = self.workbook.sheet_by_index(0)

                    print('已切换到%s' % self.workbook.sheet_names()[0])
        elif isinstance(self.workbook, xlwt.Workbook):
            raise Exception(f'写入使用切换sheet方法失败,{self._checkout_sheet.__name__}')

    def read_row(self, row=None, skip=0, sheetIndex=0, sheetName=None):
        """
        读取excel数据
        :param row: 要读取的行数
        :param skip:要跳过的行数
        :param sheetIndex:第几个sheet的索引
        :param sheetName:sheet名称
        :return:dict
        """
        if not isinstance(self.workbook, xlrd.book.Book):
            raise Exception("老实的去新建，不要乱来读取")
        self._checkout_sheet(sheetIndex, sheetName)
        nrows = self.sheet.nrows
        ncols = self.sheet.ncols
        print('共计(%s行,%s列)' % (nrows, ncols))
        if row is None:
            row = nrows
        if skip >= row:
            print('跳过的比要得到的都多了')
            return {}
        if row > nrows:
            print('要得到rows比总共的rows都多了，变为总共的rows')
            row = nrows

        rows_dict = {}
        for i in range(row):
            if i + 1 <= skip:
                continue
            rows_dict['row{0}'.format(i + 1)] = self.sheet.row_values(i)
        # print(rows_dict)
        return rows_dict

    def read_col(self, col=None, skip=0, sheetIndex=0, sheetName=None):
        """
        读取excel数据
        :param col: 要读取的列数
        :param skip:要跳过的列数
        :param sheetIndex:第几个sheet的索引
        :param sheetName:sheet名称
        :return:dict
        """
        if not isinstance(self.workbook, xlrd.book.Book):
            raise Exception("老实的去新建，不要乱来读取")
        self._checkout_sheet(sheetIndex, sheetName)
        nrows = self.sheet.nrows
        ncols = self.sheet.ncols
        # print('共计(%s行,%s列)' % (nrows, ncols))
        if col is None:
            col = ncols
        if skip >= col:
            print('跳过的比要得到的都多了')
            return {}
        if col > ncols:
            print('要得到rows比总共的rows都多了，变为总共的rows')
            col = ncols

        cols_dict = {}
        for i in range(col):
            if i + 1 <= skip:
                continue
            cols_dict['col{0}'.format(i + 1)] = self.sheet.col_values(i)
        # print(cols_dict)
        return cols_dict

    def update_cell(self,x,y,msg,sheetIndex=0):
        """更新单元格"""
        if not isinstance(self.workbook, xlrd.book.Book):
            raise Exception("更新单元格数据，请使用xlrd。")
        wb = copy(self.workbook)
        ws = wb.get_sheet(sheetIndex)
        # for x,y,msg in args:
        #     print(x,y,msg)
        #     ws.write(int(x),int(y),msg)
        ws.write(int(x),int(y),msg)
        ## 这里处理只能保存为xls，xlsx保存打不开
        if os.path.splitext(self.excel_path[1]) != 'xls':
            __saveExcelPath = '{0}.{1}'.format(os.path.splitext(self.excel_path)[0],'xls')
        else:
            __saveExcelPath = self.excel_path
        wb.save(__saveExcelPath)

    def create_Excel(self,*args,sheetName='Sheet1'):
        # print(self.excel_path)
        '''新建用的方法，路径传入是已经存在的同学去反思
        仅针对传入路径为不存在的，如果已经存在，请反思，没有处理
        '''
        # 嘴上虽然说不传路径不处理，但是还是乖乖的处理了，真香。。。
        if os.path.exists(self.excel_path):
            raise Exception('有这个文件，呸。')
        _sheet = self.workbook.add_sheet(sheetName)
        ## 写入数据
        for x,y,info in args:
            _sheet.write(x,y,label = info)
        self.workbook.save(self.excel_path)

if __name__ =='__main__':
    # p = r'/Users/dangfuli/Documents/log/p.xls'
    #log_tmp = ExcelUntil(os.path.join(os.getcwd(),'taobao.xls'))
    # log_tmp.create_Excel((0,0,'1'),(0,1,'2'),(0,2,'3'))
    # print("123")
    # t_read = log_tmp.read_row(row=1)
    # t_read1 = log_tmp.read_row(sheetIndex=1)
    # t1_read = log_tmp.read_row(sheetIndex=10)
    # t3_read = log_tmp.read_row(sheetName='123')
    # t4_read = log_tmp.read_row(sheetName='Sheet2')
    # cr = log_tmp.read_col(col=2,sheetIndex=1)
    # log_tmp.create_Excel()

    pa = r'/Users/dangfuli/Documents/log/p.xls'
    t = ExcelUntil(pa)
    t.update_cell(1,2,'a')
