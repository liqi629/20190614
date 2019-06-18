# -*- coding: utf-8 -*-
# @Time     : 2019/5/29 14:13
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : do_mysql.py
# @Software : PyCharm
import pymysql
from Common import dir_config
from Common.readconfig import ReadConfig
class DoMysql:
    def __init__(self):
        self.config = ReadConfig().read_config(dir_config.db_config_path, "DB", "config")
        self.db = pymysql.connect(**self.config)
    #查询功能
    def do_mysql(self,sql):
        # db = pymysql.connect(**self.config)
        # 1：根据登录信息  去登录数据库 产生一个数据库连接
        # 2：产生一个游标  可以获取数据库操作权限
        cursor = self.db.cursor()
        # 3:利用游标 进行操作
        cursor.execute(sql)  # 执行sql
        # 获取结果：1）获取单条   2）获取多条
        # res=cursor.fetchone() #单  返回的是一个元组
        res = cursor.fetchall()  # 多  返回的是一个嵌套元组的列表
        # 关掉游标 关掉连接
        cursor.close()
        self.db.close()
        return res
    #删除数据表的内容
    def deletc_data(self,sql):
        cursor = self.db.cursor()
        cursor.execute(sql)
        #commit()方法：在数据库里增、删、改的时候，必须要进行提交，否则插入的数据不生效。
        self.db.commit()
        cursor.close()
        self.db.close()
if __name__ == '__main__':
    sql = 'select * from AUTO_test_02'  # sql语句
    res = DoMysql().do_mysql(sql)
    print("数据库的查询结果是：{0}".format(res))
    # sql2 = 'DELETE FROM AUTO_test_02'
    # DoMysql().deletc_data(sql2)
    # print(DoMysql().select_table_1('select * from AUTO_test_02'))