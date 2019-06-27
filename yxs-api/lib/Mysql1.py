# coding=utf-8
import pymysql,os
from lib.getConfig import getConfig

sql_config = getConfig(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'config/MysqlInfo.json'))

class Mysql:
    '''数据库连接工具'''
    def __init__(self,sql_config):
        try:
            self.conn = Mysql.__connect(sql_config['host'],sql_config['user'],sql_config['passwd'],sql_config['db'],sql_config['port'])
        except:
            print("请检查你的配置参数格式是否正确")

    @staticmethod
    def __connect(host,user,passwd,db,port):

        try:
            conn = pymysql.connect(host=host,user=user,passwd=passwd,db=db,port=port)
            return conn

        except:
            print("连接失败，请检查配置参数")
            raise

    def excute(self,sql):
        ## 执行sql语句
        try:
            cursor = self.conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql)
        except Exception as e:
            print("执行出错：%s"%e)
            self.conn.rollback()

        self.conn.commit()
        cursor.close()
        return cursor

    def get_row(self,sql):
        ## 获取一行数据
        try:
            cur = self.excute(sql)
            row = cur.fetchone()
            return row
        except Exception as e:
            print("查询单行数据出错：%s"%s)
            raise

    def get_rows(self,sql):
        ## 获取多行数据
        try:
            cur = self.excute(sql)
            rows = cur.fetchall()
            return rows
        except Exception as e:
            print("查询多行数据出错：%s" % s)
            raise

    def get_table(self):
        ## 获取数据列表名称
        tables = []
        try:
            __tables_list = self.get_rows("select table_name from information_schema.tables where table_schema='%s'"%sql_config["db"])
            for i in __tables_list:
                tables.append(i["table_name"])
            return tables
        except Exception as e:
            print("查询列表名称出错：%s"%e)
            raise

    def get_key_name(self,sql):
        ## 获取所查询的表的key

        row = self.get_row(sql)
        try:
            key_name_list = [i for i in row.keys()]
            return key_name_list
        except Exception as e:
            print("生成列表名称错误：%s"%e)

    def close(self):
        try:
            self.conn.close()
        except Exception as e:
            print("关闭连接失败")

if __name__ == '__main__':
    s = Mysql(sql_config)
    s.get_key_name("select * from tbl_book_type ")
    print(s.get_row("select * from tbl_book_type "))
    s.close()

