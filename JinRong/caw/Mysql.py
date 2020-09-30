'''
数据库的操作
'''
import pymysql


class Mysql:
    #连接
    def connect(self,db1):
        ip=db1['ip']
        port=int(db1['port'])
        name=db1['name']
        user=db1['user']
        pwd=db1['pwd']
        try:
            conn=pymysql.connect(host=ip,port=port,user=user,password=pwd,charset='utf8',database=name)
            print(f"连接数据库{ip},{port}成功")
            return conn
        except Exception as e:
            print(f"连接数据库异常，异常信息为：{e}")

    #删除
    def delete(self,conn,sql):
        try:
            cursor=conn.cursor()#获取游标
            cursor.execute(sql)#使用游标执行sql
            conn.commit()#
            cursor.close()#释放游标
            print(f"执行sql语句{sql}")
        except Exception as e:
            print(f"执行sql语句异常，异常信息为{e}")

    #断开
    def disconnect(self,conn):
        try:
            conn.close()
        except Exception as e:
            print(f"断开数据库异常，异常信息为：{e}")



if __name__=='__main__':
    db1={"ip":"192.168.150.52","port":"3306","name":"apple","user":"root","pwd":"123456"}
    mysql=Mysql()
    conn=mysql.connect(db1)
    # print(conn)
    mysql.delete(conn,"delete from member where mobilephone=15510086369;")
    mysql.disconnect(conn)


