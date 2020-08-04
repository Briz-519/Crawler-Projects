# -*- coding : utf-8 -*-
# @Time : 7/16/2020 15:16
# @Author : Briz
# @File : testSqlite.py
# @Software: PyCharm


import sqlite3

# conn=sqlite3.connect("test.db")
#
# c=conn.cursor()
#
# sql='''
#     create table company
#         (id int primary key not null ,
#         name text not null ,
#         age int not null,
#         address char(50),
#         salary real
#         );
#
# '''
#
# c.execute(sql)
#
# conn.commit()
#
# conn.close()

#增
# conn=sqlite3.connect("test.db")
#
# c=conn.cursor()
#
# sql1='''
#     insert into company(id,name,age,address,salary)
#     values(1,'Briz',20,"China",8000);
#
# '''
#
# sql2='''
#     insert into company(id,name,age,address,salary)
#     values(2,'briz',20,"China",8000);
#
# '''
#
# c.execute(sql1)
# c.execute(sql2)
# conn.commit()
#
# conn.close()


#查
# conn=sqlite3.connect("test.db")
#
# c=conn.cursor()
#
# sql="select id,name,address,salary from company"
#
# cursor=c.execute(sql)
#
# for row in cursor:
#     print("id=",row[0])
#     print("name=",row[1])
#     print("address=",row[2])
#     print("salary=",row[3])
#
# conn.close()