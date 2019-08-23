# coding=utf-8
import os,time

from xlwt import Workbook

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
            ext = os.path.splitext(excel_path)
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
            pass

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

    def update_cell(self, *args, sheetIndex=0):
        """更新单元格"""
        if not isinstance(self.workbook, xlrd.book.Book):
            raise Exception("更新单元格数据，请使用xlrd。")
        wb = copy(self.workbook)
        ws = wb.get_sheet(sheetIndex)
        for i in args:
            for x,y,data in i:
                ws.write(x,y, data)
        # print(self.excel_path)        ## 这里处理只能保存为xls，xlsx保存打不开
        if os.path.splitext(self.excel_path[1]) != 'xls':
            __saveExcelPath = '{0}.{1}'.format(os.path.splitext(self.excel_path)[0], 'xls')
        else:
            __saveExcelPath = self.excel_path
        wb.save(__saveExcelPath)

    def create_Excel(self,*args,sheetName='Sheet1'):
        # print(self.excel_path)
        '''新建用的方法，路径传入是已经存在的同学去反思
        仅针对传入路径为不存在的，如果已经存在，请反思，没有处理
        '''
        # 嘴上虽然说不传路径不处理，但是还是乖乖的处理了。
        if os.path.exists(self.excel_path) is True:
            raise Exception('有这个文件，呸。')
        _sheet = self.workbook.add_sheet(sheetName)
        ## 写入数据
        for x,y,info in args:
            _sheet.write(x,y,label = info)

        ## 保存
        self.workbook.save(self.excel_path)

try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests
import re
from urllib import parse
##前6页的网址，对比一下
# https://s.taobao.com/search?ie=utf8&initiative_id=staobaoz_20190602&stats_click=search_radio_all%3A1&js=1&imgfile=&q=空气消毒液&suggest=history_1&_input_charset=utf-8&wq=&suggest_query=&source=suggest&bcoffset=6&ntoffset=6&p4ppushleft=2%2C48&s=0
# https://s.taobao.com/search?ie=utf8&initiative_id=staobaoz_20190602&stats_click=search_radio_all%3A1&js=1&imgfile=&q=空气消毒液&suggest=history_1&_input_charset=utf-8&wq=&suggest_query=&source=suggest&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=44
# https://s.taobao.com/search?ie=utf8&initiative_id=staobaoz_20190602&stats_click=search_radio_all%3A1&js=1&imgfile=&q=空气消毒液&suggest=history_1&_input_charset=utf-8&wq=&suggest_query=&source=suggest&bcoffset=0&ntoffset=0&p4ppushleft=1%2C48&s=88
# https://s.taobao.com/search?ie=utf8&initiative_id=staobaoz_20190602&stats_click=search_radio_all%3A1&js=1&imgfile=&q=空气消毒液&suggest=history_1&_input_charset=utf-8&wq=&suggest_query=&source=suggest&bcoffset=-3&ntoffset=-3&p4ppushleft=1%2C48&s=132
# https://s.taobao.com/search?ie=utf8&initiative_id=staobaoz_20190602&stats_click=search_radio_all%3A1&js=1&imgfile=&q=空气消毒液&suggest=history_1&_input_charset=utf-8&wq=&suggest_query=&source=suggest&bcoffset=-6&ntoffset=-6&p4ppushleft=1%2C48&s=176
# https://s.taobao.com/search?ie=utf8&initiative_id=staobaoz_20190602&stats_click=search_radio_all%3A1&js=1&imgfile=&q=空气消毒液&suggest=history_1&_input_charset=utf-8&wq=&suggest_query=&source=suggest&bcoffset=-9&ntoffset=-9&p4ppushleft=1%2C48&s=220

def get_url(__search,get_page_num):
    ## 处理一下url
    ## _search搜索词
    ## _get_page_num获取到第几页的数据
    url_list = []
    bcoffset = [x*-3 for x in range(get_page_num)]
    s = 0
    for i in bcoffset:
        _url = 'https://s.taobao.com/search?ie=utf8&initiative_id=staobaoz_20190602&stats_click=search_radio_all%3A1&js=1&imgfile=&q={0}&suggest=history_1&_input_charset=utf-8&wq=&suggest_query=&source=suggest&bcoffset={1}&ntoffset={2}&p4ppushleft=1%2C48&s={3}'.format(
        __search,i+6,i+6, s)
        s += 44
        url_list.append(_url)

    return url_list

def urlopen(*args,**kwargs):
    # 公共headers
    headers = {
        'path':'/search?q=%E7%A9%BA%E6%B0%94%E6%B6%88%E6%AF%92%E6%B6%B2&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306',
        'referer':'https://www.taobao.com/',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'scheme':'https',
        'cookie':'cna=wskKE7l12g0CAWoIMpIRA8Tw; miid=8467352501835762891; tg=0; thw=cn; t=c732a82708bea23f6e785bf1d3d48c0b; _cc_=URm48syIZQ%3D%3D; enc=QEdcEV5myLTLQk3M6trY0RgTccCzhneu7PMikUbGFS0d%2FCptcAS6n52odZRI2wOGsT4SVu7X9BnQYF0z05gVCA%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; cookie2=523ec5f65b836181c8f51c2fdd893ac4; _tb_token_=f3357e56ab1e5; mt=ci=0_0; v=0; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; JSESSIONID=E3E88107A80F36891B079CCBB0061EED; l=bBLYGXanvdl0Fg6yBOfgmuI8aZ7tzIdfGiNzw4_GAICP_H1Hd2CFWZTDC6YMC3GVa6nw83oyuHLQBJ8iUy4Ed; isg=BNzcaabu7ByY65hBFTmup6rArfpO_YARWS1fmbbcMEf-AXiL3WZxDiLzZSlc47jX',
        'cache-control':'max-age=0',
        'accept-language':'zh-CN,zh;q=0.9',
        'accept-encoding':'gzip, deflate, br'
    }

    try:
        url_list = get_url(*args,**kwargs)
    except Exception as e:
        print('获取url列表出错：%s'% e)

    ## 得到url列表之后循环请求，得到数据处理
    print('开始请求淘宝网址'.center(50,'-'))
    for j in url_list:
        req = requests.get(j,headers=headers)
        # print(req.text)
        to_file(req.text)

def __get_data(text):
    ## 处理请求得到的数据
    ##乍一看有点乱，意思就是先找到所有的当前页的数据，再把红色字体的css代码替换掉，再重新用utf-8编码，最后再找一次得到单个商品的所有信息。
    data = re.findall('"pid":"",(.+?)"encryptedUserId"',re.findall('auctions":(.+),"recommendAuctions"',text)[0].replace('\\u003cspan class\\u003dH\\u003e','').replace('/span','').replace(r'\u003c\u003e',''))
    ###"title":"滴露消毒液家用杀菌儿童衣物家居除菌液非84消毒水1.15L*2瓶","raw_title":"滴露消毒液家用衣物宠物地板除菌液洗衣杀菌","pic_url":"//g-search1.alicdn.com/img/bao/uploaded/i4/imgextra/i3/110197389/O1CN01h829Zs24SD3z7SJFM_!!0-saturn_solar.jpg","detail_url":"https://click.simba.taobao.com/cc_im?p\u003d%CF%FB%B6%BE%D2%BA\u0026s\u003d147198501\u0026k\u003d633\u0026e\u003d1hx2k2imvWlVl1JuKnszQFgcO%2BnFKa408SbRsQkAD3AtVIBiPVaAj%2FtC%2FuQKdj99ZpblSwL%2FuN3fiTbVWxJA1QREUzc%2BIlr9CV15MqqSHB7ivHq5ZUeZmrbrzgc3LwxcIcVTVUhdvp0WM3rZj00tn3sAofq2F9BG8fzh0xgdZwl4F0ljYcnhTDFpEV%2BKgANeuLJYNZhzsUcVg4N8eJM7q5zaP5Af2qvF0L1a44kh9pfHEyEpWzu1v432W67w0NX1r1cWS8oilN%2BY9D3Bny3sRjPLdeNnPpws0xvg1XZ6K83Xau5AmN5Gul8R01Cd7DH6IvjiWFu6wr877zyWUUHnEoCZU6ANPtUlfpEOklufgvh59GE2GCT0UpXJG4ASPoVrsN5O0%2BKGJj3k3NohA6TfzsgsEUtzugN0KYD%2FXHFwKxGrSmakTqRb%2BaEpY7O7591YcFDFMoHcocCD8kH8%2BkhwU9JAlaSE%2BH%2FpjxWoRv06JDzvy9urLhZUhoU9MUaz2DaDTsDIvgP%2B74lhVpgcvhyS%2BVVtkIg5KsKccZ9XbEhjsm5o5ocGv2%2FYkkA4xCnuYUdDMlXqrBKZR6pqwjAkiA5rovT4%2BZ%2BM6jVkwX4Elfo7z%2Fl8Sni9v%2Bf8Ig%3D%3D","view_price":"119.90","view_fee":"0.00","item_loc":"上海","view_sales":"1.5万+人付款","comment_count":"","user_id":"2405035918","nick":"dettol滴露官方旗舰店","shopcard":{"levelClasses":[],"isTmall":true,"delivery":[0,1,4004],"description":[0,1,5068],"service":[0,1,4449]
    all_item = []
    __temp_item = {}
    for item in data:
        #print(item)
        __temp_item['title'] = re.findall(':"(.+?)","raw_title"',item)[0]
        __temp_item['raw_title'] = re.findall('"raw_title":"(.+?)","pic_url"',item)[0]
        __temp_item['item_loc'] = re.findall('"item_loc":"(.+?)","view_sales"',item)[0]
        __temp_item['view_sales'] = re.findall('"view_sales":"(.+?)","comment_count"',item)[0]
        __temp_item['nick'] = re.findall('"nick":"(.+?)","shopcard"',item)[0]
        __temp_item['delivery'] = re.findall('"delivery":(.+?),"description"',item)[0]
        __temp_item['view_price'] = re.findall('"view_price":"(.+?)","view_fee"',item)[0]
        __temp_item['view_fee'] = re.findall('"view_fee":"(.+?)","item_loc"',item)[0]
        __temp_item['detail_url'] =  __get_real_url(re.findall('"detail_url":"(.+?)","view_price"',item)[0].replace('\\u003d','=').replace('\\u0026','&'))
        ##print(__temp_item)
        try:

            ## 收集收藏数以及评论数,收藏数暂时拿不到了，先获取月销量跟评价数
            try:
                detail = __get_detail_item_info(__temp_item['title'])
                __temp_item['shoucang'] = detail[0]
                __temp_item['pingjia'] = detail[1]
            except Exception as e:
                print('获取月销量与收藏数失败，错误信息为%s'%e)
            all_item.append(__temp_item.copy())
            # print(__temp_item)
        except Exception as e:
            print('获取收藏数以及评价失败，商品名：%s\n错误：%s'%(__temp_item['title'],e))

        ## 显示在cmd中
        print('-' * 60)
        print('商品名称:{0}'.format(__temp_item.get('title')))
        print('归属地:{0}'.format(__temp_item.get('item_loc')))
        print('已付款:{0}'.format(__temp_item.get('view_sales')))
        print('店铺名称:{0}'.format(__temp_item.get('nick')))
        print('售价:{0}'.format(__temp_item.get('view_price')))
        print('优惠价格:{0}'.format(__temp_item.get('view_fee')))
        print('月销量:{0}'.format(__temp_item.get('shoucang')))
        print('评价数:{0}'.format(__temp_item.get('pingjia')))
        print('详情地址:{0}'.format(__temp_item.get('detail_url')))

    return all_item


def to_file(*args):
    ##  获取数据
    try:
        print('正在处理数据...')
        _ = __get_data(*args)
    except:
        print('__get_data报错，获取数据失败')
        return
    print('正在写入excel'.center(50,'-'))
    __excel_writer(_)
    print('写入excel成功......')
    ## 处理数据，输出到excel中

def __get_detail_item_info(*args):
    ## 这里评价数与月销量数从天猫获取
    _url = 'https://list.tmall.com/search_product.htm?q={0}&type=p&spm=a220o.0.a2227oh.d100&from=.detail.pc_1_searchbutton'.format(*args)
    ## 获取收藏数，以及评价数
    req = requests.get(_url)
    # print(req.text)
    ################################
    ##没法获取到天猫详情页的收藏数，他是动态数据，留个陨石坑，相信会有解决办法的

    ## 获取月成交数量
    yuexiao = re.findall('<span>月成交 <em>(.+?)笔</em></span>',req.text)[0]
    pingjia = re.findall('data-p="1-1">(.+?)</a></span>',req.text)[0]

    return [yuexiao,pingjia]

def __get_real_url(detail_url):
    ## 处理url，天猫的加上域名，淘宝的不改动
    if detail_url == '' or detail_url is None:
        print('url是错误的，不能为空')
        raise Exception
    if 'http' not in detail_url:
        detail_url = '{0}{1}'.format('https:',detail_url)

    return detail_url

def __excel_writer(data):
    ## 写入excel文件
    excel_path = os.path.join(os.getcwd(), '{0}.xls'.format(time.strftime('%Y-%m-%d',time.localtime())))
    excel = ExcelUntil(excel_path)
    ## 如果有文件则直接打开，没有则新建一个
    if not os.path.exists(excel_path):
        excel.create_Excel((0, 0, 'title'), (0, 1, 'raw_title'), (0, 2, 'item_loc'), (0, 3, 'view_sales'), (0, 4, 'nick'), (0, 5, 'delivery'),(0, 6, 'view_price'), (0, 7, 'view_fee'), (0, 8, 'detail_url'),(0,9,'shoucang'),(0,10,'pingjia'))

    excel = ExcelUntil(excel_path)

    ## 这里开始更新数据

    x = len(excel.read_row())
    y = 0
    __param = []
    ## 循环一下次数，以便定位x的数字
        ##循环一下数据集中的单个数据，顺便定位y的数字
    for detail in data:
        for value in detail.values():
            __param.append((x,y,value))
            y += 1
        excel.update_cell(__param)
        excel = ExcelUntil(excel_path)
        __param = []
        x += 1
        y = 0

## 定时任务
from apscheduler.schedulers.background import BackgroundScheduler
__run_timing  = input('定时任务执行间隔（分钟）：')
search = input('请输入要查询的词：')
get_page_num = input('统计前多少页的数据：')

def apscheduler(func):
    ## 定时器,装饰器
    def wrapper(*args,**kwargs):
        background = BackgroundScheduler()
        background.add_job(func,'interval',args=args,kwargs=kwargs,seconds=int(__run_timing)*60)
        background.start()
        try:
            while 1:
                start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                print('当前时间：{0}'.format(start_time))
                time.sleep(300)
        except:
            print('定时器已停止'.center(50,'*'))
            background.shutdown()
    return wrapper

@apscheduler
def main():
    print(search,get_page_num)
    urlopen(search,int(get_page_num))
main()
input('按任意键退出!!!')
