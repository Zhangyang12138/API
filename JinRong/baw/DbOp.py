'''
跟业务相关的数据库的操作
'''
from JinRong.caw.Mysql import Mysql


class DbOp:
    def delete_user(self,db1,mobilephone):
        mysql = Mysql()
        conn = mysql.connect(db1)
        # print(conn)
        mysql.delete(conn, f"delete from member where mobilephone={mobilephone};")
        mysql.disconnect(conn)
