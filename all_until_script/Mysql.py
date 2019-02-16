# coding=utf-8
import os

import pymysql

configs = {
    "host":"10.96.88.151",
    "user":"soda_test",
    "passwd":"soda8888",
    "db":"soda_d_delivery",
    "port":3306
}
class Mysql:
    '''
    传入配置信息格式
    host，user，passwd，db
    '''
    def __init__(self,configs):
        try:
            self.configs = dict(configs)
        except Exception as e:
            print("please checkout configs data ")
        values = list(self.configs.values())
        self.conn = Mysql.__connect(values[0],values[1],values[2],values[3],values[4])
    ## 静态方法，连接数据库
    @staticmethod
    def __connect(host,user,passwd,db,port=3306):
        '''
        连接数据库用
        :param db_info:数据库信息
        :return:
        '''
        try:
            con = pymysql.connect(host=host,port=port,user=user,passwd=passwd,db=db)
            return con
        except Exception as e:
            print("connect db faild,error:%s" %e)

    def execute(self,sql):
        '''
        执行sql
        :param sql:sql语句，字符串
        :return:游标
        '''
        try:
            cur = self.conn.cursor(pymysql.cursors.DictCursor)   ##创建游标，指定dict返回
            cur.execute(sql)
        except Exception as e:
            print("execute sql faild:%s"%e)
        else:
            self.conn.commit()
            cur.close()
            return cur
    def getrows(self,sql,all=False):
        '''
        返回执行结果
        :param sql:sql语句，字符串
        :param all：ture为返回fetchall（），false返回fetchone（）
        :return:
        '''
        try:
            cur = self.conn.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
        except Exception as e:
            print("execute sql faild:%s"%e)
        else:
            if all == True:
                rows = cur.fetchall()
                return rows
            elif all == False:
                rows = cur.fetchone()
                cur.close()
            #print(rows)
                return rows
    def get_rowname(self,sql):
        '''
        返回表列名，return list
        :param sql:sql语句，字符串格式
        :return:list
        '''
        rows = self.execute(sql)
        rowlist = []
        if rows != None:
            for row in rows:
                for i in row:
                    try:
                        rowlist.index(i)
                    except:
                        rowlist.append(i)
                    else:
                        pass
#        print rowlist
        return rowlist

    def get_table(self):
        '''
        返回数据库中其他表dict
        :return:
        '''
        table_list = []
        all = Mysql(self.configs).getrows("select table_name from information_schema.tables where table_schema='%s'" % list(self.configs.values())[3])
        for i in all:
            table_list.append(i)
        return table_list

    def db_close(self):
        '''
        关闭数据库
        :return:
        '''
        try:
            self.conn.close()
        except Exception as e:
            print("closed db faild:%s" % e)

if __name__ == '__main__':
    m = Mysql(configs)
    #m.getrows("select * from d_delivery_47 where status='110'")
    #m.get_rowname(`)
    print(m.get_table())
    m.db_close()
